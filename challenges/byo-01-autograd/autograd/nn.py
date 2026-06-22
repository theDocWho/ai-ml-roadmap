"""
BYO-1 Stage 4 starter — a minimal neural-net library built on your Value engine.
Implement the TODOs. Only `autograd.Value` is allowed (no NumPy).
"""
import random
from .engine import Value


class Module:
    def zero_grad(self):
        for p in self.parameters():
            p.grad = 0.0

    def parameters(self):
        return []


class Neuron(Module):
    def __init__(self, nin):
        # TODO(stage4): self.w = [Value(random.uniform(-1, 1)) for _ in range(nin)]
        #               self.b = Value(0.0)
        raise NotImplementedError("implement Neuron.__init__")

    def __call__(self, x):
        # TODO(stage4): act = sum(wi*xi) + b  ; return act.tanh()
        raise NotImplementedError("implement Neuron.__call__")

    def parameters(self):
        # TODO(stage4): return self.w + [self.b]
        raise NotImplementedError("implement Neuron.parameters")


class Layer(Module):
    def __init__(self, nin, nout):
        # TODO(stage4): self.neurons = [Neuron(nin) for _ in range(nout)]
        raise NotImplementedError("implement Layer.__init__")

    def __call__(self, x):
        # TODO(stage4): outs = [n(x) for n in self.neurons]
        #               return outs[0] if len(outs) == 1 else outs
        raise NotImplementedError("implement Layer.__call__")

    def parameters(self):
        return [p for n in self.neurons for p in n.parameters()]


class MLP(Module):
    def __init__(self, nin, nouts):
        # TODO(stage4): sizes = [nin] + nouts
        #               self.layers = [Layer(sizes[i], sizes[i+1]) for i in range(len(nouts))]
        raise NotImplementedError("implement MLP.__init__")

    def __call__(self, x):
        for layer in self.layers:
            x = layer(x)
        return x

    def parameters(self):
        return [p for layer in self.layers for p in layer.parameters()]
