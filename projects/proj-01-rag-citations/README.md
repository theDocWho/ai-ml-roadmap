# proj-01 — Support Copilot with Verified Citations

> Reinforces: RAG · hybrid retrieval · grounding & evals · Phase 6 · ⭐⭐⭐
> A support assistant that answers from your docs **and proves it** — every claim is checked against the
> chunk it cites, so unsupported or hallucinated sentences get flagged or dropped. This is RAG with the
> guardrail interviewers actually ask about: *how do you know the answer is grounded?*

> Do [BYO-9](../../challenges/byo-09-rag/README.md) first to build retrieval from scratch; this productionizes it.

## 🆓 Free stack (vs the paid version)

| The guide says (paid) | Use this (free, capable) |
|---|---|
| OpenAI embeddings | **bge-base-en** / **nomic-embed-text** (sentence-transformers / Ollama) |
| GPT-4o-mini / Claude Haiku | **Qwen2.5-7B** or **Llama-3.1-8B** via **Ollama** |
| Qdrant Cloud | **Chroma** (local, Docker) |
| RAGAS w/ OpenAI judge | **RAGAS / DeepEval** with a **local-LLM judge** |
| (hosted UI) | **Gradio** + **Docker Compose** |

See the [model reference](../README.md#free-but-capable-model-reference-shared--briefs-point-here).

## What you'll build
A FastAPI service + Gradio UI: ask a question → **hybrid retrieve** (dense + BM25) → generate a grounded
answer with **inline numbered citations** → a **citation verifier** that checks each sentence is entailed by
its cited chunk → an **eval report** (faithfulness, answer relevance, context precision, citation accuracy).

## Stages
1. **Knowledge scope & ingestion** — pick a real corpus (a product's docs, a security runbook, 10-K filings).
   Loader → chunker (size + overlap) → embed → store in Chroma. Print chunk count + embedding dim.
2. **Hybrid retrieval** — dense cosine top-k **+** `rank-bm25` keyword top-k → reciprocal-rank fusion. Show it
   beats dense-only on a few keyword-heavy queries.
3. **Grounded generation with citations** — assemble a context prompt that *requires* `[n]` citations; render
   answer with footnotes that link back to the source chunk.
4. **Citation verification** — for each answer sentence, ask the judge "is this entailed by chunk [n]?"; drop or
   flag unsupported sentences. This is the differentiator.
5. **Eval suite** — a 30–50 case golden set; report faithfulness / relevance / context-precision (RAGAS) **plus**
   your own citation-accuracy metric. Wire it so a regression drops the score visibly.

## Dataset / inputs
Any corpus you care about (50–500 docs). Hand-write ~30–50 Q&A golden cases with the expected source.

## Make it better — local ↔ cloud
- **(local)** add a **bge-reranker** after fusion; try a bigger local model (Qwen2.5-14B/32B); tune chunk
  size/overlap; add query rewriting; cache embeddings.
- **(free cloud)** use a stronger **free-tier judge** (Groq / Gemini free) for more reliable faithfulness
  scoring; move vectors to **Qdrant Cloud (1 GB free)**; deploy the Gradio app on **HF Spaces**.

## Done when
- [ ] Runs offline via `docker compose up` (no paid keys).
- [ ] Answers carry working inline citations; unsupported sentences are flagged/removed.
- [ ] Hybrid retrieval measurably beats dense-only on your eval set.
- [ ] You can read off faithfulness + citation-accuracy and explain a failure case.

## Concepts to be able to explain
Why hybrid > dense-only; what "faithfulness" vs "answer relevance" measure; how citation-entailment checking
catches hallucinations RAG alone doesn't; chunking trade-offs; why a local judge can be noisy and how you'd calibrate it.

## Decision Lens (filled)
1. **Problem:** let support agents/users get *trustworthy* answers from internal docs without reading them all.
2. **Is ML right?** Keyword search alone misses paraphrases; LLM-only hallucinates. **Hybrid (retrieval + grounded LLM)** is justified.
3. **Framing:** retrieval/RAG + verification. Input = question; output = cited answer. Baseline = BM25 + extractive snippet.
4. **Data reality:** your docs (may be stale/duplicated); golden Q&A is small + hand-labeled → watch overfitting to it.
5. **Metric:** **faithfulness** + **citation accuracy** (a wrong-but-confident answer is the costly failure). Bar: ≥0.85 faithfulness, ≥0.9 citation accuracy.
6. **Cost of wrong:** a fabricated "fact" with a fake citation erodes all trust → prefer "I don't know" over ungrounded answers.
7. **Path to prod:** real-time API; monitor unanswered-rate + faithfulness drift (→ proj-07 / Phase 7).
8. **Build vs leverage:** leverage frameworks for serving; the **citation verifier** is your own logic — that's the interview story.
