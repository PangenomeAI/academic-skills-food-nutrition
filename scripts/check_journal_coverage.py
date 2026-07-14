#!/usr/bin/env python3
"""Verify the journal coverage maps point to existing skill folders.

- journals/_coverage.md must map exactly 60 food journals (numbered 1..60).
- journals/_coverage_nutrition.md maps the nutrition journals (contiguous 1..N).
Every referenced folder must contain a SKILL.md.

Run: python3 scripts/check_journal_coverage.py
Exits non-zero on any problem.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
JOURNALS = ROOT / "journals"
ROW = re.compile(r"\|\s*(\d+)\s*\|(.+)\|(.+)\|(.+)\|\s*([a-z0-9-]+)\s*\|")


def parse(path: pathlib.Path):
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        m = ROW.match(line)
        if m:
            rows.append((int(m.group(1)), m.group(5).strip()))
    return rows


def check(path, expected):
    rows = parse(path)
    if not rows:
        print(f"FAIL: no rows parsed from {path.name}")
        return 1
    numbers = sorted(n for n, _ in rows)
    if numbers != list(range(1, len(rows) + 1)):
        print(f"FAIL: {path.name} numbers not contiguous 1..{len(rows)}: {numbers}")
        return 1
    if expected is not None and len(rows) != expected:
        print(f"FAIL: {path.name} expected {expected} rows, found {len(rows)}")
        return 1
    missing = sorted({f for _, f in rows if not (JOURNALS / f / "SKILL.md").exists()})
    if missing:
        print(f"FAIL: {path.name} references folders with no SKILL.md: {missing}")
        return 1
    folders = sorted({f for _, f in rows})
    print(f"OK: {path.name} — {len(rows)} journals mapped to {len(folders)} folders, all present.")
    return 0


def main() -> int:
    rc = check(JOURNALS / "_coverage.md", expected=60)
    rc |= check(JOURNALS / "_coverage_nutrition.md", expected=None)
    rc |= check(JOURNALS / "_coverage_multidisciplinary.md", expected=None)
    return rc


if __name__ == "__main__":
    sys.exit(main())
