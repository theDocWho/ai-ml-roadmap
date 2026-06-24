# Phase 5 — NLP + Transformers (≈4–6 weeks)

**Goal:** from classical NLP to the Transformer that powers every modern LLM. Covers exam **Q46, Q47**
plus *(beyond-exam)* classical NLP and generation metrics. You'll fine-tune real models.

**Environment:** **☁️ Colab** / **📊 Kaggle** for the **free GPU** (fine-tuning). Classical-NLP bits run
fine **🖥️ Local**.

**🔄 Freshness:** **Hugging Face** libraries move fast — use the **current** course/docs. The
*Transformer architecture* itself (2017) is stable — Illustrated Transformer & Karpathy stay valid.

**Primary resources** (open the link, then the **bold** item):
- [Hugging Face — *NLP Course*](https://huggingface.co/learn/nlp-course) (free, hands-on) · 🆕 [Vizuara](https://www.youtube.com/@vizuara) (Transformers/LLM "from scratch" series)
- [Jay Alammar — *The Illustrated Transformer*](https://jalammar.github.io/illustrated-transformer/) · [*The Illustrated Word2vec*](https://jalammar.github.io/illustrated-word2vec/)
- [Karpathy — *Let's build GPT*](https://karpathy.ai/zero-to-hero.html) · [StatQuest — Transformers](https://www.youtube.com/@statquest) · [Stanford CS224n (optional)](https://web.stanford.edu/class/cs224n/)
- 🎨 **[Illustrated explainers](../illustrated/index.html)** (interactive, offline): [Self-attention — Q·Kᵀ→softmax→·V](../illustrated/self-attention.html); plus curated [Transformer Explainer (live GPT-2)](https://poloclub.github.io/transformer-explainer/) & [LLM Visualization](https://bbycroft.net/llm).

---

## Module 5A — Classical NLP foundations *(beyond exam, but essential)*

| # | Topic | Open exactly this | ~Time |
|---|-------|-------------------|-------|
| 1 | Text preprocessing: tokenize, stem/lemmatize, stopwords | [HF NLP Course](https://huggingface.co/learn/nlp-course/chapter6/1) — **Ch.6 "Tokenizers"** (intro) | 40m |
| 2 | Bag-of-words, **TF-IDF**, n-grams | [scikit-learn UG](https://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction) — **"Text feature extraction (TF-IDF)"** | 40m |
| 3 | **Word embeddings**: word2vec / GloVe | [Jay Alammar — *The Illustrated Word2vec*](https://jalammar.github.io/illustrated-word2vec/) + [StatQuest](https://www.youtube.com/@statquest) — **"Word Embedding and Word2Vec"** | 45m |
| 4 | NER & POS tagging | [spaCy 101 (current docs)](https://spacy.io/usage/spacy-101) — **"Linguistic Features → POS, NER"** | 40m |
| 5 | Topic modeling (LDA) | [Gensim docs](https://radimrehurek.com/gensim/auto_examples/tutorials/run_lda.html) — **"LDA Model"** tutorial | 30m |

**✅ Checkpoint 5A** — 🖥️ Local — one per topic:
- **(T1)** Tokenize + lemmatize a paragraph; remove stopwords; show before/after token counts.
- **(T2)** Build a **TF-IDF** matrix for 3 docs; which terms get the highest weights and why?
- **(T3)** Load word2vec/GloVe vectors; show `king − man + woman ≈ queen`; cosine-similar words.
- **(T4)** Run spaCy NER + POS on a sentence; list entities and their labels.
- **(T5)** Fit LDA on a small corpus; print the top words per topic.

---

## Module 5B — Seq2seq & attention (the bridge)

| # | Topic | Open exactly this | ~Time |
|---|-------|-------------------|-------|
| 6 | Encoder–decoder / seq2seq | [Jay Alammar — "Visualizing A Neural Machine Translation Model (seq2seq + Attention)"](https://jalammar.github.io/visualizing-neural-machine-translation-mechanics-of-seq2seq-models-with-attention/) | 40m |
| 7 | **Attention** mechanism | [StatQuest](https://www.youtube.com/@statquest) — **"Attention for Neural Networks, Clearly Explained!!!"** | 16m |
| 8 | Beam search / decoding strategies | [HF NLP Course](https://huggingface.co/learn/nlp-course/chapter1/6) — **"Text generation strategies"** | 25m |

**✅ Checkpoint 5B** — 🖥️ Local/☁️ Colab — one per topic:
- **(T6)** Draw an encoder–decoder for translation; what's the information bottleneck without attention?
- **(T7)** Explain attention as weighted retrieval (query/key/value) in one paragraph.
- **(T8)** Compare greedy vs beam vs sampling decoding on a generation example.

---

## Module 5C — The Transformer (exam Q46, Q47)

| # | Topic | Open exactly this | ~Time |
|---|-------|-------------------|-------|
| 9 | The architecture (overview) | [Jay Alammar — *The Illustrated Transformer*](https://jalammar.github.io/illustrated-transformer/) | 1h |
| 10 | **Self-attention & multi-head attention** | [StatQuest](https://www.youtube.com/@statquest) — **"Transformer Neural Networks, Clearly Explained!!!"** | 36m |
| 11 | **Positional encoding** (exam Q46) | [Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) — **"Positional Encoding"** section | 20m |
| 12 | **Residual connections + LayerNorm** (exam Q47) | [Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) — **"The Residuals"** section | 15m |
| 13 | Build it from scratch | [Karpathy — *Let's build GPT*](https://karpathy.ai/zero-to-hero.html) (full) | 2h |
| 14 | Encoder vs decoder: BERT vs GPT | [HF NLP Course](https://huggingface.co/learn/nlp-course/chapter1/4) — **"How do Transformers work?"** | 30m |

**✅ Checkpoint 5C** — ☁️ Colab — one per topic:
- **(T9)** Sketch the full Transformer block (attention → add&norm → FFN → add&norm).
- **(T10)** Compute one self-attention output by hand for 3 tokens; why *multi-head*?
- **(T11)** What does sinusoidal positional encoding capture, and why is it needed (exam Q46)? 🔨 **[BYO-8](../challenges/byo-08-minigpt/README.md)**.
- **(T12)** What do residual connections do for deep transformers (exam Q47)?
- **(T13)** 🔨 Finish **[BYO-7 (BPE)](../challenges/byo-07-bpe/README.md)** and **[BYO-8 (mini-GPT)](../challenges/byo-08-minigpt/README.md)**.
- **(T14)** When would you use BERT (encoder) vs GPT (decoder)?

---

## Module 5D — Practical NLP with Hugging Face

| # | Topic | Open exactly this | ~Time |
|---|-------|-------------------|-------|
| 15 | `pipeline`, models, tokenizers | [HF NLP Course](https://huggingface.co/learn/nlp-course/chapter2/1) — **Ch.2 "Using Transformers"** | 1.5h |
| 16 | `datasets` library | [HF NLP Course](https://huggingface.co/learn/nlp-course/chapter5/1) — **Ch.5 "The Datasets library"** | 1h |
| 17 | **Fine-tuning** a transformer (classification) | [HF NLP Course](https://huggingface.co/learn/nlp-course/chapter3/1) — **Ch.3 "Fine-tuning a model"** | 2h |
| 18 | **Eval metrics**: BLEU, ROUGE, perplexity *(beyond)* | [HF — Evaluate docs](https://huggingface.co/docs/evaluate/index) — **"BLEU / ROUGE / Perplexity"** | 30m |
| 19 | Push to the Hub; deploy a demo | [HF NLP Course](https://huggingface.co/learn/nlp-course/chapter4/1) — **Ch.4 "Sharing models"** + Gradio on Spaces | 1h |

**✅ Checkpoint 5D** — ☁️ Colab/📊 Kaggle — one per topic:
- **(T15)** Run a sentiment `pipeline`; then tokenize + run the model manually to get the same result.
- **(T16)** Load a dataset with `datasets`, map a tokenization function, split train/test.
- **(T17)** **Fine-tune** DistilBERT on a real text-classification task (toxic-comment / news / resume-classifier).
- **(T18)** Compute BLEU/ROUGE for a summary and perplexity for a language model; what does each measure?
- **(T19)** Push your fine-tuned model to the **HF Hub** and deploy a **Gradio** demo on Spaces.

---

## 🏁 Phase 5 capstone — fine-tuned NLP app  (☁️ Colab → HF Hub/Spaces)
Fine-tune a transformer for a real task and ship a **Gradio** demo (e.g. a phishing-email classifier
for your cyber track, or financial-news sentiment). Finish **[BYO-7](../challenges/byo-07-bpe/README.md)**
+ **[BYO-8](../challenges/byo-08-minigpt/README.md)**. Read **"Attention Is All You Need"** using your
[research-skills](research-skills.md) 3-pass method.

**Ready for Phase 6 when** you can fine-tune + deploy a transformer and explain attention, positional
encoding, and residuals end-to-end.
