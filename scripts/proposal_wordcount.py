#!/usr/bin/env python3
"""Check a proposal draft against a funding scheme's length limit. Stdlib only.

Reads a Markdown draft (headings as `#`/`##`…), counts words per section, and compares
the total (or, for schemes that count only some sections, just those) against the
scheme's limit in `food-proposal/schemes/schemes.json`. Page limits are reported as a
word-based estimate — always confirm the real page count in the scheme's template.

Usage:
  proposal_wordcount.py draft.md --scheme uom-major-minor-project
  proposal_wordcount.py draft.md --words 1500 --tolerance 150
  proposal_wordcount.py --selftest

Exit 0 within limit; 1 over limit / usage error.
"""
import json
import os
import re
import sys

HEADING = re.compile(r"^\s{0,3}#{1,6}\s+(.+?)\s*#*\s*$")


def schemes_path():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(root, "food-proposal", "schemes", "schemes.json")


def load_scheme(scheme_id):
    data = json.load(open(schemes_path(), encoding="utf-8"))
    return data["schemes"][scheme_id]


def count_words(text):
    return len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'\-]*", text))


def sections(md):
    """Return [(heading, body_words)] split on Markdown headings."""
    out, cur, buf = [], None, []
    for line in md.splitlines():
        m = HEADING.match(line)
        if m:
            if cur is not None:
                out.append((cur, count_words("\n".join(buf))))
            cur, buf = m.group(1).strip(), []
        else:
            buf.append(line)
    if cur is not None:
        out.append((cur, count_words("\n".join(buf))))
    return out


def _matches(heading, counted):
    h = heading.lower()
    return any(c.lower() in h for c in counted)


def check(md, scheme=None, words=None, tolerance=0):
    secs = sections(md)
    total = sum(w for _, w in secs)
    counted = (scheme or {}).get("counted_sections")
    if counted:
        counted_total = sum(w for h, w in secs if _matches(h, counted))
    else:
        counted_total = total

    report = {"sections": secs, "total_words": total, "counted_words": counted_total}
    if scheme and scheme.get("limit_type") == "pages":
        wpp = scheme.get("words_per_page", 650)
        report["limit_type"] = "pages"
        report["page_limit"] = scheme["limit_value"]
        report["est_pages"] = round(total / wpp, 1)
        report["over"] = report["est_pages"] > scheme["limit_value"]
        report["word_proxy"] = scheme["limit_value"] * wpp
    else:
        limit = (scheme or {}).get("limit_value", words)
        tol = (scheme or {}).get("tolerance", tolerance) or 0
        report["limit_type"] = "words"
        report["word_limit"] = limit
        report["tolerance"] = tol
        report["over"] = (limit is not None) and counted_total > (limit + tol)
        report["under"] = (limit is not None) and counted_total < (limit - tol)
    return report


def selftest():
    md = ("# Abstract\nalpha beta gamma delta\n"
          "# Introduction\n" + " ".join(["w"] * 20) + "\n"
          "# Methods\n" + " ".join(["m"] * 50) + "\n")
    secs = dict(sections(md))
    assert secs["Abstract"] == 4 and secs["Introduction"] == 20 and secs["Methods"] == 50
    # counted-sections scheme: Methods excluded
    sch = {"limit_type": "words", "limit_value": 30, "tolerance": 5,
           "counted_sections": ["Abstract", "Introduction"]}
    r = check(md, sch)
    assert r["counted_words"] == 24 and r["total_words"] == 74
    assert r["over"] is False and r["under"] is True     # 24 < 30-5? no: 24<25 -> under
    sch2 = {"limit_type": "words", "limit_value": 10, "tolerance": 2,
            "counted_sections": ["Abstract", "Introduction"]}
    assert check(md, sch2)["over"] is True               # 24 > 12
    # page scheme
    pg = check(md, {"limit_type": "pages", "limit_value": 1, "words_per_page": 50})
    assert pg["est_pages"] == round(74 / 50, 1) and pg["over"] is True
    # real schemes.json loads
    assert load_scheme("arc-discovery-eoi")["limit_type"] == "pages"
    print("OK: proposal_wordcount selftest passed")


def main(argv):
    if "--selftest" in argv:
        selftest(); return 0
    args = [a for a in argv[1:] if not a.startswith("--")]
    scheme_id = words = None; tol = 0
    for i, a in enumerate(argv):
        if a == "--scheme": scheme_id = argv[i + 1]
        if a == "--words": words = int(argv[i + 1])
        if a == "--tolerance": tol = int(argv[i + 1])
    if not args:
        print("usage: proposal_wordcount.py draft.md --scheme <id> | --words N [--tolerance T] | --selftest")
        return 1
    md = open(args[0], encoding="utf-8").read()
    scheme = load_scheme(scheme_id) if scheme_id else None
    r = check(md, scheme, words, tol)
    print("Per-section word count:")
    for h, w in r["sections"]:
        print(f"  {w:>6}  {h}")
    if r["limit_type"] == "pages":
        print(f"\nTotal words: {r['total_words']}  (~{r['est_pages']} A4 pages @ "
              f"{scheme.get('words_per_page',650)} w/pg; limit {r['page_limit']} pages)")
        print("VERDICT:", "OVER — trim" if r["over"] else "within estimate — confirm real page count in the template")
    else:
        lim = r.get("word_limit")
        base = r["counted_words"] if scheme and scheme.get("counted_sections") else r["total_words"]
        note = " (counted sections only)" if scheme and scheme.get("counted_sections") else ""
        print(f"\nCounted words: {base}{note}  (limit {lim} ± {r.get('tolerance',0)})")
        print("VERDICT:", "OVER — trim" if r.get("over") else ("UNDER — expand" if r.get("under") else "within limit"))
    return 1 if r.get("over") else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
