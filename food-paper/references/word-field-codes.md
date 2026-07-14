# Preserving citation field codes when editing a Word manuscript

Reference managers — **EndNote, Zotero, Mendeley, and Word's own citation tool** —
insert each in-text citation as a Word **field**, not as plain text. In OOXML a
field is a *complex field* spread across runs:

```xml
<w:r><w:fldChar w:fldCharType="begin"/></w:r>
<w:r><w:instrText xml:space="preserve"> ADDIN EN.CITE &lt;EndNote&gt;…&lt;/EndNote&gt; </w:instrText></w:r>
<w:r><w:fldChar w:fldCharType="separate"/></w:r>
<w:r><w:t>(Ghosh &amp; Sil, 2013)</w:t></w:r>   <!-- the only part Word shows -->
<w:r><w:fldChar w:fldCharType="end"/></w:r>
```

The `w:instrText` is the field **code** (EndNote's XML record / Zotero's
`CSL_CITATION` JSON) — Word hides it and uses it to rebuild the bibliography. Only
the text between `separate` and `end` is visible.

## The bug to avoid
If you read a paragraph by concatenating **every** run — including `w:instrText` —
and then rewrite the paragraph as plain `w:t` runs, the hidden code becomes visible
body text, producing a stray block like:

```
ADDIN EN.CITE <EndNote><Cite><Author>Ghosh</Author>…</EndNote>(Ghosh & Sil, 2013)
```

right before the real citation. **Never flatten a field into visible text.**

## Rules
1. **Treat each citation field as one opaque, atomic unit.** Do not split it,
   inline it, reflow it, or convert its `w:instrText` into `w:t`. Edit the prose
   *around* it, never inside it.
2. **When extracting text** (for reading, analysis, or round-trip editing), **skip
   `w:instrText`** and read only the display text (between `fldChar separate` and
   `end`). Simple fields (`w:fldSimple`) work the same way — read the `w:t`, not the
   `w:instr` attribute.
3. **When applying tracked changes**, wrap `w:ins`/`w:del` around whole runs; keep
   the `fldChar begin / separate / end` runs together and in order. Never put a
   field instruction inside a `w:t`.
4. **Prefer the `docx` skill**, which preserves fields. If a tool cannot preserve
   them, **do not paste the raw instruction** — keep only the display citation and
   **warn the author** that live EndNote/Zotero/Mendeley fields were downgraded to
   static text (the bibliography will no longer auto-update on their machine).
5. Applies equally to **comments** (`../../food-review/references/word-review-comments.md`),
   **tracked-change revision** (`revision-response.md`), and **format conversion**.

## Verify before delivering
Run `scripts/check_docx_fields.py <file>.docx`. It fails if any field code
(`ADDIN EN.CITE`, `CSL_CITATION`, `<EndNote>`, `ADDIN ZOTERO`, …) leaked into the
visible text. Fix every hit — restore the field or delete the stray code — before
sending the file (alongside `scripts/privacy_scan.py`).
