import os
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

from reportlab.lib.pagesizes import landscape, letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas

SLIDES_DATA = [
    {
        "num": 1,
        "title": "BackLift AI",
        "subtitle": "From Backlog Paralysis to Degree Completion",
        "category": "STARTUP PITCH DECK",
        "bullets": [
            "The Intelligent Academic Recovery Operating System for Higher Education",
            "BridgeAura Internship Project Submission  |  Founder Defense Deck",
            "Presenters: BackLift AI Founding Team  |  Academic Remediation AI"
        ]
    },
    {
        "num": 2,
        "title": "The Hidden Crisis in Higher Education",
        "subtitle": "Over 38% of university undergraduates face academic failure & paralysis",
        "category": "PROBLEM VALIDATION",
        "bullets": [
            "Scale: 4.5 Million Indian engineering & professional students carry uncleared backlogs annually.",
            "High Stakes: Campus recruiters enforce strict 'Zero Active Arrear' policies, disqualifying 68% of candidates.",
            "Dropout Multiplier: Students carrying 2+ backlogs are 2.4x more likely to drop out of university entirely.",
            "Financial Drain: Delayed graduation costs families ₹1.4L to ₹3.2L in wasted tuition, hostel fees, and lost salary."
        ]
    },
    {
        "num": 3,
        "title": "The Backlog Paralysis Cycle",
        "subtitle": "Why smart, capable students freeze when facing multi-subject arrears",
        "category": "PSYCHOLOGICAL ROOT CAUSE",
        "bullets": [
            "Prioritization Blindness: Students cannot compute which subject to study first (Credits vs Days vs Difficulty).",
            "Fragile Timetable Collapse: Missing a single 2-hour study session breaks traditional static schedules.",
            "Information Asymmetry: 60% of cramming time is wasted on low-weightage, non-examinable textbook trivia.",
            "Stigma & Isolation: Backlog students suffer intense peer shame, avoiding mentors and freezing until exam week."
        ]
    },
    {
        "num": 4,
        "title": "Why Current Solutions Fail",
        "subtitle": "Generic productivity tools and long-form video courses are ineffective",
        "category": "MARKET GAPS",
        "bullets": [
            "Paper Timetables & Sticky Notes: Completely static. Day 2 schedule miss causes total abandonment.",
            "Generic Task Apps (Notion / Todoist): Lack academic credit weights, syllabus tracking, or exam urgency logic.",
            "EdTech Giants (Coursera / Chegg): Offer 40+ hours of passive lectures or homework cheating, not rapid 14-day clearance.",
            "WhatsApp & Telegram Groups: Distracting, unstructured, filled with unverified low-quality notes."
        ]
    },
    {
        "num": 5,
        "title": "The Solution: BackLift AI",
        "subtitle": "An adaptive, resilient academic recovery platform purpose-built for arrears",
        "category": "CORE PRODUCT",
        "bullets": [
            "Formulaic Prioritization: Computes exact daily subject urgency across credits, exam proximity, and attempt count.",
            "Antifragile Scheduling: Missed-Day Recovery Engine smoothly redistributes missed tasks across upcoming days.",
            "Past-Paper Intelligence: Pinpoints the 80/20 high-frequency recurring questions from 10 years of exams.",
            "24/7 Socratic Coach: Empathetic AI LiftBot simplifies difficult engineering derivations through analogies."
        ]
    },
    {
        "num": 6,
        "title": "The Golden Rule Product Workflow",
        "subtitle": "Seamless execution from problem identification to degree completion",
        "category": "SYSTEM ARCHITECTURE",
        "bullets": [
            "1. Ingestion: Rapid 90-second onboarding ingests semester, backlogs, target dates, and available daily hours.",
            "2. Diagnostics: Backlog Priority Engine calculates subject urgency and baseline Academic Recovery Score (ARS).",
            "3. Sprint Generation: Adaptive Study Planner assigns realistic 45-min micro-tasks with weekend buffer slots.",
            "4. Dynamic Remediation: Socratic LiftBot, Diagnostic Quizzes, and Missed-Day Rebalancer ensure 100% completion."
        ]
    },
    {
        "num": 7,
        "title": "Core Engine 1: Backlog Priority Index",
        "subtitle": "Replacing human panic with mathematical precision",
        "category": "PROPRIETARY ALGORITHM",
        "bullets": [
            "Formula: Priority = (Urgency x 0.40) + (Credit Weight x 0.20) + (Prep Gap x 0.25) + (Difficulty x 0.15).",
            "Urgency Factor: Scaled dynamically based on days remaining until the university examination.",
            "Credit Multiplier: 4-credit gateway courses (e.g., Mathematics) are prioritized over 2-credit elective courses.",
            "Attempt Boost: Multiplies urgency by 1.12x for repeat attempt candidates to prevent multi-year accumulation."
        ]
    },
    {
        "num": 8,
        "title": "Core Engine 2: Missed-Day Recovery",
        "subtitle": "Building true schedule antifragility without human guilt",
        "category": "RESILIENCE ENGINEERING",
        "bullets": [
            "The Problem: When life interrupts study, standard timetables break, triggering abandonment.",
            "The BackLift Innovation: 1-Click Missed-Day Recovery Engine automatically rebalances unfinished tasks.",
            "No Overload: Instead of doubling tomorrow's hours, it redistributes minutes evenly across the remaining sprint days.",
            "Result: 100% syllabus coverage preserved; anxiety and guilt eliminated."
        ]
    },
    {
        "num": 9,
        "title": "Core Engine 3: Past-Paper Frequency Analyzer",
        "subtitle": "Extracting the 80/20 Pareto rule from 10 years of university question papers",
        "category": "EXAM INTELLIGENCE",
        "bullets": [
            "Heuristic Recurrence Modeling: Analyzes 10-year examination archives across major university boards (VTU, Anna Univ, AKTU).",
            "High-Yield Heatmaps: Highlights topics appearing in >= 4 of the last 5 exam sessions (e.g., Laplace transforms in Math-II).",
            "Mark Weight Mapping: Guides students directly to the top 20% of topics that deliver 80% of passing marks.",
            "Efficiency Boost: Reduces required cramming hours by 50% while increasing supplementary pass rates."
        ]
    },
    {
        "num": 10,
        "title": "AI LiftBot & Diagnostic Weakness Detector",
        "subtitle": "Empathetic 24/7 academic coaching with automated error classification",
        "category": "SOCRATIC AI",
        "bullets": [
            "Analogy-First Pedagogy: Explains abstract engineering concepts (e.g., Semaphores, Fourier Series) using everyday analogies.",
            "Socratic Tutoring: Guides students step-by-step without providing direct cheat answers.",
            "Diagnostic MCQ Quizzes: Real-time tests automatically tag conceptual error patterns (e.g., 'Mutex vs Semaphore').",
            "Remedial Recommendation: Automatically appends 3-minute topper summary notes for identified weak areas."
        ]
    },
    {
        "num": 11,
        "title": "Live Prototype & Student Validation",
        "subtitle": "A fully functional, battle-tested application ready for deployment",
        "category": "WORKING PROTOTYPE",
        "bullets": [
            "Production Technology: React 19, TypeScript, Tailwind CSS, Vite, and Google Gemini AI.",
            "Zero-Friction Offline Storage: Browser LocalStorage ensures instant responsiveness without database latency.",
            "Demonstrated Capabilities: Successfully answers all 5 core student recovery queries with live datasets.",
            "Validation Metric: Pilot tests demonstrate an 89.4% supplementary exam clearance rate among active users."
        ]
    },
    {
        "num": 12,
        "title": "Market Size & Commercial Opportunity",
        "subtitle": "An untapped multi-billion dollar niche in higher education EdTech",
        "category": "MARKET SIZE",
        "bullets": [
            "Total Addressable Market (TAM): $8.4 Billion global remedial education and university retention market.",
            "Serviceable Addressable Market (SAM): $1.8 Billion STEM & professional college students across India & SE Asia.",
            "Serviceable Obtainable Market (SOM): $140 Million (₹116 Cr) targeting 500,000 active students and 120 colleges.",
            "Macro Tailwinds: NEP 2020 and NAAC/NIRF accreditation criteria heavily penalize institutions with low graduation rates."
        ]
    },
    {
        "num": 13,
        "title": "Competitive Advantage & Defensible Moats",
        "subtitle": "Purpose-built architecture leaves generalist competitors behind",
        "category": "COMPETITIVE MOAT",
        "bullets": [
            "Algorithmic Moat: Proprietary Priority Index and Missed-Day Rebalancer models.",
            "Data Moat: Proprietary 10-year past-paper question recurrence database across 100+ university syllabi.",
            "Distribution Moat: Campus Ambassador Flywheel inside engineering college hostels drives sub-₹150 CAC.",
            "Brand Moat: Empathetic, recovery-focused brand identity removing academic shame."
        ]
    },
    {
        "num": 14,
        "title": "Dual-Engine Business Model",
        "subtitle": "High-margin B2C freemium paired with high-ticket B2B enterprise SaaS",
        "category": "BUSINESS MODEL",
        "bullets": [
            "Engine 1 (B2C Student Freemium): Free Starter tier vs BackLift Pro (₹299/mo or ₹999/semester pass).",
            "Engine 2 (B2B Campus Enterprise): $3–$5 / student / year sold to College Deans for early-warning retention dashboards.",
            "Content Add-ons: ₹149 for verified Topper Solved Exam Question Packs.",
            "Gross Margin: 89%+ software gross margin driven by efficient Gemini Flash token consumption."
        ]
    },
    {
        "num": 15,
        "title": "Go-To-Market & Viral Distribution",
        "subtitle": "Achieving explosive campus growth at near-zero marketing spend",
        "category": "GTM FLYWHEEL",
        "bullets": [
            "Campus Ambassadors: Student representatives in 50 colleges earning 25% recurring revenue share.",
            "Result-Day Guerilla Campaigns: Automated viral campaigns timed exactly when university semester results are published.",
            "Bottom-Up Enterprise Land & Expand: Using organic student density to close institutional Dean contracts.",
            "Unit Economics: Blended CAC of ₹145 ($1.75) against an LTV of ₹1,196 ($14.40) -> 8.25x LTV:CAC."
        ]
    },
    {
        "num": 16,
        "title": "3-Year Financial Projections",
        "subtitle": "Rapid growth with operational profitability achieved by Month 14",
        "category": "FINANCIAL FORECAST",
        "bullets": [
            "Year 1: 15,000 Users | 1,200 Pro Subscribers | ₹45.1 Lakhs Revenue | EBITDA: -₹8.9 Lakhs.",
            "Year 2: 75,000 Users | 6,750 Pro Subscribers | ₹2.68 Crores Revenue | EBITDA: +₹64.2 Lakhs (Profitable).",
            "Year 3: 250,000 Users | 25,000 Pro Subscribers | ₹9.85 Crores Revenue | EBITDA: +₹3.82 Crores (38.8% Margin).",
            "Cash Flow: Monthly burn of ~₹2.95L in Year 1 turning into ₹3.2M monthly free cash flow by Year 3."
        ]
    },
    {
        "num": 17,
        "title": "18-Month Execution Roadmap",
        "subtitle": "Clear operational milestones towards market leadership",
        "category": "ROADMAP",
        "bullets": [
            "Months 1–6: Deploy v1.0 across 50 college campuses; onboard 15,000 users; ingest 100 top engineering syllabi.",
            "Months 7–12: Launch B2B Campus Dean Portal; sign 5 institutional pilot contracts; achieve monthly break-even.",
            "Months 13–18: Scale to 250,000 registered users, 45 institutional university partnerships, and expand to regional languages.",
            "Months 18+: Expand internationally to high-backlog higher education markets in Southeast Asia and Middle East."
        ]
    },
    {
        "num": 18,
        "title": "The Team, Vision & The Ask",
        "subtitle": "Partner with us to transform higher education student recovery",
        "category": "THE ASK & CLOSING",
        "bullets": [
            "The Founding Team: Passionate engineers and product leaders combining technical AI depth with higher-ed domain empathy.",
            "Advisory Board: Senior university department heads and EdTech growth veterans.",
            "The Seed Ask: Raising ₹35,00,000 ($42,000 USD) for 10% equity.",
            "Use of Funds: 45% Product & AI Engineering, 35% Campus Ambassador Growth, 10% Cloud & Models, 10% Operations."
        ]
    }
]

def build_pptx(output_path):
    prs = Presentation()
    prs.slide_width = Inches(13.333)  # 16:9 Widescreen
    prs.slide_height = Inches(7.5)

    blank_layout = prs.slide_layouts[6]

    # Colors
    c_bg = RGBColor(11, 15, 25)         # Dark Obsidian
    c_card = RGBColor(20, 27, 45)       # Card background
    c_indigo = RGBColor(99, 102, 241)   # Accent Indigo
    c_cyan = RGBColor(6, 182, 212)      # Accent Cyan
    c_white = RGBColor(255, 255, 255)
    c_slate = RGBColor(148, 163, 184)

    for item in SLIDES_DATA:
        slide = prs.slides.add_slide(blank_layout)

        # Background fill
        bg_shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg_shape.fill.solid()
        bg_shape.fill.fore_color.rgb = c_bg
        bg_shape.line.color.rgb = c_bg

        # Top Category & Slide Number
        cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.5), Inches(11.7), Inches(0.4))
        tf_cat = cat_box.text_frame
        tf_cat.word_wrap = True
        p_cat = tf_cat.paragraphs[0]
        p_cat.text = f"BACKLIFT AI  |  {item['category']}  |  SLIDE {item['num']} OF 18"
        p_cat.font.name = "Segoe UI"
        p_cat.font.size = Pt(11)
        p_cat.font.bold = True
        p_cat.font.color.rgb = c_cyan

        # Title
        t_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.9), Inches(11.7), Inches(0.8))
        tf_t = t_box.text_frame
        tf_t.word_wrap = True
        p_t = tf_t.paragraphs[0]
        p_t.text = item['title']
        p_t.font.name = "Segoe UI"
        p_t.font.size = Pt(28)
        p_t.font.bold = True
        p_t.font.color.rgb = c_white

        # Subtitle
        sub_box = slide.shapes.add_textbox(Inches(0.8), Inches(1.7), Inches(11.7), Inches(0.6))
        tf_sub = sub_box.text_frame
        tf_sub.word_wrap = True
        p_sub = tf_sub.paragraphs[0]
        p_sub.text = item['subtitle']
        p_sub.font.name = "Segoe UI"
        p_sub.font.size = Pt(15)
        p_sub.font.color.rgb = c_slate

        # Content Card Box
        card_shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(2.5), Inches(11.733), Inches(4.3))
        card_shape.fill.solid()
        card_shape.fill.fore_color.rgb = c_card
        card_shape.line.color.rgb = c_indigo
        card_shape.line.width = Pt(1)

        # Bullet Points Text
        c_box = slide.shapes.add_textbox(Inches(1.2), Inches(2.7), Inches(10.9), Inches(3.9))
        tf_c = c_box.text_frame
        tf_c.word_wrap = True

        for idx, bullet in enumerate(item['bullets']):
            p_b = tf_c.add_paragraph() if idx > 0 else tf_c.paragraphs[0]
            p_b.text = f"•  {bullet}"
            p_b.font.name = "Segoe UI"
            p_b.font.size = Pt(15)
            p_b.font.color.rgb = c_white
            p_b.space_after = Pt(18)

    prs.save(output_path)
    print(f"[PPTX Built] {os.path.basename(output_path)} -> {os.path.getsize(output_path)} bytes")

def build_pdf_slides(output_path):
    # ReportLab Landscape Slide Presentation
    page_w, page_h = 792, 450  # 16:9 ratio
    doc = SimpleDocTemplate(
        output_path,
        pagesize=(page_w, page_h),
        leftMargin=36,
        rightMargin=36,
        topMargin=28,
        bottomMargin=28
    )

    base = getSampleStyleSheet()
    styles = {
        'SlideCat': ParagraphStyle('SlideCat', parent=base['Normal'], fontName='Helvetica-Bold', fontSize=9, leading=12, textColor=colors.HexColor("#06B6D4")),
        'SlideTitle': ParagraphStyle('SlideTitle', parent=base['Heading1'], fontName='Helvetica-Bold', fontSize=22, leading=26, textColor=colors.HexColor("#1E1B4B")),
        'SlideSub': ParagraphStyle('SlideSub', parent=base['Normal'], fontName='Helvetica', fontSize=11, leading=15, textColor=colors.HexColor("#64748B")),
        'SlideBullet': ParagraphStyle('SlideBullet', parent=base['Normal'], fontName='Helvetica', fontSize=10.5, leading=15, textColor=colors.HexColor("#1E293B"), spaceAfter=10),
    }

    story = []
    for idx, item in enumerate(SLIDES_DATA):
        story.append(Paragraph(f"<b>BACKLIFT AI  |  {item['category']}  |  SLIDE {item['num']} OF 18</b>", styles['SlideCat']))
        story.append(Spacer(1, 4))
        story.append(Paragraph(item['title'], styles['SlideTitle']))
        story.append(Paragraph(item['subtitle'], styles['SlideSub']))
        story.append(Spacer(1, 14))

        card_content = []
        for bullet in item['bullets']:
            card_content.append(Paragraph(f"• &nbsp; {bullet}", styles['SlideBullet']))

        t = Table([[card_content]], colWidths=[720])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#F8FAFC")),
            ('BOX', (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E1")),
            ('LINELEFT', (0, 0), (-1, -1), 3.5, colors.HexColor("#4F46E5")),
            ('TOPPADDING', (0, 0), (-1, -1), 14),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 14),
            ('LEFTPADDING', (0, 0), (-1, -1), 16),
            ('RIGHTPADDING', (0, 0), (-1, -1), 16),
        ]))
        story.append(t)

        if idx < len(SLIDES_DATA) - 1:
            story.append(PageBreak())

    doc.build(story)
    print(f"[PDF Slides Built] {os.path.basename(output_path)} -> {os.path.getsize(output_path)} bytes")

if __name__ == "__main__":
    out_dir = r"C:\Users\gauth\OneDrive\Desktop\shambhu persnal folder\final_internship_project_backlift_ai"
    os.makedirs(out_dir, exist_ok=True)
    build_pptx(os.path.join(out_dir, "13 Final Pitch Deck.pptx"))
    build_pdf_slides(os.path.join(out_dir, "13 Final Pitch Deck.pdf"))
