# AI Image Generation — schematics & graphical abstracts (opt-in)

**Default is always Python or R.** Use an AI image model **only when the user
explicitly asks** to generate the image with **Gemini, ChatGPT, or Claude** (or
another named image model) instead of code.

## When it is allowed
Only for **conceptual/qualitative visuals**:
- Mechanism diagrams (e.g. a food-process or reaction pathway, encapsulation
  release, gut-microbiome interaction)
- Graphical abstracts / concept art
- Workflow or process pipelines
- Before/after or split-panel schematic illustrations

## When it is NOT allowed
**Never** use an AI image model for **any data-bearing figure** — bar/line/scatter
plots, heatmaps, chromatograms, microscopy, dose–response, forest plots, PCA, etc.
Those are quantitative evidence and **must** be produced in Python or R from the
real data. This preserves scientific integrity and reproducibility.

## Non-negotiable rules
- **No fabricated data or values.** The image must not contain invented numbers,
  axes with values, p-values, error bars, sample sizes, or made-up mechanisms.
- **No fabricated logos, journal marks, or institutional branding.**
- **Draft concept, not evidence.** Treat the output as a visual draft; the
  underlying science must be established and cited elsewhere in the manuscript.
- **Legibility is limited** — AI images often render text poorly. Re-label the
  final figure in a vector editor (Inkscape/Illustrator) or overlay text in
  Python/R before submission.
- **Disclose** AI image generation per the venue's policy (see
  `food-paper/references/declarations-guide.md`), and check the journal permits
  AI-generated figures — many restrict them.

## Workflow (when opted-in)
1. **Define the concept** from the manuscript: the central idea, the key entities,
   the cause→effect logic, and the layout (left-to-right / circular / split).
2. **Write a tight prompt:** "clean scientific mechanism schematic, minimal text,
   flat vector style, labelled boxes and arrows, white background, no fabricated
   data or numbers, [entities], [relationships], [layout]."
3. **Generate** with the model the user requested (Gemini / ChatGPT / Claude image
   generation), using that tool's own image interface. Prefer a high resolution
   and the aspect ratio the journal wants (e.g. graphical-abstract box).
4. **Review & finalize:** check for fabricated content and mislabelling; fix text
   in a vector editor; confirm it matches the manuscript's claims.

If the user has not asked for AI image generation, do not use it — return to the
Python/R backend gate.
