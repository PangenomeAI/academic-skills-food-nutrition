# Python Backend — matplotlib / seaborn

Toolkit: matplotlib, seaborn, pandas, numpy, statsmodels, scikit-learn (PCA/PLS),
scikit-image (image plates), lifelines (survival). Prefer Python when the data is
already in pandas/numpy, the key panel needs custom layout/image mosaics, or the
user's pipeline is Python.

## Publication defaults
```python
import matplotlib as mpl, matplotlib.pyplot as plt
mpl.rcParams.update({
    "figure.dpi": 300, "savefig.dpi": 300,
    "font.family": "Arial", "font.size": 8,
    "axes.linewidth": 0.8, "axes.spines.top": False, "axes.spines.right": False,
    "svg.fonttype": "none", "pdf.fonttype": 42, "ps.fonttype": 42,  # editable vector text
})
OKABE = ['#000000','#E69F00','#56B4E9','#009E73','#F0E442','#0072B2','#D55E00','#CC79A7']
```

## Sizing (journal spec)
```python
MM = 1/25.4
fig, ax = plt.subplots(figsize=(90*MM, 66*MM))   # single column ~90 mm; double ~190 mm
```

## Grouped bar + error bars + significance letters
```python
ax.bar(x, means, yerr=sems, capsize=3, color=OKABE)
for xi, mi, si, L in zip(x, means, sems, letters):
    ax.text(xi, mi+si+pad, L, ha="center", va="bottom")
ax.set_ylabel("Firmness (N)"); ax.set_xticks(x); ax.set_xticklabels(groups)
```

## Multi-panel
```python
fig, axs = plt.subplots(1, 3, figsize=(190*MM, 60*MM))
for ax, tag in zip(axs, "abc"):
    ax.text(-0.15, 1.05, tag, transform=ax.transAxes, fontsize=9, fontweight="bold")
fig.tight_layout()
```

## Export
```python
fig.savefig("fig1.pdf")                                   # vector (line/bar/scatter)
fig.savefig("fig1.svg")                                   # editable source
fig.savefig("fig1.tiff", dpi=300, pil_kwargs={"compression": "tiff_lzw"})  # raster
```

Other panels: `seaborn` for box/violin/strip; `sklearn.decomposition.PCA` +
scatter for PCA; `seaborn.clustermap` for clustered heatmaps; `lifelines` for
Kaplan–Meier; `statsmodels`/`scipy` for regression + CI bands. See
`food-recipes.md` for food-specific panels.
