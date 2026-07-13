# Food-Figure Gallery

This gallery is a runnable end-to-end test of `food-figure`. Every value, study
label, scenario, figure, and caption is **synthetic/illustrative**. None is
evidence, a real experiment, or a result suitable for citation or submission.

Run from the repository root:

```bash
Rscript food-figure/examples/gallery/render_gallery.R
```

The script uses base R and writes vector PDF plus 1800 × 1200 PNG outputs to
`figures/`. On macOS, it uses the built-in `sips` renderer so PNG export also
works when R lacks optional Cairo/X11 components. The source CSV files, captions,
and trace cards are kept alongside the rendering script so each result is
auditable.

| Case | Food & nutrition scenario | Chart types | Files |
|---|---|---|---|
| 1 | Active pectin packaging and blueberry polyphenol retention | Grouped bar; dose-response | `fig1_active_packaging.*` |
| 2 | Refrigerated probiotic survival | Kinetic line | `fig2_probiotic_storage_kinetics.*` |
| 3 | Illustrative yogurt sensory panel profile | Radar | `fig3_sensory_radar.*` |
| 4 | Rapid phenolic assay validation and illustrative evidence summary | Bland–Altman; forest | `fig4_method_validation_and_evidence.*` |

The AI schematic route was also tested with a four-layer food-science prompt.
The image service returned HTTP 403 in this environment, so no AI-generated
asset is included or represented as generated. See `ai-image-test.md`.

For actual research, replace every synthetic CSV with verified study data;
validate statistics and model assumptions; update the trace card; and disclose
any AI use in line with institutional and journal requirements.
