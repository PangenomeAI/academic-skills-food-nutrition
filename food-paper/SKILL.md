---
name: food-paper
description: "Write, structure, or revise a food & nutrition science manuscript, journal-aware. Use when the user wants to draft, outline, revise, or format a food-science paper, an abstract, a section (introduction/methods/results/discussion), or convert a draft to a target journal's style. Always resolves the target journal first (via journal-selector) and routes figures through food-figure. Triggers: write my paper, draft a manuscript, food science paper, outline my paper, revise my manuscript, format for a journal, publish on <journal>, prepare my paper for <journal>, edit the manuscript based on <journal> style, write the abstract, write the introduction/methods/results/discussion."
metadata:
  version: "1.0.0"
  verified: "2026-07"
  related_skills: [journal-selector, food-figure, food-research, food-review]
---

# Food-Paper — Journal-Aware Manuscript Writing for Food & Nutrition Science

Draft and shape food & nutrition manuscripts so they read like the target
journal expects. This skill is original work; it uses no third-party manuscript
text.

## First move — always resolve the target journal
Before drafting or restructuring, invoke the **`journal-selector`** skill to get
the target journal's `Formatting constraints` (structure, word/abstract limits,
reference style, figure spec). If the user names a journal anywhere in the
request ("publish on Food Chemistry", "Food Chemistry style"), pass it straight
through. If no journal is set, ask once, or proceed with generic food-science
conventions and state the assumption. **Route every figure request to the
`food-figure` skill**, passing the journal's `figure_dpi` / column widths.

## Modes
- **outline** — section-by-section skeleton mapped to the journal's structure + an evidence map (claim → data → citation).
- **full** — complete draft from the author's data/notes/outline.
- **section** — draft or rewrite one section (abstract, introduction, methods, results, discussion, conclusion).
- **revise** — revise against reviewer comments (pairs with `food-review`).
- **format-to-journal** — convert an existing draft to the target journal's structure, limits, and reference style.

## Manuscript structure (IMRaD default; override with the journal skill)
1. **Title & abstract** — abstract to the journal's limit and style (structured vs unstructured — e.g. British Food Journal requires a structured abstract). Keywords per journal count.
2. **Introduction** — knowledge gap → objective; end with a crisp aim/hypothesis.
3. **Materials and methods** — reproducible detail: sample source (cultivar/breed/batch), preparation, storage; instruments and settings; assay conditions (HPLC/GC/LC-MS columns, mobile phase, detector; antioxidant assays with the reference standard, e.g. Trolox equivalents); microbiological media and incubation; experimental design, replication (n), and the full statistical model.
4. **Results** — report with food-science conventions: proximate composition as g/100 g (state wet/dry basis) with AOAC method; microbial counts as log CFU/g with detection limit; texture (TPA parameters) and rheology with settings; mean ± SD/SEM with n; significance shown consistently (letters from post-hoc, or asterisks with the test named).
5. **Discussion** — interpret against mechanism and literature; avoid overclaiming beyond the data; note limitations (single batch, panel size, matrix effects).
6. **Conclusion** — what changed in understanding, and the practical/food-system implication.
7. **Declarations** — competing interests, funding, author contributions (CRediT), data availability, and ethics (human sensory panels, animal tissue, or pathogen work).

## References — match the journal's style exactly
Apply the `reference_style` from the resolved journal skill. Common food-journal styles this suite supports:
- **numbered-vancouver** (e.g. Food Chemistry, most Elsevier): in-text `[1]`, list by order of appearance.
- **author-date** (Harvard/APA variants; many Wiley, T&F, Springer, ADSA): in-text `(Author & Author, 2023)`, alphabetical.
- **nature-superscript-numbered** (Nature Food/npj): superscript numbers; article titles required.
- **acs-numbered** (JAFC); **rsc-superscript-numbered** (Food & Function); **numbered-mdpi** (Foods/Antioxidants/Toxins); **harvard-emerald** (British Food Journal).

When switching journals, **re-flow the entire reference list and in-text markers** to the new style — do not leave mixed styles. Keep DOIs.

## Food-science reporting defaults (enforce unless told otherwise)
Units in SI; report n and error type on every mean; name every statistical test and threshold; disclose panel type and size for sensory work; validated methods (LOD/LOQ, recovery) for analytical claims; identification by standards or MS/MS, not library hits alone.

## Figures & tables
All figures via **`food-figure`** at the journal's spec. Tables editable (never images). Cite every display item in order; keep within the journal's display-item limit.

## Output
Markdown by default; on request, provide conversion notes to DOCX (Pandoc) or LaTeX. Always provide the abstract and keywords, and a submission checklist drawn from the journal skill.

## Handoffs
`food-research` (evidence in) → **food-paper** → `food-review` (critique) → **food-paper** (revise). Orchestrated by `food-pipeline`.
