"""Staged acceptance tests for BYO-8 (transformer forward pass)."""
import numpy as np
from minigpt.model import (
    relu, softmax, positional_encoding, causal_mask,
    scaled_dot_product_attention, layer_norm, multi_head_attention, transformer_block,
)


# ----- Stage 1: primitives -----
def test_stage1_softmax():
    s = softmax(np.array([[1.0, 2.0, 3.0], [1.0, 1.0, 1.0]]), axis=-1)
    assert np.allclose(s.sum(axis=-1), 1.0)
    assert np.all(s > 0)
    # stable for large inputs
    assert np.allclose(softmax(np.array([1000.0, 1001.0])).sum(), 1.0)


def test_stage1_positional_encoding():
    pe = positional_encoding(10, 16)
    assert pe.shape == (10, 16)
    assert pe.max() <= 1.0 + 1e-9 and pe.min() >= -1.0 - 1e-9


def test_stage1_causal_mask():
    m = causal_mask(3)
    assert m.shape == (3, 3)
    assert np.array_equal(m, np.array([[1, 0, 0], [1, 1, 0], [1, 1, 1]], dtype=bool))


# ----- Stage 2: attention -----
def test_stage2_attention_weights_and_causality():
    rng = np.random.default_rng(0)
    T, dk = 4, 8
    Q, K, V = (rng.normal(size=(T, dk)) for _ in range(3))
    out, attn = scaled_dot_product_attention(Q, K, V, causal_mask(T))
    assert out.shape == (T, dk)
    assert np.allclose(attn.sum(axis=-1), 1.0)
    for i in range(T):
        for j in range(T):
            if j > i:
                assert attn[i, j] < 1e-6        # no attending to the future


def test_stage2_layer_norm():
    rng = np.random.default_rng(1)
    x = rng.normal(size=(5, 16)) * 3 + 2
    y = layer_norm(x, np.ones(16), np.zeros(16))
    assert np.allclose(y.mean(axis=-1), 0.0, atol=1e-6)
    assert np.allclose(y.std(axis=-1), 1.0, atol=1e-3)


def test_stage2_multi_head_attention_shape():
    rng = np.random.default_rng(2)
    T, d = 6, 16
    X = rng.normal(size=(T, d))
    Wq, Wk, Wv, Wo = (rng.normal(size=(d, d)) * 0.1 for _ in range(4))
    out = multi_head_attention(X, Wq, Wk, Wv, Wo, n_heads=4, mask=causal_mask(T))
    assert out.shape == (T, d)


# ----- Stage 3: the block -----
def test_stage3_transformer_block():
    rng = np.random.default_rng(3)
    T, d, hid = 5, 16, 32
    X = rng.normal(size=(T, d))
    p = dict(
        ln1_g=np.ones(d), ln1_b=np.zeros(d), ln2_g=np.ones(d), ln2_b=np.zeros(d),
        Wq=rng.normal(size=(d, d)) * 0.1, Wk=rng.normal(size=(d, d)) * 0.1,
        Wv=rng.normal(size=(d, d)) * 0.1, Wo=rng.normal(size=(d, d)) * 0.1,
        W1=rng.normal(size=(d, hid)) * 0.1, b1=np.zeros(hid),
        W2=rng.normal(size=(hid, d)) * 0.1, b2=np.zeros(d),
    )
    out = transformer_block(X, p, n_heads=4, mask=causal_mask(T))
    assert out.shape == (T, d)
    assert not np.allclose(out, X)      # the block actually transforms its input
