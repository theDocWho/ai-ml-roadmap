# Phase 7 — MLOps & Productionization (≈5–6 weeks)

**Goal:** turn a notebook model into a **deployed, monitored service**. Data pipelines, experiment
tracking, packaging, **REST APIs**, **Docker**, **CI/CD**, and **monitoring/drift**. This is what
separates "did a Kaggle notebook" from "shipped ML."

> 🏗️ **Production projects (this phase):** [Local LLM deployment kit](../projects/proj-06-local-llm-deploy/README.md) ·
> [Evaluation-as-a-service](../projects/proj-07-eval-as-service/README.md) · [Multimodal document intake](../projects/proj-05-multimodal-intake/README.md) ·
> harden the **[car-damage estimator (India)](../capstones/car-damage-cost-india/README.md)** (container + drift). Optional infra extras
> (prompt-safety gate, spend control, log-to-eval, RAG drift monitor, trace explorer, semantic cache, rollout monitor) are in [`projects/`](../projects/README.md).

> 🏛️ **Going further (architect track):** [Phase 9 — AI Solution Architecture](phase-9-architecture.md)
> deepens this into **data architecture** (lakes, streaming, feature stores), **Kubernetes/Terraform**, and
> **FinOps** cost modeling — the design-and-tradeoffs layer above MLOps.

**Environment:** **🖥️ Local** (Docker, FastAPI, CI) + a **free cloud/HF Spaces** deploy target. No GPU
needed for most of it.

**🔄 Freshness:** tools (MLflow, FastAPI, Docker, GitHub Actions) update — use **current** docs;
*principles* (CI/CD, monitoring, drift) are stable (Made With ML / Chip Huyen stay valid).

**Primary resources** (open the link, then the **bold** item):
- [Made With ML](https://madewithml.com) (design→develop→deploy→iterate; the best free production-ML course)
- [MLOps Zoomcamp (DataTalks.Club)](https://github.com/DataTalksClub/mlops-zoomcamp) (free, self-paced) · [Full Stack Deep Learning (free)](https://fullstackdeeplearning.com/course/)
- [Chip Huyen — MLOps guide](https://huyenchip.com/mlops/) · [Google — Rules of ML / MLOps](https://developers.google.com/machine-learning/guides/rules-of-ml)
- 🎨 **[Illustrated explainer](https://thedocwho.github.io/ai-ml-roadmap/illustrated/index.html)** (interactive, offline): [MLOps lifecycle & drift](https://thedocwho.github.io/ai-ml-roadmap/illustrated/7-mlops/mlops-lifecycle.html) — click the loop, then simulate drift, monitoring & auto-retrain.

---

## Module 7A — Data pipelines & experiment tracking

| # | Topic | Open exactly this | ~Time |
|---|-------|-------------------|-------|
| 1 | Reproducible data prep & versioning | [Made With ML](https://madewithml.com) — **"Data → preprocessing / splitting"** | 2h |
| 2 | **Experiment tracking** (MLflow) | [MLflow docs](https://mlflow.org/docs/latest/index.html) — **"MLflow Tracking Quickstart"** | 1.5h |
| 3 | Alternative: Weights & Biases | [W&B docs](https://docs.wandb.ai/quickstart) — **"Quickstart"** | 1h |
| 4 | Config & reproducibility (seeds, params) | [MLOps Zoomcamp](https://github.com/DataTalksClub/mlops-zoomcamp) — **"Experiment tracking"** module | 2h |

**✅ Checkpoint 7A** — 🖥️ Local — one per topic:
- **(T1)** Write a reproducible data-prep script (deterministic split, saved artifacts).
- **(T2)** Track 3 training runs in **MLflow** (params, metrics, model); compare them in the UI.
- **(T3)** Log one run to **W&B**; explain when you'd pick it over MLflow.
- **(T4)** Make a run fully reproducible (fixed seed + logged config); re-run and match the metric.

---

## Module 7B — Packaging & serving

| # | Topic | Open exactly this | ~Time |
|---|-------|-------------------|-------|
| 5 | Package a model (registry, artifacts) | [MLflow Models docs](https://mlflow.org/docs/latest/models.html) — **"Storing and serving models"** | 1h |
| 6 | **REST API with FastAPI** | [FastAPI docs](https://fastapi.tiangolo.com/tutorial/) — **"Tutorial - User Guide"** (first half) | 2h |
| 7 | **Docker** (containerize the service) | [Docker — Get Started](https://docs.docker.com/get-started/) — **"Containerize an application"** | 2h |
| 8 | Batch vs real-time serving | [Chip Huyen — MLOps guide](https://huyenchip.com/mlops/) — **"Model serving"** section | 30m |

**✅ Checkpoint 7B** — 🖥️ Local — one per topic:
- **(T5)** Save + load a model from the MLflow registry; version it.
- **(T6)** Wrap inference in a **FastAPI** `/predict` endpoint; test it with `curl`/`httpx`.
- **(T7)** **Dockerize** the API; run the container; hit the endpoint from the host.
- **(T8)** Decide batch vs real-time for your churn model vs a fraud-scoring stream; justify.

---

## Module 7C — CI/CD & deployment

| # | Topic | Open exactly this | ~Time |
|---|-------|-------------------|-------|
| 9 | **CI/CD with GitHub Actions** | [GitHub Actions docs](https://docs.github.com/en/actions/learn-github-actions) — **"Building and testing Python"** | 2h |
| 10 | Testing ML code (data + model tests) | [Made With ML](https://madewithml.com) — **"Testing"** lesson | 1.5h |
| 11 | Deploy (free targets) | [Hugging Face Spaces — Docker SDK](https://huggingface.co/docs/hub/spaces-sdks-docker) or a free cloud tier | 1.5h |

**✅ Checkpoint 7C** — 🖥️ Local + cloud — one per topic:
- **(T9)** A GitHub Actions workflow that runs `pytest` + builds the Docker image on push.
- **(T10)** Add a **data test** (schema/range) and a **model test** (min accuracy on a fixed set) to CI.
- **(T11)** **Deploy** the Dockerized API to HF Spaces / a free cloud; share the live URL.

---

## Module 7D — Monitoring & drift

| # | Topic | Open exactly this | ~Time |
|---|-------|-------------------|-------|
| 12 | Why models decay; **data/concept drift** | [Evidently AI — docs](https://docs.evidentlyai.com) — **"What is data drift"** | 1h |
| 13 | Monitoring in practice (metrics, alerts) | [Evidently AI](https://docs.evidentlyai.com) — **"Generate a drift report"** | 1.5h |
| 14 | Logging & observability | [MLOps Zoomcamp](https://github.com/DataTalksClub/mlops-zoomcamp) — **"Monitoring"** module | 2h |

**✅ Checkpoint 7D** — 🖥️ Local — one per topic:
- **(T12)** Explain data drift vs concept drift with an example from your domain (fraud/finance).
- **(T13)** Generate an **Evidently** drift report comparing "reference" vs "current" data.
- **(T14)** Add request/prediction logging to your API; describe what you'd alert on in production.

---

## 🏁 Phase 7 capstone — productionize one model end-to-end
Take your **Phase 3 churn model** (or the CV/intrusion model): data pipeline → **MLflow** tracking →
packaged model → **FastAPI** service → **Docker** → **CI/CD** (GitHub Actions) → **deployed** →
**monitoring + drift** (Evidently). Document the full lifecycle in the README — a standout resume item
most candidates lack. Finish **MLOps Zoomcamp** or **Made With ML** for the certificate/portfolio.

**Ready for Phase 8 when** you can take any model from notebook → versioned, tested, deployed,
monitored service — and explain every stage.
