# Capstone — AI Solution Architecture design package (Architect track)

> [Phase 9](../../phases/phase-9-architecture.md) · ⭐⭐⭐⭐
> The capstone with **no code** — and that's the point. You take a system you **already built** in
> [`projects/`](../../projects/README.md) and produce the **design package an AI Architect is hired on:**
> a diagram, an ADR, a decision matrix, a cost model, and a governance checklist. The article's thesis is
> *portfolio of decisions over certificates* — this is that portfolio.

> **Prereq:** finish Phases 6–8 and build ≥1 `projects/` system first. You can't credibly *architect* a
> system you haven't *built*.

## Pick your system
Architect one of your own builds end-to-end. Richest choices:
- [`proj-01` support copilot](../../projects/proj-01-rag-citations/README.md) — RAG at enterprise scale (data, retrieval, cost, PII).
- [`proj-08` agent sandbox](../../projects/proj-08-agent-sandbox/README.md) — multi-agent, permissions, reliability, governance.
- the [car-damage estimator (India)](../car-damage-cost-india/README.md) — CV + tabular + an insurance compliance angle.

## What's provided vs what you build

| Given (use them) | You produce (the deliverables) |
|---|---|
| The 4 templates in [`../../templates/`](../../templates/) | a filled instance of each, for *your* system |
| The system you already built | a design package that scales it to "real users" |
| [Phase 9](../../phases/phase-9-architecture.md) modules 9A–9E | the reasoning behind each artifact |

## The 5 deliverables (→ `docs/architecture/` in that project's repo)

1. **Architecture diagram** ([C4](https://c4model.com), drawn in Excalidraw/draw.io/Mermaid) — components,
   interfaces, **where state lives**, data flow (batch vs stream), and **labelled failure points**. Include
   the **10× scale** version: where queuing, horizontal scaling, and a semantic cache go.
2. **ADR** ([template](../../templates/adr-template.md)) — the pivotal decision (e.g. **open-weight vs
   managed**), options considered, decision, **consequences + reversibility**.
3. **Decision matrix** ([template](../../templates/decision-matrix-template.md)) — the weighted scoring
   behind that ADR, with *your* constraints (latency, privacy, volume, team).
4. **Cost model** ([template](../../templates/cost-model-template.md)) — monthly **token + inference +
   retrieval** cost at a stated volume, managed-vs-self-host, and the **break-even**.
5. **Governance checklist** ([template](../../templates/ai-governance-checklist.md)) — **NIST AI RMF**
   functions, **EU AI Act** risk tier, a risk register, model card, and **≥2 success metrics defined before
   shipping**.

## Done when
- [ ] All 5 artifacts exist in `docs/architecture/` (Markdown + diagram source committed).
- [ ] The diagram names every component, interface, state store, and **≥3 failure scenarios** with handling.
- [ ] The ADR's decision is justified by the decision matrix and lists accepted tradeoffs.
- [ ] The cost model gives a number at a stated volume + a break-even vs a managed API.
- [ ] The governance checklist names the EU AI Act tier and maps NIST AI RMF Govern/Map/Measure/Manage.
- [ ] You can present the whole thing to a **non-technical stakeholder** in cost/risk/outcome terms.

## Why this wins
Most candidates show *code*. Few can show a **diagram + ADR + cost model + compliance read** for a system
they built. This package is exactly what separates "ML engineer" from "AI architect" in an interview — it
demonstrates **judgment and ownership of tradeoffs**, the senior half of the role.

## Concepts to be able to explain
Component reasoning & failure-mode analysis; loose coupling / provider-swappability; build-vs-buy criteria
(cost-at-volume, latency, privacy, lock-in); horizontal scaling vs queuing vs graceful degradation; FinOps
cost drivers for LLMs; NIST AI RMF & EU AI Act in one breath; translating all of it into business value.

## Decision Lens (filled)
1. **Problem:** prove you can *own the design and tradeoffs* of an AI system, not just implement parts.
2. **Is ML right?** N/A — this is the **architecture** discipline around ML systems.
3. **Framing:** design + decision documentation. Baseline = "a working demo with no design rationale."
4. **Data reality:** the inputs are *your own* system's constraints + real current pricing/compliance facts.
5. **Metric:** could a reviewer make/defend the same decisions from your docs alone? (clarity, not cleverness)
6. **Cost of wrong:** an undocumented one-way-door decision (lock-in, a compliance miss) is the costly failure.
7. **Path to prod:** the package *is* the production plan — scaling, cost, and governance are pre-answered.
8. **Build vs leverage:** leverage your built system; **the architecture judgment is the deliverable.**

---
**Pairs with:** [Phase 9 — AI Solution Architecture](../../phases/phase-9-architecture.md) ·
templates in [`../../templates/`](../../templates/).
