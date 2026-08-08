---
name: food-ppt
description: "Turn a food & nutrition review report, evidence brief, or manuscript into a fully EDITABLE PowerPoint (.pptx) that opens in PowerPoint / Keynote / Google Slides with every title, bullet, table, and figure as a native editable object — nothing flattened to an image. Converts the outputs of food-research, food-deep-research, food-paper, and food-pipeline (or any Word/PDF/Markdown/txt source) into a well-designed deck: it plans the outline, writes concise grounded slide text with presenter notes on every slide, places figures as movable picture objects, builds the .pptx via python-pptx, and QA-checks editability. Design informed by taste-skill. Use to make slides, a presentation, a PPT, or a deck from a report or paper. Triggers: make a PPT, create slides, presentation from my report, turn this review into slides, build a deck, PPTX from my paper, journal-club slides, conference presentation."
metadata:
  version: "1.0.0"
  verified: "2026-07"
  subagents: [ppt_coordinator, outline_planner, slide_writer, figure_placer, deck_builder, deck_qa]
  related_skills: [food-research, food-deep-research, food-paper, food-pipeline, food-figure, agri-ppt]
  references:
    - references/source-to-slides.md
    - references/deck-spec.md
    - references/slide-design.md
    - references/editability-and-qa.md
---

# Food-Ppt — Editable Presentations from Food & Nutrition Reports

Turn a **review report, evidence brief, or manuscript** into a **fully editable
`.pptx`** — every title, bullet, table, and figure is a **native PowerPoint object the
author can edit**, never a flattened image. Original work; the schema→builder→QA
architecture and design sensibility are informed by the open-source (MIT) `ppt-master`,
`GordenPPTSkill`, and `codex-ppt-skill` skills and the `taste-skill` design guide (see
the repo README Acknowledgements). No third-party templates are bundled.

## What it converts
The outputs of the suite's other skills, or any report/paper the user supplies:
- **`food-review`** panel report / Review & Response Report → a review-findings deck.
- **`food-research` / `food-deep-research`** evidence brief or literature review → a
  synthesis deck.
- **`food-paper`** manuscript (or sections) → a paper-presentation / journal-club deck.
- **`food-pipeline`** — offered at FINALIZE to package the finished work as slides.

## Editable-first (non-negotiable) — `references/editability-and-qa.md`
Build with **python-pptx** so the deck is genuinely editable: **real text frames**
for titles/bullets, **native tables** (editable cells) for data, and figures placed as
**movable/resizable picture objects**. **Never** render a slide to a background image,
never bake text into a picture, never deliver a PDF in place of a `.pptx`. If a figure
exists only as a raster, embed it as a picture object (still movable/replaceable) and
say so; prefer a vector/redrawable source where available.

## Subagents (dispatch via the Agent tool)
1. **`ppt_coordinator`** — takes the source report/manuscript + audience/length, runs the flow, returns the `.pptx` + a slide-by-slide summary.
2. **`outline_planner`** — reads the source and builds the **slide outline** (`references/source-to-slides.md`): one idea per slide, a clear narrative arc, target slide count for the audience.
3. **`slide_writer`** — writes concise, **grounded** slide text (bullets ≤ ~1 line each), speaker notes carrying the detail; every claim/number traces to the source — no new facts, no invented data.
4. **`figure_placer`** — selects figures/tables from the source (or calls **`food-figure`**) and maps them to slides as editable picture objects / native tables.
5. **`deck_builder`** — assembles the **deck-spec JSON** (`references/deck-spec.md`) and runs **`python3 scripts/build_pptx.py <spec>.json --out <deck>.pptx`**.
6. **`deck_qa`** — verifies editability, checks text overflow / slide density, and confirms every slide's content is faithful to the source (`references/editability-and-qa.md`).

## Design — clean and non-generic (`references/slide-design.md`)
Restrained academic style: one accent colour + ink/greys, generous whitespace, strong
type hierarchy, one idea per slide, layout **variety** (title / section / bullets /
two-column / figure / table / references) rather than wall-to-wall bullets. Informed by
`taste-skill`: avoid the templated "AI deck" look — no clip-art, no gradient soup, no
dense text dumps.

## Grounding & privacy (inherited)
Slides are **only** as true as the source — never add a finding, number, or citation
that isn't in it (`food-paper/references/faithfulness-and-citation.md`). Apply the
academic-style + `human-writing.md` pairing to slide prose. Run
`scripts/privacy_scan.py` on the deliverable; keep the mandatory **AI-use disclosure**
on a closing slide when the deck presents AI-assisted work.

## Requirements
`python-pptx` (`pip install python-pptx`). Figures come from the source or `food-figure`.
