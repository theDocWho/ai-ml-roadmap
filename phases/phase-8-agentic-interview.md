# Phase 8 — Agentic Systems + Interview Readiness (≈5–7 weeks)

**Goal:** master **designing** agentic systems (not just calling a library) and convert everything into
**interview-ready** capability — ML system design, concepts, DSA, and a portfolio you can narrate.

> 🏗️ **Production projects (this phase):** [Permissioned agent sandbox](../projects/proj-08-agent-sandbox/README.md) ·
> [Evaluation-as-a-service](../projects/proj-07-eval-as-service/README.md) · [AI policy guardrail service](../projects/proj-03-guardrail-service/README.md) — see [all projects](../projects/README.md).

> 🏛️ **Going further (architect track):** [Phase 9 — AI Solution Architecture](phase-9-architecture.md) turns
> ML system design into architect **deliverables** — diagrams, **ADRs**, decision matrices, cost models, and
> governance (NIST AI RMF, EU AI Act) — for systems you already built.

**Environment:** mostly **🖥️ Local** (build agents, mock interviews) with **free API/Ollama** for agent runs.

**🔄 Freshness:** agent frameworks move monthly — use **latest** docs; the **patterns** (Anthropic's
workflow/agent taxonomy) and **interview fundamentals** are stable.

**Primary resources** (open the link, then the **bold** item):
- [Anthropic — Building Effective AI Agents](https://www.anthropic.com/research/building-effective-agents) + [cookbook patterns](https://github.com/anthropics/anthropic-cookbook/tree/main/patterns/agents)
- [HF Agents Course](https://huggingface.co/learn/agents-course) · [LangChain Academy (free)](https://academy.langchain.com) · [DeepLearning.AI agent short courses](https://www.deeplearning.ai/short-courses/)
- [Chip Huyen — *Introduction to ML Interviews* (free book)](https://huyenchip.com/ml-interviews-book/) · [NeetCode (DSA)](https://neetcode.io) · 🆕 [Vizuara](https://www.youtube.com/@vizuara)
- 🎨 **[Illustrated explainer](../illustrated/index.html)** (interactive, offline): [Agent patterns — workflows vs agents](../illustrated/8-agentic/agent-patterns.html) (chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer).

---

## Module 8A — Agentic system design

| # | Topic | Open exactly this | ~Time |
|---|-------|-------------------|-------|
| 1 | **Workflow vs agent** + when NOT to use an agent | [Anthropic — Building Effective AI Agents](https://www.anthropic.com/research/building-effective-agents) · 🎨 [Visualize: workflow vs agent](../illustrated/8-agentic/agent-patterns.html) | 1h |
| 2 | Patterns: chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer | [Anthropic cookbook — agent patterns](https://github.com/anthropics/anthropic-cookbook/tree/main/patterns/agents) · 🎨 [Visualize: the 5 patterns](../illustrated/8-agentic/agent-patterns.html) | 2h |
| 3 | **Multi-agent orchestration** (CrewAI) | [DeepLearning.AI — "Multi AI Agent Systems with crewAI" (free)](https://www.deeplearning.ai/short-courses/multi-ai-agent-systems-with-crewai/) · 📖 [CrewAI docs](https://docs.crewai.com) | 1.5h |
| 4 | Stateful multi-agent with LangGraph | [LangChain Academy](https://academy.langchain.com) — **"LangGraph"** modules · 📖 [LangGraph docs](https://langchain-ai.github.io/langgraph/) | 2h |
| 5 | Agent **evaluation & guardrails** | [HF Agents Course](https://huggingface.co/learn/agents-course) — **"Evaluation"** unit | 1h |

**✅ Checkpoint 8A** — 🖥️ Local — one per topic:
- **(T1)** For 3 tasks, decide workflow vs agent and justify the cost/latency/flexibility tradeoff.
- **(T2)** Implement two Anthropic patterns (e.g. routing + evaluator-optimizer) on a real task.
- **(T3)** Build a CrewAI crew (planner → researcher → writer → critic) for a research task.
- **(T4)** Rebuild it in **LangGraph** with shared state + a retry branch. 🔨 **[BYO-13 (multi-agent)](../challenges/byo-13-multiagent/README.md)**.
- **(T5)** Add an eval harness + a guardrail (input/output filter); measure success rate.

---

## Module 8B — Production agents

| # | Topic | Open exactly this | ~Time |
|---|-------|-------------------|-------|
| 6 | Cost / latency / observability | [Anthropic — Building Effective AI Agents](https://www.anthropic.com/research/building-effective-agents) (engineering tradeoffs) | 45m |
| 7 | Agent security (OWASP, prompt injection) | [OWASP — Top 10 for Agentic / LLM Apps](https://genai.owasp.org/llm-top-10/) | 1h |
| 8 | Memory & tools at scale | [DeepLearning.AI — "Long-Term Agentic Memory with LangGraph"](https://www.deeplearning.ai/short-courses/long-term-agentic-memory-with-langgraph/) · 📖 [LangGraph: Memory concepts](https://langchain-ai.github.io/langgraph/concepts/memory/) | 1h |

**✅ Checkpoint 8B** — 🖥️ Local — one per topic:
- **(T6)** Add token/latency logging to an agent; identify the most expensive step and optimize it.
- **(T7)** Red-team your agent for tool-misuse / prompt injection; 🔨 reuse **[BYO-16](../challenges/byo-16-llm-redteam/README.md)**.
- **(T8)** Give the agent persistent memory + 2 tools (RAG + a calculator); test a multi-step task.

---

## Module 8C — ML system design (interviews)

| # | Topic | Open exactly this | ~Time |
|---|-------|-------------------|-------|
| 9 | The ML system design framework | [Chip Huyen — ML Interviews book](https://huyenchip.com/ml-interviews-book/) — **"ML systems design"** chapter | 2h |
| 10 | Reuse your **Decision Lens** | [Decision Lens template](../templates/decision-lens-template.md) — frame → data → model → eval → serving → monitoring | 30m |
| 11 | Worked case studies | [Chip Huyen — Designing ML Systems case examples](https://huyenchip.com/mlops/) | 2h |

**✅ Checkpoint 8C** — 🖥️ Local — one per topic:
- **(T9)** Do a full ML-system-design writeup for "design a fraud-detection system" (frame→data→model→eval→serve→monitor).
- **(T10)** Apply the Decision Lens to a fresh problem in a timed 20 minutes.
- **(T11)** Write up a second case (recommendation or a RAG assistant); note the tradeoffs.

---

## Module 8D — Interview readiness

| # | Topic | Open exactly this | ~Time |
|---|-------|-------------------|-------|
| 12 | ML/DL **concept** interviews | [Chip Huyen — ML Interviews book](https://huyenchip.com/ml-interviews-book/) — **"ML concepts" Q&A** | 3h |
| 13 | **Coding / DSA** rounds | [NeetCode 150](https://neetcode.io/practice) — work the roadmap in Python | ongoing |
| 14 | **Portfolio narrative** (2-min per project) | your repo — script "problem → approach → result → what I'd improve" for each capstone | 2h |
| 15 | **Mock interviews** | [Pramp / interviewing.io free peer mocks](https://www.pramp.com) — do 2–3 | ongoing |

**✅ Checkpoint 8D** — 🖥️ Local — one per topic:
- **(T12)** Answer 10 concept questions out loud (bias/variance, regularization, attention, RAG, drift) — re-take your **50-question exam** and reason through each.
- **(T13)** Solve 20 NeetCode problems across arrays/strings/trees/graphs/DP in Python.
- **(T14)** Record a 2-minute narration for each of your ~8 portfolio projects.
- **(T15)** Do **2–3 mock interviews** (one ML-design, one coding); note and fix weak spots.

---

## 🏁 Phase 8 capstone — be hireable
Ship the two domain flagships (security analyst + investing dashboard), a **multi-agent** system
(BYO-13), an ML **system-design** doc, polished **2-minute narratives** for every project, and complete
**2–3 mock interviews**. You should be able to whiteboard an agentic system, argue workflow-vs-agent,
and explain any project under pressure.

**You're job-ready when** you can: judge whether ML fits a problem, build it, productionize it, improve
it independently, design an agentic system, and narrate your portfolio — and clear the toughest
interviews on knowledge that's practical and yours.
