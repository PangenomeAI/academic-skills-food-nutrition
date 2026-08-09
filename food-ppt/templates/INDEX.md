# food-ppt themes (templates)

Eight code-generated, fully-editable themes. **No third-party template files are
bundled** — each theme is a palette + type + layout style applied by
`scripts/build_pptx.py`, so every element stays native and editable. Pick one with the
deck-spec `"theme"` field (or `--theme`); default is **slate**. Preview all eight in
[`theme-previews.svg`](theme-previews.svg); definitions live in
[`themes.json`](themes.json).

| theme | style | accent | best for |
|---|---|---|---|
| **slate** *(default)* | Minimal business | deep navy `#1F3A5F` | conference & journal-club talks; clean, neutral |
| **sage** | Academic, calm | forest green `#3B5A40` | literature reviews, food & nutrition science, thesis talks |
| **burgundy** | Scholarly, warm | wine `#6E2431` | defenses, formal academic reviews |
| **teal** | Fresh, food-science | teal `#155E63` | food & nutrition topics, public-facing talks |
| **graphite** | Monochrome + amber | charcoal `#2B2F36` | data-forward, executive-style summaries |
| **ocean** | Indigo + cyan | indigo `#213A78` | results-heavy, chart-driven decks |
| **terracotta** | Warm clay + sand | clay `#A0522D` | agronomy, soil & field-trial talks (`agri-ppt`) |
| **forest** | Deep green + lime | green `#24503A` | crop, horticulture & sustainability talks (`agri-ppt`) |

## Choosing
- Ask the user, or infer from topic/audience: food/nutrition → sage · teal · slate;
  agriculture → terracotta · forest · sage; data-heavy → ocean · graphite; formal
  defense → burgundy · sage. When unsure, offer 2–3 and show them
  `theme-previews.svg`.
- One theme per deck — consistency is part of looking professional.

## What each theme controls
Palette (background, surface, ink, muted, **accent**, **accent2**, on-accent), heading
and body fonts, and the styling the builder applies: title cover with brand bar + accent
rule, full-bleed **section dividers**, per-slide **accent edge stripe** + underlined
title + **footer with slide number**, accent bullet marks, and **styled tables**
(accent header row, banded rows). See `references/slide-design.md`.

## Adding a theme
Add one entry to `themes.json` (copy the field set of an existing theme, change the
hex + fonts). It is picked up automatically — no code change. Keep good contrast
(dark accent on white; white on-accent) and use widely available fonts
(Calibri/Arial/Georgia) so the deck renders everywhere.
