# Module C — Graph Neural Networks (optional, ≈3 weeks)

**Goal:** learn on graph-structured data — fraud rings, recommendation, knowledge graphs, and
**network security** (hosts/flows as a graph). Pairs with your **[GNN fraud capstone](../capstones/gnn-fraud/README.md)**.

**Environment:** **☁️ Colab** / **📊 Kaggle** (GPU helps); small graphs run **🖥️ Local**.

**🔄 Freshness:** **PyTorch Geometric** updates — use **current** docs. The core ideas (message passing,
GCN/GAT) are stable.

**Primary resources** (open the link, then the **bold** item):
- [Stanford CS224W — Machine Learning with Graphs](https://web.stanford.edu/class/cs224w/) ([free lectures on YouTube](https://www.youtube.com/playlist?list=PLoROMvodv4rPLKxIpqhjhPgdQy7imNkDn)) · 🆕 [Vizuara](https://www.youtube.com/@vizuara)
- [Distill — "A Gentle Introduction to Graph Neural Networks"](https://distill.pub/2021/gnn-intro/) · [PyTorch Geometric docs](https://pytorch-geometric.readthedocs.io)

---

## Module C1 — Graph foundations & message passing

| # | Topic | Open exactly this | ~Time |
|---|-------|-------------------|-------|
| 1 | Graphs as data; node/edge/graph tasks | [Distill — Gentle Intro to GNNs](https://distill.pub/2021/gnn-intro/) (first half) | 1h |
| 2 | Representation: adjacency, node features, normalization | [PyG docs](https://pytorch-geometric.readthedocs.io/en/latest/get_started/introduction.html) — **"Introduction by Example → Data"** | 45m |
| 3 | **Message passing / neighborhood aggregation** | [Distill — Gentle Intro to GNNs](https://distill.pub/2021/gnn-intro/) (second half) + [CS224W](https://www.youtube.com/playlist?list=PLoROMvodv4rPLKxIpqhjhPgdQy7imNkDn) — **"GNN intuition"** lecture | 1.5h |
| 4 | **GCN** (graph convolution) | [CS224W](https://www.youtube.com/playlist?list=PLoROMvodv4rPLKxIpqhjhPgdQy7imNkDn) — **"Graph Convolutional Networks"** lecture | 1.5h |

**✅ Checkpoint C1** — 🖥️ Local/☁️ Colab — one per topic:
- **(T1)** Give a node-, an edge-, and a graph-level task example (e.g. fraud node, link prediction, molecule property).
- **(T2)** Build a small graph's adjacency + feature matrices; compute the normalized adjacency Â.
- **(T3)** Explain message passing in one paragraph: how does a node update from its neighbors?
- **(T4)** Write the GCN layer `Â·H·W`; 🔨 build **[BYO/GNN fraud capstone](../capstones/gnn-fraud/README.md)** (GCN from scratch).

---

## Module C2 — GNN architectures & tasks

| # | Topic | Open exactly this | ~Time |
|---|-------|-------------------|-------|
| 5 | **GraphSAGE** (sampling aggregation, scalable) | [CS224W](https://www.youtube.com/playlist?list=PLoROMvodv4rPLKxIpqhjhPgdQy7imNkDn) — **"GraphSAGE"** lecture | 1h |
| 6 | **GAT** (graph attention) | [PyG docs](https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.nn.conv.GATConv.html) — **"GATConv"** + paper | 1h |
| 7 | Node classification (transductive) | [PyG docs](https://pytorch-geometric.readthedocs.io/en/latest/get_started/introduction.html) — **"Node classification on Cora"** | 1h |
| 8 | Link prediction & graph-level (pooling) | [PyG examples](https://pytorch-geometric.readthedocs.io/en/latest/tutorial/index.html) — **"Link Prediction" / "Graph pooling"** | 1.5h |
| 9 | PyTorch Geometric end-to-end | [PyG docs](https://pytorch-geometric.readthedocs.io/en/latest/get_started/colabs.html) — **"Official Colab notebooks"** | 2h |

**✅ Checkpoint C2** — ☁️ Colab/📊 Kaggle — one per topic:
- **(T5)** Explain how GraphSAGE scales to huge graphs (neighbor sampling) vs full-batch GCN.
- **(T6)** What does attention add over GCN's fixed weights? Run `GATConv` on a small graph.
- **(T7)** Train a GCN on **Cora** for node classification; report test accuracy.
- **(T8)** Do link prediction on a graph; describe a graph-pooling readout for graph-level tasks.
- **(T9)** Reproduce a PyG official Colab; swap in a dataset relevant to fraud/security.

---

## 🏁 Module C capstone — fraud-ring / lateral-movement detector
Finish the **[GNN fraud capstone](../capstones/gnn-fraud/README.md)** (GCN from scratch), then redo it in
**PyTorch Geometric** with GraphSAGE/GAT and compare to a features-only baseline — proving structure
adds signal. For your cyber track: model hosts/flows as a graph and detect lateral-movement clusters.
Read the **GCN** or **GraphSAGE** paper with your [research-skills](research-skills.md) method.

**You've got GNNs when** you can explain message passing, implement a GCN, train node-classification in
PyG, and articulate when graph structure beats tabular features (fraud rings, AML, network security).
