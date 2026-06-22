"""BYO-8 starter — the transformer forward pass from scratch (NumPy only). See README.md.

This builds the architecture behind GPT: positional encoding, scaled dot-product attention with a
causal mask, multi-head attention, LayerNorm, and a pre-norm transformer block with residuals
(exam Q46 positional encoding, Q47 residual connections). Forward only — training is the stretch.

Convention: a single sequence X has shape (T, d_model); weight matrices are (d_model, d_model).
"""
import numpy as np


def relu(x):
    raise NotImplementedError("implement relu")


def softmax(x, axis=-1):
    """Numerically stable softmax along `axis` (subtract the max first)."""
    raise NotImplementedError("implement softmax")


def positional_encoding(T, d):
    """Sinusoidal positional encoding, shape (T, d):
        PE[pos, 2i]   = sin(pos / 10000^(2i/d))
        PE[pos, 2i+1] = cos(pos / 10000^(2i/d))
    """
    raise NotImplementedError("implement positional_encoding")


def causal_mask(T):
    """(T, T) boolean lower-triangular mask. True where attention is allowed (j <= i)."""
    raise NotImplementedError("implement causal_mask")


def scaled_dot_product_attention(Q, K, V, mask=None):
    """Q,K,V shaped (..., T, dk). Return (out, attn).
        scores = Q @ K^T / sqrt(dk)
        if mask is not None: set disallowed positions to a very negative number before softmax
        attn   = softmax(scores, axis=-1)         # rows sum to 1
        out    = attn @ V
    """
    raise NotImplementedError("implement scaled_dot_product_attention")


def layer_norm(x, gamma, beta, eps=1e-5):
    """Normalize over the last axis, then scale/shift: (x-mean)/sqrt(var+eps) * gamma + beta."""
    raise NotImplementedError("implement layer_norm")


def multi_head_attention(X, Wq, Wk, Wv, Wo, n_heads, mask=None):
    """X is (T, d_model). Project to Q/K/V, split into n_heads of size d_model//n_heads, run
    scaled_dot_product_attention per head, concat the heads, then apply the output projection Wo.
    Return (T, d_model)."""
    raise NotImplementedError("implement multi_head_attention")


def transformer_block(X, p, n_heads, mask=None):
    """Pre-norm block with residual connections (`p` is a dict of weights):
        a = X + MHA(LayerNorm(X, ln1_g, ln1_b), Wq, Wk, Wv, Wo)
        m = relu(LayerNorm(a, ln2_g, ln2_b) @ W1 + b1) @ W2 + b2
        return a + m
    Expected keys in p: ln1_g, ln1_b, ln2_g, ln2_b, Wq, Wk, Wv, Wo, W1, b1, W2, b2.
    """
    raise NotImplementedError("implement transformer_block")
