---
name: nature-food
description: "Author-guideline skill for Nature Portfolio food journals: Nature Food and npj Science of Food. Use to format or check a manuscript for these journals — strict article-type word limits, unreferenced short abstracts, Nature superscript-numbered references, display-item limits, and Methods placement. Triggers: submit to Nature Food, npj Science of Food guidelines, Nature Portfolio food formatting. Also fires when the user wants to publish on/in this journal, format a manuscript for it, or match its reference/citation style."
metadata:
  publisher: Nature Portfolio
  verified: "2026-11"
  source: "https://www.nature.com/natfood/submission-guidelines/aip-and-formatting"
---

# Nature Portfolio Food Journals — Author Guideline Skill

> **Verification status:** **Verified** — Nature Food content types and AIP formatting pages, and npj Science of Food content types, read 2026-11-27.

**Publisher:** Nature Portfolio · Sources: [Nature Food content types](https://www.nature.com/natfood/content) · [Nature Food formatting](https://www.nature.com/natfood/submission-guidelines/aip-and-formatting) · [npj Science of Food content types](https://www.nature.com/npjscifood/content-types). Confirm at source.

## Applies to
- **Nature Food** — selective; strict word/display limits (below).
- **npj Science of Food** — open access; more flexible length but same Nature referencing and rigor.

## Nature Food article types
| Type | Main text | Abstract (unreferenced) | Display items | References |
|---|---|---|---|---|
| Article | ≤3,000 words (excl. abstract, Methods, refs, legends) | ≤150 | ≤6 | ~50 |
| Analysis | ≤3,000 | 100–150 | ≤6 | ~50 |
| Resource | ≤3,000 | 100–150 | ≤8 | ~50 |
| Brief Communication | ≤1,500 incl. abstract, refs, legends; no headings | ≤70 | ≤2 | ~20 |
| Review | ≤6,000 | 100–150 | ≤6 | ≤100 |
| Perspective | ≤3,000; no Methods | ≤100 | ≤5 | ≤50 |
| Comment | ~2,000 | standfirst ≤70 | ~2 | ≤15 |

Brief Communication titles: ≤10 words / 90 characters. Article order: Introduction (**no heading**) → Results → Discussion (no subheadings) → Methods.

## npj Science of Food (Article)
No strict length limit. Title ≤15 words; abstract **≤150 words**, no subheadings; Introduction → Results → Discussion (no subheadings, limitations or conclusions sections) → Methods → Data availability → Code availability → Acknowledgments (funding goes here) → Author contributions → Competing interests → References (about 60 max) → Figure legends (≤350 words each).

## Reference style
**Nature style: superscript numbers** in order of citation (`...as shown previously^12`). Reference list numbered. **Article titles are required** for Nature Food long-form manuscripts. Include DOIs.

Example:
> 12. Author, A. B. & Author, C. D. Title of the article. *Nat. Food* **4**, 123–130 (2023).

## Structure & sections
Articles: Title → Abstract (unreferenced) → main text with headings (Introduction implicit) → Results → Discussion → Methods → References → Figure legends → Tables. Reference list order and numbering for Nature Food: main text, Methods, data availability, tables, figure legends. Figures cited as `Fig. 1`, `Fig. 2` in sequence. A data availability and code availability statement is mandatory; reporting summary required.

## Figures & tables
High-resolution (≥300 dpi at final size); RGB for online; maximum width 180 mm; 5–7 pt sans-serif labels; avoid red/green combinations for accessibility. Editable tables.

## Submission checklist
- [ ] Correct article type + within word/display limits · [ ] Abstract unreferenced within limit
- [ ] Nature superscript-numbered refs with article titles + DOIs · [ ] Methods after main text
- [ ] Data & code availability statements · [ ] Reporting summary (Nature Food)
- [ ] Cover letter (significance, fit) · [ ] Figures ≥300 dpi, accessible palette

## Formatting constraints
```yaml
journal_group: Nature Portfolio (Nature Food, npj Science of Food)
reference_style: nature-superscript-numbered
require_article_titles: true
article_word_limit: 3000
abstract_words: {article: 150, npj_article: 150, brief_communication: 70, perspective: 100}
display_items_max: 6
methods: after-main-text
data_availability: required
figure_dpi: 300
```
