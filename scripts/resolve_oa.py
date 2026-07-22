#!/usr/bin/env python3
"""Resolve a DOI to a legal open-access PDF URL (Unpaywall + OpenAlex). Stdlib only.

An agent building a review's knowledge base can call this to find the free full text
of a cited paper without any connected literature tool. It returns the OA PDF URL
when a legitimate one exists; it does **not** crack paywalls — no OA copy means the
source must come from a user-supplied PDF or institutional access
(see food-research/references/full-text-access.md).

Usage:
  resolve_oa.py 10.1016/j.foodchem.2023.135000 --email you@example.org
  resolve_oa.py --selftest

Prints a small JSON object: {doi, is_oa, pdf_url, landing_url, source}. Exit code is
0 if an OA PDF URL was found, 3 if the DOI resolved but has no OA copy, 1 on error.
"""
import json
import sys
import urllib.parse
import urllib.request

UA = "food-nutrition-skills/1.0 (mailto:food_agents@lists.unimelb.edu.au)"


def _get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=15) as r:
        return json.loads(r.read().decode("utf-8"))


def parse_unpaywall(data):
    """Return (pdf_url, landing_url, is_oa) from an Unpaywall v2 record."""
    loc = data.get("best_oa_location") or {}
    return loc.get("url_for_pdf"), loc.get("url"), bool(data.get("is_oa"))


def parse_openalex(data):
    """Return (pdf_url, landing_url, is_oa) from an OpenAlex work record."""
    oa = data.get("open_access") or {}
    best = data.get("best_oa_location") or {}
    pdf = best.get("pdf_url") or oa.get("oa_url")
    landing = best.get("landing_page_url") or oa.get("oa_url")
    return pdf, landing, bool(oa.get("is_oa"))


def resolve(doi, email="food_agents@lists.unimelb.edu.au"):
    doi = doi.strip().replace("https://doi.org/", "")
    # 1. Unpaywall — purpose-built for the OA-PDF question.
    try:
        pdf, landing, is_oa = parse_unpaywall(
            _get(f"https://api.unpaywall.org/v2/{urllib.parse.quote(doi)}?email={email}"))
        if pdf:
            return {"doi": doi, "is_oa": is_oa, "pdf_url": pdf,
                    "landing_url": landing, "source": "unpaywall"}
    except Exception:
        pass
    # 2. OpenAlex — second opinion, also gives a landing page when there's no PDF.
    try:
        pdf, landing, is_oa = parse_openalex(
            _get(f"https://api.openalex.org/works/doi:{urllib.parse.quote(doi)}"))
        return {"doi": doi, "is_oa": is_oa, "pdf_url": pdf,
                "landing_url": landing, "source": "openalex"}
    except Exception as e:
        return {"doi": doi, "is_oa": False, "pdf_url": None,
                "landing_url": None, "source": None, "error": str(e)}


def selftest():
    # Parsing is the only non-trivial logic; test it offline with canned payloads.
    uw = {"is_oa": True, "best_oa_location":
          {"url_for_pdf": "https://example.org/paper.pdf", "url": "https://example.org/paper"}}
    assert parse_unpaywall(uw) == ("https://example.org/paper.pdf",
                                   "https://example.org/paper", True)
    assert parse_unpaywall({"is_oa": False, "best_oa_location": None}) == (None, None, False)

    oax = {"open_access": {"is_oa": True, "oa_url": "https://ex.org/x"},
           "best_oa_location": {"pdf_url": "https://ex.org/x.pdf",
                                "landing_page_url": "https://ex.org/x"}}
    assert parse_openalex(oax) == ("https://ex.org/x.pdf", "https://ex.org/x", True)
    # Closed access: no PDF, not OA — must not fabricate a URL.
    assert parse_openalex({"open_access": {"is_oa": False, "oa_url": None},
                           "best_oa_location": None}) == (None, None, False)
    print("OK: resolve_oa selftest passed")


def main(argv):
    if "--selftest" in argv:
        selftest()
        return 0
    args = [a for a in argv[1:] if not a.startswith("--")]
    if not args:
        print("usage: resolve_oa.py <doi> [--email you@example.org] | --selftest")
        return 1
    email = "food_agents@lists.unimelb.edu.au"
    for a in argv:
        if a.startswith("--email="):
            email = a.split("=", 1)[1]
    res = resolve(args[0], email)
    print(json.dumps(res, indent=2))
    return 0 if res.get("pdf_url") else 3


if __name__ == "__main__":
    sys.exit(main(sys.argv))
