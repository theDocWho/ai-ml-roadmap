"""Staged acceptance tests for BYO-14."""
import numpy as np
from ids.engine import standardize, precision_recall, roc_auc, KNNAnomalyDetector


# ----- Stage 1 -----
def test_stage1_standardize():
    X = np.array([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
    Xs, m, s = standardize(X)
    assert np.allclose(Xs.mean(axis=0), 0.0, atol=1e-9)
    assert np.allclose(Xs.std(axis=0), 1.0, atol=1e-9)
    # reuse fitted stats
    Xs2, _, _ = standardize(X, m, s)
    assert np.allclose(Xs, Xs2)


# ----- Stage 4 metrics -----
def test_stage4_precision_recall():
    y = np.array([1, 1, 0, 0, 1])
    pred = np.array([1, 0, 0, 1, 1])     # TP=2, FP=1, FN=1
    p, r = precision_recall(y, pred)
    assert np.isclose(p, 2 / 3) and np.isclose(r, 2 / 3)


def test_stage4_roc_auc():
    y = np.array([0, 0, 1, 1])
    assert np.isclose(roc_auc(y, [0.1, 0.2, 0.8, 0.9]), 1.0)
    assert np.isclose(roc_auc(y, [0.9, 0.8, 0.2, 0.1]), 0.0)


# ----- Stage 2/3: the detector -----
def test_stage23_flags_injected_intrusions():
    rng = np.random.default_rng(0)
    X_train = rng.normal(0, 1, size=(300, 5))           # normal traffic only
    normal_test = rng.normal(0, 1, size=(100, 5))
    attacks = rng.normal(8, 1, size=(20, 5))            # injected anomalies, far away
    X_test = np.vstack([normal_test, attacks])
    y_test = np.array([0] * 100 + [1] * 20)

    det = KNNAnomalyDetector(k=5, contamination=0.05).fit(X_train)
    pred = det.predict(X_test)
    p, r = precision_recall(y_test, pred)
    assert r > 0.95 and p > 0.8
    assert roc_auc(y_test, det.score_samples(X_test)) > 0.99
