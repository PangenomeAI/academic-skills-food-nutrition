# Getting the Full Text of an Article

Canonical retrieval policy for any agent that must **read the actual article**, not
just its abstract. It applies to **two situations**, with the same ladder but
different realistic routes:

- **(A) Papers the manuscript already cites** — `knowledge_builder` **Pathway A**;
  `food-paper`/`food-review` integrity checks. The user's **reference-manager
  library** is the best source here — they cited these, so they usually have the PDFs.
- **(B) Field literature the manuscript does *not* cite**, discovered to build a
  broader knowledge base — `knowledge_builder` **Pathway B**; `food-research`
  (`source_scout` discovers → `screener_appraiser` Phase B / `data_extractor` read);
  `food-deep-research` (`investigator` Pass 1 discovers → Pass 2 reads). Here the
  user's library usually **won't** have the paper (it wasn't cited), so the realistic
  routes are **open access (`resolve_oa.py`/PMC) and connected literature tools**, and
  — as in any screening — you **full-text-read only the key subset** (key reviews and
  the closest prior work / novelty-map candidates); the rest are screened at
  abstract/metadata level, which is expected and fine for a field scan.

The `agri-*` skills inherit this via delegation.

## Why full text is often not reachable
In an AI agent environment you can freely reach **metadata and abstracts** (Crossref,
OpenAlex, Semantic Scholar, PubMed, Europe PMC) and **open-access full text**. But a
manuscript's reference list is mostly **DOIs and titles, not PDFs**, and **most
published articles are paywalled** — there is no institutional login by default. So
an honest agent will read what it can and **mark the rest as unretrieved**. That is
correct (never summarize a paper you did not read), but it is not the end of the
options below.

## Ask for full-text access up front (highlighted request)
Any skill that builds a knowledge base or evidence synthesis **needs the full text**,
not abstracts. Before the heavy work, surface **one prominent, highlighted request**
in the chat (a bold blockquote callout) so the user can unlock deep access. **Reading
PDFs from a folder path the user gives is exactly how Claude accesses local files —
this is the correct method**, in Claude Code and in Cowork (add the folder to the
project). Use this template, adapting the wording:

> 📚 **To ground this in the actual literature — not just abstracts — I need access to
> the full-text articles.** Please provide **one** of:
> - the path to your **EndNote library's `.Data` folder** (or Zotero `storage/` /
>   Mendeley folder) — I'll read the PDFs you've already downloaded, **read-only**;
> - a **folder of PDFs** for the key references; or
> - reply **"open-access only"** and I'll use open-access full text + abstracts, and
>   **flag every paywalled source as read at abstract-level (unverified)**.

Ask **once, up front**, and proceed as soon as the user answers (don't block on it —
if they decline, continue at open-access + abstract level and say so in the output's
coverage note). If they give a folder, confirm what you found (e.g. "read 34 PDFs
from your EndNote library") so access is transparent.

## Retrieval ladder — try in order, per cited source
1. **Open-access copy (free, legitimate).**
   - **Europe PMC** / **PMC** full-text (`europepmc.org`, `pmc.ncbi.nlm.nih.gov`).
     **Prefer this for reading an OA article's text** — it serves clean HTML full
     text without the consent/auth gates that publisher sites often use.
   - **Unpaywall** via the DOI (`api.unpaywall.org/v2/<doi>?email=…`) and OpenAlex
     `open_access.oa_url` — both point to the legal free version if one exists.
   - **Preprint servers:** bioRxiv, agriRxiv, arXiv, ChemRxiv, Research Square.
   - The **publisher's free HTML** (many OA and hybrid-OA articles) — but note that
     even for an OA article the publisher page may **redirect through a cookie-consent
     or auth IdP that a simple web-fetch can't clear** (e.g. BMC → SpringerLink). That
     is not a paywall; when it happens, read the **PMC / Europe PMC mirror** instead of
     giving up on the article.
2. **A connected full-text tool/MCP,** if the user has one enabled — e.g. a PubMed
   full-text tool (works for PMC-OA), Europe PMC, or a publisher/library connector.
   Prefer these over scraping; they are cleaner and rights-cleared.
3. **Green OA / author copies** in an **institutional repository** (university
   library, CORE, OpenAIRE). Prefer the version of record; note when it is an
   accepted manuscript.
4. **User-supplied PDFs (most reliable for paywalled work).** Ask the user to place
   the cited PDFs in the working folder or attach them; then read those directly
   (the `pdf` skill / built-in PDF reading). See "When to ask the user" below.
   - **A reference manager's local library is exactly this — a folder of already-
     downloaded PDFs.** If the user gives access to their **EndNote** library, the
     attached full text lives under `<Library>.Data/PDF/` (many randomly-named
     subfolders, one PDF each); **Zotero** keeps them under `Zotero/storage/<KEY>/`,
     and **Mendeley** in its watched/`Downloaded` folder. Point Claude at that folder,
     then map each cited reference to its PDF by the DOI or title on the PDF's first
     page (or its filename) and read it. This turns the user's own library into a
     high-coverage, fully-legal full-text source — see "Connecting a reference
     manager" below.
5. **Institutional access via a logged-in browser session** the user drives (their
   library/VPN in Claude-in-Chrome, or a downloader that reuses an institutional
   login). This is **user-initiated** — the agent does not log in on its own.

**Legitimate access only.** Use OA copies, a genuine institutional entitlement, or
files the user provides. **Never bypass a paywall, share credentials, or scrape
against a site's terms.** If none of the above reaches it, the source stays
**unretrieved** — mark it, do not invent its contents.

## API endpoints you can fetch directly (no connected tool needed)
When no literature MCP is connected, the agent can still resolve open access with the
**built-in web-fetch tool** over these public REST APIs. They return metadata,
abstracts, and — crucially — **the URL of the legal free PDF when one exists**. None
of them returns paywalled full text; that still needs a user PDF or institutional
access.

| Purpose | Endpoint (substitute the DOI, URL-encoded) | Gives you |
|---|---|---|
| **OA PDF location** | `https://api.unpaywall.org/v2/<doi>?email=<email>` | `best_oa_location.url_for_pdf` — the legal free PDF, if any |
| **OA + metadata + refs** | `https://api.openalex.org/works/doi:<doi>` | `open_access.oa_url`, `primary_location`, abstract, referenced works |
| **Metadata + license** | `https://api.crossref.org/works/<doi>` | title / authors / year, `license`, `link` (OA full-text links) |
| **Abstract + OA PDF** | `https://api.semanticscholar.org/graph/v1/paper/DOI:<doi>?fields=title,abstract,openAccessPdf` | abstract + `openAccessPdf.url` |
| **Full text (OA only)** | `https://www.ebi.ac.uk/europepmc/webservices/rest/<SRC>/<ID>/fullTextXML` | full-text XML for Europe PMC / PMC-OA articles |
| **Find ID from a title** | `https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=<title>&format=json` | the source + ID when you only have a title |
| **PubMed lookup** | NCBI E-utilities `esearch`/`efetch`/`elink` (add your `tool=`+`email=`) | PMIDs, abstracts, PMC-OA links |

**One-command resolver:** `python3 scripts/resolve_oa.py <doi>` does the
Unpaywall→OpenAlex step and prints `{is_oa, pdf_url, landing_url, source}`. If
`pdf_url` is set, fetch and read that PDF; if `is_oa` is false, there is no legal free
copy — get it from a user PDF or institutional access, don't summarize the abstract as
if it were the paper.

**Flow for one cited DOI:** `resolve_oa.py` (or fetch Unpaywall/OpenAlex) → if OA,
read the **PMC / Europe PMC HTML full text** (cleanest; avoids publisher consent
gates), falling back to the `pdf_url` → else use the abstract and mark it.

**Worked example** — *"Microbial interactions within the plant holobiont"* (Hassani
et al., Microbiome 2018): Crossref title search → DOI `10.1186/s40168-018-0445-0` →
`resolve_oa.py` → `is_oa: true`. The publisher page
(`microbiomejournal.biomedcentral.com`) redirected through a SpringerLink consent
IdP, so the full text was read from the OA mirror
`pmc.ncbi.nlm.nih.gov/articles/PMC5870681/` — abstract, all seven sections, and
conclusions, no PDF needed. `scripts/verify_citations.py --online` and `resolve_oa.py` both
query these hosts, so network access works in this environment.

Prefer a **connected MCP/literature tool** over raw fetching when the user has one
(cleaner, rate-limit-friendly, rights-cleared); these endpoints are the **zero-setup
fallback**.

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

## Connecting a reference manager (EndNote / Zotero / Mendeley)
The single best way to give the tool the **full picture** of a manuscript's
literature is the user's **own reference library**, because they have already
downloaded the paywalled PDFs legitimately. No special integration is needed — the
attachments are ordinary files on disk that Claude can read once it has folder access:

- **EndNote:** the library is `MyLibrary.enl` **plus a `MyLibrary.Data/` folder**;
  the PDFs are in `MyLibrary.Data/PDF/` (one PDF per randomly-named subfolder), and
  reference metadata is in `MyLibrary.Data/sdb/sdb.eni` (a SQLite file). Give access
  to the **`.Data` folder** (or the whole library folder).
- **Zotero:** PDFs under `Zotero/storage/<ITEMKEY>/…pdf`; metadata in `zotero.sqlite`.
- **Mendeley:** PDFs in the app's watched/download folder.

**Workflow:** point Claude at the folder (in Claude Code, open that directory; in
Cowork, add it to the project — libraries synced via OneDrive/Dropbox work the same).
Then, per cited reference, match to a PDF by the **DOI or title** on the PDF's first
page (or the filename) and read it with the `pdf` skill. Treat the library as
**read-only** — never modify or move the user's `.Data`/`storage` files.

**Caveats.** Access is only as complete as the user's library (a reference they never
attached a PDF for is still just metadata). Respect that these are licensed copies for
the user's own use. There is no official EndNote MCP connector, and none is needed —
this is plain file access.

## What the user can enable for deeper access
If reviews routinely need paywalled full text, any **one** of these removes the
limitation, in rough order of ease:
1. **Point Claude at your reference-manager library** (EndNote `.Data/` / Zotero
   `storage/` / Mendeley) — reuses PDFs you already downloaded; highest coverage.
2. **Drop the specific cited PDFs into the project folder** (zero setup, always works).
3. **Connect a literature MCP/connector** that returns full text (PubMed full-text,
   Europe PMC, a publisher or library connector).
4. **Use a logged-in institutional browser session** (library proxy / VPN) via
   Claude-in-Chrome so entitled articles resolve.
Metadata, abstracts, and open-access full text already work with no setup.
