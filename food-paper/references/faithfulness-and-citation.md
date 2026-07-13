# Faithfulness & Citation Verification — grounding rules

**The overriding rule for every writing, research, and review agent in this
project: write 100% from true information collected from the literature and the
user's own data. Never invent, guess, or "fill in" anything.** Architecture of
the four-gate check below is informed by the MIT `Light-skills` project (see the
repo README Acknowledgements); wording here is original.

## Grounding principle
Every **claim, number, and citation** in any output must trace to a **real,
verified source** or to the user's supplied data. If it can't be traced, it does
not go in the text — mark it `[UNVERIFIED]` or `[EVIDENCE GAP]` and stop. Do not
resolve a gap from memory.

## Four-gate citation verification
A citation is only usable when it passes, in order:
1. **Existence** — the work exists: its DOI resolves at Crossref or DataCite (or the PMID/arXiv id resolves). A network failure or index miss is **not** proof of non-existence — mark it `UNAVAILABLE`, never invent the work.
2. **Identity** — the metadata (title, authors, year, venue) matches an independent source (PubMed, Semantic Scholar, OpenAlex). A real DOI attached to a **wrong** title/authors/year is a **chimeric citation** — a critical failure; block it.
3. **Publication status** — check for retraction / correction / expression of concern (Crossref `update-to`); never cite a retracted work as valid evidence.
4. **Semantic support** — the source **actually states** the claim, checked at a specific **locator** (section/page/table/figure). Metadata existence is **not** claim support. Abstract-only access cannot support a claim unless the claim is explicitly in the abstract.

**Statuses:** `CONFIRMED` (exists + independent match) · `CONFIRMED-MISSING`
(authorities agree it does not exist) · `UNAVAILABLE` (lookup failed) ·
`UNRESOLVED` (partial evidence only). Only `CONFIRMED` + gate-4 support may back a
claim in the final text.

## Non-negotiable anti-fabrication rules
1. **Never invent** a reference, DOI, author, year, venue, citekey, page/locator, quotation, or support verdict.
2. **Never invent data** — no made-up means, p-values, effect sizes, sample sizes, compositions, or CFU counts. Numbers come from the user's dataset or a cited source; if a source doesn't report a value, write **"not reported"**, never a guess.
3. **Metadata ≠ support.** A work existing does not prove it supports the claim.
4. **Preserve the author's raw citation** until a conflict is confirmed against a registration agency; no fuzzy overwriting.
5. **Don't overstate.** A claim must not generalize beyond what the source tested (matrix, dose, population, in-vitro vs in-vivo).
6. **Quotes are exact** and attributed with a locator; paraphrases stay faithful to the source's meaning and its stated limitations.
7. **Unsupported content is flagged, not shipped** (`[UNVERIFIED]` / `[EVIDENCE GAP]`), and routed back for sourcing.

## Claim ↔ source binding
Maintain, in effect, a claim→source map: each substantive claim lists the
source(s) that support it and the locator. A claim with no bound, gate-4-supported
source cannot appear as a factual statement. This applies to `food-paper`
(`citation_manager`, `draft_writer`), `food-deep-research` (`bibliography`,
`claim_verifier`, `source_verifier`, `compiler`), `food-research`
(`synthesis`/`sr_synthesis`), and `food-review` (`reviewer_integrity`).

## Tooling
Use free sources only (Crossref, DataCite, PubMed, Semantic Scholar, OpenAlex).
`scripts/verify_citations.py` runs a lightweight version of these checks over a
citations file (format + optional online DOI resolution + claim-binding audit).
