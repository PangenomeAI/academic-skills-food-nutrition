# Data → Figure — recommendation rules

Given the data profile (from `scripts/analyze_data.py` or elicited from the
user), pick the figure that makes the paper's claim most directly. These are the
rules the script encodes; use them to explain and, where the script is unsure, to
decide. Full catalog: `chart-types.md`. Food-specific recipes: `food-recipes.md`.

## Profile the data first
Identify, per variable: type (numeric / categorical / datetime), cardinality,
missingness, and role — **grouping factor** (categorical, 2–12 levels, repeated),
**time axis** (day/week/hour/date), **dose/condition axis** (dose/conc/temp/pH),
**subject/sample id**, and **response(s)** (the measured numerics). Count the
responses: **≥4 numeric responses = a multivariate/wide matrix**.

## Rules (most common food & nutrition shapes)
| Data shape | Recommend | Why / alternative |
|---|---|---|
| 1 grouping factor × 1 response, few obs/level | **grouped bar + error bars + significance letters** | means with SD/SEM + post-hoc letters |
| 1 grouping factor × 1 response, many obs/level (≥~8) | **box/violin + jittered points** | show the distribution, not just the mean |
| time axis × response (± group) | **line / kinetic curve** | trend over storage/time; microbial growth/survival, drying |
| dose/condition axis × response | **dose–response curve** | fit/overlay a model (e.g. Weibull/Gompertz for microbial) |
| 2 numeric responses | **scatter + regression** | relationship; if same quantity by two methods → **Bland–Altman** (agreement, not correlation) |
| 1 numeric response only | **histogram / density (+ box)** | distribution of a single variable |
| wide matrix (≥4 responses) × samples/groups | **PCA / PLS-DA** (+ **clustered heatmap**) | metabolomics, volatiles, composition; colour by group |
| many attributes per sample (sensory profile) | **radar / spider** | compare full sensory/attribute profiles across samples |
| proportions that sum to a whole | **stacked bar** | avoid pie charts |
| effect sizes + CI across studies | **forest plot** | meta-analysis / systematic review |
| time-to-event | **survival / Kaplan–Meier curve** | shelf-life, spoilage onset |
| structure/appearance | **microscopy image plate** | SEM/CLSM/light micrographs with scale bars |

## Guardrails
- Never a **bar-of-means** where the distribution matters — use box/violin + points.
- Don't imply a trend across an **unordered categorical** with a line.
- Prefer the **fewest** panels that tell the story; combine only related panels.
- If the shape is ambiguous, start with a summary table + simple bar and clarify
  the claim before committing.
