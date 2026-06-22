"""Staged acceptance tests for BYO-11."""
import numpy as np
from vectordb.db import cosine_similarities, VectorDB


def _data(seed=0, n=200, d=8):
    return np.random.default_rng(seed).normal(size=(n, d))


# ----- Stage 1: brute force -----
def test_stage1_cosine_similarities():
    M = np.array([[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]])
    sims = cosine_similarities(np.array([1.0, 0.0]), M)
    assert np.isclose(sims[0], 1.0)
    assert np.isclose(sims[1], 0.0)
    assert np.isclose(sims[2], 1 / np.sqrt(2))


def test_stage1_search_finds_self():
    V = _data()
    db = VectorDB()
    for i, v in enumerate(V):
        db.add(i, v)
    top = db.search(V[5], k=3)
    assert top[0][0] == 5                      # nearest neighbour of a point is itself
    assert top[0][1] >= top[1][1]              # sorted by descending similarity


# ----- Stage 2: ANN index -----
def test_stage2_ann_recall_matches_bruteforce():
    V = _data(seed=1, n=300, d=8)
    db = VectorDB()
    for i, v in enumerate(V):
        db.add(i, v)
    db.build_index(n_clusters=10, seed=0)
    rng = np.random.default_rng(2)
    hits, Q = 0, 30
    for _ in range(Q):
        q = rng.normal(size=8)
        bf = db.search(q, k=1)[0][0]
        ann = db.search_ann(q, k=1, n_probe=3)[0][0]
        hits += int(bf == ann)
    assert hits / Q >= 0.7                      # ANN recovers the exact top-1 most of the time


# ----- Stage 3: persistence -----
def test_stage3_persistence_roundtrip(tmp_path):
    V = _data(seed=3)
    db = VectorDB()
    for i, v in enumerate(V):
        db.add(i, v, {"tag": f"t{i}"})
    path = str(tmp_path / "db.pkl")
    db.save(path)

    db2 = VectorDB.load(path)
    assert len(db2.ids) == len(db.ids)
    assert db2.search(V[7], k=1)[0][0] == 7     # search still works after reload
    assert db2.meta[7]["tag"] == "t7"           # metadata survived
