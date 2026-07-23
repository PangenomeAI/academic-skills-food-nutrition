# Title Page & Declarations Guide

The **title-page metadata** and **end-matter statements** nearly every journal
requires. `intake` collects them, `draft_writer` (food-paper) / `writer`
(food-research) / `compiler` (food-deep-research) write them, and `citation_manager` /
`internal_reviewer` check they are present.

## Author-provided information is required — ASK, never invent
Author names, affiliations, contact details, ORCIDs, CRediT roles, funding/grant
numbers, competing interests, ethics-approval numbers, and data locations are **facts
only the authors know**. **Never fabricate, guess, or auto-fill any of them** — an
invented author, email, affiliation, or grant number is a fabrication *and* a privacy
error. If the manuscript, data, or user request doesn't already supply an item,
**generate a clear, structured questionnaire and ask the user** before finalizing;
leave a visible `[NEEDS: …]` placeholder for anything still unanswered — never a
plausible-looking invented value.

### Intake questionnaire (present the missing items as one consolidated set)
Ask only for what's missing; group into one message:
1. **Authors, in final order** — full names as they should appear (given + family),
   and each author's **ORCID** if available.
2. **Affiliations** — each author's institution(s), department, city, country; map
   authors → affiliations (superscript numbers). Note any **equal-contribution** or
   **present-address** cases.
3. **Corresponding author** — who, plus the **email** and **full postal address**
   the journal will publish (some journals allow more than one).
4. **CRediT roles per author** — which of the 14 roles each author had (see below).
5. **Competing interests** — any financial/personal COI, or confirm "none".
6. **Funding** — funder name(s) + grant number(s), or confirm "none".
7. **Ethics** — human/animal approval body + number, consent, trial registration, as
   applicable; allergen disclosure where relevant.
8. **Data availability** — repository + accession/DOI, access conditions, or the
   journal's accepted "available on request" wording.
9. **AI-use disclosure** — confirm the model/version used (below); ask if unsure.

Confirm the exact required set and placement with the target journal (via
`journal-selector`) — requirements and field order vary by publisher.

## Title page / authorship block
Build from the collected answers, in the target journal's format:
- **Title** (and a short **running title** if required); **keywords**.
- **Author list** in the confirmed order, each linked by superscript to its
  **affiliation(s)**; ORCIDs where given; equal-contribution and present-address notes.
- **Corresponding author** clearly marked, with the **email** (and postal address if
  required). Author personal contact details on a title page are **intentional,
  author-supplied** content — they are required by the journal and are not a privacy
  leak (distinct from stray local paths/secrets the privacy scan flags), but they must
  come from the user, never be invented.

## CRediT author contributions
Use the 14 CRediT roles; assign each author explicitly. Common: Conceptualization,
Methodology, Investigation, Formal analysis, Data curation, Writing – original
draft, Writing – review & editing, Supervision, Funding acquisition.
> Example: "P. Zhang: Conceptualization, Methodology, Writing – original draft. J.
> Smith: Formal analysis, Writing – review & editing."

## Competing interests
State any financial/personal COI; if none: "The authors declare no competing
interests." Disclose industry funding and author roles in funding bodies.

## Funding
Name funder(s) and grant number(s); if none: "This research received no specific
grant…".

## Data availability
State where data are (repository + accession/DOI), or the access conditions, or
"Data available on reasonable request." Many journals now require a statement.

## Ethics (food & nutrition)
- Human sensory/dietary studies: ethics-committee approval (name + number),
  informed consent; trial registration where applicable.
- Animal studies: approval + ARRIVE compliance.
- Allergen disclosure where relevant.

## AI-assistance disclosure (required — tool + model + version)
Every manuscript this suite helps write **must** acknowledge AI assistance
honestly. In the **Acknowledgements** section (or the journal's required location
for an AI statement), always state:
1. **This tool** — *Academic Skills for Food & Nutrition Science*
   (github.com/PangenomeAI/academic-skills-food-nutrition).
2. **The AI model(s) and version(s)** actually used — name the model **and its
   version** and the harness (e.g. *Claude Opus 4.8 via Claude Code*, *OpenAI
   Codex / GPT-5.x*, *Gemini 2.x*). If unsure of the exact version, ask the user
   rather than guessing.
3. **What the AI did** (e.g. literature synthesis, drafting, figure code, language
   editing) and that **the authors reviewed and verified all AI-assisted content
   and take full responsibility** for the work.

Template (adapt to the venue):
> The authors used *Academic Skills for Food & Nutrition Science*
> (github.com/PangenomeAI/academic-skills-food-nutrition) with [AI model and
> version, e.g. Claude Opus 4.8 via Claude Code] to assist with [tasks, e.g.
> literature search and synthesis, drafting, figure generation, and language
> editing]. All AI-assisted content was checked and verified by the authors, who
> take full responsibility for the manuscript.

Some venues require the AI statement in **Methods** or a **dedicated section**
rather than Acknowledgements — follow the target journal's policy (via
`journal-selector`); default to Acknowledgements. Match exact wording/headings to
the target journal.
