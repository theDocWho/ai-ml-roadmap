"""BYO-5 Stage 3 — optimizers (exam Q7/Q8 made concrete)."""
import numpy as np


class SGD:
    def __init__(self, params, lr=0.1):
        self.params = list(params)
        self.lr = lr

    def step(self):
        # TODO: for each p: p.data -= lr * p.grad
        raise NotImplementedError("implement SGD.step")

    def zero_grad(self):
        for p in self.params:
            p.grad = np.zeros_like(p.data)


class Adam:
    def __init__(self, params, lr=0.01, betas=(0.9, 0.999), eps=1e-8):
        self.params = list(params)
        self.lr = lr
        self.b1, self.b2 = betas
        self.eps = eps
        self.m = [np.zeros_like(p.data) for p in self.params]
        self.v = [np.zeros_like(p.data) for p in self.params]
        self.t = 0

    def step(self):
        # TODO: standard Adam:
        #   t += 1
        #   m = b1*m + (1-b1)*g ;  v = b2*v + (1-b2)*g**2
        #   mhat = m/(1-b1**t) ;   vhat = v/(1-b2**t)
        #   p.data -= lr * mhat / (sqrt(vhat) + eps)
        raise NotImplementedError("implement Adam.step")

    def zero_grad(self):
        for p in self.params:
            p.grad = np.zeros_like(p.data)
