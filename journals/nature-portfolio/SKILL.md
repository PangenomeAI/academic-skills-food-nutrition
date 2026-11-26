---
name: nature-portfolio
description: "Shared author-guideline skill for Nature Portfolio research journals that food & nutrition researchers publish in: Nature, Nature Communications, Nature Microbiology, Nature Metabolism, Nature Sustainability, Nature Biotechnology, Nature Medicine, and Nature Reviews titles. Use to format or check a manuscript for a Nature-family journal — strict article-type word limits, unreferenced short abstracts, Nature superscript-numbered references (article titles required), display-item limits, Methods placement, reporting summary. (Nature Food and npj Science of Food are in the nature-food skill.) Triggers: submit to Nature, Nature Communications, Nature Microbiology, Nature Metabolism guidelines, Nature Portfolio formatting. Also fires when the user wants to publish on/in this journal, format a manuscript for it, or match its reference/citation style."
metadata:
  publisher: "Nature Portfolio (Springer Nature)"
  verified: "2026-11 partial"
  source: "https://www.nature.com/nature/for-authors/formatting-guide"
---

# Nature Portfolio Research Journals — Author Guideline Skill

> **Verification status:** **Partly verified** — Nature formatting guide and Nature Communications Article page read 2026-11-27. Other titles **not verified**.
> Anything not confirmed must be checked at the journal's guide before submission. Tell the
> author so, and ask them to paste or upload the current guide if it cannot be read.

**Publisher:** Nature Portfolio · Confirm each journal's own submission guidelines (limits differ by title/article type). Nature Food and npj Science of Food have their own skill (`nature-food`).

## Applies to (food/nutrition-relevant Nature journals)
| Journal | Abbrev | Relevance |
|---|---|---|
| Nature | NATURE | Multidisciplinary flagship |
| Nature Communications | NAT COMMUN | Multidisciplinary, open access |
| Nature Microbiology | NAT MICROBIOL | Food/gut microbiology |
| Nature Metabolism | NAT METAB | Nutrition & metabolism |
| Nature Sustainability | NAT SUSTAIN | Food systems, sustainability |
| Nature Biotechnology | NAT BIOTECHNOL | Food/agri biotech |
| Nature Medicine | NAT MED | Clinical nutrition |
| Nature Reviews (various) | NAT REV * | Reviews (commissioned) |

## Format (Nature style)
- **References: superscript numbers** in order of citation; numbered list; **article titles required**. Include DOIs.
  > 12. Author, A. B. & Author, C. D. Title of the article. *Nat. Commun.* **15**, 1234 (2026).
- **Nature Article:** a **fully referenced** summary paragraph, ideally ≤200 words; title ≤75 characters; about 2,500 words (6 pages) to 4,300 words (8 pages); about 50 references; Methods follow the figure legends (typically ≤3,000 words).
- **Nature Communications Article:** title ≤15 words; **unreferenced** abstract ≤200 words; main text ideally ≤5,000 words (Introduction → Results → Discussion → Methods); ≤10 display items; about 70 references.
- **Other titles:** confirm.
- **Structure:** Title → Abstract → main text → **Methods after the main text** (not counted in the word limit) → References → Figure legends → Tables.
- **Display items:** capped by article type (often ≤6–8); cite as `Fig. 1` in sequence.
- **Mandatory:** data availability + code availability statements; **Reporting Summary**; competing interests; author contributions.
- **Figures:** ≥300 dpi at final size; RGB; ~180 mm double column; accessible palette (avoid red/green as sole encoding).

## Formatting constraints
```yaml
publisher: Nature Portfolio
reference_style: nature-superscript-numbered
require_article_titles: true
abstract: {nature: referenced-summary-200, nature_communications: unreferenced-200}
methods: after-main-text
data_and_code_availability: required
reporting_summary: required
figure_dpi: 300
notes: "Nature Food + npj Science of Food -> nature-food skill"
```
