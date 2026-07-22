# Changelog

## 1.40.0 — 2026-07

- **Skills now ask for full-text access up front, with a highlighted request.** Any
  skill that builds a knowledge base or evidence synthesis surfaces **one prominent
  chat callout** asking the user to point it at their **EndNote `.Data` folder** (or
  Zotero `storage/` / Mendeley folder) or a **folder of PDFs**, or to reply
  "open-access only". Reading PDFs from a user-provided folder is confirmed as the
  correct way Claude reaches that full text (Claude Code and Cowork). It asks once and
  doesn't block — declining proceeds at open-access + abstract level with paywalled
  sources flagged. Added to `full-text-access.md` (template) and wired as a "first
  move" into `food-review` (`knowledge_builder`), `food-research`, and
  `food-deep-research`; `agri-*` inherit it via delegation.
- **The extraction agents now actually retrieve full text — they no longer assume it.**
  `screener_appraiser` (Phase B), `data_extractor`, `investigator` (Pass 2), and
  `source_verifier` previously said "read the full text" without saying how, so in
  practice they stopped at abstracts. Each now works the retrieval ladder
  (open access via `resolve_oa.py`/PMC → connected tool → **the user's
  reference-manager library / provided PDFs**) **before** extracting, and marks any
  source that stays paywalled and unsupplied as abstract-only/unverified with its
  access route — never inventing a value or locator from an abstract.

## 1.39.0 — 2026-07

- **README "Limitations" section.** States plainly that the tool is only as informed
  as the literature it can legitimately read: metadata/abstracts/open-access full text
  work with no setup, but **paywalled articles are read at abstract-level only and
  flagged as unverified** unless the user supplies a copy — the tool never bypasses
  paywalls and never summarizes a paper it did not read. Lists the four ways to lift
  the limit, plus the standing limits (no live model database; verify everything).
- **Reference-manager library as a full-text source.** Documented in
  `full-text-access.md`: a user's **EndNote** (`<Library>.Data/PDF/`), **Zotero**
  (`storage/`), or **Mendeley** library is a folder of already-downloaded, legitimate
  PDFs. Point Claude Code / Cowork at that folder (OneDrive/Dropbox-synced libraries
  included) and it maps each cited reference to its PDF by DOI/title and reads it —
  the highest-coverage, fully-legal way to give a review the full picture of a
  manuscript's literature. No EndNote MCP connector is required; it is plain,
  read-only file access.

## 1.38.1 — 2026-07

- **Publisher consent-gate fallback in `full-text-access.md`.** A live test on an
  open-access reference (Hassani et al., *Microbiome* 2018) showed the BMC publisher
  page redirecting through a SpringerLink cookie-consent/auth IdP that a simple
  web-fetch can't clear — not a paywall, but it blocks the fetch. Guidance now says to
  **prefer the PMC / Europe PMC HTML mirror** for reading an OA article's text, and to
  fall back to it whenever a publisher page bounces through a consent/auth redirect.
  Added the worked DOI→OA→full-text example.

## 1.38.0 — 2026-07

- **Fetchable literature-API endpoints + a one-command OA resolver.** The model has
  no live database of its own — literature access is entirely via tools — so
  `full-text-access.md` now lists the public REST endpoints the built-in web-fetch can
  hit with **no connected tool**: Unpaywall and OpenAlex (legal free-PDF URL), Crossref
  (metadata/license), Semantic Scholar (abstract + OA PDF), Europe PMC (PMC-OA full
  text), and PubMed E-utilities. These return metadata, abstracts, and the OA PDF URL
  when one exists — **never paywalled full text**.
- New **`scripts/resolve_oa.py`** (`--selftest`): give it a DOI, it queries
  Unpaywall→OpenAlex and prints `{is_oa, pdf_url, landing_url, source}`, exiting 0 when
  a free PDF is found and 3 when the DOI is closed-access (so it never dresses up a
  paywalled paper as readable). Verified live — finds the real PLOS OA PDF and reports
  a paywalled Biochimie DOI as `is_oa: false`. Wired into `knowledge_builder` and the
  `AGENTS.md` self-test suite.

## 1.37.0 — 2026-07

- **Full-text access for the review knowledge base.** During testing,
  `knowledge_builder` correctly refused to summarize cited papers it could not open
  ("can't extract cited source PDFs in this environment") — honest, but it had no
  real retrieval strategy and no way for the author to supply access. New
  `food-research/references/full-text-access.md` defines a **retrieval ladder** —
  open-access copy (Europe PMC/PMC, Unpaywall/OpenAlex OA URL, preprint servers, free
  publisher HTML) → a connected full-text tool/MCP → institutional/green-OA copy →
  **user-supplied PDFs** → a user-driven logged-in library browser session — with
  **legitimate access only** (no paywall bypass or scraping).
- **`knowledge_builder` now escalates instead of silently degrading.** It marks
  **load-bearing** citations, works the ladder, and if the papers behind the central
  claims stay paywalled it raises **one consolidated request** ("drop these PDFs in
  the folder or enable a full-text tool, otherwise these claims are assessed at
  abstract-level and flagged as unverified") — never per-paper prompts, and peripheral
  citations stay abstract-level without asking. The cited-source audit and
  `Coverage & limits` now record each source's **access route** and how many
  load-bearing citations were read in full vs abstract-only, so the grounding's depth
  is transparent.
- Wired the retrieval policy into `food-research`/`food-deep-research` (`source_scout`,
  `source_verifier`, `investigator`) and `literature-sources.md`. The `agri-*` skills
  inherit it via delegation. **Answer to "do we need extra programs":** no setup is
  needed for metadata, abstracts, and open-access full text; for paywalled papers,
  the easiest fix is to **drop the cited PDFs in the project folder**, or connect a
  full-text literature tool, or use a logged-in institutional browser session.

## 1.36.1 — 2026-07

- **Documented `food-paper`'s eight modes in the README** — new
  *"`food-paper` modes: what each one does"* section with a table of every mode, what
  it does, and **what to say to trigger it** (you never type a mode name). **`polish`**
  and **`format-convert`** are marked as the two most-used; `agri-paper` shares the
  same eight modes.
- **The `polish` mode description undersold it.** It read only "language editing to
  publication-quality English", with no hint that `polisher` also runs
  `human-writing.md`. Both the SKILL.md mode line and the README now state that
  `polish` **removes AI writing tells** (inflated significance, vague attribution,
  stock AI vocabulary, copula avoidance, filler, stacked hedging, generic upbeat
  endings) and runs the two-pass *"what still reads as machine-written?"* check —
  while **keeping** calibrated hedging, passive Methods, and journal-mandated form,
  and never changing a number, claim scope, or citation. Restates that this is a
  writing-quality edit, **not** a way to hide AI use.

## 1.36.0 — 2026-07

- **`journal-selector` no longer appears in the skill list (12 → 11 skills).** It is
  machinery the other skills use, not something a user invokes, so it cluttered the
  `/` menu. Unregistered from `plugin.json` and `marketplace.json`; it still **ships
  with the plugin** and is now loaded as a **shared procedure file**
  (`journal-selector/SKILL.md`) — the same treatment the 24 `journals/*` author-guideline
  files already get. Every "call the `journal-selector` skill" phrasing across
  `food-*`/`agri-*` was rewritten to load the file, so journal resolution keeps
  working; users still reach it by naming a journal to any skill.
- **Reformatting a finished manuscript is now discoverable.** A user with a done,
  reviewed, polished paper who only wants another journal's format should use
  **`food-paper` / `agri-paper` `format-convert`** — not the pipeline, which would
  re-research, re-review, and re-edit finished work. Added explicit triggers to both
  descriptions ("reformat my manuscript for a different journal", "change the journal
  format", "my paper is finished I just need the formatting"), a **"Which one do I
  pick?"** table to the README, and a routing row + explicit warning to
  `food-pipeline`'s `mode-advisor.md`.

## 1.35.0 — 2026-07

- **Reports are Word (`.docx`), not Markdown.** `report-format.md` never named a file
  format, so reports were shipping as `.md`. It now specifies **Word as the
  deliverable** — Markdown is a working format only — with the export path (Pandoc
  `pandoc report.md -o report.docx`, else the **`docx` skill**), a filename
  convention, the colour legend applied as real Word formatting, no Markdown syntax
  left in the file, and the standing rule: if no Word tooling exists, say so and hand
  over the Markdown **with** the conversion command — **never claim a `.docx` you did
  not produce**. Wired through `food-review` (output + `review_coordinator`),
  `food-paper` (revise), and `food-pipeline`.
- **`food-pipeline` now delivers ONE report, not two.** It previously emitted a
  combined review report **and** a separate response letter. There is now exactly
  **one manuscript** and **one `Review_and_Response_Report_<slug>_<date>.docx`** that
  **evolves in place**: `food-review` writes the reviewer feedback (black) at Stage 3;
  `food-paper` fills each item's `Response (<type>)` (blue) into the **same file** at
  Stage 4; an authorized round 2 appends `R2-*` items to it. The result carries
  **both the reviewer feedback and the editing response** in one document. **No
  separate reviewer report and no standalone response letter in the pipeline.**
- **The point-by-point response letter is now standalone-only** — produced by
  `food-paper` revise when responding to a **real journal's reviewers** outside the
  pipeline (`revision-response.md` §2a pipeline / §2b standalone). The no-Word-tooling
  Markdown path is explicitly a **last resort**, after trying Pandoc and the `docx`
  skill.
- **The `agri-*` skills inherit all of the above** through delegation;
  `agri-review` and `agri-pipeline` updated to state the `.docx` rule and the single
  Review & Response Report.

## 1.34.0 — 2026-07

- **New `agri-*` skill set for agricultural science (5 skills).** `agri-research`,
  `agri-deep-research`, `agri-paper`, `agri-review`, and `agri-pipeline` — each
  **delegates its machinery to the corresponding `food-*` skill** (same subagents,
  gates, modes, and output contracts) and applies three substitutions: the
  **persona**, the **evidence base**, and **journal routing**. No duplicated
  architecture; figures still route through the domain-neutral `food-figure`.
  The plugin now registers **12 skills** (was 7) — verified by installing the plugin
  and reading its component inventory.
  - **Persona:** a **senior agricultural scientist of the specific discipline** —
    agronomy · agriculture multidisciplinary · dairy & animal science · soil science ·
    agricultural economics & policy · horticulture · agricultural engineering.
  - **Evidence base:** agriculture + multidisciplinary literature ranked as in the
    food suite — **Tier 1** the 230 Q1/Q2 agriculture journals + Nature/Science/Cell/
    PNAS + Q1/Q2 adjacent disciplines; **Tier 2** Q3 for gaps; **Q4 avoided**.
    FAO/USDA/CGIAR/EFSA/extension sources count as dated evidence. Systematic reviews
    still include by pre-specified eligibility, never prestige.
  - **Agricultural rigour:** field-trial reporting (site, season/years, soil,
    cultivar, design, replication), **the experimental unit / pseudoreplication**,
    G×E and season-to-season variation, ARRIVE for animal work, soil sampling depth
    and equivalent-soil-mass basis, no pot-to-field extrapolation. Contract:
    `agri-research/references/agriculture-domain.md`.
  - Everything else is **inherited unchanged**: anti-fabrication grounding, four-gate
    citations, privacy scan, `journal-selector` ask-once, the review report format
    and editor queries, `human-writing.md`, and the mandatory AI-use disclosure.
- **Agriculture journal coverage (Q1 + Q2): 230 journals** across the seven JCR
  agriculture categories (JCR 2025), **deduplicated** across categories at each
  journal's best quartile — new `journals/_coverage_agriculture.md` (109 Q1, 121 Q2).
  **No duplicate formats:** because the journal folders are publisher-tiered, **185 of
  the 230 reuse an existing skill** (an Elsevier agronomy journal follows the same
  Guide for Authors as an Elsevier food journal), and journals already in the food or
  nutrition lists **keep their existing folder** (Journal of Dairy Science →
  `j-dairy-science`, Food Policy → `elsevier-food`). Only the society/regional tail
  gets one new folder, **`journals/agri-other`** (Copernicus, CSIRO, Czech Academy,
  CABI, AAAP, KSAST, ISTA, ASEV, USP/ESALQ and similar). `journal-selector` resolves
  agriculture journals and lists the common routings.
- `scripts/check_journal_coverage.py` now validates the agriculture map too, and
  accepts rows with extra columns (agriculture adds Category and Quartile) as long as
  the row starts with the number and ends with the skill folder.
- README, plugin, and marketplace descriptions updated to cover food, nutrition **and
  agriculture**; added `agriculture`/`agronomy`/`soil-science`/`horticulture` keywords.

## 1.33.0 — 2026-07

- **`human-writing.md` completed against both sources.** A coverage audit found the
  first version carried only **20 of the 33** `humanizer` patterns and none of
  Wikipedia's citation/markup categories. Now **33/33**, reorganised into five
  groups. Added: name-dropping/canned notability · persuasive authority tropes
  ("It is well established that") · false ranges · hyphenated word-pair overuse ·
  inline-header vertical lists · emoji · curly-quote inconsistency · fragmented and
  skipped headings · manufactured drama and aphorism formulas ("X isn't just Y —
  it's Z") · conversational rhetorical openers ("Let's dive in") · knowledge-cutoff
  disclaimers · pronounced style shifts between sections · **voice calibration**
  from the author's own prior papers.
- **New: citation and markup tells from Wikipedia's "Signs of AI writing"**, which
  `humanizer` does not cover and which matter most for manuscripts —
  **DOIs that resolve to an *unrelated* article**, unresolvable DOIs / invalid ISBN
  checksums, plausible-but-invented references, book citations without page numbers,
  references never cited in the text, `utm_source=` tracking junk, citation stacking,
  mixed reference styles, **Markdown leaking into a Word manuscript**, unfilled
  placeholder text, and leftover LLM tokens (`oaicite`, `oai_citation`,
  `contentReference`, `turn0search…`, `citeturn`, `grok_card`, `:::writing`).
- **`scripts/verify_citations.py` now enforces Gate 2 (Identity), not just existence.**
  A resolving DOI was previously enough to pass — so an invented reference carrying a
  real DOI that belongs to a *different* paper slipped through, exactly the failure
  Wikipedia documents. The `--online` check now fetches the DOI's registered title
  from Crossref and fails when it doesn't match the cited title (word-overlap
  comparison, tolerant of subtitle/case/punctuation differences, silent when there is
  nothing to compare). Verified against live Crossref; self-test extended.
- Reaffirmed in the guide: **AI detectors are unreliable in both directions** — never
  treat a detector score as a target or as evidence, and never accuse an author of AI
  use. Expanded the "ineffective indicators" false-positive list.

## 1.32.0 — 2026-07

- **Write like a scientist, not like a chatbot.** New canonical
  `food-paper/references/human-writing.md`: the AI writing tells to strip —
  inflated significance ("pivotal role", "paves the way"), "-ing" tack-ons, vague
  attribution ("studies have shown" → a specific citation), stock AI vocabulary
  ("delve", figurative "landscape", "showcase", "testament"), copula avoidance
  ("serves as" → "is"), promotional adjectives, negative parallelism, rule-of-three
  padding, filler, hedge **stacking**, generic upbeat endings, formulaic "Challenges
  and Future Prospects" scaffolding, and synonym cycling — plus a two-pass check
  ("what still reads as machine-written?"). Wired into `food-paper`
  (`draft_writer`, `polisher`, `writing-style.md`, `writing-quality-check.md`),
  `food-research` (`writer`), `food-deep-research` (`compiler`), and `food-review`
  (reviewers now flag these as substantive writing-quality faults).
  Pattern taxonomy informed by the MIT-licensed `humanizer` skill (Siqi Chen) and
  Wikipedia's "Signs of AI writing", rewritten for scientific manuscripts.
- **Academic exceptions are explicit**, because general humanising rules misfire on
  manuscripts: **calibrated hedging is kept** (de-hedging into an unsupported claim
  is a fabrication-grade error), **passive voice stays in Methods**, and
  **journal-mandated heading case/structure wins** over any style rule. A style edit
  may never change a value, a claim's scope, or a citation.
- **Explicit integrity boundary:** this is a *writing-quality* edit, **not** a way to
  hide AI involvement, defeat AI detectors, or evade a journal's or institution's AI
  policy. **The mandatory AI-use disclosure is unaffected.** Documented in the
  README's "Using AI responsibly" section and enforced in the guide itself.
- **Zenodo DOI and citation metadata.** Added the DOI badge and a **Citation**
  section to the README, explaining Zenodo's two DOIs — the **concept DOI**
  [10.5281/zenodo.21372994](https://doi.org/10.5281/zenodo.21372994) (cite the
  project; always resolves to the latest version) and the per-release **version DOI**
  (cite the exact version you ran). `CITATION.cff` gains `doi` (the concept DOI, so
  GitHub's "Cite this repository" always points at the latest) and `date-released`.
  Acknowledged `humanizer` (MIT) in the README.

## 1.31.1 — 2026-07

- **Fix: `food-paper` and `journal-selector` did not appear on Claude online (5 of 7
  skills shown).** Both descriptions used `<journal>` as a placeholder — the only two
  of the seven skills containing angle brackets. Read as HTML/XML tags, they made the
  web client drop those skills, while Claude Code (desktop) tolerated them and showed
  all 7. Length was not the cause (`food-figure`, at 926 chars, is longer than
  `food-paper` and loaded fine). Replaced the placeholders with bracket-free wording
  and concrete journal examples ("publish on a specific journal", "I want to publish
  on Food Chemistry", "submit to LWT"), which also match user phrasing better. All 7
  skill descriptions are now free of HTML/XML-like placeholders.

## 1.31.0 — 2026-07

- **OpenClaw support.** The installer (`install.sh`) now supports `openclaw` as a
  target platform, installing skills into `${OPENCLAW_HOME:-~/.openclaw}/skills/`
  with the same flat layout used for Codex and MiniMax Agent. OpenClaw is also
  auto-detected in the `all` target. README updated with install and update
  instructions.

## 1.30.0 — 2026-07

- **`food-pipeline` no longer researches the same field twice.** When the pipeline
  ran **Stage 1** (entry at Stage 0/1), Stages **3 · REVIEW** and **5 · RE-REVIEW**
  now carry the **Stage-1 evidence base** into `food-review` instead of letting
  `knowledge_builder` repeat a full literature search. It reuses Stage 1's validated
  sources / synthesis / gap list and **tops it up via `food-research` `quick brief`
  to identify the field's key review publications and read those reviews in full** —
  knowledge base = **Stage-1 knowledge + key-review knowledge**. The manuscript's own
  cited sources are still read and audited (Pathway A), reusing Stage-1 records
  rather than re-fetching. `intake_router` records `stage1_evidence_base:
  available | none` and passes it through `review_coordinator`.
- **Standalone `food-review` is unchanged** — with no Stage-1 base (used standalone,
  or pipeline entry at Stage 2/3 with a finished draft) it still builds the full
  Pathway A + B knowledge base. (`food-review` skill 2.3.0.)

## 1.29.0 — 2026-07

- **`food-review` grounds the panel before it critiques.** New `knowledge_builder`
  subagent runs **first** and builds a shared **knowledge base** from two pathways:
  **(A)** retrieve and **read the full articles the manuscript cites**, extracting
  what each actually shows and auditing whether it supports the claim it is attached
  to; **(B)** extract the manuscript's **keywords and research disciplines** and
  search the literature for the field's key work — it may use the `food-research`
  **full review** branch for discovery/screening, but **knowledge extraction only:
  no literature-review article, PRISMA flow, or synthesis**. A + B yield the state of
  the art, standard methods and benchmark ranges, consensus vs contested points, a
  novelty map, gaps, and a cited-source audit. `reviewer_methodology` (benchmarks),
  `reviewer_domain` (novelty map), `reviewer_integrity` (cited-source audit) and
  `devils_advocate` (contested points) now judge from this evidence rather than
  impression; sources never retrieved are marked, never summarized. `quick` mode uses
  a light Pathway-A pass. (`food-review` skill 2.2.0.)
- Added the University of Melbourne **"Using AI as a graduate researcher"** policy
  link (graduate researchers and digital assistance tools) to the README's UoM policy
  section.

## 1.28.2 — 2026-07

- **Fix: EndNote/Zotero/Mendeley citation field codes leaking into the manuscript.**
  Reference-manager citations are Word **fields** — the code (`ADDIN EN.CITE
  <EndNote>…</EndNote>`) lives in a hidden `w:instrText` and only `(Author, Year)`
  is shown. When an edit read every run and rewrote the paragraph as plain text, the
  hidden code was dumped into the body as a stray block before the citation. New
  guidance `food-paper/references/word-field-codes.md` (treat each citation field as
  an atomic unit; never flatten `w:instrText` into visible text; keep `fldChar`
  runs together; warn if a tool can't preserve fields), wired into the revise,
  comment, and format-convert paths. New `scripts/check_docx_fields.py` (with
  `--selftest`) detects leaked field codes in a `.docx`'s visible text; added to the
  pre-delivery checks and `AGENTS.md`.

## 1.28.1 — 2026-07

- **Editorial decision made explicit in the report format.** `report-format.md`
  now spells out that Part B carries the **panel verdict — exactly one of Accept ·
  Minor Revision · Major Revision · Reject — with the decisive reasons** (citing
  issue IDs and what would lower the severity), as the coordinator's weighing of
  the whole panel. (The decision was already produced; this pins it in the spec so
  it is never dropped.)

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
