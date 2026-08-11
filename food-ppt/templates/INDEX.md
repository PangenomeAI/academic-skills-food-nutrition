# food-ppt themes (templates)

**Seventeen** code-generated, fully-editable themes. **No third-party template files are
bundled** — each theme is a palette + type + layout style applied by
`scripts/build_pptx.py`, so every element stays native and editable. Pick one with the
deck-spec `"theme"` field (or `--theme`); default is **slate**. Preview them all in
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
| **consulting** | Crimson + navy | crimson `#A52524` | strategy & structured argument, executive decks |
| **dashboard** | Navy + brick red | navy `#23406B` | results-heavy metrics & KPI decks, competitive analyses |
| **azure** | Royal corporate blue | royal blue `#1F3A93` | industry/professional talks, operations & project updates |
| **geometric** | Navy + coral, colorful | indigo-navy `#243670` | overviews & summaries that want energy without clutter |
| **indigo** | Electric indigo, modern | electric `#3D3DF5` | bold modern talks, pitches & seminars |
| **scholar** | Navy + gold on parchment | navy `#2A3F75` | thesis & grant proposals, dissertations |
| **claret** | Wine red on cream | wine `#7A2B22` | formal defenses & prestige academic decks |
| **apricot** | Friendly orange | warm orange `#B85F2A` | public engagement, teaching & science-communication |
| **midnight** | Dark slate + blue *(dark theme)* | blue `#3B82F6` | AI/tech briefings, news summaries, modern dark-mode talks |

## Auto-selection (and offering options)
`ppt_coordinator` runs **`python3 scripts/suggest_theme.py --text "<deck title +
abstract/topic>" [--audience ..] [--doctype ..]`** to **auto-pick a suitable theme**
from the deck's own text and **offer the top few as options** for the user to choose.
Each theme carries `keywords` in `themes.json`; the script ranks themes by keyword
match and returns the best (with the matched terms as the reason). It ranks *aesthetics
only* — never deck content. The user's explicit choice always wins.

## Provenance
Most themes **recreate the look** (palette + style, in English) of the open-source
`GordenPPTSkill` template gallery — mapped onto original, code-generated theme
definitions; **no `.pptx`/image files are copied or bundled** (that project's templates
carry no clear licence). **`midnight`** is the sole **dark theme**, recreating the
dark-slate + blue look of a user-supplied Grok-generated briefing (palette re-derived,
no file copied). Near-identical corporate-blue templates are consolidated into
`azure` / `dashboard` / `slate`; the four Chinese political-education ("red patriot" /
"red teaching") templates are intentionally **not** recreated as an international,
English-only academic suite — their crimson/gold aesthetic is available via
`consulting` / `claret` / `scholar`.

Recreation map: mckinsey-style, premium-corp → **consulting**; data-viz-deck,
competition-speech, report-savior → **dashboard**; architecture-deck, operations-deck,
report-massive-* → **azure**; geometric-summary → **geometric**; quarterly-illust →
**indigo**; thesis-formula → **scholar**; top-thesis → **claret**; thesis-novice → sage
/ forest; cute-orange-class → **apricot**. Separately, a Grok-generated AI-news deck →
**midnight** (dark).

## What each theme controls
Palette (background, surface, ink, muted, **accent**, **accent2**, on-accent), heading
and body fonts, and the styling the builder applies: title cover with brand bar + side
panel + accent rule, full-bleed **section dividers**, per-slide **accent edge stripe** +
underlined title + **footer with slide number**, accent bullet marks, **big-number
heroes**, **accent-bar cards**, and **styled tables**. See `references/slide-design.md`.

## Adding a theme
Add one entry to `themes.json` (copy the field set of an existing theme, change the
hex + fonts + `keywords`). It is picked up automatically — no code change, and the
selector reaches it via its `keywords`. Keep good contrast — for a **light** theme use a
dark accent + dark `ink` on a light `bg`; for a **dark** theme (like `midnight`) invert:
a dark `bg`/`surface` with a **light `ink`** and a bright accent (the builder reads
`bg`/`ink` per-theme, so dark mode needs no code change). Use widely available fonts
(Calibri / Arial / Arial Black / Georgia / Trebuchet MS) so the deck renders everywhere.
