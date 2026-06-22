"""BYO-15 starter — a from-scratch vectorized backtesting engine (NumPy only).

ANALYSIS ONLY. This computes the historical performance of a signal — it never connects to a
broker and never executes trades. Backtests overstate live results; always lag your signal to
avoid look-ahead and charge fees on turnover. See README.md.
"""
import numpy as np


def simple_returns(prices):
    """Stage 1: period returns r[t] = prices[t+1]/prices[t] - 1. Length len(prices)-1."""
    raise NotImplementedError("implement simple_returns")


def sharpe(returns, periods_per_year=252):
    """Stage 1: annualized Sharpe = mean(returns)/std(returns) * sqrt(periods_per_year).
    Return 0.0 if std is 0 (guard tiny floating-point std, e.g. < 1e-12, as zero too)."""
    raise NotImplementedError("implement sharpe")


def max_drawdown(equity):
    """Stage 1: most negative (equity - running_peak)/running_peak. Returns a value <= 0."""
    raise NotImplementedError("implement max_drawdown")


class Backtester:
    def __init__(self, fee=0.0):
        self.fee = fee          # cost per unit of turnover (|position change|)

    def run(self, prices, signal):
        """Stages 2-4. `signal[t]` is the position decided using info up to time t (so it is held
        over the return from t to t+1 — this LAG is what prevents look-ahead).

        asset_ret = simple_returns(prices)              # length N-1
        pos       = signal[:-1]                         # position over each return period
        turnover  = |pos[t] - pos[t-1]|  (pos[-1] := 0 at the start)
        strat_ret = pos * asset_ret - fee * turnover
        equity    = cumprod(1 + strat_ret)

        Return a dict with keys: 'returns', 'equity', 'total_return' (equity[-1]-1),
        'sharpe' (of strat_ret), 'max_drawdown' (of equity).
        """
        raise NotImplementedError("implement Backtester.run")
