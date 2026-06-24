# Phase 4 — Deep Learning Foundations (≈6–8 weeks)

**Goal:** build and train neural nets — and understand them from the inside (you'll re-implement the
core). Covers exam **Q26–Q45** plus *(beyond-exam)* training tricks and advanced architectures.

**Environment:** **☁️ Colab** or **📊 Kaggle** for the **free GPU** (training is slow on CPU). Develop
locally, push to git, then `!git clone` into the GPU session.

**🔄 Freshness:** **PyTorch** moves fast — use the **current 2.x** docs/tutorials. The *math/ideas*
(backprop, conv, attention) are timeless — Karpathy, StatQuest, 3B1B stay valid regardless of age.

**Primary resources** (open the link, then the **bold** item):
- [Andrej Karpathy — *Neural Networks: Zero to Hero*](https://karpathy.ai/zero-to-hero.html) (do it in full) · 🆕 [Vizuara](https://www.youtube.com/@vizuara) (DL/“build from scratch”)
- [StatQuest — *Neural Networks* playlist](https://www.youtube.com/playlist?list=PLblh5JKOoLULxxmbyeF5kxYp_RKB-PfT0) · [3B1B — *Neural Networks*](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi)
- [fast.ai — Practical Deep Learning](https://course.fast.ai) · [*Dive into Deep Learning* (d2l.ai)](https://d2l.ai) · [PyTorch Tutorials (2.x)](https://pytorch.org/tutorials/) · [CS231n (advanced CV)](https://cs231n.github.io)
- 🎨 **[Illustrated explainers](../illustrated/index.html)** (interactive, offline): [Backpropagation](../illustrated/backprop.html), [LSTM/GRU gates](../illustrated/lstm-gru.html); plus curated [TensorFlow Playground](https://playground.tensorflow.org/), [CNN Explainer](https://poloclub.github.io/cnn-explainer/) & [GAN Lab](https://poloclub.github.io/ganlab/).

---

## Module 4A — Neural-net foundations

| # | Topic | Open exactly this | ~Time |
|---|-------|-------------------|-------|
| 1 | Perceptron → **MLP**, hidden layers (exam Q26, Q27) | [3B1B NN](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi) — **Ch.1 "But what is a neural network?"** · 📖 [Nielsen: Neural Networks (Ch.1)](http://neuralnetworksanddeeplearning.com/chap1.html) | 19m |
| 2 | Forward pass; weights, biases | [StatQuest NN](https://www.youtube.com/playlist?list=PLblh5JKOoLULxxmbyeF5kxYp_RKB-PfT0) — **"The Essential Main Ideas of Neural Networks"** · 📖 [d2l.ai: Multilayer Perceptrons](https://d2l.ai/chapter_multilayer-perceptrons/mlp.html) | 19m |
| 3 | **Activation functions** (sigmoid/tanh/ReLU/softmax) (exam Q32, Q37, Q38, Q39) | [StatQuest NN](https://www.youtube.com/playlist?list=PLblh5JKOoLULxxmbyeF5kxYp_RKB-PfT0) — **"ReLU In Action"** + StatQuest **"Softmax"** / **"Sigmoid"** · 📖 [CS231n: Neural Nets (activations)](https://cs231n.github.io/neural-networks-1/) | 30m |
| 4 | Loss functions (MSE, cross-entropy) | [StatQuest NN](https://www.youtube.com/playlist?list=PLblh5JKOoLULxxmbyeF5kxYp_RKB-PfT0) — **"Cross Entropy / Neural Networks Part 6"** · 📖 [d2l.ai: Softmax Regression & Cross-Entropy](https://d2l.ai/chapter_linear-classification/softmax-regression.html) | 15m |
| 5 | **Backpropagation** (exam Q34) | [3B1B NN](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi) — **Ch.3 "What is backpropagation really doing?"** + **Ch.4 "Backpropagation calculus"** · 📖 [Nielsen: Backpropagation (Ch.2)](http://neuralnetworksanddeeplearning.com/chap2.html) | 30m |
| 6 | Build it from scratch (the deep version) | [Karpathy Z2H](https://karpathy.ai/zero-to-hero.html) — **"The spelled-out intro to neural networks and backpropagation: building micrograd"** · 📖 [CS231n: Backprop notes](https://cs231n.github.io/optimization-2/) | 2.5h |
| 7 | Epochs, batches, iterations (exam Q29) | [Google ML Crash Course](https://developers.google.com/machine-learning/crash-course) — **"Training → epochs/batch size"** | 15m |
| 8 | Why hidden layers: the **XOR** problem (exam Q33) | [Vizuara](https://www.youtube.com/@vizuara) — search **"XOR neural network"** · 📖 [Nielsen: Universal approximation (Ch.4)](http://neuralnetworksanddeeplearning.com/chap4.html) | 15m |

**✅ Checkpoint 4A** — 🖥️ Local (CPU is fine here) — one per topic:
- **(T1)** Draw an MLP with one hidden layer; how many hidden layers does an MLP have *at least* (exam Q27)?
- **(T2)** Compute a forward pass for a 2-2-1 net by hand with given weights.
- **(T3)** Sketch sigmoid/tanh/ReLU/softmax; which is the output for binary (exam Q37) vs multiclass; what's softmax's range (exam Q32)? Is ReLU non-linear (exam Q38, Q39)?
- **(T4)** Compute cross-entropy loss for one example by hand.
- **(T5)** Write the backprop weight-update for output neuron k, input j (exam Q34).
- **(T6)** 🔨 Finish **[BYO-1 (autograd)](../challenges/byo-01-autograd/README.md)** — your backprop, from scratch.
- **(T7)** If you have 1000 samples, batch size 100, how many iterations per epoch (exam Q29)?
- **(T8)** Explain why a single-layer perceptron can't learn XOR but one hidden layer can (exam Q33).

---

## Module 4B — Training deep nets (PyTorch + the tricks)

| # | Topic | Open exactly this | ~Time |
|---|-------|-------------------|-------|
| 9 | **PyTorch**: tensors, autograd, `nn.Module`, training loop | [PyTorch Tutorials (2.x)](https://pytorch.org/tutorials/beginner/basics/intro.html) — **"Learn the Basics"** (full) | 3h |
| 10 | **Optimizers** in practice (SGD/Adagrad/RMSprop/Adam) (exam Q7, Q8, Q35) | [PyTorch docs](https://pytorch.org/docs/stable/optim.html) — **"torch.optim"** + recap [Ruder's blog](https://www.ruder.io/optimizing-gradient-descent/) | 30m |
| 11 | **Dropout** *(beyond)* | [d2l.ai](https://d2l.ai/chapter_multilayer-perceptrons/dropout.html) — **"Dropout"** | 25m |
| 12 | **Batch / Layer normalization** *(beyond)* | [d2l.ai](https://d2l.ai/chapter_convolutional-modern/batch-norm.html) — **"Batch Normalization"** | 25m |
| 13 | Weight init, LR schedules, gradient clipping *(beyond)* | [d2l.ai](https://d2l.ai/chapter_optimization/) — **"Optimization → learning-rate scheduling"** | 30m |
| 14 | Data augmentation; early stopping; weight decay *(beyond)* | [PyTorch Tutorials](https://pytorch.org/tutorials/) — **"Transfer Learning / Data Loading"** transforms | 30m |

**✅ Checkpoint 4B** — ☁️ Colab/📊 Kaggle — one per topic:
- **(T9)** Train an MLP on MNIST in PyTorch (load → `nn.Module` → loss → optimizer → loop → eval). 🔨 then **[BYO-5 (mini-PyTorch)](../challenges/byo-05-minitorch/README.md)**.
- **(T10)** Swap SGD↔Adam on the same net; compare convergence; one line each on Adagrad/RMSprop (exam Q7, Q8).
- **(T11)** Add dropout; show it reduces the train/val gap (overfitting).
- **(T12)** Add batch norm; observe faster/stabler training.
- **(T13)** Add an LR scheduler + gradient clipping; explain when each helps.
- **(T14)** Add data augmentation + early stopping to an image model; explain how each regularizes.

---

## Module 4C — Convolutional networks (computer vision)

| # | Topic | Open exactly this | ~Time |
|---|-------|-------------------|-------|
| 15 | **Convolution** (linear op) (exam Q36, Q44) | [StatQuest NN](https://www.youtube.com/playlist?list=PLblh5JKOoLULxxmbyeF5kxYp_RKB-PfT0) — **"Image Classification with Convolutional Neural Networks (CNNs)"** · 📖 [CS231n: Convolutional Networks](https://cs231n.github.io/convolutional-networks/) | 16m |
| 16 | **Pooling** (downsampling) (exam Q45) | [CS231n](https://cs231n.github.io/convolutional-networks/) — **"Pooling Layer"** section | 15m |
| 17 | CNN architectures (LeNet→ResNet) *(beyond)* | [d2l.ai](https://d2l.ai/chapter_convolutional-modern/resnet.html) — **"Residual Networks (ResNet)"** | 40m |
| 18 | **Transfer learning** *(beyond)* | [PyTorch Tutorials](https://pytorch.org/tutorials/beginner/transfer_learning_tutorial.html) — **"Transfer Learning for Computer Vision"** | 40m |
| 19 | Object detection (YOLO) & segmentation (U-Net) *(beyond)* | [CS231n](https://cs231n.github.io) — **"Detection and Segmentation"** lecture notes | 1h |

**✅ Checkpoint 4C** — ☁️ Colab/📊 Kaggle — one per topic:
- **(T15)** Is convolution linear or non-linear (exam Q36)? What does it *do* in a CNN (exam Q44)? 🔨 **[BYO-6 (CNN)](../challenges/byo-06-cnn/README.md)**.
- **(T16)** What does pooling do to spatial dimensions (exam Q45)? Does it have learnable params?
- **(T17)** What problem do ResNet's residual connections solve (vanishing gradients)?
- **(T18)** Fine-tune a pretrained ResNet on a small custom image set; deploy on **HF Spaces** (Gradio).
- **(T19)** In one paragraph each, how do YOLO (detection) and U-Net (segmentation) differ from classification?

---

## Module 4D — Sequence models & autoencoders

| # | Topic | Open exactly this | ~Time |
|---|-------|-------------------|-------|
| 20 | **RNNs** (exam Q43) | [StatQuest NN](https://www.youtube.com/playlist?list=PLblh5JKOoLULxxmbyeF5kxYp_RKB-PfT0) — **"Recurrent Neural Networks (RNNs), Clearly Explained!!!"** · 📖 [Karpathy: Unreasonable Effectiveness of RNNs](https://karpathy.github.io/2015/05/21/rnn-effectiveness/) | 16m |
| 21 | **LSTM / GRU** (exam Q42) | [StatQuest NN](https://www.youtube.com/playlist?list=PLblh5JKOoLULxxmbyeF5kxYp_RKB-PfT0) — **"Long Short-Term Memory (LSTM), Clearly Explained"** · 📖 [Chris Olah: Understanding LSTMs](https://colah.github.io/posts/2015-08-Understanding-LSTMs/) | 21m |
| 22 | seq2seq & attention (bridge to Phase 5) | [StatQuest NN](https://www.youtube.com/playlist?list=PLblh5JKOoLULxxmbyeF5kxYp_RKB-PfT0) — **"Sequence-to-Sequence (seq2seq) / Attention"** · 📖 [Jay Alammar: Seq2seq + Attention](https://jalammar.github.io/visualizing-neural-machine-translation-mechanics-of-seq2seq-models-with-attention/) | 17m |
| 23 | **Autoencoders** (exam Q41, Q50) | [Vizuara](https://www.youtube.com/@vizuara) — search **"Autoencoders from scratch"** · 📖 [Lilian Weng: From Autoencoder to Beta-VAE](https://lilianweng.github.io/posts/2018-08-12-vae/) | 30m |
| 24 | Self-supervised & contrastive learning *(beyond)* | [Lilian Weng — "Self-Supervised Representation Learning"](https://lilianweng.github.io/posts/2019-11-10-self-supervised/) | 45m |

**✅ Checkpoint 4D** — ☁️ Colab/📊 Kaggle — one per topic:
- **(T20)** What's the primary advantage of RNNs over feedforward nets (exam Q43)? Train an RNN on a toy sequence.
- **(T21)** Which activations sit in LSTM/GRU gates (exam Q42)? Why do gates fix vanishing gradients?
- **(T22)** Explain attention in one paragraph; why does it beat a fixed-length seq2seq context vector?
- **(T23)** Train an autoencoder for denoising; what does the bottleneck learn (exam Q50)? 🔨 **[BYO-12](../challenges/byo-12-generative/README.md)**.
- **(T24)** In words: how does contrastive learning create labels from unlabeled data?

---

## 🏁 Phase 4 capstone — deployed CV classifier  (☁️ Colab/📊 Kaggle → HF Spaces)
Train a CNN (from scratch *and* transfer learning) on a meaningful dataset (plant disease / X-ray /
custom), deploy with **Gradio on Hugging Face Spaces**. Also finish the from-scratch set:
**[BYO-5](../challenges/byo-05-minitorch/README.md)**, **[BYO-6](../challenges/byo-06-cnn/README.md)**.

**Ready for Phase 5 when** you can build, train, debug, and deploy a PyTorch model on a free GPU, and
explain backprop, conv, pooling, and RNN/LSTM from memory.
