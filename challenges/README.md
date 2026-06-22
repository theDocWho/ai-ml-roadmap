# Build-Your-Own AI — challenge series

Free, CodeCrafters-style, staged & test-driven builds — but for **ML / DL / RAG / agents**.
Each challenge is a folder with a `README.md` (staged spec), a starter package with TODOs, and
`pytest` acceptance tests that define the contract. Implement until the tests go green.

**Philosophy:** the core logic is hand-built (no high-level libraries) so you understand the
internals — this is what makes you *independent* of tools and able to ace interviews.

| ID | Build Your Own… | Reinforces (exam Q) | Phase | Status |
|----|-----------------|---------------------|-------|--------|
| **BYO-1** | Autograd engine (micrograd-style) | Backprop Q27/Q34 | 0–1 | ✅ scaffolded (`byo-01-autograd/`) |
| BYO-2 | Regression engine (GD, L1/L2, logistic) | RSS/MAE Q9/Q14/Q35 | 2 | ✅ scaffolded (`byo-02-regression/`) |
| BYO-3 | Decision Tree + Random Forest | Trees/boosting Q11/Q30 | 3 | ✅ scaffolded (`byo-03-trees/`) |
| BYO-4 | K-Means + PCA | Q10/Q18/Q31 | 2–3 | ✅ scaffolded (`byo-04-kmeans-pca/`) |
| BYO-5 | Mini-PyTorch framework | Q26–Q39 | 4 | ✅ scaffolded (`byo-05-minitorch/`) |
| BYO-6 | CNN from scratch | Q44/Q45 | 4 | ✅ scaffolded (`byo-06-cnn/`) |
| BYO-7 | BPE tokenizer (minBPE-style) | LLM prep | 5 | ✅ scaffolded (`byo-07-bpe/`) |
| BYO-8 | Mini-GPT (char transformer) | Q46/Q47 | 5 | ✅ scaffolded (`byo-08-minigpt/`) |
| BYO-9 | RAG engine from scratch (no LangChain) | RAG | 6 | ✅ scaffolded (`byo-09-rag/`) |
| BYO-10 | ReAct agent | Agents | 6 | ✅ scaffolded (`byo-10-react-agent/`) |
| BYO-11 | Vector database (ANN) | systems depth | 6 | ✅ scaffolded (`byo-11-vectordb/`) |
| BYO-12 | Autoencoder → VAE → tiny GAN | Q41/Q48–Q50 | 4–6 | ✅ scaffolded (`byo-12-generative/`) |
| BYO-13 | Multi-agent orchestrator | agentic design | 8 | ✅ scaffolded (`byo-13-multiagent/`) |
| BYO-14 | Intrusion / anomaly detector (from scratch) | cyber, metrics Q23 | 3–4 | ✅ scaffolded (`byo-14-intrusion/`) |
| BYO-15 | Backtesting engine (from scratch) | finance | 3 | ✅ scaffolded (`byo-15-backtester/`) |
| BYO-16 | LLM red-team probe (prompt injection) | LLM security | 6B | ✅ scaffolded (`byo-16-llm-redteam/`) |

> **Start here:** [`byo-01-autograd/`](byo-01-autograd/README.md) is fully scaffolded with stages
> and tests. Ask Claude to "scaffold BYO-N" to generate any of the others the same way when you
> reach its phase.

## Stage outlines (for the not-yet-scaffolded challenges)

- **BYO-2 Regression engine** — `predict` → MSE & cross-entropy loss → batch gradient descent →
  L1/L2 regularization → mini-batch SGD → metrics (MAE/RMSE/R²). Tests vs a closed-form solution.
- **BYO-3 Decision Tree + RF** — Gini/entropy → best split search → recursive `fit` → `predict` →
  bagging → random feature subsets → forest vote. Tests on a separable toy set + accuracy floor.
- **BYO-4 K-Means + PCA** — distances → assignment → centroid update → convergence → k-means++ init;
  PCA: mean-center → covariance → eigh → project/reconstruct. Tests: known clusters; variance retained.
- **BYO-5 Mini-PyTorch** — `Tensor` w/ autograd (extend BYO-1 to arrays) → `Linear`/`ReLU`/`Softmax`
  → cross-entropy → SGD & Adam → train on MNIST subset to a target accuracy.
- **BYO-6 CNN** — `conv2d` forward → `maxpool` → flatten → conv backprop (im2col ok) → train a tiny
  classifier. Tests: gradient check on conv; accuracy on a small set.
- **BYO-7 BPE tokenizer** — byte vocab → pair-frequency counts → iterative merges → `encode`/`decode`
  round-trip → train on a text file. Tests: round-trip identity; known merges.
- **BYO-8 Mini-GPT** — token + positional embeddings → scaled dot-product attention → multi-head →
  block (residual + LayerNorm + MLP) → train char-level; loss decreases; sampling produces text.
- **BYO-9 RAG engine** — loader/chunker → embeddings (call a free model) → cosine top-k search →
  prompt assembly w/ context → LLM call → citations → a tiny eval (hit@k / faithfulness). No LangChain.
- **BYO-10 ReAct agent** — tool registry → tool-described prompt → parse `Action/Action Input` →
  execute → feed `Observation` back → stop on `Final Answer` → add scratchpad memory. Tests w/ mock tools.
- **BYO-11 Vector DB** — add/store vectors → brute-force cosine search → an ANN index (IVF or HNSW-lite)
  → persistence to disk. Tests: recall vs brute force; round-trip after reload.
- **BYO-12 AE → VAE → GAN** — autoencoder reconstruct → VAE reparameterization + KL term → minimal
  GAN generator/discriminator loop. Tests: reconstruction error drops; shapes/loss sanity.
- **BYO-13 Multi-agent orchestrator** — agent base class → message bus → roles (planner/worker/critic)
  → shared memory/state → evaluation loop / stopping. Tests w/ mock agents reaching a goal state.
- **BYO-14 Intrusion / anomaly detector** *(cyber)* — feature extraction → a from-scratch anomaly
  score (k-NN distance or isolation-style) → threshold selection → precision/recall/ROC-AUC on
  NSL-KDD/CIC-IDS. Tests: separable injected anomalies; metric floors.
- **BYO-15 Backtesting engine** *(finance)* — price feed → strategy signal → position sizing → PnL &
  returns → metrics (Sharpe, max drawdown, win rate) with fees/slippage. Tests vs a hand-computed
  buy-and-hold and a known signal. *Analysis only — never auto-executes trades.*
- **BYO-16 LLM red-team probe** *(LLM security, optional)* — a prompt-injection corpus → attack
  runner against your RAG app → a simple detector → an OWASP-LLM-Top-10-style report. Tests with
  mock model responses.
