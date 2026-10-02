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
        title="06 Business Model Canvas",
        subtitle="Commercial Architecture, Dual-Engine Monetization, and Strategic Canvas",
        category_tag="DELIVERABLE 06 — BUSINESS MODEL",
        meta_info="BackLift AI  |  Strategic Monetization Blueprint"
    ))
    story.append(Spacer(1, 14))

    # Executive Overview
    story.append(Paragraph("1. Commercial Strategy & Dual-Engine Model", styles['Heading1']))
    story.append(Paragraph(
        "<b>BackLift AI</b> operates a robust, highly defensible <b>Dual-Engine Business Model</b>. "
        "Engine 1 is a viral, low-friction <b>B2C Product-Led Freemium model</b> targeted directly at university students facing backlog panic. "
        "Engine 2 is a high-ticket, recurring <b>B2B Enterprise SaaS model</b> (BackLift Campus) sold directly to university Deans, "
        "Provosts, and Chancellors who face institutional financial and ranking penalties when student dropout rates increase.",
        styles['Body']
    ))
    story.append(Spacer(1, 8))

    # High-level monetization cards
    metrics = [
        {"val": "₹299 / mo", "lbl": "BackLift Pro (B2C)", "sub": "Or ₹999/semester pass"},
        {"val": "$3 - $5", "lbl": "BackLift Campus (B2B)", "sub": "Per enrolled student / year"},
        {"val": "₹145 ($1.75)", "lbl": "Target Blended CAC", "sub": "Driven by campus viral loops"},
        {"val": "8.25x", "lbl": "LTV to CAC Ratio", "sub": "Healthy SaaS unit economics"}
    ]
    story.append(create_metric_card_row(metrics))
    story.append(Spacer(1, 14))

    # The 9 Building Blocks of Business Model Canvas
    story.append(Paragraph("2. The 9 Building Blocks of the Business Model Canvas", styles['Heading1']))
    
    canvas_blocks = [
        [
            Paragraph("<b>Building Block</b>", styles['TableHeader']),
            Paragraph("<b>Strategic Operational Components & Implementation</b>", styles['TableHeader'])
        ],
        [
            Paragraph("<b>1. Customer Segments</b>", styles['TableCellBold']),
            Paragraph("• <b>Primary (B2C):</b> 2nd to 4th year STEM & undergraduate students with 1–4 active exam arrears.<br/>"
                      "• <b>High-Urgency Segment:</b> Final-year students facing immediate placement cutoff or degree prolongation.<br/>"
                      "• <b>Institutional (B2B):</b> Private engineering colleges, autonomous state universities, and community colleges seeking NAAC/NIRF accreditation improvement.", styles['TableCell'])
        ],
        [
            Paragraph("<b>2. Value Propositions</b>", styles['TableCellBold']),
            Paragraph("• <b>For Students:</b> Eliminates prioritization confusion; resilient study schedule that adapts to missed days; saves 1–2 academic years; restores placement eligibility.<br/>"
                      "• <b>For Universities:</b> Increases graduation rates by 12–18%; reduces first-to-second-year dropouts; provides actionable accreditation retention compliance dossiers.", styles['TableCell'])
        ],
        [
            Paragraph("<b>3. Distribution Channels</b>", styles['TableCellBold']),
            Paragraph("• <b>Campus Ambassador Flywheel:</b> Student reps in engineering hostels earning revenue share per Pro referral.<br/>"
                      "• <b>Semester Result Guerilla Campaigns:</b> Targeted digital outreach on the exact days university arrear results are announced.<br/>"
                      "• <b>B2B Institutional Sales:</b> Direct outreach to Academic Deans via pilot demonstration audits.", styles['TableCell'])
        ],
        [
            Paragraph("<b>4. Customer Relationships</b>", styles['TableCellBold']),
            Paragraph("• <b>Automated Empathy:</b> AI LiftBot acts as an encouraging 24/7 academic advisor without judgement.<br/>"
                      "• <b>Study Buddy Peer Circles:</b> Community-driven repeat exam lobbies fostering mutual accountability.<br/>"
                      "• <b>Dedicated Campus Success Managers:</b> For institutional B2B enterprise deployments.", styles['TableCell'])
        ],
        [
            Paragraph("<b>5. Revenue Streams</b>", styles['TableCellBold']),
            Paragraph("• <b>B2C Subscriptions:</b> BackLift Pro (₹299/mo or ₹999/semester).<br/>"
                      "• <b>B2B Campus Licensing:</b> $3.00–$5.00 per student/year under institutional multi-year contracts.<br/>"
                      "• <b>Content Add-on Packs:</b> ₹149 for verified Topper Solved Exam Question Packs.", styles['TableCell'])
        ],
        [
            Paragraph("<b>6. Key Resources</b>", styles['TableCellBold']),
            Paragraph("• <b>Proprietary Algorithms:</b> Backlog Priority Index formulation and Missed-Day Rebalancing Engine.<br/>"
                      "• <b>Historical Exam Database:</b> 10-year question paper frequency index across major university boards.<br/>"
                      "• <b>Cloud & AI Infrastructure:</b> Scalable vector database (pgvector) and high-throughput LLM pipelines.", styles['TableCell'])
        ],
        [
            Paragraph("<b>7. Key Activities</b>", styles['TableCellBold']),
            Paragraph("• Continuous algorithm optimization and syllabus schema ingestion.<br/>"
                      "• Past paper parsing, question extraction, and topic recurrence modeling.<br/>"
                      "• Campus marketing, user acquisition, and institutional B2B enterprise sales demos.", styles['TableCell'])
        ],
        [
            Paragraph("<b>8. Key Partners</b>", styles['TableCellBold']),
            Paragraph("• <b>Academic Institutions:</b> Colleges providing syllabus structures and running pilot retention programs.<br/>"
                      "• <b>Cloud & Model Providers:</b> Google Cloud Platform (Gemini API, Cloud Run) and AWS.<br/>"
                      "• <b>Student Bodies & Exam Forums:</b> Campus engineering clubs and exam prep communities.", styles['TableCell'])
        ],
        [
            Paragraph("<b>9. Cost Structure</b>", styles['TableCellBold']),
            Paragraph("• <b>COGS / Cloud Hosting:</b> LLM token consumption (Gemini Flash), vector search DB, cloud servers (~14%).<br/>"
                      "• <b>Product Engineering:</b> Full-stack and AI engineering salaries (~45%).<br/>"
                      "• <b>Sales & Campus Marketing:</b> Campus ambassador commissions, digital ads, and field sales (~26%).<br/>"
                      "• <b>General & Administrative:</b> Legal, compliance, accounting, tools (~15%).", styles['TableCell'])
        ]
    ]

    t_canvas = Table(canvas_blocks, colWidths=[130, 374])
    t_canvas.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), COLOR_PRIMARY),
        ('GRID', (0, 0), (-1, -1), 0.5, COLOR_BORDER),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, COLOR_LIGHT_BG])
    ]))
    story.append(t_canvas)
    story.append(Spacer(1, 12))

    # Pricing Tier Table
    story.append(Paragraph("3. Detailed Pricing & Subscription Architecture", styles['Heading1']))
    
    pricing_data = [
        [
            Paragraph("<b>Tier</b>", styles['TableHeader']),
            Paragraph("<b>Price Point</b>", styles['TableHeader']),
            Paragraph("<b>Target Segment</b>", styles['TableHeader']),
            Paragraph("<b>Feature Entitlements</b>", styles['TableHeader'])
        ],
        [
            Paragraph("<b>Free Starter</b>", styles['TableCellBold']),
            Paragraph("₹0 (Free Forever)", styles['TableCell']),
            Paragraph("Casual users / new signups", styles['TableCell']),
            Paragraph("Track up to 2 backlogs; basic static study plan; 10 AI chatbot queries/week; basic resource hub.", styles['TableCell'])
        ],
        [
            Paragraph("<b>BackLift Pro (Monthly)</b>", styles['TableCellBold']),
            Paragraph("₹299 / month<br/>($4.99)", styles['TableCell']),
            Paragraph("Students in active cram mode", styles['TableCell']),
            Paragraph("Unlimited backlogs; <b>Missed-Day Recovery Engine</b>; unlimited AI LiftBot; Past Paper Frequency Analyzer; Diagnostic Quizzes.", styles['TableCell'])
        ],
        [
            Paragraph("<b>Semester Recovery Pass</b>", styles['TableCellBold']),
            Paragraph("₹999 / semester<br/>($14.99)", styles['TableCell']),
            Paragraph("Students with 3+ backlogs across 6 months", styles['TableCell']),
            Paragraph("All Pro features for full 6 months; Topper Solved Exam Packs; Priority Study Buddy matching; printable recovery dossier.", styles['TableCell'])
        ],
        [
            Paragraph("<b>Campus Enterprise</b>", styles['TableCellBold']),
            Paragraph("$3–$5 / student / year<br/>(Annual contract)", styles['TableCell']),
            Paragraph("Colleges & Universities (B2B SaaS)", styles['TableCell']),
            Paragraph("Institutional Dean Dashboard; batch-wide dropout risk alerts; bottleneck subject diagnostics; NAAC compliance reports.", styles['TableCell'])
        ]
    ]

    t_pricing = Table(pricing_data, colWidths=[100, 100, 114, 190])
    t_pricing.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), COLOR_SECONDARY),
        ('GRID', (0, 0), (-1, -1), 0.5, COLOR_BORDER),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, COLOR_LIGHT_BG])
    ]))
    story.append(t_pricing)

    build_pdf_document(output_path, story, "06 Business Model — BackLift AI")

if __name__ == "__main__":
    out_dir = r"C:\Users\gauth\OneDrive\Desktop\shambhu persnal folder\final_internship_project_backlift_ai"
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, "06 Business Model.pdf")
    generate_pdf(out_file)
