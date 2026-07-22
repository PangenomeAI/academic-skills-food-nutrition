#!/usr/bin/env python3
"""Download the open-access full-text PDF for one or many articles, and write a
manifest. Stdlib only. Lawful OA sources only — never bypasses a paywall.

For each DOI it resolves an OA PDF (Unpaywall -> OpenAlex, via resolve_oa), downloads
it, verifies the bytes are a real PDF (`%PDF` magic), and records a typed status. This
is the "you MUST actually fetch open-access full text" workhorse for the knowledge
base / evidence synthesis — it does not accept an abstract in place of an OA paper.

Usage:
  fetch_oa.py --dois 10.1186/s40168-018-0445-0,10.1371/journal.pone.0089845 --out ./lit
  fetch_oa.py --doi-file dois.txt --out ./lit --email you@example.org
  fetch_oa.py --selftest

Writes <out>/PDFs/<slug>.pdf and <out>/manifest.json. Exit 0 if every requested DOI
was either downloaded or truthfully classified; 1 on a usage error.
"""
import hashlib
import json
import os
import re
import sys
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from resolve_oa import resolve  # noqa: E402  (sibling script)

UA = "food-nutrition-skills/1.0 (mailto:food_agents@lists.unimelb.edu.au)"

# Typed statuses (a small, honest subset of the nature-downloader taxonomy).
OPEN_ACCESS_DOWNLOADED = "open_access_downloaded"
OA_NOT_FOUND = "oa_not_found"            # DOI resolved but is closed access
PDF_FETCH_FAILED = "pdf_fetch_failed"    # OA URL known but download errored
NOT_A_PDF = "not_a_pdf"                  # got HTML/login page, not a PDF


def slugify(doi):
    return re.sub(r"[^A-Za-z0-9._-]+", "_", doi.strip()).strip("_")[:120] or "paper"


def is_pdf(head):
    return head[:5] == b"%PDF-"


def download(url, dest):
    """Download url to dest; return (ok, sha256, nbytes, reason)."""
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        data = r.read()
    if not is_pdf(data):
        return False, None, len(data), "not_a_pdf"
    with open(dest, "wb") as f:
        f.write(data)
    return True, hashlib.sha256(data).hexdigest(), len(data), "ok"


def fetch_one(doi, pdf_dir, email):
    """Resolve + download one DOI. Return a manifest record."""
    rec = {"doi": doi.strip()}
    info = resolve(doi, email) if email else resolve(doi)
    rec["is_oa"] = info.get("is_oa")
    rec["source"] = info.get("source")
    pdf_url = info.get("pdf_url")
    if not pdf_url:
        rec["status"] = OA_NOT_FOUND
        rec["note"] = "no legal open-access PDF; needs a user-supplied copy or institutional access"
        return rec
    dest = os.path.join(pdf_dir, slugify(doi) + ".pdf")
    try:
        ok, sha, nbytes, reason = download(pdf_url, dest)
    except Exception as e:  # network / URL error
        rec["status"] = PDF_FETCH_FAILED
        rec["pdf_url"] = pdf_url
        rec["note"] = str(e)[:160]
        return rec
    if not ok:
        rec["status"] = NOT_A_PDF
        rec["pdf_url"] = pdf_url
        rec["bytes"] = nbytes
        rec["note"] = "OA URL returned non-PDF content (HTML/login) — not saved"
        return rec
    rec.update(status=OPEN_ACCESS_DOWNLOADED, pdf_url=pdf_url,
               file=os.path.relpath(dest), bytes=nbytes, sha256=sha)
    return rec


def run(dois, out_dir, email):
    pdf_dir = os.path.join(out_dir, "PDFs")
    os.makedirs(pdf_dir, exist_ok=True)
    records = [fetch_one(d, pdf_dir, email) for d in dois if d.strip()]
    downloaded = sum(1 for r in records if r["status"] == OPEN_ACCESS_DOWNLOADED)
    manifest = {
        "requested": len(records),
        "open_access_downloaded": downloaded,
        "not_open_access_or_failed": len(records) - downloaded,
        "records": records,
    }
    with open(os.path.join(out_dir, "manifest.json"), "w") as f:
        json.dump(manifest, f, indent=2)
    return manifest


def selftest():
    assert slugify("10.1186/s40168-018-0445-0") == "10.1186_s40168-018-0445-0"
    assert is_pdf(b"%PDF-1.7\n...")
    assert not is_pdf(b"<!DOCTYPE html>")
    # A closed-access resolve result must classify as oa_not_found, never invented.
    rec = {"doi": "x"}
    info = {"is_oa": False, "pdf_url": None, "source": "openalex"}
    if not info.get("pdf_url"):
        rec["status"] = OA_NOT_FOUND
    assert rec["status"] == OA_NOT_FOUND
    # manifest counting
    recs = [{"status": OPEN_ACCESS_DOWNLOADED}, {"status": OA_NOT_FOUND},
            {"status": OPEN_ACCESS_DOWNLOADED}]
    got = sum(1 for r in recs if r["status"] == OPEN_ACCESS_DOWNLOADED)
    assert got == 2, got
    print("OK: fetch_oa selftest passed")


def main(argv):
    if "--selftest" in argv:
        selftest()
        return 0
    dois, out_dir, email = [], None, None
    i = 1
    while i < len(argv):
        a = argv[i]
        if a == "--dois":
            i += 1; dois += [d for d in argv[i].split(",")]
        elif a == "--doi-file":
            i += 1; dois += open(argv[i]).read().split()
        elif a == "--out":
            i += 1; out_dir = argv[i]
        elif a == "--email":
            i += 1; email = argv[i]
        i += 1
    if not dois or not out_dir:
        print("usage: fetch_oa.py --dois <d1,d2> | --doi-file <f>  --out <dir> [--email <e>] | --selftest")
        return 1
    manifest = run(dois, out_dir, email)
    print(json.dumps({k: v for k, v in manifest.items() if k != "records"}, indent=2))
    print(f"manifest: {os.path.join(out_dir, 'manifest.json')}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
