# Access Routing

How `access_router` picks a lawful route for one article. The ladder is cheapest-and-
most-legal first; stop at the first that yields the real full text.

## Decide
1. **Normalize + identify.** Resolve to a DOI (Crossref title search if only a title).
   Run `python3 scripts/resolve_oa.py <doi>` → `{is_oa, pdf_url, landing_url, source}`.
2. **Route:**

| Condition | Route | Agent |
|---|---|---|
| `is_oa: true`, or a known legal OA/preprint URL | **Open access** (download it) | `oa_fetcher` |
| Reference is in the user's EndNote/Zotero/Mendeley library | **Library PDF** | `library_fetcher` |
| Paywalled **and** the user opted into institutional access | **Institutional** (their own session) | `institutional_fetcher` |
| Paywalled, no access route available | stop → `oa_not_found`; tell the user, offer to add a library/PDF | — |

## Rules
- **Open access is always fetched and read** — never routed to abstract-level when a
  legal PDF exists. This is the fix for "read the reference list but not the papers".
- A resolving DOI is **not** proof of entitlement, and OA status must be **resolved**,
  never guessed.
- Prefer the **PMC / Europe PMC** HTML full text for reading an OA article's text — it
  avoids the publisher consent/auth gates that block a simple fetch
  (`food-research/references/full-text-access.md`).
- Publisher matters only for the institutional route (which library link to expect);
  there is **no publisher-API key handling** in this skill — API keys are a separate,
  user-managed concern and out of scope here.
- Chinese-language sources and CNKI are **out of scope** for the food/nutrition/
  agriculture suite; route those to the user.
