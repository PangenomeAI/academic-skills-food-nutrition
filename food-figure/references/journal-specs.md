# Journal Figure Specs

Export figures to the target journal's requirements. When a journal is set, get
its spec from the journal skill; otherwise use the defaults below.

## How to get the spec
1. Resolve the target journal via the **`journal-selector`** procedure (`journal-selector/SKILL.md`).
2. Read that journal skill's `## Formatting constraints` block — use
   `figure_dpi`, `column_widths_mm` (or `_cm`), and any format requirement
   (e.g. RSC/ACS **TOC graphic**, MDPI **≥1000 dpi line art**, Nature accessible
   palette + ~180 mm double column).
3. Apply DPI, width, font, and file format **before** export.

## Defaults (no journal set)
- **Raster DPI:** ≥300 dpi (halftone), ≥1000 dpi (line art).
- **Widths:** single ~90 mm, double ~190 mm (≈83/171 mm for some publishers).
- **Format:** vector (PDF/SVG/EPS) for line/bar/scatter; **TIFF (LZW)** for
  raster/microscopy; keep an editable source.
- **Fonts:** Arial/Helvetica, 7–9 pt at final size; embed fonts.
- **Colour:** RGB for online; colourblind-safe palette.

## Common publisher notes
- **Nature Portfolio:** RGB, ~180 mm double column, accessible palette (avoid red/green), ≥300 dpi.
- **Elsevier:** ~90/190 mm; vector preferred; halftone ≥300 dpi, line art ≥1000 dpi.
- **ACS / RSC:** require a **TOC/graphical-abstract** image at the specified size.
- **MDPI:** figures near first citation; ≥1000 dpi line art.

Always confirm exact numbers at the journal skill / author guide before final export.
