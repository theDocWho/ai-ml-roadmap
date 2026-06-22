"""BYO-6 starter — a convolution layer from scratch (NumPy only). See README.md.

Tensors are NCHW: X is (N, Cin, H, W); kernels W are (Cout, Cin, kh, kw); bias b is (Cout,).
We use 'valid' convolution (no padding, stride 1). The point of this challenge is the
**backward pass** — getting conv gradients right, verified against a numerical gradient.
"""
import numpy as np


def relu(x):
    """ReLU forward."""
    raise NotImplementedError("implement relu")


def conv2d_forward(X, W, b):
    """Stage 1: valid 2D convolution. Output is (N, Cout, H-kh+1, W-kw+1).
    out[n, co, i, j] = sum over (cin, di, dj) of X[n, cin, i+di, j+dj] * W[co, cin, di, dj] + b[co].
    """
    raise NotImplementedError("implement conv2d_forward")


def max_pool2d(X, size):
    """Stage 2: non-overlapping max pooling with window `size`. Output (N, C, H//size, W//size)."""
    raise NotImplementedError("implement max_pool2d")


def conv2d_backward(X, W, dout):
    """Stage 3: given upstream gradient `dout` (shape of the forward output), return (dX, dW, db).
        db[co]              = sum of dout[:, co]
        dW[co, cin, di, dj] = sum over (n,i,j) of X[n,cin,i+di,j+dj] * dout[n,co,i,j]
        dX[n,cin,i+di,j+dj] += W[co,cin,di,dj] * dout[n,co,i,j]   (accumulate over co,i,j)
    Verify it with a numerical gradient — that's what the test does.
    """
    raise NotImplementedError("implement conv2d_backward")
