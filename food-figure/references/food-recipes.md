# Food & Nutrition Figure Recipes

Domain-specific panels with the conventions reviewers expect. Use with
`python-guide.md` or `r-guide.md` for the base setup/export.

## Proximate composition / treatment means
Grouped bar + error bars + **post-hoc significance letters** (Tukey). State the
basis (wet/dry) and n. Alternative for many replicates: box/violin + points.

## Sensory profile
**Radar/spider** with one polygon per sample across attributes; mark the scale
(e.g. 0–9 or 0–15); report panel type and size in the legend. For preference
data, prefer bar + CI or a penalty analysis over radar.

## Microbial growth / survival / inactivation
Line/kinetic curve of **log CFU/g vs time**; overlay a fitted model
(Gompertz/Weibull/log-linear + tail) with goodness-of-fit; show LOD as a dashed
line; error bars = SD of biological replicates. Time-to-spoilage → survival curve.

## Shelf-life / storage
Line curves per treatment over storage time (quality index, colour ΔE, texture,
oxidation TBARS); mark the acceptability threshold.

## Chromatogram (HPLC/GC/LC-MS)
Retention-time (x) vs signal (y); label identified peaks with compound IDs;
preserve the baseline; offset-stack multiple traces for comparison.

## Texture Profile Analysis (TPA)
Either the **force–time trace** (annotate hardness, adhesiveness, cohesiveness,
springiness, chewiness) or grouped bars of the derived parameters; state the
probe, deformation %, and speed in the legend.

## Rheology
Flow curves (shear stress/viscosity vs shear rate, log–log) or oscillatory sweeps
(G′, G″ vs frequency/strain); mark the linear viscoelastic region; label G′/G″.

## Metabolomics / volatiles / multivariate
**PCA** scores (colour by group, 95% ellipses) + loadings; or **PLS-DA** with
cross-validation and permutation test (report R²/Q²); **clustered heatmap**
(z-scored) with sample and variable dendrograms.

## Antioxidant / dose–response
Response vs concentration with a fitted curve; report IC50/EC50 and the reference
standard (e.g. Trolox equivalents).

## Method agreement
**Bland–Altman** (mean vs difference, limits of agreement) when comparing two
assays for the same measurand — not correlation alone.

## Microstructure
SEM/CLSM/light-microscopy **image plate**: consistent magnification, a **scale
bar on every panel**, and the stain/mode stated; keep panels aligned and labelled.

## Meta-analysis (systematic review)
**Forest plot** of effect sizes + 95% CI, study weights, pooled diamond, and I².
