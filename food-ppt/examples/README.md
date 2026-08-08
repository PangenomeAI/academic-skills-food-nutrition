# food-ppt examples

Sample decks that show the skill end to end. Each is a **deck-spec JSON** (the
reproducible, text source) plus the **editable `.pptx`** built from it.

## polyphenols-antimicrobial-review
A 10-slide journal-club deck built from a real open-access food-science paper:

> Rossi, L., Rocchetti, G., Lucini, L., & Rebecchi, A. (2025). *Antimicrobial Potential
> of Polyphenols: Mechanisms of Action and Microbial Responses — A Narrative Review.*
> **Antioxidants** 14(2):200. https://doi.org/10.3390/antiox14020200 (CC-BY).

- `polyphenols-antimicrobial-review.deck.json` — the deck spec.
- `polyphenols-antimicrobial-review.pptx` — the built, fully editable deck.

Rebuild it with:
```bash
python3 ../scripts/build_pptx.py polyphenols-antimicrobial-review.deck.json \
  --out polyphenols-antimicrobial-review.pptx
```

**What it demonstrates**
- Layout variety: title · section · bullets · two-column · **native table** · references.
- **Everything editable:** every slide has real text runs (`<a:t>`), the data slide is a
  **native PowerPoint table** (editable cells), and there are **zero flattened
  background images** — verified from the `.pptx` XML.
- **Presenter notes on every slide** (10 slides, 10 notes panes).

**Provenance & honesty.** The slide content is grounded in the paper's **published
abstract and metadata** (via OpenAlex/Crossref). In normal use, `food-fetch` + the
`pdf` skill read the **full** open-access PDF; in this sandbox the publisher
bot-blocked the automated PDF pull, so the example draws on the abstract. No numeric
results are claimed beyond what the abstract states — the "Mechanisms at a glance"
table is a conceptual summary of the abstract's described interaction sites, not
invented data. The deck ends with an AI-use disclosure slide, per the suite's rules.
