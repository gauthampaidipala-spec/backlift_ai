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
        title="04 User Journey Map",
        subtitle="End-to-End Behavioral Experience: From Backlog Paralysis to Degree Completion",
        category_tag="DELIVERABLE 04 — USER EXPERIENCE",
        meta_info="BackLift AI  |  UX Journey & Emotional Mapping"
    ))
    story.append(Spacer(1, 14))

    # Executive Overview
    story.append(Paragraph("1. User Journey Architecture", styles['Heading1']))
    story.append(Paragraph(
        "The BackLift AI user experience is deliberately architected around the psychological rehabilitation of an academically distressed student. "
        "Unlike standard enterprise software, our journey accounts for high cortisol levels, severe avoidance procrastination, "
        "and the pervasive stigma surrounding exam arrears. Every touchpoint is engineered to deliver immediate cognitive relief, "
        "actionable clarity, and continuous positive reinforcement.",
        styles['Body']
    ))
    story.append(Spacer(1, 10))

    # The 7 Stages Detailed Table
    story.append(Paragraph("2. The 7-Stage User Journey Matrix", styles['Heading1']))
    
    stages_data = [
        [
            Paragraph("<b>Stage & Touchpoint</b>", styles['TableHeader']),
            Paragraph("<b>User Goals & Mindset</b>", styles['TableHeader']),
            Paragraph("<b>Emotional State</b>", styles['TableHeader']),
            Paragraph("<b>Pain Points & Frustrations</b>", styles['TableHeader']),
            Paragraph("<b>BackLift AI Solution</b>", styles['TableHeader'])
        ],
        [
            Paragraph("<b>1. Awareness</b><br/><font size=7 color='#64748B'>Result Portal / Telegram</font>", styles['TableCellBold']),
            Paragraph("Views semester grade sheet. Discovers 2-3 backlogs. Panics over placement criteria.", styles['TableCell']),
            Paragraph("<font color='#E11D48'><b>Panic & Shame</b></font><br/>(Stress: 9.5/10)", styles['TableCell']),
            Paragraph("Overwhelmed; doesn't know where to start. Feels isolated from passing friends.", styles['TableCell']),
            Paragraph("Peer word-of-mouth & viral campus Telegram links: <i>'BackLift AI: Calculate your recovery plan in 90 seconds.'</i>", styles['TableCell'])
        ],
        [
            Paragraph("<b>2. Discovery</b><br/><font size=7 color='#64748B'>Landing Page / Mobile Web</font>", styles['TableCellBold']),
            Paragraph("Wants to see if an app can actually fix multi-subject backlogs.", styles['TableCell']),
            Paragraph("<font color='#D97706'><b>Skeptical Curiosity</b></font><br/>(Stress: 8.0/10)", styles['TableCell']),
            Paragraph("Hates complex setup. Tired of useless generic to-do list templates.", styles['TableCell']),
            Paragraph("Interactive Hero Section shows real-time Priority Engine calculator. Instant proof of domain relevance.", styles['TableCell'])
        ],
        [
            Paragraph("<b>3. Sign-up & Onboarding</b><br/><font size=7 color='#64748B'>Web App / 4-Step Modal</font>", styles['TableCellBold']),
            Paragraph("Input college, semester, backlog subjects, credit weights, and daily hours.", styles['TableCell']),
            Paragraph("<font color='#0284C7'><b>Cautious Hope</b></font><br/>(Stress: 6.5/10)", styles['TableCell']),
            Paragraph("Lengthy registration forms cause dropoff.", styles['TableCell']),
            Paragraph("Frictionless 4-step wizard with preloaded university syllabi & 1-click subject selection.", styles['TableCell'])
        ],
        [
            Paragraph("<b>4. First Use ('Aha!' Moment)</b><br/><font size=7 color='#64748B'>Central Dashboard</font>", styles['TableCellBold']),
            Paragraph("Wants to know: <i>'What exact subject and topic should I study right now?'</i>", styles['TableCell']),
            Paragraph("<font color='#059669'><b>Instant Relief</b></font><br/>(Stress: 4.0/10)", styles['TableCell']),
            Paragraph("Prioritization paralysis previously blocked action.", styles['TableCell']),
            Paragraph("Dashboard displays Diagnostic Recovery Score (ARS) & exact ranked study priorities.", styles['TableCell'])
        ],
        [
            Paragraph("<b>5. Core Experience</b><br/><font size=7 color='#64748B'>Study Planner & LiftBot</font>", styles['TableCellBold']),
            Paragraph("Completes daily 45m Pomodoro study sprints. Asks AI to explain difficult derivations.", styles['TableCell']),
            Paragraph("<font color='#059669'><b>Empowered Flow</b></font><br/>(Stress: 3.0/10)", styles['TableCell']),
            Paragraph("Getting stuck on a single concept derails an entire study evening.", styles['TableCell']),
            Paragraph("AI LiftBot provides instant analogy-based explanations; Past-Paper Analyzer highlights 80/20 topics.", styles['TableCell'])
        ],
        [
            Paragraph("<b>6. The Resilience Event</b><br/><font size=7 color='#64748B'>Missed-Day Engine</font>", styles['TableCellBold']),
            Paragraph("Student misses Day 4 due to college event or illness. Needs recovery plan.", styles['TableCell']),
            Paragraph("<font color='#312E81'><b>Reassured Calm</b></font><br/>(Stress: 2.0/10)", styles['TableCell']),
            Paragraph("Normally, a missed day leads to timetable collapse and abandonment.", styles['TableCell']),
            Paragraph("<b>1-Click Missed-Day Recovery</b> rebalances remaining topics smoothly across upcoming days.", styles['TableCell'])
        ],
        [
            Paragraph("<b>7. Outcome & Retention</b><br/><font size=7 color='#64748B'>Exam Hall & Community</font>", styles['TableCellBold']),
            Paragraph("Takes exam, scores 70%+, clears all arrears, receives placement offer.", styles['TableCell']),
            Paragraph("<font color='#059669'><b>Triumphant Confidence</b></font><br/>(Stress: 1.0/10)", styles['TableCell']),
            Paragraph("None (Milestone accomplished).", styles['TableCell']),
            Paragraph("Graduation celebration badge, shareable turnaround report, student becomes a campus brand advocate.", styles['TableCell'])
        ]
    ]

    t_stages = Table(stages_data, colWidths=[90, 104, 85, 110, 115])
    t_stages.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), COLOR_PRIMARY),
        ('GRID', (0, 0), (-1, -1), 0.5, COLOR_BORDER),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LEFTPADDING', (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, COLOR_LIGHT_BG])
    ]))
    story.append(t_stages)
    story.append(Spacer(1, 14))

    # Persona Walkthrough Narrative
    story.append(Paragraph("3. Deep Persona Walkthrough: Rahul Sharma's 21-Day Turnaround", styles['Heading1']))
    story.append(Paragraph(
        "<b>Day 1 (The Crisis):</b> Rahul, a 7th-semester Computer Science student at NIET, receives his supplementary examination dates. "
        "He has 14 days before <i>Engineering Mathematics-II (MATH201, 4 credits)</i> and 28 days before <i>Operating Systems (CS302, 3 credits)</i>. "
        "Campus placement drives begin in 30 days, and the policy is strict: students with uncleared backlogs cannot sit for interviews. "
        "Rahul is overwhelmed, unsure whether to focus on Math or OS.<br/><br/>"
        "<b>Day 2 (Onboarding & Clarity):</b> A senior recommends BackLift AI. Rahul enters his backlog subjects and specifies his daily capacity (4 hours). "
        "Within seconds, the <b>Backlog Priority Engine</b> identifies MATH201 as Critical Priority (Index 88/100) due to its 14-day proximity and 4-credit weight. "
        "The planner builds an achievable 7-day sprint: 2.5 hours on MATH201 (Unit 1 & 2 high-frequency topics) and 1.5 hours on CS302.<br/><br/>"
        "<b>Day 6 (The Resilience Test):</b> Rahul catches a viral fever and misses Day 5 entirely. Previously, this would have triggered total timetable abandonment. "
        "Instead, Rahul opens BackLift AI and clicks <b>'Missed-Day Recovery'</b>. The engine instantly detects the 4 unstudied hours and redistributes them "
        "by extending daily sessions by 40 minutes over the next 6 days. Zero panic; the plan remains completely intact.<br/><br/>"
        "<b>Day 14 (Exam Day & Victory):</b> Rahul takes the MATH201 supplementary exam. Over 75% of the questions match the high-frequency topics highlighted by "
        "BackLift AI's Past-Paper Analyzer. Two weeks later, results are published: Rahul passes with a B+ grade. He is officially placement-eligible and goes on to clear his campus drive interview.",
        styles['Body']
    ))
    story.append(Spacer(1, 8))

    story.append(create_callout(
        "<b>UX Design Principle:</b> The transition from anxiety to action must take under 120 seconds. BackLift AI prioritizes low cognitive friction, clear visual hierarchy, and instant rebalancing over complex configuration.",
        title="Core UX Philosophy",
        style="success"
    ))

    build_pdf_document(output_path, story, "04 User Journey Map — BackLift AI")

if __name__ == "__main__":
    out_dir = r"C:\Users\gauth\OneDrive\Desktop\shambhu persnal folder\final_internship_project_backlift_ai"
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, "04 User Journey Map.pdf")
    generate_pdf(out_file)
