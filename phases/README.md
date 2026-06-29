# Detailed Phase Guides — topic → resource → exercise

The [main roadmap](../ROADMAP.md) is the map; these guides are the turn-by-turn directions.

**The problem these solve:** a course or YouTube playlist has its *own* flow and will happily take
you on tangents that don't serve this roadmap. So for **every topic** below you get the **exact
video / chapter / article** (with a link) that covers *just that topic* — open that, then move on.
After each cluster there's a **✅ Checkpoint** with exercises so you can prove you understood it.

## How to use a phase guide
1. Go top-to-bottom. Each row = one topic + the single best free resource (linked, by exact title).
2. Open only what the row points to (don't binge the whole course).
3. At each **✅ Checkpoint**, do the exercises *without looking things up*. If you can't, re-watch
   that cluster's resources. Each checkpoint is tagged with **where** to do it (see below).

## Coverage principle (important)
**Every topic in a module has at least one checkpoint exercise.** The 50 exam questions cover only a
*subset* of the field, so exercises deliberately go beyond them — including topics tagged *(beyond the
exam)*. If a topic is taught, there is a question that tests it. Checkpoint items are numbered to the
topic they verify (e.g. "(T8)" = topic 8 in that module).

## How links & freshness work
- A resource link points to the **playlist / site / doc root**; the **bold title** is the exact video,
  chapter, or article to open inside it. (Titles stay stable even when individual video URLs change.)
- 📖 **Read companion:** every topic gives you at least one *written* resource (official docs, a free
  book, or a high-quality article) — look for the **📖** marker next to a row. Where the primary link is
  a video, the 📖 read covers the **same topic** in text, so you can learn by reading instead of (or as
  well as) watching. 🎨 marks an interactive [illustrated explainer](https://thedocwho.github.io/ai-ml-roadmap/illustrated/index.html).
- **Freshness rule:** for fast-moving tools (Python, NumPy/Pandas, PyTorch, LLM libraries) always use
  the **latest stable docs/version** — links go to "current" docs (e.g. Python **3.12+**). For
  **timeless** material (math, core stats, classic algorithms) an older-but-excellent reference is
  fine — it won't be "updated" because the content doesn't change. If a topic's best resource ever
  goes stale, the guide will say so.
- 🆕 **Vizuara** (https://www.youtube.com/@vizuara) is an excellent, current channel for ML/DL/LLM
  "from scratch" — referenced throughout as a strong alternative/supplement.

## Working environments — where to do the exercises (set this up once)

Each checkpoint is tagged: **🖥️ Local**, **☁️ Colab**, or **📊 Kaggle**. Rule of thumb:
- **Phases 0–3 → 🖥️ Local** (fast iteration, real tooling, your `git` repo).
- **Phases 4–6B (deep learning / LLMs) → ☁️ Colab or 📊 Kaggle** when you need a **free GPU**.
- **Data-heavy / competitions → 📊 Kaggle** (datasets + GPU/TPU already attached).

**🖥️ Local — set up once (recommended default):**
```bash
# install Python 3.12+ (python.org or `brew install python`), then per project:
python3 -m venv .venv && source .venv/bin/activate    # Windows: .venv\Scripts\activate
pip install numpy pandas matplotlib seaborn scikit-learn jupyter pytest
jupyter notebook        # or use VS Code's notebook support
```
**☁️ Google Colab** (no install, free GPU): open https://colab.research.google.com → New notebook →
*Runtime ▸ Change runtime type ▸ GPU* → verify with `!nvidia-smi`. Mount Drive to save work.
**📊 Kaggle Notebooks** (datasets + free GPU/TPU): https://www.kaggle.com/code → New Notebook →
*Add Data* to attach a dataset → *Settings ▸ Accelerator ▸ GPU*.

> Tip: keep your code in the **git repo** (this folder) even when you train on Colab/Kaggle — develop
> locally, push, then `!git clone` your repo into the Colab/Kaggle session for the GPU run.

## 🎨 Illustrated, interactive explainers
For visual intuition, see [`../illustrated/`](https://thedocwho.github.io/ai-ml-roadmap/illustrated/index.html) — **22 interactive** explainers we
built, spanning every phase: Python (mutability, truthiness, comprehensions), the NumPy/Pandas stack
(broadcasting, axis, indexing, DataFrames, GroupBy), classic ML/DL (k-means, backprop, optimizers,
LSTM/GRU), transformers (self-attention), the modern LLM stack (BPE, decoding, LoRA/quant, RAG, ReAct
agents, vector search, embeddings, prompt injection), and MLOps — **plus curated links** to the best
existing ones (Illustrated Transformer, CNN Explainer, MLU-Explain, R2D3, Setosa, Seeing Theory…). Fully
offline, no dependencies. Topic rows across the guides link to these with a 🎨 marker.

## 🏗️ Production AI-engineering projects
Beyond the from-scratch [`../challenges/`](../challenges/README.md) (build the *engine*), the
[**`../projects/`**](../projects/README.md) track has you build the **deployable system around a model** —
RAG with verified citations, guardrails, agent sandboxes, evals-as-a-service, local LLM serving. A curated
**core 8** (+ 7 optional infra extras), **100% free** (every paid LLM swapped for a free-but-capable one, with
a "make it better — local ↔ cloud" path). Do them in **Phases 6 → 8**; topic rows link to them with a 🏗️ marker.
The insurance/CV flagship — a **[car-damage repair-cost estimator (India)](../capstones/car-damage-cost-india/README.md)**
— lives in [`../capstones/`](../capstones/) and spans Phases 3, 4 and 7.

## 🏛️ AI Solution Architecture (optional architect track)
After Phases 6–8, **[Phase 9](phase-9-architecture.md)** takes you from *engineer* to *architect*: data &
infra architecture, system-design (diagrams, **ADRs**, build-vs-buy), scale/reliability/**FinOps**, and
**governance** (NIST AI RMF, EU AI Act, Well-Architected). It produces **deliverables, not code** — assembled
in the **[AI-solution-architecture capstone](../capstones/ai-solution-architecture/README.md)** into a design
package for a system you already built. Reusable artifact templates (ADR, decision-matrix, cost-model,
governance checklist) live in [`../templates/`](../templates/).

## Guides
| Phase | Guide | Status |
|-------|-------|--------|
| 0 | [Python for a Java dev](phase-0-python.md) | ✅ |
| 1 | [Scientific Python stack + plotting](phase-1-scientific-stack.md) | ✅ |
| 2 | [Math foundations (visual-first)](phase-2-math.md) | ✅ |
| 3 | [Classic Machine Learning](phase-3-classic-ml.md) | ✅ |
| 4 | [Deep Learning foundations](phase-4-deep-learning.md) | ✅ |
| 5 | [NLP + Transformers](phase-5-nlp-transformers.md) | ✅ |
| 6 | [LLMs, RAG & Agents](phase-6-llms-rag-agents.md) | ✅ |
| 6B | [LLM in-depth](phase-6b-llm-indepth.md) | ✅ |
| 7 | [MLOps & Productionization](phase-7-mlops.md) | ✅ |
| 8 | [Agentic systems + Interview readiness](phase-8-agentic-interview.md) | ✅ |
| 9 | [AI Solution Architecture *(optional — architect track)*](phase-9-architecture.md) | ✅ |
| — | [**Research skills: reading, verifying & writing papers**](research-skills.md) | ✅ |

### Optional specialization modules (pick by interest / target role)
| Module | Guide | Pairs with capstone | Status |
|--------|-------|---------------------|--------|
| A | [Reinforcement Learning](module-a-reinforcement-learning.md) | [DQN trading](../capstones/dqn-trading/README.md) | ✅ |
| B | [Diffusion & Generative Vision](module-b-diffusion.md) | image generator (build) | ✅ |
| C | [Graph Neural Networks](module-c-gnn.md) | [GNN fraud](../capstones/gnn-fraud/README.md) | ✅ |
