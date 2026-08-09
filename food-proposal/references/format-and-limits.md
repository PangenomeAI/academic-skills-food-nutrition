# Format & Length Limits

Every scheme carries a **length limit** — treat it as hard. Enforce with
`python3 scripts/proposal_wordcount.py <draft>.md --scheme <id>`.

## Words vs pages
- **Word limit** (e.g. UoM: 1500 ± 150): the checker counts words. Some schemes count
  **only certain sections** — UoM counts Abstract, Introduction, Aims & Objectives,
  Literature Review, and in-text citations; **not** cover sheet, TOC, tables/figures,
  methods, acknowledgements, references, risks, resources, timeline, or appendix. The
  checker applies the scheme's `counted_sections`.
- **Page limit** (e.g. ARC: 2 pages EOI, 7 pages Full): true pages depend on the
  template's font, margins, and figures, which a word counter can't see exactly. The
  checker gives a **word-based estimate** (~650 words/A4 page) as an early-warning proxy
  — always **confirm the real page count in the scheme's own template** before
  submitting. ARC counts **text inside figures and tables** too.

## Formatting
Apply the scheme's font/spacing (e.g. UoM 11 pt / 1.5 spacing; ARC per §2.4, references
may be 10 pt). Use sub-headings and bold key phrases where the scheme encourages it
(ARC: "formatting is your friend"). Match the scheme's heading wording exactly.

## Over / under limit
Over the limit **blocks** `compliance_gate` — trim (tighten prose via
`human-writing.md`, move detail to non-counted sections where allowed, cut
low-value content) rather than shrinking the font below the scheme's minimum.
Well under a word target usually means an under-developed case — expand the argument,
not padding.
