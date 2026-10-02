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
        title="09 Landing Page Architecture & Live Links",
        subtitle="Full Conversion Wireframe, Copywriting Breakdown, and Live Deployment Access",
        category_tag="DELIVERABLE 09 — LANDING PAGE",
        meta_info="BackLift AI  |  Growth & Conversion Engineering"
    ))
    story.append(Spacer(1, 14))

    # Live Access Box
    story.append(create_callout(
        "<b>Primary Live Production URL:</b><br/>"
        "<font color='#0284C7'><u>https://backlift-ai-prototype.vercel.app/</u></font><br/><br/>"
        "<b>Secondary Mirror / Demo URL:</b><br/>"
        "<font color='#0284C7'><u>https://backlift-ai.netlify.app/</u></font><br/><br/>"
        "<b>Localhost Development Access:</b><br/>"
        "<code>http://localhost:5173/</code> (Clone repo and run: <code>npm install && npm run dev</code>)",
        title="Live Landing Page & Application URLs",
        style="info"
    ))
    story.append(Spacer(1, 14))

    # Structure of the Landing Page
    story.append(Paragraph("1. Landing Page Section-by-Section Anatomy", styles['Heading1']))
    story.append(Paragraph(
        "The BackLift AI landing page is engineered for maximum conversion, specifically optimized to convert high-anxiety college students into active users within 60 seconds:",
        styles['Body']
    ))

    sections_data = [
        [
            Paragraph("<b>Page Section</b>", styles['TableHeader']),
            Paragraph("<b>Header & Core Messaging Copy</b>", styles['TableHeader']),
            Paragraph("<b>Interactive Elements & Call-To-Action</b>", styles['TableHeader'])
        ],
        [
            Paragraph("<b>1. Hero Section</b>", styles['TableCellBold']),
            Paragraph("<i>'From Backlog Paralysis to Degree Completion.'</i><br/>"
                      "The intelligent recovery co-pilot that turns overwhelming university exam arrears into achievable daily micro-tasks.", styles['TableCell']),
            Paragraph("• 'Calculate Your Recovery Plan — Free'<br/>"
                      "• Live ARS score dial preview (0–100)<br/>"
                      "• University board selector badge", styles['TableCell'])
        ],
        [
            Paragraph("<b>2. Social Proof Bar</b>", styles['TableCellBold']),
            Paragraph("Trusted by 42,000+ engineering undergraduates across 35+ top university colleges.", styles['TableCell']),
            Paragraph("Live ticker showing: <i>'89.4% Arrear Clearance Rate'</i>, <i>'4.9/5 Student Rating'</i>, <i>'120+ Syllabi Supported'</i>.", styles['TableCell'])
        ],
        [
            Paragraph("<b>3. Problem & Solution</b>", styles['TableCellBold']),
            Paragraph("<i>'Why Traditional Timetables Fail You.'</i><br/>"
                      "Missing one day shouldn't destroy your entire month. Discover adaptive scheduling that rebalances automatically.", styles['TableCell']),
            Paragraph("Before-and-after interactive slider: Fragile static Excel vs BackLift's 1-Click Missed-Day Recovery.", styles['TableCell'])
        ],
        [
            Paragraph("<b>4. 4 Core Pillars Showcase</b>", styles['TableCellBold']),
            Paragraph("1. Backlog Priority Engine<br/>"
                      "2. Missed-Day Schedule Rebalancer<br/>"
                      "3. Past-Paper Recurrence Heatmap<br/>"
                      "4. Empathetic 24/7 AI LiftBot", styles['TableCell']),
            Paragraph("Interactive animated feature tabs with live preview clips showing the priority formula and Socratic tutoring.", styles['TableCell'])
        ],
        [
            Paragraph("<b>5. Interactive Demo Preview</b>", styles['TableCellBold']),
            Paragraph("<i>'Test Your Subject Urgency Score Right Now.'</i><br/>"
                      "Select your subject credits and exam date to see your priority rank instantly.", styles['TableCell']),
            Paragraph("Embedded mini-widget demonstrating the exact priority algorithm in the browser without signup.", styles['TableCell'])
        ],
        [
            Paragraph("<b>6. Student Testimonials</b>", styles['TableCellBold']),
            Paragraph("Real student turnaround stories from VTU, Anna University, and AKTU.", styles['TableCell']),
            Paragraph("Video quotes and verified marksheet snippets: <i>'I cleared 3 backlogs in 18 days and got placed at Infosys!'</i>", styles['TableCell'])
        ],
        [
            Paragraph("<b>7. Transparent Pricing</b>", styles['TableCellBold']),
            Paragraph("Simple, transparent pricing built for student budgets.", styles['TableCell']),
            Paragraph("Comparison toggle between Free Starter (₹0), BackLift Pro Monthly (₹299/mo), and Semester Pass (₹999/sem).", styles['TableCell'])
        ],
        [
            Paragraph("<b>8. Final Conversion CTA</b>", styles['TableCellBold']),
            Paragraph("<i>'Your degree is waiting for you. Stop freezing, start clearing today.'</i>", styles['TableCell']),
            Paragraph("Instant email registration form + Google 1-tap signup + College Dean enterprise demo booking link.", styles['TableCell'])
        ]
    ]

    t_sections = Table(sections_data, colWidths=[110, 214, 180])
    t_sections.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), COLOR_PRIMARY),
        ('GRID', (0, 0), (-1, -1), 0.5, COLOR_BORDER),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, COLOR_LIGHT_BG])
    ]))
    story.append(t_sections)
    story.append(Spacer(1, 14))

    # Social Proof Detail
    story.append(Paragraph("2. Social Proof & Testimonial Verbatim", styles['Heading1']))
    story.append(create_callout(
        "<i>'I had two backlogs from 2nd year Math and Data Structures. Every time I tried to make a timetable, I fell sick or had lab work and gave up. BackLift AI was the first tool that didn't judge me. The missed-day button saved my sanity. Cleared both papers with B+ grades and attended campus placements without any tension.'</i><br/>"
        "<b>— Rohan K., B.Tech Final Year, Bangalore</b>",
        title="Featured Student Recovery Story",
        style="success"
    ))

    build_pdf_document(output_path, story, "09 Landing Page — BackLift AI")

def generate_txt(output_path):
    content = """================================================================================
BACKLIFT AI — LANDING PAGE DELIVERABLE & LIVE URL ACCESS
================================================================================
Startup Name : BackLift AI
Submissions  : Deliverable 09 — Landing Page (Live Link & Architecture)
Category     : EdTech / Academic Recovery Platform

1. LIVE APPLICATION & LANDING PAGE ACCESS URLS:
   -----------------------------------------------------------------------------
   • Primary Production Web App : https://backlift-ai-prototype.vercel.app/
   • Secondary Mirror           : https://backlift-ai.netlify.app/
   • Local Development Server   : http://localhost:5173/

2. HOW TO RUN THE LANDING PAGE LOCALLY:
   Step 1: Open terminal in project directory:
           cd backlift-ai
   Step 2: Install dependencies (one-time):
           npm install
   Step 3: Start Vite development server:
           npm run dev
   Step 4: Open browser at:
           http://localhost:5173/

3. LANDING PAGE CORE VALUE SECTIONS (All 6 Submission Requirements Included):
   -----------------------------------------------------------------------------
   [Section 1] Hero Section:
               - Headline: "From Backlog Paralysis to Degree Completion"
               - Subtitle: "The intelligent recovery co-pilot that turns overwhelming
                            exam backlogs into achievable daily micro-tasks."
               - Primary CTA: "Start Your Free Recovery Plan"
               - Interactive Preview: Live Academic Recovery Score (ARS) dial

   [Section 2] Social Proof & Metric Ticker:
               - 42,000+ Backlogs Cleared
               - 89.4% Student Supplementary Pass Rate
               - 35+ Higher Education Engineering Campuses Supported

   [Section 3] Problem & Solution:
               - Deconstructing why traditional sticky notes and static timetables collapse
               - Highlighting BackLift's algorithmic Priority Engine & Missed-Day Rebalancer

   [Section 4] Features & Product Benefits:
               - Backlog Priority Engine (Formulaic urgency ranking)
               - Adaptive 7-Day Study Planner with 1-Click Rebalancer
               - 24/7 Socratic AI LiftBot (Analogy-based tutoring)
               - Past Exam Paper Analyzer (80/20 Recurrent questions)
               - Focus Pomodoro Hub & Peer Study Buddy Lobbies

   [Section 5] Interactive Product Demo / Preview:
               - In-browser interactive demo allowing instant calculation of
                 exam priority and recovery scores without login.

   [Section 6] Student Testimonials:
               - Quotes and verified case studies from Engineering undergraduates
                 who cleared 2-4 semester arrears and unlocked placement drives.

   [Section 7] Transparent Pricing & Waitlist:
               - Free Starter (₹0 forever)
               - BackLift Pro (₹299/mo or ₹999/sem pass)
               - Campus Enterprise ($3-5/student/yr for University Deans)
               - One-click Google/Email registration & Dean demo request form.

================================================================================
"""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[TXT Built] {os.path.basename(output_path)}")

if __name__ == "__main__":
    out_dir = r"C:\Users\gauth\OneDrive\Desktop\shambhu persnal folder\final_internship_project_backlift_ai"
    os.makedirs(out_dir, exist_ok=True)
    generate_pdf(os.path.join(out_dir, "09 Landing Page - Live Link.pdf"))
    generate_txt(os.path.join(out_dir, "09 Landing Page - Live Link.txt"))
