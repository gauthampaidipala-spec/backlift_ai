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
        title="03 Product Definition",
        subtitle="Functional Architecture, Algorithmic Engines, and Value Proposition",
        category_tag="DELIVERABLE 03 — PRODUCT BLUEPRINT",
        meta_info="BackLift AI  |  Product Specification Document"
    ))
    story.append(Spacer(1, 14))

    # Product Overview
    story.append(Paragraph("1. Product Overview & System Definition", styles['Heading1']))
    story.append(Paragraph(
        "<b>BackLift AI</b> is an intelligent, resilient Academic Recovery and Study Management Software platform. "
        "Unlike generic note-taking or static calendar applications, BackLift AI is purpose-built to convert overwhelming, "
        "multi-semester academic backlogs into mathematically optimized, achievable daily micro-actions. "
        "The system combines algorithmic prioritization, resilient schedule rebalancing, historical past-paper frequency heuristics, "
        "and a 24/7 empathetic Socratic AI tutor to ensure higher-education students systematically clear backlogs and graduate on time.",
        styles['Body']
    ))
    story.append(Spacer(1, 10))

    # Core What It Does
    story.append(Paragraph("2. What the Product Does: The 10 Core Functional Modules", styles['Heading1']))
    
    modules = [
        ("<b>1. Central Recovery Command Dashboard:</b> Displays a real-time diagnostic Academic Recovery Score (ARS, 0–100), active exam countdown meters, sprint progress bars, and high-priority action alerts.", styles['Bullet']),
        ("<b>2. Multi-Factor Backlog Priority Engine:</b> An algorithmic engine that continuously computes urgency by weighting exam proximity, credit value, preparation gap, difficulty rating, and attempt multipliers.", styles['Bullet']),
        ("<b>3. Interactive Backlog Lifecycle CRUD Manager:</b> Allows students to track multi-semester backlogs with granular syllabus unit tracking, completion flags, and color-coded status badges.", styles['Bullet']),
        ("<b>4. Adaptive 7-Day Study Planner:</b> Automatically translates available daily study hours into realistic 45-minute and 90-minute subject-tagged time slots with built-in rest intervals.", styles['Bullet']),
        ("<b>5. Missed-Day Recovery Engine:</b> A resilient schedule rebalancer that redistributes unfinished tasks across future days with a single click, completely eliminating timetable collapse guilt.", styles['Bullet']),
        ("<b>6. AI LiftBot (Academic Recovery Coach):</b> A 24/7 Socratic conversational agent that simplifies complex engineering concepts, explains mathematical formulas through real-world analogies, and answers questions contextualized to student notes.", styles['Bullet']),
        ("<b>7. Past Exam Paper Analyzer:</b> Parses historical university question papers to extract recurrent questions, unit weightages, and 80/20 high-yield topics.", styles['Bullet']),
        ("<b>8. AI Diagnostic Quiz Generator & Weakness Detector:</b> Generates customized 5-question multiple-choice diagnostic tests that automatically tag conceptual weaknesses and recommend remedial resources.", styles['Bullet']),
        ("<b>9. Integrated Focus Pomodoro Timer:</b> A 25-minute deep work focus timer with ambient soundscapes that tags completed minutes directly to the active backlog subject.", styles['Bullet']),
        ("<b>10. Institutional Campus Dean Retention Portal:</b> A B2B enterprise analytics dashboard enabling university administrators to track department-wide arrear trends, pinpoint bottleneck subjects, and deploy proactive student interventions.", styles['Bullet'])
    ]
    for text, s in modules:
        story.append(Paragraph(text, s))
    story.append(Spacer(1, 12))

    # How It Works (Algorithmic Logic)
    story.append(Paragraph("3. How It Works: Algorithmic Architecture", styles['Heading1']))
    story.append(Paragraph(
        "BackLift AI replaces human guesswork with proven computational formulations:",
        styles['Body']
    ))

    # Priority Engine Box
    story.append(create_callout(
        "<b>The Backlog Priority Index Formula:</b><br/>"
        "<code>Priority Index = (Urgency × 0.40) + (Credit Weight × 0.20) + (Prep Gap × 0.25) + (Difficulty × 0.15) × Attempt Multiplier</code><br/><br/>"
        "• <b>Urgency (40%):</b> Scaled linearly based on days remaining until the target examination date.<br/>"
        "• <b>Credit Weight (20%):</b> High-credit subjects (e.g., 4 credits) receive priority over 2-credit labs.<br/>"
        "• <b>Preparation Gap (25%):</b> Measured as (100% - Current Topic Mastery %).<br/>"
        "• <b>Difficulty Rating (15%):</b> Subjective scale from 1 (easy) to 5 (extreme difficulty).<br/>"
        "• <b>Attempt Multiplier:</b> If attempt count ≥ 2, a 1.12x boost is applied to prevent multi-year accumulation.",
        title="1. Proprietary Backlog Priority Formulation",
        style="info"
    ))
    story.append(Spacer(1, 10))

    story.append(create_callout(
        "<b>The Academic Recovery Score (ARS) Formulation:</b><br/>"
        "<code>ARS (0–100) = (Avg Prep % × 0.35) + (Quiz Performance % × 0.25) + (Study Streak % × 0.20) + (Exam Time Cushion % × 0.20)</code><br/><br/>"
        "<b>Ethical Positioning:</b> The ARS is explicitly formulated and presented as an <i>internal study planning diagnostic</i>. "
        "It visualizes student momentum and preparation hygiene, and is never misrepresented as a guaranteed university exam passing grade.",
        title="2. Diagnostic Academic Recovery Score (ARS)",
        style="success"
    ))
    story.append(Spacer(1, 12))

    # Value Proposition & Differentiation
    story.append(Paragraph("4. Differentiation & Competitive Value Proposition", styles['Heading1']))
    
    diff_data = [
        [
            Paragraph("<b>Product Capability</b>", styles['TableHeader']),
            Paragraph("<b>Generic Planners (Notion / Google)</b>", styles['TableHeader']),
            Paragraph("<b>EdTech Giants (Chegg / Coursera)</b>", styles['TableHeader']),
            Paragraph("<b>BackLift AI</b>", styles['TableHeader'])
        ],
        [
            Paragraph("<b>Primary Purpose</b>", styles['TableCellBold']),
            Paragraph("General task management", styles['TableCell']),
            Paragraph("Long-form video courses", styles['TableCell']),
            Paragraph("<b>Rapid Academic Backlog Clearance</b>", styles['TableCellBold'])
        ],
        [
            Paragraph("<b>Schedule Resilience</b>", styles['TableCellBold']),
            Paragraph("Static; breaks when day is missed", styles['TableCell']),
            Paragraph("N/A (Self-paced catalog)", styles['TableCell']),
            Paragraph("<b>1-Click Missed-Day Rebalancer</b>", styles['TableCellBold'])
        ],
        [
            Paragraph("<b>Prioritization Logic</b>", styles['TableCellBold']),
            Paragraph("Manual to-do ordering", styles['TableCell']),
            Paragraph("None (Syllabus sequence)", styles['TableCell']),
            Paragraph("<b>Algorithmic Priority Index</b>", styles['TableCellBold'])
        ],
        [
            Paragraph("<b>Exam Intelligence</b>", styles['TableCellBold']),
            Paragraph("None", styles['TableCell']),
            Paragraph("Q&A database search", styles['TableCell']),
            Paragraph("<b>Past-Paper Recurrence Heatmap</b>", styles['TableCellBold'])
        ],
        [
            Paragraph("<b>AI Tutoring Mode</b>", styles['TableCellBold']),
            Paragraph("None", styles['TableCell']),
            Paragraph("Standard homework answers", styles['TableCell']),
            Paragraph("<b>Socratic Analogy-Based Coach</b>", styles['TableCellBold'])
        ],
        [
            Paragraph("<b>Institutional SaaS</b>", styles['TableCellBold']),
            Paragraph("None", styles['TableCell']),
            Paragraph("Employee upskilling portals", styles['TableCell']),
            Paragraph("<b>Campus Dean Retention Portal</b>", styles['TableCellBold'])
        ]
    ]

    t_diff = Table(diff_data, colWidths=[114, 126, 126, 138])
    t_diff.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), COLOR_PRIMARY),
        ('GRID', (0, 0), (-1, -1), 0.5, COLOR_BORDER),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, COLOR_LIGHT_BG])
    ]))
    story.append(t_diff)

    build_pdf_document(output_path, story, "03 Product Definition — BackLift AI")

if __name__ == "__main__":
    out_dir = r"C:\Users\gauth\OneDrive\Desktop\shambhu persnal folder\final_internship_project_backlift_ai"
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, "03 Product Definition.pdf")
    generate_pdf(out_file)
