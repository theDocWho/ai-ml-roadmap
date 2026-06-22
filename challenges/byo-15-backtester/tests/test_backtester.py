"""Staged acceptance tests for BYO-15."""
import numpy as np
from backtester.engine import simple_returns, sharpe, max_drawdown, Backtester


# ----- Stage 1: building blocks -----
def test_stage1_simple_returns():
    assert np.allclose(simple_returns([100, 110, 99]), [0.1, -0.1])


def test_stage1_max_drawdown():
    # peak 1.2 -> trough 0.6 => (0.6-1.2)/1.2 = -0.5
    assert np.isclose(max_drawdown([1.0, 1.2, 0.9, 1.0, 0.6]), -0.5)


def test_stage1_sharpe_zero_vol_is_zero():
    assert sharpe(np.full(10, 0.5)) == 0.0     # constant returns -> no volatility


def test_stage1_sharpe_positive_for_noisy_uptrend():
    rng = np.random.default_rng(0)
    r = 0.01 + 0.005 * rng.normal(size=200)
    assert sharpe(r) > 0


# ----- Stage 2: buy and hold -----
def test_stage2_buy_and_hold_matches_price_change():
    prices = np.array([100, 101, 102, 99, 105], dtype=float)
    res = Backtester(fee=0.0).run(prices, np.ones(len(prices)))
    assert np.isclose(res["total_return"], prices[-1] / prices[0] - 1)


# ----- Stage 3: no look-ahead -----
def test_stage3_no_lookahead():
    # the jump happens between index 1 and 2; a signal that turns on AT index 2 must NOT capture it
    prices = np.array([100, 100, 200, 200], dtype=float)
    signal = np.array([0, 0, 1, 1], dtype=float)     # pos = signal[:-1] = [0, 0, 1]
    res = Backtester(fee=0.0).run(prices, signal)
    assert np.isclose(res["total_return"], 0.0)


# ----- Stage 4: fees on turnover -----
def test_stage4_fees_reduce_return():
    prices = np.array([100, 101, 100, 101, 100, 101], dtype=float)
    churn = np.array([1, 0, 1, 0, 1, 0], dtype=float)   # high turnover
    no_fee = Backtester(fee=0.0).run(prices, churn)["total_return"]
    with_fee = Backtester(fee=0.01).run(prices, churn)["total_return"]
    assert with_fee < no_fee


def test_stage4_result_keys():
    res = Backtester().run(np.array([100.0, 101.0, 102.0]), np.array([1.0, 1.0, 1.0]))
    for key in ("returns", "equity", "total_return", "sharpe", "max_drawdown"):
        assert key in res
