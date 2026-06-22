"""Experience replay buffer (provided, fully implemented)."""
import random
from collections import deque


class ReplayBuffer:
    def __init__(self, capacity=10000, seed=0):
        self.buf = deque(maxlen=capacity)
        self.rng = random.Random(seed)

    def add(self, state, action, reward, next_state, done):
        self.buf.append((state, action, reward, next_state, done))

    def sample(self, batch_size):
        return self.rng.sample(self.buf, min(batch_size, len(self.buf)))

    def __len__(self):
        return len(self.buf)
