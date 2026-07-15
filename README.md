<p align="center">
  <img src="assets/banner.svg" alt="Academic Skills for Food & Nutrition Science — open AI research skills for Claude Code and Codex" width="100%">
</p>

# Academic Skills for Food & Nutrition Science

> **AI research assistant for food science and nutrition** — Claude Code, Codex,
> MiniMax Agent, and OpenClaw skills for **literature
> review, systematic review (PRISMA & meta-analysis), data analysis and
> statistics, scientific figures, journal formatting, and peer review**.
> Food-science research automation, end to end.

Original, **MIT-licensed** skills for the food & nutrition research lifecycle —
**research → write → review → revise → finalize** — where each core skill is a
**multi-subagent system** and a master pipeline orchestrates them, with built-in
knowledge of food & nutrition journal author guidelines and a food-science figure
workflow. Supports Claude Code, Codex, MiniMax Agent, and OpenClaw.

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

**Claude Code, Codex, and MiniMax Agent** (one command via the installer):

```bash
curl -fsSL https://raw.githubusercontent.com/PangenomeAI/academic-skills-food-nutrition/main/install.sh | bash
```

Or, from a local clone: `./install.sh` (all) · `./install.sh claude` · `./install.sh codex` · `./install.sh minimax` · `./install.sh openclaw`.
The installer registers the Claude Code plugin, and for **Codex**
(`${CODEX_HOME:-~/.codex}/skills/`), **[MiniMax Agent](https://agent.minimax.io/)**
(Mavis; `${MAVIS_SKILLS_DIR:-~/.mavis/skills}/`),
**[OpenClaw](https://openclaw.ai)** (`${OPENCLAW_HOME:-~/.openclaw}/skills/`) it installs **each skill flat**
(`…/skills/<name>/SKILL.md`, so the agent discovers it) **plus** the shared
`journals/` and `scripts/` directories so cross-skill references resolve. Restart
the app so it rescans skills. (Override the location with `CODEX_HOME` /
`MAVIS_SKILLS_DIR` / `OPENCLAW_HOME`, or add via MiniMax's
in-app Skill Creator/import.)

## Updating

**Updates are not automatic** — once installed you stay on that version until you
choose to update. To get the latest release:

**Claude Code** (built-in update):
```bash
claude plugin update academic-skills-food-nutrition
```
Restart Claude Code (or run `/plugin`) to apply. If it doesn't yet show the newest
version, refresh the marketplace first:
```bash
claude plugin marketplace update academic-skills-food-nutrition
```

**Codex / MiniMax Agent (Mavis) / OpenClaw** — re-run the installer
(it cleanly replaces the skills), then restart the app:
```bash
curl -fsSL https://raw.githubusercontent.com/PangenomeAI/academic-skills-food-nutrition/main/install.sh | bash
# or, from a local clone:  ./install.sh codex  |  ./install.sh minimax  |  ./install.sh openclaw
```

Check your installed version with `claude plugin list`; see all versions on the
[Releases](https://github.com/PangenomeAI/academic-skills-food-nutrition/releases)
page (a GitHub Release is published automatically on each feature update).

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
- **`food-deep-research`** — source-validated literature-review engine (scope → design
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
  journal selection → research (`food-research`/`food-deep-research`) → write & analyze
  (`food-paper` → `food-figure`) → peer review (`food-review`) → revise →
  finalize, with mandatory author decision points. **Default: one** review→revise
  round; a second round and in-place Tracked Changes on the original Word file
  require **explicit author authorization** (avoids over-automation).

### Journal knowledge
- **`journal-selector`** — asks which journal you're targeting (or reads it from
  your request) and loads that journal's constraints. Covers the **Food Science &
  Technology** (60) and **Nutrition & Dietetics** (59) journal lists, plus **35
  multidisciplinary / cross-discipline** journals food & nutrition researchers
  publish in (Nature, Science, Cell, and PNAS families, eLife, PLOS, ES&T, Gut,
  etc.). See [`journals/_coverage.md`](journals/_coverage.md),
  [`journals/_coverage_nutrition.md`](journals/_coverage_nutrition.md), and
  [`journals/_coverage_multidisciplinary.md`](journals/_coverage_multidisciplinary.md).
- **`journals/*`** — 24 publisher-tiered author-guideline skills covering the
  **Food Science & Technology**, **Nutrition & Dietetics**, and multidisciplinary
  journal lists
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
  microscopy plates, multi-panel), with Python (matplotlib/seaborn/subplot_mosaic/
  statsmodels) and R (ggplot2/patchwork/ComplexHeatmap/ggrepel + svglite/cairo_pdf/
  ragg) template libraries, curated colourblind-safe palettes, per-figure
  provenance + captions, and a QA gate. Exports journal-ready SVG/PDF/TIFF. For
  **schematics/graphical abstracts**, an opt-in AI-image route (Gemini/ChatGPT/
  Claude) with a structured prompt method — never for data figures. A runnable
  **synthetic/illustrative Figure-story gallery** provides four final 11- or
  12-panel food-science figures spanning active packaging, probiotic storage,
  trained sensory analysis, and analytical-method validation. Each narrative
  progresses from a code-drawn experimental schematic through topic-specific raw
  and derived evidence to an explicitly illustrative synthesis panel, with
  deterministic source-data generation, PDF + PNG exports, captions, and trace
  cards. The gallery also documents an AI schematic-route test and its
  QA/reproducibility safeguards.

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

## Using AI responsibly for academic work

> **AI can make mistakes.** Large language models can produce fluent but incorrect
> statements, invented references, and unsupported conclusions. **You — the
> researcher — are responsible for the integrity of your work.**

These skills are research **assistants, not authors**. Treat every AI-generated
statement as a *draft to be verified*, never as established fact.

### Your responsibilities
- **Validate everything.** Check every claim, number, and citation against the
  primary source before you use or submit it. This project enforces an
  anti-fabrication grounding rule and ships a runnable check
  ([`scripts/verify_citations.py`](scripts/verify_citations.py); see
  [`faithfulness-and-citation.md`](food-paper/references/faithfulness-and-citation.md)) —
  use them, but they do **not** replace your own judgement.
- **Never present unverified AI output** as your own knowledge or as fact; do not
  submit AI-written text you have not checked and understood.
- **Disclose your use of AI** honestly, following your venue's and institution's
  policy — most journals and universities now require an AI-use statement
  (see [`declarations-guide.md`](food-paper/references/declarations-guide.md)).
- **Follow your institution's academic-integrity rules.**

### University of Melbourne policy (for UoM staff and students)
This project is initiated by the Food Science Research Team at the University of Melbourne; UoM users must comply with University policy on acknowledging and using generative AI. Always check the
current policy and your course/coordinator's specific requirements:
- [Acknowledging use of AI tools and technologies](https://students.unimelb.edu.au/academic-skills/academic-integrity/acknowledging-use-of-ai-tools-and-technologies)
- [Academic integrity](https://students.unimelb.edu.au/academic-skills/academic-integrity)
- [Using AI as a graduate researcher (graduate researchers and digital assistance tools)](https://gradresearch.unimelb.edu.au/preparing-my-thesis/graduate-researchers-and-digital-assistance-tools)
- [Guidelines for allowing student GenAI use in assessment](https://www.unimelb.edu.au/tli/lda/genai-hub/resources-links/guidelines-for-allowing-student-genai-use-in-assessment)
- [Writing with GenAI](https://students.unimelb.edu.au/academic-skills/study-skills/learning-with-genai/writing-with-genai)
- [Studying with GenAI](https://students.unimelb.edu.au/academic-skills/study-skills/learning-with-genai/studying-with-genai)
- [Organising with GenAI](https://students.unimelb.edu.au/academic-skills/study-skills/learning-with-genai/organising-with-genai)
- [Using GenAI effectively](https://students.unimelb.edu.au/academic-skills/study-skills/learning-with-genai/using-genai-effectively)

### Further reading
- Sarkar, R. (2026). Why AI can't be trusted to write scientific reviews. *Nature*. https://doi.org/10.1038/d41586-026-01616-3
- Using AI responsibly in scientific publishing. (2026). *Nature Methods* (editorial). https://doi.org/10.1038/s41592-026-03020-1

## Contributing

We welcome contributions from food & nutrition research groups worldwide. If your
team would like to contribute or collaborate, please contact the development team
at **[food_agents@lists.unimelb.edu.au](mailto:food_agents@lists.unimelb.edu.au)**.

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

### Contributors and institutions

- **PangeZAU** — Principal Investigator, Food Science Research Team, University of Melbourne.
- **Zijian Liang** — Research Coordinator, Food Science Research Team, University of Melbourne.
- **Calebsch** — Developer, Food Science Research Team, University of Melbourne.
- **Pimiao Huang** — Contributor, Food Science Research Team, University of Melbourne.

## Acknowledgements

This is original, independently written work released under MIT. It was informed
by — but contains no code or text from — earlier community projects exploring
academic-research and scientific-figure skills for Claude Code, including the
`nature-skills` collection (Apache-2.0), `deer-flow` (MIT), `Light-skills` (MIT),
`academic-figure-skills` and `academic-figure-generator` (MIT),
`Awesome-Journal-Skills` (MIT), and `academic-research-skills` (CC-BY-NC-4.0). Only non-copyrightable workflow
*concepts* (e.g. multi-source search, layered retrieval, staged screening,
parallel extraction, PRISMA structure, subagent teams, evidence/citation
verification gates, and publication figure styles) were drawn on; all wording
here is our own, so this project is free of their license obligations and is
offered under MIT.
