# Changelog

## 1.28.0 — 2026-07

- **Structured review report + revision-log format, and manuscript editor queries.**
  - New canonical `food-review/references/report-format.md`: the combined **review
    report + revision log** now uses **stable issue IDs** grouped by category
    (`A#/B#/C#/D#`, `SQ#`, `R2-*`, `FC#`), each concern paired with a
    `Response (<type>)` line — **Tracked edit · Editor query · Recommendation ·
    Residual** — with precise manuscript locations (`P##` / Table / Figure), an
    overall assessment, editorial decision, summary of changes, and a residual-items
    list (Parts A/B/C). Wired into `food-review` (report + `review_coordinator`),
    `food-pipeline` (the one combined report), and `food-paper` revise (revision log).
  - **Editor queries in the manuscript:** when the reviewer/reviser suggests a fix
    it **cannot make itself** (needs the author's data or decision), it now also
    inserts a **comment / tracked "EDITOR QUERY" note in the manuscript at that
    location**, tagged with the same report issue ID — so the author can jump from a
    report item straight to the spot, not just read it in the report. Updated
    `word-review-comments.md` and `revision-response.md`.

## 1.27.0 — 2026-07

- **Prompt for the target journal once, then persist.** `food-paper`,
  `food-review`, `food-deep-research`, and `food-pipeline` now resolve the target
  journal up front by calling `journal-selector`, which **asks the user which
  journal they are targeting** (answer 'generic' for APA 7.0 defaults) instead of
  silently defaulting. The choice is asked **exactly once** per project and reused
  by every downstream subagent/stage; it is re-resolved **only** when the user asks
  to switch journals. `journal-selector` gained an explicit "ask once, then
  persist" contract, and `food-pipeline` resolves the journal at ROUTE and passes
  it to every downstream skill so none of them re-asks.

## 1.26.1 — 2026-07

- **Journal skills no longer register as top-level plugin skills.** The 24
  publisher/journal author-guideline folders under `journals/` are *reference
  material* that `journal-selector` reads on demand (`journals/<folder>/SKILL.md`
  → its `## Formatting constraints`), not skills a user invokes directly. They
  were cluttering the plugin's skill list. Trimmed the `skills` array in
  `plugin.json` and `marketplace.json` to the **7** real skills (the six
  `food-*` skills + `journal-selector`). The journal files still ship with the
  plugin, so `journal-selector` resolves them exactly as before.

## 1.26.0 — 2026-07

- Added **Pimiao Huang** and **Chenghao Shen** (The University of Melbourne) as
  co-authors in `CITATION.cff`; bumped its version to match the release.
- First released version to roll up the 1.25.1–1.25.3 changes (README updating
  docs; Claude Code plugin 0-skills fix; Windows/Codex UTF-8 coverage-check fix;
  `food-pipeline` safer single-round defaults).

## 1.25.3 — 2026-07

- **Windows / Codex verification fix.** `scripts/check_journal_coverage.py` now
  reads coverage maps with `encoding="utf-8"`, so the required journal-coverage
  check no longer fails on Windows Python defaults (e.g. GBK) that cannot decode
  the UTF-8 markdown tables. Citation and privacy self-tests were already fine.
- **`food-pipeline` safer defaults (explicit authorization).** Default is **one**
  review→revise round, then FINALIZE — not an automatic two-round loop. A second
  round (RE-REVIEW) and applying Tracked Changes to the **original** Word
  manuscript both require the author's explicit confirmation; otherwise leave the
  original file untouched and deliver a revised copy / change log + response
  letter. Hard cap remains 2 rounds. Updated `food-pipeline` SKILL + state machine
  / gates / intake router, and `food-paper/references/revision-response.md`.

## 1.25.2 — 2026-07

- **Fix: Claude Code plugin loaded with 0 skills.** Skills live at the repo root
  (`food-research/`, `journals/*/`, …) rather than in a `skills/` directory, so
  the plugin manifest had no way to find them. Added a `skills` array to
  `plugin.json` listing all 31 skill directories (files stay in place, so
  cross-skill references and the Codex/MiniMax flat install are unaffected).
  Update with `claude plugin update academic-skills-food-nutrition`, then restart.

## 1.25.1 — 2026-07

- Documented **updating** in the README (updates are not automatic): Claude Code
  via `claude plugin update` (+ `marketplace update` to refresh), Codex/MiniMax by
  re-running the installer. Made `install.sh` update-safe (installs if new, else
  updates) and noted the update path in its header.

## 1.25.0 — 2026-07

- **Word review comments + tracked-changes revision workflow.**
  - `food-review`: when the manuscript is a Word (`.docx`) file (or LibreOffice/
    Pages/Google Docs), it now also returns the manuscript with **margin comments**
    (Word Review) anchored to the text, one per concern with reviewer lens +
    severity — in addition to the panel report. New
    `references/word-review-comments.md`.
  - `food-paper` (revise mode): revises **the original Word file with Tracked
    Changes** (resolving the comments) and produces a **point-by-point response
    letter as a new `.docx`**. New `references/revision-response.md`.
  - `food-pipeline`: across its **two** review→revise rounds (Stage 3 onward), all
    edits stay as tracked changes on the **one** original Word manuscript, and it
    delivers exactly **one combined review report** and **one combined response
    letter** (not per-round copies).
  Prefers the `docx` skill for the Word plumbing; falls back to a comments table /
  change log when Word tooling isn't available (never claims a file it didn't make).

## 1.24.0 — 2026-07

- **Complete Figure-story design for food-figure.** Added a workflow for planning
  8–12 panel journal figures from experimental sequence, evidence hierarchy,
  non-redundant panel questions, and source-data mapping. The consolidated
  synthetic/illustrative gallery now contains one final 11- or 12-panel version
  for each of four themes: active packaging, probiotic storage, trained sensory
  analysis, and analytical-method validation. Each uses a code-drawn schematic,
  topic-specific evidence panels, a shared semantic palette, and an explicitly
  illustrative synthesis panel. Source CSVs, captions, trace cards, and stable
  PDF + PNG names are kept in one gallery structure.
- **Binary privacy-scan hardening.** PDF and PNG checks now inspect stable
  printable metadata while excluding short compression-noise fragments that can
  resemble email addresses; the self-test covers both leak detection and this
  false-positive case.

## 1.22.0 — 2026-07

- **Renamed the `deep-research` skill to `food-deep-research`** to avoid name
  collisions with other agents' skills of the same name. Updated the folder,
  frontmatter name, marketplace registration, installer skill list, and every
  cross-reference in food-research/food-paper/food-review/food-pipeline and their
  references/agents. (Historical CHANGELOG entries keep the old name.)

## 1.21.0 — 2026-07

- **Fixed the Codex/MiniMax installer** (reported by a MiniMax/Mavis test). Two
  bugs: (1) wrong MiniMax path — now installs to Mavis's `~/.mavis/skills`
  (override `MAVIS_SKILLS_DIR`), not `~/.agents/skills`; (2) wrong layout — the
  whole repo was copied as one folder, leaving `SKILL.md` files two levels deep
  where agents don't recurse. Now each skill is installed **flat**
  (`…/skills/<name>/SKILL.md`) **plus** the shared `journals/` and `scripts/`
  directories, so `journal-selector` and the helper scripts keep working. Applies
  to both Codex and MiniMax Agent. `minimax` accepts the `mavis` alias.

## 1.20.0 — 2026-07

- **MiniMax Agent support.** `install.sh` gains a `minimax` target that installs
  the skills bundle into MiniMax Agent's shared skills directory
  (`${MINIMAX_SKILLS_DIR:-~/.agents/skills}/`); the default (`all`) now installs
  for Claude Code, Codex, **and** MiniMax Agent. README Install section and the
  project/plugin descriptions updated to name all three platforms.

## 1.19.0 — 2026-07

- **food-figure gallery and route hardening.** Added a reproducible,
  explicitly synthetic/illustrative food & nutrition gallery with four scenarios:
  active packaging/polyphenol retention, probiotic storage kinetics, sensory
  profiling, and method agreement/evidence-summary layouts. Each includes source
  CSVs, a base-R rendering script, PDF + PNG outputs, captions, and trace cards.
  The gallery exercises grouped bars, dose-response, kinetic, radar,
  Bland–Altman, and forest layouts.
- **AI schematic route improved.** Added a text-free draft → vector-label final
  workflow, a content-boundary/JSON-spec pattern, and AI-specific QA/trace-record
  requirements. The recorded test correctly reports an HTTP 403 service failure
  without representing an image as generated.
- **Privacy scan fix.** The scanner now safely examines readable text embedded in
  binary figure deliverables (PDF/PNG) instead of failing on UTF-8 decoding.

## 1.18.0 — 2026-07

- **Mandatory AI-use acknowledgement** when writing a manuscript. `food-paper`
  (`draft_writer`), `deep-research` (`compiler`), and `food-research` (`writer`)
  now always add an **Acknowledgements** section disclosing **this tool**
  (Academic Skills for Food & Nutrition Science) and the **AI model(s) and
  version(s)** used (e.g. Claude Opus 4.8 via Claude Code / OpenAI Codex /
  Gemini), what the AI did, and that the authors verified and take responsibility
  for all AI-assisted content. `declarations-guide.md` updated with the required
  content + template (move to the journal's required AI-statement location where
  applicable).

## 1.17.0 — 2026-07

- Added **multidisciplinary & cross-discipline journal skills** (from the MIT
  `Awesome-Journal-Skills` list) that food & nutrition researchers publish in,
  grouped by publisher format: `nature-portfolio` (Nature, Nature Communications,
  Nature Microbiology/Metabolism/Sustainability/Biotechnology/Medicine),
  `science-aaas` (Science, Science Advances, …), `cell-press` (Cell, Cell
  Metabolism, Cell Host & Microbe, …), `pnas`, and `multidisciplinary` (eLife,
  PLOS Biology/Medicine, National Science Review, The Innovation, Environmental
  Science & Technology, Gut, Gastroenterology, Diabetes Care, The ISME Journal).
  `journal-selector` updated; new `journals/_coverage_multidisciplinary.md` (35
  journals) + checker.

## 1.16.0 — 2026-07

Learned from the MIT `academic-figure-skills` / `academic-figure-generator`
projects and the visualization-agent pattern; improved `food-figure`:

- **AI-image route enriched** — a structured four-layer prompt method, a
  schematic figure-type taxonomy (process/mechanism/experimental-design/graphical-
  abstract/comparison, food examples), text-budget and flat-academic style rules,
  a JSON structured-spec option, and reinforced anti-fabrication (schematics only,
  never data figures, never invented values).
- **`references/color-palettes.md`** — curated colourblind-safe palettes
  (qualitative / sequential / diverging / monochrome) with a by-data-type decision
  hierarchy; `design-principles` now points to it.
- **`references/figure-provenance.md`** — a per-figure trace card (data → script →
  what it shows → supported claim → limitations) + self-contained caption (APA 7.0
  or journal) + LaTeX inclusion; ties figures to real data (grounding).
- **QA checklist** gains explicit blocked pitfalls (no 3-D, no pie, no dual y-axes,
  no truncated axes, error bars + n required, no rainbow colormap) and a
  provenance/caption check. Figures are now delivered with a caption + trace card.

## 1.15.0 — 2026-07

- **food-figure expanded** (informed by the nature-figure project):
  - Detailed Python guidance — matplotlib, seaborn, **subplot_mosaic** (named
    multi-panel), and **statsmodels** (regression/CI/ANOVA/mixed models).
  - Detailed R guidance — ggplot2, patchwork, **ComplexHeatmap**, **ggrepel**, and
    export via **svglite / cairo_pdf / ragg**.
  - Template libraries `examples/python_food_figures.py` and
    `examples/r_food_figures.R` with a ready function for every figure type
    (bar+letters, box/violin, kinetic/growth+fit, dose–response, scatter+CI,
    Bland–Altman, sensory radar, PCA, clustered heatmap, Kaplan–Meier, forest,
    multi-panel).
  - **AI image route (opt-in):** `references/ai-image-generation.md` — only when
    the user explicitly requests Gemini/ChatGPT/Claude, and only for schematics/
    graphical abstracts (never data figures, never fabricated data).
- **Privacy check for all skills.** New `scripts/privacy_scan.py` (flags local
  paths, temp/machine paths, IPs, tokens, non-project emails; self-tested) and
  `food-paper/references/privacy-and-confidentiality.md`. Wired into AGENTS.md, the
  food-pipeline pre-finalize gate, and every core skill's delivery step.

## 1.14.0 — 2026-07

- Banner: removed the "Initiated by…" line; added a responsible-AI declaration
  ("Use AI responsibly — scientists must validate AI-generated information. AI can
  make mistakes.").
- README: new **"Using AI responsibly for academic work"** section — researcher
  responsibility to validate AI output, disclosure, University of Melbourne
  GenAI/academic-integrity policy links, and two Nature/Nature Methods references
  (metadata verified via Crossref, not fabricated).

## 1.13.0 — 2026-07

- **Automatic GitHub releases on major updates.** Added
  `.github/workflows/release.yml`: when a new MINOR/MAJOR version (`x.y.0`) lands
  on `main`, a release `v<version>` is published automatically with notes from the
  matching CHANGELOG section. Patch releases do not trigger a release. Documented
  the rule in `AGENTS.md`.

## 1.12.0 — 2026-07

Informed by investigating the MIT `Light-skills` project (evidence/citation
gates, typesetting, figure styles):

- **Anti-fabrication / grounding (no made-up information).** New
  `food-paper/references/faithfulness-and-citation.md` (four-gate citation check
  + no-fabrication rules) and `scripts/verify_citations.py` (runnable gate that
  fails on references with no verifiable identifier or unbound claims). A repo-wide
  grounding rule added to `AGENTS.md`; the rule is wired into `food-paper`,
  `deep-research`, `food-research`, and `food-review`.
- **LaTeX support** documented and enabled: `food-paper/references/latex-guide.md`
  (Pandoc and latexmk/tectonic routes, engine/bib selection, journal templates,
  figure inclusion); `food-paper` format-convert mode now states it can prepare/
  edit `.tex` and build a PDF.
- **Figure style file** `food-figure/assets/publication.mplstyle` (Okabe-Ito,
  publication defaults) referenced from the Python guide.
- README acknowledges `Light-skills` (MIT).

## 1.11.5 — 2026-07

- OHAT risk-of-bias, in vitro: added `food-research/references/ohat-risk-of-bias.md`
  (full tool from the NTP/OHAT *In Vitro* guidance) and **corrected the in-vitro
  applicability** — **Q3 (participant selection) and Q4 (confounding) are Not
  Applicable** to in vitro (previously Q4 was wrongly included). Added the
  in-vitro-specific answering criteria per question (homogeneous-suspension logic,
  identical culture conditions, robotic-handling blinding, well/plate loss,
  substance purity/stability/solubility/volatility, etc.). `risk_of_bias` agent
  updated to match.

## 1.11.4 — 2026-07

- Added the development team contact email
  (`food_agents@lists.unimelb.edu.au`) to README, CONTRIBUTING.md, and AGENTS.md
  for research teams wishing to contribute or collaborate.

## 1.11.3 — 2026-07

- Added a project banner (`assets/banner.svg`) at the top of the README.

## 1.11.2 — 2026-07

- `AGENTS.md`: strengthened the language rule — **all project files must be in
  English**; if a file is created in another language, an English copy must be
  made and kept as the **main/canonical document** (non-English files are
  secondary translations with a language suffix).

## 1.11.1 — 2026-07

- Discoverability: added a keyword-rich README tagline (food science / nutrition,
  literature review, systematic review, PRISMA, meta-analysis, figures, peer
  review) and set GitHub repo topics (incl. `food`, `food-science`,
  `food-science-innovation`, `nutrition`). No functional changes.

## 1.11.0 — 2026-07

- Published to `github.com/PangenomeAI/academic-skills-food-nutrition` with a
  `main` (release) + `development` (working) branch model.
- Added **`AGENTS.md`** (machine-actionable collaborator/coding-agent instructions)
  and **`CONTRIBUTING.md`**: never push to `main`; work on `development` and open a
  PR; always update README + CHANGELOG and bump the version; verification steps;
  original-content (MIT) and English-only rules; structure conventions.
- README gained a Contributing section documenting the branching model.

## 1.10.0 — 2026-07

- Added a one-command **installer** (`install.sh`) that installs the skills as a
  Claude Code plugin (via `claude plugin marketplace add` + `install`) and as a
  Codex skills bundle (`${CODEX_HOME:-~/.codex}/skills/`), with a `curl | bash`
  remote form. README gained an **Install** section (native Claude Code one-liner
  + installer).
- Reworded attribution: the project is **initiated by the Food Science Group,
  University of Melbourne** and welcomes food & nutrition research groups
  worldwide to use and contribute.

## 1.9.0 — 2026-07

- Added curated, food-tuned **reference libraries** to the multi-agent skills
  (progressive disclosure), adapting only the genuinely useful upstream references
  and dropping internal-machinery ones:
  - Shared/canonical: `apa7-quickref` (food-paper), `literature-sources`,
    `source-quality-hierarchy`, `reporting-guidelines` (food-research),
    `ethics-integrity-checklist` (food-review) — cross-referenced by other skills.
  - `food-pipeline`: `pipeline-state-machine`, `quality-gates`, `mode-advisor`.
  - `deep-research`: `reasoning-and-fallacies`.
  - `food-paper`: `writing-style`, `writing-quality-check`, `paper-structure`,
    `declarations-guide`, `statistics-reporting`.
  - `food-review`: `review-criteria`, `quality-rubrics`, `editorial-decisions`.
  Each skill's frontmatter lists its references and a "References (load as needed)"
  section points agents to them.

## 1.8.0 — 2026-07

- `food-figure` rebuilt into a comprehensive, multi-file figure system:
  - **Data analysis + figure recommendation** front end — `scripts/analyze_data.py`
    profiles a CSV/TSV (variable types, cardinality, missingness, group/time/dose
    structure) and recommends the best figure type(s) with rationale (stdlib only,
    self-tested).
  - `scripts/backend_pref.py` — persists the Python-vs-R backend choice
    (get/set/clear/path, self-tested).
  - Nine reference docs (chart-types, data-to-figure rules, design-principles,
    figure-contract, qa-checklist, python-guide, r-guide, food-recipes,
    journal-specs) loaded progressively.
  - Six-step workflow (analyze → recommend → contract → backend gate → render/export
    → QA) covering all common scientific figure types in Python or R at the target
    journal's spec.

## 1.7.0 — 2026-07

- `food-paper` rebuilt into a whole-process, 12-subagent manuscript system:
  `intake`, `literature_lead` (→ food-research), `question_framer`,
  `data_curator`, `statistician`, `viz_designer` (→ food-figure),
  `structure_architect`, `argument_builder`, `draft_writer`, `polisher`,
  `citation_manager`, and `internal_reviewer` (→ food-review). Covers the full
  research lifecycle from field understanding through data analysis, statistics,
  figures, argument, drafting, and self-review — journal-aware throughout.
- `food-pipeline` rebuilt as a master orchestrator with its own `intake_router`
  and `quality_gate` subagents; routes the project to the specialist skills
  (each with its own subagent team) and enforces quality gates and the
  review→revise loop across research → write → review → revise → finalize.
- README revised to reflect the multi-subagent skill set; project attributed to
  the Food Science Group, University of Melbourne.

## 1.6.0 — 2026-07

- `food-review` rebuilt into a multi-reviewer panel: `review_coordinator`
  (editor-in-chief), `reviewer_methodology`, `reviewer_domain`,
  `reviewer_integrity`, `devils_advocate`, and `format_checker` (formatting/
  reference-style compliance vs the target journal — APA 7.0 default, or a
  specific journal via `journal-selector`). Outputs an editorial decision +
  revision checklist + response-letter skeleton.
- Journal coverage extended to the **Nutrition & Dietetics** journal list,
  grouped by publisher format alongside food: existing publisher skills
  (Elsevier, Wiley, Springer, Taylor & Francis, MDPI, Annual Reviews, BMC,
  Oxford) now list their nutrition journals, and three new skills were added —
  `cambridge-nutrition`, `frontiers-nutrition`, and `nutrition-other` (niche
  publishers). New `journals/_coverage_nutrition.md` map + checker update.

## 1.5.0 — 2026-07

- `food-research` **systematic** stream rebuilt into a full PRISMA pipeline with
  new subagents: `sr_search` (≥3 databases — Web of Science/Scopus/PubMed —
  combine + dedupe), `sr_screener` (two independent instances, three steps:
  title → abstract → full text), `sr_moderator` (compares the two screeners at
  each step and resolves conflicts), `risk_of_bias` (**OHAT** for in vitro /
  human / animal, 11 questions × 6 domains × 4-point scale), and `sr_synthesis`
  (PRISMA description → bias results → per-research-question synthesis). Clearer
  activation conditions for when to use systematic vs full review.
- New shared `writer` (writes the manuscript and exports **Word .docx**, APA 7.0
  or target-journal style via `journal-selector`) and `reviewer` (combined
  editorial + integrity review with a revision loop). The **full review** and
  **systematic** streams now both end in a reviewed Word manuscript.
- `data_extractor` now produces a results table organized by research question
  from the final shortlist.

## 1.4.0 — 2026-07

- `deep-research` rebuilt into a source-validated **literature-review** engine
  (12 subagents): `research_scope` (comprehensive scoping), `research_architect`
  (methodology blueprint), `investigator` (two-pass discovery + evidence),
  `source_screener` (journal-ranking tiers, reusing the food-research priority
  data), `source_verifier` (existence/venue/retraction/predatory/COI → Source
  Quality Matrix), `bibliography` (dedupe + APA 7.0 / target-journal formatting
  via `journal-selector`), `claim_verifier`, an expanded `synthesizer`, `critic`,
  `compiler` (writes & formats the review), and `editor` + `ethics_reviewer` with
  a compile↔review polish loop. Evidence is drawn only from validated sources.
- `food-research`: clarified the quick brief and full review streams with
  explicit invocation phrases and the exact subagent call sequence for each.

## 1.3.0 — 2026-07

- `food-research`: new **`journal_ranker`** subagent that prioritizes sources by
  journal ranking (Q1/Q2 food-science & nutrition, Nature/Science/Cell families,
  and Q1/Q2 in any other discipline = highest; Q3 second; Q4 avoided), backed by
  `references/journal-priority.csv` (JCR quartiles for Food Science & Technology
  and Nutrition & Dietetics). Applied to the quick brief, full review, and deep
  research streams — **not** to systematic review (eligibility-based inclusion).
- Clarified `food-research` into four named streams (quick brief / full review /
  deep research / systematic) with when-to-use guidance and a workflow flowchart.
- Added workflow flowcharts to `food-research` and the `systematic_reviewer`
  subagent.

## 1.2.0 — 2026-07

- New **`deep-research`** skill: general iterative deep-research engine (scope →
  plan → investigate → verify → synthesize → critique → report) with a 6-subagent
  team (`question_scoper`, `research_planner`, `investigator`, `verifier`,
  `synthesizer`, `critic`). Runs standalone or as `food-research`'s deep-dive engine.
- `food-research` gains a **PRISMA 2020 systematic-review** capability: new
  `systematic_reviewer` (protocol → search → PRISMA flow → extraction →
  risk-of-bias → synthesis ± meta-analysis) and `data_extractor` (parallel,
  batched structured extraction) subagents; `systematic` mode now routes to them.

## 1.1.0 — 2026-07

- `food-research` expanded to a comprehensive, multi-source workflow: four-layer
  search (structured → backward chaining → forward chaining → semantic),
  two-phase screening with a food-science quality rubric, and cross-source
  synthesis with an evidence matrix, evidence grading, coverage advisory, and gap
  analysis. MCP-tool-aware (PubMed, Consensus, bioRxiv, CrossRef, …) with web
  fallback.
- Added four `food-research` subagents: `search_strategist`, `source_scout`,
  `screener_appraiser`, `synthesis`.

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
