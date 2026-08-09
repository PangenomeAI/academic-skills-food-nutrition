#!/usr/bin/env python3
"""Render an SVG preview gallery of the food-ppt themes, so a reviewer can see each
look without opening PowerPoint. Stdlib only.

The mock slides mirror the layout `build_pptx.py` produces (cover, bullets, table)
using each theme's real palette from `food-ppt/templates/themes.json`, so the preview
faithfully represents the built deck. This is a preview only — the real, editable
output comes from `build_pptx.py`.

Usage:
  preview_themes.py --out gallery.svg      # all themes
  preview_themes.py --out one.svg --theme sage
  preview_themes.py --selftest
"""
import html
import json
import os
import sys

SW, SH, GAP = 300, 169, 16          # slide mock size (16:9) + gap
LABEL_W = 96


def themes_path():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(root, "food-ppt", "templates", "themes.json")


def load_all():
    return json.load(open(themes_path(), encoding="utf-8"))


def _rect(x, y, w, h, fill, rx=0):
    return f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" fill="#{fill}" rx="{rx}"/>'


def _text(x, y, s, size, fill, weight="normal", anchor="start", family="sans-serif"):
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-family="{family}" font-size="{size}" '
            f'font-weight="{weight}" fill="#{fill}" text-anchor="{anchor}">{html.escape(s)}</text>')


def cover(ox, oy, t):
    e = [_rect(ox, oy, SW, SH, t["bg"])]
    e.append(_rect(ox, oy, SW, 7, t["accent"]))                       # top brand bar
    e.append(_text(ox + 20, oy + 70, "Antimicrobial Potential", 17, t["accent"], "bold"))
    e.append(_text(ox + 20, oy + 90, "of Polyphenols", 17, t["accent"], "bold"))
    e.append(_rect(ox + 21, oy + 100, 70, 3, t["accent2"]))
    e.append(_text(ox + 20, oy + 122, "Mechanisms & microbial responses", 9, t["ink"]))
    e.append(_text(ox + 20, oy + 136, "Rossi et al. (2025) · Antioxidants", 8, t["muted"]))
    e.append(_rect(ox, oy + SH - 14, SW, 14, t["surface"]))           # bottom band
    return "".join(e)


def bullets(ox, oy, t):
    e = [_rect(ox, oy, SW, SH, t["bg"])]
    e.append(_rect(ox, oy, 4, SH, t["accent"]))                       # left stripe
    e.append(_text(ox + 18, oy + 26, "Key findings", 14, t["accent"], "bold"))
    e.append(_rect(ox + 19, oy + 32, 52, 2, t["accent2"]))
    ys = oy + 56
    for b in ("Bioactive antimicrobial agents", "Hydroxyl groups drive activity",
              "Disrupt membranes & proteins", "Natural preservative potential"):
        e.append(_rect(ox + 19, ys - 7, 6, 6, t["accent"]))
        e.append(_text(ox + 32, ys, b, 9.5, t["ink"]))
        ys += 22
    e.append(_rect(ox + 18, oy + SH - 20, SW - 36, 1, t["surface"]))
    e.append(_text(ox + 18, oy + SH - 9, "Polyphenols · journal club", 7, t["muted"]))
    e.append(_text(ox + SW - 14, oy + SH - 9, "3", 7, t["muted"], anchor="end"))
    return "".join(e)


def table(ox, oy, t):
    e = [_rect(ox, oy, SW, SH, t["bg"]), _rect(ox, oy, 4, SH, t["accent"])]
    e.append(_text(ox + 18, oy + 26, "Mechanisms at a glance", 14, t["accent"], "bold"))
    e.append(_rect(ox + 19, oy + 32, 52, 2, t["accent2"]))
    tx, tw, rh = ox + 18, SW - 36, 20
    rows = [("Target", "Consequence"), ("Cell membrane", "Damage"),
            ("Proteins", "Impaired"), ("Metal ions", "Chelated")]
    for r, (a, b) in enumerate(rows):
        y = oy + 46 + r * rh
        fill = t["accent"] if r == 0 else (t["band"] if r % 2 else t["bg"])
        e.append(_rect(tx, y, tw, rh, fill))
        col = t["onaccent"] if r == 0 else t["ink"]
        wt = "bold" if r == 0 else "normal"
        e.append(_text(tx + 8, y + 13, a, 8.5, col, wt))
        e.append(_text(tx + tw / 2 + 6, y + 13, b, 8.5, col, wt))
    return "".join(e)


def section(ox, oy, t):
    e = [_rect(ox, oy, SW, SH, t["accent"])]
    e.append(_text(ox + 20, oy + SH / 2, "Mechanisms of action", 15, t["onaccent"], "bold"))
    e.append(_rect(ox + 21, oy + SH / 2 + 10, 60, 3, t["accent2"]))
    return "".join(e)


def theme_row(oy, key, t):
    x = LABEL_W
    parts = [_text(10, oy + 22, t["name"], 13, t["ink"], "bold"),
             _text(10, oy + 38, t.get("style", "")[:18], 7.5, t["muted"]),
             _text(10, oy + SH, "#" + t["accent"], 7, t["accent"])]
    for fn in (cover, section, bullets, table):
        parts.append(fn(x, oy, t)); x += SW + GAP
    return "".join(parts), x


def build_svg(data, only=None):
    themes = data["themes"]
    keys = [only] if only else list(themes)
    row_h = SH + 26
    width = LABEL_W + 4 * (SW + GAP)
    height = 40 + row_h * len(keys)
    body = [_rect(0, 0, width, height, "FFFFFF"),
            _text(12, 26, "food-ppt themes — cover · section · bullets · table", 15, "222222", "bold")]
    y = 44
    for k in keys:
        t = {**{"onaccent": "FFFFFF", "band": "F2F2F2"}, **themes[k]}
        row, _ = theme_row(y, k, t)
        body.append(row); y += row_h
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
            f'viewBox="0 0 {width} {height}">' + "".join(body) + "</svg>")


def selftest():
    data = load_all()
    assert data["themes"] and data.get("default") in data["themes"]
    svg = build_svg(data)
    assert svg.startswith("<svg") and svg.rstrip().endswith("</svg>")
    assert all(("#" + data["themes"][k]["accent"]) in svg for k in data["themes"])
    assert build_svg(data, only="sage").count("food-ppt themes") == 1
    print("OK: preview_themes selftest passed")


def main(argv):
    if "--selftest" in argv:
        selftest(); return 0
    out = only = None
    for i, a in enumerate(argv):
        if a == "--out": out = argv[i + 1]
        if a == "--theme": only = argv[i + 1]
    if not out:
        print("usage: preview_themes.py --out gallery.svg [--theme <name>] | --selftest")
        return 1
    open(out, "w", encoding="utf-8").write(build_svg(load_all(), only))
    print(f"OK: wrote {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
