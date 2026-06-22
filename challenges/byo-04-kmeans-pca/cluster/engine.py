"""BYO-4 starter — implement the TODOs with NumPy only. See README.md."""
import numpy as np


class KMeans:
    def __init__(self, k, max_iters=100, init="kmeans++", seed=0, tol=1e-6):
        self.k = k
        self.max_iters = max_iters
        self.init = init
        self.seed = seed
        self.tol = tol
        self.centroids_ = None
        self.labels_ = None
        self.inertia_ = None

    def _init_centroids(self, X, rng):
        """Stage 1: random rows. Stage 2: kmeans++ (distance-weighted seeding)."""
        raise NotImplementedError("implement _init_centroids")

    def fit(self, X):
        """Stage 1: Lloyd's algorithm.
        loop max_iters:
            labels = argmin over centroids of ||x - c||^2
            new_centroids = mean of points per cluster
            stop if centroids move less than tol
        set self.centroids_, self.labels_, self.inertia_ ; return self."""
        raise NotImplementedError("implement KMeans.fit")

    def predict(self, X):
        """Assign each row to the nearest fitted centroid."""
        raise NotImplementedError("implement KMeans.predict")


class PCA:
    def __init__(self, n_components):
        self.n_components = n_components
        self.mean_ = None
        self.components_ = None                 # shape (n_components, n_features)
        self.explained_variance_ratio_ = None

    def fit(self, X):
        """Stage 3: mean-center X; C = covariance(X); eigen-decompose C (use np.linalg.eigh);
        sort eigenvectors by descending eigenvalue; keep the top n_components.
        Store self.mean_, self.components_, self.explained_variance_ratio_ ; return self."""
        raise NotImplementedError("implement PCA.fit")

    def transform(self, X):
        """Stage 4: (X - mean_) @ components_.T  -> shape (n_samples, n_components)."""
        raise NotImplementedError("implement PCA.transform")

    def inverse_transform(self, Z):
        """Stage 4: Z @ components_ + mean_  -> back to original space."""
        raise NotImplementedError("implement PCA.inverse_transform")
