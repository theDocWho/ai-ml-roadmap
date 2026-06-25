# proj-08 — Permissioned Tool-Using Agent Sandbox

> Reinforces: agents · tool use · security · human-in-the-loop · observability · Phase 8 · ⭐⭐⭐⭐
> An agent environment where the LLM can use tools — but **only** within permissions, rate limits, audit logs,
> and human approval for sensitive actions. This is the grown-up version of a ReAct loop: the Phase 8 lesson
> that *the hard part of agents is control, not capability*.

> Builds on [BYO-10 (ReAct)](../../challenges/byo-10-react-agent/README.md) + [BYO-13 (multi-agent)](../../challenges/byo-13-multiagent/README.md).

## 🆓 Free stack (vs the paid version)

| The guide says (paid) | Use this (free, capable) |
|---|---|
| GPT-4o / Claude | **Qwen2.5-14B / Llama-3.1-8B** via **Ollama** |
| (managed orchestration) | **LangGraph** (free) |
| (paid observability) | **OpenTelemetry** + local collector / Jaeger |
| — | **Pydantic** · **FastAPI** · **SQLite** (audit log) · Streamlit/React · Docker Compose |

## What you'll build
A LangGraph agent that plans and calls tools, where each tool has **declared permissions + rate limits**;
sensitive actions hit a **human-approval queue**; every step is written to an **audit log** and traced with
OpenTelemetry. A console shows the agent's reasoning, tool calls, approvals, and traces.

## Stages
1. **Agent & tool model** — define tools with a schema + a **permission/risk level**; a Pydantic tool registry.
2. **Permission checks & rate limits** — the agent can only call tools it's granted; enforce per-tool rate limits.
3. **LangGraph workflow** — reason → select tool → (check) → act → observe loop with state + retries/branches.
4. **Human approval queue** — high-risk tool calls pause for explicit approval before executing.
5. **Observability** — OpenTelemetry traces of each run; audit log of every tool call + decision; a trace/console UI.

## Dataset / inputs
A handful of tools (search, a mock write-action, your RAG retriever from proj-01) + scripted tasks, including
ones that **must** trigger approval or be denied.

## Make it better — local ↔ cloud
- **(local)** stronger local model for multi-step planning; add a critic/verifier agent; per-tool budgets.
- **(free cloud)** **Groq/Gemini free** for faster planning; export traces to **Grafana/Jaeger free tiers**; deploy console on **HF Spaces**.

## Done when
- [ ] The agent cannot call a tool it lacks permission for (tested).
- [ ] High-risk actions wait for human approval; denials are logged.
- [ ] Every run produces a full audit trail + trace.
- [ ] A task needing retrieval + a guarded write action completes end-to-end.

## Concepts to be able to explain
ReAct vs graph/state agents; least-privilege + human-in-the-loop as the core agent safety pattern; OWASP
"excessive agency"; why observability/audit is non-negotiable for agents; when a workflow beats an agent.

## Decision Lens (filled)
1. **Problem:** let an agent take real actions without it doing something unauthorized or unsafe.
2. **Is ML right?** A fixed workflow is safer for known tasks; an **agent** is justified only when the path varies — and even then, gated.
3. **Framing:** agent + policy enforcement. Baseline = a deterministic workflow (proj-02).
4. **Data reality:** task/tool traces; the key "data" is your permission matrix + approval rules.
5. **Metric:** **unauthorized-action rate (must be 0)** + task success at acceptable approval overhead.
6. **Cost of wrong:** an unapproved destructive tool call is the worst outcome → least-privilege + approval gates.
7. **Path to prod:** behind auth; full audit + trace retention; monitor tool-error and approval rates.
8. **Build vs leverage:** LangGraph for the loop; **permissions, approval queue, and audit are your design** — the interview centerpiece.
