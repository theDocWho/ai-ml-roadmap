# AI / ML Learning Roadmap — Beginner → RAG / LLM

A free, project-first path from "Java dev who knows no Python" to a practitioner who can **judge
whether ML fits a problem, build it, take it to production, improve it independently, design agentic
systems, and pass tough interviews.** Built around a 50-question AIML exam syllabus.

## What's here

| File / folder | What it is |
|---|---|
| [`AI_ML_Roadmap.pdf`](AI_ML_Roadmap.pdf) | The full roadmap as a **clickable PDF** (index + live resource links). Start here. |
| [`ROADMAP.md`](ROADMAP.md) | Same roadmap in Markdown (8 phases, resources, projects, certs, milestones). |
| [`challenges/`](challenges/README.md) | The **Build-Your-Own AI** series (13 staged, test-driven builds). |
| [`challenges/byo-01-autograd/`](challenges/byo-01-autograd/README.md) | First challenge, fully scaffolded with `pytest` tests. |
| [`phases/`](phases/README.md) | Detailed topic-by-topic study guides (links + checkpoints) for every phase. |
| [`illustrated/`](illustrated/index.html) | 🎨 Interactive, offline **illustrated explainers** + curated links to the best existing ones. |
| [`templates/decision-lens-template.md`](templates/decision-lens-template.md) | The problem-framing one-pager to fill for every project. |
| `build_roadmap_pdf.py` | Regenerates the PDF from `ROADMAP.md`. |

## How to use it

1. Read `AI_ML_Roadmap.pdf` end-to-end once; skim the **North-Star outcomes** table.
2. Work the phases in order (~10–15 hrs/week). Each phase ships a portfolio artifact.
3. At each phase, do the matching **Build-Your-Own** challenge for the internals.
4. From Phase 3 on, fill a **Decision Lens** for every project.
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
