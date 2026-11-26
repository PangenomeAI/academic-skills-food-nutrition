---
name: british-food-journal
description: "Author-guideline skill for British Food Journal (Emerald, ISSN 0007-070X). Use to format or check a manuscript for BFJ — Emerald's required structured abstract, article classification, Harvard references, and figure specs. Triggers: submit to British Food Journal, Emerald food journal guidelines, structured abstract for BFJ. Also fires when the user wants to publish on/in this journal, format a manuscript for it, or match its reference/citation style."
metadata:
  publisher: "Emerald Publishing"
  issn: "0007-070X"
  verified: "2026-11"
  source: "https://www.emeraldgrouppublishing.com/journal/bfj#author-guidelines"
---

# British Food Journal (Emerald) — Author Guideline Skill

> **Verification status:** **Verified** for British Food Journal and China Agricultural Economic Review (journal pages and Emerald author guidelines, 2026-11-27).
> Anything not listed here is unconfirmed: check the journal's guide, or ask the author to
> paste or upload it, before applying a limit.

**Publisher:** Emerald · [BFJ](https://www.emerald.com/bfj/#author-guidelines) · [Emerald author guidelines](https://www.emerald.com/journals/author-guidance/1627/emerald-publishing-author-guidelines)

## Publisher-wide guidance (shared by both journals and the Emerald guide)
- **Structured abstract**, required for all articles, ≤250 words **including keywords and article classification**; research limitations, practical and social implications headings are optional.
- **Harvard** references.
- Up to **6 keywords**; select the article classification.
- Research paper, case study and general review ≤**8,000 words**, including all text, figures and tables (allow 280 words per figure or table). Editorial ≤3,000.
- Check each journal's page for its article types (CAER: practitioner paper ≤2,000, policy/academic debate ≤8,000).

## Formatting constraints
```yaml
publisher: Emerald
reference_style: harvard-emerald
structured_abstract: {required: true, words_max: 250}
keywords_max: 6
word_limit: 8000   # includes figures/tables at 280 words each
article_classification: required
```
