# Phase 9 — AI Solution Architecture (optional, ≈4–6 weeks)

**Goal:** make the jump from *engineer* (who implements components) to **architect** (who designs the
end-to-end system and **owns the tradeoffs**). You won't learn new ML here — you'll learn to **specify,
select, scale, govern, and justify** AI systems, and to produce the artifacts an architect is judged on:
**architecture diagrams, Architecture Decision Records (ADRs), decision matrices, cost models, and
governance checklists.** *Portfolio of decisions > certificates.*

**Who/when:** do this **after Phases 6–8** (you need to have *built* systems before you can credibly
*architect* them). It pairs with the [`projects/`](../projects/README.md) you've already built — you'll
architect one of them properly. Targets **AI Architect / AI Solutions Architect / Staff+ ML** roles.

**Environment:** **🖥️ Local + 🆓 free-tier** by default — concepts, diagrams, and decision docs need no
spend; hands-on infra uses **free/local emulation** (k3d/minikube/kind for Kubernetes, Terraform OSS,
LocalStack for AWS, cloud free-tiers/credits). A few topics are only *real* on a live cloud — those are
marked **💳 (small cost, optional)**; do them on a free-tier/credit and **tear down** after.

**🔄 Freshness:** cloud services and pricing change constantly — always check **current** docs/pricing.
The **principles** (loose coupling, the Well-Architected pillars, NIST AI RMF, the EU AI Act risk tiers,
FinOps) are stable. Treat every specific product name (SageMaker/Bedrock/Vertex/Foundry) as an *example*.

> 🏗️ **This phase has no new builds — it has deliverables.** Each module's checkpoint produces one
> architect artifact; the capstone assembles them into a portfolio-grade **design package** for a system
> you already built. Templates live in [`../templates/`](../templates/).

**Primary resources** (open the link, then the **bold** item):
- [System Design Primer](https://github.com/donnemartin/system-design-primer) (free) · [ByteByteGo](https://bytebytego.com) — **scalability, queues, caching, load balancing** fundamentals
- [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) — **the 6 pillars** + the **Machine Learning Lens** & **Generative AI Lens** (free whitepapers)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) + **AI RMF Playbook** · [EU AI Act Explorer](https://artificialintelligenceact.eu/) (free)
- 📖 Chip Huyen — **[*Designing Machine Learning Systems*](https://huyenchip.com/) / [*AI Engineering*](https://huyenchip.com/)** (the canonical architect texts; her [blog](https://huyenchip.com/blog/) is free) · 📖 **[*ML Design Patterns*](https://www.oreilly.com/library/view/machine-learning-design/9781098115777/)** (Lakshmanan et al.)
- 📖 Kleppmann — **[*Designing Data-Intensive Applications*](https://dataintensive.net/)** (the data-systems bible) · [Google Cloud Architecture Center](https://cloud.google.com/architecture) (free reference architectures)
- [DataTalks.Club — **Data Engineering Zoomcamp**](https://github.com/DataTalksClub/data-engineering-zoomcamp) (free: Kafka, Spark, Airflow, dbt, Terraform, Docker) · [**MLOps Zoomcamp**](https://github.com/DataTalksClub/mlops-zoomcamp)

---

## Module 9A — Data & infrastructure architecture

*The substrate everything runs on.* An architect must know **where data lives, how it moves, and what
runs the compute** — even without operating it daily.

| # | Topic | Open exactly this | ~Time |
|---|-------|-------------------|-------|
| 1 | Data lakes / lakehouse / warehouse | [Data Engineering Zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp) — **"Data lake vs warehouse / lakehouse"** · 📖 [Databricks: Lakehouse](https://www.databricks.com/glossary/data-lakehouse) | 2h |
| 2 | **Batch vs streaming pipelines** | DE Zoomcamp — **Kafka** (streaming) + **Spark** (batch) + **Airflow/dbt** (orchestration) modules | 4h |
| 3 | **Feature stores** (train/serve consistency) | [Feast docs](https://docs.feast.dev) — **"What is a feature store / quickstart"** (free, OSS) | 1.5h |
| 4 | Containers → **Kubernetes** | [Kubernetes Basics](https://kubernetes.io/docs/tutorials/kubernetes-basics/) — run locally with **[k3d](https://k3d.io)/minikube/kind** (🆓 no cloud) | 3h |
| 5 | **Infrastructure-as-Code (Terraform)** | [HashiCorp — Terraform tutorials](https://developer.hashicorp.com/terraform/tutorials) (OSS, 🆓) — provision against **LocalStack** or a free tier | 2h |
| 6 | **Managed AI platforms** (know the tradeoffs) | [AWS SageMaker](https://docs.aws.amazon.com/sagemaker/) / [Bedrock](https://docs.aws.amazon.com/bedrock/) · [Google Vertex AI](https://cloud.google.com/vertex-ai/docs) · [Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/) — **what each is, when to pick it** (💳 only if you do a hands-on deploy) | 2h |

**✅ Checkpoint 9A** — 🖥️ Local / 🆓:
- **(T1–T2)** Draw a **data-flow diagram** for one of your `projects/`: where each datum is stored, how it
  moves (batch vs stream), and **mark every failure point**. (This is the article's foundational exercise.)
- **(T3)** Explain train/serve skew and how a feature store prevents it; sketch where it sits in your system.
- **(T4)** Run your `proj-06` (or any container) on a **local k3d/minikube** cluster; scale it to 3 replicas.
- **(T5)** Write a tiny **Terraform** file that provisions one resource against **LocalStack** (🆓).
- **(T6)** One paragraph: for *your* system, **self-host (open-weight) vs a managed platform** — which and why.

---

## Module 9B — AI system architecture design

*The core intellectual skill:* reason about **components, data flow, interfaces, state, and failure modes** —
and communicate it as a **diagram**.

| # | Topic | Open exactly this | ~Time |
|---|-------|-------------------|-------|
| 7 | Components, interfaces, state, failure modes | [System Design Primer](https://github.com/donnemartin/system-design-primer) — **"System design topics"** | 2h |
| 8 | **Architecture diagrams as the deliverable** | [C4 model](https://c4model.com) (context→container→component) — draw with [Excalidraw](https://excalidraw.com)/[draw.io](https://draw.io)/[Mermaid](https://mermaid.js.org) or [Diagrams-as-code](https://diagrams.mingrammer.com) | 2h |
| 9 | **Established AI patterns** | [AWS GenAI Lens](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/generative-ai-lens.html) + [Anthropic — Building Effective Agents](https://www.anthropic.com/research/building-effective-agents) — **RAG, multi-agent, routing gateway, batch vs real-time** | 2h |
| 10 | **Loose coupling & changeability** | Pattern: provider-/model-swappable behind an interface (gateway) — relate to your `proj-08` tool registry | 1h |
| 11 | Reference architectures (study real ones) | [Google Cloud Architecture Center](https://cloud.google.com/architecture) + [Azure Architecture Center](https://learn.microsoft.com/azure/architecture/) — **a GenAI/RAG reference arch** | 1.5h |

**✅ Checkpoint 9B** — 🖥️ Local:
- **(T8)** Produce a **C4 container diagram** for a **multi-agent customer-support system**: components,
  interfaces, where state is stored, and **3 named failure scenarios** + how each is handled. (Article exercise.)
- **(T10)** Refactor *on paper*: show how to swap the LLM provider in your design **without rewriting** the
  app — name the interface/seam that makes it possible.

---

## Module 9C — Technology selection & build-vs-buy

*Architects are paid for judgment.* Turn "which option?" into a **defensible, documented decision**.

| # | Topic | Open exactly this | ~Time |
|---|-------|-------------------|-------|
| 12 | **Open-weight vs managed proprietary** | [Designing the choice](https://huyenchip.com/blog/) — cost-at-volume, latency, **data privacy**, vendor lock-in, team capability, maintenance | 1.5h |
| 13 | **Architecture Decision Records (ADRs)** | [ADR collection](https://github.com/joelparkerhenderson/architecture-decision-record) + [adr.github.io](https://adr.github.io) — Nygard format · use [`../templates/adr-template.md`](../templates/adr-template.md) | 1h |
| 14 | **Decision matrix** (weighted scoring) | use [`../templates/decision-matrix-template.md`](../templates/decision-matrix-template.md) — criteria × weights × options | 1h |
| 15 | Failure modes: over-engineering / under-resourcing | When custom infra is wrong (use managed); when self-hosting without a team is wrong | 0.5h |

**✅ Checkpoint 9C** — 🖥️ Local:
- **(T12/T14)** Build a **decision matrix** comparing **open-weight vs proprietary** for one project, with
  *your* defined constraints (latency target, privacy, projected volume, team size). Pick a winner. (Article exercise.)
- **(T13)** Write a **one-page ADR** for that decision: context, options considered, decision, **consequences**.

---

## Module 9D — Scale, reliability & cost (SRE + FinOps for AI)

*Make it survive 10× traffic and a budget review.* AI adds two twists: **variable latency** and
**nondeterministic outputs**.

| # | Topic | Open exactly this | ~Time |
|---|-------|-------------------|-------|
| 16 | Horizontal scaling, **queuing**, load balancing | [System Design Primer](https://github.com/donnemartin/system-design-primer) — **"Scalability / message queues / load balancer"** | 2h |
| 17 | **Graceful degradation & fallback routing** | reduced-functionality-over-failure; secondary model / cached result — relate to your `proj` routing | 1h |
| 18 | **Semantic caching** (meaning, not string match) | your optional `projects/` "Semantic Cache Gateway" — where to place it, hit-rate vs staleness | 1h |
| 19 | AI reliability: variable latency, nondeterminism | timeouts, retries with backoff, idempotency, output validation (tie to `proj-03` guardrails) | 1h |
| 20 | **FinOps: cost modeling** | [FinOps Foundation](https://www.finops.org/introduction/what-is-finops/) (free framework) — model **token + inference + retrieval** cost at volume · use [`../templates/cost-model-template.md`](../templates/cost-model-template.md) | 1.5h |
| 21 | Distributed compute at scale | [Ray docs](https://docs.ray.io) (serving/scaling) · [Kubeflow](https://www.kubeflow.org/docs/) (pipelines) — **awareness + when you'd reach for them** | 1.5h |

**✅ Checkpoint 9D** — 🖥️ Local:
- **(T16/T18)** Take one project to **10× traffic** *on paper*: where do you add **queuing**, **horizontal
  scaling**, and a **semantic cache**? Mark it on your 9B diagram. (Article exercise.)
- **(T20)** Build a **monthly cost model** (baseline token/inference/retrieval cost) for that system at a
  stated request volume; show the **break-even** vs a managed API.

---

## Module 9E — Governance, compliance & business alignment

*The senior half of the role.* Make it **safe, compliant, and worth the money** — and explain it to
non-engineers.

| # | Topic | Open exactly this | ~Time |
|---|-------|-------------------|-------|
| 22 | **AWS Well-Architected** (pillars as a lens) | [Well-Architected](https://aws.amazon.com/architecture/well-architected/) — review your design against **reliability + security** pillars | 1.5h |
| 23 | **NIST AI Risk Management Framework** | [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework) + **Playbook** — Govern / Map / Measure / Manage | 2h |
| 24 | **EU AI Act** (risk-tiered compliance) | [EU AI Act Explorer](https://artificialintelligenceact.eu/) — **which risk tier** your system is, obligations | 1.5h |
| 25 | Data governance, security-by-design, **model cards** | [Google — Model Cards](https://modelcards.withgoogle.com/about) · PII/data-retention/access — extends [Thread C](../ROADMAP.md) | 1.5h |
| 26 | **Business communication & value/ROI** | express tradeoffs in **cost/risk/outcome** (not jargon); **define success metrics pre-deployment** & track ROI | 1.5h |

**✅ Checkpoint 9E** — 🖥️ Local:
- **(T23/T24/T25)** Fill an **[AI governance checklist](../templates/ai-governance-checklist.md)** for your
  system: NIST AI RMF functions, EU AI Act risk tier, a **risk section**, and an industry-compliance list. (Article exercise.)
- **(T26)** Write the **business case** in one page: the tradeoff in **cost/risk/outcome** terms a non-engineer
  understands, plus **≥2 measurable success outcomes** defined *before* you'd ship.

---

## 🏁 Phase 9 capstone — architect a system you already built

Pick one system from [`projects/`](../projects/README.md) (the **support copilot** `proj-01` and the
**permissioned agent sandbox** `proj-08` are the richest) and produce a portfolio-grade **design package** —
the exact artifacts an AI Architect is hired on. This is the
[**`capstones/ai-solution-architecture`**](../capstones/ai-solution-architecture/README.md) capstone:

1. **Architecture diagram** (C4) — components, interfaces, state, data flow, failure points.
2. **ADR** — the key technology decision (e.g. open-weight vs managed), options + consequences.
3. **Decision matrix** — weighted scoring behind that ADR.
4. **Cost model** — monthly token/inference/retrieval cost at a stated volume + break-even.
5. **Governance checklist** — NIST AI RMF + EU AI Act tier + risk section + success metrics/ROI.

Bundle them as a `docs/architecture/` folder (Markdown + diagram source) in that project's repo — a
recruiter can read it and see you think like an architect.

**Ready (architect-capable) when** you can take **any** AI problem and, on a whiteboard, sketch the system,
name the components and failure modes, state the build-vs-buy decision *with* its tradeoffs, estimate the
cost at volume, name its compliance tier, and explain all of it to a non-technical stakeholder in
cost/risk/outcome terms.

---

### Certifications for this track (optional, after the phase)

The article's thesis is **portfolio over credentials** — but if you want the cloud-architect signal:
**AWS Solutions Architect – Associate (SAA-C03)**, **Google Professional Cloud Architect**, or
**Azure Solutions Architect Expert (AZ-305)**. Study free via the Zoomcamps + free tiers; sit the exam only
once your design package above exists to back it up. (These complement — don't replace — the ML certs in the
[main roadmap](../ROADMAP.md).)
