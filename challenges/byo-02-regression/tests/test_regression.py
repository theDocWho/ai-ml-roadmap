"""Staged acceptance tests for BYO-2. Implement until all pass."""
import numpy as np
from linreg.engine import LinearRegression, LogisticRegression, mse


# ----- Stage 1: predict + loss -----
def test_stage1_mse():
    assert mse(np.array([1.0, 2.0, 3.0]), np.array([1.0, 2.0, 3.0])) == 0.0
    assert np.isclose(mse(np.array([0.0, 0.0]), np.array([1.0, 3.0])), 5.0)


def test_stage1_predict():
    m = LinearRegression()
    m.w = np.array([2.0, -1.0])
    m.b = 0.5
    X = np.array([[1.0, 1.0], [2.0, 0.0]])
    assert np.allclose(m.predict(X), [1.5, 4.5])


# ----- Stage 2: closed form -----
def test_stage2_normal_equation_recovers_line():
    rng = np.random.default_rng(0)
    X = rng.normal(size=(200, 1))
    y = (3.0 * X[:, 0] + 2.0)            # exact line, no noise
    m = LinearRegression()
    m.fit_normal_equation(X, y)
    assert np.isclose(m.w[0], 3.0, atol=1e-6)
    assert np.isclose(m.b, 2.0, atol=1e-6)


# ----- Stage 3: gradient descent -----
def test_stage3_gradient_descent_converges():
    rng = np.random.default_rng(1)
    X = rng.normal(size=(300, 2))
    y = X @ np.array([1.5, -2.0]) + 0.7
    m = LinearRegression(lr=0.05, n_iters=5000)
    m.fit(X, y)
    assert mse(y, m.predict(X)) < 1e-3
    assert np.allclose(m.w, [1.5, -2.0], atol=0.05)


# ----- Stage 4: regularization + logistic -----
def test_stage4_l2_shrinks_weights():
    rng = np.random.default_rng(2)
    X = rng.normal(size=(200, 5))
    y = X @ np.array([3.0, 3.0, 3.0, 3.0, 3.0]) + 1.0
    plain = LinearRegression(lr=0.02, n_iters=3000, l2=0.0).fit(X, y)
    ridge = LinearRegression(lr=0.02, n_iters=3000, l2=1.0).fit(X, y)
    assert np.linalg.norm(ridge.w) < np.linalg.norm(plain.w)


def test_stage4_logistic_separates():
    rng = np.random.default_rng(3)
    pos = rng.normal(loc=2.0, size=(100, 2))
    neg = rng.normal(loc=-2.0, size=(100, 2))
    X = np.vstack([pos, neg])
    y = np.array([1] * 100 + [0] * 100)
    clf = LogisticRegression(lr=0.1, n_iters=3000).fit(X, y)
    acc = (clf.predict(X) == y).mean()
    assert acc > 0.95
