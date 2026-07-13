# AI Image Route Test — Synthetic Concept Only

## Test scope

The tested route was a non-data graphical abstract for an illustrative concept:
a pectin coating forms a protective barrier around blueberries during chilled
storage. The prompt used the four layers in `references/ai-image-generation.md`:
concept boundary, global layout, three explicit sections, and flat-academic style
constraints. It prohibited text, numerical values, axes, fabricated mechanisms,
logos, and branding.

## Result

The configured built-in image service returned **HTTP 403 Forbidden**. No image
was produced, assessed, retained, or represented as a generated asset. This is an
environment/access failure, not evidence of prompt quality.

## Optimisation incorporated after the test

- Start with a no-text compositional draft; add any required labels later in a
  controlled vector editor. This avoids unreliable image-model typography.
- Convert the layout into a compact JSON geometry specification before rendering.
  It makes box/arrow relationships auditable and permits deterministic redraw.
- Treat generated output as a draft that needs a content-boundary and visual QA
  check. Reject any generated data, axes, numbers, unsupported causal detail,
  branding, or illegible text.
- Record the model, date, prompt/spec, source basis, and human edits in a
  schematic trace card; disclose permitted AI assistance in the manuscript.

## Retest recommendation

When an authorised image service is available, run the same text-free prompt,
inspect it at final output size, then create a labelled vector version from the
approved geometry. The regenerated visual must remain explicitly illustrative
unless its underlying conceptual claims are supported and cited in the manuscript.
