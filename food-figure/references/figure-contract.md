# Figure Contract — fix this before any code

State each in one or two lines. Do not plot until they are explicit; if the data
can't fill them, ask.

1. **Conclusion** — the single claim this figure must let a reader reach
   (e.g. "the coating cut weight loss vs control across 14 days").
2. **Evidence logic** — which comparison/trend carries that claim, and the
   controls that make it defensible: replicates (biological n), the error type
   (SD/SEM/CI), and the statistic shown.
3. **Export needs** — the target journal and its figure spec (DPI, column width,
   file format, fonts). Pull these from `journal-specs.md`; if no journal is set,
   default to 300 dpi, ~90/190 mm widths, TIFF+PDF, Arial 7–9 pt.
4. **Review risks** — what a reviewer will attack: missing error bars or n,
   pseudo-replication, truncated/misleading axes, undisclosed statistics, jet
   colormaps, unreadable labels, a bar-of-means hiding a distribution.

One figure = one message. Multi-panel only when panels share a logical thread;
label panels **a, b, c** (lower-case, bold).
