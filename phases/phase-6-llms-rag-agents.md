# Phase 6 — LLMs, RAG & Agents (≈6–8 weeks)

**Goal:** your stated end-goal — build with LLMs: prompting, embeddings + vector search, **RAG**, and
**tool-using agents**. (Going *inside* the LLM — fine-tuning, quantization, serving — is **Phase 6B**.)

**Environment:** **🖥️ Local** with **Ollama** (run open models free), plus **☁️ Colab**/**📊 Kaggle** for
GPU work and free API tiers. This Claude Code env also exposes the **Claude API**.

**🔄 Freshness:** this is the **fastest-moving** area in the whole roadmap — **always use the latest
docs and current models**; treat any specific model name below as an *example*, not a fixed choice.
The *patterns* (RAG, ReAct, tool use) are stable; the models/libraries change monthly.

> 🎨 **Visualize this phase (interactive, offline):** [RAG pipeline](../illustrated/rag-pipeline.html) ·
> [ReAct agent loop](../illustrated/react-agent.html) · [Vector search: brute-force vs ANN](../illustrated/vector-search.html) ·
> [Embeddings & cosine similarity](../illustrated/embeddings.html) — see [all explainers](../illustrated/index.html).

**Primary resources** (open the link, then the **bold** item):
- [Hugging Face — *LLM Course*](https://huggingface.co/learn/llm-course) · [*Agents Course*](https://huggingface.co/learn/agents-course) · 🆕 [Vizuara](https://www.youtube.com/@vizuara) (RAG/agents)
- [DeepLearning.AI — Short Courses (free)](https://www.deeplearning.ai/short-courses/) · [LangChain Academy (free)](https://academy.langchain.com) · [Activeloop — free RAG course](https://learn.activeloop.ai/courses/rag)
- [Ollama (run models locally)](https://ollama.com) · [Anthropic — Building Effective AI Agents](https://www.anthropic.com/research/building-effective-agents)

---

## Module 6A — LLM fundamentals & prompting

| # | Topic | Open exactly this | ~Time |
|---|-------|-------------------|-------|
| 1 | What an LLM is (the big picture) | [Karpathy — "Intro to Large Language Models" (1hr talk)](https://www.youtube.com/@AndrejKarpathy) | 60m |
| 2 | Tokens, context window, temperature/sampling | [HF LLM Course](https://huggingface.co/learn/llm-course) — **"How LLMs work / generation params"** | 40m |
| 3 | **Prompt engineering** | [DeepLearning.AI — "ChatGPT Prompt Engineering for Developers" (free)](https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/) | 1.5h |
| 4 | **Function calling / structured output** | [DeepLearning.AI — "Functions, Tools and Agents with LangChain"](https://www.deeplearning.ai/short-courses/functions-tools-agents-langchain/) (functions part) | 1h |
| 5 | Run models locally (free, private) | [Ollama docs](https://ollama.com) — install, `ollama run llama3`, the REST API | 30m |

**✅ Checkpoint 6A** — 🖥️ Local (Ollama) / free API — one per topic:
- **(T1)** In your own words, how does next-token prediction become "intelligence"? Name 2 limitations.
- **(T2)** Show how temperature 0 vs 1 changes outputs; what is the context window and why does it matter?
- **(T3)** Write a prompt with role + few-shot examples + output format; iterate to fix a bad output.
- **(T4)** Get an LLM to return strict **JSON** for a schema (structured extraction); validate it.
- **(T5)** Run a local model with Ollama and call it from Python over the REST API.

---

## Module 6B — Embeddings & vector search

| # | Topic | Open exactly this | ~Time |
|---|-------|-------------------|-------|
| 6 | **Embeddings** (semantic vectors) | [SBERT docs](https://www.sbert.net) — **"Sentence Transformers → Quickstart"** | 40m |
| 7 | Cosine similarity & semantic search | [SBERT docs](https://www.sbert.net/examples/applications/semantic-search/README.html) — **"Semantic Search"** | 30m |
| 8 | **Vector databases** (Chroma / FAISS) | [Chroma docs](https://docs.trychroma.com) — **"Getting Started"** | 40m |

**✅ Checkpoint 6B** — 🖥️ Local — one per topic:
- **(T6)** Embed 5 sentences with `sentence-transformers`; print the embedding dimension.
- **(T7)** Build semantic search: given a query, return the most similar sentence by cosine.
- **(T8)** Store + query vectors in Chroma/FAISS; 🔨 then build **[BYO-11 (vector DB)](../challenges/byo-11-vectordb/README.md)** from scratch.

---

## Module 6C — Retrieval-Augmented Generation (RAG)

| # | Topic | Open exactly this | ~Time |
|---|-------|-------------------|-------|
| 9 | The RAG pipeline (chunk→embed→retrieve→generate) | [DeepLearning.AI — "LangChain: Chat with Your Data" (free)](https://www.deeplearning.ai/short-courses/langchain-chat-with-your-data/) | 1.5h |
| 10 | RAG from scratch (deep understanding) | [freeCodeCamp — "RAG From Scratch"](https://www.youtube.com/@freecodecamp) (LangChain engineer) | 2h |
| 11 | Chunking strategies & citations | [LangChain docs](https://python.langchain.com/docs/concepts/text_splitters/) — **"Text splitters"** | 30m |
| 12 | **Evaluating RAG** (faithfulness, relevance) | [RAGAS docs](https://docs.ragas.io) — **"Getting Started / Metrics"** | 45m |
| 13 | Advanced RAG (re-ranking, query transforms) | [DeepLearning.AI — "Building and Evaluating Advanced RAG"](https://www.deeplearning.ai/short-courses/building-evaluating-advanced-rag/) | 1.5h |

**✅ Checkpoint 6C** — 🖥️ Local / ☁️ Colab — one per topic:
- **(T9)** Build a "chat with your PDF" RAG over a document you care about (security runbook / 10-K).
- **(T10)** 🔨 Build **[BYO-9 (RAG engine)](../challenges/byo-09-rag/README.md)** with no framework — prove you understand each step.
- **(T11)** Try 2 chunking strategies; add numbered **citations** to answers; compare retrieval quality.
- **(T12)** Evaluate your RAG with **RAGAS** (faithfulness + answer relevance); report the scores.
- **(T13)** Add a re-ranker or query rewriting; measure the lift vs naive RAG.

---

## Module 6D — Tool-using agents

| # | Topic | Open exactly this | ~Time |
|---|-------|-------------------|-------|
| 14 | What an agent is; **when NOT to use one** | [Anthropic — "Building Effective AI Agents"](https://www.anthropic.com/research/building-effective-agents) | 45m |
| 15 | **ReAct** (reason + act + tools) | [HF Agents Course](https://huggingface.co/learn/agents-course) — **Unit 1 "Introduction to Agents"** | 2h |
| 16 | LangGraph (stateful agents) | [DeepLearning.AI — "AI Agents in LangGraph" (free)](https://www.deeplearning.ai/short-courses/ai-agents-in-langgraph/) | 1.5h |
| 17 | Agent memory (short/long-term) | [DeepLearning.AI — "Long-Term Agentic Memory with LangGraph"](https://www.deeplearning.ai/short-courses/long-term-agentic-memory-with-langgraph/) | 1h |
| 18 | Agent tools = your RAG retriever | [LangChain docs](https://python.langchain.com/docs/concepts/tools/) — **"Tools"** | 30m |

**✅ Checkpoint 6D** — 🖥️ Local / ☁️ Colab — one per topic:
- **(T14)** Give one task where an **agent** is right and one where a simple **workflow** is better, with reasons.
- **(T15)** 🔨 Build **[BYO-10 (ReAct agent)](../challenges/byo-10-react-agent/README.md)** from scratch (parse Action/Observation loop).
- **(T16)** Rebuild the same agent in **LangGraph**; add a retry/branch.
- **(T17)** Add long-term memory so the agent recalls facts across turns.
- **(T18)** Give the agent your **RAG retriever** as a tool; ask a question that needs retrieval + reasoning.

---

## 🏁 Phase 6 capstone — flagship RAG app + agent  (🖥️ Local/☁️ Colab → HF Spaces)
1. **"Chat with your documents" RAG** with citations + RAGAS eval, deployed (Streamlit/Gradio).
2. A **tool-using agent** (LangGraph) that uses your RAG retriever + a tool.
For your domains: a **security analyst** (RAG over CVE/ATT&CK + triage agent) or an **investing
research assistant** (RAG over filings). Finish **[BYO-9](../challenges/byo-09-rag/README.md)**,
**[BYO-10](../challenges/byo-10-react-agent/README.md)**, **[BYO-11](../challenges/byo-11-vectordb/README.md)**.

**Ready for Phase 6B when** you've shipped a deployed, evaluated RAG system and a working agent, and
can explain every component (embedding, retrieval, prompt assembly, tool loop).
