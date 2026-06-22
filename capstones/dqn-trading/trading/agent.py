"""The RL agent — THIS is what you implement (the env and buffer are given).

Start with this linear Q-learning agent (a "DQN" with a linear Q-network). Once the tests pass,
the README shows how to grow it into a real deep DQN (a neural-net Q-function + target network).
"""
import numpy as np


class QLearningAgent:
    def __init__(self, state_dim, n_actions, lr=0.01, gamma=0.95, seed=0):
        self.rng = np.random.default_rng(seed)
        # linear Q-network: a weight row per action, plus a bias column
        self.W = self.rng.normal(0, 0.01, (n_actions, state_dim + 1))
        self.n_actions = n_actions
        self.lr = lr
        self.gamma = gamma

    def _feat(self, state):
        return np.append(np.asarray(state, dtype=float), 1.0)      # append bias term

    def q_values(self, state):
        """TODO: return the Q-value for each action = W @ [state, 1] (length n_actions)."""
        raise NotImplementedError("implement q_values")

    def act(self, state, epsilon=0.0):
        """TODO: epsilon-greedy: with prob epsilon pick a random action (self.rng.integers),
        otherwise argmax of q_values(state). Return an int action."""
        raise NotImplementedError("implement act")

    def update(self, batch):
        """TODO: semi-gradient Q-learning over a batch of (s, a, r, ns, done):
            target = r                        if done
                   = r + gamma * max_a' Q(ns, a')   otherwise
            td     = target - Q(s)[a]
            W[a]  += lr * td * feat(s)
        Return the mean |td| over the batch (a useful training signal)."""
        raise NotImplementedError("implement update")
