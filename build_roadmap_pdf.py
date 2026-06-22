# -*- coding: utf-8 -*-
"""Render ROADMAP.md into a styled, clickable PDF (clickable index + live links).

A small, purpose-built Markdown renderer for this controlled document. Handles:
H1/H2/H3, horizontal rules, blockquotes, bullet lists (1-level nesting),
GitHub pipe tables, and inline **bold**, *italic*, `code`, [text](url), bare URLs.
"""
import re
import html
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak,
)
from reportlab.platypus.flowables import Flowable

SRC = "ROADMAP.md"
OUT = "AI_ML_Roadmap.pdf"

NAVY = colors.HexColor("#1a2b4a")
BLUE = colors.HexColor("#1456b0")
GREEN = colors.HexColor("#0a7d2c")
GREY = colors.HexColor("#555555")
LIGHT = colors.HexColor("#f3f6fb")
BORDER = colors.HexColor("#cfd8e6")

styles = getSampleStyleSheet()
S = {
    "title": ParagraphStyle("title", parent=styles["Title"], fontSize=24, textColor=NAVY,
                            spaceAfter=6),
    "subtitle": ParagraphStyle("subtitle", parent=styles["Normal"], fontSize=11,
                               textColor=GREY, alignment=1, spaceAfter=2),
    "h2": ParagraphStyle("h2", parent=styles["Heading1"], fontSize=15, textColor=NAVY,
                         spaceBefore=14, spaceAfter=6),
    "h3": ParagraphStyle("h3", parent=styles["Heading2"], fontSize=12, textColor=NAVY,
                         spaceBefore=8, spaceAfter=4),
    "body": ParagraphStyle("body", parent=styles["Normal"], fontSize=9.8, leading=14,
                           spaceAfter=3),
    "bullet": ParagraphStyle("bullet", parent=styles["Normal"], fontSize=9.5, leading=13.5,
                             leftIndent=14, bulletIndent=4, spaceAfter=1.5),
    "bullet2": ParagraphStyle("bullet2", parent=styles["Normal"], fontSize=9.2, leading=13,
                              leftIndent=28, bulletIndent=18, spaceAfter=1.5),
    "note": ParagraphStyle("note", parent=styles["Normal"], fontSize=9, leading=13,
                           textColor=GREY, backColor=colors.HexColor("#fff8e6"),
                           borderColor=colors.HexColor("#e6cf8a"), borderWidth=0.6,
                           borderPadding=6, spaceBefore=4, spaceAfter=4),
    "toc": ParagraphStyle("toc", parent=styles["Normal"], fontSize=10, leading=15),
    "cell": ParagraphStyle("cell", parent=styles["Normal"], fontSize=8.3, leading=11),
    "cellh": ParagraphStyle("cellh", parent=styles["Normal"], fontSize=8.4, leading=11,
                            textColor=colors.white, fontName="Helvetica-Bold"),
}

URL_RE = re.compile(r"(https?://[^\s)>\]]+)")
LINK_RE = re.compile(r"\[([^\]]+)\]\((https?://[^)]+)\)")

# Built-in Helvetica (WinAnsi) lacks these glyphs -> map to safe ASCII.
SAFE_MAP = {
    "→": "->", "⇒": "=>", "←": "<-",
    "≈": "~", "≤": "<=", "≥": ">=",
    "…": "...", "•": "-",
    "×": "x", "−": "-",
}


def safe(text):
    for k, v in SAFE_MAP.items():
        text = text.replace(k, v)
    return text


def slug(text):
    t = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return "sec-" + t[:40]


def inline(md):
    """Convert inline markdown to reportlab mini-HTML markup."""
    # protect existing markdown links first -> placeholder
    links = []

    def _stash(m):
        links.append((m.group(1), m.group(2)))
        return "\x00%d\x00" % (len(links) - 1)

    md = LINK_RE.sub(_stash, md)
    md = safe(md)
    md = html.escape(md, quote=False)
    # bold, italic, code
    md = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", md)
    md = re.sub(r"(?<!\*)\*(?!\*)([^*]+)\*(?!\*)", r"<i>\1</i>", md)
    md = re.sub(r"`([^`]+)`", r'<font face="Courier" size="8.5">\1</font>', md)
    # bare URLs (not already in a stashed link)
    md = URL_RE.sub(lambda m: '<a href="%s" color="#1456b0">%s</a>'
                    % (m.group(1), m.group(1)), md)
    # restore stashed links
    def _pop(m):
        text, url = links[int(m.group(1))]
        text = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>",
                      html.escape(safe(text), quote=False))
        return '<a href="%s" color="#1456b0">%s</a>' % (url, text)

    md = re.sub(r"\x00(\d+)\x00", _pop, md)
    return md


class Anchor(Flowable):
    def __init__(self, name):
        Flowable.__init__(self)
        self.name = name
        self.width = 0
        self.height = 0

    def draw(self):
        self.canv.bookmarkPage(self.name)


class HRule(Flowable):
    def __init__(self, width):
        Flowable.__init__(self)
        self.width = width
        self.height = 8

    def draw(self):
        self.canv.setStrokeColor(BORDER)
        self.canv.setLineWidth(0.6)
        self.canv.line(0, 4, self.width, 4)


def parse(md_lines):
    """Yield ('type', payload) tokens."""
    i = 0
    n = len(md_lines)
    while i < n:
        line = md_lines[i].rstrip("\n")
        s = line.strip()
        if not s:
            yield ("space", None)
            i += 1
            continue
        if s.startswith("# "):
            yield ("h1", s[2:])
            i += 1
        elif s.startswith("## "):
            yield ("h2", s[3:])
            i += 1
        elif s.startswith("### "):
            yield ("h3", s[4:])
            i += 1
        elif s == "---":
            yield ("hr", None)
            i += 1
        elif s.startswith(">"):
            block = []
            while i < n and md_lines[i].strip().startswith(">"):
                block.append(md_lines[i].strip()[1:].strip())
                i += 1
            yield ("note", " ".join(block))
        elif s.startswith("|"):
            rows = []
            while i < n and md_lines[i].strip().startswith("|"):
                rows.append(md_lines[i].strip())
                i += 1
            yield ("table", rows)
        elif s.startswith("- ") or s.startswith("* "):
            indent = len(line) - len(line.lstrip())
            yield ("li2" if indent >= 2 else "li", s[2:])
            i += 1
        else:
            # paragraph (may span until blank)
            para = [s]
            i += 1
            while i < n and md_lines[i].strip() and not re.match(
                r"^(#|>|\||-\s|\*\s|---)", md_lines[i].strip()
            ):
                para.append(md_lines[i].strip())
                i += 1
            yield ("p", " ".join(para))


def build_table(rows):
    # drop the separator row (---|---)
    cells = []
    for r in rows:
        parts = [c.strip() for c in r.strip().strip("|").split("|")]
        cells.append(parts)
    if len(cells) >= 2 and set("".join(cells[1]).replace("-", "").replace(":", "")) == set():
        header = cells[0]
        data = cells[2:]
    else:
        header = cells[0]
        data = cells[1:]
    ncol = len(header)
    table_data = [[Paragraph(inline(c), S["cellh"]) for c in header]]
    for row in data:
        row = (row + [""] * ncol)[:ncol]
        table_data.append([Paragraph(inline(c), S["cell"]) for c in row])
    avail = 175 * mm
    # heuristic widths: first column a bit wider for 2-col tables
    if ncol == 2:
        widths = [avail * 0.42, avail * 0.58]
    else:
        widths = [avail / ncol] * ncol
    t = Table(table_data, colWidths=widths, repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, LIGHT]),
        ("GRID", (0, 0), (-1, -1), 0.4, BORDER),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
    ]))
    return t


def main():
    with open(SRC, encoding="utf-8") as f:
        md_lines = f.readlines()

    tokens = list(parse(md_lines))
    # collect H2 sections for the clickable index
    h2s = [(t[1], slug(t[1])) for t in tokens if t[0] == "h2"]

    story = []
    # ---- Cover ----
    story.append(Spacer(1, 24))
    story.append(Paragraph("AI / ML Learning Roadmap", S["title"]))
    story.append(Paragraph(safe("Beginner → RAG / LLM · Free · Project-Based · ~10-12 months"),
                           S["subtitle"]))
    story.append(Paragraph("Built around your 50-question AIML exam syllabus",
                           S["subtitle"]))
    story.append(Spacer(1, 16))

    # ---- Clickable index ----
    story.append(Paragraph("Contents — click to jump", S["h2"]))
    story.append(Spacer(1, 4))
    for label, anchor in h2s:
        story.append(Paragraph(
            '<a href="#%s" color="#1456b0">%s</a>' % (anchor, html.escape(safe(label))),
            S["toc"]))
    story.append(PageBreak())

    first_h2_seen = False
    for typ, payload in tokens:
        if typ == "h1":
            continue  # title already on cover
        if typ == "h2":
            anchor = slug(payload)
            story.append(Anchor(anchor))
            story.append(Paragraph(inline(payload), S["h2"]))
            first_h2_seen = True
        elif typ == "h3":
            story.append(Paragraph(inline(payload), S["h3"]))
        elif typ == "hr":
            story.append(Spacer(1, 2))
            story.append(HRule(175 * mm))
        elif typ == "note":
            story.append(Paragraph(inline(payload), S["note"]))
        elif typ == "p":
            story.append(Paragraph(inline(payload), S["body"]))
        elif typ == "li":
            story.append(Paragraph(inline(payload), S["bullet"], bulletText="•"))
        elif typ == "li2":
            story.append(Paragraph(inline(payload), S["bullet2"], bulletText="–"))
        elif typ == "table":
            story.append(Spacer(1, 2))
            story.append(build_table(payload))
            story.append(Spacer(1, 4))
        elif typ == "space":
            story.append(Spacer(1, 3))

    def footer(canvas, doc):
        canvas.saveState()
        canvas.setFont("Helvetica", 8)
        canvas.setFillColor(colors.HexColor("#999999"))
        canvas.drawCentredString(A4[0] / 2, 10 * mm,
                                 "AI/ML Roadmap · page %d" % doc.page)
        if doc.page > 1:
            canvas.setFillColor(BLUE)
            canvas.drawRightString(A4[0] - 18 * mm, 10 * mm, "Contents")
            canvas.linkRect("", h2s[0][1] if h2s else "",
                            (A4[0] - 38 * mm, 8 * mm, A4[0] - 16 * mm, 14 * mm),
                            relative=0, thickness=0)
        canvas.restoreState()

    doc = SimpleDocTemplate(OUT, pagesize=A4, leftMargin=17 * mm, rightMargin=17 * mm,
                            topMargin=15 * mm, bottomMargin=15 * mm,
                            title="AI/ML Learning Roadmap")
    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    print("Wrote", OUT)


if __name__ == "__main__":
    main()
