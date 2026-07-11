---
name: food-figure
description: "Submission-grade figure workflow for food & nutrition manuscripts in Python or R. Use whenever the user asks to make, create, design, revise, audit, or polish a figure, chart, or plot, multi-panel scientific plots, or journal-ready SVG/PDF/TIFF outputs for a food-science paper. Before plotting, define the figure's conclusion, evidence logic, export needs, and review risks. If the user has not chosen Python or R, ask 'Python or R?' and stop; use only the selected backend. Supports matplotlib/seaborn and ggplot2/patchwork. Covers food-specific plots: grouped bars with error bars + significance letters, sensory radar, microbial growth/survival curves, chromatograms, texture profile analysis, rheology, PCA/heatmaps, microscopy panels. Triggers: make a figure, create a figure, design a figure, help me design a figure, plot my data, chart my results, food science figure, journal figure, scientific plotting, data visualization for a manuscript."
metadata:
  version: "1.0.0"
  verified: "2026-07"
---

# Food-Figure — Submission-Grade Figures for Food & Nutrition Manuscripts

**The chart serves the scientific logic; aesthetic polish is subordinate to
making the core conclusion clear, defensible, and reviewable.**

## Workflow (follow in order)

### Step 1 — Figure contract (before any code)
State, in one or two lines each:
1. **Conclusion** — the single claim this figure must let a reader reach
   (e.g. "coating cut weight loss vs control across 14 days").
2. **Evidence logic** — which comparison/trend carries that claim, and the
   controls that make it defensible (replicates n, error type, statistics).
3. **Export needs** — target journal + its figure spec (DPI, column width,
   file format, fonts). If a target journal is set, pull this from the matching
   `journals/<name>` skill's `## Formatting constraints` (`figure_dpi`,
   `column_widths_mm`). If unset, default to 300 dpi, ~90/190 mm widths, TIFF+PDF.
4. **Review risks** — what a reviewer will attack (missing error bars, pseudo-
   replication, truncated axes, undisclosed n, jet colormaps, unreadable labels).

Do not proceed to code until the contract is explicit. If the data isn't
described well enough to fill it, ask.

### Step 2 — Backend gate (blocking)
- Honor an explicit **Python** or **R** choice, or a language-specific input
  file (`.py`/`.ipynb` → Python; `.R`/`.Rmd` → R).
- Otherwise ask exactly once: **"Python or R?"** and stop. Use only the
  selected backend for plotting, preview, export, and QA.

### Step 3 — Build to the contract
Use the backend recipes below. One figure = one clear message; multi-panel only
when panels share a logical thread (label panels **a, b, c**, lower-case, bold).

### Step 4 — Export
- **Vector** (PDF/SVG/EPS) for line/bar/scatter; **TIFF** (LZW) at the journal's
  DPI for raster/microscopy. Always keep an editable source (`.svg`/`.pdf`).
- Embed fonts; sans-serif (Arial/Helvetica), ~7–9 pt at final size.
- Size to the journal column width; never rely on the reader to rescale.

### Step 5 — QA checklist (self-review before delivery)
- [ ] Error bars defined (SD/SEM/CI stated) and n disclosed
- [ ] Statistics shown consistently (letters or asterisks; test named in legend)
- [ ] Axes start where they should; no misleading truncation; units on every axis
- [ ] Colorblind-safe palette (avoid red/green pairing; avoid `jet`)
- [ ] Labels legible at final print size; no overlap
- [ ] Matches the target journal's DPI / width / format
- [ ] Every panel cited in the text and the legend states what each shows

## Food & nutrition figure recipes

| Figure type | When | Key rules |
|---|---|---|
| Grouped bar + error bars + significance letters | treatments × response (composition, texture, antioxidant activity) | letters (a,b,c) from post-hoc (Tukey); state n and error type |
| Line/kinetic curve | storage/shelf-life, microbial growth/survival, drying | log CFU/g for microbes; model fit (Weibull/Gompertz) overlaid if used |
| Sensory radar/spider | trained-panel or consumer attribute profiles | scale 0–max marked; overlay treatments; report panel size |
| Chromatogram (HPLC/GC) | separation/identification | label peaks with compound IDs; retention time axis; keep baseline |
| Texture Profile Analysis | hardness/springiness/chewiness | show force–time trace or grouped bars; note probe/settings in legend |
| Rheology | flow/oscillatory behavior | log axes where appropriate; mark model region; label G′/G″ |
| PCA / heatmap | metabolomics, volatile/sensory clustering | show variance explained; scale/normalize; dendrogram if clustered |
| Boxplot/violin + points | distributions across groups | overlay raw points; show n; avoid bar-of-means for distributions |
| Microscopy panel | structure (SEM/CLSM/light) | scale bar on every panel; consistent magnification; state stain/mode |

## Python backend (matplotlib / seaborn)
```python
import matplotlib as mpl, matplotlib.pyplot as plt
mpl.rcParams.update({
    "figure.dpi": 300, "savefig.dpi": 300,
    "font.family": "Arial", "font.size": 8,
    "axes.linewidth": 0.8, "svg.fonttype": "none",
    "pdf.fonttype": 42, "ps.fonttype": 42,           # editable text in vector output
})
# grouped bar + error bars + significance letters
fig, ax = plt.subplots(figsize=(3.5, 2.6))          # ~90 mm single column
ax.bar(x, means, yerr=sds, capsize=3, color=palette) # palette = colorblind-safe
for xi, mi, si, letter in zip(x, means, sds, letters):
    ax.text(xi, mi + si + pad, letter, ha="center", va="bottom")
ax.set_ylabel("Firmness (N)"); ax.set_xticks(x); ax.set_xticklabels(groups)
fig.tight_layout()
fig.savefig("fig1.pdf"); fig.savefig("fig1.tiff", dpi=300, pil_kwargs={"compression": "tiff_lzw"})
```
Colorblind-safe palette (Okabe–Ito): `['#000000','#E69F00','#56B4E9','#009E73','#F0E442','#0072B2','#D55E00','#CC79A7']`.

## R backend (ggplot2 / patchwork)
```r
library(ggplot2); library(patchwork)
okabe <- c("#000000","#E69F00","#56B4E9","#009E73","#F0E442","#0072B2","#D55E00","#CC79A7")
p <- ggplot(df, aes(group, mean, fill = group)) +
  geom_col(width = .7) +
  geom_errorbar(aes(ymin = mean - sd, ymax = mean + sd), width = .2) +
  geom_text(aes(y = mean + sd, label = letter), vjust = -0.4) +
  scale_fill_manual(values = okabe) +
  labs(y = "Firmness (N)", x = NULL) +
  theme_classic(base_size = 8, base_family = "Arial") +
  theme(legend.position = "none")
ggsave("fig1.pdf", p, width = 90, height = 66, units = "mm")
ggsave("fig1.tiff", p, width = 90, height = 66, units = "mm", dpi = 300, compression = "lzw")
```
For multi-panel: `(<code>p1 | p2) / p3 + plot_annotation(tag_levels = "a")</code>`.

## Journal figure-spec hook
When a target journal is selected (via `journal-selector`), read its
`## Formatting constraints` block and apply `figure_dpi`, `column_widths_mm`
(or `_cm`), and any format requirement (e.g. RSC TOC graphic, ACS TOC graphic,
MDPI ≥1000 dpi line art) before export. If no journal is set, use the defaults
in Step 4 and note the assumption.

## Not for
Dashboards, slide infographics, or Illustrator/Figma-first artwork. This skill
produces reproducible, code-generated, submission-grade scientific figures.
