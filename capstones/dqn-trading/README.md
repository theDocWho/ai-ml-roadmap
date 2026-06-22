# Capstone — Deep Q-Learning Trading Agent (RL × Finance)

> Optional Module A (Reinforcement Learning) × your finance track · ⭐⭐⭐⭐
> A reinforcement-learning agent that learns a trading policy in a market simulator. The
> environment and replay buffer are **given**; you implement the **agent** (Q-learning → DQN), then
> grow it into a real deep DQN and evaluate it honestly.

> **Research/analysis only.** This is a simulator. Never connect it to a broker or live orders.
> A backtest/sim that looks profitable usually isn't — account for fees, slippage, and regime change.

```bash
cd capstones/dqn-trading
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest tests/ -v
```

## What's provided vs what you build

| Given (read it) | You implement |
|---|---|
| `trading/env.py` — Gym-style market env (state = recent returns; actions flat/long/short; no look-ahead) | `trading/agent.py` — `q_values`, `act` (ε-greedy), `update` (semi-gradient Q-learning) |
| `trading/buffer.py` — experience replay | the training loop tweaks (ε schedule, γ, lr) |

## Stages
1. **Linear Q-agent** — implement `q_values` / `act` / `update`; pass the tests (the agent learns to
   go long on an up-trend and beats a random policy).
2. **Make it a *deep* Q-network** — swap the linear `W` for a small MLP Q-function. Reuse your
   **BYO-5 mini-PyTorch** autograd (or PyTorch). Add a **target network** and ε-decay for stability.
3. **Real data + honest evaluation** — load prices with **`yfinance`**, train on one period, **test
   out-of-sample**, and evaluate with your **BYO-15 backtester** (Sharpe, max-drawdown, turnover).
   Compare against buy-and-hold — most RL traders lose to it after costs. Report that truthfully.

## Why this is a strong portfolio piece
It shows RL (MDP, Q-learning, replay, ε-greedy, deep function approximation), finance modeling, and
the maturity to evaluate out-of-sample and not overclaim — exactly what interviewers probe.

## Concepts to be able to explain
MDP / state-action-reward, the Bellman target, why a replay buffer + target network stabilize DQN,
exploration vs exploitation (ε-greedy), and overfitting/look-ahead in financial RL.
