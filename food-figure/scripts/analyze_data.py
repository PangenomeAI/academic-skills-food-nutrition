#!/usr/bin/env python3
"""Profile a food/nutrition dataset and recommend figure types.

Stdlib only (csv/statistics) so it runs anywhere — no pandas required.
For Excel, export to CSV/TSV first.

Usage:
  python analyze_data.py DATA.csv          # profile + figure recommendations
  python analyze_data.py --selftest        # run built-in asserts, print OK

The recommendation rules mirror references/data-to-figure.md.
"""
import csv
import io
import statistics
import sys

DATE_HINTS = ("date", "time", "day", "week", "month", "hour", "min")
DOSE_HINTS = ("dose", "conc", "concentration", "level", "temperature", "temp", "ph")
ID_HINTS = ("id", "subject", "panelist", "replicate", "rep", "sample", "batch")


def _is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def infer_type(values):
    """Return 'numeric', 'datetime', or 'categorical' for a list of raw strings."""
    vals = [v for v in values if v not in ("", "NA", "NaN", "null", "None")]
    if not vals:
        return "empty"
    if all(_is_number(v) for v in vals):
        return "numeric"
    # crude datetime sniff: contains '-' or '/' with digits, or ISO-like
    dateish = sum(1 for v in vals if any(c.isdigit() for c in v) and ("-" in v or "/" in v or ":" in v))
    if dateish >= 0.8 * len(vals):
        return "datetime"
    return "categorical"


def profile_columns(header, rows):
    profiles = []
    for i, name in enumerate(header):
        col = [r[i] if i < len(r) else "" for r in rows]
        nonempty = [v for v in col if v not in ("", "NA", "NaN", "null", "None")]
        t = infer_type(col)
        p = {
            "name": name,
            "type": t,
            "n": len(col),
            "missing": len(col) - len(nonempty),
            "cardinality": len(set(nonempty)),
        }
        if t == "numeric" and nonempty:
            nums = [float(v) for v in nonempty]
            p["min"], p["max"] = min(nums), max(nums)
            p["mean"] = round(statistics.fmean(nums), 4)
            p["std"] = round(statistics.pstdev(nums), 4) if len(nums) > 1 else 0.0
        elif t == "categorical":
            levels = {}
            for v in nonempty:
                levels[v] = levels.get(v, 0) + 1
            p["levels"] = sorted(levels.items(), key=lambda kv: -kv[1])[:12]
        profiles.append(p)
    return profiles


def _named(name, hints):
    n = name.lower()
    return any(h in n for h in hints)


def detect_structure(profiles):
    numeric = [p for p in profiles if p["type"] == "numeric"]
    categ = [p for p in profiles if p["type"] == "categorical"]
    # grouping factor: categorical, 2..12 levels, repeated (rows > levels)
    groups = [p for p in categ if 2 <= p["cardinality"] <= 12 and p["n"] > p["cardinality"]]
    ids = [p for p in profiles if _named(p["name"], ID_HINTS)]
    time_axis = [p for p in numeric if _named(p["name"], DATE_HINTS)] + \
                [p for p in profiles if p["type"] == "datetime"]
    dose_axis = [p for p in numeric if _named(p["name"], DOSE_HINTS)]
    # response numerics = numeric cols that aren't the time/dose/id axes
    axis_names = {p["name"] for p in time_axis + dose_axis + ids}
    responses = [p for p in numeric if p["name"] not in axis_names]
    return {
        "numeric": numeric, "categorical": categ, "groups": groups, "ids": ids,
        "time_axis": time_axis, "dose_axis": dose_axis, "responses": responses,
    }


def recommend(profiles, s):
    """Return a list of (chart, rationale) tuples, most-recommended first."""
    recs = []
    g, resp = s["groups"], s["responses"]
    wide = len(resp) >= 4  # many response variables => multivariate

    if s["time_axis"] and resp:
        who = " by " + g[0]["name"] if g else ""
        recs.append(("line / kinetic curve",
                     f"time axis '{s['time_axis'][0]['name']}' vs response{who} — show the trend over time"))
    if s["dose_axis"] and resp:
        recs.append(("dose–response curve",
                     f"'{s['dose_axis'][0]['name']}' vs response — fit/overlay a dose–response model"))
    if g and resp and not s["time_axis"]:
        # rows per group: many -> distribution; few -> bar+error
        per = profiles and (max(p["n"] for p in resp) / max(1, g[0]["cardinality"]))
        if per and per >= 8:
            recs.append(("box/violin + jittered points",
                         f"several observations per level of '{g[0]['name']}' — show the distribution, not just the mean"))
        recs.append(("grouped bar + error bars + significance letters",
                     f"treatment factor '{g[0]['name']}' vs response — group means with SD/SEM and post-hoc letters"))
    if wide:
        colour = f", colour by '{g[0]['name']}'" if g else ""
        recs.append(("PCA / PLS-DA (scores + loadings)",
                     f"{len(resp)} response variables across samples — reduce dimensions{colour}"))
        recs.append(("clustered heatmap",
                     f"{len(resp)} variables — show the sample × variable matrix with clustering"))
    if len(resp) == 2 and not g:
        recs.append(("scatter + regression",
                     f"two numeric variables ('{resp[0]['name']}', '{resp[1]['name']}') — relationship/correlation"))
        recs.append(("Bland–Altman",
                     "if the two variables are methods measuring the same quantity — assess agreement (not just correlation)"))
    if len(resp) == 1 and not g and not s["time_axis"]:
        recs.append(("histogram / density (+ box)",
                     f"single numeric '{resp[0]['name']}' — show its distribution"))
    if wide and not (g or s["ids"]):
        recs.append(("radar / spider (per sample)",
                     "many attributes per sample (e.g. sensory profile) — compare profiles across samples"))
    if not recs:
        recs.append(("summary table + simple bar",
                     "data shape is ambiguous — start with a table and a basic bar; refine after clarifying the claim"))
    return recs


def render_report(path, profiles, s, recs):
    out = io.StringIO()
    w = out.write
    w(f"# Data profile: {path}\n\n")
    w(f"rows: {profiles[0]['n'] if profiles else 0}  columns: {len(profiles)}\n\n")
    w("## Columns\n")
    for p in profiles:
        line = f"- {p['name']}: {p['type']} (unique={p['cardinality']}, missing={p['missing']})"
        if p["type"] == "numeric" and "mean" in p:
            line += f" mean={p['mean']} sd={p['std']} range=[{p['min']}, {p['max']}]"
        if p["type"] == "categorical":
            line += " levels=" + ", ".join(f"{k}({v})" for k, v in p["levels"])
        w(line + "\n")
    w("\n## Detected structure\n")
    for k in ("groups", "time_axis", "dose_axis", "ids", "responses"):
        names = ", ".join(p["name"] for p in s[k]) or "—"
        w(f"- {k}: {names}\n")
    w("\n## Recommended figures (best first)\n")
    for i, (chart, why) in enumerate(recs, 1):
        w(f"{i}. **{chart}** — {why}\n")
    return out.getvalue()


def analyze(header, rows):
    profiles = profile_columns(header, rows)
    s = detect_structure(profiles)
    return profiles, s, recommend(profiles, s)


def read_delimited(path):
    with open(path, newline="", encoding="utf-8-sig") as f:
        sample = f.read(2048)
        f.seek(0)
        delim = "\t" if sample.count("\t") > sample.count(",") else ","
        reader = csv.reader(f, delimiter=delim)
        rows = [r for r in reader if any(c.strip() for c in r)]
    if not rows:
        raise SystemExit("empty file")
    return rows[0], rows[1:]


def selftest():
    # treatment × response -> bar
    header = ["treatment", "firmness"]
    rows = [["A", "10"], ["A", "11"], ["B", "20"], ["B", "21"]]
    _, s, recs = analyze(header, rows)
    assert any("bar" in c for c, _ in recs), recs
    assert s["groups"], "should detect a grouping factor"

    # time × response by group -> line
    header = ["day", "group", "count"]
    rows = [["0", "ctrl", "6"], ["7", "ctrl", "5"], ["0", "trt", "6"], ["7", "trt", "3"]]
    _, s, recs = analyze(header, rows)
    assert recs[0][0].startswith("line"), recs
    assert s["time_axis"], "should detect a time axis"

    # two numerics -> scatter
    header = ["x", "y"]
    rows = [["1", "2"], ["2", "4"], ["3", "5"]]
    _, _, recs = analyze(header, rows)
    assert any("scatter" in c for c, _ in recs), recs

    # wide matrix + group -> PCA/heatmap
    header = ["group", "a", "b", "c", "d"]
    rows = [["x", "1", "2", "3", "4"], ["y", "2", "3", "4", "5"], ["z", "5", "4", "3", "2"]]
    _, _, recs = analyze(header, rows)
    assert any("PCA" in c or "heatmap" in c for c, _ in recs), recs

    print("OK: analyze_data selftest passed")


def main(argv):
    if len(argv) == 2 and argv[1] == "--selftest":
        selftest()
        return 0
    if len(argv) != 2:
        print(__doc__)
        return 2
    header, rows = read_delimited(argv[1])
    profiles, s, recs = analyze(header, rows)
    print(render_report(argv[1], profiles, s, recs))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
