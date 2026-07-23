# Writing Quality Check (self-review before internal review)

Run over the draft; fix before handing to `internal_reviewer`.

## Claims & evidence
- [ ] Every claim traces to a specific result or cited source; none beyond the data.
- [ ] Interpretation kept out of Results; Results state the numbers, not just "see Fig. 2".
- [ ] Limitations stated; no overreach in Discussion/Conclusion.

## Reporting completeness (food/nutrition)
- [ ] n (biological) and error type on every mean; statistical test named and appropriate.
- [ ] Methods reproducible: source/cultivar/breed/batch, prep, storage, instrument settings, LOD/LOQ, recovery.
- [ ] Units SI and consistent; composition basis stated; log CFU/g for microbes.

## Structure & style
- [ ] Sections and limits match the target journal (or APA 7.0 default).
- [ ] Abstract matches its required type (structured/unstructured) and word count.
- [ ] Every figure/table cited in order with a self-contained legend.
- [ ] Abbreviations defined once; terminology consistent; tenses correct.

## Reads like a scientist, not a chatbot (`human-writing.md`)
- [ ] No inflated significance ("pivotal role", "paves the way", "growing attention"); no "-ing" tack-ons ("highlighting the potential of…").
- [ ] No vague attribution — every "studies have shown" replaced by a specific citation.
- [ ] No stock AI vocabulary ("delve", "intricate", figurative "landscape", "testament", "showcase", "underscore"); no "serves as" where "is" works.
- [ ] No promotional adjectives ("novel"/"groundbreaking" without a supported claim); no generic upbeat ending ("opens exciting avenues").
- [ ] Filler and **stacked** hedges cut — but calibrated hedging, passive Methods, and journal-mandated form **kept**.
- [ ] Sentence length varies; one term per concept (no synonym cycling).
- [ ] Two-pass check run ("what still reads as machine-written?"), and **no number, claim scope, or citation changed** by the style edit.

## Anti-patterns to remove
- Vague quantifiers ("significantly higher" without the number/test).
- Bar-of-means where a distribution matters (fix in `food-figure`).
- Redundant restatement of Results in the Discussion.
- Undefined jargon; inconsistent naming of the same construct.
- `[NEEDS DATA]` / `[EVIDENCE GAP]` placeholders left in the text.

## Title page & declarations present (`declarations-guide.md`)
- [ ] **Title page:** author list (correct order) + affiliations + corresponding author with email; ORCIDs / equal-contribution notes where relevant.
- [ ] Competing interests, funding, CRediT, data availability, ethics/food-safety, AI-use disclosure.
- [ ] **No invented author data** and **no unanswered `[NEEDS: …]` placeholder** — every author/affiliation/COI/funding/ethics item came from the user or was asked for, never fabricated.
