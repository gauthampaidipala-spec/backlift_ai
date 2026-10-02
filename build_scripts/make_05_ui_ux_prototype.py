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
        title="05 UI/UX Prototype Specification",
        subtitle="Complete Information Architecture, Screen Blueprints, and Interactive Prototype Links",
        category_tag="DELIVERABLE 05 — UI/UX PROTOTYPE",
        meta_info="BackLift AI  |  Figma Architecture & Screen Workflows"
    ))
    story.append(Spacer(1, 14))

    # Live Prototype Links Box
    story.append(create_callout(
        "<b>Interactive Figma Prototype Link:</b><br/>"
        "<font color='#0284C7'><u>https://www.figma.com/make/KN916hkdl3762ch5EnrQoV/backlift_ai?t=b51UAJWRmicmOZu8-1</u></font><br/><br/>"
        "<b>Working Interactive Web Prototype (Local / Live):</b><br/>"
        "• Localhost URL: <code>http://localhost:5173/</code><br/>"
        "• Production Deployment: <code>https://backlift-ai-prototype.vercel.app/</code><br/>"
        "• Repository Source: <code>backlift-ai (React 19 + TypeScript + Tailwind CSS)</code>",
        title="Official Prototype & Figma Deliverable Links",
        style="info"
    ))
    story.append(Spacer(1, 14))

    # Information Architecture & Screen Inventory
    story.append(Paragraph("1. Complete Prototype Screen Inventory", styles['Heading1']))
    story.append(Paragraph(
        "The BackLift AI user interface is structured into 12 core screens and interactive modals, strictly fulfilling the submission criteria:",
        styles['Body']
    ))

    screens_data = [
        [
            Paragraph("<b>Screen Name</b>", styles['TableHeader']),
            Paragraph("<b>Key UI Components & Controls</b>", styles['TableHeader']),
            Paragraph("<b>User Action & Dynamic State</b>", styles['TableHeader'])
        ],
        [
            Paragraph("<b>1. Landing / Hero Page</b>", styles['TableCellBold']),
            Paragraph("Hero headline, value proposition badges, interactive ARS calculator preview, social proof ticker, CTA button.", styles['TableCell']),
            Paragraph("Captures student interest; allows 1-click launch into the interactive recovery demo.", styles['TableCell'])
        ],
        [
            Paragraph("<b>2. Login & Signup</b>", styles['TableCellBold']),
            Paragraph("Social auth (Google/GitHub/College SSO), email registration, student semester verification.", styles['TableCell']),
            Paragraph("Creates student profile record; syncs state seamlessly to local and cloud storage.", styles['TableCell'])
        ],
        [
            Paragraph("<b>3. 4-Step Onboarding Modal</b>", styles['TableCellBold']),
            Paragraph("Step 1: College & Degree. Step 2: Semester & Daily Study Hours. Step 3: Backlog Subject Selection. Step 4: Exam Date Picker.", styles['TableCell']),
            Paragraph("Initializes student database; populates default priority scores and custom 7-day study plan.", styles['TableCell'])
        ],
        [
            Paragraph("<b>4. Student Command Dashboard</b>", styles['TableCellBold']),
            Paragraph("Dynamic Academic Recovery Score (ARS 0–100), exam countdown clocks, today's schedule checklist, quick study actions.", styles['TableCell']),
            Paragraph("Primary home base; allows 1-click task checkoffs, focus timer launches, and missed-day triggers.", styles['TableCell'])
        ],
        [
            Paragraph("<b>5. Backlog Lifecycle Manager</b>", styles['TableCellBold']),
            Paragraph("CRUD subject cards, credit multiplier badges, attempt counter, unit completion checklist, priority score meters.", styles['TableCell']),
            Paragraph("Allows adding new backlogs, editing credits/difficulty, and updating unit mastery percentages.", styles['TableCell'])
        ],
        [
            Paragraph("<b>6. Adaptive 7-Day Study Planner</b>", styles['TableCellBold']),
            Paragraph("Day-by-day calendar cards, morning/evening study blocks, subject tags, <b>'Missed-Day Recovery' button</b>.", styles['TableCell']),
            Paragraph("Visualizes 7-day sprint; clicking 'Missed-Day Recovery' smoothly redistributes missed tasks across future days.", styles['TableCell'])
        ],
        [
            Paragraph("<b>7. AI LiftBot (Academic Coach)</b>", styles['TableCellBold']),
            Paragraph("Interactive chat interface, quick suggestion chips ('Explain with analogy', 'Ask from my notes', 'Generate revision quiz').", styles['TableCell']),
            Paragraph("Provides instant, empathetic 24/7 Socratic explanations for tough engineering concepts.", styles['TableCell'])
        ],
        [
            Paragraph("<b>8. Past Exam Paper Analyzer</b>", styles['TableCellBold']),
            Paragraph("Year-by-year university exam paper list, unit mark distributions, question recurrence frequency heatmaps (80/20 topics).", styles['TableCell']),
            Paragraph("Enables students to filter high-yield topics that appear in 80%+ of university past papers.", styles['TableCell'])
        ],
        [
            Paragraph("<b>9. Diagnostic Quiz Generator</b>", styles['TableCellBold']),
            Paragraph("Interactive MCQ test runner, real-time timer, option selection, explanation modal, <b>Automatic Weak Topic Detector</b>.", styles['TableCell']),
            Paragraph("Tests student concept retention; failed questions automatically append weak topics to the student's revision list.", styles['TableCell'])
        ],
        [
            Paragraph("<b>10. Integrated Focus Pomodoro</b>", styles['TableCellBold']),
            Paragraph("25-minute circular progress timer, play/pause controls, subject selector, ambient noise toggle (White Noise / Rain / Library).", styles['TableCell']),
            Paragraph("Logs deep work focus minutes directly to student's total study hours and active backlog.", styles['TableCell'])
        ],
        [
            Paragraph("<b>11. Study Buddy Peer Lobbies</b>", styles['TableCellBold']),
            Paragraph("Active peer sprint groups, repeat exam lobbies (e.g., 'Math-II Arrear Sprint'), live participant avatars, shared goals.", styles['TableCell']),
            Paragraph("Fosters community motivation and healthy peer accountability; eliminates isolation.", styles['TableCell'])
        ],
        [
            Paragraph("<b>12. Institutional Dean Portal</b>", styles['TableCellBold']),
            Paragraph("Departmental failure rate heatmaps, student backlog distribution charts, early-warning dropout risk indicators.", styles['TableCell']),
            Paragraph("Demonstrates B2B enterprise value for university administrators and accreditation reporting.", styles['TableCell'])
        ]
    ]

    t_screens = Table(screens_data, colWidths=[120, 230, 154])
    t_screens.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), COLOR_PRIMARY),
        ('GRID', (0, 0), (-1, -1), 0.5, COLOR_BORDER),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING', (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, COLOR_LIGHT_BG])
    ]))
    story.append(t_screens)
    story.append(Spacer(1, 12))

    # Design System Specifications
    story.append(Paragraph("2. Design System Tokens & Component Standards", styles['Heading1']))
    story.append(Paragraph(
        "<b>Layout Grid:</b> Desktop: 12-column responsive grid (max-width 1280px) with 24px gutters. Mobile: Single column with 16px horizontal margins.<br/>"
        "<b>Elevation & Glassmorphism:</b> Translucent panels styled with <code>bg-slate-900/60 backdrop-blur-xl border border-white/[0.08]</code> to provide a modern, sleek aesthetic.<br/>"
        "<b>Accessibility (WCAG 2.1 AA):</b> High-contrast text on dark backgrounds (minimum 4.5:1 ratio for body copy; 7:1 for headings). Non-color dependent status indicators (badges feature both icons and text).",
        styles['Body']
    ))

    build_pdf_document(output_path, story, "05 UI/UX Prototype Specification — BackLift AI")

def generate_txt(output_path):
    content = """================================================================================
BACKLIFT AI — UI/UX PROTOTYPE SPECIFICATION & FIGMA DELIVERABLE
================================================================================
Startup Name : BackLift AI
Submissions  : Deliverable 05 — UI/UX Prototype (Figma & Working Code)
Category     : EdTech / Academic Recovery & Study Management Platform

1. LIVE FIGMA PROTOTYPE LINK:
   https://www.figma.com/make/KN916hkdl3762ch5EnrQoV/backlift_ai?t=b51UAJWRmicmOZu8-1

2. LIVE INTERACTIVE WEB PROTOTYPE (Production & Local):
   • Production URL : https://backlift-ai-prototype.vercel.app/
   • Localhost Dev  : http://localhost:5173/ (Run via `npm run dev`)
   • Codebase Path  : backlift-ai/ (React 19 + TypeScript + Vite + Tailwind CSS)

3. PROTOTYPE SCREEN ARCHITECTURE (All 12 Core Requirements Fulfilled):
   -----------------------------------------------------------------------------
   Screen 01: Home / Landing Page (Hero, Value Proposition, ARS Calculator Preview)
   Screen 02: Login / Signup (Email, Student SSO, Semester Credentials)
   Screen 03: 4-Step Academic Onboarding Modal (College, Backlog selection, Hours)
   Screen 04: Central Student Dashboard (Diagnostic ARS 0-100, Priority Engine, Clocks)
   Screen 05: Backlog Lifecycle CRUD Manager (Credit Multipliers, Unit Checklists)
   Screen 06: Adaptive 7-Day Study Planner (With 1-Click Missed-Day Recovery Engine)
   Screen 07: AI LiftBot Academic Coach (Socratic Tutoring, Analogy Explanations)
   Screen 08: Past Exam Paper Analyzer (80/20 Recurrent Question Heatmap)
   Screen 09: Diagnostic Quiz Generator & Weakness Detector (Automated Error Tags)
   Screen 10: Integrated Focus Pomodoro Timer (Subject-Tagged Study Session Logging)
   Screen 11: Study Buddy Peer Collaboration Lobbies (Arrear Group Sprints)
   Screen 12: Academic Recovery Progress Report & Export Modal (Printable PDF)

4. DESIGN SYSTEM SPECIFICATIONS:
   • Primary Colors: Deep Obsidian (#0B0F19), Indigo (#4F46E5), Cyan (#06B6D4)
   • Semantic Colors: Emerald (#10B981), Amber (#F59E0B), Crimson (#F43F5E)
   • Typography: Plus Jakarta Sans / Inter / JetBrains Mono
   • Visual Style: Dark Glassmorphic Modern UI with Tailwind CSS

================================================================================
"""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[TXT Built] {os.path.basename(output_path)}")

if __name__ == "__main__":
    out_dir = r"C:\Users\gauth\OneDrive\Desktop\shambhu persnal folder\final_internship_project_backlift_ai"
    os.makedirs(out_dir, exist_ok=True)
    generate_pdf(os.path.join(out_dir, "05 UI UX Prototype - Figma Link.pdf"))
    generate_txt(os.path.join(out_dir, "05 UI UX Prototype - Figma Link.txt"))
