# BYO-13 — Build Your Own Multi-Agent Orchestrator

> Reinforces: agentic system design · Phase 8 · ⭐⭐⭐
> Build the coordination layer behind multi-agent frameworks (CrewAI / LangGraph) — from scratch,
> stdlib only. Agents are callables over a shared state; tests use deterministic mock agents.

```bash
cd challenges/byo-13-multiagent
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest tests/ -v
```

## Stages (`multiagent/orchestrator.py`)

1. **Message bus + shared state** — run agents in order, log every `(name, update)` message, and
   merge each update into the shared "blackboard"; don't mutate the caller's dict.
2. **Roles reaching a goal** — a **planner → worker → critic** loop runs over rounds until the
   critic approves (the `stop_when` predicate), demonstrating real cooperation.
3. **Safety** — `max_rounds` bounds the loop so agents can't spin forever.

## Real next step
Swap mock agents for LLM-backed roles (each agent = a prompt + your **BYO-10** ReAct loop), add
long-term memory, then rebuild on **LangGraph** for production multi-agent workflows (Phase 8).

## Done when
`pytest tests/` is green and you can explain orchestration patterns (planner/worker/critic,
blackboard state, stop conditions) and when multi-agent beats a single agent.
