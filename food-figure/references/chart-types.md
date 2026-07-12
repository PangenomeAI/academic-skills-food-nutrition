# Chart Types — catalog

Each entry: **when to use · data shape · encodings · pitfalls**. Food/nutrition
examples throughout. Rendering code is in `python-guide.md` / `r-guide.md` /
`food-recipes.md`.

## Comparison of groups
- **Grouped/clustered bar + error bars.** When: treatment means. Data: categorical factor(s) × numeric. Encode: bar height = mean, whisker = SD/SEM, letters = post-hoc. Pitfall: hides distribution; always state n and error type.
- **Box plot / violin (+ points).** When: distributions across groups. Data: factor × numeric, many obs/level. Encode: quartiles/density + raw points. Pitfall: needs enough n per group.
- **Dot/strip plot.** When: small n where every point matters.

## Trends & kinetics
- **Line / kinetic curve.** When: change over time/storage. Data: time × numeric (± group). Pitfall: don't connect unordered categories.
- **Area / stacked area.** When: cumulative composition over time. Pitfall: hard to read many layers.
- **Dose–response / regression curve.** When: response vs dose/condition; model fits (Weibull/Gompertz/log-logistic). Encode: points + fitted line + CI band.
- **Survival / Kaplan–Meier.** When: time-to-event (spoilage, shelf-life). Encode: step curve + censoring ticks + risk table.

## Relationships
- **Scatter (+ regression, + marginal).** When: two numerics. Pitfall: correlation ≠ agreement.
- **Bland–Altman.** When: two methods measuring the same quantity. Encode: mean vs difference + limits of agreement.
- **Bubble.** When: scatter with a third quantitative encoding (size).

## Multivariate
- **PCA / PLS-DA (scores + loadings).** When: many variables (metabolomics, volatiles, sensory, composition). Encode: scores coloured by group + loadings; report variance explained; cross-validate PLS-DA.
- **Clustered heatmap.** When: sample × variable matrix. Encode: scaled colour + dendrograms. Pitfall: state the scaling (z-score/row).
- **Correlation matrix / corrplot.** When: pairwise correlations among variables.

## Profiles & proportions
- **Radar / spider.** When: multi-attribute profiles per sample (sensory). Pitfall: area is misleading; mark the scale.
- **Stacked / 100% bar.** When: proportions/composition. Pitfall: prefer over pie charts.

## Distributions
- **Histogram / density.** When: one variable's distribution.
- **ECDF.** When: comparing distributions without binning.

## Evidence synthesis
- **Forest plot.** When: effect sizes + CIs across studies (meta-analysis). Encode: point + CI + weight; pooled diamond; I².

## Images & structure
- **Microscopy image plate.** When: SEM/CLSM/light micrographs. Encode: consistent magnification, **scale bar on every panel**, state stain/mode.
- **Chromatogram (HPLC/GC).** When: separation/identification. Encode: retention-time axis, labelled peaks, preserved baseline.
- **Texture Profile Analysis (TPA) trace.** When: force–time curve or grouped texture parameters.
- **Rheology.** When: flow/oscillatory data; log axes where appropriate; label G′/G″.

## Layout
- **Multi-panel (GridSpec / patchwork).** Combine related panels; label a, b, c; align axes; share legends.
