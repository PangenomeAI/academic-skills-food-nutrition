#!/usr/bin/env python3
"""Build a fully EDITABLE PowerPoint (.pptx) from a deck-spec JSON.

Everything on every slide is a native, editable object: titles and body text are real
text frames, tables are native PowerPoint tables (editable cells), and figures are
embedded as movable/resizable picture objects. Nothing is flattened to a background
image. Speaker notes are written to each slide's notes.

Requires python-pptx (`pip install python-pptx`). The spec validator is stdlib-only so
it (and `--selftest`) run without python-pptx installed.

Deck-spec JSON:
{
  "title": "...", "subtitle": "...", "authors": "...", "date": "...", "aspect": "16:9",
  "slides": [
    {"layout": "title",   "title": "...", "subtitle": "...", "authors": "...", "notes": "..."},
    {"layout": "section", "title": "..."},
    {"layout": "bullets", "title": "...", "bullets": ["a", ["subpoint"], "b"], "notes": "..."},
    {"layout": "two_column", "title": "...", "left": ["..."], "right": ["..."]},
    {"layout": "figure",  "title": "...", "image": "fig.png", "caption": "...", "notes": "..."},
    {"layout": "table",   "title": "...", "table": [["H1","H2"], ["a","b"]], "notes": "..."},
    {"layout": "references", "title": "References", "items": ["..."]}
  ]
}

Usage:
  build_pptx.py deck.json --out deck.pptx
  build_pptx.py --selftest
"""
import json
import os
import sys
import zipfile

LAYOUTS = {"title", "section", "bullets", "two_column", "figure", "table", "references"}


def validate_spec(spec):
    """Return a list of problems (stdlib only). Empty list == valid."""
    problems = []
    if not isinstance(spec, dict):
        return ["spec must be a JSON object"]
    slides = spec.get("slides")
    if not isinstance(slides, list) or not slides:
        return ["spec.slides must be a non-empty list"]
    for i, s in enumerate(slides):
        if not isinstance(s, dict):
            problems.append(f"slide {i}: not an object"); continue
        lay = s.get("layout")
        if lay not in LAYOUTS:
            problems.append(f"slide {i}: layout '{lay}' not in {sorted(LAYOUTS)}")
        if lay in ("bullets",) and not s.get("bullets"):
            problems.append(f"slide {i} (bullets): missing 'bullets'")
        if lay == "figure":
            if not s.get("image"):
                problems.append(f"slide {i} (figure): missing 'image'")
        if lay == "table":
            t = s.get("table")
            if not (isinstance(t, list) and t and all(isinstance(r, list) for r in t)):
                problems.append(f"slide {i} (table): 'table' must be a list of rows")
        if lay == "references" and not s.get("items"):
            problems.append(f"slide {i} (references): missing 'items'")
    return problems


# ---------- python-pptx build (only imported when actually building) ----------
def build(spec, out_path):
    from pptx import Presentation
    from pptx.util import Inches, Pt
    from pptx.enum.text import PP_ALIGN
    from pptx.dml.color import RGBColor

    ACCENT = RGBColor(0x2F, 0x5D, 0x62)   # muted teal; academic, brand-neutral
    INK = RGBColor(0x1A, 0x1A, 0x1A)
    MUTED = RGBColor(0x55, 0x55, 0x55)

    prs = Presentation()
    prs.slide_width = Inches(13.333)      # 16:9
    prs.slide_height = Inches(7.5)
    blank = prs.slide_layouts[6]          # truly blank; we place every shape ourselves
    W, H = prs.slide_width, prs.slide_height

    def add_slide():
        return prs.slides.add_slide(blank)

    def textbox(slide, l, t, w, h):
        tb = slide.shapes.add_textbox(l, t, w, h)
        tb.text_frame.word_wrap = True
        return tb.text_frame

    def set_para(p, text, size, bold=False, color=INK, level=0, align=None):
        p.text = text
        p.level = level
        for r in p.runs:
            r.font.size = Pt(size); r.font.bold = bold; r.font.color.rgb = color
        if align is not None:
            p.alignment = align

    def notes(slide, text):
        if text:
            slide.notes_slide.notes_text_frame.text = str(text)

    def title_bar(slide, text):
        tf = textbox(slide, Inches(0.6), Inches(0.4), Inches(12.1), Inches(1.0))
        set_para(tf.paragraphs[0], text, 30, bold=True, color=ACCENT)

    for s in spec["slides"]:
        lay = s["layout"]
        slide = add_slide()

        if lay == "title":
            tf = textbox(slide, Inches(0.8), Inches(2.4), Inches(11.7), Inches(2.0))
            set_para(tf.paragraphs[0], s.get("title", spec.get("title", "")), 40,
                     bold=True, color=ACCENT)
            for extra in (s.get("subtitle") or spec.get("subtitle"),
                          s.get("authors") or spec.get("authors"),
                          s.get("date") or spec.get("date")):
                if extra:
                    set_para(tf.add_paragraph(), extra, 20, color=MUTED)

        elif lay == "section":
            tf = textbox(slide, Inches(0.8), Inches(3.0), Inches(11.7), Inches(1.5))
            set_para(tf.paragraphs[0], s.get("title", ""), 34, bold=True,
                     color=ACCENT, align=PP_ALIGN.CENTER)

        elif lay in ("bullets", "references"):
            title_bar(slide, s.get("title", "References" if lay == "references" else ""))
            tf = textbox(slide, Inches(0.7), Inches(1.6), Inches(11.9), Inches(5.4))
            items = s.get("bullets") if lay == "bullets" else s.get("items", [])
            first = True
            for it in items:
                if isinstance(it, list):          # nested sub-points
                    for sub in it:
                        set_para(tf.add_paragraph(), f"– {sub}", 16, color=MUTED, level=1)
                    continue
                p = tf.paragraphs[0] if first else tf.add_paragraph()
                bullet = it if lay == "references" else f"• {it}"
                set_para(p, bullet, 15 if lay == "references" else 18)
                first = False

        elif lay == "two_column":
            title_bar(slide, s.get("title", ""))
            for col, x in (("left", Inches(0.7)), ("right", Inches(6.9))):
                tf = textbox(slide, x, Inches(1.6), Inches(5.7), Inches(5.4))
                first = True
                for it in s.get(col, []):
                    p = tf.paragraphs[0] if first else tf.add_paragraph()
                    set_para(p, f"• {it}", 18); first = False

        elif lay == "figure":
            title_bar(slide, s.get("title", ""))
            img = s.get("image")
            if img and os.path.exists(img):
                slide.shapes.add_picture(img, Inches(1.2), Inches(1.7), height=Inches(4.6))
            else:
                set_para(textbox(slide, Inches(1.2), Inches(3.0), Inches(10), Inches(1)).paragraphs[0],
                         f"[figure not found: {img}]", 16, color=MUTED)
            if s.get("caption"):
                set_para(textbox(slide, Inches(0.7), Inches(6.5), Inches(11.9), Inches(0.8)).paragraphs[0],
                         s["caption"], 13, color=MUTED)

        elif lay == "table":
            title_bar(slide, s.get("title", ""))
            data = s["table"]
            rows, cols = len(data), max(len(r) for r in data)
            gt = slide.shapes.add_table(rows, cols, Inches(0.7), Inches(1.7),
                                        Inches(11.9), Inches(0.4 * rows)).table
            for r, row in enumerate(data):
                for c in range(cols):
                    cell = gt.cell(r, c)
                    cell.text = str(row[c]) if c < len(row) else ""
                    for p in cell.text_frame.paragraphs:
                        for run in p.runs:
                            run.font.size = Pt(12); run.font.bold = (r == 0)

        notes(slide, s.get("notes"))

    prs.save(out_path)
    return out_path


def selftest():
    spec = {
        "title": "Test Deck", "authors": "A. Author", "slides": [
            {"layout": "title", "title": "T", "subtitle": "S"},
            {"layout": "bullets", "title": "Points", "bullets": ["one", ["sub"], "two"],
             "notes": "speaker note"},
            {"layout": "table", "title": "Data", "table": [["Trt", "Value"], ["A", "1.2"]]},
            {"layout": "references", "title": "References", "items": ["Ref 1", "Ref 2"]},
        ],
    }
    assert validate_spec(spec) == [], validate_spec(spec)
    bad = validate_spec({"slides": [{"layout": "bogus"}, {"layout": "figure"}]})
    assert any("layout 'bogus'" in p for p in bad) and any("missing 'image'" in p for p in bad), bad
    assert validate_spec({}) == ["spec.slides must be a non-empty list"]

    try:
        import pptx  # noqa: F401
    except ImportError:
        print("OK: build_pptx selftest passed (validator only; python-pptx not installed)")
        return
    import tempfile
    out = os.path.join(tempfile.mkdtemp(), "t.pptx")
    build(spec, out)
    # A real .pptx is a zip carrying ppt/presentation.xml; slides hold editable text.
    with zipfile.ZipFile(out) as z:
        names = z.namelist()
        assert "ppt/presentation.xml" in names, names
        s2 = z.read("ppt/slides/slide2.xml").decode("utf-8", "ignore")
        assert "<a:t>" in s2 and "one" in s2, "body text must be native editable runs"
    print("OK: build_pptx selftest passed (validator + editable .pptx built)")


def main(argv):
    if "--selftest" in argv:
        selftest()
        return 0
    args = [a for a in argv[1:] if not a.startswith("--")]
    out = None
    for i, a in enumerate(argv):
        if a == "--out":
            out = argv[i + 1]
    if not args or not out:
        print("usage: build_pptx.py <deck.json> --out <deck.pptx> | --selftest")
        return 1
    spec = json.load(open(args[0]))
    problems = validate_spec(spec)
    if problems:
        print("FAIL: invalid deck spec:")
        for p in problems:
            print("  ✗", p)
        return 1
    path = build(spec, out)
    print(f"OK: built editable {path} ({len(spec['slides'])} slides)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
