# proj-05 — Multimodal Document Intake Reviewer

> Reinforces: OCR · vision-LLM extraction · validation · human-in-the-loop · Phase 6B–7 · ⭐⭐⭐
> Accept scanned forms / PDFs / photos → extract **structured fields** → validate them → route low-confidence
> results to a human. This is the workhorse of real-world AI (insurance, KYC, invoices) and a clean showcase
> of *multimodal + confidence-aware routing*.

## 🆓 Free stack (vs the paid version)

| The guide says (paid) | Use this (free, capable) |
|---|---|
| GPT-4o / Claude vision | **Qwen2-VL** / **Llama-3.2-Vision** via **Ollama** |
| (managed OCR) | **Tesseract** / **EasyOCR** + **PyMuPDF** |
| — | **Pydantic** (schema) · **Streamlit/React** review UI · SQLite · Docker Compose |

## What you'll build
A pipeline + review UI: upload a document → preprocess → OCR (text layer) **with a vision-LLM fallback** for
hard scans → extract fields into a Pydantic schema with **per-field confidence** → validate (types, ranges,
cross-field rules) → auto-accept high-confidence, **queue low-confidence for human review**.

## Stages
1. **Upload & preprocess** — accept PDF/image; deskew/denoise; split pages (PyMuPDF).
2. **OCR + vision fallback** — Tesseract/EasyOCR first; if confidence/coverage is low, send the page image to a
   **local vision-LLM** to read fields directly.
3. **Structured extraction** — map to a Pydantic schema (e.g. claim/invoice fields) with a confidence per field.
4. **Validation & routing** — type/range/cross-field checks; route by confidence threshold (auto-accept vs human queue).
5. **Review UI + analytics** — reviewer corrects fields; track auto-accept rate, field-level accuracy, throughput.

## Dataset / inputs
A small set of sample forms/invoices (public templates or synthetic) with hand-labeled ground-truth fields.

## Make it better — local ↔ cloud
- **(local)** larger vision model for messy scans; learn per-field thresholds from review corrections;
  add layout parsing for tables.
- **(free cloud)** **Gemini free vision tier** for the hardest pages; deploy the reviewer on **HF Spaces**;
  feed reviewer corrections back as eval data (→ proj-07).

## Done when
- [ ] End-to-end: upload → structured, validated fields with confidences.
- [ ] Low-confidence items land in the human queue; corrections persist.
- [ ] Field-level accuracy + auto-accept rate reported.
- [ ] Runs offline (local OCR + local vision model).

## Concepts to be able to explain
OCR vs vision-LLM extraction (when each wins); calibrating confidence to a routing threshold; human-in-the-loop
as a precision lever; why field-level (not doc-level) accuracy is the right metric.

## Decision Lens (filled)
1. **Problem:** turn messy documents into trustworthy structured data with minimal human effort.
2. **Is ML right?** Templates fail on varied real-world scans → ML extraction + targeted human review.
3. **Framing:** extraction + per-field classification/confidence. Baseline = OCR + regex field-grab.
4. **Data reality:** scan quality varies wildly; labels need careful field-level ground truth.
5. **Metric:** **field-level accuracy** at a chosen **auto-accept rate** (precision-first). Bar: ≥0.98 on auto-accepted fields.
6. **Cost of wrong:** an auto-accepted wrong field flows downstream → keep auto-accept high-precision, route the rest.
7. **Path to prod:** batch + on-demand API; monitor auto-accept precision drift as document mix changes.
8. **Build vs leverage:** OCR/vision libs; **the confidence→routing policy is your contribution**.
