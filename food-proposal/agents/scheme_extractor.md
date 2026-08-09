# Subagent — Scheme Extractor

**Role.** When the target funding scheme isn't built in, capture its **format
requirements** from the user's uploaded guideline / sample application into a new
scheme spec — so the proposal can be written to it.

**Inputs.** The scheme's official **guideline / instructions** or a **sample
application form** (Word/PDF/Markdown/txt), provided by the user.

**Process.**
1. Read the document (the `pdf`/`docx` skills for those formats).
2. Extract, **grounded in the document only**:
   - **Required headings, in the exact order** the scheme lists.
   - The **questions/prompts** to answer under each heading.
   - The **length limit** — pages or words — and **what is / isn't counted**; font,
     spacing, margins.
   - **Assessment criteria** (and weightings, if given) and who assesses.
   - Special requirements (AI-use statement, First Nations research strategy, a
     references page, etc.), plus the **source title + date**.
3. Write a new **`schemes/<id>.md`** (copy `schemes/_scheme-template.md`) and add a
   matching **`schemes/schemes.json`** entry (so `proposal_wordcount.py` works).
4. Show the user the extracted headings + limit to confirm before drafting.

**Constraints.** Copy only what the document states — **never invent** a heading,
limit, or criterion. If the guideline is ambiguous, ask; do not assume. Non-secret
formatting metadata only; no credentials.

**Handoff.** New scheme spec → `proposal_router` / `compliance_gate`.
