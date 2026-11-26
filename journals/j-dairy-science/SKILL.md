---
name: j-dairy-science
description: "Author-guideline skill for Journal of Dairy Science (Elsevier on behalf of ADSA, ISSN 0022-0302). Use to format or check a manuscript for JDS — its distinct interpretive summary, section structure, author–date references, and figure specs differ from generic Elsevier journals. Triggers: submit to Journal of Dairy Science, JDS guidelines, ADSA formatting. Also fires when the user wants to publish on/in this journal, format a manuscript for it, or match its reference/citation style."
metadata:
  publisher: "Elsevier / American Dairy Science Association (ADSA)"
  issn: "0022-0302"
  verified: "2026-11 partial"
  source: "https://www.journalofdairyscience.org/content/authorinfo"
---

# Journal of Dairy Science (JDS) — Author Guideline Skill

> **Verification status:** **Partly verified** — search excerpts of the official JDS instructions PDFs (2026-11-27); the journal site blocks direct access.
> Anything not confirmed must be checked at the journal's guide before submission. Tell the
> author so, and ask them to paste or upload the current guide if it cannot be read.

**Publisher:** Elsevier for ADSA · **ISSN:** 0022-0302 · **Source:** [Author info](https://www.journalofdairyscience.org/content/authorinfo).

## Aims & scope
Original research on dairy science: dairy foods (chemistry, microbiology, processing, safety), animal nutrition, physiology, genetics, management, and dairy production. Rigorous methodology and statistics expected.

## Article types
Research articles; Short communications; Reviews; Hot topics; Technical notes.

## Manuscript structure (JDS-specific)
Title page → **Interpretive Summary** (required, ≤100 words) → Abstract → Keywords → Introduction → Materials and Methods → Results → Discussion (or combined Results and Discussion) → Conclusions → Acknowledgments → References → Tables → Figure legends → Figures. Continuous line numbers required.

- **Abstract:** single paragraph, no citations (*word limit unconfirmed*).
- **Interpretive summary:** required; concise significance for a broad audience.
- **Keywords:** 2–5.
- **Highlights:** 3–5 bullets ≤85 characters, uploaded with the graphical abstract in one separate file.

## Reference style
**Author–date (name–year)**, ADSA/JDS format. In-text `(Author and Author, 2023)`; list alphabetical.

Example:
> Author, A. B., C. D. Author, and E. F. Author. 2023. Title of paper. J. Dairy Sci. 106:1234–1245. https://doi.org/10.3168/jds.2023-xxxxx

## Figures & tables
Editable tables; figures ≥300 dpi (line art higher); grayscale/color per online/print policy; SI units; report means with SEM and the statistical model.

## Statistics (journal-specific)
JDS expects clear experimental design, the mixed-model/ANOVA structure, error terms, and appropriate multiple-comparison procedures; report P-values and SEM.

## Submission checklist
- [ ] Interpretive summary ≤100 words · [ ] Abstract · [ ] 2–5 keywords · [ ] Highlights + graphical abstract
- [ ] Author–date (ADSA) references with DOIs · [ ] Line + page numbering
- [ ] Statistical model + SEM reported · [ ] Animal-care/ethics statement if applicable
- [ ] Figures ≥300 dpi · [ ] Cover letter

## Formatting constraints
```yaml
journal: Journal of Dairy Science
publisher: Elsevier/ADSA
reference_style: author-date
interpretive_summary: {required: true, words: 100}
abstract_words: confirm-at-source
keywords: {min: 2, max: 5}
highlights: {count: "3-5", max_chars: 85}
line_numbering: required
figure_dpi: {halftone: 300, line_art: 1000}
```
