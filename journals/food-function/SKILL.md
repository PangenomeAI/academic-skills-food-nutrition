---
name: food-function
description: "Shared author-guideline skill for Royal Society of Chemistry food journals: Food & Function and Sustainable Food Technology. Use to format or check a manuscript for an RSC food journal — article types, structure, RSC superscript-numbered references with article titles, and figure specs. Triggers: submit to Food & Function, Sustainable Food Technology guidelines, RSC food formatting. Also fires when the user wants to publish on/in this journal, format a manuscript for it, or match its reference/citation style."
metadata:
  publisher: "Royal Society of Chemistry"
  verified: "2026-11"
  source: "https://www.rsc.org/publishing/publish-with-us/publish-a-journal-article/food-and-function"
---

# RSC Food Journals — Shared Author Guideline Skill

> **Verification status:** **Verified** — checked 2026-11-27 against the official author guide (RSC pages for both journals).

**Publisher:** Royal Society of Chemistry · Sources: [Food & Function](https://www.rsc.org/publishing/publish-with-us/publish-a-journal-article/food-and-function), [Sustainable Food Technology](https://www.rsc.org/publishing/publish-with-us/publish-a-journal-article/sustainable-food-technology).

## Applies to
| Journal | Abbrev | Scope |
|---|---|---|
| Food & Function | FOOD FUNCT | Chemistry and physics of food linked with health and nutrition |
| Sustainable Food Technology | SUSTAIN FOOD TECHNOL | Sustainable food processing/technology (open access) |

## Article types (Food & Function)
Communications (preliminary, urgent; include a short justification), Full papers (no page limit), Reviews (no length/figure/reference limits; PRISMA recommended for systematic reviews), Comments.

## Manuscript structure
Title → Authors & affiliations → Abstract → Introduction → **Experimental** → **Results and discussion** → Conclusions → Author contributions → Conflicts of interest → Data availability → Acknowledgements → References.

- **Experimental comes before Results and discussion.** If section numbers are used, renumber them after any reorder (`food-paper/references/section-renumbering.md`).
- **Abstract:** single paragraph, about 50–250 words.
- **Author contributions:** strongly encouraged (CRediT); required statement if more than 10 authors.
- **Conflicts of interest:** required (“There are no conflicts to declare” if none).
- **Data availability statement:** required.
- **Acknowledgements:** include funding and any AI-tool use.
- Live-animal studies: follow ARRIVE 2.0 and submit the checklist (Food & Function).

## Reference style
Vancouver (numbered, **not** Harvard). Superscript numbers in citation order, usually after punctuation; `12,13`, `14–20`. List **all authors**; **article title is required**; journal abbreviations per CASSI; DOI optional.

Format: `A. Name, B. Name and C. Name, Article title, Journal Title, year, volume, page/article number(s), DOI [optional].`

## Figures, TOC entry & submission
- Figures, schemes, charts: TIFF ≥600 dpi (EPS/PDF accepted); width 8.3 cm (single) or 17.1 cm (double), height ≤23.3 cm; colour free.
- **Table of contents entry** (submitted at **revision**): graphic ≤8 × 4 cm, TIFF ≥600 dpi, plus 1–2 sentences, ≤250 characters.
- On submission: cover letter stating the importance of the work; preferred reviewers.

## Submission checklist
- [ ] Introduction → Experimental → Results and discussion → Conclusions (numbers re-checked)
- [ ] Abstract 50–250 words · [ ] Vancouver superscript references with article titles
- [ ] Conflicts of interest + Data availability · [ ] Author contributions (CRediT)
- [ ] Figures TIFF ≥600 dpi · [ ] Cover letter · [ ] TOC entry ready for revision

## Formatting constraints
```yaml
publisher: RSC
reference_style: rsc-superscript-numbered
require_article_titles: true
abstract_words: {min: 50, max: 250}
section_order: [introduction, experimental, results_and_discussion, conclusions]
methods_section: before-results   # "Experimental"
conflicts_statement: required
data_availability: required
toc_entry: {stage: revision, size_cm: [8, 4], text_max_chars: 250}
figure_dpi: 600
column_widths_cm: [8.3, 17.1]
```
