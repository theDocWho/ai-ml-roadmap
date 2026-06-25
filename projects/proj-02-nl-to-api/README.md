# proj-02 — Natural-Language → API Assistant

> Reinforces: tool/function calling · structured output · guardrails · Phase 6 · ⭐⭐⭐
> Turn "refund order 1841 and email the customer" into **safe, validated API calls** against a real schema —
> with dry-runs, confirmation for write actions, and an audit log. This is the bridge from "chatbot" to
> "agent that *does* things," done with the safety rails a production system needs.

> Pairs with [BYO-10 (ReAct agent)](../../challenges/byo-10-react-agent/README.md) — same tool-loop idea, here schema-driven and guarded.

## 🆓 Free stack (vs the paid version)

| The guide says (paid) | Use this (free, capable) |
|---|---|
| GPT-4o-mini / Claude Haiku | **Qwen2.5-7B/14B** (good at JSON/tool-calling) via **Ollama** |
| (hosted business API) | a **FastAPI mock** business API you write |
| — | **OpenAPI / JSON-Schema** + **Pydantic** validation, **SQLite**, **Streamlit** |

## What you'll build
Two FastAPI apps: a **mock business API** (orders/customers/refunds) with an OpenAPI schema, and an
**assistant** that reads that schema, plans the call(s) from natural language, **validates against the schema**,
**dry-runs**, asks for confirmation on writes, executes, and logs everything.

## Stages
1. **Mock business API** — 5–8 endpoints (read + write) with a real OpenAPI spec and a SQLite store.
2. **Schema-aware planning** — feed endpoint schemas to the LLM; get back a *structured* call plan (method,
   path, params) as strict JSON. Reject anything not in the schema.
3. **Validation & dry-run** — Pydantic-validate params; simulate the effect and show it before executing.
4. **Multi-step workflows** — chain calls (look up customer → create refund → send confirmation), passing
   outputs forward; **require human confirmation** for any write/irreversible step.
5. **Logs, UI, tests** — Streamlit console showing plan → validation → result; pytest for the planner on a fixed
   set of NL requests (including ones that *must* be refused).

## Dataset / inputs
~40–60 natural-language requests (incl. ambiguous + disallowed) as your test set; seed data in SQLite.

## Make it better — local ↔ cloud
- **(local)** larger local model for trickier multi-step plans; add a **retry-on-validation-failure** loop;
  constrain output with a JSON grammar (llama.cpp GBNF) for 100% valid plans.
- **(free cloud)** use **Groq / Gemini free** for faster, stronger planning; deploy the demo on **HF Spaces**.

## Done when
- [ ] No call leaves the assistant without passing schema + Pydantic validation.
- [ ] Write/irreversible actions always require explicit confirmation.
- [ ] Disallowed or out-of-schema requests are refused (tested).
- [ ] A 3-step workflow runs end-to-end with a full audit trail.

## Concepts to be able to explain
Function/tool calling vs free-text; why schema-constrained output prevents whole classes of failures; dry-run +
human-in-the-loop for write actions; the OWASP "excessive agency" risk and how confirmation gates mitigate it.

## Decision Lens (filled)
1. **Problem:** let non-technical users operate business systems by describing intent, safely.
2. **Is ML right?** A fixed form would do for one task; **NL→many-tools** with validation is where the LLM earns its place.
3. **Framing:** tool-calling/structured-generation. Input = NL + schema; output = validated call plan. Baseline = a command parser.
4. **Data reality:** schemas drift; test set must include adversarial/ambiguous inputs and train/serve-skew on phrasing.
5. **Metric:** **plan validity rate** + **unsafe-action rate** (must be ~0). Bar: 100% schema-valid executions, 0 unconfirmed writes.
6. **Cost of wrong:** an unintended write (refund/delete) is far costlier than a refusal → bias to confirm/refuse.
7. **Path to prod:** real-time API behind auth; rate-limit + audit every call; monitor refusal/error rates.
8. **Build vs leverage:** leverage FastAPI/Pydantic; **the validation + confirmation gate is yours** — that's the safety story.
