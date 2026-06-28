# Cost Model — <system name>

> **FinOps for AI.** A back-of-envelope monthly cost model so an architect can answer "what does this cost at
> volume, and where's the break-even vs a managed API?" *before* committing. The three AI cost drivers are
> **tokens, inference compute, and data retrieval.** Used in [Phase 9](../phases/phase-9-architecture.md).

## 1. Workload assumptions
- Requests/day: ____ → requests/month (×30): ____
- Avg **input tokens**/request: ____ · avg **output tokens**/request: ____
- Retrieval/request: ____ vector queries · embeddings re-indexed/month: ____ docs
- Peak factor (for sizing, not cost): ____×

## 2. Per-unit prices (fill from current pricing — they change!)
| Item | Unit | Price |
|---|---|---|
| LLM input | per 1M tokens | |
| LLM output | per 1M tokens | |
| Embeddings | per 1M tokens | |
| Vector DB | per month (tier) or per query | |
| Compute (self-host) | GPU/CPU instance-hour | |

## 3. Monthly cost — two scenarios
| Cost line | Managed API | Self-hosted (open-weight) |
|---|---|---|
| LLM input tokens | reqs × in-tok × price | (amortized in compute) |
| LLM output tokens | reqs × out-tok × price | (amortized in compute) |
| Embeddings / re-index | | |
| Vector store | | |
| Compute (instances × hrs × price) | — | |
| Ops/maintenance (eng time est.) | low | **higher** |
| **Total / month** | | |

## 4. Break-even & verdict
- **Break-even volume:** at ____ requests/month the two columns cross; below it managed wins, above it
  self-host wins (on $, before ops effort).
- **Levers if too expensive:** smaller/quantized model · **semantic cache** (cuts repeat calls) · shorter
  prompts/context · batch off-peak · cheaper embeddings + reranker · route easy queries to a small model.
- **Verdict (1 line):** ____ — feed this into the [decision matrix](decision-matrix-template.md) / [ADR](adr-template.md).

> Estimates are directional — label them as such, and re-check against real usage after launch (this is a
> monitoring metric, not a one-time guess).
