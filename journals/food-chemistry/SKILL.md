---
name: food-chemistry
description: "Author-guideline skill for Food Chemistry (Elsevier, ISSN 0308-8146). Use when preparing, formatting, or checking a manuscript for submission to Food Chemistry — structure, word/abstract limits, Highlights, graphical abstract, APA author–date references, and figure specs. Triggers: submit to Food Chemistry, Food Chem guidelines, format for Food Chemistry. Also fires when the user wants to publish on/in this journal, format a manuscript for it, or match its reference/citation style."
metadata:
  publisher: Elsevier
  issn: "0308-8146"
  verified: "2026-11 partial"
  source: "https://www.sciencedirect.com/journal/food-chemistry/publish/guide-for-authors"
---

# Food Chemistry — Author Guideline Skill

> **Verification status:** **Partly verified** — the publisher blocks direct access; only search-engine excerpts of the official ScienceDirect guide were read (2026-11-27). Items marked *unconfirmed* were not.
> Anything not confirmed must be checked at the journal's guide before submission. Tell the
> author so, and ask them to paste or upload the current guide if it cannot be read.

**Publisher:** Elsevier · **ISSN:** 0308-8146 · **Source:** [Guide for Authors](https://www.sciencedirect.com/journal/food-chemistry/publish/guide-for-authors).

## Aims & scope
Food Chemistry publishes original, rigorous **analytical/chemistry-driven** research on the chemistry of food: composition and structure, bioactive compounds, analysis and authentication, processing chemistry, food safety (chemical), and sensory-linked chemistry tied to identified compounds. The bar is **chemical insight from validated methods** — not descriptive screening. Studies must report validated methods, adequate controls, genuine replication, and defensible quantification. Scope-mismatched food-engineering or purely sensory work is desk-rejected.

## Article types
Original Research Articles; Review Articles (usually invited or pre-proposed); Short Communications; Analytical Methods papers. Rapid, well-validated method papers are welcome.

## Manuscript structure
Title page → Abstract → Keywords → 1. Introduction → 2. Materials and methods → 3. Results and discussion → 4. Conclusions → (Declarations) → References → Figure/table legends. Use **continuous line numbering** and page numbers.

- **Abstract:** unstructured, single paragraph (*word limit unconfirmed*).
- **Keywords:** 1–7, in English.
- **Highlights (required):** required; a separate editable file (3–5 bullets, ≤85 characters each is the usual Elsevier rule — *unconfirmed* here).
- **Graphical abstract** (*requirement unconfirmed*): one concise image submitted as a separate file, legible at Elsevier's display size.

## Reference style
**APA style, author–date** (official guide excerpt). In-text `(Author & Author, 2023)`; reference list alphabetical, then chronological.

Example (journal article):
> Author, A. B., & Author, C. D. (2023). Title of the article. *Food Chemistry*, *400*, Article 133912. https://doi.org/10.1016/j.foodchem.2023.133912

## Figures & tables
- Vector where possible (EPS/PDF); raster: halftone ≥300, combination ≥500, line art ≥1000 dpi (Elsevier artwork guide). TIFF/JPEG accepted.
- Fit one (~90 mm) or two (~190 mm) column widths; embed fonts; consistent, legible labels.
- Tables editable (not images); cite all figures/tables in order.

## Method-validation requirements (journal-specific)
Report linearity, LOD/LOQ, recovery, precision, and quantitative concentrations. Compound identification needs authentic standards or MS/MS confirmation (not library hits alone). Bioactivity claims must be backed by chemistry; chemometric models must be validated; avoid single-batch-only conclusions.

## Submission checklist
- [ ] Highlights file · [ ] Graphical abstract (check) · [ ] Abstract within the guide's limit
- [ ] APA author–date references, DOIs included · [ ] Line + page numbering
- [ ] Declaration of interest · [ ] Data availability statement · [ ] CRediT author contributions
- [ ] Figures ≥300 dpi, correct column widths · [ ] Cover letter stating scope fit and novelty

## Formatting constraints
```yaml
journal: Food Chemistry
publisher: Elsevier
reference_style: author-date-apa
abstract_words: confirm-at-source
keywords: {min: 1, max: 7}
highlights: {count: "3-5", max_chars: 85, required: true}
graphical_abstract: confirm-at-source
line_numbering: required
figure_dpi: {halftone: 300, line_art: 1000}
column_widths_mm: [90, 190]
```
