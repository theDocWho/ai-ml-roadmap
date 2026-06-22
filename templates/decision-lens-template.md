# Decision Lens — <project / problem name>

> Fill this one-pager **before** writing model code, for every project from Phase 3 on.
> It is the habit that lets you walk into an interview and reason about *any* problem.
> (Backed by Google's *Rules of ML* and Andrew Ng's *Machine Learning Yearning*.)

## 1. The problem, in one sentence
What outcome does someone actually want? (Not "use ML" — the business/user outcome.)

## 2. Is ML even the right tool?
- Could a **rule / heuristic / SQL query** solve 80% of this? If yes, do that first.
- ML is justified when: the pattern is complex, data is available, the rules would be unmanageable,
  and being approximately right at scale beats hand-coding. Write your justification here.
- **Decision:** ☐ rules/heuristic   ☐ ML   ☐ hybrid

## 3. Framing
- Task type: ☐ classification ☐ regression ☐ ranking ☐ clustering ☐ generation ☐ retrieval/RAG ☐ agent
- What is one **example** (input → desired output)?
- What's the **simplest baseline** (majority class / linear model / keyword rule)? You must beat it.

## 4. Data reality check
- Where does the data come from? How much? Labeled?
- Leakage risks? Train/serve skew? Class imbalance?
- How will you split train / dev / test (and does the dev set reflect production)?

## 5. Success metric
- The **single metric** you'll optimize, and **why it maps to the outcome** (e.g. F1 for imbalanced,
  recall when misses are costly, MAE for robust regression).
- Minimum bar to be useful in production: __________

## 6. Cost of being wrong
- Cost of a false positive vs false negative? Which matters more here?
- Any fairness / safety / privacy concerns?

## 7. Path to production (sketch now, build in Phase 7)
- Serving mode: ☐ batch ☐ real-time API ☐ embedded
- How will you monitor it and detect drift after deploy?

## 8. Build vs leverage (your independence vs tools)
- Will you implement the core yourself, use a library, or call an agent/LLM? Justify the choice on
  cost / latency / control / explainability — *and* note what you'd do if the tool were unavailable.

---
**Result after building:** baseline score ___ → model score ___ · top error category (from error
analysis) ___ · next improvement you'd make ___
