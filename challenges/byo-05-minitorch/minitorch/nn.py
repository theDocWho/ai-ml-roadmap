"""BYO-5 Stage 2 — layers and loss built on the Tensor engine."""
import numpy as np
from .tensor import Tensor


class Module:
    def parameters(self):
        return []

    def zero_grad(self):
        for p in self.parameters():
            p.grad = np.zeros_like(p.data)


class Linear(Module):
    def __init__(self, nin, nout, seed=0):
        rng = np.random.default_rng(seed)
        # TODO: self.W = Tensor(small random, shape (nin, nout)); self.b = Tensor(zeros(nout))
        raise NotImplementedError("implement Linear.__init__")

    def __call__(self, x):
        # TODO: return x @ self.W + self.b
        raise NotImplementedError("implement Linear.__call__")

    def parameters(self):
        return [self.W, self.b]


def relu(x):
    return x.relu()


def softmax_cross_entropy(logits, labels):
    """Stage 2: numerically-stable softmax + cross-entropy over a batch.

    `logits` is a Tensor of shape (N, C); `labels` is an int array of shape (N,).
    Returns a scalar Tensor. Its backward must set:
        logits.grad += (softmax(logits) - onehot(labels)) / N * out.grad
    (the clean closed-form gradient — no need to autodiff through log/exp).
    """
    raise NotImplementedError("implement softmax_cross_entropy")
