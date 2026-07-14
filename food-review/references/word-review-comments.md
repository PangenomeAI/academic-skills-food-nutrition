# Word Review Comments — annotate the manuscript in the margin

When the manuscript is a **Microsoft Word (`.docx`) file (or an equivalent —
LibreOffice `.odt`, Pages, Google Docs)**, `food-review` delivers **two** things:
1. the panel **review report** (as now), and
2. **the manuscript itself with margin comments** inserted using the word
   processor's **Review / Comments** feature — each reviewer concern anchored to
   the exact text it refers to.

## What to annotate
For each concern the panel raised, insert a **margin comment** on the specific
sentence/figure/table/reference it targets. Prefix with the reviewer lens and
severity so the author can triage, e.g.:
> **[Methodology · Major]** n is not stated for this assay — is it biological (not analytical) replication? Add n and the error type.
> **[Domain · Minor]** Overreaches beyond the tested matrix; qualify to "in blueberry purée".
> **[Integrity · Critical]** These means do not match Table 2 — reconcile.

Keep each comment short and actionable; the full reasoning stays in the report.
Comment on the actual location, not the general area.

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
