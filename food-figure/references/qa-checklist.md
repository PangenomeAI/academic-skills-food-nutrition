# QA Checklist — run before delivering

- [ ] **Error & n:** error bars defined (SD/SEM/CI stated) and n disclosed; n is biological, not technical.
- [ ] **Statistics:** shown consistently (letters or asterisks); the test is named in the legend.
- [ ] **Axes:** start where they should (bars at 0); no misleading truncation; units on every axis; log scales justified and labelled.
- [ ] **Colour:** colourblind-safe palette; no jet/rainbow; survives greyscale (redundant encoding).
- [ ] **Legibility:** labels/ticks readable at final print size; no overlap or clipping.
- [ ] **Message:** one clear conclusion per figure; multi-panel panels share a thread and are labelled a, b, c.
- [ ] **Data fidelity:** the plot matches the underlying numbers; no cherry-picked axis range; distributions shown where they matter (not bar-of-means).
- [ ] **Journal spec:** DPI, column width, file format, and fonts match the target journal (or the stated default); vector where possible, TIFF-LZW for raster.
- [ ] **Self-contained:** legend states what each panel shows, the error type, n, and the test; scale bars on all micrographs.
- [ ] **Cited:** every figure/panel is referenced in the manuscript text in order.
- [ ] **Reproducible:** an editable source (`.svg`/`.pdf`) and the plotting code are kept.

If any item fails, fix it before handing the figure back.
