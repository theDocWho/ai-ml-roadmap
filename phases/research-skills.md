# Research Skills — Reading, Verifying & Writing AI/ML Papers

The field moves monthly. Courses teach you what's settled; **papers** are where the frontier lives.
This guide is a recurring skill, not a phase — start it lightly in **Phase 3** and deepen it forever.
Goal: learn to **find**, **read**, **verify/reproduce**, and eventually **write** papers — i.e. to
*understand and test* new ideas instead of just trusting headlines.

---

## Module R1 — Find papers & stay current

| # | Topic | Use exactly this | How often |
|---|-------|------------------|-----------|
| 1 | The primary source | [**arXiv**](https://arxiv.org) — categories **cs.LG** (ML), **cs.CL** (NLP), **cs.CV** (vision), **stat.ML** | daily/weekly skim |
| 2 | Paper + code together | [**Papers with Code**](https://paperswithcode.com) — SOTA tables, trending, linked repos | weekly |
| 3 | Curated, discussed papers | [**Hugging Face — Daily Papers**](https://huggingface.co/papers) | daily |
| 4 | Discovery / explore citations | [**Connected Papers**](https://www.connectedpapers.com) · [**Semantic Scholar**](https://www.semanticscholar.org) · [**alphaXiv**](https://www.alphaxiv.org) (comment on arXiv) | as needed |
| 5 | Newsletters (curation beats firehose) | [**The Batch** (DeepLearning.AI)](https://www.deeplearning.ai/the-batch/) · [**Ahead of AI** — Sebastian Raschka](https://magazine.sebastianraschka.com) · [**Import AI**](https://jack-clark.net) | weekly |
| 6 | Where papers get published | conferences: **NeurIPS, ICML, ICLR** (ML) · **ACL/EMNLP** (NLP) · **CVPR/ICCV** (vision); reviews on [**OpenReview**](https://openreview.net) | seasonal |
| 7 | Visual explanations of classics | [**Distill**](https://distill.pub) · [**Vizuara**](https://www.youtube.com/@vizuara) · [**Yannic Kilcher** (paper walkthroughs)](https://www.youtube.com/@YannicKilcher) | per paper |

**✅ Checkpoint R1** — 🖥️ Local (just a browser + a notes file):
- **(T1)** Open arXiv **cs.LG** "recent"; save 3 titles that sound relevant to your projects.
- **(T2)** Find one of them on **Papers with Code**; note whether official code exists and its star count.
- **(T5)** Subscribe to **one** newsletter (The Batch or Ahead of AI). Set a fixed weekly 30-min "paper skim" slot.
- **(T7)** Watch one **Vizuara** or **Yannic Kilcher** walkthrough of a landmark paper (e.g. "Attention Is All You Need").

---

## Module R2 — How to read a paper (so it sticks)

| # | Topic | Use exactly this |
|---|-------|------------------|
| 8 | The **three-pass method** | [**Keshav, "How to Read a Paper" (PDF)**](http://ccr.sigcomm.org/online/files/p83-keshavA.pdf) |
| 9 | A practitioner's reading workflow | [**Andrew Ng — "Reading Research Papers" (Stanford CS230)**](https://www.youtube.com/@stanfordonline/search?query=reading%20research%20papers) (advice on reading + career) |
| 10 | What to extract every time | template below (problem → method → results → limitations → "what I'd test") |
| 11 | Filling math/notation gaps | [**The Math for ML book**](https://mml-book.github.io) + search the specific notation; don't skip equations |

**The three passes (Keshav), in short:**
1. **Pass 1 (~10 min):** title, abstract, intro, section headings, figures, conclusion. Decide: relevant? what are the claims?
2. **Pass 2 (~1 hr):** read carefully, ignore proofs; understand the method and the figures/tables. Mark what you don't get.
3. **Pass 3 (re-implement-level):** reconstruct the paper's logic as if you were the author; this is where you find hidden assumptions.

**Extraction template (one page per paper):** *Problem · Key idea (1 sentence) · Method · Datasets &
metrics · Main result · Baselines it beats · Limitations / assumptions · Does code exist? · One thing
I'd verify.*

**✅ Checkpoint R2** — 🖥️ Local:
- **(T8)** Do a **Pass-1** read of a paper in 10 minutes; write the claims in one sentence.
- **(T9/T10)** Do a **Pass-2** read of the same paper and fill the one-page extraction template.
- **(T11)** Pick one equation you didn't understand and explain it in plain words (use the MML book / a video).

---

## Module R3 — Verify & reproduce (the part most people skip)

Reading isn't believing. A claim is only real if it survives scrutiny and reproduction.

| # | Topic | How |
|---|-------|-----|
| 12 | Find the official code | [**Papers with Code**](https://paperswithcode.com) link, or the repo in the paper; check the **README + license + commit activity** |
| 13 | Reproduce the headline number | run the repo on the stated dataset/seed; compare to the paper's table (expect small gaps) |
| 14 | Re-implement the **core idea** small | strip it to the minimum and test on a tiny dataset (your BYO-style approach) — proves *you* understand it |
| 15 | Read it critically (red flags) | weak/old baselines, no error bars, cherry-picked datasets, no ablation, "SOTA" by tiny margins, no code/data |
| 16 | The reproducibility bar | [**ML Reproducibility Checklist (Joelle Pineau)**](https://www.cs.mcgill.ca/~jpineau/ReproducibilityChecklist.pdf) · [**Papers with Code — Reproducibility**](https://paperswithcode.com/rc2022) |

**✅ Checkpoint R3** — ☁️ Colab/📊 Kaggle (you'll likely want a GPU):
- **(T12/T13)** Clone a paper's repo into Colab; reproduce **one** reported metric on a small subset.
- **(T14)** Re-implement the paper's **central idea** in ~50 lines of NumPy/PyTorch on toy data; confirm it behaves as claimed.
- **(T15)** Write 3 critical questions about the paper (baseline fairness? ablation? does it generalize?).
- **(T16)** Score the paper against the reproducibility checklist (how many boxes does it tick?).

> This is exactly what your **Build-Your-Own challenges** trained you for: re-implementing core ideas
> from scratch is how you *verify* a paper, not just read it.

---

## Module R4 — Incorporate it into your work

| # | Topic | How |
|---|-------|-----|
| 17 | From paper → your project | take the one transferable idea, plug it into a project you already have (e.g. a better optimizer, a new attention variant, a RAG re-ranker) |
| 18 | Keep a research log | a `research-log.md` in your repo: paper → extraction template → "tried it, result was X" |
| 19 | Build a small literature map | use **Connected Papers** to find the 5 papers around an idea; read their intros to get the lineage |

**✅ Checkpoint R4** — 🖥️ Local:
- **(T17)** Apply one paper's idea to a project in this repo; commit it with a note linking the paper.
- **(T18)** Start `research-log.md` with your first 3 paper summaries.
- **(T19)** Make a Connected-Papers graph for one topic; list the 3 most-cited "ancestor" papers.

---

## Module R5 — Write & submit your own

You don't need a PhD. Start with a **workshop paper** or a **technical blog + arXiv preprint** built on
a reproduction or a small novel result (often from your capstones).

| # | Topic | Use exactly this |
|---|-------|------------------|
| 20 | Paper structure & craft | [**Simon Peyton Jones — "How to Write a Great Research Paper" (talk)**](https://www.youtube.com/results?search_query=Simon+Peyton+Jones+how+to+write+a+great+research+paper) |
| 21 | Writing tool (LaTeX, no install) | [**Overleaf**](https://www.overleaf.com) + an official conference template (NeurIPS/ICLR style files) |
| 22 | What to claim & how to evaluate | strong baselines, ablations, error bars, honest limitations; follow the [**NeurIPS Paper Checklist**](https://neurips.cc/public/guides/PaperChecklist) |
| 23 | Where to submit (start small) | **arXiv** preprint ([submission help](https://arxiv.org/help/submit), needs an endorsement) → a **workshop** at NeurIPS/ICML/ICLR (lower bar, great feedback) → main conference |
| 24 | Open-source the code | a clean GitHub repo + README + a Papers-with-Code entry — reproducibility *is* credibility |

**✅ Checkpoint R5** — 🖥️ Local:
- **(T20/T21)** Draft a 4-page write-up of one capstone (e.g. your GNN fraud detector) in Overleaf using a conference template: abstract, method, experiments, limitations.
- **(T22)** Add a baseline comparison + one ablation + an honest "limitations" paragraph; run it past the NeurIPS checklist.
- **(T23)** Identify one **workshop** whose topic fits your work and note its deadline/format.
- **(T24)** Publish the code as a clean repo with a README that lets a stranger reproduce your result.

---

## 🏁 Research-skills capstone
Pick **one recent paper** close to your interests (RAG, agents, fraud-GNNs, RL trading), and produce:
1. a one-page extraction summary (R2),
2. a small **reproduction** of one result + a ~50-line re-implementation of the core idea (R3),
3. a short blog post explaining it simply (teaching = the deepest test of understanding),
4. a paragraph on what you'd change or try next (the seed of your *own* paper).

**You've got this skill when** you can take a brand-new arXiv paper, judge in 10 minutes whether it's
worth your time, reproduce its core claim, and explain it to someone else — without taking it on faith.
