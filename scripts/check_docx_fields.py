#!/usr/bin/env python3
"""Detect reference-manager FIELD CODES that leaked into the visible text of a .docx.

EndNote / Zotero / Mendeley / Word store each in-text citation as a Word *field*:
the code (e.g. ``ADDIN EN.CITE <EndNote>...</EndNote>``) lives in ``<w:instrText>``
and Word shows only the formatted citation ``(Author, Year)``. If an editing tool
flattens the field — concatenating every run and rewriting the paragraph as plain
``<w:t>`` text — the hidden code lands in the visible body, e.g.::

    ADDIN EN.CITE <EndNote><Cite><Author>Ghosh</Author>...</EndNote>(Ghosh & Sil, 2013)

This checks the *visible* text (``<w:t>``, not ``<w:instrText>``) for such markers,
so an intact field passes and a leaked one fails.

Usage:
    check_docx_fields.py manuscript.docx      # exit 1 if leaked field codes found
    check_docx_fields.py --selftest
"""
import re
import sys
import zipfile
from xml.etree import ElementTree as ET

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"

# Markers that only ever belong inside a field instruction, never in visible prose.
MARKERS = re.compile(
    r"ADDIN\s+EN\.(?:CITE|REF|REFLIST)"
    r"|ADDIN\s+ZOTERO"
    r"|ADDIN\s+Mendeley"
    r"|CSL_CITATION"
    r"|MENDELEY_CITATION"
    r"|</?EndNote>"
    r"|<Cite>",
    re.IGNORECASE,
)

BODY_PART_RE = re.compile(r"word/(?:document|footnotes|endnotes|header\d*|footer\d*)\.xml$")


def visible_text_hits(xml_bytes):
    """Return leaked marker snippets found in <w:t> (visible) runs of one part."""
    hits = []
    root = ET.fromstring(xml_bytes)
    for el in root.iter(W + "t"):
        if el.text and MARKERS.search(el.text):
            hits.append(el.text.strip()[:120])
    return hits


def scan_docx(path):
    """Return list of (part_name, snippet) for every leaked field code in visible text."""
    z = zipfile.ZipFile(path)
    hits = []
    for name in z.namelist():
        if BODY_PART_RE.search(name):
            for snip in visible_text_hits(z.read(name)):
                hits.append((name, snip))
    return hits


def selftest():
    # Leaked: the field instruction ended up inside a visible <w:t> run.
    leaked = (
        f'<w:document xmlns:w="{W[1:-1]}"><w:body><w:p><w:r><w:t>'
        "ADDIN EN.CITE &lt;EndNote&gt;&lt;Cite&gt;&lt;Author&gt;Ghosh&lt;/Author&gt;"
        "&lt;/EndNote&gt;(Ghosh &amp; Sil, 2013)</w:t></w:r></w:p></w:body></w:document>"
    ).encode("utf-8")
    assert visible_text_hits(leaked), "should flag a leaked field code in <w:t>"

    # Intact: code is in <w:instrText>; only the citation shows in <w:t>.
    intact = (
        f'<w:document xmlns:w="{W[1:-1]}"><w:body><w:p>'
        '<w:r><w:fldChar w:fldCharType="begin"/></w:r>'
        "<w:r><w:instrText> ADDIN EN.CITE &lt;EndNote&gt;&lt;/EndNote&gt; </w:instrText></w:r>"
        '<w:r><w:fldChar w:fldCharType="separate"/></w:r>'
        "<w:r><w:t>(Ghosh &amp; Sil, 2013)</w:t></w:r>"
        '<w:r><w:fldChar w:fldCharType="end"/></w:r>'
        "</w:p></w:body></w:document>"
    ).encode("utf-8")
    assert visible_text_hits(intact) == [], "an intact field must NOT be flagged"

    print("OK: check_docx_fields selftest passed")


def main(argv):
    if "--selftest" in argv:
        selftest()
        return 0
    args = [a for a in argv[1:] if not a.startswith("--")]
    if not args:
        print("usage: check_docx_fields.py <file.docx> | --selftest")
        return 2
    hits = scan_docx(args[0])
    if hits:
        print(f"FAIL: {len(hits)} leaked citation field code(s) in visible text — "
              "an edit flattened a reference-manager field; restore the field or "
              "remove the stray code before delivering:")
        for part, snip in hits:
            print(f"  ✗ {part}: {snip}")
        return 1
    print("OK: no EndNote/Zotero/Mendeley field codes leaked into visible text.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
