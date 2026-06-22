# BYO-5 — Build Your Own Mini-PyTorch

> Reinforces: MLP, backprop, activations, optimizers (exam Q26–Q39, Q7, Q8) · Phase 4 · ⭐⭐⭐⭐
> Generalize BYO-1 from scalars to **arrays** and rebuild the core of a deep-learning framework
> (NumPy only): autograd tensors, layers, a loss, and SGD/Adam. Then train a real classifier.

```bash
cd challenges/byo-05-minitorch
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest tests/ -v
```

## Stages

1. **Autograd Tensor** (`minitorch/tensor.py`) — `__add__`, `__mul__`, `__matmul__`, `relu`, `sum`,
   `mean`, and `backward()`. The twist vs BYO-1 is **broadcasting**: the backward pass must sum
   gradients back to each input's shape (`_unbroadcast` is provided). A numerical gradient check
   guards correctness.
2. **Layers + loss** (`minitorch/nn.py`) — `Linear` (`x @ W + b`) and a numerically-stable
   `softmax_cross_entropy` whose gradient is the clean `(softmax − onehot)/N`.
3. **Optimizers + training** (`minitorch/optim.py`) — `SGD` and `Adam`; then train a 2-layer MLP
   (Linear → ReLU → Linear) on two Gaussian blobs until loss collapses and accuracy > 95%.

## Done when
`pytest tests/` is green. You'll have built — and understood — every moving part PyTorch hides:
the tape, broadcasting gradients, a loss with a hand-derived backward, and adaptive optimizers.
