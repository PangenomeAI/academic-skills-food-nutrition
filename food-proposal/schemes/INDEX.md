# Funding-scheme / proposal formats

Built-in proposal formats. Pick one at intake (see `references/scheme-selection.md`);
machine-readable limits are in [`schemes.json`](schemes.json). **If the user's scheme
isn't here, don't guess** — have them upload the scheme's guideline / sample form and
extract it with the `scheme_extractor` subagent into a new file (copy
[`_scheme-template.md`](_scheme-template.md)) + a `schemes.json` entry.

| id | scheme | length limit | required headings |
|---|---|---|---|
| `arc-discovery-eoi` | ARC Discovery Projects — EOI | **≤ 2 A4 pages** | Title · Quality & Innovation · References · Acknowledgements* |
| `arc-discovery-full` | ARC Discovery Projects — Full Application | **≤ 7 A4 pages** | Title · Quality & Innovation · Benefit · Communication of Results · References · Acknowledgements* |
| `uom-major-minor-project` | UoM Ag & Food Major/Minor Research Project | **1500 ± 150 words** (counted sections only) | Cover · Abstract · TOC · Intro · Aims & Objectives · Lit Review · Methods · Acknowledgements · References · Risks · Resources · Timelines |

\* Acknowledgements heading is optional in the ARC schemes.

Each scheme has its own `<id>.md` with the full headings, per-heading questions,
limits, assessment criteria, and source. Add more over time — one `.md` + one
`schemes.json` entry each.
