# BYO-15 — Build Your Own Backtesting Engine

> Reinforces: time-series, risk/return metrics · Phase 3 · finance track · ⭐⭐⭐
> Build a vectorized backtester from scratch (NumPy only) and learn why most backtests lie.

> **Analysis only.** This measures a signal's *historical* performance. It never connects to a
> broker or places an order. Real results differ — fees, slippage, and look-ahead all matter.

```bash
cd challenges/byo-15-backtester
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest tests/ -v
```

## Stages (`backtester/engine.py`)

1. **Building blocks** — `simple_returns`, annualized `sharpe` (guard zero-vol), `max_drawdown`.
2. **Buy & hold** — `Backtester.run` with an all-ones signal must reproduce the raw price change.
3. **No look-ahead** — the signal is **lagged** one step (you trade on what you knew, not the
   future). A signal that turns on *at* a jump must not capture that jump.
4. **Fees on turnover** — charge `fee * |position change|`; churny signals must underperform.

## Real next step
Feed real data with **`yfinance`** (https://github.com/ranaroussi/yfinance), code a strategy
(e.g. moving-average crossover), and produce an honest tear sheet (Sharpe, drawdown, turnover).
Then graduate to **Backtrader** / **vectorbt** for realism.

## Done when
`pytest tests/` is green and you can explain look-ahead bias and why turnover costs sink many
"profitable" strategies.
