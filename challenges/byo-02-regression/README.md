# BYO-2 — Build Your Own Regression Engine

> Reinforces: RSS/MAE (exam Q9, Q14), gradient descent (Q35) · Phase 2 · ⭐⭐
> You implement linear & logistic regression from scratch (NumPy only) — the two models every ML
> interview assumes you can derive.

```bash
cd challenges/byo-02-regression
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest tests/ -v
```

## Stages (`linreg/engine.py`)

1. **Predict + loss** — `predict(X) = X·w + b`; `mse(y, yhat)`. (exam Q14: RSS = Σ(y−ŷ)²)
2. **Closed form** — `fit_normal_equation`: w = (XᵀX)⁻¹Xᵀy. Recovers an exact line.
3. **Gradient descent** — `fit`: init weights, loop `n_iters` doing `w -= lr·∂MSE/∂w`. Loss must drop
   and converge near the closed-form solution.
4. **Regularization + logistic** — add **L2** (ridge) and **L1** (lasso) penalties; implement
   `LogisticRegression` (sigmoid + binary cross-entropy) that separates a 2-class set.

## Done when
`pytest tests/` is green and you can derive the MSE gradient (`2/n · Xᵀ(Xw − y)`) on paper.
