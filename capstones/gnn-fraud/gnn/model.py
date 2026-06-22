"""The Graph Convolutional Network — THIS is what you implement.

`relu`, `softmax`, `cross_entropy_loss` are given. You build the graph-conv op and the 2-layer GCN
(forward + the backprop in `train`). Backprop math is spelled out in the README and `train` docstring.
"""
import numpy as np


def relu(x):
    return np.maximum(0.0, x)


def softmax(x):
    x = x - x.max(axis=1, keepdims=True)
    e = np.exp(x)
    return e / e.sum(axis=1, keepdims=True)


def cross_entropy_loss(logits, y, mask):
    """Mean cross-entropy over the masked (labeled) nodes only."""
    p = softmax(logits)
    return float(-np.log(p[mask, y[mask]] + 1e-12).mean())


def gcn_layer(A_hat, H, W):
    """TODO: one graph-conv step = propagate over neighbours then transform: A_hat @ H @ W."""
    raise NotImplementedError("implement gcn_layer")


class GCN:
    """A 2-layer GCN:  logits = Â · ReLU(Â · X · W0) · W1."""

    def __init__(self, in_dim, hidden, n_classes, seed=0):
        rng = np.random.default_rng(seed)
        self.W0 = rng.normal(0, np.sqrt(2.0 / (in_dim + hidden)), (in_dim, hidden))
        self.W1 = rng.normal(0, np.sqrt(2.0 / (hidden + n_classes)), (hidden, n_classes))

    def forward(self, A_hat, X):
        """TODO: Z1 = gcn_layer(A_hat, X, W0); H1 = relu(Z1); logits = gcn_layer(A_hat, H1, W1).
        Return logits (and keep Z1, H1 around if you compute gradients in train)."""
        raise NotImplementedError("implement forward")

    def train(self, A_hat, X, y, train_mask, lr=0.5, epochs=200):
        """TODO: full-batch training with manual backprop. Each epoch:
            Z1 = A_hat @ X @ W0 ; H1 = relu(Z1) ; logits = A_hat @ H1 @ W1
            P  = softmax(logits)
            dlogits = (P - onehot(y)) / n_train ; zero out rows NOT in train_mask
            dW1 = H1.T @ (A_hat @ dlogits)             # A_hat is symmetric
            dH1 = A_hat @ dlogits @ W1.T ; dZ1 = dH1 * (Z1 > 0)
            dW0 = X.T  @ (A_hat @ dZ1)
            W0 -= lr*dW0 ; W1 -= lr*dW1
        Return self."""
        raise NotImplementedError("implement train")

    def predict(self, A_hat, X):
        return self.forward(A_hat, X).argmax(axis=1)
