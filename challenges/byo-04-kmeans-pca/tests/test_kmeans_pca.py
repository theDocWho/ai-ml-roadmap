"""Staged acceptance tests for BYO-4."""
import numpy as np
from cluster.engine import KMeans, PCA


def _two_blobs(n=150, seed=0):
    rng = np.random.default_rng(seed)
    a = rng.normal(loc=[-5, -5], scale=0.5, size=(n, 2))
    b = rng.normal(loc=[5, 5], scale=0.5, size=(n, 2))
    return np.vstack([a, b]), np.array([0] * n + [1] * n)


# ----- Stage 1/2: K-Means -----
def test_stage1_kmeans_recovers_clusters():
    X, true = _two_blobs()
    km = KMeans(k=2, seed=0).fit(X)
    labels = km.labels_
    # cluster purity: each predicted cluster is almost entirely one true class
    purity = max(
        (labels == true).mean(),
        (labels == (1 - true)).mean(),     # labels may be permuted
    )
    assert purity > 0.98
    assert km.inertia_ > 0


def test_stage1_predict_matches_fit():
    X, _ = _two_blobs()
    km = KMeans(k=2, seed=1).fit(X)
    assert np.array_equal(km.predict(X), km.labels_)


# ----- Stage 3/4: PCA -----
def test_stage3_pca_captures_variance_on_a_line():
    rng = np.random.default_rng(2)
    t = rng.normal(size=300)
    # data mostly along direction (3, 1) with tiny orthogonal noise
    X = np.c_[3 * t, 1 * t] + rng.normal(scale=0.01, size=(300, 2))
    pca = PCA(n_components=1).fit(X)
    assert pca.explained_variance_ratio_[0] > 0.99


def test_stage4_transform_and_reconstruct():
    rng = np.random.default_rng(3)
    t = rng.normal(size=200)
    X = np.c_[2 * t, -t] + rng.normal(scale=0.01, size=(200, 2))
    pca = PCA(n_components=1).fit(X)
    Z = pca.transform(X)
    assert Z.shape == (200, 1)
    X_rec = pca.inverse_transform(Z)
    assert np.mean((X - X_rec) ** 2) < 0.01
