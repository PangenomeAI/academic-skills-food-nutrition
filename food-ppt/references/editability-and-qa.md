# Editability & QA

The deck's defining promise: **everything is editable in PowerPoint** — and faithful
to the source. Check both before delivery.

## Editable-first (hard rules)
- **Text** (titles, bullets, captions, references) → **real text frames** the author
  can click and edit. Never text baked into an image.
- **Tables** → **native PowerPoint tables** with editable cells. Never an image of a
  table.
- **Figures** → **movable/resizable picture objects**. Never flatten a slide to a
  background image; never bake text onto a figure.
- Deliver a real **`.pptx`** — never a PDF or an image-only "deck" in its place. If a
  figure exists only as a raster, embed it as a picture object (still movable /
  replaceable) and say so.

Spot-check the built file: each slide's `ppt/slides/slideN.xml` should contain `<a:t>`
text runs; data slides should contain `<a:tbl>`; no content slide should be a single
full-bleed picture standing in for text.

## Presenter notes (required)
**Every content slide must have presenter notes** in the real Notes pane — the script,
the numbers/caveats behind the bullets, and the source locator. QA fails a deck whose
content slides have empty notes.

## Readability
- One idea per slide; ≤ ~5 bullets; body font not tiny.
- **No text overflow** past the slide — if it overflows, cut text, raise the split, or
  move detail to notes; do **not** shrink the font to illegible sizes.
- Layout variety, not wall-to-wall bullets.

## Faithful & clean
- Every slide claim / number / citation appears in the source — nothing invented,
  hedging preserved (`food-paper/references/faithfulness-and-citation.md`).
- AI-use disclosure slide present when the deck presents AI-assisted work.
- `scripts/privacy_scan.py` on the `.pptx` — no local paths or secrets.
