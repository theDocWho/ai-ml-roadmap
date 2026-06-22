"""BYO-2 starter — implement the TODOs with NumPy only. See README.md."""
import numpy as np


def mse(y_true, y_pred):
    """Stage 1: mean squared error = mean((y_true - y_pred)**2)."""
    raise NotImplementedError("implement mse")


class LinearRegression:
    def __init__(self, lr=0.01, n_iters=2000, l2=0.0, l1=0.0):
        self.lr = lr
        self.n_iters = n_iters
        self.l2 = l2
        self.l1 = l1
        self.w = None          # shape (n_features,)
        self.b = 0.0

    def predict(self, X):
        """Stage 1: return X @ self.w + self.b."""
        raise NotImplementedError("implement predict")

    def fit_normal_equation(self, X, y):
        """Stage 2: closed form. Augment X with a bias column, solve
        theta = (Xb^T Xb)^-1 Xb^T y, then split into self.w and self.b."""
        raise NotImplementedError("implement fit_normal_equation")

    def fit(self, X, y):
        """Stage 3: batch gradient descent.
        init w = zeros(n_features), b = 0; for n_iters:
            err  = (X @ w + b) - y
            dw   = (2/n) * X.T @ err  + l2*2*w + l1*sign(w)
            db   = (2/n) * sum(err)
            w   -= lr*dw ; b -= lr*db
        Stage 4 adds the l2/l1 terms above. Return self."""
        raise NotImplementedError("implement fit")


class LogisticRegression:
    def __init__(self, lr=0.1, n_iters=3000, l2=0.0):
        self.lr = lr
        self.n_iters = n_iters
        self.l2 = l2
        self.w = None
        self.b = 0.0

    @staticmethod
    def _sigmoid(z):
        return 1.0 / (1.0 + np.exp(-z))

    def fit(self, X, y):
        """Stage 4: gradient descent on binary cross-entropy.
        p = sigmoid(X@w+b); grad of BCE wrt w is (1/n) X.T @ (p - y) (+ l2 term).
        Return self (the tests chain .fit(X, y))."""
        raise NotImplementedError("implement LogisticRegression.fit")

    def predict_proba(self, X):
        raise NotImplementedError("implement predict_proba")

    def predict(self, X):
        """Return 0/1 at threshold 0.5."""
        raise NotImplementedError("implement predict")
