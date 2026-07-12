#!/usr/bin/env Rscript
# Food & nutrition figure templates (R: ggplot2 / patchwork / ComplexHeatmap /
# ggrepel; export via svglite / cairo_pdf / ragg). Ready to adapt — replace the
# synthetic data with your own.
# Packages: ggplot2, patchwork, ggrepel, ComplexHeatmap, circlize, svglite, ragg,
#           ggpubr/rstatix (stats), survminer (KM), factoextra (PCA).
#   Rscript r_food_figures.R      # renders a demo multi-panel

suppressPackageStartupMessages({
  library(ggplot2); library(patchwork)
})

okabe <- c("#000000","#E69F00","#56B4E9","#009E73","#F0E442","#0072B2","#D55E00","#CC79A7")
theme_pub <- theme_classic(base_size = 8, base_family = "Arial") +
  theme(axis.line = element_line(linewidth = 0.4), legend.key.size = unit(3, "mm"),
        strip.background = element_blank())
theme_set(theme_pub)

# --- grouped bar + error bars + significance letters --------------------------
fig_bar_letters <- function(df) {
  ggplot(df, aes(group, mean, fill = group)) +
    geom_col(width = 0.7) +
    geom_errorbar(aes(ymin = mean - sem, ymax = mean + sem), width = 0.2) +
    geom_text(aes(y = mean + sem, label = letter), vjust = -0.4, size = 2.5) +
    scale_fill_manual(values = okabe[-1]) +
    labs(x = NULL, y = "Firmness (N)") + theme(legend.position = "none")
}

# --- box/violin + jittered points ---------------------------------------------
fig_box <- function(df) {
  ggplot(df, aes(group, value, fill = group)) +
    geom_violin(alpha = 0.4, colour = NA) +
    geom_boxplot(width = 0.2, outlier.shape = NA) +
    geom_jitter(width = 0.12, size = 0.8, colour = "grey20") +
    scale_fill_manual(values = okabe[-1]) +
    labs(x = NULL, y = "Response") + theme(legend.position = "none")
}

# --- kinetic / growth curve + fit ---------------------------------------------
fig_curve <- function(df) {
  ggplot(df, aes(time, logN, colour = treatment)) +
    geom_point(size = 1) +
    geom_smooth(method = "loess", se = TRUE, linewidth = 0.6) +
    scale_colour_manual(values = okabe[-1]) +
    labs(x = "Time (day)", y = "log CFU/g")
}

# --- scatter + regression -----------------------------------------------------
fig_scatter <- function(df) {
  ggplot(df, aes(x, y)) +
    geom_point(size = 1, colour = okabe[3]) +
    geom_smooth(method = "lm", se = TRUE, colour = "grey10") +
    labs(x = "x", y = "y")
}

# --- PCA scores + repelled loadings (ggrepel) ---------------------------------
fig_pca <- function(X, groups) {
  pr <- prcomp(scale(X)); ve <- summary(pr)$importance[2, 1:2] * 100
  scores <- data.frame(pr$x[, 1:2], group = groups)
  load <- data.frame(pr$rotation[, 1:2] * 3, var = rownames(pr$rotation))
  ggplot(scores, aes(PC1, PC2, colour = group)) +
    geom_point(size = 1.5) + stat_ellipse(level = 0.95, linewidth = 0.3) +
    ggrepel::geom_text_repel(data = load, aes(PC1, PC2, label = var),
                             inherit.aes = FALSE, size = 2.3, max.overlaps = 20) +
    scale_colour_manual(values = okabe[-1]) +
    labs(x = sprintf("PC1 (%.0f%%)", ve[1]), y = sprintf("PC2 (%.0f%%)", ve[2]))
}

# --- ComplexHeatmap (draw to a device to export) ------------------------------
fig_heatmap <- function(mat, groups, file = "heatmap.tiff") {
  suppressPackageStartupMessages({ library(ComplexHeatmap); library(circlize); library(ragg) })
  m <- t(scale(mat))                                   # z-score by variable
  col <- colorRamp2(c(-2, 0, 2), c("#0072B2", "white", "#D55E00"))
  ha <- HeatmapAnnotation(group = groups)
  ht <- Heatmap(m, name = "z", col = col, top_annotation = ha,
                row_names_gp = gpar(fontsize = 6), column_names_gp = gpar(fontsize = 6))
  agg_tiff(file, width = 120, height = 100, units = "mm", res = 300); draw(ht); dev.off()
}

# --- export helper (svglite / cairo_pdf / ragg) -------------------------------
save_fig <- function(p, stem, w = 90, h = 66) {
  ggsave(paste0(stem, ".svg"),  p, device = svglite::svglite, width = w, height = h, units = "mm")
  ggsave(paste0(stem, ".pdf"),  p, device = cairo_pdf,        width = w, height = h, units = "mm")
  ggsave(paste0(stem, ".tiff"), p, device = ragg::agg_tiff,   width = w, height = h, units = "mm", res = 300)
}

# --- demo ---------------------------------------------------------------------
demo <- function() {
  set.seed(1)
  bar <- data.frame(group = c("Ctrl", "T1", "T2"), mean = c(10, 15, 22),
                    sem = c(1, 1.2, 1.5), letter = c("a", "b", "c"))
  box <- data.frame(group = rep(c("Ctrl", "T1", "T2"), each = 20),
                    value = c(rnorm(20, 10), rnorm(20, 14), rnorm(20, 20)))
  sc  <- data.frame(x = rnorm(40, 10, 2)); sc$y <- 2 * sc$x + rnorm(40, 0, 2)
  fig <- (fig_bar_letters(bar) | fig_box(box)) / fig_scatter(sc) +
    plot_annotation(tag_levels = "a")
  save_fig(fig, "demo_food_figures_r", w = 180, h = 130)
  message("wrote demo_food_figures_r.{svg,pdf,tiff}")
}

if (sys.nframe() == 0) demo()
