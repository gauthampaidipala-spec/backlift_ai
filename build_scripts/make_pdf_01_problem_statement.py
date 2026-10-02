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
        title="01 Problem Statement",
        subtitle="Deconstructing Academic Backlogs, Student Paralysis, and Higher Education Retention",
        category_tag="DELIVERABLE 01 — CORE FOUNDATION",
        meta_info="BackLift AI  |  Track: EdTech & Remediation AI"
    ))
    story.append(Spacer(1, 14))

    # Executive Problem Overview
    story.append(Paragraph("1. Executive Summary & Problem Scope", styles['Heading1']))
    story.append(Paragraph(
        "Academic backlogs and semester arrears represent the single largest, most neglected crisis in undergraduate STEM and professional higher education. "
        "Every academic semester, tens of thousands of capable university students fail one or more examinations. Rather than an intellectual deficiency, "
        "this failure triggers a compounding psychological and logistical breakdown known as the <b>Backlog Paralysis Cycle</b>. "
        "Students are suddenly forced to prepare for past-semester uncleared papers alongside regular ongoing semester classes, projects, and lab submissions.",
        styles['Body']
    ))
    story.append(Spacer(1, 6))

    # Key Metrics Row
    metrics = [
        {"val": "38.4%", "lbl": "Undergraduates with Arrears", "sub": "Engineering & Tech (AISHE data)"},
        {"val": "68%", "lbl": "Placement Ineligibility", "sub": "Due to active backlogs"},
        {"val": "2.4x", "lbl": "Higher Dropout Risk", "sub": "Students with 2+ backlogs"},
        {"val": "₹1.4L - ₹3.2L", "lbl": "Cost of Extra Semester", "sub": "Tuition, lodging & lost earnings"}
    ]
    story.append(create_metric_card_row(metrics))
    story.append(Spacer(1, 14))

    # Detailed Problem Breakdown
    story.append(Paragraph("2. The Anatomy of Academic Backlog Paralysis", styles['Heading1']))
    story.append(Paragraph(
        "When an undergraduate student accumulates backlogs, traditional study methods break down completely due to four systemic stressors:",
        styles['Body']
    ))

    paralysis_points = [
        ("<b>Prioritization Blindness:</b> When facing 3 backlogs (e.g., Engineering Mathematics, Operating Systems, Microprocessors) plus 6 ongoing subjects, students cannot objectively compute which paper carries the greatest graduation risk or requires immediate intervention.", styles['Bullet']),
        ("<b>The Fragile Timetable Collapse:</b> Conventional time-management tools (spreadsheets, paper timetables, calendar blocks) are rigid. If a student misses a single 2-hour study block due to illness, fatigue, or college submissions, the entire 30-day schedule collapses. Guilt and defeat set in, leading to total study avoidance.", styles['Bullet']),
        ("<b>Syllabus Asymmetry & Information Scarcity:</b> Backlog students spend up to 60% of their limited cramming hours on low-weightage, obscure textbook chapters because they lack visibility into historical exam paper question frequency trends.", styles['Bullet']),
        ("<b>Psychological Isolation & Stigma:</b> Unlike regular semester courses where peer groups study collectively, backlog students feel profound shame. They are isolated from study circles, fear approaching professors, and lack a non-judgmental mentor.", styles['Bullet'])
    ]
    for text, style in paralysis_points:
        story.append(Paragraph(text, style))
    story.append(Spacer(1, 10))

    story.append(create_callout(
        "<b>The Psychological Reality:</b> Backlog failure is fundamentally a cognitive load and prioritization failure, not a lack of student intelligence. Without adaptive scheduling, students freeze in panic until 48 hours before the exam, resulting in repeated failures.",
        title="Key Diagnostic Insight",
        style="danger"
    ))
    story.append(Spacer(1, 14))

    # Target Users
    story.append(Paragraph("3. Target User Personas", styles['Heading1']))
    
    # Table of Personas
    persona_data = [
        [
            Paragraph("<b>Target Persona</b>", styles['TableHeader']),
            Paragraph("<b>Demographics & Context</b>", styles['TableHeader']),
            Paragraph("<b>Core Pain Points & Needs</b>", styles['TableHeader']),
            Paragraph("<b>BackLift Solution Fit</b>", styles['TableHeader'])
        ],
        [
            Paragraph("<b>The Placement-Blocked Senior</b><br/>(Rahul Sharma, 21)", styles['TableCellBold']),
            Paragraph("7th Semester B.Tech CSE.<br/>Carries 3 backlogs from Sem 2 & 4.<br/>Eligible for placements in 45 days.", styles['TableCell']),
            Paragraph("Campus recruiters require 0 active arrears. Terrified of losing job offers. Needs high-yield cramming plan.", styles['TableCell']),
            Paragraph("Priority Engine ranks highest-credit papers first; Exam Analyzer surfaces 80/20 repeated topics.", styles['TableCell'])
        ],
        [
            Paragraph("<b>The Repeat Arrear Candidate</b><br/>(Priya Patel, 20)", styles['TableCellBold']),
            Paragraph("5th Semester ECE.<br/>Failed Applied Mathematics-II twice.<br/>Has deep math anxiety.", styles['TableCell']),
            Paragraph("Paralyzed by past failures. Traditional textbooks are impenetrable. Loses motivation after 2 days.", styles['TableCell']),
            Paragraph("LiftBot Socratic tutor explains tough derivations using analogies; daily micro-quizzes build confidence.", styles['TableCell'])
        ],
        [
            Paragraph("<b>The Working / Commuter Student</b><br/>(Arjun Verma, 22)", styles['TableCellBold']),
            Paragraph("6th Semester Mech Engg.<br/>Works part-time job (4 hrs/day).<br/>Only 2.5 study hours available daily.", styles['TableCell']),
            Paragraph("Unpredictable shifts cause schedule misses. Needs plans that adapt automatically without guilt.", styles['TableCell']),
            Paragraph("Missed-Day Recovery Engine automatically rebalances missed hours across remaining days.", styles['TableCell'])
        ]
    ]

    t_persona = Table(persona_data, colWidths=[110, 124, 140, 130])
    t_persona.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), COLOR_PRIMARY),
        ('GRID', (0, 0), (-1, -1), 0.5, COLOR_BORDER),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, COLOR_LIGHT_BG])
    ]))
    story.append(t_persona)
    story.append(Spacer(1, 14))

    # Current Solutions & Why They Fail
    story.append(Paragraph("4. Analysis of Existing Solutions & Market Gaps", styles['Heading1']))
    
    comp_data = [
        [
            Paragraph("<b>Existing Solution</b>", styles['TableHeader']),
            Paragraph("<b>How It Works Today</b>", styles['TableHeader']),
            Paragraph("<b>Why It Fails for Backlog Students</b>", styles['TableHeader']),
            Paragraph("<b>BackLift AI Advantage</b>", styles['TableHeader'])
        ],
        [
            Paragraph("<b>Paper Timetables & Sticky Notes</b>", styles['TableCellBold']),
            Paragraph("Handwritten calendar blocks or Excel schedules.", styles['TableCell']),
            Paragraph("Completely static. A single missed study day causes irrecoverable failure.", styles['TableCell']),
            Paragraph("Dynamic algorithmic rebalancing with 1-click missed-day redistribution.", styles['TableCell'])
        ],
        [
            Paragraph("<b>Generic Productivity Tools</b><br/>(Notion, Todoist)", styles['TableCellBold']),
            Paragraph("Task checklists, kanban boards, reminders.", styles['TableCell']),
            Paragraph("Zero domain intelligence. Does not understand credits, syllabus, or exam dates.", styles['TableCell']),
            Paragraph("Pre-configured academic schema: credits, attempt multipliers, unit weights.", styles['TableCell'])
        ],
        [
            Paragraph("<b>EdTech Content Portals</b><br/>(Coursera, Chegg, Udemy)", styles['TableCellBold']),
            Paragraph("Massive 40-hour lecture video libraries.", styles['TableCell']),
            Paragraph("Information overload. Backlog students need 10-day targeted clearance, not 50 hrs of theory.", styles['TableCell']),
            Paragraph("Laser-targeted high-frequency past paper analysis & 15-minute concept summaries.", styles['TableCell'])
        ],
        [
            Paragraph("<b>Telegram & WhatsApp Groups</b>", styles['TableCellBold']),
            Paragraph("Peer sharing of notes and leaked questions.", styles['TableCell']),
            Paragraph("Chaotic, distraction-heavy, filled with unverified low-quality materials.", styles['TableCell']),
            Paragraph("Curated topper resources matched specifically to student's diagnosed weak topics.", styles['TableCell'])
        ]
    ]

    t_comp = Table(comp_data, colWidths=[110, 114, 140, 140])
    t_comp.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), COLOR_SECONDARY),
        ('GRID', (0, 0), (-1, -1), 0.5, COLOR_BORDER),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, COLOR_LIGHT_BG])
    ]))
    story.append(t_comp)
    story.append(Spacer(1, 14))

    # The Opportunity
    story.append(Paragraph("5. The Strategic & Economic Opportunity", styles['Heading1']))
    story.append(Paragraph(
        "The academic recovery space represents an untapped multi-billion-dollar niche within EdTech. "
        "While K-12 test prep and coding bootcamps are saturated, university remedial education remains completely unaddressed by modern software. "
        "Furthermore, university administrators (Deans and Chancellors) face severe institutional penalties when graduation rates drop. "
        "Under national accreditation frameworks (such as NAAC and NIRF in India, or ABET in the US), student dropout and delayed completion directly lower institutional rankings and government funding. "
        "<b>BackLift AI serves a dual economic beneficiary:</b> empowering students to clear backlogs affordably via B2C freemium, while selling enterprise retention intelligence to universities via B2B SaaS.",
        styles['Body']
    ))
    story.append(Spacer(1, 8))

    story.append(create_callout(
        "<b>Core Takeaway:</b> BackLift AI transforms academic failure from a terminal roadblock into an analytically managed recovery sprint. By replacing shame with structure and fragility with resilience, BackLift AI empowers every student to graduate on time.",
        title="The BackLift AI Thesis",
        style="success"
    ))

    build_pdf_document(output_path, story, "01 Problem Statement — BackLift AI")

if __name__ == "__main__":
    out_dir = r"C:\Users\gauth\OneDrive\Desktop\shambhu persnal folder\final_internship_project_backlift_ai"
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, "01 Problem Statement.pdf")
    generate_pdf(out_file)
