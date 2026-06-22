"""Staged acceptance tests for BYO-5."""
import numpy as np
from minitorch.tensor import Tensor
from minitorch.nn import Linear, softmax_cross_entropy
from minitorch.optim import SGD, Adam


# ----- Stage 1: autograd over arrays -----
def test_stage1_backward_matches_numeric():
    a = Tensor([[1.0, 2.0], [3.0, 4.0]])
    b = Tensor([[2.0, 0.0], [1.0, 3.0]])
    out = ((a @ b) + (a * b)).relu().sum()
    out.backward()

    def f(av):
        A = av.reshape(2, 2)
        return np.maximum(0, (A @ b.data) + (A * b.data)).sum()

    base = a.data.flatten()
    num = np.zeros(4)
    h = 1e-6
    for i in range(4):
        p = base.copy(); p[i] += h
        m = base.copy(); m[i] -= h
        num[i] = (f(p) - f(m)) / (2 * h)
    assert np.allclose(a.grad.flatten(), num, atol=1e-4)


def test_stage1_broadcast_bias_grad_shape():
    x = Tensor(np.ones((5, 3)))
    bias = Tensor(np.zeros(3))
    (x + bias).sum().backward()
    assert bias.grad.shape == (3,)
    assert np.allclose(bias.grad, 5.0)     # each bias element summed over 5 rows


# ----- Stage 2: layers + loss -----
def test_stage2_linear_forward_and_params():
    lin = Linear(3, 4, seed=0)
    y = lin(Tensor(np.ones((5, 3))))
    assert y.data.shape == (5, 4)
    assert len(lin.parameters()) == 2


def test_stage2_softmax_cross_entropy_gradient():
    logits = Tensor([[2.0, 1.0, 0.1], [0.5, 2.5, 0.3]])
    labels = np.array([0, 1])
    loss = softmax_cross_entropy(logits, labels)
    assert loss.data > 0
    loss.backward()
    assert logits.grad.shape == (2, 3)
    # softmax - onehot sums to 0 per row -> gradient rows sum to ~0
    assert np.allclose(logits.grad.sum(axis=1), 0.0, atol=1e-6)


# ----- Stage 3: train a real MLP -----
def _data(seed=0):
    rng = np.random.default_rng(seed)
    pos = rng.normal(loc=[2, 2], size=(100, 2))
    neg = rng.normal(loc=[-2, -2], size=(100, 2))
    return Tensor(np.vstack([pos, neg])), np.array([0] * 100 + [1] * 100)


def test_stage3_sgd_trains_classifier():
    X, y = _data()
    l1, l2 = Linear(2, 16, seed=1), Linear(16, 2, seed=2)
    opt = SGD(l1.parameters() + l2.parameters(), lr=0.1)

    def forward():
        return l2(l1(X).relu())

    init = softmax_cross_entropy(forward(), y).data
    for _ in range(300):
        opt.zero_grad()
        softmax_cross_entropy(forward(), y).backward()
        opt.step()
    final = softmax_cross_entropy(forward(), y).data
    assert final < init * 0.3
    assert (forward().data.argmax(1) == y).mean() > 0.95


def test_stage3_adam_reduces_loss():
    X, y = _data(seed=4)
    l1, l2 = Linear(2, 8, seed=5), Linear(8, 2, seed=6)
    opt = Adam(l1.parameters() + l2.parameters(), lr=0.05)

    def forward():
        return l2(l1(X).relu())

    init = softmax_cross_entropy(forward(), y).data
    for _ in range(150):
        opt.zero_grad()
        softmax_cross_entropy(forward(), y).backward()
        opt.step()
    assert softmax_cross_entropy(forward(), y).data < init * 0.5
