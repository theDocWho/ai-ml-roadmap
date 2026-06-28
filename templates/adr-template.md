# ADR-NNNN — <short decision title>

> **Architecture Decision Record.** One per significant, hard-to-reverse decision. Keep it to one page.
> An ADR is the upgrade from a [Decision Lens](decision-lens-template.md): the Lens frames *whether/how* to
> use ML; the ADR records *which technology/approach you chose and why* — so future-you (and reviewers)
> can see the reasoning, not just the result. (Nygard format.) Used in [Phase 9](../phases/phase-9-architecture.md).

- **Status:** ☐ proposed ☐ accepted ☐ superseded by ADR-____ ☐ deprecated
- **Date:** YYYY-MM-DD · **Decision owner:** ____ · **Stakeholders:** ____

## Context
What's the situation and the forces at play? Constraints (latency, privacy, budget, team size, deadline),
requirements, and assumptions. State the problem **neutrally** — don't pre-bake the answer.

## Decision
The choice, in one sentence: **"We will use ____ because ____."**

## Options considered
| Option | Pros | Cons | Why (not) chosen |
|---|---|---|---|
| **A — <chosen>** | | | ✅ chosen |
| B — <alt> | | | |
| C — do nothing / defer | | | |

> Back the scoring with a [decision-matrix](decision-matrix-template.md) when the choice is close.

## Consequences
- **Positive:** what gets easier/better.
- **Negative / accepted tradeoffs:** what gets harder, what risk you're accepting, the new lock-in or cost.
- **Follow-ups:** what this forces later (migration path, monitoring, a revisit trigger — e.g. "re-evaluate
  if volume > N req/day or if the managed price changes").

## Reversibility
☐ easy to reverse (low stakes) ☐ costly to reverse (one-way door — justify the extra rigor).
