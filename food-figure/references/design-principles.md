# Design Principles

## Colour
- **Colourblind-safe by default.** Use the Okabe–Ito palette:
  `#000000 #E69F00 #56B4E9 #009E73 #F0E442 #0072B2 #D55E00 #CC79A7`.
- Never `jet`/rainbow for continuous data — use perceptually uniform maps
  (viridis, cividis, magma). Avoid red/green as the only contrast.
- Sequential data → sequential map; diverging data (around a midpoint) → diverging
  map; categorical → the qualitative palette above.
- Encode redundantly (colour + shape/linetype) so the figure survives greyscale.

## Typography
- Sans-serif (Arial/Helvetica), ~7–9 pt at final print size; keep all text legible
  when the figure is scaled to the journal column width.
- Embed fonts in vector output (`pdf.fonttype=42`, `svg.fonttype="none"`).
- Define units on every axis; abbreviations consistent with the manuscript.

## Axes & honesty
- Bar charts start at zero; do not truncate axes to exaggerate differences.
- Log axes only where the science warrants (microbial counts, rheology); label clearly.
- Show error (SD/SEM/CI) and state which; show n. Show the statistic consistently
  (letters or asterisks) and name the test in the legend.

## Layout
- One message per figure; multi-panel only for a shared thread; align and share axes.
- Minimise chartjunk (no 3-D bars, no gratuitous gridlines/shadows).
- Legends inside the plot area when space allows; label directly for few series.

## Reproducibility
- Generate figures from code (no hand-editing pixels); keep the script with the data.
- Set a random seed where jitter/simulation is involved.
