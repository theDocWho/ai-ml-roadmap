# proj-03 — AI Output Policy Guardrail Service

> Reinforces: safety · PII · structured validation · LLM security · Phase 6B · ⭐⭐⭐
> A service that sits **between your LLM and the user** and reviews every output for policy violations, PII
> leakage, and unsafe instructions — then rewrites, blocks, or passes it. The "seatbelt" layer every serious
> LLM product ships, and the natural home for the OWASP-LLM lessons from Phase 6B.

> Complements [BYO-16 (LLM red-team)](../../challenges/byo-16-llm-redteam/README.md): BYO-16 *attacks*, this *defends*.

## 🆓 Free stack (vs the paid version)

| The guide says (paid) | Use this (free, capable) |
|---|---|
| GPT-4o-mini / Claude Haiku (policy judge) | **Qwen2.5-7B/14B** or **Llama-3.1-8B** via **Ollama** |
| (managed PII) | **Microsoft Presidio** (free, OSS) |
| — | YAML policies · **Pydantic** · **FastAPI** · **PostgreSQL/SQLite** · Streamlit |

## What you'll build
A FastAPI `/review` endpoint: text in → run **deterministic validators** (regex/Presidio for PII, banned
patterns, schema checks) → run an **LLM policy review** against YAML-defined policies → decide
**pass / rewrite / block** → log the decision. Plus a review dashboard.

## Stages
1. **Policy definition** — YAML policies (no PII, no medical/legal advice, no secrets, must be on-topic) with
   severity + action.
2. **Deterministic validators** — Presidio for PII, regex for secrets/links, Pydantic for structure. Fast, cheap, run first.
3. **LLM policy review** — the judge classifies remaining/again-subtle violations with a reason. Combine with the deterministic layer.
4. **Rewrite / block flows** — redact PII and rewrite to compliant text, or block with a safe message; never leak the original.
5. **Review dashboard + tests** — log every decision; Streamlit view of flags by policy; pytest over a labeled
   set of safe/unsafe outputs (precision/recall on "should block").

## Dataset / inputs
~60–100 labeled example outputs (safe / PII / unsafe-instruction / off-policy), partly from a red-team run.

## Make it better — local ↔ cloud
- **(local)** ensemble two local judges + majority vote; tune the deterministic layer to cut judge calls;
  add a small classifier (fine-tuned, → proj-04) for high-volume pre-filtering.
- **(free cloud)** stronger **free-tier judge** (Gemini/Groq) for the hard cases; persist logs to **Qdrant/Postgres free tier**.

## Done when
- [ ] PII is reliably caught + redacted (test it on synthetic PII).
- [ ] Blocked outputs never leak the offending content.
- [ ] Precision/recall on "should block" reported on a labeled set.
- [ ] Deterministic layer short-circuits before the (slower) LLM judge.

## Concepts to be able to explain
Defense-in-depth (cheap deterministic → expensive LLM); precision/recall trade-off for guardrails (false-block
vs false-allow); OWASP LLM02 (insecure output handling) & LLM06 (sensitive-info disclosure); why you log decisions.

## Decision Lens (filled)
1. **Problem:** stop unsafe/PII-leaking/off-policy LLM text from reaching users.
2. **Is ML right?** Regex catches the obvious; subtle policy violations need an LLM judge → **hybrid**.
3. **Framing:** classification (pass/rewrite/block) + redaction. Baseline = regex/Presidio only.
4. **Data reality:** violations are rare (imbalanced); labels are subjective → write a clear rubric.
5. **Metric:** **recall on true violations** (a miss is the dangerous error) at acceptable false-block rate. Bar: ≥0.95 PII recall.
6. **Cost of wrong:** a leaked secret/PII >> an over-cautious block → tune toward recall.
7. **Path to prod:** inline real-time filter; monitor block-rate + drift; alert on spikes.
8. **Build vs leverage:** Presidio + framework; **the policy engine + decision logic is yours**.
