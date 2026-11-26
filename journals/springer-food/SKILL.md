---
name: springer-food
description: "Shared author-guideline skill for Springer / Springer Nature food journals: Food Engineering Reviews, Food and Bioprocess Technology, Food Security, and the SpringerOpen journal Food Production Processing and Nutrition. Use to format or check a manuscript for a Springer food journal — structure, abstract/keyword limits, Springer reference styles, and figure specs. Triggers: submit to Food and Bioprocess Technology, Food Security, Food Engineering Reviews guidelines, Springer food formatting. Also fires when the user wants to publish on/in this journal, format a manuscript for it, or match its reference/citation style."
metadata:
  publisher: "Springer / Springer Nature"
  verified: "2026-11 partial"
  source: "https://www.springer.com/gp/authors-editors/journal-author"
---

# Springer Food Journals — Shared Author Guideline Skill

> **Verification status:** **Partly verified** — SpringerLink guidelines for Food and Bioprocess Technology, Food Security, Food Engineering Reviews, European Journal of Nutrition and the IJO guide on nature.com read 2026-11-27. All other titles **not verified**.
> Anything not confirmed must be checked at the journal's guide before submission. Tell the
> author so, and ask them to paste or upload the current guide if it cannot be read.

**Publisher:** Springer / Springer Nature · Confirm each journal's "Submission guidelines" on SpringerLink. Structure below reflects the common Springer template.

## Applies to
| Journal | Abbrev | Type focus | Access | Ref style* |
|---|---|---|---|---|
| Food Engineering Reviews | FOOD ENG REV | Reviews | Subscription | **numbered, square brackets** |
| Food and Bioprocess Technology | FOOD BIOPROCESS TECH | Research | Subscription | author–date |
| Food Security | FOOD SECUR | Research + reviews (policy/agri) | Subscription | author–date |
| Food Production Processing and Nutrition | FOOD PROD PROCESS NU | Research (SpringerOpen) | Gold OA | numbered (Vancouver) |

*Style differs by journal — check the table, never assume one Springer default.

## Common Springer structure
Title page → Abstract → Keywords → Introduction → Materials and Methods → Results → Discussion → Conclusion → Statements & Declarations (funding, competing interests, ethics, author contributions, data availability) → References → Tables → Figure legends → Figures.

- **Abstract:** unstructured, typically ≤250 words.
- **Keywords:** 4–6.
- **Abstract (FBT, Food Security, FER):** 150–250 words. European Journal of Nutrition: **structured**, 150–250 words.
- **Food Security research articles:** about 8,000 words; Results and Discussion must be **separate** sections.
- **European Journal of Nutrition:** original articles ≤50,000 characters, reviews ≤100,000.
- **Declarations section:** required by Springer (funding, conflicts, ethics approval, consent, data availability, author contributions).

## Reference style
- **Food and Bioprocess Technology, Food Security:** name and year in parentheses **with a comma** — `(Abbott, 1991; Barakat et al., 1995; Kelso & Smith, 1998)`; alphabetical list; FBT asks for APA 7 author-number rules.
- **Food Engineering Reviews, European Journal of Nutrition:** numbers in square brackets `[1]`; consecutively numbered list.
- **Food Production, Processing and Nutrition:** numbered, BMC style.

## Figures & tables
Halftones ≥300 dpi, combination ≥600, line art ≥1200; large-format journals 84 mm or 174 mm wide, ≤234 mm high (small-format 119 mm, ≤195 mm); editable tables; cite in order.

## Submission checklist
- [ ] Correct reference style for the specific journal (see above)
- [ ] Abstract ≤~250 words · [ ] 4–6 keywords
- [ ] Statements & Declarations block (funding, competing interests, ethics, contributions, data availability)
- [ ] Figures ≥300 dpi · [ ] Cover letter

## Also covers — Springer / Springer Nature nutrition journals
Same Springer template (style per journal);
clinical titles add structured abstracts, trial registration, reporting guidelines.

International Journal of Obesity (official guide): abstract ≤300 words (structured for original research); main text ≤4,000 words, ≤6 tables/figures, ≤60 references for original articles. Numbered styles below other than IJO and EJN are from the Citation Style Language repository.

| Journal | Abbrev | Notes |
|---|---|---|
| Current Obesity Reports | CURR OBES REP | Reviews; numbered |
| Current Nutrition Reports | CURR NUTR REP | Reviews; numbered |
| European Journal of Nutrition | EUR J NUTR | Numbered |
| International Journal of Obesity | INT J OBESITY | Numbered |
| Nutrition & Diabetes | NUTR DIABETES | Numbered |
| European Journal of Clinical Nutrition | EUR J CLIN NUTR | Numbered |
| Plant Foods for Human Nutrition | PLANT FOOD HUM NUTR | Numbered |

## Formatting constraints
```yaml
publisher: Springer
scope: food & nutrition
reference_style: per-journal   # see per-journal list
abstract_words: 250
keywords_max: 6
declarations_block: required
figure_dpi: {halftone: 300, line_art: 1200}
column_widths_mm: [84, 174]
```
