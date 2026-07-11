---
name: food-research
description: "Run a literature and evidence-synthesis workflow for food & nutrition science. Use when the user wants to research a food/nutrition topic, do a literature review, build an evidence brief, screen and synthesize sources, or scope a systematic review. Prioritizes food-science databases and food-safety/regulatory sources and grades evidence. Triggers: research this topic, literature review, evidence synthesis, systematic review, scope a review, find the literature, what does the evidence say, food science research, nutrition evidence."
metadata:
  version: "1.0.0"
  verified: "2026-07"
  related_skills: [food-paper, food-review]
---

# Food-Research — Evidence Synthesis for Food & Nutrition Science

Turn a question into a defensible evidence brief. Original work; no third-party
research text is reused.

## Modes
- **quick brief** — fast orienting summary with the strongest sources and open questions.
- **full review** — structured narrative review with an evidence map and gaps.
- **systematic** — PRISMA-style scoping: explicit question, search string, screening log, inclusion/exclusion, extraction table (no unsupported meta-analysis unless data allow).

## Workflow
1. **Frame the question.** For interventions/nutrition, use a PICO frame (Population, Intervention/Exposure, Comparator, Outcome); for composition/process questions, define the food matrix, factor, and measured response. State scope and exclusions.
2. **Plan the search.** Prioritize:
   - **Primary literature:** FSTA (Food Science and Technology Abstracts), PubMed, Web of Science, Scopus, AGRICOLA.
   - **Safety & regulatory / grey literature:** EFSA, US FDA, USDA (incl. FoodData Central), Codex Alimentarius, EU and national food-standards bodies.
   Record the search strings and databases so the search is reproducible.
3. **Screen.** Title/abstract → full text; log reasons for exclusion. Distinguish peer-reviewed evidence from regulatory/industry grey literature.
4. **Extract.** Tabulate study design, food/matrix, sample size, methods (with validation where relevant), outcomes, effect direction/size, and funding/conflicts (common and material in food/nutrition).
5. **Synthesize.** Integrate across sources; resolve conflicts by weighing design and rigor; separate consistent findings from contested ones.
6. **Grade the evidence.** Prefer systematic reviews/meta-analyses and controlled trials for health/nutrition claims; require method-standardized measurements (AOAC/ISO) for compositional/process claims. State the confidence level and why.
7. **Report gaps.** What is missing, under-powered, or single-batch; propose the next study.

## Output
An evidence brief containing: question and scope, search strategy, an evidence
map (claim → supporting sources → strength), a synthesis, graded conclusions,
limitations, and a gap list. Cite sources with DOIs. Feeds directly into
`food-paper` (Introduction and Discussion evidence) and `food-pipeline`.

## Rigor notes specific to food & nutrition
- Watch for pseudo-replication (analytical replicates counted as biological n).
- Flag matrix effects, single-cultivar/single-batch generalization, and unvalidated assays.
- Note funding and conflicts of interest explicitly.
