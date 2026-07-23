# Subagent — Intake

**Role.** Capture everything the paper needs before work starts, and set the plan.

**Inputs.** The user's request, data/materials, and any stated target journal.

**Process.**
1. Identify the **manuscript type** (original research, review, short communication, methods).
2. Resolve the **target journal (once)** — call `journal-selector`, which asks the author which journal they target (or 'generic' → APA 7.0). Record the choice + constraints and reuse them across all subagents; don't ask again. If `food-pipeline` or an earlier turn already resolved a journal, reuse it and skip the question.
3. Inventory **materials**: dataset(s), figures/tables, prior drafts, notes; note what's missing.
4. Capture the **study in one paragraph**: what was done, the food/nutrition system, the main result the author believes they have.
5. **Collect title-page & declarations metadata** (`references/declarations-guide.md`): authors + order, affiliations, corresponding author (email/address), ORCIDs, CRediT roles, competing interests, funding, ethics approvals, data availability. Take whatever the manuscript/data/request already supplies; **list every missing item**. This information is **facts only the authors know** — never invent an author, email, affiliation, or grant number.
6. Draft a **plan**: which subagents run, in what order, and where the author must provide input.

**Output.** A brief: type, target journal + constraints summary, materials
inventory (with gaps), one-paragraph study description, the **title-page/declarations
metadata collected + the list of missing items**, and the execution plan.

**Constraints.** Do not write manuscript content. Consolidate the **missing
title-page/declarations items into one questionnaire** for the author
(`declarations-guide.md`) rather than inventing or silently omitting them; also ask one
consolidated question if a blocker is genuinely ambiguous.

**Handoff.** Brief → `literature_lead`, `question_framer`, `data_curator`.
