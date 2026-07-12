#!/usr/bin/env python3
"""Food & nutrition figure templates (Python: matplotlib / seaborn / statsmodels).

Ready-to-adapt functions for the common manuscript figure types. Each uses
synthetic data so it runs standalone; replace the synthetic frames with your own.
Requires: matplotlib, numpy, pandas, seaborn, statsmodels, scipy, scikit-learn
(lifelines optional for Kaplan-Meier). Apply the house style first.

    python python_food_figures.py            # render a demo multi-panel
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

OKABE = ["#000000", "#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7"]
MM = 1 / 25.4


def apply_style():
    mpl.rcParams.update({
        "figure.dpi": 300, "savefig.dpi": 300, "font.family": "Arial", "font.size": 8,
        "axes.linewidth": 0.8, "axes.spines.top": False, "axes.spines.right": False,
        "svg.fonttype": "none", "pdf.fonttype": 42, "ps.fonttype": 42,
    })


def save(fig, stem):
    fig.savefig(f"{stem}.pdf")
    fig.savefig(f"{stem}.tiff", dpi=300, pil_kwargs={"compression": "tiff_lzw"})


# --- grouped bar + error bars + significance letters --------------------------
def grouped_bar_letters(ax, groups, means, sems, letters, ylabel="Firmness (N)"):
    x = np.arange(len(groups))
    ax.bar(x, means, yerr=sems, capsize=3, color=OKABE[1:1 + len(groups)])
    for xi, mi, si, L in zip(x, means, sems, letters):
        ax.text(xi, mi + si + 0.03 * max(means), L, ha="center", va="bottom")
    ax.set_xticks(x); ax.set_xticklabels(groups); ax.set_ylabel(ylabel)


# --- box/violin + jittered points ---------------------------------------------
def box_points(ax, df, x, y):
    import seaborn as sns
    sns.boxplot(data=df, x=x, y=y, ax=ax, palette=OKABE[1:], width=0.6, fliersize=0)
    sns.stripplot(data=df, x=x, y=y, ax=ax, color="0.2", size=2.5, jitter=0.15)


# --- microbial growth / inactivation curve + model fit ------------------------
def growth_curve(ax, t, logN, group_label="treatment"):
    from scipy.optimize import curve_fit
    def weibull(t, N0, b, n):  # log-linear + tail style
        return N0 - b * np.power(t, n)
    p, _ = curve_fit(weibull, t, logN, p0=[logN[0], 0.1, 1.0], maxfev=10000)
    tt = np.linspace(t.min(), t.max(), 100)
    ax.plot(t, logN, "o", color=OKABE[5], label="data")
    ax.plot(tt, weibull(tt, *p), "-", color=OKABE[5], label="Weibull fit")
    ax.set_xlabel("Time (day)"); ax.set_ylabel("log CFU/g"); ax.legend()


# --- dose-response ------------------------------------------------------------
def dose_response(ax, dose, resp):
    from scipy.optimize import curve_fit
    def hill(x, bottom, top, ic50, h):
        return bottom + (top - bottom) / (1 + (x / ic50) ** h)
    p, _ = curve_fit(hill, dose, resp, p0=[0, max(resp), np.median(dose), 1], maxfev=10000)
    xx = np.logspace(np.log10(dose.min()), np.log10(dose.max()), 100)
    ax.plot(dose, resp, "o", color=OKABE[3]); ax.plot(xx, hill(xx, *p), color=OKABE[3])
    ax.set_xscale("log"); ax.set_xlabel("Concentration"); ax.set_ylabel("Response (%)")


# --- scatter + regression with statsmodels CI band ----------------------------
def scatter_regression(ax, df, x, y):
    import statsmodels.formula.api as smf
    m = smf.ols(f"{y} ~ {x}", data=df).fit()
    xs = pd.DataFrame({x: np.linspace(df[x].min(), df[x].max(), 100)})
    pr = m.get_prediction(xs).summary_frame(alpha=0.05)
    ax.scatter(df[x], df[y], s=10, color=OKABE[2])
    ax.plot(xs[x], pr["mean"], color="0.1")
    ax.fill_between(xs[x], pr["mean_ci_lower"], pr["mean_ci_upper"], color="0.6", alpha=0.3)
    ax.set_xlabel(x); ax.set_ylabel(y)


# --- Bland-Altman (method agreement) ------------------------------------------
def bland_altman(ax, m1, m2):
    mean = (m1 + m2) / 2; diff = m1 - m2
    md, sd = np.mean(diff), np.std(diff, ddof=1)
    ax.scatter(mean, diff, s=10, color=OKABE[6])
    for yv, ls in [(md, "-"), (md + 1.96 * sd, "--"), (md - 1.96 * sd, "--")]:
        ax.axhline(yv, color="0.3", linestyle=ls, linewidth=0.8)
    ax.set_xlabel("Mean of methods"); ax.set_ylabel("Difference (M1 - M2)")


# --- sensory radar (polar) ----------------------------------------------------
def sensory_radar(ax, attributes, profiles):
    n = len(attributes); ang = np.linspace(0, 2 * np.pi, n, endpoint=False)
    ang = np.concatenate([ang, ang[:1]])
    for i, (name, vals) in enumerate(profiles.items()):
        v = np.concatenate([vals, vals[:1]])
        ax.plot(ang, v, color=OKABE[i + 1], label=name); ax.fill(ang, v, color=OKABE[i + 1], alpha=0.1)
    ax.set_xticks(ang[:-1]); ax.set_xticklabels(attributes); ax.legend(loc="upper right", bbox_to_anchor=(1.3, 1.1))


# --- PCA scores ---------------------------------------------------------------
def pca_scores(ax, X, groups):
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import StandardScaler
    sc = PCA(n_components=2).fit(StandardScaler().fit_transform(X))
    Z = sc.transform(StandardScaler().fit_transform(X))
    for i, g in enumerate(sorted(set(groups))):
        m = np.array(groups) == g
        ax.scatter(Z[m, 0], Z[m, 1], s=12, color=OKABE[i + 1], label=str(g))
    ax.set_xlabel(f"PC1 ({sc.explained_variance_ratio_[0]*100:.0f}%)")
    ax.set_ylabel(f"PC2 ({sc.explained_variance_ratio_[1]*100:.0f}%)"); ax.legend()


# --- clustered heatmap (returns a seaborn ClusterGrid; save separately) -------
def clustered_heatmap(df_numeric, outfile="heatmap"):
    import seaborn as sns
    g = sns.clustermap(df_numeric, z_score=1, cmap="vlag", figsize=(120 * MM, 100 * MM),
                       xticklabels=True, yticklabels=True)
    g.savefig(f"{outfile}.pdf"); return g


# --- forest plot (meta-analysis) ----------------------------------------------
def forest(ax, labels, est, lo, hi):
    y = np.arange(len(labels))[::-1]
    ax.errorbar(est, y, xerr=[np.array(est) - np.array(lo), np.array(hi) - np.array(est)],
                fmt="s", color=OKABE[0], capsize=2)
    ax.axvline(0, color="0.6", linestyle="--", linewidth=0.8)
    ax.set_yticks(y); ax.set_yticklabels(labels); ax.set_xlabel("Effect size (95% CI)")


# --- demo multi-panel via subplot_mosaic --------------------------------------
def demo():
    apply_style()
    rng = np.random.default_rng(0)
    fig, axd = plt.subplot_mosaic("AB\nCD", figsize=(180 * MM, 130 * MM))
    grouped_bar_letters(axd["A"], ["Ctrl", "T1", "T2"], [10, 15, 22], [1, 1.2, 1.5], ["a", "b", "c"])
    t = np.arange(0, 15, 1.0); growth_curve(axd["B"], t, 6 - 0.03 * t ** 1.5 + rng.normal(0, 0.1, t.size))
    df = pd.DataFrame({"dose": np.repeat([1, 10, 100], 6).astype(float),
                       "response": np.r_[rng.normal(0.9, .05, 6), rng.normal(.6, .05, 6), rng.normal(.2, .05, 6)] * 100})
    dose_response(axd["C"], df["dose"].values, df["response"].values)
    x = rng.normal(10, 2, 40); df2 = pd.DataFrame({"x": x, "y": 2 * x + rng.normal(0, 2, 40)})
    scatter_regression(axd["D"], df2, "x", "y")
    for k, ax in axd.items():
        ax.set_title(k.lower(), loc="left", fontweight="bold")
    fig.tight_layout(); save(fig, "demo_food_figures")
    print("wrote demo_food_figures.pdf / .tiff")


if __name__ == "__main__":
    demo()
