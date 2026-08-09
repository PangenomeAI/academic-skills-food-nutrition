# Slide Design — clean, academic, non-generic

Goal: a deck that looks considered, not a templated "AI slide dump". Design sensibility
informed by `taste-skill` (avoid slop; real hierarchy; restraint) and the MIT-licensed
`ui-ux-pro-max-skill` (layout patterns, a real typographic scale, and layout→emotion
logic), adapted for scientific presentations.

## Principles
- **One idea per slide.** If a slide has two messages, split it. The title states the
  message; the bullets support it.
- **Type hierarchy.** Big, informative title; readable body (≈18 pt bullets, not 12);
  captions/refs smaller. Don't shrink text to fit — cut text or add a slide.
- **Whitespace.** Generous margins; ≤ ~5 bullets; never fill every pixel.
- **Restrained palette.** One accent colour + ink/greys (the builder uses a muted teal
  accent). No gradient soup, no clip-art, no decorative stock images.
- **Layout variety.** Alternate title / section dividers / bullets / two-column /
  figure / table / metric / cards / flow / result / references — monotony of bullet
  slides is the templated look to avoid. When a point is a number use `metric`; when
  it's a set of parallel facts use `cards`.
- **Show the data.** A figure or a native table beats a paragraph of numbers. One main
  visual per slide, captioned.
- **Informative titles.** "Coating cut weight loss 23%" > "Results". The audience
  should get the point from titles alone.

## Typographic scale (what the builder applies)
Strong size **and weight** contrast is what separates a designed slide from a wall of
18 pt text. `build_pptx.py` uses (adapted from `ui-ux-pro-max-skill`'s slide-typography
scale, scaled to PowerPoint points):
- **Cover title** 46 pt bold, tight tracking, line-height ~1.0.
- **Section divider** 40 pt bold on the accent field.
- **Content title** 26 pt bold accent, with an accent-2 underline.
- **Big-number hero** (`metric`) 96 pt bold — one figure the audience remembers.
- **Card heading** (`cards`) 22 pt (or 30 pt for a single row of headline stats).
- **Body/bullets** 18 pt; **captions/refs** 11–15 pt; **footer** 9 pt.
Rule of thumb: headlines tight (line-height ≤1.1, slightly negative letter-spacing);
body loose (1.4–1.6). Never shrink body below ~16 pt to fit — cut text or add a slide.

## Layout → message (pick the layout that fits the point)
From `ui-ux-pro-max-skill`'s layout-logic, mapped to academic use:
- **A single striking number** (effect size, sample size, % change) → `metric`
  (big-number hero). Trust/proof reads best on a calm surface background.
- **3–6 parallel facts** (objectives, contributions, study parameters, KPIs) → `cards`
  (accent-bar cards), *not* a bullet list — a grid reads as designed, bullets as filler.
- **Compare two things** → `two_column`. **Progression/pipeline** → `flow`.
- **Evidence** → `figure`/`table`; **a result** → `result` (evidence + key findings).
- **Break the pattern** at the 1/3 and 2/3 points of the deck with a full-bleed
  `section` divider — pattern breaks create the engagement peaks a flat deck lacks.

## Academic register
Slide prose follows `food-paper/references/writing-style.md` + `human-writing.md`:
no inflated significance, no "studies have shown", no stock AI vocabulary; keep
calibrated hedging. Units and symbols exact. Nothing on a slide that isn't in the
source.

## Consistency
Same accent, fonts, and title position on every slide (the builder enforces this).
Section dividers signal the arc. A short closing slide carries conclusions and the
**AI-use disclosure** when presenting AI-assisted work.
