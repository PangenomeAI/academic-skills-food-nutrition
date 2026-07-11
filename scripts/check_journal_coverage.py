#!/usr/bin/env python3
"""Verify journals/_coverage.md maps all 60 target journals to existing skill folders.

Run: python3 scripts/check_journal_coverage.py
Exits non-zero if the count is wrong or any referenced folder is missing.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
JOURNALS = ROOT / "journals"
COVERAGE = JOURNALS / "_coverage.md"

EXPECTED = 60


def main() -> int:
    rows = []
    for line in COVERAGE.read_text().splitlines():
        m = re.match(r"\|\s*(\d+)\s*\|(.+)\|(.+)\|(.+)\|\s*([a-z0-9-]+)\s*\|", line)
        if m:
            rows.append((int(m.group(1)), m.group(5).strip()))

    if len(rows) != EXPECTED:
        print(f"FAIL: expected {EXPECTED} journal rows, found {len(rows)}")
        return 1

    numbers = sorted(n for n, _ in rows)
    if numbers != list(range(1, EXPECTED + 1)):
        print(f"FAIL: journal numbers are not 1..{EXPECTED}: {numbers}")
        return 1

    missing = sorted({f for _, f in rows if not (JOURNALS / f / "SKILL.md").exists()})
    if missing:
        print(f"FAIL: skill folders missing SKILL.md: {missing}")
        return 1

    folders = sorted({f for _, f in rows})
    print(f"OK: {len(rows)} journals mapped to {len(folders)} skill folders, all present.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
