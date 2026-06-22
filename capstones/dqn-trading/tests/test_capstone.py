"""Acceptance tests for the DQN trading capstone."""
import numpy as np
from trading.env import TradingEnv
from trading.buffer import ReplayBuffer
from trading.agent import QLearningAgent


def uptrend(n=200, drift=0.01):
    return 100.0 * np.cumprod(1 + np.full(n, drift))     # strictly increasing prices


# ----- environment (given) -----
def test_env_state_shape_and_reset():
    env = TradingEnv(uptrend(), window=4)
    s = env.reset()
    assert s.shape == (4,)


def test_env_long_profits_short_loses_on_uptrend():
    env = TradingEnv(uptrend(), window=3)
    env.reset()
    _, r_long, _, _ = env.step(1)
    env.reset()
    _, r_short, _, _ = env.step(2)
    assert r_long > 0 and r_short < 0


def test_env_runs_to_done():
    env = TradingEnv(uptrend(50), window=3)
    env.reset()
    steps, done = 0, False
    while not done:
        _, _, done, _ = env.step(0)
        steps += 1
    assert steps == len(env.returns) - env.window


# ----- replay buffer (given) -----
def test_replay_buffer_capacity_and_sample():
    b = ReplayBuffer(capacity=5, seed=0)
    for i in range(10):
        b.add(np.zeros(3), 0, 0.0, np.zeros(3), False)
    assert len(b) == 5
    assert len(b.sample(3)) == 3


# ----- agent (you implement) -----
def test_agent_act_returns_valid_action():
    ag = QLearningAgent(state_dim=3, n_actions=3)
    assert ag.act(np.zeros(3), epsilon=0.0) in (0, 1, 2)


def test_agent_update_reduces_td_error():
    ag = QLearningAgent(state_dim=2, n_actions=3, lr=0.1, seed=0)
    batch = [(np.array([1.0, 0.0]), 1, 1.0, np.array([0.0, 1.0]), True)] * 8
    td0 = ag.update(batch)
    for _ in range(50):
        td = ag.update(batch)
    assert td < td0                       # repeated updates fit the transition


def test_agent_learns_to_beat_random_on_uptrend():
    env = TradingEnv(uptrend(300), window=4)
    ag = QLearningAgent(env.state_dim, env.n_actions, lr=0.05, gamma=0.9, seed=0)
    buf = ReplayBuffer(seed=0)
    for _ in range(20):                   # train
        s = env.reset()
        done = False
        while not done:
            a = ag.act(s, epsilon=0.1)
            ns, r, done, _ = env.step(a)
            buf.add(s, a, r, ns, done)
            if len(buf) >= 32:
                ag.update(buf.sample(32))
            s = ns

    def run(policy):
        s, done, total = env.reset(), False, 0.0
        while not done:
            ns, r, done, _ = env.step(policy(s))
            total += r
            s = ns
        return total

    greedy = run(lambda s: ag.act(s, epsilon=0.0))
    rng = np.random.default_rng(1)
    random_pol = run(lambda s: int(rng.integers(0, 3)))
    assert greedy > random_pol
    assert greedy > 0
