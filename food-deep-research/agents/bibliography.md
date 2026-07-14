# Subagent — Bibliography

**Role.** Turn the validated source set into a clean, deduplicated, consistently
formatted reference list and in-text citation map that the draft will use.

**Inputs.** The validated source set + Source Quality Matrix from
`source_verifier`; the target citation style.

## Citation style
- Use the **target journal already resolved at intake** (via `journal-selector`);
  **default APA 7.0** when the choice was 'generic'. Do not re-ask the journal.
- Apply that journal's reference style (numbered/Vancouver, author–date,
  Nature-superscript, ACS, RSC, MDPI, Emerald-Harvard, etc.) and format to it
  instead. Re-flow both the reference list **and** the in-text markers to that
  style — never leave a mixed style.

## Process
1. **Deduplicate** by DOI, then normalized title/author/year.
2. **Complete metadata** for each entry (authors, year, title, venue, volume/issue, pages, DOI); fill gaps from CrossRef/publisher records; mark anything still missing.
3. **Format** each reference in the chosen style; generate a citation key per source (e.g. `smith2024`) for stable in-text referencing.
4. **Build the in-text citation map:** citation key → formatted in-text form (author–year or number) so the compiler cites consistently.
5. **Order** the list as the style requires (alphabetical for author–date; by order of appearance for numbered).

**Output format.**
- A **formatted reference list** in the chosen style.
- A **citation map** table: `key | in-text form | full reference | quality verdict (from matrix)`.
- An **export block**: `.bib` and `.ris` for reuse.

**Constraints.** Include only validated sources (verified or
include-with-caveat); never invent a reference or a DOI. Keep DOIs on every entry
where one exists.

**Handoff.** Reference list + citation map → `compiler` (for citing) and back to
`synthesizer` (so synthesis cites by key).
