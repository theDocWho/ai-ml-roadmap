# Phase 6B — LLM In-Depth (≈5–7 weeks)

**Goal:** go from *using* LLMs to *understanding and shaping* them — internals, **fine-tuning**,
**quantization**, **serving**, **evaluation**, and **security**. This is what separates an "API caller"
from an "LLM engineer." Builds on **BYO-7 (tokenizer)** and **BYO-8 (mini-GPT)**.

**Environment:** **☁️ Colab** / **📊 Kaggle** for the **free GPU** (QLoRA fine-tuning, quantization).
Local **Ollama**/**llama.cpp** for serving experiments.

**🔄 Freshness:** **fastest-moving area** — always use the **latest** library docs and models; specific
model/tool names below are examples. The *fundamentals* (attention, LoRA math, quantization) are stable.

**Primary resources** (open the link, then the **bold** item):
- [Maxime Labonne — *LLM Course*](https://github.com/mlabonne/llm-course) (Fundamentals/Scientist/Engineer + Colabs) · 🆕 [Vizuara](https://www.youtube.com/@vizuara) ("Build an LLM from scratch")
- [Sebastian Raschka — *Build an LLM From Scratch* (code)](https://github.com/rasbt/LLMs-from-scratch) · [Stanford CS336 — Language Modeling from Scratch](https://stanford-cs336.github.io)
- [Karpathy — "Deep Dive into LLMs" + "Let's build the GPT Tokenizer"](https://www.youtube.com/@AndrejKarpathy) · [LLM Visualization (interactive)](https://bbycroft.net/llm) · [HF LLM Course](https://huggingface.co/learn/llm-course)

---

## Module 6BA — LLM internals (deep)

| # | Topic | Open exactly this | ~Time |
|---|-------|-------------------|-------|
| 1 | Transformer internals, KV cache | [LLM Visualization](https://bbycroft.net/llm) (walk the whole pipeline) + [3B1B — "But what is a GPT?"](https://www.youtube.com/@3blue1brown) | 45m |
| 2 | Tokenization deep (BPE) | [Karpathy — "Let's build the GPT Tokenizer"](https://www.youtube.com/@AndrejKarpathy) | 2h |
| 3 | Decoding/sampling (greedy, top-k/p, temperature) | [HF LLM Course](https://huggingface.co/learn/llm-course) — **"Generation strategies"** | 30m |
| 4 | Scaling laws & emergent abilities | [Maxime Labonne — LLM Course](https://github.com/mlabonne/llm-course) — **"Fundamentals → scaling"** refs | 30m |
| 5 | Mixture of Experts (MoE) | [Hugging Face blog — "Mixture of Experts Explained"](https://huggingface.co/blog/moe) | 40m |

**✅ Checkpoint 6BA** — ☁️ Colab — one per topic:
- **(T1)** Explain a transformer forward pass end-to-end using the bbycroft viz; what does the **KV cache** save?
- **(T2)** 🔨 Finish **[BYO-7 (BPE)](../challenges/byo-07-bpe/README.md)**; explain why "tokens ≠ words" causes LLM quirks.
- **(T3)** Show how top-p vs temperature change generations; when use greedy vs sampling?
- **(T4)** State a scaling law in words; what does "emergent ability" mean (and the critique of it)?
- **(T5)** Explain how MoE routes tokens to experts and why it cuts compute per token.

---

## Module 6BB — Fine-tuning & alignment

| # | Topic | Open exactly this | ~Time |
|---|-------|-------------------|-------|
| 6 | Supervised fine-tuning (SFT) | [HF LLM Course](https://huggingface.co/learn/llm-course) — **"Supervised fine-tuning"** | 1.5h |
| 7 | **LoRA / QLoRA / PEFT** | [HF PEFT docs](https://huggingface.co/docs/peft/index) — **"LoRA / QLoRA"** + [Labonne course](https://github.com/mlabonne/llm-course) fine-tuning notebooks | 2h |
| 8 | Fast fine-tuning toolkits | [Unsloth docs](https://docs.unsloth.ai) — **"Fine-tuning Guide"** (2–5× faster on free Colab) | 1h |
| 9 | **Alignment: RLHF, DPO, ORPO** | [HF — "Illustrated RLHF"](https://huggingface.co/blog/rlhf) + [TRL docs](https://huggingface.co/docs/trl/index) — **"DPO"** | 1.5h |

**✅ Checkpoint 6BB** — ☁️ Colab/📊 Kaggle (GPU) — one per topic:
- **(T6)** Run an SFT on a small instruction dataset; show before/after behavior.
- **(T7)** **QLoRA fine-tune** an open model (Llama/Mistral/Qwen) on a domain set (security Q&A *or* finance); push to the HF Hub.
- **(T8)** Redo a fine-tune with **Unsloth**; compare speed/VRAM.
- **(T9)** In words: how does **DPO** avoid the reward model that RLHF needs? When prefer ORPO?

---

## Module 6BC — Efficiency: quantization & serving

| # | Topic | Open exactly this | ~Time |
|---|-------|-------------------|-------|
| 10 | **Quantization** (GGUF, GPTQ, AWQ, bitsandbytes) | [Labonne — LLM Course](https://github.com/mlabonne/llm-course) — **"Quantization"** notebooks | 1.5h |
| 11 | Run quantized models: llama.cpp / Ollama | [llama.cpp repo](https://github.com/ggml-org/llama.cpp) — **"Quantize → GGUF"** README | 1h |
| 12 | High-throughput serving (vLLM / TGI), KV cache | [vLLM docs](https://docs.vllm.ai) — **"Quickstart"** | 1h |

**✅ Checkpoint 6BC** — ☁️ Colab / 🖥️ Local — one per topic:
- **(T10)** Quantize your fine-tuned model to 4-bit; measure size + quality vs full precision.
- **(T11)** Convert to **GGUF** and run it locally via llama.cpp/Ollama; benchmark tokens/sec.
- **(T12)** Serve a model with **vLLM**; measure throughput vs a naive loop; explain what the KV cache + batching buy.

---

## Module 6BD — Evaluation & LLM security

| # | Topic | Open exactly this | ~Time |
|---|-------|-------------------|-------|
| 13 | **LLM evaluation** (benchmarks, LLM-as-judge) | [EleutherAI — lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) — **README/quickstart** + [promptfoo](https://www.promptfoo.dev/docs/intro/) | 1.5h |
| 14 | **OWASP LLM Top 10** & prompt injection | [OWASP GenAI — LLM Top 10](https://genai.owasp.org/llm-top-10/) | 1h |
| 15 | Red-teaming your own app | [Anthropic — Building Effective Agents](https://www.anthropic.com/research/building-effective-agents) (safety) + practice | 1h |

**✅ Checkpoint 6BD** — ☁️ Colab / 🖥️ Local — one per topic:
- **(T13)** Compare 2–3 models on a task with **lm-eval-harness** + an **LLM-as-judge** rubric; report results.
- **(T14)** Name the OWASP LLM Top-10 risks; demonstrate a **prompt-injection** against a naive bot.
- **(T15)** 🔨 Build **[BYO-16 (LLM red-team)](../challenges/byo-16-llm-redteam/README.md)**; red-team your Phase-6 RAG app and write the report.

---

## 🏁 Phase 6B capstone — your own fine-tuned, quantized, served, evaluated LLM
QLoRA fine-tune an open model on a domain dataset → **quantize** (GGUF) → **serve** (Ollama/vLLM) →
**evaluate** (before/after + lm-eval-harness) → **red-team** it (OWASP). One write-up tying it together
— a standout "LLM engineer" portfolio piece. Read a key paper (e.g. **LoRA** or **DPO**) with your
[research-skills](research-skills.md) method.

**Ready for Phase 7 when** you can explain a transformer end-to-end, fine-tune + quantize + serve an
open model, evaluate it, and reason about its security.
