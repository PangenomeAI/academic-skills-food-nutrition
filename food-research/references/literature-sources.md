# Literature Sources & APIs (food & nutrition)

Canonical source list for `food-research` and `food-deep-research`. Prefer connected
MCP tools; fall back to web search. Record which source/tool produced each hit so
the search is reproducible.

## Bibliographic databases
- **FSTA** (Food Science & Technology Abstracts) — the core food index; controlled vocabulary.
- **PubMed / MEDLINE** — nutrition, clinical, food safety; MeSH terms.
- **Web of Science**, **Scopus** — broad coverage, citation chaining (cited-by / references).
- **CAB Abstracts**, **AGRICOLA**, **AGRIS (FAO)** — agriculture/food.
- **Cochrane CENTRAL** — controlled trials (for systematic reviews).

## Semantic / aggregator APIs
- **CrossRef** (`api.crossref.org`) — DOI metadata, references.
- **OpenAlex** (`api.openalex.org`) — open metadata, citations, concepts.
- **Semantic Scholar** (`api.semanticscholar.org`) — semantic search, embeddings, citations.
- **Consensus** — evidence-oriented search.
- **Europe PMC**, **arXiv/bioRxiv/ChemRxiv/agriRxiv** — preprints/full text.

## Safety, regulatory & compositional
- **EFSA**, **US FDA**, **USDA** (incl. **FoodData Central**), **Codex Alimentarius**, **WHO**, EU/national food-standards bodies.
- **PubChem**, **ChEMBL**, **FooDB**, **Phenol-Explorer** — compounds/bioactives.
- **AOAC**, **ISO** — standard methods.

## Getting the actual full text (not just metadata)
Metadata and abstracts are always reachable; **paywalled full-text PDFs are not,
without help.** When an agent must read the whole article (e.g. `knowledge_builder`
Pathway A, `source_verifier`), follow the retrieval ladder and escalation rules in
**`full-text-access.md`** — open access → connected full-text tool → user-supplied
PDFs → institutional browser session — using **legitimate access only**, and mark
anything unread rather than summarizing it.

## Use notes
- Distinguish peer-reviewed literature from regulatory/industry **grey literature**.
- Use controlled vocabulary (MeSH, FSTA/CAB descriptors) plus free-text synonyms.
- For reproducibility, log the exact query string and result count per source.
- Journal ranking of retrieved articles is applied by `journal_ranker` /
  `source_screener` (see `journal-priority.csv`), not here.
