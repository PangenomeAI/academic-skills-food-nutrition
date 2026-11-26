---
name: cambridge-nutrition
description: "Shared author-guideline skill for Cambridge University Press nutrition journals: British Journal of Nutrition, Nutrition Research Reviews, Proceedings of the Nutrition Society, Public Health Nutrition, Journal of Nutritional Science. Use to format or check a manuscript for a Cambridge nutrition journal — structure, abstract limits, Vancouver references, and figure specs. Triggers: submit to British Journal of Nutrition, Nutrition Research Reviews, Proceedings of the Nutrition Society guidelines, Cambridge nutrition formatting. Also fires when the user wants to publish on/in this journal, format a manuscript for it, or match its reference/citation style."
metadata:
  publisher: "Cambridge University Press"
  verified: "2026-11 partial"
  source: "https://www.cambridge.org/core/journals/british-journal-of-nutrition/information/instructions-contributors"
---

# Cambridge Nutrition Journals — Shared Author Guideline Skill

> **Verification status:** **Verified** for British Journal of Nutrition and in part for NRR, PHN, PNS and JNS (Cambridge Core, 2026-11-27). Agriculture titles **not verified**.
> Anything not confirmed must be checked at the journal's guide before submission. Tell the
> author so, and ask them to paste or upload the current guide if it cannot be read.

**Publisher:** Cambridge University Press · Confirm each journal's "Instructions for Contributors" on Cambridge Core.

## Applies to
| Journal | Abbrev | Type focus |
|---|---|---|
| British Journal of Nutrition | BRIT J NUTR | Human & animal nutrition research |
| Nutrition Research Reviews | NUTR RES REV | Reviews |
| Proceedings of the Nutrition Society | P NUTR SOC | Symposium/review papers |
| Public Health Nutrition | PUBLIC HEALTH NUTR | Population nutrition |
| Journal of Nutritional Science | J NUTR SCI | Open-access research |

## Manuscript structure
Title page → Abstract → Keywords → Introduction → (Experimental/Methods) → Results → Discussion → Acknowledgements → Financial support → Conflicts of interest → Authorship → References → Tables → Figure legends.

- **Abstract:** BJN — unstructured, single paragraph, ≤250 words, no subheadings. NRR — single paragraph ≤250. JNS — unstructured ≤250 (150 for Brief Reports and Perspectives).
- **Keywords:** at least 4, each up to 3 words (BJN, NRR, JNS); 3–4 for Proceedings of the Nutrition Society.
- **Length:** PHN research article ≤5,000 words and ≤50 references (systematic/scoping review ≤100 references); PNS papers ≤7,000 words excluding references; BJN introduction ≤2 manuscript pages.
- **Graphical abstract:** mandatory for review articles (BJN) and full reviews (NRR).
- **Human/clinical studies:** ethics approval + trial registration (where applicable), following ICMJE and the relevant reporting guideline (CONSORT/STROBE/PRISMA).

## Reference style
**British Journal of Nutrition: Vancouver, numbered.** Superscript Arabic numerals **in parentheses**, in order of first appearance, e.g. `highlighted(1,2)`. More than three authors: first three then *et al.*; abbreviated journal titles.

NRR and PHN are also numbered (Citation Style Language repository). Proceedings of the Nutrition Society and Journal of Nutritional Science: *confirm*. Cambridge agriculture titles (e.g. Journal of Agricultural Science, Renewable Agriculture and Food Systems) are author–date per that repository.

## Figures & tables
Figures ≥300 dpi (line art higher); TIFF/EPS/PDF; editable tables; SI units; cite in order.

## Submission checklist
- [ ] Abstract ≤250 words · [ ] Keywords per journal · [ ] Reference style per journal (BJN: Vancouver)
- [ ] Financial support + Conflicts of interest + Authorship statements
- [ ] Ethics/trial registration + reporting guideline for human/clinical studies
- [ ] Figures ≥300 dpi · [ ] Cover letter

## Formatting constraints
```yaml
publisher: Cambridge University Press
reference_style: per-journal   # BJN/NRR/PHN numbered
abstract_words: 250
keywords_min: 4
declarations: [financial_support, conflicts_of_interest, authorship]
clinical: [ethics, trial_registration, reporting_guideline]
figure_dpi: {halftone: 300, line_art: 1000}
```
