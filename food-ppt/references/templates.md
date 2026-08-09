# Templates & Themes

food-ppt ships **eight editable themes** (see [`../templates/INDEX.md`](../templates/INDEX.md)
and the preview [`../templates/theme-previews.svg`](../templates/theme-previews.svg)).
A theme is a palette + type + layout style — **not** a bundled file — so the deck stays
fully editable.

## Pick a theme (do this in `ppt_coordinator`)
1. Ask the user, or infer from topic/audience (food/nutrition → `sage`/`teal`/`slate`;
   agriculture → `terracotta`/`forest`; data-heavy → `ocean`/`graphite`; formal defense
   → `burgundy`). When unsure, name 2–3 and point to `theme-previews.svg`.
2. Set it in the deck spec: `"theme": "sage"` (or pass `--theme sage` to the builder).
   Default is `slate`. One theme per deck.

## What the theme applies (all editable shapes/text — nothing flattened)
- **Cover:** top brand bar, large accent title, accent-2 rule, subtitle/authors, bottom band.
- **Section divider:** full-bleed accent background, white centred title, accent-2 rule.
- **Content slides:** slim accent **edge stripe**, accent title with an accent-2 underline,
  and a **footer** (deck label left, **slide number** right).
- **Bullets:** accent square marks; sub-points in muted with an accent dash.
- **Tables:** accent **header row** (white bold), alternating banded body rows.
- **Figures:** placed as movable picture objects with a muted caption.

## Rules
- **Consistency > variety of colour:** one theme, applied everywhere.
- Keep the palette restrained (one accent + accent-2 + ink/greys) — the theme already
  enforces this; don't add extra colours per slide.
- Design never overrides substance: readable body sizes, one idea per slide, no overflow
  (`references/editability-and-qa.md`), and everything grounded in the source.
- Custom theme? Add an entry to `templates/themes.json` (see INDEX.md).
