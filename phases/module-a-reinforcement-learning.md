# Module A — Reinforcement Learning (optional, ≈4–5 weeks)

**Goal:** learn agents that act to maximize reward — absent from your exam but core to robotics, game
AI, **RLHF**, and agentic decision-making. Pairs with your **[DQN trading capstone](../capstones/dqn-trading/README.md)**.

**Environment:** **☁️ Colab** / **📊 Kaggle** (a GPU helps for deep RL); tabular methods run **🖥️ Local**.

**🔄 Freshness:** RL libraries (Gymnasium, Stable-Baselines3) update — use **current** docs. The
*theory* (Sutton & Barto) is timeless.

**Primary resources** (open the link, then the **bold** item):
- [Hugging Face — *Deep RL Course*](https://huggingface.co/learn/deep-rl-course) (hands-on, free, certificate) · 🆕 [Vizuara](https://www.youtube.com/@vizuara)
- [OpenAI — *Spinning Up in Deep RL*](https://spinningup.openai.com) · [Sutton & Barto — *RL: An Introduction* (free PDF)](http://incompleteideas.net/book/the-book.html)
- [David Silver — RL Course (DeepMind, YouTube)](https://www.youtube.com/playlist?list=PLqYmG7hTraZDM-OYHWgPebj2MfCFzFObQ) · [Gymnasium (environments)](https://gymnasium.farama.org)

---

## Module A1 — RL foundations (tabular)

| # | Topic | Open exactly this | ~Time |
|---|-------|-------------------|-------|
| 1 | MDPs: states, actions, rewards, policies | [HF Deep RL Course](https://huggingface.co/learn/deep-rl-course) — **Unit 1 "Introduction to RL"** | 1.5h |
| 2 | Value functions & the **Bellman equation** | [Sutton & Barto](http://incompleteideas.net/book/the-book.html) — **Ch.3 "Finite MDPs"** | 1.5h |
| 3 | Dynamic programming: value & policy iteration | [Sutton & Barto](http://incompleteideas.net/book/the-book.html) — **Ch.4 "Dynamic Programming"** | 1.5h |
| 4 | Monte Carlo & **temporal-difference** learning | [Sutton & Barto](http://incompleteideas.net/book/the-book.html) — **Ch.5–6** | 2h |
| 5 | **Q-learning** (tabular) | [HF Deep RL Course](https://huggingface.co/learn/deep-rl-course) — **Unit 2 "Q-Learning"** | 2h |
| 6 | Exploration vs exploitation (ε-greedy) | [Spinning Up](https://spinningup.openai.com/en/latest/spinningup/rl_intro.html) — **"Key concepts"** | 30m |

**✅ Checkpoint A1** — 🖥️ Local — one per topic:
- **(T1)** Define an MDP for a gridworld (states/actions/rewards); what is a policy?
- **(T2)** Write the Bellman equation for the state-value function; explain the discount factor γ.
- **(T3)** Run value iteration on a small gridworld; show the optimal policy.
- **(T4)** Contrast Monte Carlo vs TD updates (when does each update?).
- **(T5)** Implement tabular Q-learning on `FrozenLake` (Gymnasium); show it learns.
- **(T6)** Show how ε affects exploration; decay ε over training.

---

## Module A2 — Deep RL

| # | Topic | Open exactly this | ~Time |
|---|-------|-------------------|-------|
| 7 | **Deep Q-Networks (DQN)**: replay + target net | [HF Deep RL Course](https://huggingface.co/learn/deep-rl-course) — **Unit 3 "Deep Q-Learning"** | 2.5h |
| 8 | **Policy gradients (REINFORCE)** | [Spinning Up](https://spinningup.openai.com/en/latest/algorithms/vpg.html) — **"Vanilla Policy Gradient"** | 1.5h |
| 9 | **Actor-critic (A2C)** | [HF Deep RL Course](https://huggingface.co/learn/deep-rl-course) — **Unit 6 "Actor-Critic"** | 2h |
| 10 | **PPO** (the workhorse, incl. RLHF) | [HF Deep RL Course](https://huggingface.co/learn/deep-rl-course) — **Unit 8 "PPO"** + [Spinning Up PPO](https://spinningup.openai.com/en/latest/algorithms/ppo.html) | 2.5h |
| 11 | Gymnasium + Stable-Baselines3 | [Gymnasium docs](https://gymnasium.farama.org/introduction/basic_usage/) — **"Basic Usage"** + [SB3 docs](https://stable-baselines3.readthedocs.io) | 1.5h |

**✅ Checkpoint A2** — ☁️ Colab/📊 Kaggle — one per topic:
- **(T7)** Train a **DQN** on CartPole; explain why replay + target network stabilize it. 🔨 **[DQN trading capstone](../capstones/dqn-trading/README.md)**.
- **(T8)** Implement REINFORCE; why is it high-variance vs DQN?
- **(T9)** Explain how the critic reduces policy-gradient variance.
- **(T10)** Train PPO with SB3 on a Gym env; one line on how PPO relates to **RLHF** (Phase 6B).
- **(T11)** Wrap a custom environment (e.g. your trading env) in the Gymnasium API.

---

## 🏁 Module A capstone — RL trading agent
Finish the **[DQN trading capstone](../capstones/dqn-trading/README.md)**: linear Q → deep DQN (target
net + ε-decay) → evaluate **out-of-sample** with your **[BYO-15 backtester](../challenges/byo-15-backtester/README.md)**;
compare to buy-and-hold and report honestly (most RL traders lose after costs). Read the **DQN** or
**PPO** paper with your [research-skills](research-skills.md) method.

**You've got RL when** you can explain MDPs/Bellman/Q-learning, implement DQN, and reason about
exploration, variance, and why a replay buffer + target network matter.
