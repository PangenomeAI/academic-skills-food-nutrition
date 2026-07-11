---
name: food-pipeline
description: "Orchestrate the full food & nutrition paper workflow end to end: pick the target journal, research, write, review, and revise. Use when the user wants to go from a topic or dataset to a submission-ready manuscript, or wants the whole process coordinated rather than one step. Triggers: write my paper end to end, take this from research to submission, run the full paper workflow, help me get this published, manage the whole paper process."
metadata:
  version: "1.0.0"
  verified: "2026-07"
  related_skills: [journal-selector, food-research, food-paper, food-review, food-figure]
---

# Food-Pipeline — End-to-End Food & Nutrition Paper Orchestrator

Coordinate the other skills into one path from idea/data to a submission-ready
manuscript. Original work.

## Stage 0 — Target journal (do this first)
Invoke **`journal-selector`** to resolve the target journal and load its
`Formatting constraints`. If the user named a journal ("publish on Food
Chemistry"), pass it through; otherwise ask once or default to generic
food-science conventions and say so. These constraints govern every later stage.
All figures in later stages go through **`food-figure`** at the journal's spec.

## Stages
| Stage | Skill | Output |
|---|---|---|
| 0 · JOURNAL | `journal-selector` | Journal constraints (structure, limits, reference style, figure spec) |
| 1 · RESEARCH | `food-research` | Evidence brief + gap list |
| 2 · WRITE | `food-paper` | Draft mapped to the journal's structure, references in its style, figures via `food-figure` |
| 3 · REVIEW | `food-review` | Reviewer reports + editor decision + revision checklist |
| 4 · REVISE | `food-paper` (revise) | Revised draft + point-by-point response |
| 5 · FINALIZE | `food-paper` (format-to-journal) | Submission-ready draft + checklist |

## Flow and checkpoints
1. Stage 0 → confirm journal with the user.
2. Stage 1 → present the evidence brief; confirm before writing.
3. Stage 2 → draft; **checkpoint** for author input on framing and data.
4. Stage 3 → review; **mandatory checkpoint** — author decides which concerns to address.
5. Stage 4 → revise against chosen concerns; loop to Stage 3 once more if issues remain (cap at two review rounds).
6. Stage 5 → finalize to the journal's format; produce the submission checklist.

Entry can be mid-pipeline: a dataset starts at Stage 1, a full draft starts at
Stage 2 or 3, reviewer comments start at Stage 4.

## Rules
- Re-flow references and re-check limits whenever the target journal changes.
- Keep food-science reporting standards throughout (n, error type, validated methods, panel details, ethics).
- Never advance past a mandatory checkpoint without author input.
