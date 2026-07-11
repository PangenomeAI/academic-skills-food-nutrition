---
name: food-research
description: "Run a comprehensive, multi-source literature and evidence-synthesis workflow for food & nutrition science. Use when the user wants to research a food/nutrition topic in depth, do a literature review, build an evidence brief, screen and synthesize many sources, verify citations, or scope a systematic review. Coordinates food-science databases, preprints, semantic search, and food-safety/regulatory sources; runs a four-layer search, two-phase screening, and cross-source synthesis via subagents; grades evidence and maps gaps. Triggers: research this topic, deep literature review, comprehensive review, evidence synthesis, systematic review, scope a review, find all the literature, what does the evidence say, food science research, nutrition evidence, survey the field."
metadata:
  version: "2.0.0"
  verified: "2026-07"
  related_skills: [deep-research, food-paper, food-review, food-pipeline]
  subagents: [search_strategist, source_scout, screener_appraiser, synthesis, systematic_reviewer, data_extractor]
---

# Food-Research — Comprehensive Evidence Synthesis for Food & Nutrition Science

Build a broad, defensible understanding of a topic by searching many sources,
screening them consistently, and synthesizing across them. Original work; no
third-party research text is reused. Architecture informed by open community
literature-search skills (see Acknowledgements in the repo README).

## When to go deep vs light
- **quick brief** — fast orientation: run one search pass, top sources, open questions.
- **full review** — the default: full four-layer search + two-phase screening + synthesis.
- **systematic** — full PRISMA 2020 systematic review, run by the **`systematic_reviewer`** subagent (fixed protocol, reproducible search, PRISMA flow counts, structured extraction via `data_extractor`, risk-of-bias assessment, synthesis ± meta-analysis, certainty of evidence). Use this whenever the user asks for a systematic review, PRISMA review, or meta-analysis.

## Subagents (dispatch, don't inline)
Run these as subagents (via the Agent tool). Layers that are independent — e.g.
per-source retrieval — run in **parallel**.
1. **`search_strategist`** — turns the question into a search plan: concepts, synonyms/controlled vocabulary (MeSH, FSTA/CAB thesaurus terms), Boolean strings per database, filters, and the source list.
2. **`source_scout`** — executes the four-layer retrieval across sources, records hit counts, and deduplicates into one candidate set.
3. **`screener_appraiser`** — two-phase screening + the food-science quality rubric; outputs the included set with quality tags.
4. **`synthesis`** — evidence matrix, contradiction resolution, evidence grading, gap analysis, and the coverage advisory.

For a quick brief you may run the workflow inline without subagents.

## Step 1 — Frame the question (`search_strategist`)
- Interventions/nutrition: PICO (Population, Intervention/Exposure, Comparator, Outcome).
- Composition/process/safety: define the food matrix, factor/treatment, and measured response.
- State scope, timeframe, languages, and exclusions. Break the question into concepts and list synonyms + controlled-vocabulary terms per concept.

## Step 2 — Plan the sources
Cover several source classes so the picture isn't skewed by one index:
- **Bibliographic:** FSTA (Food Science & Technology Abstracts — the core food index), PubMed/MEDLINE, Web of Science, Scopus, CAB Abstracts, AGRICOLA, AGRIS (FAO).
- **Preprints:** bioRxiv, ChemRxiv, agriRxiv.
- **Semantic / aggregators:** CrossRef, Semantic Scholar, Consensus, Dimensions, Lens.org.
- **Safety & regulatory / grey:** EFSA, US FDA, USDA (incl. FoodData Central), Codex Alimentarius, WHO, EU/national food-standards bodies.
- **Chemistry / bioactives:** PubChem, ChEMBL, FooDB, Phenol-Explorer.
- **Methods / standards:** AOAC, ISO.

**Tooling:** use whatever literature MCP tools are connected (e.g. PubMed,
Consensus, bioRxiv, CrossRef, Scopus/ScienceDirect) for live retrieval; fall
back to web search for any source without a tool. Record which tool/source
produced each result so the search is reproducible.

## Step 3 — Four-layer search (`source_scout`)
1. **Layer 1 — structured search:** Boolean/keyword + controlled vocabulary across the bibliographic databases (target 100–500 raw hits). Apply date/language filters.
2. **Layer 2 — backward chaining:** mine the reference lists of the key reviews and seminal papers for older frequently-cited work.
3. **Layer 3 — forward chaining:** "cited by" from seminal works to catch the latest research.
4. **Layer 4 — semantic / cross-disciplinary:** related-article and semantic tools to catch methodologically or disciplinarily adjacent work (chemistry, engineering, nutrition, microbiology) that keyword search misses.
- **Deduplicate** by DOI/title across sources. Record the hit count at each layer.
- **Stop** when the search saturates — e.g. ≥3 of: no new themes appearing, citation loops closing, timeframe covered, key authors/venues all seen, new hits <10% novel.

## Step 4 — Two-phase screening & appraisal (`screener_appraiser`)
- **Phase A — title/abstract:** apply inclusion/exclusion; narrow to ~30–50 candidates.
- **Phase B — full text:** read the semantically strong and borderline items; land ~15–30 (more for systematic).
- **Quality rubric (score each source):** study design & rigor; replication and whether n is biological (not pseudo-replicated); method validation (LOD/LOQ, recovery, controls, appropriate standards); journal quality and predatory/fabrication check; relevance to the question; recency/currency. Tag each source **High / Medium / Low**.
- Universal gates (relevance, methodological soundness, predatory/fabrication) are never waived; only publication-type/recency expectations flex by subfield.

## Step 5 — Synthesis (`synthesis`)
- **Evidence matrix:** source × theme grid showing coverage density and method spread.
- **Integrate & resolve conflicts:** weigh by design and rigor; separate consistent findings from contested ones; explain disagreements (matrix, method, dose, population).
- **Grade the evidence:** prefer systematic reviews/RCTs for health/nutrition claims; require standardized measurement (AOAC/ISO) for compositional/process claims. State confidence and why.
- **Coverage advisory:** flag when >70% of sources share one publication year, region, food matrix, method, or venue family — a bias risk.
- **Gaps:** under-powered areas, missing methods, population/geographic voids; propose the next study.

## Deliverables
An evidence brief containing: question & scope; **reproducible search strategy**
(sources, Boolean strings, filters, dates); screening funnel with counts;
**annotated bibliography** (per source: design, findings, relevance, quality tag,
intended paper section); **literature/evidence matrix**; graded conclusions;
**coverage advisory**; and a **gap list**. Export references as `.bib`/`.ris`
(deduplicated) for reuse.

## Deep dives
For a subtopic that needs open-ended investigation beyond the literature (e.g.
regulatory landscape, market/technology state), call the **`deep-research`**
skill and fold its sourced synthesis back into the evidence brief.

## Handoff
Sources tagged and assigned by section feed `food-paper` (Introduction and
Discussion evidence, reference list) and are orchestrated by `food-pipeline`.

## Food & nutrition rigor notes
Watch for pseudo-replication (analytical replicates as biological n); matrix
effects and single-cultivar/single-batch over-generalization; unvalidated
assays; and undisclosed funding/conflicts, which are common and material here.
