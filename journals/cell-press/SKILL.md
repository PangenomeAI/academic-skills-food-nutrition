---
name: cell-press
description: "Shared author-guideline skill for Cell Press journals that food & nutrition researchers publish in: Cell, Cell Metabolism, Cell Host & Microbe, Molecular Cell, Immunity, Current Biology, Cell Reports Medicine, One Earth, Joule, Matter, Chem. Use to format or check a manuscript for a Cell Press journal — structure with STAR Methods, abstract + eTOC blurb, Cell Press reference style, and figure specs. Triggers: submit to Cell, Cell Metabolism, Cell Host & Microbe guidelines, Cell Press formatting. Also fires when the user wants to publish on/in this journal, format a manuscript for it, or match its reference/citation style."
metadata:
  publisher: "Cell Press (Elsevier)"
  verified: "2026-11 partial"
  source: "https://www.cell.com/cell/authors"
---

# Cell Press — Author Guideline Skill

> **Verification status:** **Partly verified** — search excerpts of cell.com author documents (2026-11-27); direct access blocked.
> Anything not confirmed must be checked at the journal's guide before submission. Tell the
> author so, and ask them to paste or upload the current guide if it cannot be read.

**Publisher:** Cell Press (Elsevier) · Confirm the exact reference style and limits at the specific journal's Guide for Authors (Cell Press has updated citation formats; verify current style).

## Applies to (food/nutrition-relevant)
| Journal | Abbrev | Relevance |
|---|---|---|
| Cell | CELL | Flagship |
| Cell Metabolism | CELL METAB | Nutrition & metabolism |
| Cell Host & Microbe | CELL HOST MICROBE | Gut/food microbiome |
| Molecular Cell | MOL CELL | Molecular |
| Immunity | IMMUNITY | Nutr-immunology |
| Current Biology | CURR BIOL | Broad biology |
| Cell Reports Medicine | CELL REP MED | Clinical/translational |
| One Earth | ONE EARTH | Food systems/sustainability |
| Joule / Matter / Chem | — | Energy/materials/chemistry |

## Format (Cell Press style)
- **References:** numbered in citation order — **superscript numbers** in Cell-style research journals; some titles (e.g. Trends journals) use square brackets. Include DOIs.
- **Abstract:** ≤150 words, single paragraph; plus a short **eTOC blurb** (one–two sentences) and a **graphical abstract** for many titles; **Highlights** (count/length differ by title; *confirm*).
- **Structure:** Title → Abstract → Introduction → Results → Discussion → **STAR★Methods** (structured methods) → References → Figure legends. Research articles use STAR Methods (required at acceptance, optional at first submission; subheadings ≤45 characters, unnumbered).
- **Display items:** cite `Figure 1` in order; supplemental information allowed.
- **Mandatory:** data/code availability (STAR Methods Key Resources Table), declaration of interests, author contributions.
- **Figures:** ≥300 dpi; RGB; Cell column widths; accessible palette.

## Formatting constraints
```yaml
publisher: Cell Press
reference_style: cell-press   # numbered superscript
abstract_words: 150
highlights: confirm-at-source
graphical_abstract: common
methods: STAR-Methods
data_and_code_availability: required
figure_dpi: 300
```
