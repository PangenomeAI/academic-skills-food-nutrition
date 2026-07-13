#!/usr/bin/env Rscript
# Reproducible synthetic/illustrative food & nutrition figure gallery.
# Requires only base R. Run from this directory: Rscript render_gallery.R

root <- "food-figure/examples/gallery"
data_dir <- file.path(root, "data")
figure_dir <- file.path(root, "figures")
dir.create(figure_dir, recursive = TRUE, showWarnings = FALSE)

read_case <- function(name) read.csv(file.path(data_dir, name), check.names = FALSE)
okabe <- c("#000000", "#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7")
save_pair <- function(stem, draw, width = 1800, height = 1200) {
  pdf_path <- file.path(figure_dir, paste0(stem, ".pdf"))
  png_path <- file.path(figure_dir, paste0(stem, ".png"))
  pdf(pdf_path, width = width / 300, height = height / 300,
      family = "Helvetica", useDingbats = FALSE)
  draw(); dev.off()
  # macOS sips renders a PDF page without R's optional Cairo/X11 dependency.
  # JPEG intermediate flattens the PDF's transparent page onto white before PNG.
  tmp_jpg <- tempfile(fileext = ".jpg")
  status <- system2("sips", c("-s", "format", "jpeg", "-z", as.character(height), as.character(width), pdf_path, "--out", tmp_jpg), stdout = FALSE, stderr = FALSE)
  if (status == 0) status <- system2("sips", c("-s", "format", "png", tmp_jpg, "--out", png_path), stdout = FALSE, stderr = FALSE)
  unlink(tmp_jpg)
  if (status != 0 || !file.exists(png_path)) stop("PNG conversion failed for ", stem)
}

# Case 1: active packaging, grouped bars plus an in-vitro screening dose-response.
poly <- read_case("polyphenol_retention.csv")
dose <- read_case("film_extract_dose_response.csv")
save_pair("fig1_active_packaging", function() {
  par(mfrow = c(1, 2), mar = c(4.5, 4.5, 2, 1), las = 1, cex.axis = 0.85, cex.lab = 0.95)
  groups <- unique(poly$package); labels <- c("Control", "Pectin", "Active pectin"); means <- tapply(poly$retention_percent, poly$package, mean)
  sds <- tapply(poly$retention_percent, poly$package, sd)
  mids <- barplot(means, names.arg = labels, ylim = c(0, 100), col = okabe[c(3, 4, 2)], border = NA,
                  ylab = "Polyphenol retention (%)", xlab = "Packaging treatment", cex.names = 0.8)
  arrows(mids, means - sds, mids, means + sds, angle = 90, code = 3, length = 0.04)
  text(mids, means + sds + 5, c("a", "b", "c"), cex = 1.1)
  mtext("a", side = 3, adj = 0, font = 2, line = 0.2)
  doses <- sort(unique(dose$concentration_mg_ml)); resp <- tapply(dose$radical_scavenging_percent, dose$concentration_mg_ml, mean)
  plot(doses, resp, log = "x", pch = 16, col = okabe[4], ylim = c(0, 100), xaxt = "n",
       xlab = "Film-extract concentration (mg/mL)", ylab = "Radical scavenging (%)")
  axis(1, at = doses, labels = doses)
  fit <- smooth.spline(log10(doses), resp, spar = 0.65); xx <- seq(log10(min(doses)), log10(max(doses)), length.out = 200)
  lines(10^xx, predict(fit, xx)$y, col = okabe[4], lwd = 2)
  mtext("b", side = 3, adj = 0, font = 2, line = 0.2)
})

# Case 2: probiotic storage kinetics.
kin <- read_case("probiotic_storage_kinetics.csv")
save_pair("fig2_probiotic_storage_kinetics", function() {
  par(mar = c(4.5, 4.8, 1.5, 1), las = 1, cex.axis = 0.9, cex.lab = 1)
  treatments <- unique(kin$treatment)
  plot(range(kin$day), c(3, 9), type = "n", xlab = "Storage time (day)", ylab = expression("Viable count (log CFU/g)"))
  abline(h = 6, lty = 2, col = "grey45"); text(26, 6.15, "Illustrative quality threshold", pos = 2, cex = 0.75, col = "grey35")
  for (i in seq_along(treatments)) {
    d <- kin[kin$treatment == treatments[i], ];
    means <- tapply(d$log_cfu_g, d$day, mean); sds <- tapply(d$log_cfu_g, d$day, sd)
    xs <- as.numeric(names(means)); arrows(xs, means - sds, xs, means + sds, angle = 90, code = 3, length = 0.025, col = okabe[i + 2])
    lines(xs, means, type = "b", pch = 15 + i, lwd = 2, col = okabe[i + 2])
  }
  legend("topright", treatments, col = okabe[3:4], pch = 16:17, lwd = 2, bty = "n")
})

# Case 3: sensory profile.
sensory <- read_case("sensory_panel_profile.csv")
save_pair("fig3_sensory_radar", function() {
  par(mar = c(1, 1, 1, 1))
  attributes <- unique(sensory$attribute); n <- length(attributes); theta <- seq(0, 2 * pi, length.out = n + 1)[-(n + 1)]
  plot(0, 0, type = "n", xlim = c(-1.2, 1.2), ylim = c(-1.2, 1.2), axes = FALSE, xlab = "", ylab = "", asp = 1)
  for (r in c(3, 6, 9)) lines(r / 9 * cos(c(theta, theta[1])), r / 9 * sin(c(theta, theta[1])), col = "grey85")
  for (i in seq_len(n)) {
    segments(0, 0, cos(theta[i]), sin(theta[i]), col = "grey75")
    text(1.12 * cos(theta[i]), 1.12 * sin(theta[i]), attributes[i], cex = 0.8)
  }
  samples <- unique(sensory$sample)
  for (i in seq_along(samples)) {
    d <- sensory[sensory$sample == samples[i], ]; d <- d[match(attributes, d$attribute), ]
    rr <- c(d$mean_score / 9, d$mean_score[1] / 9)
    lines(rr * cos(c(theta, theta[1])), rr * sin(c(theta, theta[1])), col = okabe[i + 1], lwd = 2)
    polygon(rr * cos(c(theta, theta[1])), rr * sin(c(theta, theta[1])), border = okabe[i + 1], col = adjustcolor(okabe[i + 1], alpha.f = 0.12))
  }
  legend("topright", samples, col = okabe[2:3], lwd = 2, bty = "n", title = "Illustrative 0-9 scale")
})

# Case 4: method agreement and synthetic evidence synthesis.
agreement <- read_case("method_validation_agreement.csv")
forest <- read_case("illustrative_forest_effects.csv")
save_pair("fig4_method_validation_and_evidence", function() {
  par(mfrow = c(1, 2), mar = c(4.5, 4.7, 2, 1), las = 1, cex.axis = 0.85, cex.lab = 0.95)
  mean_val <- rowMeans(agreement[c("hplc_mg_100g", "rapid_assay_mg_100g")]); difference <- agreement$rapid_assay_mg_100g - agreement$hplc_mg_100g
  bias <- mean(difference); sd_diff <- sd(difference); loa <- bias + c(-1.96, 1.96) * sd_diff
  plot(mean_val, difference, pch = 16, col = okabe[7], xlab = "Mean phenolic concentration (mg/100 g)", ylab = "Rapid assay - HPLC (mg/100 g)")
  abline(h = c(bias, loa), lty = c(1, 2, 2), col = c("black", "grey35", "grey35")); mtext("a", side = 3, adj = 0, font = 2, line = 0.2)
  y <- rev(seq_len(nrow(forest))); plot(range(forest$lower_ci, forest$upper_ci), c(0.5, nrow(forest) + 0.5), type = "n", yaxt = "n", xlab = "Standardised mean difference (95% CI)", ylab = "")
  axis(2, at = y, labels = forest$study_label, las = 1); abline(v = 0, lty = 2, col = "grey40")
  arrows(forest$lower_ci, y, forest$upper_ci, y, angle = 90, code = 3, length = 0.04, col = okabe[1]); points(forest$effect, y, pch = 15, col = okabe[1])
  mtext("b", side = 3, adj = 0, font = 2, line = 0.2)
})

message("Wrote PDF and PNG files to ", figure_dir)
