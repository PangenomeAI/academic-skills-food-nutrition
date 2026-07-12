# Changelog

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
