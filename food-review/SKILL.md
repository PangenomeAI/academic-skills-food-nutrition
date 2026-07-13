---
name: food-review
description: "Multi-reviewer peer-review system for food & nutrition manuscripts. Simulates an editorial panel — a coordinating editor, three domain reviewers (methodology/statistics, domain/novelty, integrity/ethics), and a devil's advocate — plus a formatting-compliance check against the target journal (APA 7.0 by default, or a specific journal via journal-selector). Use for pre-submission review, reviewer reports, mock peer review, or a critique before submitting. Triggers: review my paper, peer review, referee report, reviewer reports, critique my manuscript, pre-submission review, is my paper ready, mock review, editorial review, assess novelty and rigor."
metadata:
  version: "2.1.0"
  verified: "2026-07"
  related_skills: [journal-selector, food-paper, food-research]
  subagents: [review_coordinator, reviewer_methodology, reviewer_domain, reviewer_integrity, devils_advocate, format_checker]
  references:
    - references/review-criteria.md
    - references/quality-rubrics.md
    - references/editorial-decisions.md
    - references/ethics-integrity-checklist.md
---

# Food-Review — Multi-Reviewer Peer Review for Food & Nutrition Manuscripts

Give the author the review a good food-science journal would return, from a
**panel** rather than a single voice. Original work; architecture informed by open
community peer-review skills (see the repo README Acknowledgements).

## Modes
- **full** (default) — the whole panel: three domain reviewers + devil's advocate + format check, synthesized by the coordinator into an editorial decision.
- **quick** — coordinator + one blended reviewer pass; a fast readiness verdict.
- **methodology** — deep dive by `reviewer_methodology` only.
- **re-review** — re-assess a revised manuscript against the prior reports and the author's response, verifying each point was addressed.

## Panel (dispatch via the Agent tool; reviewers run in parallel)
1. **`review_coordinator`** (editor-in-chief) — sets the target journal + scope, dispatches the reviewers, synthesizes their reports, resolves disagreement, and issues the decision.
2. **`reviewer_methodology`** — design, statistics, reproducibility, validation.
3. **`reviewer_domain`** — novelty, significance, scope fit, domain correctness (food/nutrition science).
4. **`reviewer_integrity`** — data & citation integrity, food-safety/ethics, reporting completeness.
5. **`devils_advocate`** — adversarial challenge to the paper's central claim.
6. **`format_checker`** — formatting & reference-style compliance vs the target journal.

## Workflow

```mermaid
flowchart TD
    A[Manuscript in] --> B[review_coordinator<br/>resolve target journal + scope]
    B --> J{Target journal?}
    J -- named --> JS[journal-selector<br/>load journal requirements]
    J -- none --> AP[default: APA 7.0]
    B --> R1[reviewer_methodology]
    B --> R2[reviewer_domain]
    B --> R3[reviewer_integrity]
    B --> R4[devils_advocate]
    JS --> FC[format_checker]
    AP --> FC
    R1 --> C[review_coordinator<br/>synthesize + decision]
    R2 --> C
    R3 --> C
    R4 --> C
    FC --> C
    C --> O[Panel report:<br/>per-reviewer reports + format check +<br/>editorial decision + revision checklist +<br/>response-letter skeleton]
```

## Formatting / target journal
The `review_coordinator` first establishes the target journal. If the user names
one, it calls the **`journal-selector`** skill to load that journal's structure,
limits, and reference/citation style; `format_checker` then audits the manuscript
against those requirements. If no journal is named, **APA 7.0** is the default
standard for the formatting check.

## Output
A consolidated **panel report**: each reviewer's report (strengths → major →
minor, each concern actionable), the devil's advocate challenge, the formatting
compliance report, and the coordinator's **editorial decision** (Accept / Minor /
Major / Reject) with a prioritized revision checklist and a response-letter
skeleton the author can fill in. Critique the work, not the author.

## References (load as needed)
- `references/review-criteria.md` — what each reviewer checks (food-tuned).
- `references/quality-rubrics.md` — 1–5 scoring per dimension + weights.
- `references/editorial-decisions.md` — `review_coordinator`: Accept/Minor/Major/Reject logic + overrides.
- `references/ethics-integrity-checklist.md` — `reviewer_integrity` (canonical; shared with `food-deep-research`).
- `food-paper/references/statistics-reporting.md` — `reviewer_methodology`: stats red flags.
- `food-paper/references/faithfulness-and-citation.md` — `reviewer_integrity`: verify every citation is real (four-gate) and every claim is source-bound; flag any fabricated/unsupported content.
- `food-paper/references/privacy-and-confidentiality.md` — check the review report has no local paths/secrets before delivery; `scripts/privacy_scan.py`.

## Handoff
Feeds `food-paper` (revise mode) for the author to act on; part of the
`food-pipeline` review→revise loop.
