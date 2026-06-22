# BYO-7 — Build Your Own BPE Tokenizer

> Reinforces: tokenization (the LLM front-end) · Phase 5 · ⭐⭐
> Every LLM starts by turning text into token ids. Build byte-pair encoding from scratch — pure
> Python, no deps. Inspired by [minBPE](https://github.com/karpathy/minbpe).

```bash
cd challenges/byo-07-bpe
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest tests/ -v
```

## Stages (`bpe/tokenizer.py`)

1. **Primitives** — `get_stats(ids)` counts adjacent pairs; `merge(ids, pair, idx)` replaces every
   occurrence of a pair with a new id.
2. **Train** — start from UTF-8 bytes (ids 0–255), repeatedly merge the most frequent pair into a
   new id until you hit `vocab_size`. Record the merges in order.
3. **Encode / decode** — apply learned merges greedily (lowest merge-id first) to encode; rebuild
   the byte strings to decode. `decode(encode(text)) == text` for any input, including Unicode.

## Done when
`pytest tests/` is green (round-trips ASCII *and* Unicode, and compresses repetition). You'll
understand why "tokens ≠ characters" and where weird LLM tokenization artifacts come from.
