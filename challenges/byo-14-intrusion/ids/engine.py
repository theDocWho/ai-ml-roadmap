"""BYO-14 starter — a from-scratch anomaly-based intrusion detector (NumPy only).

The cyber framing: you train only on *normal* traffic, then flag points that look unlike anything
seen in training. This is exactly how unsupervised network-intrusion detection works (NSL-KDD,
CIC-IDS). See README.md.
"""
import numpy as np


def standardize(X, mean=None, std=None):
    """Stage 1: z-score features. If mean/std are None compute them from X.
    Return (X_scaled, mean, std). Guard against std == 0 (use 1.0 there)."""
    raise NotImplementedError("implement standardize")


def precision_recall(y_true, y_pred):
    """Stage 4: positive class = 1 (anomaly). Return (precision, recall).
    precision = TP / (TP + FP); recall = TP / (TP + FN)."""
    raise NotImplementedError("implement precision_recall")


def roc_auc(y_true, scores):
    """Stage 4: ROC-AUC via the Mann-Whitney U / rank formula:
        AUC = (sum_of_ranks_of_positives - n_pos*(n_pos+1)/2) / (n_pos * n_neg)
    Higher score should mean 'more anomalous'."""
    raise NotImplementedError("implement roc_auc")


class KNNAnomalyDetector:
    """Distance-to-k-nearest-neighbors anomaly detector."""

    def __init__(self, k=5, contamination=0.05):
        self.k = k
        self.contamination = contamination
        self.mean_ = None
        self.std_ = None
        self.train_ = None          # standardized training (normal) data
        self.threshold_ = None

    def fit(self, X):
        """Stage 2+3: standardize and store X; set self.threshold_ to the
        (1 - contamination) quantile of the training anomaly scores (exclude each point's own
        zero self-distance when scoring the training set). Return self."""
        raise NotImplementedError("implement KNNAnomalyDetector.fit")

    def score_samples(self, X):
        """Stage 2: anomaly score = mean Euclidean distance to the k nearest *training* points
        (after standardizing X with the fitted mean/std)."""
        raise NotImplementedError("implement score_samples")

    def predict(self, X):
        """Stage 3: 1 (anomaly) if score > threshold_, else 0."""
        raise NotImplementedError("implement predict")
