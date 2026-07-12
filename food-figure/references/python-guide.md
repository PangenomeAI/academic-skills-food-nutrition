# Python Backend — matplotlib · seaborn · subplot_mosaic · statsmodels

Toolkit: **matplotlib** (base), **seaborn** (statistical charts), **numpy/pandas**
(data), **statsmodels** (regression/CI/ANOVA/mixed models), **scipy** (stats,
curve_fit), **scikit-learn** (PCA/PLS), **scikit-image** (image plates),
**lifelines** (survival). Ready-to-adapt scripts: `examples/python_food_figures.py`.

## Publication defaults
Quickest: apply the bundled style file, then override per journal:
```python
import matplotlib.pyplot as plt
plt.style.use("food-figure/assets/publication.mplstyle")   # Okabe-Ito, editable vector text, 300 dpi
```
Or set rcParams directly:
```python
import matplotlib as mpl
mpl.rcParams.update({"figure.dpi":300,"savefig.dpi":300,"font.family":"Arial","font.size":8,
    "axes.linewidth":0.8,"axes.spines.top":False,"axes.spines.right":False,
    "svg.fonttype":"none","pdf.fonttype":42,"ps.fonttype":42})
OKABE=['#000000','#E69F00','#56B4E9','#009E73','#F0E442','#0072B2','#D55E00','#CC79A7']
MM=1/25.4   # size in mm: fig,ax=plt.subplots(figsize=(90*MM,66*MM))
```

## matplotlib — figures, axes, layout
- **Single/grid:** `fig, ax = plt.subplots()` · `fig, axs = plt.subplots(2, 3, figsize=..., sharex=True)`.
- **GridSpec** for unequal panels: `gs = fig.add_gridspec(2, 3, height_ratios=[2,1]); ax = fig.add_subplot(gs[0, :2])`.
- **Twin axis:** `ax2 = ax.twinx()` (e.g. log CFU/g and pH over storage time).
- **Annotations:** significance letters/asterisks with `ax.text(x, y, "a", ha="center")`; brackets via `ax.annotate`.
- **Export:** `fig.savefig("f.pdf")` (vector), `fig.savefig("f.svg")` (editable), `fig.savefig("f.tiff", dpi=300, pil_kwargs={"compression":"tiff_lzw"})` (raster).

## subplot_mosaic — named multi-panel layouts (preferred for manuscript figures)
`subplot_mosaic` lays panels out from an ASCII map and returns a dict keyed by
name — clearer than index juggling, and easy to give panels different sizes:
```python
fig, axd = plt.subplot_mosaic(
    """
    AAB
    CCB
    DEB
    """,
    figsize=(180*MM, 150*MM),
    gridspec_kw={"height_ratios":[1,1,1], "width_ratios":[1,1,1.2]},
    per_subplot_kw={"B": {"projection": "polar"}},   # e.g. a radar panel
)
for label, ax in axd.items():
    ax.set_title(label, loc="left", fontweight="bold")   # panel tags a, b, c…
# axd["A"].bar(...); axd["B"].plot(...); ...
fig.savefig("figure1.pdf")
```
Use `.` in the map for an empty cell. This is the recommended way to build the
composite figures a manuscript needs.

## seaborn — statistical charts
Seaborn draws onto matplotlib Axes and respects the rcParams above (call
`sns.set_theme(style="ticks", rc=mpl.rcParams)` or just use your style file).
- **Groups × response:** `sns.barplot(data=df, x="treatment", y="firmness", errorbar="sd", ax=ax)`; add points with `sns.stripplot`/`sns.swarmplot`.
- **Distributions:** `sns.boxplot` / `sns.violinplot` (+ overlay `sns.stripplot`), `sns.histplot`, `sns.kdeplot`, `sns.ecdfplot`.
- **Relationships:** `sns.regplot` / `sns.lmplot` (scatter + fit + CI), `sns.scatterplot` (hue/size/style for extra encodings).
- **Multivariate:** `sns.heatmap` (annotated matrix), `sns.clustermap` (row/col dendrograms, `z_score`/`standard_scale` for scaling), `sns.pairplot`.
- **Faceting:** `sns.catplot(..., col="storage", kind="box")` for small multiples.
- Set the palette to Okabe-Ito: `sns.set_palette(OKABE)`.

## statsmodels — fits, CIs, ANOVA, mixed models
Use to compute the statistics you overlay or report (pair with `food-paper`'s
`statistics-reporting.md`).
```python
import statsmodels.api as sm, statsmodels.formula.api as smf
# OLS regression + 95% CI band to overlay on a scatter
m = smf.ols("response ~ dose", data=df).fit()
pred = m.get_prediction(newdf).summary_frame(alpha=0.05)   # mean, mean_ci_lower/upper
ax.plot(newdf.dose, pred["mean"]); ax.fill_between(newdf.dose, pred["mean_ci_lower"], pred["mean_ci_upper"], alpha=0.2)
# LOWESS trend
lo = sm.nonparametric.lowess(df.y, df.x, frac=0.3)
# One/two-way ANOVA (report F, p)
sm.stats.anova_lm(smf.ols("firmness ~ C(treatment)", data=df).fit(), typ=2)
# Mixed model (random batch/panelist)
smf.mixedlm("response ~ treatment", df, groups=df["batch"]).fit()
```
For non-linear food kinetics (Weibull/Gompertz microbial models, dose–response),
fit with `scipy.optimize.curve_fit` and overlay the fitted curve + CI.

## Figure types → helper in `examples/python_food_figures.py`
grouped bar + significance letters · box/violin + points · kinetic/growth curve +
model fit · dose–response · scatter + regression (statsmodels CI) · Bland–Altman ·
sensory radar (polar) · PCA scores+loadings · clustered heatmap · Kaplan–Meier ·
forest plot · multi-panel via `subplot_mosaic`.
