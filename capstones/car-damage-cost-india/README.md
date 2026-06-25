# Capstone — Car-Damage Repair-Cost Estimator, India edition (CV × Tabular × MLOps)

> Your finance/insurance track × computer vision · ⭐⭐⭐⭐⭐
> From a photo of a damaged car, **detect the damaged parts** and **estimate the repair cost in ₹** — built
> for the Indian market with real Indian vehicles, Indian parts pricing, and a hardened, monitored service.
> This is the flagship that spans three phases at once: CV detection (Phase 4), tabular cost regression
> (Phase 3), and productionization (Phase 7).

> **Decision-support estimate, not a binding quote. Not insurance advice.** A model estimate must never be
> presented as a guaranteed payout; a human surveyor stays in the loop for real claims.

## v1 → v2: what this builds on

**v1 (upstream, done):** [`theDocWho/car-crash-fix-amount-predictor`](https://github.com/theDocWho/car-crash-fix-amount-predictor)
— ResNet50 / YOLOv8 / XGBoost, Gradio on HF Spaces, CI/CD, 64 tests, v1.0.0. It is **honest about its
limitation**: real per-image repair costs are paywalled (IAAI) or broken, so v1's cost target is **synthetic**
(catalog × severity × segment + noise) and data is US/international with a **USD→INR FX bolt-on**.

**v2 (this capstone):** make it genuinely **India-first and production-ready** — real Indian vehicles, an
**INR-native** parts catalog (no FX hack), India-relevant damage data, and serving hardening with monitoring.

## What changes for India

| v1 (US / synthetic) | v2 (India / this capstone) |
|---|---|
| Stanford Cars / international makes | **Indian makes & models** — Maruti Suzuki, Tata, Mahindra, Hyundai/Kia India, Toyota/Honda India |
| USD catalog → FX-converted to ₹ | **INR-native versioned parts catalogs** (₹ from the start, no FX) |
| US segments | **Indian segments** — hatchback / sedan / compact-SUV / SUV (incl. tax/segment quirks) |
| Generic damage images | India-relevant damage imagery (mix in CarDD + India-sourced photos where available) |
| Synthetic cost only | Synthetic **clearly labeled**, with a path to real garage/insurer-survey pricing |

**INR catalog sources (free / public):** Indian spare-parts e-commerce listings (e.g. Boodmo-style catalogs),
published insurer **motor-survey** labour rates, and authorized-service-centre price lists. Keep catalogs
**versioned** and reuse v1's **calibrator** so XGBoost can be rescaled to a new catalog **without full retrain**
(`activate <catalog_id>`).

## What's provided vs what you build

| Reuse from v1 (read it) | You build / adapt for India |
|---|---|
| `ccdp` CLI, model wrappers, three-tier fallback (exact → nearest → category) | INR catalogs + segment map; retrained detector; recalibrated regressor |
| Versioned YAML catalog + **calibrator** design | India catalog versions; calibrate XGBoost → ₹ catalog |
| Provenance/audit fields per prediction (`cost_inr`, `tier`, `catalog_id`, …) | drift monitoring + a hardened container |

## Stages
1. **India data + INR catalog** — assemble Indian make/model lists + an INR parts/labour catalog (versioned
   YAML); map vehicles to Indian segments. Document every price source.
2. **Retrain + recalibrate** — retrain the **YOLOv8** damage detector on the India-relevant image set;
   **recalibrate XGBoost** to the INR catalog via the calibrator (no full retrain needed). Report R²/MAPE.
3. **Harden serving** — containerized **FastAPI** (+ keep the Gradio demo); preserve v1's per-prediction
   provenance/audit; add **Evidently** drift monitoring (input image stats + predicted-cost distribution).
4. **Honest evaluation** — R²/MAPE on a **held-out India set**; calibration plot (predicted vs catalog);
   explicitly **document the synthetic-vs-real cost gap** and what real labels would change.

## Make it better — local ↔ cloud
- **(local)** train/recalibrate on an **M-series Mac** (~4h as in v1); stronger detector (YOLOv8m→l); richer,
  more granular INR catalog; per-segment calibration.
- **(free cloud)** retrain on free **Colab/Kaggle GPU**; serve on **HF Spaces (ZeroGPU)**; add a free
  **vision-LLM (Qwen2-VL)** cross-check on parts inference; push drift metrics to **Grafana Cloud free tier**.

## Done when
- [ ] Predictions are **₹-native** end-to-end (no FX step) and tied to a versioned INR `catalog_id`.
- [ ] Detector + regressor retrained/recalibrated for India; R²/MAPE reported on a held-out India set.
- [ ] Containerized API runs offline; every prediction carries provenance/audit + a confidence tier.
- [ ] Drift monitoring is live; the **synthetic-vs-real cost gap is documented**, not hidden.

## Concepts to be able to explain
Two-stage design (detect → cost) and why localization improves cost accuracy (v1: +9 pts R² with bounding-box
features); catalog **calibration** vs retraining; why honest treatment of synthetic targets matters; segment +
parts inference for Indian vehicles; drift monitoring for a vision+tabular service.

## Decision Lens (filled)
1. **Problem:** give an insurer/garage/owner a fast, defensible **₹ repair-cost estimate** from a damage photo.
2. **Is ML right?** Manual survey is slow + inconsistent; **CV detection + cost model** scales triage — but a human confirms real payouts. **Hybrid.**
3. **Framing:** object detection → tabular **regression**. Input = photo (+ vehicle); output = ₹ estimate + parts + confidence. Baseline = segment-average cost.
4. **Data reality:** **no public real per-image ₹ costs** → target is synthetic (labeled as such); image distribution shift (India roads/vehicles); leakage between detector + cost features to avoid.
5. **Metric:** **MAPE** (relative ₹ error is what users feel) + R²; bar: beat v1's MAPE 24.4% on the India set, or document why not.
6. **Cost of wrong:** an over-estimate inflates premiums/claims; under-estimate shortchanges the owner → calibrate + keep a human gate; never present as a final quote.
7. **Path to prod:** real-time API + batch; monitor image drift + predicted-cost drift (Evidently); re-version catalog as prices move.
8. **Build vs leverage:** YOLOv8/XGBoost libs; **the INR catalog, calibrator, and honest eval are your contribution** — and the interview story is *how you handled missing real labels*.

---
**Related:** the LLM/system side of production lives in the [`projects/`](../../projects/README.md) track;
this capstone is the **CV × tabular × MLOps** flagship of the finance/insurance domain.
