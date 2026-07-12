# Academic Skills for Food & Nutrition Science

> **AI research assistant for food science and nutrition** — Claude Code & Codex
> skills for **literature review, systematic review (PRISMA & meta-analysis), data
> analysis and statistics, scientific figures, journal formatting, and peer
> review**. Food-science research automation, end to end.

Original, **MIT-licensed** Claude Code skills for the food & nutrition research
lifecycle — **research → write → review → revise → finalize** — where each core
skill is a **multi-subagent system** and a master pipeline orchestrates them,
with built-in knowledge of food & nutrition journal author guidelines and a
food-science figure workflow.

This open project was **initiated by the Food Science Group at the University of
Melbourne**, and we warmly welcome food & nutrition research groups from around
the world to use, adapt, and contribute to it. MIT-licensed and open source.

## Install

**Claude Code** (one command):

```bash
claude plugin marketplace add PangenomeAI/academic-skills-food-nutrition && \
claude plugin install academic-skills-food-nutrition@academic-skills-food-nutrition
```

Then restart Claude Code (or run `/plugin`). Update later with
`claude plugin update academic-skills-food-nutrition`.

**Both Claude Code and Codex** (one command via the installer):

```bash
curl -fsSL https://raw.githubusercontent.com/PangenomeAI/academic-skills-food-nutrition/main/install.sh | bash
```

Or, from a local clone: `./install.sh` (both) · `./install.sh claude` · `./install.sh codex`.
The installer registers the Claude Code plugin and copies the skills bundle into
Codex's skills directory (`${CODEX_HOME:-~/.codex}/skills/`), preserving the repo
structure so cross-skill references resolve.

## Skills

### Core workflow
- **`food-research`** — comprehensive, multi-source literature discovery and
  evidence synthesis for food & nutrition (FSTA, PubMed, Web of Science, Scopus,
  AGRICOLA, preprints, semantic search; EFSA/FDA/USDA/Codex for safety and
  regulatory evidence). Four-layer search, two-phase screening, and synthesis via
  subagents; grades evidence and maps gaps. Four streams — **quick brief, full
  review, deep research, systematic**. The first three **prioritize sources by
  journal ranking** (`journal_ranker`: Q1/Q2 food-science & nutrition, plus
  Nature/Science/Cell families and Q1/Q2 in any other discipline = highest
  priority; Q3 second; Q4 avoided). The **full review** and **systematic** streams
  finish by writing a manuscript, running an editorial + integrity `reviewer`
  loop, and exporting a **Word (.docx)** (APA 7.0 default, or a target journal via
  `journal-selector`). The **PRISMA 2020 systematic review** stream adds a fixed
  protocol, ≥3 databases (Web of Science/Scopus/PubMed), **dual independent
  three-step screening** (title → abstract → full text) with a moderator, a PRISMA
  flow diagram, a results table, and **OHAT risk-of-bias** (in vitro / human /
  animal); it uses eligibility-based inclusion rather than journal ranking.
- **`deep-research`** — source-validated literature-review engine (scope → design
  → discover → **screen by journal ranking** → **validate every source** →
  extract & verify evidence → synthesize → stress-test → **write & format** →
  editorial + integrity review loop) with a 12-subagent team. Outputs a finished,
  formatted review (**APA 7.0** by default, or a target journal's style via
  `journal-selector`). Runs standalone or as `food-research`'s deep-dive engine.
- **`food-paper`** — whole-process manuscript system (12 subagents) covering the
  full research lifecycle: understand the field (calls `food-research`), frame
  research questions, **curate data**, run **statistics**, build **figures &
  tables** (calls `food-figure`), construct arguments and discussion, draft,
  **polish**, manage citations, and **self-review** (calls `food-review`) —
  journal-aware throughout (APA 7.0 default, or a target journal via
  `journal-selector`).
- **`food-review`** — multi-reviewer peer-review panel (coordinating editor +
  methodology, domain/novelty, and integrity/ethics reviewers + a devil's
  advocate) with a **formatting-compliance check** against the target journal
  (APA 7.0 default, or a specific journal via `journal-selector`), ending in an
  editorial decision + revision checklist + response-letter skeleton.
- **`food-pipeline`** — **master orchestrator** that routes a project to the
  specialist skills (each with its own subagent team) and enforces quality gates:
  journal selection → research (`food-research`/`deep-research`) → write & analyze
  (`food-paper` → `food-figure`) → peer review (`food-review`) → revise →
  re-review → finalize, with mandatory author decision points.

### Journal knowledge
- **`journal-selector`** — asks which journal you're targeting (or reads it from
  your request) and loads that journal's constraints. Covers the **Food Science &
  Technology** (60) and **Nutrition & Dietetics** (59) journal lists (see
  [`journals/_coverage.md`](journals/_coverage.md) and
  [`journals/_coverage_nutrition.md`](journals/_coverage_nutrition.md)).
- **`journals/*`** — 19 publisher-tiered author-guideline skills covering both
  the **Food Science & Technology** and **Nutrition & Dietetics** journal lists
  (Elsevier, Wiley, Nature Portfolio, Springer, Taylor & Francis, MDPI, RSC, ACS,
  Annual Reviews, Oxford, Emerald, KeAi/Tsinghua, Codon, BioMed Central,
  Cambridge, Frontiers, plus a niche-publisher skill). Each lists the journals it
  covers (see [`journals/_coverage.md`](journals/_coverage.md) and
  [`journals/_coverage_nutrition.md`](journals/_coverage_nutrition.md)), their
  limits, structure, **reference/citation style**, and a submission checklist.

### Figures
- **`food-figure`** — comprehensive figure system: **analyzes your data**
  (`scripts/analyze_data.py` profiles a CSV/TSV and **recommends the best figure
  type**), then renders submission-grade graphics in **Python or R** at the target
  journal's spec. Covers all common scientific figure types (bar/box/violin,
  line/kinetic, scatter/regression, Bland-Altman, sensory radar, chromatograms,
  TPA/rheology, dose-response, survival, PCA/PLS-DA, clustered heatmaps, forest,
  microscopy plates, multi-panel), with nine reference docs plus data-profiler and
  backend-preference scripts. Exports journal-ready SVG/PDF/TIFF.

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

## Contributing

We welcome contributions from food & nutrition research groups worldwide.

**Branching model — please read:** `main` is release-only; **never push to it
directly**. Do your work on the **`development`** branch and open a **pull request**
to merge `development` → `main`, so changes are tracked and reviewed. Always keep
[`README.md`](README.md) and [`CHANGELOG.md`](CHANGELOG.md) up to date in the same PR.

Full, machine-actionable instructions for collaborators and their AI coding agents
are in **[`AGENTS.md`](AGENTS.md)** (see also [`CONTRIBUTING.md`](CONTRIBUTING.md)).

Key documents: **[README](README.md)** · **[CHANGELOG](CHANGELOG.md)** · **[LICENSE](LICENSE)**.

## License & community

MIT — see [LICENSE](LICENSE). Free for any use, including commercial. This open
project was **initiated by the Food Science Group, University of Melbourne**
(PangeZAU / PangenomeAI). Contributions from food & nutrition research groups
worldwide are warmly welcomed — open an issue or pull request.

## Acknowledgements

This is original, independently written work released under MIT. It was informed
by — but contains no code or text from — earlier community projects exploring
academic-research and scientific-figure skills for Claude Code, including the
`nature-skills` collection (Apache-2.0), `deer-flow` (MIT), and
`academic-research-skills` (CC-BY-NC-4.0). Only non-copyrightable workflow
*concepts* (e.g. multi-source search, layered retrieval, staged screening,
parallel extraction, PRISMA structure, subagent teams) were drawn on; all wording
here is our own, so this project is free of their license obligations and is
offered under MIT.
