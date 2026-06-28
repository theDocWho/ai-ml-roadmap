# Decision Matrix — <decision name>

> **Weighted-scoring matrix** for a build-vs-buy or option-A-vs-B technology choice (e.g. open-weight vs
> managed proprietary model). Makes a judgment **defensible**: criteria, weights, and scores are explicit,
> so reviewers argue about *inputs*, not vibes. Pairs with an [ADR](adr-template.md). Used in
> [Phase 9](../phases/phase-9-architecture.md).

## 1. The decision
"Choose ____ for ____." Options being compared: **A**, **B**, **C**.

## 2. Criteria & weights
Pick the criteria that matter *for this system*; weights sum to 100. (Typical AI-system criteria below —
keep/cut to fit.)

| Criterion | Weight | Why it matters here |
|---|---|---|
| Capability / quality on the task | | |
| **Cost at projected volume** | | (model with [cost-model-template](cost-model-template.md)) |
| Latency (p95) | | |
| **Data privacy / residency** | | (does data leave our environment?) |
| Vendor lock-in / changeability | | |
| Operational burden / team capability | | |
| Time-to-ship | | |
| **Total** | **100** | |

## 3. Score each option (1–5; 5 = best)
| Criterion (weight) | A | B | C |
|---|---|---|---|
| Capability (__) | | | |
| Cost@volume (__) | | | |
| Latency (__) | | | |
| Privacy (__) | | | |
| Lock-in (__) | | | |
| Ops burden (__) | | | |
| Time-to-ship (__) | | | |
| **Weighted total** (Σ weight×score) | | | |

## 4. Result
Winner: **____**. The score is **advice, not autopilot** — note any deal-breaker (a hard privacy/compliance
constraint can veto a higher-scoring option) and any criterion the result is most **sensitive** to.

## 5. Decision → record it
Carry the winner + the accepted tradeoffs into an **[ADR](adr-template.md)**.
