# R Backend — ggplot2 · patchwork · ComplexHeatmap · ggrepel · svglite/cairo_pdf/ragg

Toolkit: **ggplot2** (grammar of graphics), **patchwork** (compose panels),
**ComplexHeatmap** (annotated/clustered heatmaps), **ggrepel** (non-overlapping
labels), plus **svglite** (SVG), **cairo_pdf** (PDF), **ragg** (high-quality
PNG/TIFF) for export; **ggpubr**/**rstatix** (stats + significance),
**survminer** (Kaplan–Meier), **factoextra**/**ropls** (PCA/PLS-DA). Ready-to-adapt
scripts: `examples/r_food_figures.R`.

## Publication theme & palette
```r
library(ggplot2); library(patchwork)
okabe <- c("#000000","#E69F00","#56B4E9","#009E73","#F0E442","#0072B2","#D55E00","#CC79A7")
theme_pub <- theme_classic(base_size = 8, base_family = "Arial") +
  theme(axis.line = element_line(linewidth = 0.4), legend.key.size = unit(3, "mm"),
        strip.background = element_blank())
theme_set(theme_pub)
```

## ggplot2 — the core charts
- **Groups × response (bar + error + letters):** `geom_col()` + `geom_errorbar()` + `geom_text(aes(label = letter))`; letters from `rstatix`/`multcomp` (Tukey).
- **Distributions:** `geom_boxplot()` / `geom_violin()` + `geom_jitter()`; `geom_histogram()`, `geom_density()`.
- **Trends/kinetics:** `geom_line()` + `geom_point()`; model fits with `geom_smooth(method = "nls"/"lm", ...)` or a precomputed fit + `geom_ribbon()` for the CI.
- **Relationships:** `geom_point()` + `geom_smooth(method = "lm")`.
- **Scales:** `scale_fill_manual(values = okabe)`, `scale_*_log10()` where warranted; `facet_wrap(~ storage)` for small multiples.
- **Stats/significance:** `ggpubr::stat_compare_means()` or `rstatix` + `stat_pvalue_manual()`.

## ggrepel — readable labels
Non-overlapping text labels (PCA loadings, volcano/metabolite names, outlier
samples):
```r
library(ggrepel)
p + geom_text_repel(aes(label = compound), size = 2.5, max.overlaps = 20,
                    box.padding = 0.3, segment.size = 0.2)
```

## patchwork — compose multi-panel figures
```r
layout <- (p_bar | p_curve) / (p_pca | p_heat) +
  plot_annotation(tag_levels = "a") +          # panel tags a, b, c…
  plot_layout(heights = c(1, 1.2), guides = "collect")
```
Use `plot_spacer()` for gaps; `wrap_elements()` to embed a base/ComplexHeatmap grob.

## ComplexHeatmap — annotated, clustered heatmaps
Best for metabolomics/volatiles/composition matrices (row = sample, col =
variable) with grouped annotations:
```r
library(ComplexHeatmap); library(circlize)
mat <- scale(t(as.matrix(df_numeric)))                       # z-score by variable
col <- colorRamp2(c(-2,0,2), c("#0072B2","white","#D55E00"))
ha  <- HeatmapAnnotation(group = groups, col = list(group = c(A="#E69F00", B="#009E73")))
ht  <- Heatmap(mat, name = "z", col = col, top_annotation = ha,
               cluster_rows = TRUE, cluster_columns = TRUE,
               row_names_gp = gpar(fontsize = 6), column_names_gp = gpar(fontsize = 6))
# export (ComplexHeatmap draws to a device — see below)
```

## Export — svglite · cairo_pdf · ragg (journal-ready)
```r
library(svglite); library(ragg)
# ggplot objects:
ggsave("fig1.svg",  p, device = svglite, width = 90, height = 66, units = "mm")           # editable vector
ggsave("fig1.pdf",  p, device = cairo_pdf, width = 90, height = 66, units = "mm")          # vector, good font embedding
ggsave("fig1.tiff", p, device = ragg::agg_tiff, width = 90, height = 66, units = "mm", res = 300)  # crisp raster
ggsave("fig1.png",  p, device = ragg::agg_png,  width = 90, height = 66, units = "mm", res = 600)
# ComplexHeatmap / base grid graphics -> open a device, draw, close:
agg_tiff("heatmap.tiff", width = 120, height = 100, units = "mm", res = 300); draw(ht); dev.off()
cairo_pdf("heatmap.pdf", width = 120/25.4, height = 100/25.4); draw(ht); dev.off()
```
- **svglite** — clean, small SVGs with real (editable) text.
- **cairo_pdf** — vector PDF with proper font embedding (better than the default `pdf()` for non-standard fonts).
- **ragg** (`agg_png`/`agg_tiff`) — high-quality antialiased raster at the journal DPI; preferred over base `png()`/`tiff()`.

## Figure types → helper in `examples/r_food_figures.R`
grouped bar + letters · box/violin + points · kinetic/growth curve + fit ·
dose–response · scatter + regression · Bland–Altman · sensory radar · PCA
(factoextra) · ComplexHeatmap · Kaplan–Meier (survminer) · forest · multi-panel
(patchwork).
