# Capstone — GNN Fraud-Ring Detector (Graphs × Cyber/Finance)

> Optional Module C (Graph Neural Networks) × cyber/finance · ⭐⭐⭐⭐
> Build a Graph Convolutional Network from scratch (NumPy only) to flag fraudulent accounts that
> form dense "rings" — collusion / money-laundering structure that node features alone can't catch.
> The graph + utilities are **given**; you implement the **GCN**.

```bash
cd capstones/gnn-fraud
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest tests/ -v
```

## What's provided vs what you build

| Given (read it) | You implement (`gnn/model.py`) |
|---|---|
| `gnn/graph.py` — synthetic account graph with planted fraud rings; `normalized_adjacency` (Â = D⁻½(A+I)D⁻½); `accuracy`; given helpers `relu`/`softmax`/`cross_entropy_loss` | `gcn_layer` (Â·H·W), `GCN.forward`, and `GCN.train` (full-batch backprop) |

## The model
A 2-layer GCN:  `logits = Â · ReLU(Â · X · W0) · W1`. Backprop (Â is symmetric):
```
dlogits = (softmax(logits) − onehot(y)) / n_train,  zeroed outside the train mask
dW1 = H1ᵀ (Â dlogits)
dH1 = Â dlogits W1ᵀ ;  dZ1 = dH1 ⊙ (Z1 > 0)
dW0 = Xᵀ (Â dZ1)
```

## Why a GNN wins here
Each node's features are weak and noisy — a plain classifier barely separates fraud. But fraud nodes
are **densely interconnected**, so message passing (`Â·H`) averages each node with its neighbours and
**amplifies the shared signal inside a ring**. The reference reaches ~0.86 test accuracy / ~0.87 fraud
recall vs a 0.61 majority baseline. Try it: a features-only logistic regression does far worse.

## Stretch (not tested)
- Add more layers / GraphSAGE-style mean aggregation; compare to a feature-only baseline explicitly.
- Swap the synthetic graph for a real one (e.g. **Elliptic** bitcoin dataset, or IEEE-CIS fraud as a
  graph), and move to **PyTorch Geometric**.
- Tie into your security work: model hosts/flows as a graph and detect lateral-movement clusters.

## Concepts to be able to explain
Message passing / neighbourhood aggregation, why the normalized adjacency (self-loops + degree
normalization) stabilizes it, transductive node classification with train/test masks, and when graph
structure adds signal over tabular features.
