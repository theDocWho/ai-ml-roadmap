# Production AI-Engineering Projects

Portfolio-grade builds where the hard part is **the system around the model**, not the model call.
Each is a *deployable service* — an API + a small UI + an **eval suite** — that you could put on a résumé
and defend in an interview.

> Inspired by Kushal Vijay's *AI Engineering Projects Guide* (15 projects), **re-cut for this roadmap:**
> a curated **core 8** that are ML-relevant and **100% free to build**, plus 7 optional infra extras.

## How this differs from `challenges/` and `capstones/`

| Bucket | What it is | Frameworks? | Goal |
|---|---|---|---|
| [`challenges/`](../challenges/README.md) (BYO) | Build the **engine** from scratch | ❌ no high-level libs | Understand the internals → independence |
| **`projects/`** (here) | Build the **system around** a model | ✅ yes (FastAPI, LangGraph, Chroma…) | Ship a deployable, **evaluated** service |
| [`capstones/`](../capstones/) | Flagship **domain** builds | ✅ yes | Multi-phase portfolio centrepieces |

They reinforce each other: do **BYO-9 (RAG from scratch)** to *understand* retrieval, then
**proj-01 (RAG + verified citations)** to *productionize* it with hybrid search, citation-checking and evals.

## 🆓 Everything here is free

The source guide assumes paid APIs (GPT-4o, Claude) and managed infra. **This track never requires payment.**
Wherever a project needs an LLM, we pick a **free model that is genuinely capable of the task** — not a token
tiny model that quietly degrades quality — and we show **how to push it further, local ↔ cloud**.

### Free-but-capable model reference (shared — briefs point here)

| Task | Free **local** (default) | Free **cloud / API** step-up | Quality lever |
|---|---|---|---|
| Reasoning / judge / agent | **Qwen2.5-7B / 14B** or **Llama-3.1-8B** via Ollama | **Groq**, **Google AI Studio / Gemini (free)**, **OpenRouter** free models, **Cerebras** free | bigger local (Qwen2.5-32B/72B, Llama-3.3-70B) if RAM allows |
| Embeddings | **bge-small/base-en**, **nomic-embed-text** (sentence-transformers / Ollama) | Jina embeddings free tier | add a **bge-reranker** after retrieval |
| Vision / multimodal | **Qwen2-VL**, **Llama-3.2-Vision**, LLaVA via Ollama | **Gemini** free vision tier | OCR (Tesseract/EasyOCR) + vision-LLM cross-check |
| Fine-tuning (GPU) | small QLoRA on CPU/MPS for a smoke test | **Colab** (T4), **Kaggle** (2×T4 / P100, ~30h/wk) free | QLoRA → full LoRA → more data |
| Vector store | **Chroma** / **Qdrant** (local, Docker) | **Qdrant Cloud** 1 GB free, Pinecone free | hybrid (dense + `rank-bm25`) |
| Tracking / serving | **MLflow** local, **Ollama**, **HF Spaces** | **HF Spaces (ZeroGPU)** free GPU serving | vLLM for throughput |
| Metrics / dashboards | **Prometheus + Grafana** (OSS), Streamlit | Grafana Cloud free tier | — |

> **Rule of thumb:** start **local** (private, offline, $0). Reach for a **free cloud tier** only to (a) get a
> stronger judge/generator for evals, (b) borrow a GPU for fine-tuning, or (c) demo a hosted URL. Never pay.

---

## Core 8 — full briefs

| # | Project | Phase | Build (free stack) | Ties to |
|---|---------|-------|--------------------|---------|
| [**proj-01**](proj-01-rag-citations/README.md) | Support copilot with **verified citations** | 6 | Ollama · sentence-transformers · Chroma · `rank-bm25` · RAGAS (local judge) · Gradio · Docker | [BYO-9](../challenges/byo-09-rag/README.md) |
| [**proj-02**](proj-02-nl-to-api/README.md) | **Natural-language → API** assistant | 6 | FastAPI (mock API) · Ollama · Pydantic/OpenAPI · SQLite | [BYO-10](../challenges/byo-10-react-agent/README.md) |
| [**proj-03**](proj-03-guardrail-service/README.md) | AI output **policy guardrail** service | 6B | Presidio (PII) · validators · local-LLM judge · FastAPI | [BYO-16](../challenges/byo-16-llm-redteam/README.md) |
| [**proj-04**](proj-04-finetune-vs-rag/README.md) | **Fine-tune vs RAG** decision lab | 6B | HF PEFT/TRL QLoRA (Colab/Kaggle) · Chroma · MLflow · Ollama | phase-6b |
| [**proj-05**](proj-05-multimodal-intake/README.md) | **Multimodal document intake** reviewer | 6B–7 | Tesseract/EasyOCR · PyMuPDF · Qwen2-VL (Ollama) · Streamlit | — |
| [**proj-06**](proj-06-local-llm-deploy/README.md) | **Local LLM deployment** kit | 7 | vLLM/Ollama/llama.cpp · GGUF/AWQ/GPTQ · FastAPI · Locust · Prometheus/Grafana | phase-6b |
| [**proj-07**](proj-07-eval-as-service/README.md) | **Evaluation-as-a-service** platform | 7–8 | FastAPI · local-LLM judges · scipy calibration · SQLite · Streamlit | phase-7/8 |
| [**proj-08**](proj-08-agent-sandbox/README.md) | **Permissioned tool-using agent** sandbox | 8 | LangGraph · Ollama · permission checks · approval queue · audit log | [BYO-10](../challenges/byo-10-react-agent/README.md)/[13](../challenges/byo-13-multiagent/README.md) |

> Each brief = goal · 🆓 free-stack swap · what you'll build · staged milestones · **Make it better (local ↔ cloud)** ·
> Done-when · concepts to explain · an embedded **[Decision Lens](../templates/decision-lens-template.md)**.

## Optional 7 — infra extras (not full briefs)

LLMOps/platform-flavoured — great portfolio pieces, lighter on *ML*. Ask Claude to **"scaffold the proj brief
for X"** when you reach the listed phase.

- **Prompt Release Safety Gate** — CI/CD regression gate on prompt changes → Phase 7
- **LLM Spend Control Center** — routing + budgets by team/feature → Phase 7/8
- **Production Log-to-Eval Dataset Builder** — mine logs → eval cases (data flywheel) → Phase 7
- **RAG Freshness & Drift Monitor** — stale-doc / retrieval-drift alerts + re-index → Phase 7
- **AI Trace Explorer** — record + visualize multi-step LLM workflow traces → Phase 7/8
- **Semantic Cache Gateway** — serve cached answers for similar requests → Phase 7
- **AI Feature Rollout Monitor** — canary + auto-rollback on quality drop → Phase 7

---

**Related flagship:** [`capstones/car-damage-cost-india`](../capstones/car-damage-cost-india/README.md) —
a production CV × tabular-regression × MLOps build (Indian motor-insurance repair-cost estimation).
