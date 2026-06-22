"""BYO-5 starter — a NumPy autograd Tensor (the engine behind PyTorch). See README.md.

This generalizes BYO-1 from scalars to arrays. The hard part is **broadcasting**: when an op
broadcasts (e.g. adding a (4,) bias to a (5,4) matrix), the backward pass must sum the gradient
back down to the original shape. `_unbroadcast` does that — it's provided for you.
"""
import numpy as np


def _unbroadcast(grad, shape):
    """Sum `grad` so it matches `shape` (the reverse of NumPy broadcasting)."""
    while grad.ndim > len(shape):
        grad = grad.sum(axis=0)
    for i, s in enumerate(shape):
        if s == 1:
            grad = grad.sum(axis=i, keepdims=True)
    return grad


class Tensor:
    def __init__(self, data, _children=(), _op=""):
        self.data = np.asarray(data, dtype=float)
        self.grad = np.zeros_like(self.data)
        self._backward = lambda: None
        self._prev = set(_children)
        self._op = _op

    # ----- Stage 1: ops -----
    def __add__(self, other):
        other = other if isinstance(other, Tensor) else Tensor(other)
        # TODO: out = Tensor(self.data + other.data, (self, other), "+")
        # backward: each input += _unbroadcast(out.grad, input.data.shape)
        raise NotImplementedError("implement __add__")

    def __mul__(self, other):
        other = other if isinstance(other, Tensor) else Tensor(other)
        # TODO: elementwise; backward: self += _unbroadcast(other.data*out.grad, self.shape), sym.
        raise NotImplementedError("implement __mul__")

    def __matmul__(self, other):
        # TODO: out = self.data @ other.data
        # backward: self.grad += out.grad @ other.data.T ; other.grad += self.data.T @ out.grad
        raise NotImplementedError("implement __matmul__")

    def relu(self):
        # TODO: max(0, data); backward: self.grad += (self.data > 0) * out.grad
        raise NotImplementedError("implement relu")

    def sum(self):
        # TODO: scalar sum; backward: self.grad += ones_like(self.data) * out.grad
        raise NotImplementedError("implement sum")

    def mean(self):
        # TODO: sum/size; backward scales by 1/size
        raise NotImplementedError("implement mean")

    def __radd__(self, other):
        return self + other

    def __rmul__(self, other):
        return self * other

    # ----- Stage 1: autodiff -----
    def backward(self):
        """Topological order, seed root grad with ones, walk in reverse calling each _backward."""
        # TODO: same shape as BYO-1 but the root grad is np.ones_like(self.data)
        raise NotImplementedError("implement backward")
