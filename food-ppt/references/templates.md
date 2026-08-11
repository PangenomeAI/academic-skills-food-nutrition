# Templates & Themes

food-ppt ships **seventeen editable themes** (see [`../templates/INDEX.md`](../templates/INDEX.md)
and the preview [`../templates/theme-previews.svg`](../templates/theme-previews.svg)),
including **`midnight`**, a **dark theme**. A theme is a palette + type + layout style —
**not** a bundled file — so the deck stays fully editable. The gallery recreates the
*look* (in English) of the open-source `GordenPPTSkill` templates (and a Grok-generated
dark deck) as original theme definitions; see INDEX.md § Provenance.

## Auto-pick a theme, then offer options (do this in `ppt_coordinator`)
1. **Auto-select from the deck's own text:** run
   `python3 scripts/suggest_theme.py --text "<title + abstract/topic>" [--audience "<who>"]
   [--doctype "<review|proposal|results|...>"] --top 3`. It ranks themes by the
   `keywords` in `themes.json` and returns the best fit (with matched terms as the
   reason). Use `--json` for machine-readable output.
2. **Recommend #1 and offer the top ~3** to the user, pointing to
   `theme-previews.svg` so they can see the look. If the user already named a theme or
   a style, that wins — the script is a suggestion, not a gate.
3. Set it in the deck spec: `"theme": "sage"` (or pass `--theme sage` to the builder).
   Default is `slate`. **One theme per deck.**

Rough map if choosing by hand: food/nutrition → `teal`/`sage`/`slate`; agriculture →
`terracotta`/`forest`; data/KPIs → `ocean`/`dashboard`/`graphite`; strategy/industry →
`consulting`/`azure`; proposals/thesis → `scholar`/`sage`; formal defense →
`claret`/`burgundy`; modern pitch → `indigo`/`geometric`; outreach/teaching →
`apricot`; AI/tech briefing or news summary, or any deck that should be **dark** →
`midnight`.

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
