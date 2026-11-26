---
name: science-aaas
description: "Author-guideline skill for the AAAS Science family that food & nutrition researchers publish in: Science, Science Advances, Science Translational Medicine, Science Immunology, Science Signaling, Science Robotics. Use to format or check a manuscript for a Science-family journal — very tight length limits, short abstract, Science numbered reference style, and figure specs. Triggers: submit to Science, Science Advances guidelines, AAAS Science formatting. Also fires when the user wants to publish on/in this journal, format a manuscript for it, or match its reference/citation style."
metadata:
  publisher: "AAAS (American Association for the Advancement of Science)"
  verified: "2026-11 partial"
  source: "https://www.science.org/content/page/science-information-authors"
---

# AAAS Science Family — Author Guideline Skill

> **Verification status:** **Verified for Science Advances**, and for Science's initial-manuscript instructions and long-format limit (2026-11-27). Science's standard length and abstract limits and the other family journals are **not verified**.
> Anything not confirmed must be checked at the journal's guide before submission. Tell the
> author so, and ask them to paste or upload the current guide if it cannot be read.

**Publisher:** AAAS · Confirm exact limits at the journal's Information for Authors (very strict; differ by title/article type).

## Applies to
Science; Science Advances (open access); Science Translational Medicine; Science
Immunology; Science Signaling; Science Robotics.

## Science (partly verified)
- Order: Title → Authors → Affiliations → Abstract → Main Text → References and Notes → Acknowledgments → List of Supplementary Materials → figure captions → tables. Materials and Methods sit in the Supplementary Materials.
- Title ≤96 characters; figure captions ≤200 words; include titles of cited articles.
- Extended online Research Articles: ≤6,000 words, ≤6 display items, ≤100 main-text references.

## Publisher-wide guidance
Science and Science Advances **differ** in title length, section order and Methods placement; do not transfer limits.

## Science Advances (verified)
[Information for authors](https://www.science.org/content/page/science-advances-information-authors)
- Research article ≤15,000 words, ≤10 figures + tables, ≤80 references. Review ≤10,000 words, ≤10 display items, ≤150 references.
- Title ≤135 characters; short title ≤50. Abstract **≤150 words**, one paragraph, no citations.
- Order: Abstract → Introduction → Results → Discussion (with limitations) → **Materials and Methods** → References → Acknowledgments (funding, contributions, competing interests, data availability).
- References numbered in order, cited in parentheses `(1, 2)`; all authors (no *et al.*), full article titles.
- No required format at initial submission; submit cover letter and five suggested reviewers; table legends ≤250 words.

## Format (Science style)
- **References: numbered** in citation order, Science style (numbered list `1., 2., …`; in-text `(1)`, `(2, 3)`). Full author lists; include DOIs.
  > 1. A. B. Author, C. D. Author, Title of the article. *Science* **380**, 1234 (2026).
- **Abstract:** single paragraph, very short (Science: *confirm*; Science Advances ≤150).
- **Structure:** Science Research Articles are tightly length-limited (*confirm current limit*); Materials and Methods often in supplementary. Science Advances: see above.
- **Display items:** limited; cite `Fig. 1` in order.
- **Mandatory:** data/materials availability; competing interests; author contributions; supplementary materials for full methods.
- **Figures:** ≥300 dpi; RGB; sized to one/two columns; accessible palette.

## Formatting constraints
```yaml
publisher: AAAS Science
reference_style: science-numbered
abstract_words: {science: confirm-at-source, science_advances: 150}
methods: {science: confirm-at-source, science_advances: after-discussion}
data_availability: required
figure_dpi: 300
```
