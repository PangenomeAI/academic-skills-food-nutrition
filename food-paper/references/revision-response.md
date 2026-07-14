# Revision with Tracked Changes + Point-by-Point Response Letter

When revising a manuscript against an **existing review** — a `food-review` panel
report and/or **margin comments** on a Word file — `food-paper` (revise mode)
produces two Word deliverables:
1. the **original manuscript revised with Tracked Changes**, and
2. a **point-by-point response letter** as a **new Word (`.docx`) document**.

The **revision log / combined report** follows
`food-review/references/report-format.md`: stable issue IDs (`A#/B#/C#/D#`, `SQ#`,
`R2-*`, `FC#`), each concern paired with a `Response (<type>)` line where type ∈
**Tracked edit · Editor query · Recommendation · Residual**, precise locations
(`P##` / Table / Figure), overall assessment, editorial decision, summary of
changes, and a residual-items list. Reuse the same IDs in the manuscript comments
and the response letter so the three cross-reference.

## 1. Revise with Tracked Changes (original file is opt-in)
- **Standalone `food-paper` revise** (user asked to revise this file): edit **the
  original `.docx`** with Tracked Changes so the editor can accept/reject each
  change — unless the user asks for a separate revised copy.
- **Inside `food-pipeline`:** do **not** modify the original Word file unless the
  author has **explicitly authorized** in-place tracked changes. Default: leave
  the original untouched; deliver a **revised copy** (or change log / marked
  draft) plus the response letter.
- When editing in place is authorized: make every edit as a **tracked change**.
  In OOXML: insertions are
  `<w:ins w:id=".." w:author=".." w:date="..">…</w:ins>` and deletions
  `<w:del …><w:r><w:delText>…</w:delText></w:r></w:del>`; enabling
  `<w:trackChanges/>` in `word/settings.xml` keeps further edits marked. Use the
  **`docx` skill** (or a Word-capable tool) to apply these — it handles the plumbing.
- **Resolve the margin comments** as you address them (or leave a reply noting the
  change), so each reviewer comment maps to a visible edit.
- **Items you cannot edit** (need the author's data/decision) are classified
  **Editor query**: instead of a silent recommendation, insert a comment or tracked
  `EDITOR QUERY` note **in the manuscript at that location**, tagged with the issue
  ID, so the author sees exactly where to act (see
  `food-review/references/word-review-comments.md`).
- Keep the project's grounding rule: every new claim/number/citation is real and
  verified (`faithfulness-and-citation.md`); run `scripts/verify_citations.py` and
  `scripts/privacy_scan.py` before delivering.

## 2. Point-by-point response letter (new .docx)
A new document, addressed to the editor/reviewers, with one numbered block per
concern:

```
Reviewer <n>, Comment <n.m>:
> "<the reviewer's comment, quoted verbatim>"

Response:
<how you addressed it — what changed and why; or a courteous, evidenced rebuttal
if you disagree, citing sources>.

Change: <what was edited and where — Section/Page/Line, e.g. "Methods §2.3, p.4,
lines 112–118">. [Optionally quote the revised text.]
```
- Cover **every** comment (major and minor); never silently skip one.
- Group by reviewer; open with a brief thank-you + summary of key changes.
- Where you disagree, say so respectfully with evidence — do not overstate.

## Equivalents & fallback
- **LibreOffice `.odt` / Pages / Google Docs:** use that tool's track-changes /
  suggesting mode; the response letter is a new document in the same format.
- **Markdown / no Word tooling:** deliver the revised manuscript with changes
  marked (e.g. a diff or change log) and the response letter as markdown, and say
  which format was used — never claim a tracked-changes `.docx` you did not produce.

## Combined vs per-round
When run standalone (one review round), produce one revised manuscript + one
response letter. Inside `food-pipeline`, the **default is one** review→revise
round (a second round needs author authorization). Only when the author has
authorized **both** a second round **and** in-place edits on the original file
does the manuscript accumulate all tracked changes in that **one** original, with
a **single combined response letter** covering both rounds — see the pipeline's
rules.
