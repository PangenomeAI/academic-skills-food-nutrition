# Word Review Comments — annotate the manuscript in the margin

When the manuscript is a **Microsoft Word (`.docx`) file (or an equivalent —
LibreOffice `.odt`, Pages, Google Docs)**, `food-review` delivers **two** things:
1. the panel **review report** (as now), and
2. **the manuscript itself with margin comments** inserted using the word
   processor's **Review / Comments** feature — each reviewer concern anchored to
   the exact text it refers to.

## What to annotate
For each concern the panel raised, insert a **margin comment** on the specific
sentence/figure/table/reference it targets. Prefix with the concern's **report
issue ID** (`A5`, `SQ3`, `FC1` — see `report-format.md`) plus the reviewer lens and
severity, so the author can jump between the report and the manuscript:
> **[A5 · Integrity · Critical]** These means do not match Table 2 — reconcile.
> **[C1 · Methodology · Major]** n is not stated for this assay — is it biological (not analytical) replication? Add n and the error type.
> **[D2 · Domain · Minor]** Overreaches beyond the tested matrix; qualify to "in blueberry purée".

Use the **same ID in the comment and the report**. Keep each comment short and
actionable; the full reasoning stays in the report. Comment on the actual location,
not the general area.

## Editor queries — comment on items you suggest but cannot edit (required)
Some concerns recommend a change the reviewer/reviser **cannot make itself** —
because it needs the author's data, a value only they have, or a decision. Do **not**
leave those only in the report. **Insert a comment in the manuscript at the exact
location**, tagged with the issue ID and marked as an **editor query**, mirroring the
report's `Response (Editor query)` line so the author can go straight to the spot:
> **[A1 · Editor query]** Results give BioProject PRJNA1482698 but Data Availability gives a different accession — insert the correct, verified number here.
> **[B1 · Editor query]** Text says 32 mg/kg; Table 1 says 320 mg/kg — which is right?

This is required whenever a report item is classified **Editor query**: every such
item must have a matching comment at its location. If in-manuscript **tracked notes**
are preferred over margin comments, insert a tracked `EDITOR QUERY: …` note at the
location instead — either way it lives where the author needs to act, keyed by the
same ID.

## How to create the comments
- **Preferred:** use the **`docx` skill** (or a Word-capable tool) to add real
  tracked **comments** to the `.docx`. In OOXML this means: a `word/comments.xml`
  part holding each `<w:comment w:id=".." w:author="Reviewer — Methodology"
  w:date=".." w:initials="RM">…</w:comment>`, with the commented span wrapped in
  `<w:commentRangeStart w:id=".."/> … <w:commentRangeEnd w:id=".."/>` plus a
  `<w:commentReference w:id=".."/>` run in `word/document.xml`, and the
  content-type + relationship registered. The `docx` skill handles this plumbing.
- Use a distinct **author name per reviewer lens** (Methodology / Domain /
  Integrity / Devil's advocate / Formatting) so comments are attributable.
- Do **not** alter the manuscript text at this stage — comments only (revision
  happens later in `food-paper`).

## Equivalents
- **LibreOffice `.odt`:** Insert → Comment (same margin-comment model).
- **Google Docs:** insert Comments anchored to selections.
- **Markdown / plain manuscript, or no Word tooling available:** deliver an
  **annotated comments table** instead — `location (section/page/line) | reviewer
  lens | severity | comment` — so the author can place them manually.

## Deliverable
Return the **commented manuscript file** alongside the panel report. State which
tool/format was used. Never fabricate a "commented file" you did not actually
produce — if Word tooling is unavailable, deliver the comments table and say so
(see `food-paper/references/privacy-and-confidentiality.md` before sending any file).
