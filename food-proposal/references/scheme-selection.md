# Scheme Selection

Resolve the target funding scheme **before writing** — it fixes the headings, order,
length limit, font, and assessment criteria the whole proposal is built to.

## Ask once, up front
> Which funding scheme / proposal format are you targeting? Built in:
> **ARC Discovery — EOI** (`arc-discovery-eoi`), **ARC Discovery — Full Application**
> (`arc-discovery-full`), **UoM Ag & Food Major/Minor Research Project**
> (`uom-major-minor-project`). If it's a different scheme, upload the scheme's
> **guideline / instructions or a sample application form** and I'll extract its format.

## Resolve
1. Match the answer to a built-in id → load `schemes/<id>.md` (human spec) +
   `schemes/schemes.json` (machine limits). See `schemes/INDEX.md` for the catalog.
2. **Not built in?** Don't guess the format. Run **`scheme_extractor`** on the uploaded
   guideline/sample to create a new `schemes/<id>.md` + `schemes.json` entry, then
   confirm the extracted headings + limit with the user before drafting.
3. Record the scheme id so `compliance_gate` and `proposal_wordcount.py` use the right
   limits everywhere.

## Multiple stages
ARC Discovery has an **EOI** and a **Full Application** — different length (2 vs 7
pages) and headings (Full adds BENEFIT and COMMUNICATION OF RESULTS). Pick the stage
the user is at; a Full Application can build on the EOI content but must expand to the
Full headings and page limit.

## Grounding
The scheme's requirements come **only** from the built-in spec or the user's uploaded
document — never from memory of "how grants usually look". Confirm the current year's
official guideline before submission; funders update instructions annually.
