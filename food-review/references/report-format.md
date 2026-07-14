# Review & Editing Report — format

Canonical structure for the combined **review report + revision log** delivered by
`food-review` (the panel report), `food-paper` (revise mode: the revision log), and
`food-pipeline` (the one combined report across rounds). One English document,
grounded — never invent an issue, a location, or a fix.

## Conventions
- **Colour legend:** reviewer feedback/concerns in **black**; the response / action
  taken in **blue**. State it near the top: *"Feedback in black · responses /
  actions taken in blue."*
- **Stable issue IDs** so every concern is traceable across the report, the
  manuscript comments, and the response letter. Group by category, number within:
  - Part A editing report: `A#` critical / data-integrity, `B#` numerical &
    internal consistency, `C#` statistics & methods reporting, `D#` editorial &
    typographic.
  - Part B scientific-quality: `SQ#`; second-round additions: `R2-a`, `R2-b`, …
  - Part C figure/table consistency: `FC#`.
- **Precise location** in every concern *and* every response: Section, paragraph or
  line (`P##`), `Table n`, `Figure n` (caption). Never "somewhere in Results".

## Response taxonomy (tag every item)
Each concern is immediately followed by a **`Response (<type>):`** line. Types:
- **Tracked edit** — the fix was applied to the manuscript as a tracked change;
  name what changed and where (`P##`).
- **Editor query** — the fix needs the author's data or decision, so it could not
  be edited. A **comment (or tracked "EDITOR QUERY" note) is inserted in the
  manuscript at that location**, carrying the same issue ID, and the author must
  resolve it. → see `word-review-comments.md`.
- **Recommendation** — an author-side action with no manuscript edit (e.g. complete
  a reference, run an extra analysis).
- **Residual** — author-dependent and **cannot be closed by editing** (needs new
  data / analysis / experiment). Carried to the residual-items list.

In a *review-only* run (`food-review` before any revision) responses are
**Recommendation** or **Editor query**; **Tracked edit** and **Residual** appear
once revision has run.

## Document structure
1. **Header** — title *"Review and Editing Report"*; `Manuscript: <title>`;
   `Target journal: <journal> · Editorial decision: <Accept/Minor/Major/Reject> ·
   Prepared: <date>`; the colour legend; one sentence noting the report accompanies
   the tracked-changes manuscript (+ tables / figures / supplementary).
2. **Overall assessment** — short narrative: what the study does well and the
   headline concerns.
3. **Part A — Editing report (by category).** Numbered issues `A#/B#/C#/D#`. Each:
   the concern (black, with location), then `Response (<type>): <action + location>`
   (blue).
4. **Summary of changes applied** — one paragraph naming which IDs got tracked
   edits, which got editor queries, and which are recommendations / residual.
5. **Part B — Scientific-quality review & revision log.**
   - **Editorial decision** — `Recommendation: <decision>` + rationale.
   - **Scientific-quality comments** — `SQ#` items, each concern + `Response (<type>)`.
   - **Round 2 (re-review) additions** — `R2-*` items (only if a second round ran).
   - **Loop status & residual (author-dependent) items** — an honest convergence
     statement (how many rounds ran; that all text-resolvable items are done) and a
     **bulleted list** of the residual items the author must resolve.
6. **Part C — Figure/Table consistency audit & revision log** (when figures/tables
   were checked). `FC#` items: each headline claim vs the figure/table, +
   `Response (<type>)`.

## Scope adaptation
- **Review-only (`food-review`, no revision yet):** keep the header, overall
  assessment, Part A/B/C concern lists, and the editorial decision, but responses
  are the **recommended fix** or an **Editor query** placed in the manuscript — no
  "Tracked edit" responses yet. Drop Part C if no figures/tables were audited.
- **Revision run (`food-paper` revise / `food-pipeline`):** responses record what
  was actually done (Tracked edit / Editor query / Recommendation / Residual). One
  combined report across authorized rounds — label which round each point came from.
- Every location, number, and fix must be real — never invent an issue, a paragraph
  number, or an edit you did not make (`food-paper/references/faithfulness-and-citation.md`).
  Run `scripts/privacy_scan.py` on the file before delivery
  (`food-paper/references/privacy-and-confidentiality.md`).

## Cross-references
- `word-review-comments.md` — placing **Editor query** / reviewer comments in the
  manuscript, tagged with these IDs.
- `food-paper/references/revision-response.md` — tracked-changes mechanics and the
  point-by-point response letter, which reuse these IDs.
