"""Staged acceptance tests for BYO-3."""
import numpy as np
from trees.engine import gini, best_split, DecisionTree, RandomForest


def _blobs(n=200, seed=0):
    rng = np.random.default_rng(seed)
    a = rng.normal(loc=[-2, -2], size=(n, 2))
    b = rng.normal(loc=[2, 2], size=(n, 2))
    X = np.vstack([a, b])
    y = np.array([0] * n + [1] * n)
    return X, y


# ----- Stage 1 -----
def test_stage1_gini():
    assert np.isclose(gini(np.array([0, 0, 0, 0])), 0.0)
    assert np.isclose(gini(np.array([0, 0, 1, 1])), 0.5)
    assert np.isclose(gini(np.array([0, 1, 1, 1])), 0.375)


# ----- Stage 2 -----
def test_stage2_best_split_finds_separating_feature():
    # feature 0 separates classes at ~0; feature 1 is noise
    X = np.array([[-1, 5], [-2, 1], [1, 9], [2, 0], [-3, 4], [3, 2]], dtype=float)
    y = np.array([0, 0, 1, 1, 0, 1])
    feat, thr = best_split(X, y)
    assert feat == 0
    assert -2 < thr < 1


# ----- Stage 3 -----
def test_stage3_tree_fits_separable_data():
    X, y = _blobs()
    tree = DecisionTree(max_depth=5).fit(X, y)
    acc = (tree.predict(X) == y).mean()
    assert acc > 0.97


def test_stage3_depth_one_is_a_stump():
    X, y = _blobs()
    stump = DecisionTree(max_depth=1).fit(X, y)
    # a single split on these blobs already separates most points
    assert (stump.predict(X) == y).mean() > 0.9


# ----- Stage 4 -----
def test_stage4_forest_trains_and_predicts_well():
    rng = np.random.default_rng(7)
    X = rng.normal(size=(400, 6))
    y = ((X[:, 0] + X[:, 1] - X[:, 2]) > 0).astype(int)     # learnable target
    Xtr, ytr, Xte, yte = X[:300], y[:300], X[300:], y[300:]
    forest = RandomForest(n_trees=20, max_depth=5, max_features=3, seed=1).fit(Xtr, ytr)
    assert len(forest.trees) == 20                          # bagged the right number of trees
    assert (forest.predict(Xte) == yte).mean() > 0.8        # generalizes on held-out data
