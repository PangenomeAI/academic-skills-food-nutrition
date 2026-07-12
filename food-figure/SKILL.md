---
name: food-figure
description: "Comprehensive figure system for food & nutrition manuscripts: analyzes the user's data, recommends the best figure(s) to make, then produces submission-grade graphics in Python or R at the target journal's spec. Handles all common scientific figure types (bar/box/violin, line/kinetic, scatter/regression, Bland–Altman, radar/sensory, chromatograms, TPA/rheology, dose–response, survival, PCA/PLS-DA, heatmaps/clustering, forest, microscopy plates, multi-panel). Use to make, create, design, revise, audit, or recommend figures/charts/plots for a food-science paper, or to work out what to plot from a dataset. If Python or R isn't chosen, ask once and remember it. Triggers: make a figure, create a figure, design a figure, what figure should I make, recommend a chart, plot my data, analyze my data and plot it, chart my results, food science figure, journal figure, scientific plotting, data visualization for a manuscript."
metadata:
  version: "2.0.0"
  verified: "2026-07"
  related_skills: [journal-selector, food-paper, food-research]
  references:
    - references/chart-types.md
    - references/data-to-figure.md
    - references/design-principles.md
    - references/figure-contract.md
    - references/qa-checklist.md
    - references/python-guide.md
    - references/r-guide.md
    - references/food-recipes.md
    - references/journal-specs.md
  scripts:
    - scripts/analyze_data.py
    - scripts/backend_pref.py
---

# Food-Figure — Data-Driven Figure System for Food & Nutrition Science

Turn a dataset (or a described result) into the right submission-grade figure.
**The chart serves the scientific logic; polish is subordinate to making the
core conclusion clear, defensible, and reviewable.** Original work; architecture
informed by open community figure skills (see the repo README Acknowledgements).

Load reference files **as needed** (progressive disclosure) — don't read them all
up front. The map is in the frontmatter `references` list.

## Workflow

```mermaid
flowchart TD
    A[Data or described result] --> B[1. Analyze the data<br/>scripts/analyze_data.py -> profile]
    B --> C[2. Recommend figures<br/>references/data-to-figure.md]
    C --> D[3. Figure contract<br/>references/figure-contract.md]
    D --> E{Backend?}
    E -- unknown --> Eq[Ask 'Python or R?' once<br/>scripts/backend_pref.py]
    E -- known --> F
    Eq --> F[4. Render<br/>python-guide.md OR r-guide.md + food-recipes.md]
    F --> G[5. Export at journal spec<br/>references/journal-specs.md]
    G --> H[6. QA<br/>references/qa-checklist.md]
    H --> OUT[Journal-ready SVG/PDF/TIFF + editable source]
```

### 1 — Analyze the data
If the user supplies a data file (CSV/TSV/Excel) or table, profile it first:
run `scripts/analyze_data.py <file>` to get, per column, the type
(numeric/categorical/datetime), cardinality, missingness, distribution summary,
and the detected structure (grouping factors, repeated measures, time/dose axis,
wide sensory/composition matrix). If the user only describes a result, elicit the
same: what varies, what's measured, n, and the error type. See
`references/data-to-figure.md`.

### 2 — Recommend the figure(s)
From the profile, propose the **best** figure type(s) with a one-line rationale
each, and say what each would show. Prefer the figure that makes the paper's
claim most directly; note honest alternatives. The decision rules and a full
catalog are in `references/data-to-figure.md` and `references/chart-types.md`.
Never force a chart the data can't support (e.g. bar-of-means where a
distribution matters → box/violin + points).

### 3 — Figure contract (before code)
Fix the conclusion, evidence logic, export needs (target journal), and review
risks. See `references/figure-contract.md`.

### 4 — Backend gate (blocking)
Resolve **Python or R** by priority: explicit request → language of the user's
input files/data → saved preference (`python scripts/backend_pref.py get`) → ask
once ("Python or R? I'll remember this") and save it
(`backend_pref.py set python|r`). The chosen backend does **all** graphics,
preview, and export; the other may only help with data prep/conversion. Backend
guidance: `references/backend-selection` note in `python-guide.md` / `r-guide.md`.

### 5 — Render & export
Use the selected backend's guide (`python-guide.md` = matplotlib/seaborn;
`r-guide.md` = ggplot2/patchwork/ComplexHeatmap) plus `food-recipes.md` for the
food/nutrition figure types. Export **vector** (PDF/SVG) for line/bar/scatter and
**TIFF (LZW)** at the journal DPI for raster/microscopy; keep an editable source.
Pull DPI, column width, font, and format from the target journal via
`references/journal-specs.md` (which reads the journal skill's constraints); if
no journal is set, default to 300 dpi, ~90/190 mm widths, TIFF+PDF, Arial 7–9 pt.

### 6 — QA
Run `references/qa-checklist.md` before delivering (error bars defined + n;
statistics shown consistently; axes honest; colorblind-safe; labels legible at
final size; matches journal spec; every panel cited).

## Modes
- **recommend** — analyze data and suggest figures, no rendering yet.
- **make** (default) — full pipeline to a rendered, exported figure.
- **revise / audit** — critique or fix an existing figure against the QA checklist and journal spec.
- **multi-panel** — compose labelled panels (a, b, c) that share a logical thread.

## Scope
Reproducible, code-generated, submission-grade scientific figures for food &
nutrition. Not for dashboards, slide infographics, or Illustrator/Figma-first
artwork. For a schematic/graphical abstract (mechanism diagram), say so — that is
a drawing task, handled separately from data plotting.

## Handoff
Called by `food-paper`'s `viz_designer` at the journal spec; figures feed the
manuscript's Results.
