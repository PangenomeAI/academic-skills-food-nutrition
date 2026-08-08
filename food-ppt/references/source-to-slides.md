# Source → Slides

How to turn a source document into a slide outline. Read the source, don't guess.

## Accept any common input format
Read whatever the user brings; extract clean text (and tables/figures where present):

| Input | How to read it |
|---|---|
| **Word `.docx`** (`.doc`, `.odt`, Pages) | the **`docx` skill** (or a Word-capable tool); pull headings, paragraphs, tables, and embedded figures |
| **PDF** | the **`pdf` skill**; if a PMC/OA source, prefer clean structured text (see `food-fetch/references/format-reading.md`) |
| **Markdown `.md` / `.markdown`** | read directly; headings → sections, tables → native tables, image links → figures |
| **Plain text `.txt`** | read directly; infer structure from blank-line/heading cues |
| **Directly from a suite skill** | the report/brief/manuscript object handed over by `food-review` / `food-research` / `food-deep-research` / `food-paper` |

Always keep **tables as data** (rows/cells) and **figures as files/links** — never
lose them into prose; they become native tables and picture objects in the deck.
State the detected input format in one line before building.

## Map the source to a narrative arc (one idea per slide)
Pick the arc from the source type:

- **Original research / `food-paper` manuscript:** Title → Background & gap → Aim/
  hypotheses → Methods (brief) → **Results, one finding per slide** (with the key
  figure/table) → Discussion & implications → Limitations → Conclusions → References →
  AI-use disclosure.
- **Literature review / `food-research` · `food-deep-research`:** Title → Scope &
  question → Methods (search, brief) → **Themes, one per slide** → Evidence gaps →
  Conclusions → References → disclosure.
- **`food-review` report:** Title → Overall assessment → **Editorial decision** →
  Major concerns grouped by theme (one slide each) → Figure/table consistency issues →
  Recommended actions / residual items → disclosure.

## Size to the audience
Journal club ~10–15 · conference ~8–12 · group meeting ~10 · thesis defense ~20–30.
Merge thin points; split any slide carrying more than one idea. Prefer **layout
variety** (title / section / bullets / two-column / figure / table / references), not
wall-to-wall bullets.

## Ground everything
Every planned slide point must exist in the source. Don't pad the deck with generic
slides ("Introduction to the field") the source doesn't support, and don't drop a
load-bearing result to hit a slide count.
