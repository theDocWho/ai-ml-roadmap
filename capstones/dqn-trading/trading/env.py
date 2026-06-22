"""A minimal Gym-style trading environment (provided, fully implemented).

State  = the last `window` returns (what you knew before acting).
Actions= 0 flat, 1 long (+1), 2 short (-1).
Reward = position * next_return - fee * |position change|.   (No look-ahead: you act, THEN the
         next return is realized.)

ANALYSIS / RESEARCH ONLY — this is a simulator, not a broker. Never wire it to live trading.
"""
import numpy as np

_POS = {0: 0, 1: 1, 2: -1}


class TradingEnv:
    def __init__(self, prices, window=5, fee=0.0):
        self.prices = np.asarray(prices, dtype=float)
        self.returns = self.prices[1:] / self.prices[:-1] - 1.0
        self.window = window
        self.fee = fee
        self.n_actions = 3
        self.state_dim = window
        self.reset()

    def reset(self):
        self.t = self.window           # index into self.returns
        self.position = 0
        return self._state()

    def _state(self):
        return self.returns[self.t - self.window:self.t].copy()

    def step(self, action):
        new_pos = _POS[action]
        reward = new_pos * self.returns[self.t] - self.fee * abs(new_pos - self.position)
        self.position = new_pos
        self.t += 1
        done = self.t >= len(self.returns)
        next_state = self._state() if not done else np.zeros(self.window)
        return next_state, float(reward), done, {}
