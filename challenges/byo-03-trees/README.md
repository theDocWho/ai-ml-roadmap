# BYO-3 — Build Your Own Decision Tree + Random Forest

> Reinforces: decision trees & overfitting (exam Q11), boosting/ensembles (Q30) · Phase 3 · ⭐⭐⭐
> Build a CART classifier and bag it into a forest — from scratch (NumPy only).

```bash
cd challenges/byo-03-trees
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest tests/ -v
```

## Stages (`trees/engine.py`)

1. **Impurity** — `gini(y)` = 1 − Σ pₖ². Pure node → 0; 50/50 → 0.5.
2. **Best split** — `best_split(X, y)` scans every feature & candidate threshold and returns the
   `(feature, threshold)` that maximizes impurity decrease.
3. **Grow the tree** — `DecisionTree.fit` recurses (respecting `max_depth`, `min_samples`), storing a
   leaf prediction (majority class) when it stops; `predict` walks the tree per row.
4. **Random Forest** — `RandomForest` bags `n_trees` trees on bootstrap samples with a random feature
   subset per split, then predicts by majority vote.

## Done when
`pytest tests/` is green and you can explain *why* an unpruned tree overfits (exam Q11) and how
bagging reduces variance.
