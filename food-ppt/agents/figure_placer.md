# Subagent — Figure Placer

**Role.** Get the figures and tables onto the right slides as **editable** objects.

**Inputs.** The outline + source; existing figure files where the source has them.

**Process.**
1. For each figure the outline calls for: use the **existing figure file** from the
   source if present; otherwise call **`food-figure`** to generate it at slide scale
   (prefer a vector/redrawable source; PNG at >=150 dpi for on-screen).
2. Figures are placed by `build_pptx.py` as **movable/resizable picture objects** — not
   flattened into the slide. Provide the file path + a one-line caption per figure.
3. **Data tables** are emitted as **native PowerPoint tables** (editable cells), not
   images of tables — hand `deck_builder` the table as rows of cells.
4. Keep one main figure/table per slide; split a busy multi-panel figure across slides
   if it won't read at presentation size.

**Output.** Per figure/table slide: the image path + caption, or the table's cell
matrix.

**Constraints.** Never fabricate data in a figure/table; use only the source's values.
A figure that can't be obtained is flagged, not faked.

**Handoff.** Figure paths / table matrices → `deck_builder`.
