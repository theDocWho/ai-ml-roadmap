"""BYO-3 starter — implement the TODOs with NumPy only. See README.md."""
import numpy as np


def gini(y):
    """Stage 1: Gini impurity = 1 - sum_k p_k**2, where p_k is the fraction of class k."""
    raise NotImplementedError("implement gini")


def best_split(X, y):
    """Stage 2: return (feature_index, threshold) that maximizes impurity decrease.

    For each feature, try thresholds (e.g. midpoints of sorted unique values). Score a split by:
        weighted_impurity = (n_left/n)*gini(y_left) + (n_right/n)*gini(y_right)
    Pick the split with the lowest weighted impurity. Return (None, None) if no useful split.
    """
    raise NotImplementedError("implement best_split")


class _Node:
    __slots__ = ("feature", "threshold", "left", "right", "value")

    def __init__(self, feature=None, threshold=None, left=None, right=None, value=None):
        self.feature = feature
        self.threshold = threshold
        self.left = left
        self.right = right
        self.value = value          # set on leaves: the predicted class


class DecisionTree:
    def __init__(self, max_depth=5, min_samples=2):
        self.max_depth = max_depth
        self.min_samples = min_samples
        self.root = None

    def fit(self, X, y):
        """Stage 3: build the tree recursively; return self.
        Stop (make a leaf with the majority class) when: depth >= max_depth, samples < min_samples,
        the node is pure, or best_split finds nothing."""
        raise NotImplementedError("implement DecisionTree.fit")

    def predict(self, X):
        """Stage 3: route each row from root to a leaf and return its class."""
        raise NotImplementedError("implement DecisionTree.predict")


class RandomForest:
    def __init__(self, n_trees=10, max_depth=5, min_samples=2, max_features=None, seed=0):
        self.n_trees = n_trees
        self.max_depth = max_depth
        self.min_samples = min_samples
        self.max_features = max_features      # how many features to consider per split
        self.seed = seed
        self.trees = []

    def fit(self, X, y):
        """Stage 4: train n_trees on bootstrap samples (sample rows with replacement); each tree
        should consider a random feature subset at its splits. Return self."""
        raise NotImplementedError("implement RandomForest.fit")

    def predict(self, X):
        """Stage 4: majority vote across the trees."""
        raise NotImplementedError("implement RandomForest.predict")
