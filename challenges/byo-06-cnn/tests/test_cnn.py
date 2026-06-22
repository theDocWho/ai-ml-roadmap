"""Staged acceptance tests for BYO-6."""
import numpy as np
from cnn.engine import conv2d_forward, conv2d_backward, max_pool2d, relu


# ----- Stage 1 -----
def test_stage1_conv_forward_known_values():
    X = np.arange(9, dtype=float).reshape(1, 1, 3, 3)
    W = np.ones((1, 1, 2, 2))
    b = np.zeros(1)
    out = conv2d_forward(X, W, b)
    assert out.shape == (1, 1, 2, 2)
    # each output = sum of a 2x2 window: [[0+1+3+4, 1+2+4+5], [3+4+6+7, 4+5+7+8]]
    assert np.allclose(out[0, 0], [[8, 12], [20, 24]])


def test_stage1_conv_forward_bias_and_channels():
    X = np.ones((2, 3, 5, 5))
    W = np.ones((4, 3, 3, 3))
    b = np.arange(4, dtype=float)
    out = conv2d_forward(X, W, b)
    assert out.shape == (2, 4, 3, 3)
    # every window sums 3*3*3 ones = 27, plus bias
    assert np.allclose(out[0, :, 0, 0], 27 + b)


# ----- Stage 2 -----
def test_stage2_maxpool():
    X = np.arange(1, 17, dtype=float).reshape(1, 1, 4, 4)
    out = max_pool2d(X, 2)
    assert out.shape == (1, 1, 2, 2)
    assert np.allclose(out[0, 0], [[6, 8], [14, 16]])


def test_stage2_relu():
    assert np.allclose(relu(np.array([-1.0, 0.0, 2.0])), [0.0, 0.0, 2.0])


# ----- Stage 3: backward via numerical gradient -----
def test_stage3_conv_backward_gradcheck():
    rng = np.random.default_rng(0)
    X = rng.normal(size=(2, 2, 4, 4))
    W = rng.normal(size=(3, 2, 2, 2))
    b = rng.normal(size=3)
    dout = np.ones((2, 3, 3, 3))          # loss = sum(conv_forward) -> upstream grad is ones
    dX, dW, db = conv2d_backward(X, W, dout)

    def loss(X, W, b):
        return conv2d_forward(X, W, b).sum()

    h = 1e-5
    for idx in [(0, 0, 0, 0), (1, 1, 3, 3), (0, 1, 2, 1)]:
        Xp = X.copy(); Xp[idx] += h
        Xm = X.copy(); Xm[idx] -= h
        assert np.isclose(dX[idx], (loss(Xp, W, b) - loss(Xm, W, b)) / (2 * h), atol=1e-4)

    for idx in [(2, 1, 1, 0), (0, 0, 0, 1)]:
        Wp = W.copy(); Wp[idx] += h
        Wm = W.copy(); Wm[idx] -= h
        assert np.isclose(dW[idx], (loss(X, Wp, b) - loss(X, Wm, b)) / (2 * h), atol=1e-4)

    bp = b.copy(); bp[1] += h
    bm = b.copy(); bm[1] -= h
    assert np.isclose(db[1], (loss(X, W, bp) - loss(X, W, bm)) / (2 * h), atol=1e-4)
