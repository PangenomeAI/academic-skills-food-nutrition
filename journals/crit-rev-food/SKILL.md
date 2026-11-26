---
name: crit-rev-food
description: "Shared author-guideline skill for Taylor & Francis food journals: Critical Reviews in Food Science and Nutrition, Food Reviews International, International Journal of Food Properties. Use to format or check a manuscript for a T&F food journal — structure, abstract/keyword limits, Taylor & Francis reference styles, and figure specs. Triggers: submit to Critical Reviews in Food Science and Nutrition, Food Reviews International, IJFP guidelines, Taylor & Francis food formatting. Also fires when the user wants to publish on/in this journal, format a manuscript for it, or match its reference/citation style."
metadata:
  publisher: "Taylor & Francis"
  verified: "2026-11"
  source: "https://www.tandfonline.com/action/authorSubmission?journalCode=bfsn20"
---

# Taylor & Francis Food Journals — Shared Author Guideline Skill

> **Verification status:** **Verified** on the Taylor & Francis instructions pages (2026-11-27) for Critical Reviews in Food Science and Nutrition, Food Reviews International and International Journal of Food Properties. Other titles are **not verified**.
> Anything not confirmed must be checked at the journal's guide before submission. Tell the
> author so, and ask them to paste or upload the current guide if it cannot be read.

## Publisher-wide guidance (compared across journals, 2026-11-27)
Shared by the three verified journals: IMRaD order with a Declaration of interest
statement, 3–6 keywords (IJFP any number), figures 1200/600/300 dpi. **Reference style and
abstract length differ per journal.**

**Publisher:** Taylor & Francis · Confirm each journal's "Instructions for authors" on tandfonline.com. Structure below reflects the common T&F template.

## Applies to
| Journal | Abbrev | Abstract | Keywords | Reference style |
|---|---|---|---|---|
| Critical Reviews in Food Science and Nutrition | CRIT REV FOOD SCI | unstructured, 200 words | 3–6 | **CSE 9th, author–date** ([guide](https://files.taylorandfrancis.com/tf_CSE.pdf)) |
| Food Reviews International | FOOD REV INT | **≤100 words** | 3–6 | **ACS, numbered** ([guide](https://files.taylorandfrancis.com/tf_usacs.pdf)) |
| International Journal of Food Properties | INT J FOOD PROP | unstructured, 200 words | any number | **ACS, numbered** (same guide) |

**These three do not share a style — and none is APA.** In ACS (T&F variant) cite with superscript numbers in square brackets, after terminal punctuation.

## Structure
Title page → Abstract → Keywords → Introduction → Materials and Methods → Results → Discussion → Acknowledgments → **Declaration of interest statement** → References → Appendices → Tables (with captions) → Figures → Figure captions.

- CRFSN and IJFP offer **format-free submission**: any consistent reference style; journal style is applied after acceptance.
- IJFP **reviews are invited only**.
- Food Reviews International: American spelling, double-spaced, ≥1 inch margins, running head ≤50 characters.
- No overall word limit was stated on these pages for the three journals.
- Disclosure and data availability statements.

## Figures & tables
Line art 1200 dpi, grayscale 600 dpi, colour 300 dpi at final size; PS, JPEG, TIFF or Word; editable tables.

**Journal of the International Society of Sports Nutrition** uses numbered references (Citation Style Language repository).

## Submission checklist
- [ ] Reference style for the specific journal · [ ] Abstract length (100 or 200) · [ ] Keywords
- [ ] Declaration of interest + data availability · [ ] Figure resolution by type

## Also covers — Taylor & Francis / Routledge nutrition journals
Same T&F template (style differs by title); clinical titles add trial registration and
reporting guidelines.

| Journal | Abbrev | Notes |
|---|---|---|
| Journal of the International Society of Sports Nutrition | J INT SOC SPORT NUTR | OA; sports nutrition |
| International Journal of Food Sciences and Nutrition | INT J FOOD SCI NUTR | Research |
| Journal of the American Nutrition Association | J AM NUTR ASSOC | Clinical/dietetics (Routledge) |
| Nutritional Neuroscience | NUTR NEUROSCI | Research |
| Journal of Dietary Supplements | J DIET SUPPL | Research |

## Formatting constraints
```yaml
publisher: Taylor & Francis
reference_style: per-journal   # CRFSN cse-author-date; FRI and IJFP acs-numbered
abstract_words: {crit_rev_food_sci_nutr: 200, food_reviews_international: 100, int_j_food_properties: 200}
keywords: {min: 3, max: 6}   # IJFP: any number
disclosure_statement: required
figure_dpi: {color: 300, grayscale: 600, line_art: 1200}
```
