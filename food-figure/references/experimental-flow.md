# Experimental-Design Flow Diagram (BioRender-style)

A schematic that lets an audience grasp a study's design at a glance: materials →
treatments/groups → timepoints → assays → analysis, laid out as labelled boxes joined
by arrows. **Every deck built from a research proposal or a research paper must include
one** (food-ppt requires it). This reference defines the design; food-ppt renders it.

## Editable, movable components — not one flat image
The flow chart is a **big figure made of many components, and each component must stay
movable and editable** in the final slide. So in a **presentation** it is **not** a
rasterised image: food-figure produces a **structured flow blueprint** (below) and
`food-ppt`'s `build_pptx.py` renders it as **native PowerPoint shapes** — one rounded
box per step, one arrow per transition, editable text in each — so the presenter can
move, relabel, or restyle any box or arrow. (For a **static manuscript figure** outside
a deck, draw the same blueprint as a code schematic — grouped vector shapes, each
component a separate object — never a single flattened bitmap.)

## The blueprint food-figure produces (the `flow` deck-spec)
```jsonc
{
  "layout": "flow",
  "title": "Experimental design",
  "lanes": [                         // stacked, labelled rows (a swimlane per phase)
    {"label": "Material",  "steps": ["Fresh blueberries", "Wash & sort", "Pack"]},
    {"label": "Treatment", "steps": ["Control", "HPP 400 MPa", "HPP 600 MPa"]},
    {"label": "Assays",    "steps": ["Firmness", "Anthocyanins", "Microbial load"]},
    {"label": "Analysis",  "steps": ["ANOVA", "PCA"]}
  ]
  // OR a single linear path: "steps": ["Sample", "Extract", "Assay", "Analyse"]
}
```
Use **lanes** for a multi-phase design (recommended for proposals/papers), or **steps**
for a simple linear pipeline. Keep each box label ≤ ~5 words; ≤ ~5 boxes per lane so
they stay readable. Put dose/timepoint detail in the box text (e.g. "HPP 600 MPa, 3
min") or the slide's speaker notes, not in a cramped caption.

## Design conventions
- **Left → right within a lane; top → bottom across lanes** (Material → Treatment →
  Assays → Analysis). Group the real replication/arms as parallel boxes in the
  Treatment lane.
- **Grounded:** boxes must reflect the **actual** design in the source (arms, n, doses,
  timepoints, assays). Never invent a step, an arm, or a sample size
  (`food-paper/references/faithfulness-and-citation.md`).
- **Theme-matched palette:** take the deck's theme colours (accent = box border,
  accent-2 = arrows, band = box fill, ink = text) so the diagram matches the slides —
  see `color-palettes.md` and the theme in `food-ppt/templates/themes.json`.
- Flat, academic look — no clip-art, no 3-D, no gradients (`design-principles.md`).

## Handoff
`food-ppt`'s `figure_placer` calls food-figure to build this blueprint; `deck_builder`
drops it in as a `flow` slide, rendered as movable native shapes. For results figures
and tables, see `chart-types.md` / `data-to-figure.md`; match the same theme palette.
