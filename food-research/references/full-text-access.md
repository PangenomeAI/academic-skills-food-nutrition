# Getting the Full Text of a Cited Paper

Canonical retrieval policy for any agent that must **read the actual article**, not
just its abstract: `knowledge_builder` (Pathway A), `food-research` /
`food-deep-research` (`source_verifier`, `investigator`), and the `agri-*` equivalents.

## Why full text is often not reachable
In an AI agent environment you can freely reach **metadata and abstracts** (Crossref,
OpenAlex, Semantic Scholar, PubMed, Europe PMC) and **open-access full text**. But a
manuscript's reference list is mostly **DOIs and titles, not PDFs**, and **most
published articles are paywalled** — there is no institutional login by default. So
an honest agent will read what it can and **mark the rest as unretrieved**. That is
correct (never summarize a paper you did not read), but it is not the end of the
options below.

## Retrieval ladder — try in order, per cited source
1. **Open-access copy (free, legitimate).**
   - **Europe PMC** / **PMC** full-text (`europepmc.org`, `ncbi.nlm.nih.gov/pmc`).
   - **Unpaywall** via the DOI (`api.unpaywall.org/v2/<doi>?email=…`) and OpenAlex
     `open_access.oa_url` — both point to the legal free version if one exists.
   - **Preprint servers:** bioRxiv, agriRxiv, arXiv, ChemRxiv, Research Square.
   - The **publisher's free HTML** (many OA and hybrid-OA articles).
2. **A connected full-text tool/MCP,** if the user has one enabled — e.g. a PubMed
   full-text tool (works for PMC-OA), Europe PMC, or a publisher/library connector.
   Prefer these over scraping; they are cleaner and rights-cleared.
3. **Green OA / author copies** in an **institutional repository** (university
   library, CORE, OpenAIRE). Prefer the version of record; note when it is an
   accepted manuscript.
4. **User-supplied PDFs (most reliable for paywalled work).** Ask the user to place
   the cited PDFs in the working folder or attach them; then read those directly
   (`docx`/`pdf` tooling). See "When to ask the user" below.
5. **Institutional access via a logged-in browser session** the user drives (their
   library/VPN in Claude-in-Chrome, or a downloader that reuses an institutional
   login). This is **user-initiated** — the agent does not log in on its own.

**Legitimate access only.** Use OA copies, a genuine institutional entitlement, or
files the user provides. **Never bypass a paywall, share credentials, or scrape
against a site's terms.** If none of the above reaches it, the source stays
**unretrieved** — mark it, do not invent its contents.

## When to ask the user (escalate, don't silently degrade)
Read every source you can via the ladder first. Then judge by **importance**:
- **Load-bearing citations** — the ones the manuscript's central claims or the
  reviewer's key concerns depend on — that remain paywalled: **surface one
  consolidated request**, e.g. *"5 of the sources behind the main claims are
  paywalled (DOIs …). To audit them properly, drop the PDFs in this folder, or
  enable a full-text/library tool. Otherwise I'll assess those claims at
  abstract-level and flag them as unverified."* Do **not** prompt per paper.
- **Peripheral citations** — abstract-level is acceptable; record the limitation and
  move on.

## Report the access state (transparency)
In the knowledge base / source audit, for each source record the **access route**
(OA · connected tool · user PDF · abstract-only · unretrieved) so the review is
reproducible and its limits are honest. In `## Coverage & limits`, state how many of
the load-bearing citations were read in full versus abstract-only, so the author
knows exactly how deep the grounding goes.

## What the user can enable for deeper access
If reviews routinely need paywalled full text, any **one** of these removes the
limitation, in rough order of ease:
1. **Drop the cited PDFs into the project folder** (zero setup, always works).
2. **Connect a literature MCP/connector** that returns full text (PubMed full-text,
   Europe PMC, a publisher or library connector).
3. **Use a logged-in institutional browser session** (library proxy / VPN) via
   Claude-in-Chrome so entitled articles resolve.
Metadata, abstracts, and open-access full text already work with no setup.
