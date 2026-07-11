# Academic Skills for Food & Nutrition Science

Original, **MIT-licensed** Claude Code skills for the food & nutrition research
lifecycle — **research → write → review → revise** — with built-in knowledge of
food-science journal author guidelines and a food-science figure workflow.

Open source. Free to use, modify, and build on.

## Skills

### Core workflow
- **`food-research`** — literature discovery and evidence synthesis for food &
  nutrition (FSTA, PubMed, Web of Science, Scopus, AGRICOLA; EFSA/FDA/USDA/Codex
  for safety and regulatory evidence); grades evidence and maps gaps.
- **`food-paper`** — journal-aware manuscript writing. Resolves the target
  journal first, drafts to its structure and limits, applies its reference
  style, and routes figures through `food-figure`.
- **`food-review`** — referee-perspective peer review (methodology,
  statistics, novelty/scope, plus food-safety/ethics) with an editor decision.
- **`food-pipeline`** — orchestrates the whole path from topic/data to a
  submission-ready manuscript, with journal selection up front.

### Journal knowledge
- **`journal-selector`** — asks which journal you're targeting (or reads it from
  your request) and loads that journal's constraints. Covers **60 journals**
  (see [`journals/_coverage.md`](journals/_coverage.md)).
- **`journals/*`** — 16 publisher-tiered author-guideline skills (Elsevier,
  Wiley, Nature Portfolio, Springer, Taylor & Francis, MDPI, RSC, ACS, Annual
  Reviews, Oxford, Emerald, KeAi/Tsinghua, Codon, BioMed Central). Each lists the
  journals it covers, their limits, structure, **reference/citation style**, and
  a submission checklist.

### Figures
- **`food-figure`** — submission-grade food-science figures in Python or R
  (grouped bars with error bars and significance letters, sensory radar,
  microbial growth/survival curves, chromatograms, texture profile analysis,
  rheology, PCA/heatmaps, microscopy), exporting journal-ready SVG/PDF/TIFF at
  the target journal's spec.

## How it fits together

Name a journal ("I want to publish on Food Chemistry" / "format for LWT") and
`journal-selector` loads that journal's rules; `food-paper` writes to them and
re-flows the reference list into the journal's citation style; any figure
request goes to `food-figure` at the journal's DPI and column width. Ask for the
whole thing and `food-pipeline` runs research → write → review → revise with
checkpoints.

## Coverage

All 60 target journals map to a publisher-tiered skill, verified by
[`scripts/check_journal_coverage.py`](scripts/check_journal_coverage.py). Full
map: [`journals/_coverage.md`](journals/_coverage.md).

Author-guideline details record a `Source:` URL and a `Verified:` date. Publisher
pages change and several block automated access — confirm exact numeric limits at
the source before submitting; structure and reference styles are the stable part.

## License

MIT — see [LICENSE](LICENSE). Free for any use, including commercial.

## Acknowledgements

This is original, independently written work. It was informed by, but contains no
code or text from, earlier community projects exploring academic-research and
scientific-figure skills for Claude Code. Workflow concepts are not
copyrightable; the wording here is our own.
