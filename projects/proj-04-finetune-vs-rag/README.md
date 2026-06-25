# proj-04 — Fine-Tune vs RAG Decision Lab

> Reinforces: LoRA/QLoRA · RAG · benchmarking · model selection · Phase 6B · ⭐⭐⭐⭐
> For one task, build **three** variants — prompt-only, RAG, and **LoRA fine-tune** — and produce the
> evidence that says which to ship. The most-asked senior question is *"would you fine-tune or RAG this?"*;
> this project lets you answer with numbers, not vibes.

## 🆓 Free stack (vs the paid version)

| The guide says (paid) | Use this (free, capable) |
|---|---|
| (paid GPUs) | **Colab (T4)** / **Kaggle (2×T4 / P100, ~30h/wk)** free GPU |
| GPT-4o / Claude (baseline) | **Llama-3.1-8B / Mistral-7B / Phi** via **Ollama** + **HF PEFT/TRL** |
| W&B (paid) | **MLflow** local (or W&B free tier) |
| Qdrant Cloud | **Chroma** local |

## What you'll build
A reproducible benchmark harness that runs the **same eval set** through (A) prompt-only, (B) RAG, (C) QLoRA
fine-tune — and reports quality, latency, and cost/effort side by side, with a written recommendation.

## Stages
1. **Task & data** — pick a narrow task (e.g. classify/structure support tickets, answer domain FAQs). Curate
   **500–1,500 examples** with a held-out test split.
2. **Baseline (prompt-only)** — best zero/few-shot prompt; record quality + latency. You must beat this.
3. **RAG variant** — index a knowledge source; same model + retrieved context; measure the lift.
4. **LoRA fine-tune** — **QLoRA** on free Colab/Kaggle GPU; track runs in MLflow; serve the adapter via Ollama/vLLM.
5. **Comparison & recommendation** — one table: quality / latency / build-effort / update-cost; write *when each
   wins* (RAG for fresh/changing knowledge; fine-tune for format/behavior/latency; prompt for quick wins).

## Dataset / inputs
500–1,500 task examples (HF datasets or your own), with a frozen test set used identically across all three.

## Make it better — local ↔ cloud
- **(local)** try rank-fusion RAG; sweep LoRA rank/target-modules; quantize the merged model (GGUF) and re-measure latency.
- **(free cloud)** longer fine-tunes on **Kaggle**; a stronger **free-tier judge** for grading open-ended outputs;
  serve the adapter on **HF Spaces (ZeroGPU)**.

## Done when
- [ ] All three variants evaluated on the **same** held-out set.
- [ ] A single comparison table (quality / latency / effort / update-cost).
- [ ] A written, defensible recommendation ("fine-tune because… / RAG because…").
- [ ] The fine-tune is reproducible from a logged MLflow run.

## Concepts to be able to explain
What LoRA/QLoRA change (low-rank adapters, 4-bit base) and why they're cheap; fine-tune vs RAG trade-offs
(freshness, format control, latency, cost); why you freeze the test set; how you'd grade open-ended answers fairly.

## Decision Lens (filled)
1. **Problem:** choose the right adaptation strategy for a specific task, with evidence.
2. **Is ML right?** It *is* the ML decision — the lens is which ML approach, justified by data.
3. **Framing:** controlled benchmark across 3 methods. Baseline = prompt-only (must be beaten by ≥X).
4. **Data reality:** 500–1,500 examples; watch label noise + test leakage into the fine-tune set.
5. **Metric:** task quality (F1/accuracy/judge-score) **plus** latency & update-cost — single decision can't ignore ops.
6. **Cost of wrong:** picking fine-tune for fast-changing knowledge = stale answers; picking RAG for strict format = inconsistency.
7. **Path to prod:** the chosen variant → proj-06 (serving) / Phase 7.
8. **Build vs leverage:** leverage PEFT/TRL; **the apples-to-apples harness is the deliverable** interviewers respect.
