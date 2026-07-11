# Changelog

## 1.0.0 — 2026-07

First open-source release. Original, MIT-licensed work.

### Skills
- Core workflow: `food-research`, `food-paper` (journal-aware), `food-review`,
  `food-pipeline`.
- `journal-selector` + 16 publisher-tiered journal author-guideline skills under
  `journals/` covering 60 food & nutrition journals
  (see `journals/_coverage.md`).
- `food-figure`: food-science figure workflow (Python or R; journal-ready
  SVG/PDF/TIFF).

### Notes
- Every skill's body and description is in English.
- Journal skills capture each journal's reference/citation style; `food-paper`
  re-flows references to the target journal's style.
- Coverage of all 60 journals verified by `scripts/check_journal_coverage.py`.
