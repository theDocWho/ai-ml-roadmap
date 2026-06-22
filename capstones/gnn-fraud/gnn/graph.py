"""Graph data + utilities (provided, fully implemented).

We synthesize an account graph where fraudsters form densely-connected "rings" (a clique-ish
community) — the structure real money-laundering / collusion rings show. Each node has weak,
noisy features; the fraud signal is barely visible per-node but is amplified when a GNN aggregates
over the dense ring. That's the whole point: structure + propagation beats features alone.
"""
import numpy as np


def make_fraud_graph(seed=0, n_normal=120, n_rings=8, ring_size=10,
                     p_normal=0.03, p_ring=0.45, p_camouflage=0.01,
                     feat_dim=8, signal=0.6):
    rng = np.random.default_rng(seed)
    n_fraud = n_rings * ring_size
    N = n_normal + n_fraud
    A = np.zeros((N, N))

    # sparse normal-to-normal edges
    for i in range(n_normal):
        for j in range(i + 1, n_normal):
            if rng.random() < p_normal:
                A[i, j] = A[j, i] = 1.0

    # fraud rings: dense intra-community edges
    y = np.zeros(N, dtype=int)
    y[n_normal:] = 1
    for r in range(n_rings):
        base = n_normal + r * ring_size
        members = range(base, base + ring_size)
        for u in members:
            for v in members:
                if u < v and rng.random() < p_ring:
                    A[u, v] = A[v, u] = 1.0

    # a few camouflage edges fraud<->normal
    for u in range(n_normal, N):
        for v in range(n_normal):
            if rng.random() < p_camouflage:
                A[u, v] = A[v, u] = 1.0

    # weak, noisy node features; fraud has a small mean shift in the first 2 dims
    X = rng.normal(0, 1, size=(N, feat_dim))
    X[n_normal:, :2] += signal

    # 60/40 train/test split
    perm = rng.permutation(N)
    n_train = int(0.6 * N)
    train_mask = np.zeros(N, dtype=bool)
    test_mask = np.zeros(N, dtype=bool)
    train_mask[perm[:n_train]] = True
    test_mask[perm[n_train:]] = True
    return A, X, y, train_mask, test_mask


def normalized_adjacency(A):
    """Symmetric normalization with self-loops: Â = D^-1/2 (A + I) D^-1/2 (Kipf & Welling)."""
    A = np.asarray(A, dtype=float)
    A_tilde = A + np.eye(A.shape[0])
    d_inv_sqrt = 1.0 / np.sqrt(A_tilde.sum(axis=1))
    D = np.diag(d_inv_sqrt)
    return D @ A_tilde @ D


def accuracy(logits, y, mask):
    pred = np.asarray(logits).argmax(axis=1)
    return float((pred[mask] == y[mask]).mean())
