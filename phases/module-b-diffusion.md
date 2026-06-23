# Module B — Diffusion & Generative Vision (optional, ≈3–4 weeks)

**Goal:** understand and build the models behind modern image/audio/video generation (Stable
Diffusion). Complements your LLM depth and the VAE/GAN work in **[BYO-12](../challenges/byo-12-generative/README.md)**.

**Environment:** **☁️ Colab** / **📊 Kaggle** — you need a **GPU** to train/sample diffusion models.

**🔄 Freshness:** the **diffusers** library and models move fast — use **current** docs/models. The core
math (**DDPM**, forward/reverse process) is stable.

**Primary resources** (open the link, then the **bold** item):
- [Hugging Face — *Diffusion Models Course*](https://huggingface.co/learn/diffusion-course) (free, hands-on) · 🆕 [Vizuara](https://www.youtube.com/@vizuara)
- [Jay Alammar — *The Illustrated Stable Diffusion*](https://jalammar.github.io/illustrated-stable-diffusion/) · [Lilian Weng — "What are Diffusion Models?"](https://lilianweng.github.io/posts/2021-07-11-diffusion-models/)
- [fast.ai — Part 2 (build Stable Diffusion from scratch)](https://course.fast.ai/Lessons/part2.html)

---

## Module B1 — How diffusion works

| # | Topic | Open exactly this | ~Time |
|---|-------|-------------------|-------|
| 1 | Generative landscape (VAE/GAN/diffusion) | [Lilian Weng — "What are Diffusion Models?"](https://lilianweng.github.io/posts/2021-07-11-diffusion-models/) (intro) | 40m |
| 2 | **Forward process** (adding noise) | [HF Diffusion Course](https://huggingface.co/learn/diffusion-course) — **Unit 1 "Introduction to Diffusers"** | 1.5h |
| 3 | **Reverse process** (denoising) + DDPM | [HF Diffusion Course](https://huggingface.co/learn/diffusion-course) — **Unit 1 "Diffusion Models from Scratch"** | 2h |
| 4 | The **U-Net** denoiser | [Illustrated Stable Diffusion](https://jalammar.github.io/illustrated-stable-diffusion/) — **"The U-Net"** section | 30m |
| 5 | Sampling: DDPM vs DDIM (fewer steps) | [HF Diffusion Course](https://huggingface.co/learn/diffusion-course) — **Unit 4 "Faster sampling"** | 1h |

**✅ Checkpoint B1** — ☁️ Colab — one per topic:
- **(T1)** In words: how does diffusion differ from a GAN (training stability, sample quality)? (recall exam Q48/Q49)
- **(T2)** Add increasing Gaussian noise to an image over T steps; visualize the schedule.
- **(T3)** Train a tiny DDPM on a small dataset (MNIST/butterflies); sample from pure noise.
- **(T4)** Explain why a U-Net (with skip connections) is the right denoiser architecture.
- **(T5)** Compare DDPM (many steps) vs DDIM (few steps) sample quality/speed.

---

## Module B2 — Conditioning & Stable Diffusion

| # | Topic | Open exactly this | ~Time |
|---|-------|-------------------|-------|
| 6 | Conditioning & **classifier-free guidance** | [HF Diffusion Course](https://huggingface.co/learn/diffusion-course) — **Unit 2 "Fine-tuning and guidance"** | 2h |
| 7 | **Latent diffusion** (Stable Diffusion) | [Illustrated Stable Diffusion](https://jalammar.github.io/illustrated-stable-diffusion/) (full) | 1h |
| 8 | Text-to-image + **CLIP** | [HF Diffusion Course](https://huggingface.co/learn/diffusion-course) — **Unit 3 "Stable Diffusion"** | 2h |
| 9 | Fine-tuning (DreamBooth / LoRA) | [HF diffusers — DreamBooth training docs](https://huggingface.co/docs/diffusers/training/dreambooth) | 2h |

**✅ Checkpoint B2** — ☁️ Colab/📊 Kaggle — one per topic:
- **(T6)** Show how the guidance scale changes outputs; what does classifier-free guidance trade off?
- **(T7)** Explain why doing diffusion in *latent* space (vs pixels) makes Stable Diffusion efficient.
- **(T8)** Generate images from text prompts with `diffusers`; explain CLIP's role in conditioning.
- **(T9)** Fine-tune Stable Diffusion (DreamBooth/LoRA) on a small concept; deploy a **Gradio** demo.

---

## 🏁 Module B capstone — your own image generator
Fine-tune Stable Diffusion on a custom concept (a style, an object) and ship a **Gradio on HF Spaces**
demo; *and/or* train a small DDPM from scratch (fast.ai Part 2 style) to prove you understand the math.
Read the **DDPM** or **Latent Diffusion** paper with your [research-skills](research-skills.md) method.

**You've got diffusion when** you can explain the forward/reverse process, why a U-Net denoises, what
guidance does, and why latent diffusion is efficient — and you've generated images both from scratch
and with Stable Diffusion.
