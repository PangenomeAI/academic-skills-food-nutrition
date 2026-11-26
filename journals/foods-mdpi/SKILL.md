---
name: foods-mdpi
description: "Shared author-guideline skill for MDPI food & nutrition journals: Foods, Antioxidants, Toxins. Use to format or check a manuscript for an MDPI food journal — the MDPI template structure, abstract/keyword limits, numbered MDPI/ACS-style references, and figure specs. Triggers: submit to Foods, Antioxidants, Toxins guidelines, MDPI food formatting. Also fires when the user wants to publish on/in this journal, format a manuscript for it, or match its reference/citation style."
metadata:
  publisher: MDPI
  verified: "2026-11"
  source: "https://www.mdpi.com/journal/foods/instructions"
---

# MDPI Food Journals — Shared Author Guideline Skill

> **Verification status:** **Verified for Foods** (instructions page, 2026-11-27). Antioxidants, Toxins, Nutrients, Dietetics, Obesities and the agriculture titles were **not read individually**.

**Publisher:** MDPI · Sources: [Foods instructions](https://www.mdpi.com/journal/foods/instructions), [Antioxidants](https://www.mdpi.com/journal/antioxidants/instructions), [Toxins](https://www.mdpi.com/journal/toxins/instructions). All Gold open access; use the MDPI Word/LaTeX template.

## Applies to
| Journal | Abbrev | Scope |
|---|---|---|
| Foods | FOODS | Broad food science & technology |
| Antioxidants | ANTIOXIDANTS-BASEL | Antioxidants, oxidative stress (food/health) |
| Toxins | TOXINS | Toxins incl. mycotoxins/food-safety toxicology |

## Article types
Article, Review, Communication, plus Perspective/Opinion, Case Report, Protocol. Special Issues are central to MDPI; note the target Special Issue if any.

## Manuscript structure (MDPI template)
Introduction → Materials and Methods → Results → Discussion (may be combined with Results) → Conclusions (**optional**). Followed by: Supplementary Materials, Author Contributions, Funding, Institutional Review Board Statement, Informed Consent Statement, Data Availability Statement, Acknowledgments, Conflicts of Interest, References.

- **Abstract:** single paragraph, about **200 words maximum**, structured logic (background, methods, results, conclusion) **without headings**.
- **Keywords:** 3–10 (aim for ~5).
- **Author Contributions:** CRediT taxonomy, required.
- All the statement sections above are **mandatory** in the MDPI template (state "not applicable" where relevant).

## Reference style
**Numbered, MDPI/ACS style.** In-text bracketed numbers `[1]`, `[2,3]` in order of appearance; numbered list.

Example:
> 1. Author, A.B.; Author, C.D. Title of the article. *Foods* **2023**, *12*, 1234. https://doi.org/10.3390/foods12xxxxxx

(Author names as Last, F.M.; journal name italic; year bold; volume italic.)

## Figures & tables
Figures preferably **≥600 dpi**, PNG/JPEG/TIFF; insert near first citation; Word tables; number all items in order. Graphical abstract optional, ≥560 × 1100 px (h × w).

**Submission:** free-format references are accepted at first submission; MDPI style is required at revision. Cover letter required. Declare GenAI use in Methods/Acknowledgments.

## Submission checklist
- [ ] MDPI template, numbered sections · [ ] Abstract ≤200 words · [ ] 3–10 keywords
- [ ] All mandatory statement sections completed (IRB, consent, data availability, conflicts, funding, contributions)
- [ ] Numbered MDPI-style references with DOIs · [ ] Figures ≥600 dpi preferred
- [ ] Cover letter · [ ] Suggested reviewers (MDPI requests several)

## Also covers — MDPI nutrition journals
Same MDPI template (numbered MDPI style, mandatory statement sections).

| Journal | Abbrev | Scope |
|---|---|---|
| Nutrients | NUTRIENTS | Human nutrition, diet, health |
| Dietetics | DIETETICS-BASEL | Dietetics (OA) |
| Obesities | OBESITIES-BASEL | Obesity (OA) |

## Formatting constraints
```yaml
publisher: MDPI
scope: food & nutrition
reference_style: numbered-mdpi
abstract_words: 200
keywords: {min: 3, max: 10}
mandatory_statements: [author_contributions, funding, irb, informed_consent, data_availability, conflicts_of_interest]
open_access: gold
figure_dpi: 600
```
