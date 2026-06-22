"""
BYO-1 starter — implement the TODOs. Do NOT peek at micrograd until you're done.

Each operation must:
  1) compute the forward value,
  2) create the output Value with `_children` and `_op` set,
  3) define a local `_backward()` closure implementing the chain rule,
  4) attach that closure as `out._backward`.
"""
import math


class Value:
    """A single scalar value and its gradient in the computation graph."""

    def __init__(self, data, _children=(), _op=""):
        self.data = float(data)
        self.grad = 0.0
        # internal autograd bookkeeping
        self._backward = lambda: None      # set by each operation
        self._prev = set(_children)        # the Values that produced this one
        self._op = _op                     # the op that produced this (for debugging)

    # ----- Stage 1 -----
    def __add__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        # TODO(stage1): out = Value(self.data + other.data, (self, other), "+")
        # TODO(stage3): define out._backward to add `out.grad` to self.grad and other.grad
        raise NotImplementedError("implement __add__")

    def __mul__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        # TODO(stage1): forward = self.data * other.data
        # TODO(stage3): self.grad += other.data * out.grad ; other.grad += self.data * out.grad
        raise NotImplementedError("implement __mul__")

    def __repr__(self):
        # TODO(stage1): return f"Value(data={self.data}, grad={self.grad})"
        raise NotImplementedError("implement __repr__")

    # ----- Stage 2 -----
    def __pow__(self, other):
        assert isinstance(other, (int, float)), "only int/float powers supported"
        # TODO(stage2): forward = self.data ** other
        # TODO(stage3): self.grad += (other * self.data**(other-1)) * out.grad
        raise NotImplementedError("implement __pow__")

    def tanh(self):
        # TODO(stage2): t = math.tanh(self.data)
        # TODO(stage3): self.grad += (1 - t**2) * out.grad
        raise NotImplementedError("implement tanh")

    def exp(self):
        # TODO(stage2): e = math.exp(self.data)
        # TODO(stage3): self.grad += e * out.grad   (d/dx e^x = e^x)
        raise NotImplementedError("implement exp")

    def relu(self):
        # TODO(stage2): forward = max(0.0, self.data)
        # TODO(stage3): self.grad += (out.data > 0) * out.grad
        raise NotImplementedError("implement relu")

    def __neg__(self):
        # TODO(stage2): return self * -1
        raise NotImplementedError("implement __neg__")

    def __sub__(self, other):
        # TODO(stage2): return self + (-other)
        raise NotImplementedError("implement __sub__")

    def __truediv__(self, other):
        # TODO(stage2): return self * (other ** -1)
        raise NotImplementedError("implement __truediv__")

    def __radd__(self, other):   # other + self
        return self + other

    def __rmul__(self, other):   # other * self
        return self * other

    def __rsub__(self, other):   # other - self
        return (-self) + other

    # ----- Stage 3 -----
    def backward(self):
        """Run reverse-mode autodiff from this node."""
        # TODO(stage3):
        #   1. build topological order of the graph behind `self`
        #   2. self.grad = 1.0
        #   3. for node in reversed(topo): node._backward()
        raise NotImplementedError("implement backward")
