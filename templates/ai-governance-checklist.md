# AI Governance & Compliance Checklist — <system name>

> One page to show a system is **safe, compliant, and accountable** — mapped to the frameworks an AI
> architect is expected to know: **NIST AI RMF**, the **EU AI Act**, and the **AWS Well-Architected** lenses.
> Extends [Thread C](../ROADMAP.md) (Responsible AI). Used in [Phase 9](../phases/phase-9-architecture.md).
> *This is a self-assessment aid, not legal advice — consult counsel for real compliance.*

- **System:** ____ · **Owner:** ____ · **Date:** YYYY-MM-DD

## 1. EU AI Act — risk tier
☐ Prohibited ☐ **High-risk** (e.g. credit, employment, biometrics, critical infra) ☐ Limited (transparency
duties — e.g. "you're talking to AI") ☐ Minimal.
→ Tier: **____** · obligations that follow: ____

## 2. NIST AI RMF — four functions
- **Govern** — who owns AI risk? policy, roles, escalation path: ____
- **Map** — context, intended use, **who could be harmed**, foreseeable misuse: ____
- **Measure** — metrics for accuracy, **bias/fairness**, robustness, security; how monitored: ____
- **Manage** — mitigations, human-in-the-loop, incident response, **kill switch / rollback**: ____

## 3. Security & data governance (Well-Architected: security + reliability)
- ☐ PII identified, minimized, **redacted** where possible (tie to [guardrails](../projects/proj-03-guardrail-service/README.md))
- ☐ Data retention & access controls defined · ☐ secrets management · ☐ audit logging of decisions
- ☐ Prompt-injection / OWASP-LLM-Top-10 reviewed (tie to [BYO-16](../challenges/byo-16-llm-redteam/README.md))
- ☐ Security-by-design: failure is **safe** (degrade, don't leak); least-privilege for tools/agents

## 4. Responsible AI
- ☐ **Model card** published (intended use, limits, eval data, known biases)
- ☐ Fairness/bias audited on relevant subgroups · ☐ interpretability available (SHAP/LIME) where decisions affect people
- ☐ Human oversight + appeal path for high-impact outputs

## 5. Risk register (top risks)
| Risk | Likelihood | Impact | Mitigation | Owner |
|---|---|---|---|---|
| | | | | |

## 6. Business value & success (define *before* shipping)
- Problem in stakeholder terms (cost/risk/outcome): ____
- **≥2 measurable success metrics** (with target + how tracked): 1) ____ 2) ____
- ROI / cost-of-not-doing-it: ____ · **revisit trigger:** ____
