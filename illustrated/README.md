# 🎨 Illustrated AI/ML — Interactive Explainers

Visual, hands-on explainers for the roadmap's concepts (in the spirit of Jay Alammar's *Illustrated
Transformer*). We **build interactive explainers for the gaps** and **link the world's best existing
ones** for everything else. Start at **[`index.html`](index.html)** — the searchable catalog.

## How to view

**Quickest:** open `index.html` in any browser (double-click). Everything is plain HTML/CSS/JS with
**no build step, no frameworks, and no external dependencies**, so it works offline.

**Recommended (clean relative paths):** serve the folder so links/assets resolve exactly as they would
online:
```bash
cd ai-ml-roadmap/illustrated
python3 -m http.server 8000
# open http://localhost:8000
```

## What's here
- `index.html` — searchable catalog (🎨 *ours* / 🔗 *curated* / ⏳ *coming soon*), grouped by phase.
- `assets/style.css`, `assets/app.js` — shared design system + tiny vanilla-JS helpers (math, SVG, sliders).
- `*.html` — one self-contained interactive explainer per concept. Built so far (Batch 1, modern stack):
  - [`rag-pipeline.html`](rag-pipeline.html) — chunk → embed → retrieve → generate, with citations (ties to BYO-9)
  - [`react-agent.html`](react-agent.html) — Reason → Act → Observe loop; tools really run (ties to BYO-10)
  - [`vector-search.html`](vector-search.html) — brute-force vs ANN/IVF on a 2-D cloud (ties to BYO-11)
  - [`embeddings.html`](embeddings.html) — cosine playground + semantic search + the king−man+woman analogy
- `CATALOG.md` — the concept → resource map (mirrors the catalog).

## Publishing as a website later (GitHub Pages)
The repo is currently **private**, and GitHub Pages serves only from **public** repos (or with GitHub
Pro). When you're ready to share a live site:
1. Make the repo public **or** push a public mirror of just `ai-ml-roadmap/`.
2. Repo **Settings → Pages → Build from branch** → `main`, folder `/ (root)` (or `/docs` if you move it).
3. The site will be at `https://<user>.github.io/<repo>/illustrated/`.

Because every page uses **relative** asset paths and no external CDNs, it works identically locally and
on Pages — no changes needed.

## The teaching standard (how these are written)
Following StatQuest and Jay Alammar's *Illustrated Transformer*: **the prose teaches; the interactive
diagram reinforces.** Every explainer should:
1. **Introduce the idea & the problem it solves** (the "why") before any widget.
2. **Explain in depth, in words** — build intuition step by step, with an analogy where it helps.
3. **Use the interactive diagram to *reinforce*** that text (with a short "how to read this" note), not
   to replace it.
4. End with **strengths / limitations / where to go deeper** and a link to the matching BYO challenge.
A reader who never touches a slider should still learn the concept from the text alone.

## Adding a new explainer
Copy any `*.html`, keep the `<nav class="topbar">` + `assets/` links, write the **prose first** (per the
standard above), build the widget with the `Ill.*` helpers in `app.js`, then add an entry to the
`ITEMS` array in `index.html` and a row in `CATALOG.md`. Keep it **dependency-free** (no CDNs) so it
stays offline-friendly.
