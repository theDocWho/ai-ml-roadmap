# proj-06 — Local LLM Deployment Kit

> Reinforces: serving · quantization · benchmarking · monitoring · Phase 7 (×6B) · ⭐⭐⭐
> Run an open model behind an **OpenAI-compatible API**, benchmark it across **quantization levels**, and wrap
> it in monitoring. This is the "I can actually *operate* an LLM, not just call one" project — directly the
> Phase 6B serving topics made production-real.

## 🆓 Free stack (vs the paid version)

| The guide says (paid) | Use this (free, capable) |
|---|---|
| (paid inference) | **vLLM** / **Ollama** / **llama.cpp** — all free |
| (proprietary models) | **Llama-3.1 / Mistral / Qwen2.5 / Phi** (open weights) |
| (managed monitoring) | **Prometheus + Grafana** (OSS) |
| — | **GGUF / AWQ / GPTQ** quant · **FastAPI** wrapper · **Locust** load test · Docker |

## What you'll build
A deployable kit: an OpenAI-compatible endpoint serving an open model, a **benchmark harness** (latency,
tokens/sec, memory) across quantization levels, a small **quality eval** so you can see the quant→quality
trade-off, and Prometheus/Grafana dashboards + a rollback path.

## Stages
1. **Serving path** — stand up the model on **Ollama** (easy) and **vLLM/llama.cpp** (throughput); expose an
   OpenAI-compatible `/v1/chat/completions`.
2. **Benchmark harness** — measure latency p50/p95, tokens/sec, and RAM/VRAM at **fp16 vs 8-bit vs 4-bit (GGUF/AWQ/GPTQ)**.
3. **Quality eval** — run a fixed eval set at each quant level; chart the **quality-vs-size/speed** curve.
4. **Monitoring & rollback** — Prometheus metrics (latency, error rate, throughput) → Grafana; a documented
   rollback to the last-good model/quant.
5. **Package** — `docker compose up` brings up model + API + dashboards; a README "ops runbook."

## Dataset / inputs
A small fixed eval set (50–100 prompts) reused across quant levels; Locust scenarios for load.

## Make it better — local ↔ cloud
- **(local)** add **continuous batching** (vLLM) and a **semantic cache** for throughput; try speculative decoding.
- **(free cloud)** serve on **HF Spaces (ZeroGPU)** for a public URL; push metrics to **Grafana Cloud free tier**.

## Done when
- [ ] OpenAI-compatible endpoint works from a plain client.
- [ ] A table/chart of latency · tokens/sec · memory · quality across ≥3 quant levels.
- [ ] Grafana shows live latency/throughput; rollback is documented + tested.
- [ ] Whole stack starts with one compose command.

## Concepts to be able to explain
What quantization trades (bits → memory/speed vs quality); GGUF vs AWQ vs GPTQ; why p95 latency and tokens/sec
matter more than p50; continuous batching; when local serving beats an API (privacy, cost, latency).

## Decision Lens (filled)
1. **Problem:** serve an LLM yourself with predictable latency, cost, and privacy.
2. **Is ML right?** N/A — this is the *ops* around a model; the decision is **which serving path + quant**.
3. **Framing:** systems benchmark. Baseline = single fp16 model, no batching.
4. **Data reality:** eval set must be fixed across runs or comparisons are meaningless.
5. **Metric:** **p95 latency + tokens/sec at a quality floor** (don't ship a quant that drops quality below bar).
6. **Cost of wrong:** an over-aggressive quant degrades answers silently → always pair speed with a quality check.
7. **Path to prod:** this *is* the production path; monitor drift in latency/error + model quality.
8. **Build vs leverage:** leverage vLLM/Ollama; **the benchmark + quant-vs-quality evidence is the deliverable**.
