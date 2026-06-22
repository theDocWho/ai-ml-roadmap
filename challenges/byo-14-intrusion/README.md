# BYO-14 — Build Your Own Intrusion / Anomaly Detector

> Reinforces: anomaly detection, evaluation metrics (exam Q23) · Phase 3–4 · cybersecurity track · ⭐⭐⭐
> Train only on **normal** traffic, then flag anything unlike it — the core of unsupervised
> network-intrusion detection (NSL-KDD / CIC-IDS). NumPy only.

```bash
cd challenges/byo-14-intrusion
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest tests/ -v
```

## Stages (`ids/engine.py`)

1. **Standardize** — z-score features (fit stats on train, reuse on test). Distance-based methods
   need comparable scales.
2. **Anomaly score** — `KNNAnomalyDetector.score_samples`: mean Euclidean distance to the *k*
   nearest training points. Attacks sit far from the normal cluster → high score.
3. **Threshold + predict** — set a threshold from the `(1 − contamination)` quantile of training
   scores; flag points above it.
4. **Evaluation** — `precision_recall` and `roc_auc` (Mann-Whitney rank formula). On injected
   anomalies you should reach recall > 0.95 and AUC > 0.99.

## Real next step
Swap the synthetic data for **NSL-KDD** or **CIC-IDS2017** (https://www.unb.ca/cic/datasets/),
keep the same pipeline, and write up precision/recall/ROC — a strong cyber-portfolio piece.

## Done when
`pytest tests/` is green and you can explain why training on only-normal data detects *novel*
attacks an unsupervised model has never seen.
