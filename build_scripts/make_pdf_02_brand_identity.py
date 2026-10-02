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
        title="02 Brand Identity",
        subtitle="Visual, Emotional, and Strategic Architecture of BackLift AI",
        category_tag="DELIVERABLE 02 — BRAND SYSTEM",
        meta_info="BackLift AI  |  Brand Standards & Guidelines"
    ))
    story.append(Spacer(1, 14))

    # Brand Essence & Overview
    story.append(Paragraph("1. Brand Overview & Etymology", styles['Heading1']))
    story.append(Paragraph(
        "<b>BackLift AI</b> was established to bridge the chasm between academic despair and university graduation. "
        "The name is derived from two core concepts:",
        styles['Body']
    ))
    
    etymology_points = [
        ("<b>'Back':</b> Acknowledges the reality of academic <i>backlogs</i>, repeat examinations, and past setbacks without stigma or shame.", styles['Bullet']),
        ("<b>'Lift':</b> Represents upward momentum, resilience, psychological restoration, and elevating students back onto the degree completion track.", styles['Bullet']),
        ("<b>'AI':</b> Signifies the underlying computational intelligence—adaptive prioritization engines, heuristic syllabus analysis, and contextual tutoring.", styles['Bullet'])
    ]
    for text, s in etymology_points:
        story.append(Paragraph(text, s))
    story.append(Spacer(1, 8))

    # Taglines & Positioning
    story.append(create_callout(
        "<b>Primary Tagline:</b> <i>'Turn Backlog Paralysis into Degree Completion.'</i><br/>"
        "<b>Secondary Slogan:</b> <i>'Your Intelligent Academic Recovery Co-Pilot.'</i><br/>"
        "<b>Elevator Hook:</b> <i>'The first adaptive operating system engineered specifically to clear college backlogs.'</i>",
        title="Official Brand Taglines & Positioning Statements",
        style="info"
    ))
    story.append(Spacer(1, 14))

    # Brand Story
    story.append(Paragraph("2. The Brand Story: From Crisis to Clearance", styles['Heading1']))
    story.append(Paragraph(
        "In university corridors, academic failure is treated as an unspoken taboo. Capable, bright students who excel in practical problem-solving "
        "frequently stumble on theoretical, high-credit gateway subjects like Differential Equations, Data Structures, or Thermodynamics. "
        "Once a paper is failed, the university system offers no structured roadmap—only an exam re-registration receipt and a distant exam date. "
        "Left to fend for themselves, students spiral into anxiety, study paralysis, and eventually abandon career aspirations. "
        "<br/><br/>"
        "BackLift AI was born out of a simple conviction: <b>no student should drop out of college or lose placement eligibility because of an unguided backlog</b>. "
        "We reject toxic academic shaming. Instead, we engineer compassionate, data-driven software that treats academic recovery like an agile sprint—breaking down "
        "monolithic syllabi into achievable 25-minute micro-tasks, automatically restructuring schedules when life gets in the way, and standing by the student 24/7 as an unwavering mentor.",
        styles['Body']
    ))
    story.append(Spacer(1, 12))

    # Mission, Vision & Values
    story.append(Paragraph("3. Mission, Vision, and Core Pillars", styles['Heading1']))
    
    mv_data = [
        [
            Paragraph("<b>Dimension</b>", styles['TableHeader']),
            Paragraph("<b>Strategic Commitment</b>", styles['TableHeader'])
        ],
        [
            Paragraph("<b>Our Mission</b>", styles['TableCellBold']),
            Paragraph("To empower every undergraduate student to systematically overcome academic backlogs, eliminate exam anxiety, and graduate with confidence through personalized, resilient learning technology.", styles['TableCell'])
        ],
        [
            Paragraph("<b>Our Vision</b>", styles['TableCellBold']),
            Paragraph("To become the global standard recovery operating system in higher education, partnering with 1,000+ universities worldwide to eliminate avoidable dropouts and maximize student graduation rates.", styles['TableCell'])
        ],
        [
            Paragraph("<b>Pillar 1: Radical Empathy</b>", styles['TableCellBold']),
            Paragraph("Zero condescension or guilt. Every alert, message, and diagnostic score is formulated to encourage forward action and self-efficacy.", styles['TableCell'])
        ],
        [
            Paragraph("<b>Pillar 2: Mathematical Rigor</b>", styles['TableCellBold']),
            Paragraph("Study prioritization is not based on guesswork; it is mathematically optimized across exam urgency, credit weight, syllabus gaps, and historical frequency.", styles['TableCell'])
        ],
        [
            Paragraph("<b>Pillar 3: Antifragility</b>", styles['TableCellBold']),
            Paragraph("Human life is unpredictable. If a student misses a study session, the system does not break—it seamlessly rebalances the workload across future days.", styles['TableCell'])
        ]
    ]

    t_mv = Table(mv_data, colWidths=[140, 364])
    t_mv.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), COLOR_PRIMARY),
        ('GRID', (0, 0), (-1, -1), 0.5, COLOR_BORDER),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, COLOR_LIGHT_BG])
    ]))
    story.append(t_mv)
    story.append(Spacer(1, 14))

    # Brand Personality & Voice
    story.append(Paragraph("4. Brand Personality & Tone of Voice", styles['Heading1']))
    story.append(Paragraph(
        "BackLift AI embodies the persona of a <b>Strategic, Empathetic Academic Mentor</b>. "
        "The voice is confident yet compassionate, analytical yet accessible.",
        styles['Body']
    ))

    voice_data = [
        [
            Paragraph("<b>Communication Scenario</b>", styles['TableHeader']),
            Paragraph("<b>We Say (BackLift AI Voice)</b>", styles['TableHeader']),
            Paragraph("<b>We Never Say (Avoid)</b>", styles['TableHeader'])
        ],
        [
            Paragraph("<b>Student Misses a Day</b>", styles['TableCellBold']),
            Paragraph("<i>'Life happened! No worries. We rebalanced your remaining 4 days so you stay 100% on track.'</i>", styles['TableCell']),
            Paragraph("<i>'You missed your study goal yesterday. You are falling behind schedule!'</i>", styles['TableCell'])
        ],
        [
            Paragraph("<b>Low Diagnostic Quiz Score</b>", styles['TableCellBold']),
            Paragraph("<i>'Great diagnostic run! We pinpointed 2 concepts in Unit 2 to review. Here is a 3-minute summary.'</i>", styles['TableCell']),
            Paragraph("<i>'You scored 40%. You failed this quiz and are at risk of exam failure.'</i>", styles['TableCell'])
        ],
        [
            Paragraph("<b>High Exam Urgency</b>", styles['TableCellBold']),
            Paragraph("<i>'14 days to Math-II. Focusing on Fourier Series today gives you the highest pass-probability yield.'</i>", styles['TableCell']),
            Paragraph("<i>'Emergency! Time is running out. Start panicking and cramming.'</i>", styles['TableCell'])
        ]
    ]

    t_voice = Table(voice_data, colWidths=[120, 200, 184])
    t_voice.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), COLOR_SECONDARY),
        ('GRID', (0, 0), (-1, -1), 0.5, COLOR_BORDER),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, COLOR_LIGHT_BG])
    ]))
    story.append(t_voice)
    story.append(Spacer(1, 14))

    # Visual Identity System
    story.append(Paragraph("5. Visual Design System: Colors & Typography", styles['Heading1']))
    
    color_data = [
        [
            Paragraph("<b>Color Name</b>", styles['TableHeader']),
            Paragraph("<b>Hex Code</b>", styles['TableHeader']),
            Paragraph("<b>Psychological Meaning & Usage</b>", styles['TableHeader'])
        ],
        [
            Paragraph("<b>Deep Tech Obsidian</b>", styles['TableCellBold']),
            Paragraph("<code>#0B0F19</code>", styles['TableCell']),
            Paragraph("Primary background; reduces eye fatigue during late-night cram sessions; premium, distraction-free atmosphere.", styles['TableCell'])
        ],
        [
            Paragraph("<b>Deep Tech Indigo</b>", styles['TableCellBold']),
            Paragraph("<code>#4F46E5 / #6366F1</code>", styles['TableCell']),
            Paragraph("Primary brand identity; evokes intellectual rigor, academic reliability, and structured calmness.", styles['TableCell'])
        ],
        [
            Paragraph("<b>Electric Cyan</b>", styles['TableCellBold']),
            Paragraph("<code>#06B6D4 / #00F5FF</code>", styles['TableCell']),
            Paragraph("Accent & dynamic highlights; represents active AI intelligence, breakthrough insights, and optimism.", styles['TableCell'])
        ],
        [
            Paragraph("<b>Emerald Recovery</b>", styles['TableCellBold']),
            Paragraph("<code>#10B981</code>", styles['TableCell']),
            Paragraph("Progress & achievement; indicates completed study blocks, cleared backlogs, and positive score trajectory.", styles['TableCell'])
        ],
        [
            Paragraph("<b>High-Priority Amber</b>", styles['TableCellBold']),
            Paragraph("<code>#F59E0B</code>", styles['TableCell']),
            Paragraph("Urgency indicator; alerts students to approaching exams (within 14 days) or moderate topic gaps.", styles['TableCell'])
        ],
        [
            Paragraph("<b>Critical Crimson</b>", styles['TableCellBold']),
            Paragraph("<code>#F43F5E</code>", styles['TableCell']),
            Paragraph("Critical bottleneck warning; flags repeat arrear attempts requiring immediate sprint intervention.", styles['TableCell'])
        ]
    ]

    t_color = Table(color_data, colWidths=[120, 100, 284])
    t_color.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), COLOR_PRIMARY),
        ('GRID', (0, 0), (-1, -1), 0.5, COLOR_BORDER),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, COLOR_LIGHT_BG])
    ]))
    story.append(t_color)
    story.append(Spacer(1, 10))

    # Typography & Logo Symbolism
    story.append(Paragraph("6. Typography & Logo Architecture", styles['Heading1']))
    story.append(Paragraph(
        "<b>Typography Stack:</b> Primary Headings use <b>Plus Jakarta Sans / Inter Bold</b> for clean modern legibility. "
        "Body typography uses <b>Inter Regular</b> (14-16px, 1.5 line height) to ensure effortless readability during long study sessions. "
        "Calculations, priority scores, and code snippets use <b>JetBrains Mono</b>.<br/><br/>"
        "<b>Logo Symbolism:</b> The BackLift AI mark features an upward-pointing dual geometric chevron seamlessly blending into the wings of an open textbook. "
        "This encapsulates both the academic domain (textbook) and the trajectory of rapid recovery (upward lift). "
        "The mark is styled in an electric gradient shifting from Deep Indigo (`#4F46E5`) to Cyan (`#06B6D4`), symbolizing the transition from dark uncertainty into enlightened clarity.",
        styles['Body']
    ))

    build_pdf_document(output_path, story, "02 Brand Identity — BackLift AI")

if __name__ == "__main__":
    out_dir = r"C:\Users\gauth\OneDrive\Desktop\shambhu persnal folder\final_internship_project_backlift_ai"
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, "02 Brand Identity.pdf")
    generate_pdf(out_file)
