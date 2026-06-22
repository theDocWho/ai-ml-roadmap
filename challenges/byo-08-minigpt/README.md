# BYO-8 — Build Your Own mini-GPT (transformer from scratch)

> Reinforces: positional encoding (exam Q46), residual connections (Q47), attention · Phase 5 · ⭐⭐⭐⭐
> Build the GPT architecture's forward pass in NumPy: positional encoding, scaled dot-product
> attention with a causal mask, multi-head attention, LayerNorm, and a pre-norm block with residuals.

```bash
cd challenges/byo-08-minigpt
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest tests/ -v
```

Convention: one sequence `X` is `(T, d_model)`; projections are `(d_model, d_model)`.

## Stages (`minigpt/model.py`)

1. **Primitives** — stable `softmax`, sinusoidal `positional_encoding`, lower-triangular `causal_mask`.
2. **Attention** — `scaled_dot_product_attention` (rows sum to 1; the causal mask blocks the future),
   `layer_norm`, and `multi_head_attention` (split heads → attend → concat → output projection).
3. **The block** — `transformer_block`: pre-norm `x + MHA(LN(x))` then `a + MLP(LN(a))`. The residual
   `+` connections are why deep transformers train (exam Q47).

## Stretch (not tested — this is the capstone)
Add a token-embedding table + an output head over a tiny char vocab, then train with backprop to
make loss drop. Easiest path: drive it with your **BYO-5 mini-PyTorch** autograd, or follow
Karpathy's [nanoGPT](https://github.com/karpathy/nanoGPT) / "Let's build GPT".

## Done when
`pytest tests/` is green — you've implemented attention and a transformer block correctly and can
explain why the causal mask makes it a *language* model.
