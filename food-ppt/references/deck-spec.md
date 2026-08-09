# Deck-Spec Schema (`scripts/build_pptx.py`)

The builder reads one JSON object and emits a fully editable `.pptx`. Every slide's
content becomes **native, editable** objects (text frames, tables, picture objects).

```jsonc
{
  "title": "Deck title",            // deck-level; used on the title slide
  "subtitle": "...",                // optional
  "authors": "...",                 // optional
  "date": "...",                    // optional
  "aspect": "16:9",                 // 16:9 (default)
  "slides": [
    {"layout": "title",   "title": "...", "subtitle": "...", "authors": "...", "notes": "..."},
    {"layout": "section", "title": "Section name", "notes": "..."},
    {"layout": "bullets", "title": "...", "bullets": ["point", ["sub-point"], "point"], "notes": "..."},
    {"layout": "two_column", "title": "...", "left": ["..."], "right": ["..."], "notes": "..."},
    {"layout": "figure",  "title": "...", "image": "path/to/fig.png", "caption": "...", "notes": "..."},
    {"layout": "table",   "title": "...", "table": [["H1","H2"], ["a","b"]], "notes": "..."},
    {"layout": "flow",   "title": "Experimental design",
       "lanes": [{"label": "Material", "steps": ["...", "..."]},
                 {"label": "Treatment", "steps": ["control", "arm 1", "arm 2"]},
                 {"label": "Assays", "steps": ["..."]}], "notes": "..."},
    {"layout": "result", "title": "Finding in a sentence",
       "image": "fig.png",          // OR "table": [["H","H"],["a","b"]]
       "key_findings": ["point", "point"], "caption": "...", "notes": "..."},
    {"layout": "references", "title": "References", "items": ["ref 1", "ref 2"], "notes": "..."}
  ]
}
```

## `flow` — experimental design (native, movable shapes)
`flow` renders a **BioRender-style experimental-design diagram as native PowerPoint
shapes** — one rounded box per step, one arrow per transition, all **movable and
editable** (never a flattened image). Give it **`lanes`** (labelled swimlanes:
Material → Treatment → Assays → Analysis) or a linear **`steps`** list. Design comes
from **food-figure** (`experimental-flow.md`); box labels ≤ ~5 words, ≤ ~5 boxes/lane.
**Required in every deck built from a research proposal or paper.**

## `result` — a findings slide (figure/table + key points)
`result` puts a **figure** (`image`) **or** a scientific-style **table** on the left
and a **Key findings** panel (`key_findings`, bullets) on the right — so every results
slide carries both the evidence and the takeaways. Prefer a figure to illustrate the
result; use a table when the numbers are the point.

## Executive summary (required)
End every deck with an **Executive summary** slide (a `bullets` slide titled
"Executive summary") capturing the key takeaways, before References and the AI-use
disclosure.

## Theme & footer
- **`theme`** — one of the keys in `templates/themes.json` (slate · sage · burgundy ·
  teal · graphite · ocean · terracotta · forest); default `slate`. Sets palette, fonts,
  and layout styling. See `templates.md`.
- **`footer`** — short deck label shown bottom-left on content slides (defaults to the
  deck title).

## Rules
- **`layout`** is one of: `title · section · bullets · two_column · figure · table ·
  references`. The validator rejects anything else and reports the offending slide.
- **`bullets`** items: a string is a top-level bullet; a **nested list** is its
  sub-points. Keep each ≤ ~1 line; ~3–5 per slide.
- **`figure.image`** is a path to a real image file → embedded as a **movable picture
  object** (never a slide background). Add a `caption`.
- **`table.table`** is a list of rows (first row = header) → a **native PowerPoint
  table** with editable cells. Never pass a table as an image.
- **`notes`** — **required on every content slide** (see "Presenter notes" below).

## Presenter notes on every slide
Each slide **must** carry a `notes` field with the presenter script — the fuller
explanation, the numbers/caveats behind the bullets, and the source locator. Slides
stay sparse (audience-facing) while the notes hold the depth (presenter-facing).
`build_pptx.py` writes `notes` to the slide's real Notes pane (editable in PowerPoint).

## Build
```bash
python3 scripts/build_pptx.py deck.json --out deck.pptx
```
Validation runs first; fix any reported problem and rebuild. Keep the JSON alongside
the `.pptx` so the deck can be edited-by-spec and rebuilt reproducibly.
