# Mode Advisor — route the project

`intake_router` uses this to pick the entry stage, the research flavor, and which
skills to run.

## Entry stage (from what the user has)
| The user brings… | Start at |
|---|---|
| A topic / question only | RESEARCH |
| A dataset / results | WRITE (analysis happens inside `food-paper`) |
| A full draft | WRITE (finish) or REVIEW |
| Reviewer comments + draft | REVISE |
| A literature question, no manuscript planned | `food-research` or `food-deep-research` standalone (skip the write path) |

## Research flavor
| Goal | Use |
|---|---|
| Fast orientation | `food-research` **quick brief** |
| Narrative review manuscript | `food-research` **full review** |
| Reproducible, auditable review / meta-analysis (protocol, dual screening, PRISMA, OHAT) | `food-research` **systematic** |
| Open-ended, source-validated deep dive or a standalone literature-review article | `food-deep-research` |
| Just the paper's evidence base (feeds writing) | `food-research` full review, then `food-paper` |

## Output target
- Original research paper → `food-paper` (full).
- Literature/systematic review → `food-research` (systematic) or `food-deep-research`.
- Figures → always via `food-figure` at the journal spec.
- Peer-review feedback → `food-review`.

## Journal
Resolve the target journal at ROUTE via `journal-selector`; if undecided, proceed
with APA 7.0 defaults and revisit before FINALIZE.
