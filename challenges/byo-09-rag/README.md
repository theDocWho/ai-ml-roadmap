# BYO-9 — Build Your Own RAG Engine (no LangChain)

> Reinforces: retrieval-augmented generation · Phase 6 · ⭐⭐⭐
> Build the whole RAG loop yourself — chunk, embed, retrieve, ground, answer — so you understand
> what frameworks hide. The embedder and LLM are **injected**, so tests run fully offline.

```bash
cd challenges/byo-09-rag
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest tests/ -v
```

## Stages (`rag/engine.py`)

1. **Chunk** — `chunk_text` splits a document into overlapping word windows.
2. **Embed + retrieve** — `cosine_similarity` and `RAGEngine.add_documents` / `retrieve` return the
   top-k chunks for a query (the tests inject a deterministic bag-of-words embedder).
3. **Ground** — `build_prompt` assembles the retrieved context with **numbered citations** + the query.
4. **Answer** — `answer` runs retrieve → prompt → `llm(prompt)` and returns the answer plus its
   sources; a hit@k check confirms retrieval quality.

## Real next step
Swap the mock embedder for `sentence-transformers`, store vectors in **Chroma/FAISS** (or your own
**BYO-11 vector DB**), call a real/local LLM (Ollama), and add **RAGAS** evaluation.

## Done when
`pytest tests/` is green and you can explain every stage of RAG and where retrieval quality comes from.
