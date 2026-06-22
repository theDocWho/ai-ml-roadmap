# BYO-6 — Build Your Own CNN (convolution from scratch)

> Reinforces: convolution & pooling (exam Q44, Q45) · Phase 4 · ⭐⭐⭐
> Implement the convolution layer — forward *and* the backward pass that frameworks hide — in
> NumPy, verified against a numerical gradient.

```bash
cd challenges/byo-06-cnn
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest tests/ -v
```

Tensors are **NCHW**: `X (N,Cin,H,W)`, kernels `W (Cout,Cin,kh,kw)`, bias `b (Cout,)`. Valid
convolution, stride 1.

## Stages (`cnn/engine.py`)

1. **`conv2d_forward`** — slide each kernel over the input; checked against hand-computed values.
2. **`max_pool2d` + `relu`** — non-overlapping max pooling and the ReLU nonlinearity.
3. **`conv2d_backward`** — return `dX, dW, db`. This is the real lesson: the convolution's
   gradients. The test runs a **numerical gradient check**, so it must be exactly right.

## Stretch (not tested)
Wire `conv → relu → max_pool → flatten → linear → softmax` and train a tiny classifier on
synthetic images (e.g. bright-top vs bright-bottom) — reuse your **BYO-5 mini-PyTorch** autograd
for the fully-connected head, or move to PyTorch.

## Done when
`pytest tests/` is green — especially the gradient check, which proves your backprop is correct.
