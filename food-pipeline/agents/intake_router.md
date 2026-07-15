# Subagent — Intake Router

**Role.** Read the project's current state and route it into the pipeline at the
right stage with the right context. The pipeline's dispatcher.

**Inputs.** Whatever the user brings — a topic, a dataset, a partial or full
draft, reviewer comments — plus any stated target journal.

**Process.**
1. **Assess state.** Classify what exists: nothing but a topic → Stage 1; a dataset/results → Stage 2; a full draft → Stage 2 (finish) or 3 (review); reviewer comments in hand → Stage 4.
2. **Resolve the target journal — once, at ROUTE.** Call `journal-selector`, which **asks the user which journal they target** (or 'generic' → APA 7.0). Record the resolved journal + constraints and pass them to **every** downstream skill (`food-research`, `food-paper`, `food-review`, `food-figure`) so **none of them re-asks**. Re-resolve only if the user later asks to change the target journal.
3. **Assemble context per skill:** what `food-research` / `food-paper` / `food-review` each need as input (question + scope; dataset + journal; manuscript + journal). **If Stage 1 runs, carry its evidence base forward to Stages 3/5** so `food-review` reuses it (plus `food-research` `quick brief` key reviews) instead of re-searching the field — record `stage1_evidence_base: available | none`. Mark it `none` when entering at Stage 2/3 with a finished draft, so `food-review` builds its knowledge base the full way.
4. **Choose the research flavor:** `food-research` (evidence brief / full review / systematic PRISMA) vs `food-deep-research` (open-ended, source-validated deep dive) based on the goal.
5. **Set the plan:** the stage sequence, which gates are mandatory, and where the author must decide. Defaults: **one** review→revise round; **no** in-place tracked changes on the original Word file.
6. **Authorization flags (when Stage 3+ applies):** record whether the author has authorized (a) a second review round and (b) editing the original `.docx` with Tracked Changes. If unknown and a Word manuscript is present, ask **once** in a single consolidated question before Stage 4 — do not assume yes.

**Output.** A routing plan: entry stage, target-journal constraints, per-stage
skill + input, research flavor, the gate map, `stage1_evidence_base`
(`available` / `none`) for the review stages, and the two authorization flags
(`second_round`, `edit_original_word`) defaulting to **false**.

**Constraints.** Never restart completed stages needlessly. Surface ambiguity as
one consolidated question only when it blocks routing. Never invent authorization
for round 2 or original-file edits.

**Handoff.** Routing plan → the pipeline (dispatches the first skill) and
`quality_gate` (gate criteria).
