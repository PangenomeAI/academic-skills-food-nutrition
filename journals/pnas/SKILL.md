---
name: pnas
description: "Author-guideline skill for PNAS (Proceedings of the National Academy of Sciences), a multidisciplinary journal food & nutrition researchers publish in. Use to format or check a manuscript for PNAS — structure, mandatory Significance Statement, abstract limit, PNAS numbered references, and figure specs. Triggers: submit to PNAS, Proceedings of the National Academy of Sciences guidelines, PNAS formatting. Also fires when the user wants to publish on/in this journal, format a manuscript for it, or match its reference/citation style."
metadata:
  publisher: "National Academy of Sciences (PNAS)"
  verified: "2026-11"
  source: "https://www.pnas.org/author-center/submitting-your-manuscript"
---

# PNAS — Author Guideline Skill

> **Verification status:** **Verified** on the PNAS author center, 2026-11-27.
> Anything not listed here is unconfirmed: check the journal's guide, or ask the author to
> paste or upload it, before applying a limit.

**Publisher:** National Academy of Sciences · [Submitting your manuscript](https://www.pnas.org/author-center/submitting-your-manuscript)

## Article types
- **Research Report:** preferred 6 pages (about 4,000 words, 50 references, 4 medium figures/tables); maximum 12 pages.
- **Brief Report:** 3 pages (about 1,600 words incl. title page, abstract, legends), 15 references.

## Structure
Title page (title under 135 characters, authors, **classification**, ≥3 keywords) → **Abstract** (≤250 words) → **Significance Statement** (≤120 words; direct and contributed submissions) → Introduction → Results → Discussion → **Materials and Methods** → References → Figure legends.

- Initial manuscript may be in any format. Extra tables/figures do not go in supporting information beyond what the journal allows.
- Reference style: numbered (Citation Style Language repository; confirm formatting).
- Figures at final size: 300 ppi (no lettering), 600–900 ppi (with type), 1000–1200 ppi (line art); RGB; editable tables.

## Formatting constraints
```yaml
journal: PNAS
reference_style: pnas-numbered
abstract_words: 250
significance_statement: {required: true, words_max: 120}
section_order: [introduction, results, discussion, materials_and_methods]
figure_dpi: {halftone: 300, combination: 600, line_art: 1000}
```
