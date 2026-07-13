# AI Image Generation — schematics & graphical abstracts (opt-in)

**Default is always Python or R.** Use an AI image model **only when the user
explicitly asks** to generate the image with **Gemini, ChatGPT, or Claude** (or
another named image model) — and **only for conceptual visuals**. Method informed
by the MIT `academic-figure-skills` / `academic-figure-generator` projects (see
the repo README Acknowledgements); wording here is original.

## When it is allowed — schematic figure types
Only for **conceptual/qualitative visuals** (no data axes/values):
| Type | Structure | Food/nutrition example |
|---|---|---|
| **Process / workflow** | Input → Step 1 → Step 2 → Output | Extraction/encapsulation pipeline; sample-prep workflow |
| **Mechanism / pathway** | Entities + labelled arrows (cause→effect) | Antioxidant action; gut-microbiome interaction; Maillard pathway |
| **Experimental design** | Groups × treatments × timepoints (schematic) | Storage/shelf-life trial layout; sensory panel design |
| **Graphical abstract** | Split or circular concept summarising the paper | The paper's core finding as one concept image |
| **Comparison (conceptual)** | N columns, shared parts grey, differences highlighted | Coating A vs B mechanism (no measured values) |

## When it is NOT allowed
**Never** use an AI image model for a **data-bearing figure** — bar/line/scatter,
heatmap, chromatogram, microscopy, dose–response, forest, PCA, etc. Those are
quantitative evidence and **must** be produced in Python/R from the real data.

## Prompt method (four layers)
1. **Understand the concept** from the manuscript: the central claim, the key
   entities, the cause→effect logic, and the layout (left-to-right / circular /
   split panels). Use only what the source states.
2. **Global description** — open with figure type, subject, layout, and style:
   *"A clean, flat academic [process/mechanism] schematic, [layout], white
   background, minimal text, no data values."*
3. **Section-by-section** — describe each region with `=== SECTION ===` markers:
   the boxes/entities, their labels, the arrows/connections and their labels, and
   any small icons. Keep the geometry explicit.
4. **Style specification** — flat academic aesthetic; the palette (see
   `color-palettes.md`); border-only colour on white fill; consistent fonts.

For tight control, output a **structured JSON spec** (boxes with positions/labels,
arrows with from→to/label) and hand that to the model — it renders text and layout
more reliably than prose alone.

## Draft → controlled final workflow
Generate a **text-free composition draft** first, then apply essential labels in a
vector editor from the approved spec. This separates the image model's useful
strength (simple visual composition) from its unreliable strength (scientific
terminology and exact typography). Before generation, create a content boundary:
list every permitted entity, relationship, and visual metaphor, and reject every
extra detail. Do not ask the model to improvise a mechanism.

Use this compact spec when the layout needs to be auditable and reproducible:
```json
{
  "layout": "left-to-right",
  "permitted_entities": ["coated berry", "protective barrier", "storage"],
  "sections": [
    {"id": "input", "position": "left", "visual": "berries"},
    {"id": "process", "position": "centre", "visual": "barrier around berries"},
    {"id": "outcome", "position": "right", "visual": "intact berries"}
  ],
  "arrows": [{"from": "input", "to": "process"}, {"from": "process", "to": "outcome"}],
  "forbidden": ["text", "numbers", "axes", "logos", "unsupported mechanisms"]
}
```
The spec is an instruction for a draft image, not evidence or a substitute for
source verification. Replace the placeholder entities only with concepts that
the manuscript source supports.

## AI schematic QA and trace record
Before use, inspect the output at final size and reject it if it contains an
invented entity, causal step, data-like mark, axis, number, logo, illegible text,
or a style element that hides the causal flow. Keep an AI-specific trace record
beside the normal figure trace card: model/service and date, final prompt and JSON
spec, source material that constrained the concept, accepted human edits, and the
policy-required disclosure location. If the service fails or access is denied,
record the failure and do not claim that an image was generated or evaluated.

## Text budget (labels only; details go in the caption)
Module/box titles ≤5 words; sub-labels ≤3 words; pipeline steps ≤2 words. **No
equations, parameters, or numbers inside the image** — those belong in the figure
**caption**. Assume AI text rendering is imperfect and re-label the final image in
a vector editor (Inkscape/Illustrator).

## Visual style constraints
Flat, academic: **no gradients, shadows, or 3-D**. 2–3 hues + greyscale from the
chosen palette; white fill dominant (≥70%); colour reserved for borders/arrows,
not filled background panels; small-caps labels with thin grey dividers.

## Non-negotiable (anti-fabrication)
- **No fabricated data or values** — no invented numbers, axes with values,
  p-values, error bars, sample sizes, or made-up mechanisms/sub-steps not in the
  source. Mark anything uncertain as *"to confirm"*, don't invent it.
- **No fabricated logos, journal marks, or institutional branding.**
- **Draft concept, not evidence** — the underlying science must be established and
  cited in the manuscript text.
- **Disclose** AI image generation per the venue's policy
  (`food-paper/references/declarations-guide.md`), and check the journal permits
  AI-generated figures — many restrict them.

If the user has not asked for AI image generation, do not use it — return to the
Python/R backend gate.
