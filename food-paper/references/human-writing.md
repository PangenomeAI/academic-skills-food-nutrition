# Write Like a Scientist, Not Like a Chatbot

Canonical anti-AI-tell guide for every skill in the suite that writes prose:
`food-paper` (`draft_writer`, `polisher`), `food-research` (`writer`),
`food-deep-research` (`compiler`), and `food-review` (which flags these in others'
manuscripts). Original text; the pattern taxonomy is informed by the MIT-licensed
`humanizer` skill (Siqi Chen) and Wikipedia's "Signs of AI writing", adapted here
for scientific manuscripts — see the repo README Acknowledgements.

## Apply this together with `writing-style.md`
This guide says what to **remove** (the machine tells); **`writing-style.md`** says the
**positive target** — write in the field's **academic register as a human scientist**
(voice/tense, precise terminology, IMRaD logic, measured interpretation). Run **both at
once**: strip the AI tells *and* keep correct academic style. The aim is not generic
"human" prose but **a human scientist writing for the target journal**. Never let a
de-AI edit cost academic correctness (see the "Academic exceptions" below), and never
let academic polish re-introduce a tell.

## What this is — and is not
**This is about writing quality, not disguise.** LLM prose has specific, learnable
tells: inflated significance, vague attribution, stock vocabulary, and hedging so
thick it says nothing. Those are *bad scientific writing* on their own terms, and
removing them makes a manuscript clearer and more honest.

**It is not a way to hide AI involvement.** The suite's **AI-use acknowledgement is
mandatory and unaffected** by anything here (`declarations-guide.md`). Do **not**
rewrite text in order to defeat an AI detector, evade a journal's or institution's
AI policy, or misrepresent who wrote what. If the user asks for that, say plainly
that the disclosure requirement stands and offer the quality edit instead.
(AI detectors are unreliable in both directions — never treat a detector score as a
target or as evidence, and never accuse an author of AI use.)

**Never let a style edit change the science.** Rewriting must not alter any value,
unit, statistical result, direction of effect, citation, or the scope of a claim. If
a cleaner sentence would overstate what was tested, keep the longer sentence. When
in doubt, meaning wins over style (`faithfulness-and-citation.md`).

## Voice calibration (do this first when possible)
Ask for two or three of the author's **own previous papers** and match their register,
sentence rhythm, and habitual terminology. A manuscript that sounds like its authors
beats a generically "well-written" one. With no sample, follow the target journal's
recent articles in the same section type.

---

## 1. Content tells
**Inflated significance.** *underscores/highlights the importance of; plays a
pivotal/crucial/key role; paves the way for; represents a paradigm shift; in the era
of; growing body of evidence; has garnered increasing attention; sheds light on.*
> ✗ Encapsulation has garnered increasing attention, playing a pivotal role in the evolving landscape of functional foods.
> ✓ Encapsulation is used to protect probiotics during storage. Reported survival gains range from 0.5 to 2 log CFU/g (refs).

**Name-dropping and canned notability.** Inflating authority instead of reporting
findings: *published in top-tier/leading journals; renowned researchers; a landmark
study; extensively studied; well-documented in the literature.* Report **what was
found and by whom**, not how famous the venue is.
> ✗ This mechanism has been extensively studied by leading groups in high-impact journals.
> ✓ Three trials have tested this mechanism (refs); two found no effect.

**"-ing" tack-ons that fake depth.** *thereby ensuring…; highlighting the potential
of…; underscoring its role in…; contributing to…; reflecting the growing…*
> ✗ Firmness decreased by 23%, highlighting the potential of HPP to enhance quality attributes.
> ✓ Firmness decreased by 23% (p < 0.05). This is consistent with pectin solubilisation reported by X et al. (2023).

**Vague attribution / weasel words.** *studies have shown; it is widely recognised;
research suggests; many experts agree; some researchers argue; it is generally
accepted.* Every one must become **a specific citation** — this is the grounding
rule, not just style.
> ✗ Studies have shown that polyphenols improve gut health.
> ✓ In a 12-week randomised trial in adults with obesity, X et al. (2024) reported increased *Akkermansia* abundance after 500 mg/day of grape polyphenols.

**Persuasive authority tropes.** *It is well established that…; It is important to
note that…; It should be emphasised that…; Needless to say.* Either the evidence
supports the claim (cite it) or it doesn't (cut it). The phrase adds nothing.

**Promotional adjectives.** *novel, groundbreaking, cutting-edge, remarkable,
promising, excellent, state-of-the-art, rich in (figurative), vibrant.* "Novel"
requires a stated claim of what is new **and** evidence it was not done before, or
it is puffery.

**Formulaic scaffolding.** Outline-shaped "Challenges and Future Prospects" sections
listing generic obstacles (*scalability, cost, regulatory hurdles*) that could be
appended to any paper. Say what **this work** leaves unresolved and what experiment
would resolve it.

**Generic upbeat conclusions.** *opens exciting new avenues; holds great promise;
future research should explore this fascinating area; represents a significant step
forward.* Name the specific open question, or say nothing.

---

## 2. Language and grammar tells
**Stock AI vocabulary.** *delve, intricate, tapestry, landscape (figurative),
testament, showcase, underscore, leverage, foster, garner, realm, pivotal, crucial,
robust (as filler), seamless, meticulous, comprehensive (as filler), multifaceted,
nuanced, holistic, interplay, align with, harness, unlock, myriad.* They cluster —
one is noise, four is a signature.

**Copula avoidance.** *serves as / stands as / represents / constitutes / functions
as* → **is**.
> ✗ Chitosan serves as a promising coating material. ✓ Chitosan is a coating material.

**Negative parallelism.** *Not only… but also…*; *It's not just X, it's Y*; *not X,
but rather Y*; clipped tailing negations (*no guesswork*, *no compromise*).

**Rule-of-three overuse.** Three-item lists where the third is padding — especially
tricolons of adjectives. Two real items beat three invented ones.

**Elegant variation / synonym cycling.** Rotating *sample / specimen / material* for
the same thing to avoid repetition. In science, **one term per concept** — repeat the
exact term. (This is the reverse of general writing advice, and getting it wrong
creates ambiguity about whether two things differ.)

**False ranges.** *from X to Y* pairs that aren't a real spectrum — *from processing
to consumer perception*, *from molecular structure to sustainability*. Use a real
range (*from 4 to 25 °C*) or list the items plainly.

**Hyphenated word-pair overuse.** *data-driven, high-quality, cutting-edge,
state-of-the-art, real-time, end-to-end, long-term* stacked as filler modifiers.

**Filler & stacked hedging.** *it is important to note that; in order to; due to the
fact that; at this point in time; has the ability to; it could potentially possibly
be argued that.*
> ✗ It could potentially possibly be suggested that the treatment might have some effect.
> ✓ The treatment reduced lipid oxidation (p = 0.03). *(Keep one accurate hedge, not four.)*

**Manufactured drama and aphorisms.** Staccato fragments for effect (*The result?
Total inhibition.*), punchline rhythm, and aphorism formulas (*X isn't just Y — it's
Z*; *The difference isn't A. It's B.*). No place in a manuscript.

**Conversational rhetorical openers.** *Ever wondered why…? Let's dive in. Here's the
thing. What does this mean for…?* Cut entirely.

**Signposting.** *In this section, we will discuss…; As mentioned earlier;
Having established X, we now turn to Y.* Journals want the content, not the tour.

---

## 3. Style and formatting tells
- **Em/en dash overuse** as a rhythm device. Occasional use is fine and human; a dash
  in every third sentence is a tell. Follow the journal's house style.
- **Overuse of boldface** for emphasis mid-paragraph; **inline-header vertical
  lists** (`**Scalability:** the process is…`) where prose belongs. Manuscripts are
  prose, not slide decks.
- **Emoji** — never in a manuscript.
- **Title Case headings** unless the journal requires it (`journal-selector` decides,
  not this guide).
- **Curly vs straight quotes/apostrophes** used inconsistently within one document.
- **Fragmented or skipped heading levels**, thematic breaks (`---`) before headings,
  and decorative rules — artifacts of chat rendering.
- **Unusual tables** — tables used to hold prose, or a table where one sentence works.
- **Markdown leaking into a Word/LaTeX manuscript** (`**bold**`, `## Heading`,
  `- bullet`). A chatbot formats in Markdown by default; a `.docx` must carry real
  Word styles instead. This is both a tell and a genuine formatting bug.
- **Pronounced style shifts** between sections — the seam where machine text was
  pasted into human text. Make the register uniform.

---

## 4. Chatbot artifacts — delete on sight
- **Collaborative communication:** *Certainly! Here's the revised section…; I hope
  this helps; Let me know if you'd like me to expand; Would you like me to…* Nothing
  addressed to the user belongs in the manuscript.
- **Sycophancy:** *That's an excellent point; Great question.*
- **Knowledge-cutoff disclaimers and speculative gap-filling:** *As of my last
  update…; As an AI language model…; While I don't have access to the full text…*
  If a source wasn't read, say so in the limitations — don't narrate the model.
- **Unfilled placeholder / phrasal templates:** `[Insert institution]`,
  `[Your Name]`, `[add citation here]`, *I hope this message finds you well*. Our own
  `[NEEDS DATA]` / `[EVIDENCE GAP]` markers are deliberate — but they must be
  resolved before submission, never shipped.
- **Leftover tool/citation tokens** — a dead giveaway and a broken document. Search
  the text for and remove: `oaicite`, `oai_citation`, `contentReference`,
  `turn0search…`, `turn0news…`, `citeturn`, `attached_file`, `grok_card`,
  `attributionIndex`, `attributableIndex`, `:::writing`, and `utm_source=` tracking
  parameters pasted into reference URLs.

---

## 5. Citation and reference tells (highest stakes)
LLM-fabricated references are the tell that ends careers, not just credibility. These
overlap the suite's four-gate citation check — run
**`scripts/verify_citations.py`** and treat every hit as blocking
(`faithfulness-and-citation.md`).
- **Unresolvable DOIs / invalid ISBN checksums** — a strong hallucination signal.
- **DOIs that resolve to an *unrelated* article.** The most dangerous case: the
  reference looks plausible and the DOI is real, but it belongs to a different paper.
  A DOI that resolves is **not** enough — confirm the resolved title, authors, year,
  and journal match the reference **and** that the source actually supports the claim.
- **Plausible-but-invented references:** real authors + real journal + real-looking
  volume/pages that don't exist. Verify against Crossref/PubMed, not memory.
- **Book citations with no page numbers, edition, or publisher**; page ranges that
  don't exist.
- **References in the list that are never cited in the text** (or in-text citations
  missing from the list).
- **Broken external links**, and URLs carrying `utm_source=`/tracking junk copied
  from a browser session.
- **Citation stacking** — three or four references appended to a generic sentence
  without any of them being specifically relevant.
- **Style mismatch within the reference list** — half author–date, half numbered —
  from text assembled out of different generations.

---

## Academic exceptions — do NOT "fix" these
General-purpose humanising rules misfire on manuscripts. Leave these alone:
- **Passive voice in Methods.** "Samples were homogenised for 60 s" is correct and
  often required. Prefer active elsewhere where the journal allows.
- **Calibrated hedging.** *may, suggests, is consistent with, under these conditions*
  carry real scientific meaning. Cut hedge **stacking**, never scientific caution —
  de-hedging into a confident claim the data don't support is a **fabrication-grade
  error**, worse than clumsy prose.
- **Journal-mandated form.** Heading case, boldface, structured-abstract headings,
  em-dash policy, and section order come from the target journal
  (`journal-selector`), not from this guide. A journal that wants Title Case gets
  Title Case.
- **Precise technical terms** that resemble AI vocabulary: *matrix, significant*
  (statistical sense), *robust* (of a method), *characterise*, *interplay* (of real
  interacting factors). The tell is the **figurative** use.
- **Repetition of a defined term**, standard formulae, and reporting conventions
  (mean ± SD, n =, p =).
- **Quoted material, titles, and the reference list** — never rewrite inside them.
- **An occasional em dash, "however", or curly quote.** Word and most editors curl
  quotes automatically. Isolated, these mean nothing.

## Ineffective indicators — do not "correct" prose on these alone
Perfect grammar and polish · formal or academic vocabulary · dryness · a
non-native-English author's register · common transition words in isolation · one
short emphatic sentence · correct, consistent formatting · a letter-style opening in
a cover letter · unsourced claims (most drafts start that way).

Judge by **clusters**, not single hits: one *however* is nothing; "delve into the
intricate landscape" plus "studies have shown" plus a "promising avenues" ending plus
an unresolvable DOI is a machine talking.

## Two-pass check (run before internal review)
1. **Draft**, then reread against §1–5 above.
2. Ask explicitly: **"What in this text still reads as machine-written?"** List what
   you find — inflated significance, unattributed claims, stock vocabulary, leftover
   tokens, an even mid-length cadence.
3. **Revise** those specific spots. Then verify no number, hedge, claim scope, or
   citation changed in the process, and that `scripts/verify_citations.py` passes.

## Preserve these — they read human because they are
Specific values and conditions (cultivar, batch, 4 °C, 21 days); honest, unresolved
tension ("we cannot rule out that…"); concrete methodological detail; **varied
sentence length** (AI drifts to an even mid-length cadence); plain *is/are/has*;
limitations in the authors' own terms; an argument the authors can defend and explain.
