---
name: jafc
description: "Author-guideline skill for Journal of Agricultural and Food Chemistry (ACS, ISSN 0021-8561). Use to format or check a manuscript for JAFC — ACS structure, TOC/abstract graphic, ACS reference style, and figure specs. Triggers: submit to Journal of Agricultural and Food Chemistry, JAFC guidelines, ACS food chemistry formatting. Also fires when the user wants to publish on/in this journal, format a manuscript for it, or match its reference/citation style."
metadata:
  publisher: "American Chemical Society"
  issn: "0021-8561"
  verified: "2026-11"
  source: "https://publish.acs.org/publish/author_guidelines?coden=jafcau"
---

# Journal of Agricultural and Food Chemistry (JAFC) — Author Guideline Skill

> **Verification status:** **Verified** — ACS Researcher Resources JAFC author guidelines, 2026-11-27. TOC graphic size **not verified**.

**Publisher:** American Chemical Society · **ISSN:** 0021-8561 · **Source:** [ACS author guidelines (JAFC)](https://publish.acs.org/publish/author_guidelines?coden=jafcau).

## Aims & scope
Original research on the chemistry and biochemistry of agriculture and food: chemistry/biochemistry of foods and beverages, bioactive constituents, food safety/toxicology, analytical methods, agricultural chemistry, and nutrition chemistry. Emphasis on chemical rigor and food/agriculture relevance.

## Article types
Article; Review; Perspective; New Analytical Methods (must show clear advance/validation); Letters to the Editor.

## Manuscript structure (ACS)
Title, authors → Abstract and keywords (single page) → Introduction → Materials and Methods (incl. safety) → Results and Discussion → Abbreviations Used → Acknowledgment → Supporting Information description → References → TOC graphic.

- **No separate Conclusions section** — put conclusions inside Results and Discussion.
- **Abstract:** **100–150 words**, one paragraph. Perspectives: ≤100 words.
- **Significance statement** (separate 3-point letter: problem/originality; new knowledge; relevance and molecular role) — required.
- **Format:** double-spaced single column, continuous line numbers; 20 typed pages excluding references, tables and figures (more needs editor approval).
- **TOC graphic:** required.

## Reference style
References may be submitted **in any style** if complete and **including titles**; number them in order of appearance. ACS style is shown below.

Example (ACS):
> (1) Author, A. B.; Author, C. D. Title of the Article. *J. Agric. Food Chem.* **2023**, *71* (10), 1234–1245. https://doi.org/10.1021/acs.jafc.3cxxxxx

## Figures & tables
Resolution: line art **1200 dpi**, grayscale **600 dpi**, colour **300 dpi**. Single column ≤3.33 in (8.47 cm); double column 4.167–7 in (10.6–17.8 cm); depth ≤9.167 in including caption; lettering ≥4.5 pt, lines ≥0.5 pt.

## Submission checklist
- [ ] TOC/abstract graphic · [ ] Abstract 100–150 words · [ ] Keywords · [ ] Significance statement · [ ] No Conclusions heading
- [ ] ACS numbered references with article titles + DOIs
- [ ] Method validation reported (analytical papers) · [ ] Safety/ethics statements as applicable
- [ ] Figure resolution by type, ACS widths · [ ] Cover letter (novelty + food/ag relevance)

## Formatting constraints
```yaml
journal: Journal of Agricultural and Food Chemistry
publisher: ACS
reference_style: acs-numbered
abstract_words: {min: 100, max: 150}
conclusions_section: none
significance_statement: required
toc_graphic: required
figure_dpi: {color: 300, grayscale: 600, line_art: 1200}
column_widths_cm: [8.47, 17.8]
```
