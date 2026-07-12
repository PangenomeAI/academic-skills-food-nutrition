#!/usr/bin/env python3
"""Privacy scan — flag confidential/local info in an AI-produced deliverable.

Before any document (manuscript, brief, figure legend, response letter, report)
is handed to the user, scan it for things that should not leak: local filesystem
paths, usernames, machine/temp paths, emails, IP addresses, and API tokens.

Usage:
  python privacy_scan.py FILE            # scan a file
  python privacy_scan.py < FILE          # scan stdin
  python privacy_scan.py --selftest

Exit code is non-zero if anything is flagged. This is a safety net, not a
substitute for review — see food-paper/references/privacy-and-confidentiality.md.
"""
import re
import sys

# Emails that are public project contacts (not confidential) — do not flag.
ALLOW_EMAILS = {"food_agents@lists.unimelb.edu.au"}

PATTERNS = [
    ("local home path (macOS)", re.compile(r"/Users/[^/\s\"']+")),
    ("local home path (Linux)", re.compile(r"/home/[^/\s\"']+")),
    ("root path", re.compile(r"/root/[^\s\"']*")),
    ("Windows user path", re.compile(r"[A-Za-z]:\\Users\\[^\\\s\"']+")),
    ("macOS temp path (/var/folders)", re.compile(r"/var/folders/[^\s\"']+")),
    ("temp/scratchpad path", re.compile(r"/private/tmp/[^\s\"']+|/tmp/[^\s\"']+")),
    ("IP address", re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")),
    ("API token / secret", re.compile(
        r"\b(?:sk-[A-Za-z0-9]{16,}|gh[oprsu]_[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|xox[baprs]-[A-Za-z0-9-]+)\b")),
]
EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")


def scan(text):
    """Return a list of (line_no, category, snippet)."""
    hits = []
    for i, line in enumerate(text.splitlines(), 1):
        for label, pat in PATTERNS:
            for m in pat.finditer(line):
                hits.append((i, label, m.group(0)))
        for m in EMAIL_RE.finditer(line):
            if m.group(0).lower() not in ALLOW_EMAILS:
                hits.append((i, "email address", m.group(0)))
    return hits


def selftest():
    bad = ("See /Users/alice/project/main.tex for the draft.\n"
           "Contact bob@example.com or 192.168.0.5.\n"
           "token gho_ABCDEFGHIJKLMNOPQRSTUVWXYZ0123 leaked\n"
           "temp at /private/tmp/claude-502/scratchpad/x")
    h = scan(bad)
    cats = {c for _, c, _ in h}
    assert "local home path (macOS)" in cats, cats
    assert "email address" in cats, cats
    assert "IP address" in cats, cats
    assert "API token / secret" in cats, cats
    assert "temp/scratchpad path" in cats, cats

    clean = ("The coating reduced weight loss by 23% (p < 0.05).\n"
             "Questions: food_agents@lists.unimelb.edu.au. DOI 10.1016/j.foodchem.2023.1\n"
             "Version 1.14.0 released.")
    assert scan(clean) == [], scan(clean)
    print("OK: privacy_scan selftest passed")


def main(argv):
    if "--selftest" in argv:
        selftest()
        return 0
    args = [a for a in argv[1:] if not a.startswith("--")]
    text = open(args[0], encoding="utf-8").read() if args else sys.stdin.read()
    hits = scan(text)
    if hits:
        print(f"FAIL: {len(hits)} potential privacy leak(s) — redact before delivering:")
        for ln, cat, snip in hits:
            print(f"  ✗ line {ln}: {cat}: {snip}")
        return 1
    print("OK: no local paths, secrets, IPs, or non-project emails found.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
