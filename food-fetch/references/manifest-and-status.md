# Manifest & Status

Every food-fetch run returns **one manifest** covering **every** requested reference,
so the calling skill's grounding is honest and auditable. `scripts/fetch_oa.py` writes
the open-access part of it automatically (`<out>/manifest.json`); the coordinator
merges the library and institutional results into the same shape.

## Per-reference record
```
- ref: <AuthorYear or citation key>
  doi: <doi>              # or pmid / url / title
  status: <one of the statuses below>
  route: open_access | library_pdf | institutional | user_pdf | none
  file: <relative path>  # when downloaded/matched
  bytes: <n>             # when downloaded
  sha256: <hash>         # when downloaded
  note: <short reason, for anything not read in full>
```

## Statuses
- **`open_access_downloaded`** — a legal OA PDF was downloaded and verified (`%PDF`).
- **`library_pdf_read`** — matched and read from the user's reference-manager library.
- **`institutional_downloaded`** — obtained via the user's own entitled session.
- **`full_text_html_available`** — readable HTML full text (e.g. PMC) but no
  downloadable PDF; still a full-text read.
- **`oa_not_found`** — DOI resolved but closed access, and no user copy/entitlement.
- **`library_no_permission`** — the institution has no entitlement (resolver said so).
- **`pdf_fetch_failed`** — an OA/entitled URL was known but the download errored.
- **`not_a_pdf`** — the URL returned HTML/login, not a PDF (not saved, not "read").
- **`abstract_only`** — only the abstract could be read; the paper was not obtained.

## Summary line (required)
End with: **"N of M references read in full (K open access, L from your library, P via
your library subscription); Q abstract-only, R unavailable."** This is the coverage
statement the review/synthesis carries so no source is silently overclaimed.

## Honesty rule
A reference with any status other than `*_downloaded` / `*_read` /
`full_text_html_available` was **not read in full** and must be treated as such by the
caller — never summarized as if the paper had been read
(`food-paper/references/faithfulness-and-citation.md`).
