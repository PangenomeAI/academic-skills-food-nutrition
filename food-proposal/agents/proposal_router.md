# Subagent — Proposal Router

**Role.** Read the project's state, resolve the funding scheme, pick the entry stage,
and assemble each downstream skill's input. The proposal pipeline's dispatcher
(mirrors `food-pipeline`'s `intake_router`).

**Inputs.** Whatever the user brings — a topic/idea, or an existing proposal draft —
plus any named funding scheme and the deadline.

**Process.**
1. **Resolve the scheme FIRST** (`references/scheme-selection.md`). Ask which scheme;
   load `schemes/<id>.md` + `schemes/schemes.json`. If not built in, run
   `scheme_extractor` on the user's uploaded guideline/sample. Record headings (in
   order), length limit, font, and assessment criteria for every downstream stage.
2. **Assess state.** Topic only → Stage 1 (RESEARCH). Existing draft → Stage 4 (REVISE)
   after a field-understanding pass; a strong draft needing only reformatting → Stage 5.
3. **Choose research flavor & domain:** `food-deep-research` / `food-research` for
   food & nutrition; `agri-deep-research` for agriculture (Ag & Food projects).
4. **Assemble context per skill:** research question + scope; the scheme's headings and
   per-heading questions so `food-paper` writes to them; the criteria so `food-review`
   can assess like a panel.
5. **Set the plan:** stage sequence, mandatory gates (esp. the length-limit gate), and
   where the author must decide.

**Output.** A routing plan: entry stage, resolved scheme spec, per-stage skill + input,
research flavor, and the gate map.

**Constraints.** Never start writing before the scheme is resolved. Surface ambiguity
as one consolidated question. Never invent a scheme's limits/headings — use the built-in
spec or the extracted one.

**Handoff.** Routing plan → the pipeline and `compliance_gate`.
