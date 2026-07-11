---
name: journal-selector
description: "Resolve a target food/nutrition journal to its author-guideline skill and formatting constraints. Use at the start of writing, formatting, or submission-prep for a food-science paper, and whenever the user names a journal they want to publish in or format their manuscript for, to load that journal's rules (word/abstract limits, structure, reference/citation style, figure spec). Triggers: which journal, target journal, publish on <journal>, publish in <journal>, I want to publish on <journal>, submit to <journal>, format for a journal, format my manuscript for <journal>, edit the manuscript based on <journal> style, <journal> style, <journal> reference style, <journal> citation style, submission guidelines, prepare for submission, pick a journal."
metadata:
  version: "0.1.0"
  verified: "2026-07"
  related_skills: [academic-paper, academic-pipeline, food-figure]
---

# Journal Selector — Route a Manuscript to Its Journal Skill

Maps a target journal to the correct `journals/<folder>` author-guideline skill
and returns its `## Formatting constraints`. Full authoritative mapping of all 60
journals: [`journals/_coverage.md`](../journals/_coverage.md).

## Behavior

1. **Determine the target journal.** If the author has already named a journal
   (full name or JCR abbreviation), resolve it. If not, **ask**:
   > "Which journal are you targeting? (name or JCR abbreviation — e.g. Food
   > Chemistry, LWT, Nature Food). If undecided, say 'generic' and I'll use
   > standard food-science conventions."
2. **Resolve** the journal to its skill folder using the alias table below (or
   `journals/_coverage.md`). Match case-insensitively on full name or abbreviation.
3. **Load** `journals/<folder>/SKILL.md` and return its `## Formatting constraints`
   block plus the checklist. Note any per-journal override row in that skill's
   "Applies to" table (limits can differ within a publisher group).
4. **Hand off:** the calling pipeline applies these constraints to structure,
   word/abstract limits, and reference style, and passes `figure_dpi` /
   `column_widths_*` to the `food-figure` skill.
5. **If 'generic' or unresolved:** use standard food-science conventions
   (IMRaD; abstract ≤250 words; numbered or author–date references; figures
   ≥300 dpi; ~90/190 mm columns) and state the assumption so the author can
   correct it.

## Resolution table (journal / abbreviation → skill folder)

- **nature-food** — Nature Food (NAT FOOD); npj Science of Food (NPJ SCI FOOD)
- **food-chemistry** — Food Chemistry (FOOD CHEM)
- **j-dairy-science** — Journal of Dairy Science (J DAIRY SCI)
- **elsevier-food** — Trends in Food Science & Technology; Food Hydrocolloids;
  Food Hydrocolloids for Health; Food Packaging and Shelf Life; Global Food
  Security; Current Opinion in Food Science; Food Chemistry-X; Future Foods;
  Food Research International; Current Research in Food Science; Postharvest
  Biology and Technology; Innovative Food Science & Emerging Technologies; LWT;
  Food Control; Journal of Agriculture and Food Research; Applied Food Research;
  Meat Science; Food Policy; Food Bioscience; Food Structure; Journal of Food
  Engineering; International Journal of Food Microbiology; Food Quality and
  Preference; Food Chemistry: Molecular Sciences; Food Microbiology; Journal of
  Food Composition and Analysis; Microbial Risk Analysis; Journal of Functional
  Foods; Journal of Cereal Science
- **wiley-food** — Comprehensive Reviews in Food Science and Food Safety; Food
  Frontiers; eFood; Legume Science; Food and Energy Security; Molecular
  Nutrition & Food Research; Journal of Food Biochemistry; Food Science &
  Nutrition
- **springer-food** — Food Engineering Reviews; Food and Bioprocess Technology;
  Food Security; Food Production Processing and Nutrition
- **crit-rev-food** — Critical Reviews in Food Science and Nutrition; Food
  Reviews International; International Journal of Food Properties
- **foods-mdpi** — Foods; Antioxidants; Toxins
- **food-function** — Food & Function; Sustainable Food Technology
- **jafc** — Journal of Agricultural and Food Chemistry
- **annu-rev-food** — Annual Review of Food Science and Technology (invited only)
- **food-quality-safety** — Food Quality and Safety (Oxford)
- **british-food-journal** — British Food Journal (structured abstract required)
- **j-future-foods** — Journal of Future Foods; Food Science and Human Wellness
- **qas-crops-foods** — Quality Assurance and Safety of Crops & Foods
- **agri-food-security** — Agriculture & Food Security (BMC declarations block)

## Output contract
Return: `{journal, publisher, skill_folder, reference_style, abstract_words,
figure_spec, notes}` drawn from the resolved skill's constraints block, so the
paper pipeline and `food-figure` can consume it directly.
