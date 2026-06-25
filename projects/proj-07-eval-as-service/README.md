# proj-07 — Evaluation-as-a-Service Platform

> Reinforces: evals · LLM-as-judge · judge calibration · quality gates · Phase 7–8 · ⭐⭐⭐⭐
> A central `/score` API any of your other projects can call: give it outputs + a rubric, it returns calibrated
> scores, supports batch runs, and exposes **quality gates** (block a release if a metric regresses). Evals are
> the skill that separates "I built a demo" from "I run AI in production."

## 🆓 Free stack (vs the paid version)

| The guide says (paid) | Use this (free, capable) |
|---|---|
| OpenAI/Claude judges | **Qwen2.5-14B / Llama-3.1-8B** local judges (+ optional free-tier judge for hard cases) |
| (managed platform) | **FastAPI** · **SQLite/Postgres** · **scipy/numpy** · Streamlit |

## What you'll build
A scoring service with: rubric-based **LLM-as-judge** scoring, **judge calibration** against ~50 human-labeled
examples (so you trust the scores), **batch eval** runs, **quality gates** (pass/fail thresholds for CI), and a
dashboard of metrics over time. proj-01…06 plug into it.

## Stages
1. **Eval API** — `POST /score` with `{outputs, rubric}`; versioned rubrics; persist every result.
2. **Judge-based scoring** — structured rubric prompts → numeric + reasoned scores from a local judge.
3. **Judge calibration** — collect ~50 human labels; measure judge↔human agreement (correlation / Cohen's κ);
   adjust prompt/threshold until agreement is acceptable. **This is the credibility step.**
4. **Batch evals & quality gates** — run a dataset through; compute aggregate metrics; expose a gate that fails a
   build if a metric drops below threshold.
5. **Dashboard & analytics** — metrics over time, per-rubric breakdowns, regressions highlighted.

## Dataset / inputs
~50 human-labeled examples per rubric for calibration; reusable eval datasets from your other projects.

## Make it better — local ↔ cloud
- **(local)** ensemble judges + aggregate; add pairwise/Elo comparison; bootstrap confidence intervals on scores.
- **(free cloud)** a stronger **free-tier judge** (Gemini/Groq) for the calibration anchor; host the dashboard on **HF Spaces**.

## Done when
- [ ] `/score` returns calibrated, reasoned scores for a rubric.
- [ ] Judge↔human agreement measured and reported (not assumed).
- [ ] A quality gate fails a run when a metric regresses.
- [ ] At least one other proj-* calls this service for its evals.

## Concepts to be able to explain
LLM-as-judge pitfalls (position/verbosity bias, self-preference) and how calibration + ensembling mitigate them;
why judge↔human agreement must be measured; quality gates as CI for AI; offline vs online eval.

## Decision Lens (filled)
1. **Problem:** measure AI output quality consistently and gate releases on it.
2. **Is ML right?** Human eval doesn't scale; **LLM-judge + calibration** does, with guardrails.
3. **Framing:** scoring/regression + thresholding. Baseline = exact-match / heuristic metrics.
4. **Data reality:** small human-label set is the anchor; rubric ambiguity is the main risk → version rubrics.
5. **Metric:** **judge↔human agreement** first (trust the judge), then the task metrics it produces. Bar: κ ≥ 0.6.
6. **Cost of wrong:** a miscalibrated judge greenlights regressions → calibrate before you trust any gate.
7. **Path to prod:** internal API + CI gate; monitor judge drift as models change.
8. **Build vs leverage:** local judges; **calibration + quality-gate logic is the platform's value**.
