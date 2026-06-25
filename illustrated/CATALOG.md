# Illustrated explainers — concept → resource map

Legend: 🎨 **ours** (interactive, in this folder) · 🔗 **curated** (best existing interactive resource) ·
⏳ coming soon. The live, searchable version is [`index.html`](index.html).

## Phase 0 · Python
- 🎨 **Java → Python mindset** — [python-java-mindset.html](0-python/python-java-mindset.html)
- 🎨 **Names, objects & mutability** — [python-data-model.html](0-python/python-data-model.html) · exam Q5 · 🔗 [Python Tutor](https://pythontutor.com/)
- 🎨 **Truthiness, bool & min/max** — [python-truthiness.html](0-python/python-truthiness.html) · exam Q3
- 🎨 **Strings & slicing** — [python-strings.html](0-python/python-strings.html) · 🔗 [Python Tutor](https://pythontutor.com/)
- 🎨 **list / tuple / set** — [python-collections.html](0-python/python-collections.html) · 🔗 [Python Tutor](https://pythontutor.com/)
- 🎨 **dict & hashing** — [python-dicts.html](0-python/python-dicts.html) · 🔗 [VisuAlgo: Hash Table](https://visualgo.net/en/hashtable)
- 🎨 **Comprehensions** — [python-comprehensions.html](0-python/python-comprehensions.html)
- 🎨 **zip & enumerate** — [python-zip-enumerate.html](0-python/python-zip-enumerate.html)
- 🎨 **\*args & \*\*kwargs** — [python-args-kwargs.html](0-python/python-args-kwargs.html) · 🔗 [Python Tutor](https://pythontutor.com/)
- 🎨 **Generators & yield** — [python-generators.html](0-python/python-generators.html) · 🔗 [Python Tutor](https://pythontutor.com/)
- 🎨 **Classes & namespaces** — [python-oop.html](0-python/python-oop.html) · 🔗 [Python Tutor](https://pythontutor.com/)
- 🎨 **Inheritance & the MRO** — [python-inheritance.html](0-python/python-inheritance.html) · 🔗 [Python Tutor](https://pythontutor.com/)
- 🎨 **Dunder (magic) methods** — [python-dunder.html](0-python/python-dunder.html)
- 🎨 **Exceptions** — [python-exceptions.html](0-python/python-exceptions.html)
- 🎨 **with & context managers** — [python-context-managers.html](0-python/python-context-managers.html) · 🔗 [Python Tutor](https://pythontutor.com/)

## Phase 1 · Scientific stack
- 🎨 **Vectorization & ufuncs** — [numpy-vectorization.html](1-scientific-stack/numpy-vectorization.html) · 🔗 [Visual NumPy](https://jalammar.github.io/visual-numpy/)
- 🎨 **NumPy broadcasting** — [numpy-broadcasting.html](1-scientific-stack/numpy-broadcasting.html) · 🔗 [Visual NumPy](https://jalammar.github.io/visual-numpy/)
- 🎨 **Aggregations & axis** — [numpy-axis.html](1-scientific-stack/numpy-axis.html) · exam Q4
- 🎨 **Indexing: slices, masks & fancy** — [numpy-indexing.html](1-scientific-stack/numpy-indexing.html)
- 🎨 **Series, DataFrames & loc/iloc** — [pandas-dataframe.html](1-scientific-stack/pandas-dataframe.html) · exam Q2
- 🎨 **GroupBy: split–apply–combine** — [pandas-groupby.html](1-scientific-stack/pandas-groupby.html)

## Phase 2 · Math
- 🎨 **Matrices as transformations** — [matrix-transformation.html](2-math/matrix-transformation.html)
- 🎨 **Dot product & projection** — [dot-product.html](2-math/dot-product.html) · exam Q1
- 🎨 **Bayes' theorem** — [bayes-theorem.html](2-math/bayes-theorem.html) · exam Q12/Q13 · 🔗 [Setosa: Conditional](https://setosa.io/conditional/)
- 🔗 Eigenvalues & eigenvectors — https://setosa.io/ev/eigenvectors-and-eigenvalues/
- 🔗 PCA — https://setosa.io/ev/principal-component-analysis/
- 🔗 Ordinary least squares — https://setosa.io/ev/ordinary-least-squares-regression/
- 🔗 Conditional probability & Bayes — https://setosa.io/conditional/
- 🔗 Probability & statistics (Seeing Theory) — https://seeing-theory.brown.edu/
- 🔗 Gradient descent + momentum (Distill) — https://distill.pub/2017/momentum/
- 🎨 **Optimizer comparison (SGD/Momentum/RMSprop/Adam)** — [optimizer-comparison.html](2-math/optimizer-comparison.html)

## Phase 3 · Classic ML
- 🔗 Visual intro to ML / decision trees (R2D3) — https://r2d3.us/visual-intro-to-machine-learning-part-1/
- 🔗 Bias–variance (MLU-Explain) — https://mlu-explain.github.io/bias-variance/
- 🔗 Cross-validation (MLU-Explain) — https://mlu-explain.github.io/cross-validation/
- 🔗 ROC & AUC (MLU-Explain) — https://mlu-explain.github.io/roc-auc/
- 🔗 Random forest (MLU-Explain) — https://mlu-explain.github.io/random-forest/
- 🔗 Linear/logistic regression (MLU-Explain) — https://mlu-explain.github.io/linear-regression/
- 🎨 **Confusion matrix & metrics** — [confusion-matrix.html](3-classic-ml/confusion-matrix.html) · exam Q23
- 🎨 **Regularization (Ridge vs Lasso)** — [regularization.html](3-classic-ml/regularization.html)
- 🎨 **k-Nearest Neighbors** — [knn.html](3-classic-ml/knn.html)
- 🎨 **SVM & the kernel trick** — [svm-margin.html](3-classic-ml/svm-margin.html)
- 🎨 **k-means clustering (steps)** — [kmeans-steps.html](3-classic-ml/kmeans-steps.html) · ties to BYO-4

## Phase 4 · Deep Learning
- 🔗 Neural net playground (TensorFlow) — https://playground.tensorflow.org/
- 🔗 CNN Explainer (poloclub) — https://poloclub.github.io/cnn-explainer/
- 🔗 Image kernels / convolution (Setosa) — https://setosa.io/ev/image-kernels/
- 🔗 GAN Lab (poloclub) — https://poloclub.github.io/ganlab/
- 🎨 **Activation functions** — [activations.html](4-deep-learning/activations.html) · exam Q32/37/38/39
- 🎨 **Loss functions (MSE vs cross-entropy)** — [loss-functions.html](4-deep-learning/loss-functions.html)
- 🎨 **Backpropagation (interactive)** — [backprop.html](4-deep-learning/backprop.html) · ties to BYO-1 / BYO-5
- 🎨 **LSTM / GRU gates** — [lstm-gru.html](4-deep-learning/lstm-gru.html)

## Phase 5 · NLP & Transformers
- 🎨 **TF-IDF** — [tfidf.html](5-nlp-transformers/tfidf.html)
- 🎨 **Positional encoding** — [positional-encoding.html](5-nlp-transformers/positional-encoding.html) · exam Q46
- 🔗 The Illustrated Transformer (Alammar) — https://jalammar.github.io/illustrated-transformer/
- 🔗 Transformer Explainer, live GPT-2 (poloclub) — https://poloclub.github.io/transformer-explainer/
- 🔗 The Illustrated Word2vec (Alammar) — https://jalammar.github.io/illustrated-word2vec/
- 🎨 **Self-attention (Q·Kᵀ→softmax→·V)** — [self-attention.html](5-nlp-transformers/self-attention.html) · ties to BYO-8

## Phase 6 · LLMs, RAG & Agents
- 🎨 **RAG pipeline** — [rag-pipeline.html](6-llms-rag-agents/rag-pipeline.html) · ties to BYO-9
- 🎨 **ReAct agent loop** — [react-agent.html](6-llms-rag-agents/react-agent.html) · ties to BYO-10
- 🎨 **Vector search: brute-force vs ANN** — [vector-search.html](6-llms-rag-agents/vector-search.html) · ties to BYO-11
- 🎨 **Embeddings & cosine similarity** — [embeddings.html](6-llms-rag-agents/embeddings.html)
- 🔗 LLM internals, 3-D walkthrough (bbycroft) — https://bbycroft.net/llm

## Phase 6B · LLM in-depth
- 🎨 **BPE tokenization** — [tokenization-bpe.html](6b-llm-indepth/tokenization-bpe.html) · ties to BYO-7
- 🎨 **LLM decoding (temp / top-k / top-p)** — [llm-decoding.html](6b-llm-indepth/llm-decoding.html)
- 🎨 **Mixture of Experts (MoE)** — [moe.html](6b-llm-indepth/moe.html)
- 🎨 **LoRA & quantization** — [lora-quantization.html](6b-llm-indepth/lora-quantization.html)
- 🔗 Diffusion Explainer (poloclub) — https://poloclub.github.io/diffusion-explainer/
- 🎨 **Prompt injection / OWASP LLM01** — [prompt-injection.html](6b-llm-indepth/prompt-injection.html) · ties to BYO-16

## Phase 7 · MLOps
- 🎨 **MLOps lifecycle & drift** — [mlops-lifecycle.html](7-mlops/mlops-lifecycle.html)

## Phase 8 · Agentic systems
- 🎨 **Agent patterns (workflows vs agents)** — [agent-patterns.html](8-agentic/agent-patterns.html)

## Modules
- 🔗 Graph Neural Networks (Distill) — https://distill.pub/2021/gnn-intro/
