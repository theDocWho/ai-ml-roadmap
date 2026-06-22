# BYO-11 — Build Your Own Vector Database

> Reinforces: vector search internals (the engine under RAG) · Phase 6 · ⭐⭐⭐
> Build what FAISS / Chroma do: exact search, an approximate (ANN) index, and persistence — from
> scratch (NumPy + stdlib).

```bash
cd challenges/byo-11-vectordb
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest tests/ -v
```

## Stages (`vectordb/db.py`)

1. **Exact search** — `cosine_similarities` + `VectorDB.add` / `search`: brute-force top-k. Correct
   but O(n) per query.
2. **ANN index** — `build_index` clusters vectors with k-means; `search_ann` probes only the nearest
   `n_probe` buckets (IVF-style). Far fewer comparisons, recall ≥ 0.7 of exact top-1 here.
3. **Persistence** — `save` / `load` round-trip the DB (vectors + metadata + index) to disk.

## Real next step
This is the storage layer for **BYO-9 RAG**. Compare your recall/latency to FAISS, then read how
HNSW graphs push recall higher than IVF.

## Done when
`pytest tests/` is green and you can explain the recall/speed trade-off of approximate search.
