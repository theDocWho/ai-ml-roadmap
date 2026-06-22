# BYO-16 — Build Your Own LLM Red-Team Probe

> Reinforces: LLM security — OWASP LLM01 prompt injection · Phase 6B · cyber + LLM track · ⭐⭐⭐
> Build both sides of LLM security: an attack corpus + a runner that measures secret leakage, and a
> detector that defends against it. The model under test is **injected**, so tests run offline.

```bash
cd challenges/byo-16-llm-redteam
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest tests/ -v
```

## Stages (`redteam/probe.py`)

1. **Detectors** — `is_injection` flags prompt-injection attempts ("ignore previous instructions",
   "system override", …); `detect_leak` checks whether a response exposed the secret.
2. **Red-team run** — `run_redteam` fires the attack corpus at a target LLM and reports the
   **leak rate**. A naive model leaks; a model guarded by `is_injection` blocks every attack.

## Real next step
Point `target` at a real/local model (Ollama) or your **BYO-9 RAG app**, expand the corpus
(jailbreaks, indirect injection via retrieved docs), and map findings to the
[OWASP LLM Top 10](https://genai.owasp.org/llm-top-10/). This pairs perfectly with your cybersecurity
background — AI red-teaming is in high demand.

## Done when
`pytest tests/` is green and you can explain prompt injection, why string-matching defenses are
necessary-but-insufficient, and what the OWASP LLM Top 10 covers.
