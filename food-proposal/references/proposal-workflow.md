# Proposal Workflow

How `food-proposal` sequences the specialist skills. Mirrors `food-pipeline`, but every
stage is bound to the target funding scheme's format and length limit.

## Stage 0 — SCHEME (always first)
Resolve the funding scheme before any writing (`scheme-selection.md`). Load its
headings (in order), length limit, font, and assessment criteria. Nothing downstream
starts until the scheme is fixed.

## From scratch (topic/idea only)
1. **RESEARCH** — `food-deep-research` (or `agri-deep-research`; `food-research` for a
   quicker brief) builds the evidence base: the gap, the significance, prior work,
   methods precedent. Full-text-access first move applies.
2. **DRAFT** — `food-paper` writes to the **scheme's headings and per-heading
   questions** (not IMRaD-by-default): e.g. ARC `PROJECT QUALITY AND INNOVATION` answers
   the 5–6 numbered questions; UoM writes Abstract/Intro/Aims/Lit review/Methods/Risks/
   Resources/Timelines. Keep within the length limit as you write.
3. **REVIEW** — `food-review` acts as a **mock funding panel**, assessing against the
   scheme's criteria (and, for ARC, writing for a general assessor). Editorial decision.
4. **REVISE** — `food-paper` (revise) fixes the panel's points and trims to the limit.
5. **FINALIZE** — `food-paper` (format-convert) to the scheme format; export `.docx`/PDF.

## Revising an existing draft
Understand the field first (a `food-research` quick brief, or reuse the user's library),
**then** edit — never rewrite blindly. Map the existing draft onto the scheme's headings,
fill gaps flagged against the assessment criteria, fix grounding, and **fit the length
limit**. Then REVIEW → REVISE → FINALIZE as above.

## Every gate
`compliance_gate` enforces headings + order, **length limit**
(`scripts/proposal_wordcount.py`), font, and criteria coverage before a stage proceeds.

## Inherited
Anti-fabrication grounding + four-gate citations, privacy scan, academic style +
`human-writing.md`, and the **mandatory AI-use disclosure** (some schemes require the
model + prompts — Acknowledgements). Figures via `food-figure`; a pitch deck via
`food-ppt`.
