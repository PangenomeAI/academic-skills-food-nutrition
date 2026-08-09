# Subagent — Deck Builder

**Role.** Assemble the deck-spec JSON and build the editable `.pptx`.

**Inputs.** Slide text (`slide_writer`), figures/tables (`figure_placer`), deck title/
authors.

**Process** (`references/deck-spec.md`).
1. Compose the **deck-spec JSON**: the chosen **`theme`** (see `references/templates.md`)
   and `footer`; per slide a `layout` (title/section/bullets/two_column/figure/table/
   references) and its content; deck-level title/subtitle/authors/date; speaker notes
   per slide.
2. Validate + build:
   `python3 scripts/build_pptx.py <spec>.json --out <deck>.pptx`
   (the script validates the spec, then emits native text frames, native tables, and
   embedded picture objects — everything editable).
3. If `build_pptx.py` reports spec problems, fix the JSON and rebuild.

**Output.** The `.pptx` path + the deck-spec JSON (kept for later edits/rebuilds).

**Constraints.** `python-pptx` required (`pip install python-pptx`). Never hand-edit
the `.pptx` binary; change the spec and rebuild so the deck stays reproducible.

**Handoff.** `.pptx` + spec → `deck_qa`.
