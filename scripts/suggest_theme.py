#!/usr/bin/env python3
"""Suggest food-ppt themes for a deck from its text content. Stdlib only.

Reads the deck's text (title + abstract + topic, or a whole source file) and ranks the
themes in `food-ppt/templates/themes.json` by how well their `keywords` match — so
`ppt_coordinator` can **auto-pick a suitable theme and still offer the user a few
options** to choose from. This ranks aesthetics; it never changes deck content.

Usage:
  suggest_theme.py --text "Polyphenols as natural antimicrobials in food packaging"
  suggest_theme.py source.md --audience "conference" --doctype "review" --top 3
  suggest_theme.py --text "..." --json
  suggest_theme.py --selftest

Exit 0 always (advice, not a gate).
"""
import json
import os
import re
import sys

DEFAULT_THEME = "slate"


def themes_path():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(root, "food-ppt", "templates", "themes.json")


def load_themes(path=None):
    return json.load(open(path or themes_path(), encoding="utf-8"))


def _tokens(text):
    return set(re.findall(r"[a-z][a-z\-]+", (text or "").lower()))


def score(text, theme):
    """Score one theme against the deck text. Multi-word keywords match as a phrase;
    single-word keywords match as a whole token. Returns (score, [matched keywords])."""
    low = (text or "").lower()
    toks = _tokens(text)
    hits = []
    for kw in theme.get("keywords", []):
        k = kw.lower()
        if " " in k:
            if k in low:
                hits.append(kw)
        elif k in toks:
            hits.append(kw)
    return len(hits), hits


def rank(text, data=None, top=3):
    data = data or load_themes()
    themes = data["themes"]
    order = list(themes)                       # stable tie-break: themes.json order
    scored = []
    for name in order:
        sc, hits = score(text, themes[name])
        scored.append((sc, -order.index(name), name, hits))
    scored.sort(key=lambda t: (t[0], t[1]), reverse=True)
    ranked = [{"theme": n, "score": sc, "matched": h} for sc, _, n, h in scored]
    # If nothing matched at all, lead with the default theme.
    if ranked and ranked[0]["score"] == 0:
        ranked.sort(key=lambda r: (r["theme"] != (data.get("default") or DEFAULT_THEME)))
    return ranked[:top], themes


def format_report(text, data=None, top=3):
    ranked, themes = rank(text, data, top)
    lines = ["Suggested themes (auto-pick = the first; offer these as options):"]
    for i, r in enumerate(ranked, 1):
        t = themes[r["theme"]]
        why = ("matches: " + ", ".join(r["matched"])) if r["matched"] else t.get("best_for", "")
        lines.append(f"  {i}. {t.get('name', r['theme'])}  (theme=\"{r['theme']}\") — {t.get('style','')}")
        lines.append(f"       {why}")
    return "\n".join(lines)


def selftest():
    data = load_themes()
    assert data["themes"] and data.get("default") in data["themes"]
    # Every theme carries keywords (so the selector can reach it).
    for name, t in data["themes"].items():
        assert t.get("keywords"), f"{name} has no keywords"
    # Topical routing works.
    r, _ = rank("A grant proposal for a PhD thesis on funding a research plan", data, top=1)
    assert r[0]["theme"] == "scholar", r
    r, _ = rank("Agronomy field trial: soil and fertilizer effects on harvest", data, top=1)
    assert r[0]["theme"] == "terracotta", r
    r, _ = rank("KPI dashboard: quarterly performance metrics and benchmark", data, top=1)
    assert r[0]["theme"] == "dashboard", r
    r, _ = rank("Public engagement and science communication for schools", data, top=1)
    assert r[0]["theme"] == "apricot", r
    # No signal -> default leads.
    r, _ = rank("", data, top=3)
    assert r[0]["theme"] == data["default"], r
    # top honoured
    assert len(rank("food nutrition", data, top=2)[0]) == 2
    print("OK: suggest_theme selftest passed")


def main(argv):
    if "--selftest" in argv:
        selftest(); return 0
    text_parts, top, as_json = [], 3, False
    files = [a for a in argv[1:] if not a.startswith("--")]
    for i, a in enumerate(argv):
        if a == "--text": text_parts.append(argv[i + 1])
        if a in ("--audience", "--doctype"): text_parts.append(argv[i + 1])
        if a == "--top": top = int(argv[i + 1])
        if a == "--json": as_json = True
    for f in files:
        try:
            text_parts.append(open(f, encoding="utf-8", errors="ignore").read())
        except OSError:
            pass
    text = "\n".join(text_parts)
    if not text.strip():
        print("usage: suggest_theme.py [source.md] --text \"...\" [--audience ..] "
              "[--doctype ..] [--top N] [--json] | --selftest")
        return 0
    if as_json:
        ranked, _ = rank(text, None, top)
        print(json.dumps(ranked, ensure_ascii=False, indent=2))
    else:
        print(format_report(text, None, top))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
