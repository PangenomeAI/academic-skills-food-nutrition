---
name: food-review
description: "Simulate peer review of a food & nutrition manuscript from the referee's perspective. Use when the user wants a pre-submission review, reviewer report, mock peer review, or a critique of methodology, novelty, statistics, or food-safety/ethics before submitting. Returns independent reviewer lenses plus an editor summary and a decision recommendation. Triggers: review my paper, peer review, referee report, critique my manuscript, pre-submission review, is my paper ready, assess novelty and rigor, mock review."
metadata:
  version: "1.0.0"
  verified: "2026-07"
  related_skills: [food-paper, food-pipeline]
---

# Food-Review — Referee-Perspective Review for Food & Nutrition Manuscripts

Give an author the review they would get from a good food-science journal, so
they can fix problems before submitting. Original work; no third-party review
text is reused.

## What it produces
Three independent reviewer reports (distinct lenses), one editor synthesis, and
a decision recommendation (Accept / Minor / Major / Reject) with the reasons.
Each report lists strengths, then numbered concerns split into **major** and
**minor**, each concern actionable.

## Reviewer lenses
1. **Methodology & reproducibility** — is the design sound; is n adequate and biological (not pseudo-replicated); are methods validated (LOD/LOQ, recovery, controls, blanks); can the work be reproduced from the Methods?
2. **Statistics & data** — right test for the design; assumptions checked; multiple-comparison handling; error type and n disclosed; figures/tables consistent with the stats; no truncated/misleading axes.
3. **Novelty, scope & significance** — is the advance real and in scope for the target journal; is identification/quantification defensible (standards or MS/MS, not library hits); are claims proportionate to the evidence.

Also always check: **food-safety/ethics** (sensory-panel consent and size, animal-tissue and pathogen handling, allergen disclosure) and **reporting completeness** (units, cultivar/batch, storage, panel details).

## Process
1. Read the manuscript against the target journal's scope and constraints (via `journal-selector` if a journal is named).
2. Run each lens independently; do not let one lens soften another.
3. Write per-reviewer reports (strengths → major → minor), each concern with a concrete fix or the evidence needed.
4. Editor synthesis: the decisive issues, points of agreement/disagreement, and the recommendation with justification.
5. Optionally emit a revision checklist that `food-paper` (revise mode) can act on.

## Tone
Firm, specific, and fair — critique the work, not the author. Every major
concern must name what would resolve it.

## Handoff
Feeds `food-paper` (revise) and is orchestrated by `food-pipeline` in the
review → revise loop.
