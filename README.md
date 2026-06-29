# AI / ML Learning Roadmap — Beginner → RAG / LLM / Agentic

A free, project-first path from "Java dev who knows no Python" to a practitioner who can **judge
whether ML fits a problem, build it, take it to production, improve it independently, design agentic
systems and architectures, and pass tough interviews.** Built around a 50-question AIML exam syllabus.

[![▶ Open live interactive explainers](https://img.shields.io/badge/%E2%96%B6%20Open%20live%20explainers-1a2b4a?style=for-the-badge)](https://thedocwho.github.io/ai-ml-roadmap/illustrated/index.html)
[![Roadmap site](https://img.shields.io/badge/Roadmap%20site-0a7d2c?style=for-the-badge)](https://thedocwho.github.io/ai-ml-roadmap/)

> **🎨 See it live:** the **49 interactive explainers** render in your browser at
> **[thedocwho.github.io/ai-ml-roadmap/illustrated](https://thedocwho.github.io/ai-ml-roadmap/illustrated/index.html)**.
> (Clicking a `.html` link *inside* GitHub shows source code, not the rendered page — use the live links.)

## What's here

| File / folder | What it is |
|---|---|
| [`AI_ML_Roadmap.pdf`](AI_ML_Roadmap.pdf) | The full roadmap as a **clickable PDF** (index + live resource links). |
| [`ROADMAP.md`](ROADMAP.md) | The roadmap in Markdown — **9 phases**, resources, projects, certs, milestones. |
| [`phases/`](phases/README.md) | Detailed **topic-by-topic study guides** (exact links + checkpoints) for every phase. |
| [`challenges/`](challenges/README.md) | The **Build-Your-Own AI** series — **16** staged, test-driven, from-scratch builds. |
| [`projects/`](projects/README.md) | **8** production "system-around-the-model" projects (RAG, guardrails, agents, evals…). |
| [`capstones/`](capstones/) | Flagship builds: RL trading, GNN fraud, **car-damage cost (India)**, **AI solution architecture**. |
| [`illustrated/`](https://thedocwho.github.io/ai-ml-roadmap/illustrated/index.html) | 🎨 **49 interactive, offline explainers** (live link) + curated links to the best existing ones. |
| [`templates/`](templates/) | Problem-framing **Decision Lens**, plus architect artifacts: ADR, decision-matrix, cost-model, governance. |

## The phases (read in order)

| # | Phase | # | Phase |
|---|-------|---|-------|
| 0 | [Python for a Java dev](phases/phase-0-python.md) | 6 | [LLMs, RAG & Agents](phases/phase-6-llms-rag-agents.md) |
| 1 | [Scientific Python stack](phases/phase-1-scientific-stack.md) | 6B | [LLM in-depth](phases/phase-6b-llm-indepth.md) |
| 2 | [Math foundations](phases/phase-2-math.md) | 7 | [MLOps & Productionization](phases/phase-7-mlops.md) |
| 3 | [Classic Machine Learning](phases/phase-3-classic-ml.md) | 8 | [Agentic systems + Interview prep](phases/phase-8-agentic-interview.md) |
| 4 | [Deep Learning foundations](phases/phase-4-deep-learning.md) | 9 | [AI Solution Architecture *(optional)*](phases/phase-9-architecture.md) |
| 5 | [NLP + Transformers](phases/phase-5-nlp-transformers.md) | — | [Research skills](phases/research-skills.md) · [optional modules](phases/README.md) |

Each phase guide links its topics to the exact video/chapter to open, a 🎨 **interactive explainer**, a
🔨 **Build-Your-Own** challenge, and a 🏗️ **production project**.

## How to use it

1. Skim `AI_ML_Roadmap.pdf` / [`ROADMAP.md`](ROADMAP.md) once — note the **North-Star outcomes** table.
2. Work the [phases](phases/README.md) in order (~10–15 hrs/week). Each ships a portfolio artifact.
3. At each phase, do the matching **[Build-Your-Own](challenges/README.md)** challenge for the internals,
   then the **[production project](projects/README.md)** for the system around it.
4. From Phase 3 on, fill a **[Decision Lens](templates/decision-lens-template.md)** for every project.
5. Take the **free certs** as you go; one cloud cert near the end.

## Quick start — the first challenge

```bash
cd challenges/byo-01-autograd
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest tests/test_stage1_value.py -v     # implement autograd/ until green, then stages 2–4
```

## Regenerate the PDF

```bash
pip install reportlab
python3 build_roadmap_pdf.py     # reads ROADMAP.md -> AI_ML_Roadmap.pdf
```
