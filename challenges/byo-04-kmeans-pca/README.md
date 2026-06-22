# BYO-4 — Build Your Own K-Means + PCA

> Reinforces: eigenvalues (exam Q10), PCA as feature extraction (Q18), k-means (Q31) · Phase 2–3 · ⭐⭐
> Two unsupervised workhorses, from scratch (NumPy only).

```bash
cd challenges/byo-04-kmeans-pca
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest tests/ -v
```

## Stages (`cluster/engine.py`)

1. **K-Means assign/update** — `fit`: init `k` centroids, then loop {assign each point to nearest
   centroid; move each centroid to its members' mean} until stable. Store `labels_`, `centroids_`,
   `inertia_` (sum of squared distances to assigned centroid).
2. **k-means++ init** — seed centroids spread out (distance-weighted) for better convergence.
3. **PCA fit** — mean-center, compute the covariance matrix, take its **eigenvectors** (the link to
   exam Q10), keep the top `n_components` by eigenvalue; store `explained_variance_ratio_`.
4. **PCA transform / inverse** — project data onto components and reconstruct it.

## Done when
`pytest tests/` is green and you can explain why PCA's components are the eigenvectors of the
covariance matrix, and why k-means only reaches a *local* optimum (exam Q31).
