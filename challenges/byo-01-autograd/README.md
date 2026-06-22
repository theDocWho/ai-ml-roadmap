# BYO-1 — Build Your Own Autograd Engine

> Reinforces: **backpropagation** (exam Q27, Q34) · Phase 0–1 · difficulty: ⭐⭐
> Inspired by Andrej Karpathy's [micrograd](https://github.com/karpathy/micrograd) —
> study it *after* you attempt this, not before.

You will build a tiny **reverse-mode automatic differentiation** engine from scratch — the
exact machinery that powers PyTorch/TensorFlow — and then use it to train a small neural net.
No NumPy, no ML libraries. When you finish, you'll *understand* backprop, not just call `.backward()`.

## How it works (CodeCrafters-style)

Each stage adds functionality and is locked behind a test file. Implement the code in
`autograd/`, then run that stage's tests. Move to the next stage only when green.

```bash
cd challenges/byo-01-autograd
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

pytest tests/test_stage1_value.py -v      # then stage 2, 3, 4
pytest -v                                  # all stages
```

## Stages

### Stage 1 — The `Value` object  (`autograd/engine.py`)
A `Value` wraps a single scalar and remembers how it was produced.
- `Value(data)` stores `.data` (float) and `.grad` (starts at `0.0`).
- Implement `__add__` and `__mul__` so `Value(2) + Value(3)` and `Value(2) * Value(3)` return
  new `Value`s with the correct `.data`.
- Implement `__repr__` → `Value(data=5.0, grad=0.0)`.
- Track the operation graph: each result stores its `_prev` (set of input Values) and `_op` (str).

**Acceptance:** `tests/test_stage1_value.py`

### Stage 2 — More operations
Add: `__pow__` (int/float exponent), `__neg__`, `__sub__`, `__truediv__`, the reflected
`__radd__`/`__rmul__` (so `2 * Value(3)` works), and the non-linearities `tanh()`, `exp()`, `relu()`.

**Acceptance:** `tests/test_stage2_ops.py`

### Stage 3 — Backpropagation
This is the heart. For every operation, define a local `_backward()` closure that pushes the
gradient from the output to its inputs (chain rule). Then implement `Value.backward()`:
1. Build a **topological order** of all nodes behind `self`.
2. Set `self.grad = 1.0`.
3. Walk the nodes in **reverse** topological order, calling each `_backward()`.

**Acceptance:** `tests/test_stage3_backprop.py` — checks the canonical hand-worked example
*and* verifies your analytic gradients against a numerical finite-difference gradient.

### Stage 4 — A neural net + a training loop  (`autograd/nn.py`)
Using only your `Value` engine:
- `Neuron(nin)` → weighted sum + bias through `tanh`.
- `Layer(nin, nout)` → list of neurons.
- `MLP(nin, nouts)` → stack of layers; `parameters()` returns every weight & bias.
- Train on the classic 4-example binary set with gradient descent; the loss must **decrease**.

**Acceptance:** `tests/test_stage4_mlp.py`

## Definition of done
All four test files pass, *and* you can explain — out loud — why `a.grad == 6.0` in the Stage 3
example. Then read micrograd and note what you'd refactor. Add a short `NOTES.md` describing what
clicked; that becomes your blog post / interview talking point.
