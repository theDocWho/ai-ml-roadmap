# BYO-10 — Build Your Own ReAct Agent

> Reinforces: tool-using agents · Phase 6 · ⭐⭐⭐
> Build the Reason+Act loop behind every tool-using agent — from scratch, stdlib only. The LLM and
> tools are **injected**, so the whole thing is deterministic and offline.

```bash
cd challenges/byo-10-react-agent
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest tests/ -v
```

## Stages (`agent/react.py`)

1. **Parsing** — `parse_action` extracts `Action:` / `Action Input:` from an LLM step; `parse_final`
   detects `Final Answer:`.
2. **The loop** — `ReActAgent.run`: prompt the LLM with the running scratchpad → if it emits a final
   answer, stop → otherwise run the named tool, append the `Observation:`, and repeat.
3. **Safety** — `max_steps` caps the loop so a misbehaving model can't run forever.

## Real next step
Swap the scripted LLM for a real/local model (Ollama) with a proper ReAct prompt template, add more
tools (search, your **BYO-9 RAG** retriever), then graduate to **LangGraph** for stateful,
multi-step agents (Phase 8 / BYO-13).

## Done when
`pytest tests/` is green and you can explain the reason→act→observe cycle and why tool grounding
beats a bare LLM for real tasks.
