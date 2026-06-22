"""BYO-11 starter — a vector database from scratch (NumPy + stdlib only). See README.md.

Build the thing FAISS/Chroma do: store vectors, do exact (brute-force) nearest-neighbour search,
then an approximate (ANN) index that trades a little recall for speed, plus save/load to disk.
"""
import numpy as np


def cosine_similarities(query, matrix):
    """Stage 1: cosine similarity of `query` (d,) against every row of `matrix` (n, d).
    Return a (n,) array. Guard zero norms."""
    raise NotImplementedError("implement cosine_similarities")


class VectorDB:
    def __init__(self):
        self.ids = []
        self.vectors = []          # list of 1-D np arrays (or build a matrix lazily)
        self.meta = []
        self.centroids_ = None     # set by build_index
        self.assignments_ = None   # cluster id per stored vector

    def add(self, id, vector, metadata=None):
        """Stage 1: store one vector with its id and optional metadata. Return self."""
        raise NotImplementedError("implement add")

    def search(self, query, k=5):
        """Stage 1: EXACT brute-force search. Return the top-k as a list of (id, score),
        most similar first."""
        raise NotImplementedError("implement search")

    def build_index(self, n_clusters, seed=0, iters=25):
        """Stage 2: cluster the stored vectors with k-means; keep self.centroids_ and the
        per-vector self.assignments_ (each vector's nearest centroid = its bucket). Return self."""
        raise NotImplementedError("implement build_index")

    def search_ann(self, query, k=5, n_probe=1):
        """Stage 2: approximate search. Find the `n_probe` nearest centroids to the query, gather
        only the vectors in those buckets as candidates, and brute-force rank just those. Return
        top-k (id, score)."""
        raise NotImplementedError("implement search_ann")

    def save(self, path):
        """Stage 3: persist the whole DB to `path` (pickle is fine — stdlib)."""
        raise NotImplementedError("implement save")

    @classmethod
    def load(cls, path):
        """Stage 3: load a DB previously written by save()."""
        raise NotImplementedError("implement load")
