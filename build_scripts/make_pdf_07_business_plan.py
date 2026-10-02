import os
import sys
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, KeepTogether, HRFlowable
from reportlab.lib import colors
from pdf_builder_common import (
    COLOR_PRIMARY, COLOR_SECONDARY, COLOR_ACCENT, COLOR_DARK, COLOR_MUTED,
    COLOR_LIGHT_BG, COLOR_BORDER, COLOR_SUCCESS, COLOR_WARNING, COLOR_DANGER,
    get_custom_styles, create_header_banner, create_callout, create_metric_card_row,
    build_pdf_document
)

def generate_pdf(output_path):
    styles = get_custom_styles()
    story = []

    # Title Banner
    story.append(create_header_banner(
        title="07 Strategic Business Plan",
        subtitle="Market Opportunity, Competitive Moats, Go-To-Market, and 3-Year Operational Plan",
        category_tag="DELIVERABLE 07 — BUSINESS PLAN",
        meta_info="BackLift AI  |  Comprehensive Startup Strategy"
    ))
    story.append(Spacer(1, 14))

    # 1. Executive Summary
    story.append(Paragraph("1. Executive Summary & Company Overview", styles['Heading1']))
    story.append(Paragraph(
        "<b>Company Name:</b> BackLift AI Inc. &nbsp;|&nbsp; <b>Industry:</b> EdTech / Higher Education Remediation SaaS.<br/>"
        "BackLift AI is developing the world's first AI-driven Academic Recovery Operating System. "
        "Every year, more than 4.5 million university students across India (and 18 million globally) accumulate uncleared semester backlogs, "
        "triggering severe study paralysis, placement disqualification, and a 2.4x surge in dropout rates. "
        "By replacing fragile, static timetables with our proprietary <b>Backlog Priority Engine</b> and <b>Missed-Day Recovery Engine</b>, "
        "BackLift AI turns multi-subject backlog crises into achievable 25-minute daily micro-sprints. "
        "We monetize through a B2C freemium subscription (₹299/month or ₹999/semester) and a high-margin B2B campus enterprise SaaS ($3–$5/student/year) "
        "that provides college Deans with early-warning retention analytics.",
        styles['Body']
    ))
    story.append(Spacer(1, 8))

    # Market Size Numbers
    metrics = [
        {"val": "$8.4 Billion", "lbl": "Global TAM", "sub": "Remedial EdTech & Retention"},
        {"val": "$1.8 Billion", "lbl": "India & Regional SAM", "sub": "STEM & professional colleges"},
        {"val": "$140 Million", "lbl": "3-Year SOM", "sub": "Capturing 500k students & 120 colleges"},
        {"val": "₹35 Lakhs ($42k)", "lbl": "Seed Funding Ask", "sub": "18 months runway to profitability"}
    ]
    story.append(create_metric_card_row(metrics))
    story.append(Spacer(1, 14))

    # 2. Problem & Solution Synthesis
    story.append(Paragraph("2. The Problem-Solution Synthesis", styles['Heading1']))
    story.append(Paragraph(
        "While K-12 test prep and generic coding bootcamps have reached peak market saturation, <b>university academic remediation is completely underserved</b>. "
        "Current higher education software treats students as administrative ledger entries rather than struggling learners. "
        "When an undergraduate fails a high-credit subject like Applied Mathematics, Operating Systems, or Thermodynamics, they are thrown into the <b>Backlog Paralysis Cycle</b>. "
        "They face: (1) Inability to prioritize between regular semester courses and repeat exams; (2) Immediate collapse of rigid timetables upon missing a single study session; "
        "(3) Severe time wastage on low-yield textbook topics; and (4) Stigma-induced isolation. "
        "<br/><br/>"
        "<b>BackLift AI solves this end-to-end:</b> Our algorithmic Priority Index determines exactly what to study first; our Missed-Day Rebalancer seamlessly restructures schedules when plans derail; "
        "our Past-Paper Analyzer surfaces the 80/20 high-frequency topics; and our AI LiftBot provides empathetic 24/7 Socratic explanations.",
        styles['Body']
    ))
    story.append(Spacer(1, 12))

    # 3. Market Size & Opportunity
    story.append(Paragraph("3. Market Sizing: TAM, SAM, and SOM", styles['Heading1']))
    
    market_data = [
        [
            Paragraph("<b>Market Level</b>", styles['TableHeader']),
            Paragraph("<b>Definition & Addressable Population</b>", styles['TableHeader']),
            Paragraph("<b>Monetization Calculation</b>", styles['TableHeader']),
            Paragraph("<b>Total Value</b>", styles['TableHeader'])
        ],
        [
            Paragraph("<b>Total Addressable Market (TAM)</b>", styles['TableCellBold']),
            Paragraph("Global undergraduate higher education students with academic arrear / remediation needs (approx. 70M students).", styles['TableCell']),
            Paragraph("Average global ARPU of $120/year across blended B2C and B2B higher-ed software.", styles['TableCell']),
            Paragraph("<b>$8.4 Billion</b>", styles['TableCellBold'])
        ],
        [
            Paragraph("<b>Serviceable Addressable Market (SAM)</b>", styles['TableCellBold']),
            Paragraph("India, Southeast Asia, and Middle East STEM & professional college students (approx. 18M students).", styles['TableCell']),
            Paragraph("Blended regional ARPU of ₹8,200 ($100)/year across institutional licenses and student subscriptions.", styles['TableCell']),
            Paragraph("<b>$1.8 Billion</b>", styles['TableCellBold'])
        ],
        [
            Paragraph("<b>Serviceable Obtainable Market (SOM)</b>", styles['TableCellBold']),
            Paragraph("Realistic 3-year target: 500,000 active students and 120 private/autonomous engineering colleges in India.", styles['TableCell']),
            Paragraph("10% B2C Pro conversion (50k paid users @ ₹2,400/yr) + 120 college contracts (@ ₹10 Lakhs/yr).", styles['TableCell']),
            Paragraph("<b>$140 Million (₹116 Cr)</b>", styles['TableCellBold'])
        ]
    ]

    t_market = Table(market_data, colWidths=[110, 160, 144, 90])
    t_market.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), COLOR_PRIMARY),
        ('GRID', (0, 0), (-1, -1), 0.5, COLOR_BORDER),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, COLOR_LIGHT_BG])
    ]))
    story.append(t_market)
    story.append(Spacer(1, 14))

    # 4. Competitive Analysis
    story.append(Paragraph("4. Competitor Landscape & Defensible Moats", styles['Heading1']))
    
    comp_matrix = [
        [
            Paragraph("<b>Competitor</b>", styles['TableHeader']),
            Paragraph("<b>Core Focus</b>", styles['TableHeader']),
            Paragraph("<b>Weakness / Vulnerability</b>", styles['TableHeader']),
            Paragraph("<b>BackLift AI Competitive Moat</b>", styles['TableHeader'])
        ],
        [
            Paragraph("<b>Notion / Todoist</b>", styles['TableCellBold']),
            Paragraph("Generic productivity templates", styles['TableCell']),
            Paragraph("Zero academic intelligence; fragile timetables collapse on missed days.", styles['TableCell']),
            Paragraph("Proprietary priority engine & automated missed-day schedule rebalancing.", styles['TableCell'])
        ],
        [
            Paragraph("<b>Chegg / Brainly</b>", styles['TableCellBold']),
            Paragraph("Q&A homework solver", styles['TableCell']),
            Paragraph("Facing plagiarism bans; high $19.95/mo price; does not build a study schedule.", styles['TableCell']),
            Paragraph("Ethical Socratic recovery coaching; focus on syllabus clearance, not homework cheating.", styles['TableCell'])
        ],
        [
            Paragraph("<b>Coursera / Udemy</b>", styles['TableCellBold']),
            Paragraph("Massive video course libraries", styles['TableCell']),
            Paragraph("40+ hours per course; passive watching; useless for 14-day exam sprints.", styles['TableCell']),
            Paragraph("Laser-targeted 80/20 high-frequency past paper analysis and 15-minute concept mastery.", styles['TableCell'])
        ],
        [
            Paragraph("<b>Forest / Flora</b>", styles['TableCellBold']),
            Paragraph("Gamified Pomodoro timers", styles['TableCell']),
            Paragraph("Just a timer; has no syllabus tracking, credit weighting, or AI coach.", styles['TableCell']),
            Paragraph("End-to-end integration: timer feeds study minutes directly into backlog progress.", styles['TableCell'])
        ]
    ]

    t_comp_mat = Table(comp_matrix, colWidths=[100, 110, 150, 144])
    t_comp_mat.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), COLOR_SECONDARY),
        ('GRID', (0, 0), (-1, -1), 0.5, COLOR_BORDER),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, COLOR_LIGHT_BG])
    ]))
    story.append(t_comp_mat)
    story.append(Spacer(1, 14))

    # 5. Go-To-Market (GTM) Strategy
    story.append(Paragraph("5. Go-To-Market & Campus Distribution Strategy", styles['Heading1']))
    story.append(Paragraph(
        "Our customer acquisition strategy leverages three powerful distribution flywheels:",
        styles['Body']
    ))

    gtm_points = [
        ("<b>Phase 1: The Campus Ambassador Hostels Flywheel (Months 1–6):</b> Appointing 2 influential student ambassadors in 50 target engineering colleges. Ambassadors receive 25% recurring commissions on Pro subscriptions. They distribute BackLift AI during supplementary exam registration periods, driving sub-₹100 CAC.", styles['Bullet']),
        ("<b>Phase 2: Result-Day Guerilla Acquisition (Months 6–12):</b> Deploying automated alerts and micro-influencer campaigns on the exact 72-hour window when state technical universities (VTU, Anna Univ, AKTU, Mumbai Univ) release semester exam results—the exact moment backlog panic peaks.", styles['Bullet']),
        ("<b>Phase 3: B2B Institutional Expansion (Months 12–24):</b> Transitioning high-density B2C student usage into B2B campus enterprise sales. We approach College Principals with proof: <i>'400 of your students are using BackLift AI; integrate BackLift Campus enterprise to improve your NAAC accreditation retention score by 15%.'</i>", styles['Bullet'])
    ]
    for text, s in gtm_points:
        story.append(Paragraph(text, s))
    story.append(Spacer(1, 10))

    # 6. Operational Milestones & Ask
    story.append(Paragraph("6. 18-Month Operational Roadmap & Funding Ask", styles['Heading1']))
    story.append(Paragraph(
        "• <b>Q1–Q2 (Months 1–6):</b> Launch production v1.0 across 50 college campuses; onboard 15,000 free users and 1,200 Pro subscribers; ingest 100 top engineering syllabi.<br/>"
        "• <b>Q3–Q4 (Months 7–12):</b> Roll out B2B Campus Dean Portal; sign 5 institutional pilot contracts; achieve monthly break-even by Month 14.<br/>"
        "• <b>Q5–Q6 (Months 13–18):</b> Expand to 250,000 free users, 25,000 paying Pro subscribers, and 45 institutional university enterprise contracts.<br/><br/>"
        "<b>The Investment Ask:</b> We are raising a Seed Round of <b>₹35,000,000 ($42,000)</b> for 10% equity. "
        "Use of funds: 45% Product & AI Engineering, 35% Campus Growth & Ambassadors, 10% Cloud/API Infrastructure, 10% Operations & Legal.",
        styles['Body']
    ))

    build_pdf_document(output_path, story, "07 Business Plan — BackLift AI")

if __name__ == "__main__":
    out_dir = r"C:\Users\gauth\OneDrive\Desktop\shambhu persnal folder\final_internship_project_backlift_ai"
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, "07 Business Plan.pdf")
    generate_pdf(out_file)
