# R Backend — ggplot2 / patchwork / ComplexHeatmap

Toolkit: ggplot2, patchwork, ComplexHeatmap, ggpubr, survminer, factoextra
(PCA), ropls/mixOmics (PLS-DA), svglite. Prefer R when the data is in
RData/RDS/data.frame, the workflow is already R, or heatmap annotations are rich
and multi-layered.

## Publication defaults
```r
library(ggplot2); library(patchwork)
okabe <- c("#000000","#E69F00","#56B4E9","#009E73","#F0E442","#0072B2","#D55E00","#CC79A7")
theme_pub <- theme_classic(base_size = 8, base_family = "Arial") +
  theme(axis.line = element_line(linewidth = 0.4), legend.key.size = unit(3, "mm"))
```

## Grouped bar + error bars + significance letters
```r
p <- ggplot(df, aes(group, mean, fill = group)) +
  geom_col(width = .7) +
  geom_errorbar(aes(ymin = mean - sem, ymax = mean + sem), width = .2) +
  geom_text(aes(y = mean + sem, label = letter), vjust = -0.4) +
  scale_fill_manual(values = okabe) +
  labs(y = "Firmness (N)", x = NULL) + theme_pub + theme(legend.position = "none")
```

## Multi-panel
```r
(p1 | p2) / p3 + plot_annotation(tag_levels = "a")
```

## Export (journal spec)
```r
ggsave("fig1.pdf",  p, width = 90, height = 66, units = "mm")            # vector
ggsave("fig1.svg",  p, width = 90, height = 66, units = "mm")            # editable (svglite)
ggsave("fig1.tiff", p, width = 90, height = 66, units = "mm", dpi = 300, compression = "lzw")
```

Other panels: `geom_boxplot`/`geom_violin` + `geom_jitter`; `factoextra::fviz_pca`
for PCA; `ComplexHeatmap::Heatmap` for clustered/annotated heatmaps;
`survminer::ggsurvplot` for Kaplan–Meier; `ggpubr::stat_compare_means` for tests.
See `food-recipes.md` for food-specific panels.
