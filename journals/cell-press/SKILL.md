---
name: cell-press
description: "Shared author-guideline skill for Cell Press journals that food & nutrition researchers publish in: Cell, Cell Metabolism, Cell Host & Microbe, Molecular Cell, Immunity, Current Biology, Cell Reports Medicine, One Earth, Joule, Matter, Chem. Use to format or check a manuscript for a Cell Press journal — structure with STAR Methods, abstract + eTOC blurb, Cell Press reference style, and figure specs. Triggers: submit to Cell, Cell Metabolism, Cell Host & Microbe guidelines, Cell Press formatting. Also fires when the user wants to publish on/in this journal, format a manuscript for it, or match its reference/citation style."
metadata:
  publisher: "Cell Press (Elsevier)"
  verified: "2026-11 partial"
  source: "https://www.cell.com/cell/authors"
---

# Cell Press — Author Guideline Skill

> **Verification status:** **Verified** for Cell Metabolism (article types) and Cell Reports Medicine (article types and final file requirements), 2026-11-27. Other Cell Press titles are **not verified**.
> Anything not listed here is unconfirmed: check the journal's guide, or ask the author to
> paste or upload it, before applying a limit.

**Publisher:** Cell Press (Elsevier). Sources: [Cell Metabolism article types](https://www.cell.com/cell-metabolism/information-for-authors/article-types), [Cell Reports Medicine final file requirements](https://www.cell.com/pb-assets/journals/EM/MasterFFCs/XCRMFFC-1790092543960.pdf).

## Applies to
Cell, Cell Metabolism, Cell Host & Microbe, Molecular Cell, Immunity, Current Biology,
Cell Reports Medicine, One Earth, Joule, Matter, Chem.

## Publisher-wide guidance (shared by both verified journals)
- **Research article:** under **7,000 words** (incl. main figure legends; excl. STAR Methods, references, supplemental legends), **≤7** figures + tables.
- **Short article / Report:** under **4,000 words**, **≤4** display items.
- Initial submission has no formatting requirement; the rules below apply to revision and final files.

## Final format (Cell Reports Medicine, verified)
- Order: Title → Authors → **Summary** → Introduction → Results → Discussion → Resource Availability → Acknowledgments → Author Contributions → Declaration of Interests → figure legends → tables → **STAR Methods** → supplemental titles → **References**.
- Title ≤145 characters. Summary: one paragraph, **≤150 words**.
- Resource Availability: Lead Contact, Materials Availability, Data and Code Availability.
- **References:** superscript numbers in citation order; include article title and DOI.
- **Highlights:** 3–4 bullets ≤85 characters. **eTOC blurb:** ≤50 words, third person. Graphical abstract: see final-file requirements.
- Figures as separate high-resolution TIFF or PDF files; editable Word tables.

## Formatting constraints
```yaml
publisher: Cell Press
reference_style: numbered-superscript
article_words: 7000
display_items_max: 7
summary_words: 150
highlights: {count: "3-4", max_chars: 85}
methods: STAR-Methods-after-figure-legends
data_and_code_availability: required
```
