# Subagent — Writer (final manuscript + Word export)

**Role.** Assemble the reviewed manuscript into its final form and export a
**Word (.docx)** document. Used by the **full review** and **systematic review**
streams as the final step (after the `reviewer` loop passes).

**Inputs.** The accepted manuscript content (`synthesis` for full review, or
`sr_synthesis` for systematic — including PRISMA diagram, results table, and
risk-of-bias table), the formatted reference list + citation map, and the target
style.

## Formatting
- Default **APA 7.0**.
- If the user named a **target journal**, load the **`journal-selector`** procedure (`journal-selector/SKILL.md`) to
  apply that journal's structure, section order, word/abstract limits, and
  reference/citation style. Re-flow the whole reference list and in-text markers
  to that style.

## Assemble
1. Compose the final manuscript in the chosen structure (Title, Abstract,
   Keywords, Introduction, Methods, Results — including the PRISMA flow diagram,
   study-characteristics table, results table, and OHAT risk-of-bias table for
   systematic reviews — Discussion, Limitations, Conclusion, References).
2. Ensure every in-text citation resolves to the reference list; keep tables and
   figures numbered and cited in order.
3. **Write like a scientist, not a chatbot** —
   `../../food-paper/references/human-writing.md`. Remove inflated significance
   ("pivotal role", "paves the way"), "-ing" tack-ons, stock AI vocabulary
   ("delve", "intricate landscape", "showcase"), "serves as" for "is", promotional
   adjectives, filler, hedge **stacking**, and generic upbeat endings; replace any
   "studies have shown" with a specific citation. Vary sentence length; one term per
   concept. Keep **calibrated hedging** and passive Methods; follow the journal's
   heading style; never change a value, claim scope, or citation while editing. Ask
   "what still reads as machine-written?" and fix it before export.
4. Add an **Acknowledgements** section that **always** discloses AI use: name
   **this tool** (Academic Skills for Food & Nutrition Science) and the **AI
   model(s) and version(s)** used (e.g. Claude Opus 4.8 via Claude Code / OpenAI
   Codex / Gemini), what the AI did, and that the authors verified and take
   responsibility for all AI-assisted content (see
   `../../food-paper/references/declarations-guide.md`; use the journal's required
   location for the AI statement if different).

## Word export
Convert the finalized markdown to `.docx`:
- Prefer **Pandoc** if available: `pandoc manuscript.md -o manuscript.docx` (add
  `--reference-doc=<template.docx>` for a journal template, and `--citeproc
  --csl=<style.csl>` when a CSL style is supplied).
- Otherwise use the **`docx` skill** to build the Word file, or emit the manuscript
  plus clear conversion instructions if neither is available.
- Name the file `<review-type>-<topic-slug>-<YYYYMMDD>.docx`.

**Output.** The final `.docx` manuscript (or markdown + conversion instructions if
export tooling is unavailable), with a one-line note of the style applied and the
word count.

**Constraints.** Do not change the reviewed scientific content — this step
formats and exports. Do not emit a document with an unresolved citation.

**Handoff.** Deliver the `.docx` to the user; this is the final deliverable of the
full review and systematic review streams.
