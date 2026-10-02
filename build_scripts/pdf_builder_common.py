import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    KeepTogether,
    HRFlowable,
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY

# Colors Palette
COLOR_PRIMARY = colors.HexColor("#1E1B4B")     # Deep Indigo
COLOR_SECONDARY = colors.HexColor("#312E81")   # Mid Indigo
COLOR_ACCENT = colors.HexColor("#0284C7")      # Cyan Blue
COLOR_DARK = colors.HexColor("#1E293B")        # Slate 800
COLOR_MUTED = colors.HexColor("#64748B")       # Slate 500
COLOR_LIGHT_BG = colors.HexColor("#F8FAFC")    # Slate 50
COLOR_BORDER = colors.HexColor("#E2E8F0")      # Slate 200
COLOR_SUCCESS = colors.HexColor("#059669")     # Emerald 600
COLOR_SUCCESS_BG = colors.HexColor("#ECFDF5")  # Emerald 50
COLOR_WARNING = colors.HexColor("#D97706")     # Amber 600
COLOR_WARNING_BG = colors.HexColor("#FFFBEB")  # Amber 50
COLOR_DANGER = colors.HexColor("#E11D48")      # Rose 600
COLOR_DANGER_BG = colors.HexColor("#FFF1F2")   # Rose 50

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(NumberedCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []
        self.doc_title = getattr(self, 'doc_title', "BackLift AI — Startup Project Submission")

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super(NumberedCanvas, self).showPage()
        super(NumberedCanvas, self).save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica-Bold", 8)
        self.setFillColor(COLOR_MUTED)

        # Header (pages after cover / first page)
        if self._pageNumber > 1:
            header_text = getattr(self, 'doc_title', "BackLift AI — Academic Recovery Platform")
            self.drawString(54, 750, header_text.upper())
            self.drawRightString(612 - 54, 750, "INTERNSHIP SUBMISSION")
            self.setStrokeColor(COLOR_BORDER)
            self.setLineWidth(0.75)
            self.line(54, 742, 612 - 54, 742)

        # Footer (all pages)
        self.setStrokeColor(COLOR_BORDER)
        self.setLineWidth(0.75)
        self.line(54, 45, 612 - 54, 45)

        self.setFont("Helvetica", 8)
        self.setFillColor(COLOR_MUTED)
        self.drawString(54, 32, "BackLift AI  |  Confidential Startup Deliverable  |  BridgeAura Internship Project")
        
        page_str = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(612 - 54, 32, page_str)
        self.restoreState()


def get_custom_styles():
    base = getSampleStyleSheet()
    styles = {}

    styles['DocTitle'] = ParagraphStyle(
        'DocTitle',
        parent=base['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=24,
        leading=28,
        textColor=COLOR_PRIMARY,
        spaceAfter=6,
    )

    styles['DocSubtitle'] = ParagraphStyle(
        'DocSubtitle',
        parent=base['Normal'],
        fontName='Helvetica',
        fontSize=12,
        leading=16,
        textColor=COLOR_ACCENT,
        spaceAfter=14,
    )

    styles['MetaBadge'] = ParagraphStyle(
        'MetaBadge',
        parent=base['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10,
        textColor=colors.white,
        alignment=TA_CENTER,
    )

    styles['Heading1'] = ParagraphStyle(
        'Heading1',
        parent=base['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=15,
        leading=19,
        textColor=COLOR_PRIMARY,
        spaceBefore=14,
        spaceAfter=8,
        keepWithNext=True,
    )

    styles['Heading2'] = ParagraphStyle(
        'Heading2',
        parent=base['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=COLOR_SECONDARY,
        spaceBefore=10,
        spaceAfter=6,
        keepWithNext=True,
    )

    styles['Heading3'] = ParagraphStyle(
        'Heading3',
        parent=base['Heading3'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=14,
        textColor=COLOR_DARK,
        spaceBefore=8,
        spaceAfter=4,
        keepWithNext=True,
    )

    styles['Body'] = ParagraphStyle(
        'Body',
        parent=base['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=COLOR_DARK,
        spaceAfter=6,
        alignment=TA_JUSTIFY,
    )

    styles['BodyBold'] = ParagraphStyle(
        'BodyBold',
        parent=base['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=13.5,
        textColor=COLOR_DARK,
        spaceAfter=4,
    )

    styles['Bullet'] = ParagraphStyle(
        'Bullet',
        parent=base['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=COLOR_DARK,
        leftIndent=14,
        firstLineIndent=-10,
        spaceAfter=3,
    )

    styles['CalloutText'] = ParagraphStyle(
        'CalloutText',
        parent=base['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=COLOR_DARK,
    )

    styles['CalloutTitle'] = ParagraphStyle(
        'CalloutTitle',
        parent=base['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=14,
        textColor=COLOR_PRIMARY,
        spaceAfter=3,
    )

    styles['TableHeader'] = ParagraphStyle(
        'TableHeader',
        parent=base['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        textColor=colors.white,
        alignment=TA_LEFT,
    )

    styles['TableCell'] = ParagraphStyle(
        'TableCell',
        parent=base['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=11,
        textColor=COLOR_DARK,
    )

    styles['TableCellBold'] = ParagraphStyle(
        'TableCellBold',
        parent=base['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=11,
        textColor=COLOR_PRIMARY,
    )

    styles['MetricValue'] = ParagraphStyle(
        'MetricValue',
        parent=base['Normal'],
        fontName='Helvetica-Bold',
        fontSize=16,
        leading=18,
        textColor=COLOR_PRIMARY,
        alignment=TA_CENTER,
    )

    styles['MetricLabel'] = ParagraphStyle(
        'MetricLabel',
        parent=base['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=10,
        textColor=COLOR_MUTED,
        alignment=TA_CENTER,
    )

    return styles


def create_header_banner(title, subtitle, category_tag="DELIVERABLE", meta_info=None):
    styles = get_custom_styles()
    meta_info = meta_info or "BackLift AI  |  Track: EdTech & AI  |  Internship Final Project"
    
    header_data = [
        [
            Paragraph(f"<font color='#0284C7'><b>● BACKLIFT AI</b></font> &nbsp;|&nbsp; <b>{category_tag.upper()}</b>", styles['TableCellBold']),
            Paragraph(meta_info, ParagraphStyle('RightM', parent=styles['TableCell'], alignment=TA_RIGHT, textColor=COLOR_MUTED))
        ],
        [
            Paragraph(title, styles['DocTitle']),
            ""
        ],
        [
            Paragraph(subtitle, styles['DocSubtitle']),
            ""
        ]
    ]

    t = Table(header_data, colWidths=[360, 144])
    t.setStyle(TableStyle([
        ('SPAN', (0, 1), (1, 1)),
        ('SPAN', (0, 2), (1, 2)),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
        ('TOPPADDING', (0, 0), (-1, -1), 2),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
    ]))
    return t


def create_callout(text, title=None, style='info'):
    styles = get_custom_styles()
    
    if style == 'info':
        bg_col = colors.HexColor("#F0F9FF")
        border_col = COLOR_ACCENT
    elif style == 'success':
        bg_col = COLOR_SUCCESS_BG
        border_col = COLOR_SUCCESS
    elif style == 'warning':
        bg_col = COLOR_WARNING_BG
        border_col = COLOR_WARNING
    elif style == 'danger':
        bg_col = COLOR_DANGER_BG
        border_col = COLOR_DANGER
    else:
        bg_col = COLOR_LIGHT_BG
        border_col = COLOR_PRIMARY

    content = []
    if title:
        content.append(Paragraph(f"<b>{title}</b>", styles['CalloutTitle']))
    content.append(Paragraph(text, styles['CalloutText']))

    t = Table([[content]], colWidths=[504])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), bg_col),
        ('LINELEFT', (0, 0), (-1, -1), 3.5, border_col),
        ('BOX', (0, 0), (-1, -1), 0.5, COLOR_BORDER),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('LEFTPADDING', (0, 0), (-1, -1), 12),
        ('RIGHTPADDING', (0, 0), (-1, -1), 12),
    ]))
    return t


def create_metric_card_row(metrics):
    styles = get_custom_styles()
    num_cols = len(metrics)
    col_width = 504 / num_cols

    cells = []
    for m in metrics:
        val = m.get('val', '')
        lbl = m.get('lbl', '')
        sub = m.get('sub', '')
        
        inner = [
            Paragraph(f"<b>{val}</b>", styles['MetricValue']),
            Spacer(1, 2),
            Paragraph(f"<b>{lbl}</b>", styles['MetricLabel']),
        ]
        if sub:
            inner.append(Spacer(1, 2))
            inner.append(Paragraph(f"<font color='#64748B' size=7>{sub}</font>", ParagraphStyle('SubM', parent=styles['MetricLabel'], fontSize=7, leading=9)))
        cells.append(inner)

    t = Table([cells], colWidths=[col_width] * num_cols)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), COLOR_LIGHT_BG),
        ('BOX', (0, 0), (-1, -1), 0.5, COLOR_BORDER),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, COLOR_BORDER),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ]))
    return t


def build_pdf_document(filename, story, doc_title):
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54,
    )
    
    # Custom canvas callback wrapper to set title
    def canvas_maker(*args, **kwargs):
        c = NumberedCanvas(*args, **kwargs)
        c.doc_title = doc_title
        return c

    doc.build(story, canvasmaker=canvas_maker)
    print(f"[PDF Built] {os.path.basename(filename)} -> {os.path.getsize(filename)} bytes")
