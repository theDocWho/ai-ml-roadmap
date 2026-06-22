"""Acceptance tests for the GNN fraud-ring detector capstone."""
import numpy as np
from gnn.graph import make_fraud_graph, normalized_adjacency, accuracy
from gnn.model import gcn_layer, GCN


# ----- graph utilities (given) -----
def test_graph_shapes_and_labels():
    A, X, y, tr, te = make_fraud_graph(seed=0)
    N = A.shape[0]
    assert A.shape == (N, N)
    assert X.shape[0] == N
    assert set(np.unique(y)) == {0, 1}
    assert not (tr & te).any()            # train/test disjoint
    assert (tr | te).all()                # every node assigned


def test_fraud_nodes_are_more_connected():
    A, X, y, _, _ = make_fraud_graph(seed=0)
    deg = A.sum(axis=1)
    assert deg[y == 1].mean() > deg[y == 0].mean()    # rings are dense


def test_normalized_adjacency_symmetric_with_self_loops():
    A, _, _, _, _ = make_fraud_graph(seed=0)
    A_hat = normalized_adjacency(A)
    assert np.allclose(A_hat, A_hat.T)
    assert np.all(np.diag(A_hat) > 0)                  # self-loops added


# ----- the GNN (you implement) -----
def test_gcn_layer_known_values():
    A_hat = np.array([[1.0, 0.0], [0.0, 1.0]])         # identity -> just H @ W
    H = np.array([[1.0, 2.0], [3.0, 4.0]])
    W = np.array([[1.0], [1.0]])
    out = gcn_layer(A_hat, H, W)
    assert out.shape == (2, 1)
    assert np.allclose(out[:, 0], [3.0, 7.0])          # row sums


def test_gcn_forward_shape():
    A, X, y, tr, te = make_fraud_graph(seed=0)
    A_hat = normalized_adjacency(A)
    gcn = GCN(X.shape[1], 16, 2, seed=1)
    logits = gcn.forward(A_hat, X)
    assert logits.shape == (A.shape[0], 2)


def test_gcn_detects_fraud_rings():
    A, X, y, tr, te = make_fraud_graph(seed=0)
    A_hat = normalized_adjacency(A)
    gcn = GCN(X.shape[1], 16, 2, seed=1)
    gcn.train(A_hat, X, y, tr, lr=0.5, epochs=300)

    acc = accuracy(gcn.forward(A_hat, X), y, te)
    assert acc > 0.8                                   # beats the majority-class baseline

    pred = gcn.predict(A_hat, X)
    fraud_test = te & (y == 1)
    recall = (pred[fraud_test] == 1).mean()
    assert recall > 0.5                                # actually catches fraud, not just normals
