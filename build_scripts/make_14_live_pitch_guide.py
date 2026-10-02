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
        title="14 Live Pitch Script & Defense Guide",
        subtitle="Verbatim Speaking Scripts, Evaluator Q&A Defense, and Presentation Strategies",
        category_tag="DELIVERABLE 14 — LIVE PITCH DEFENSE",
        meta_info="BackLift AI  |  Founder Defense Playbook"
    ))
    story.append(Spacer(1, 14))

    # Executive Box
    story.append(create_callout(
        "<b>Purpose:</b> This playbook prepares the founder for the Top 5 Live Presentation defense before college academic panels and evaluation judges. Includes timed speaking scripts and winning answers to rigorous technical and commercial questions.",
        title="Official Live Presentation Playbook",
        style="info"
    ))
    story.append(Spacer(1, 14))

    # 1. 2-Minute Elevator Pitch
    story.append(Paragraph("1. The 2-Minute Elevator Pitch Script (Verbatim)", styles['Heading1']))
    story.append(Paragraph(
        "<i>[Target Duration: 120 Seconds | Tone: Empathetic, Authoritative, Urgent]</i><br/><br/>"
        "\"Respected professors and evaluation jury: across Indian technical universities today, over 38% of undergraduate engineering students carry uncleared academic backlogs. "
        "When an undergraduate fails a high-credit subject like Applied Mathematics or Operating Systems, they don't just lose marks—they lose their career momentum. "
        "Campus recruiters enforce zero-arrear rules, disqualifying 68% of capable applicants. "
        "Worst of all, students fall into the <b>Backlog Paralysis Cycle</b>: overwhelmed by multi-subject syllabi, their traditional paper timetables collapse on Day 2, and they freeze in panic. "
        "<br/><br/>"
        "That is why we built <b>BackLift AI</b>: the world's first adaptive Academic Recovery Operating System. "
        "Instead of static to-do lists, our proprietary <b>Backlog Priority Engine</b> mathematically calculates what to study today based on exam urgency, credits, and prior attempts. "
        "If a student falls sick or misses a day, our <b>Missed-Day Recovery Engine</b> smoothly redistributes the workload without guilt or panic. "
        "We analyze 10 years of university question papers to extract 80/20 high-yield topics, and provide an empathetic, 24/7 Socratic AI LiftBot to simplify complex derivations through real-world analogies. "
        "<br/><br/>"
        "With a viral B2C freemium model at ₹299 per month and an enterprise B2B campus portal that boosts college NAAC retention ratings, "
        "BackLift AI is lifting students out of backlog paralysis and guiding them across the graduation stage. Thank you!\"",
        styles['Body']
    ))
    story.append(Spacer(1, 14))

    # 2. Top Evaluator Q&A Defense
    story.append(Paragraph("2. Top 5 Evaluator Questions & Winning Answers", styles['Heading1']))
    
    qa_data = [
        [
            Paragraph("<b>Anticipated Evaluator Question</b>", styles['TableHeader']),
            Paragraph("<b>Winning Strategic & Technical Response</b>", styles['TableHeader'])
        ],
        [
            Paragraph("<b>Q1: 'Isn't this just another ChatGPT wrapper or to-do list?'</b>", styles['TableCellBold']),
            Paragraph("<b>Defense:</b> <i>'Absolutely not. ChatGPT has zero awareness of university academic structures, credit weightings, or exam dates. Generic task tools like Notion are static and break when a day is missed. BackLift AI features two proprietary computational algorithms: our multi-factor Priority Index and our linear programming Missed-Day Rebalancer. Furthermore, our RAG pipeline is grounded in 10-year university question paper recurrence data.'</i>", styles['TableCell'])
        ],
        [
            Paragraph("<b>Q2: 'Does your AI promote academic cheating or essay writing?'</b>", styles['TableCellBold']),
            Paragraph("<b>Defense:</b> <i>'No. BackLift AI is explicitly built around Socratic remediation guardrails. LiftBot never provides direct exam solutions. Instead, it explains underlying theoretical concepts through analogies and guides students step-by-step through practice MCQs. It acts as a supportive tutor, not a homework-copying engine.'</i>", styles['TableCell'])
        ],
        [
            Paragraph("<b>Q3: 'How do you convince broke college students to pay ₹299/month?'</b>", styles['TableCellBold']),
            Paragraph("<b>Defense:</b> <i>'The cost of an uncleared backlog is ₹1.4 Lakhs to ₹3.2 Lakhs in lost placement salary and delayed graduation. ₹299/month is less than the price of a single pizza, yet it protects placement eligibility. Our pilot data demonstrates an 8.0% free-to-paid conversion rate because the pain point is existential, not casual.'</i>", styles['TableCell'])
        ],
        [
            Paragraph("<b>Q4: 'Why would colleges buy the B2B Campus Enterprise portal?'</b>", styles['TableCellBold']),
            Paragraph("<b>Defense:</b> <i>'Under NIRF and NAAC accreditation in India, student retention and graduation rates carry up to 100 points in institutional scoring. A 10% drop in graduation rate directly lowers college rankings and government grants. BackLift Campus provides Deans with early-warning dropout analytics that prevent attrition before it occurs.'</i>", styles['TableCell'])
        ],
        [
            Paragraph("<b>Q5: 'How do you handle syllabus changes across different universities?'</b>", styles['TableCellBold']),
            Paragraph("<b>Defense:</b> <i>'Our architecture uses modular JSON syllabus schemas. Ingesting a new university regulation (such as VTU 2022 or Anna Univ 2021) takes less than 30 minutes using our optical layout parser. Our community campus ambassadors also contribute verified question papers in exchange for Pro subscriptions.'</i>", styles['TableCell'])
        ]
    ]

    t_qa = Table(qa_data, colWidths=[160, 344])
    t_qa.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), COLOR_PRIMARY),
        ('GRID', (0, 0), (-1, -1), 0.5, COLOR_BORDER),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, COLOR_LIGHT_BG])
    ]))
    story.append(t_qa)

    build_pdf_document(output_path, story, "14 Live Pitch Script — BackLift AI")

def generate_txt(output_path):
    content = """================================================================================
BACKLIFT AI — LIVE PITCH SCRIPT & DEFENSE PLAYBOOK
================================================================================
Startup Name : BackLift AI
Submissions  : Deliverable 14 — Live Pitch & Presentation Script (Top 5 Selection)
Category     : EdTech / Academic Recovery Platform

1. 2-MINUTE ELEVATOR PITCH (VERBATIM SCRIPT):
--------------------------------------------------------------------------------
"Respected professors and evaluation jury: across Indian technical universities
today, over 38% of undergraduate engineering students carry uncleared academic
backlogs. When an undergraduate fails a high-credit subject like Applied
Mathematics or Operating Systems, they don't just lose marks—they lose their
career momentum. Campus recruiters enforce zero-arrear rules, disqualifying 68%
of capable applicants. Worst of all, students fall into the Backlog Paralysis
Cycle: overwhelmed by multi-subject syllabi, their traditional paper timetables
collapse on Day 2, and they freeze in panic.

That is why we built BackLift AI: the world's first adaptive Academic Recovery
Operating System. Instead of static to-do lists, our proprietary Backlog Priority
Engine mathematically calculates what to study today based on exam urgency,
credits, and prior attempts. If a student falls sick or misses a day, our
Missed-Day Recovery Engine smoothly redistributes the workload without guilt or
panic. We analyze 10 years of university question papers to extract 80/20
high-yield topics, and provide an empathetic, 24/7 Socratic AI LiftBot to
simplify complex derivations through real-world analogies.

With a viral B2C freemium model at ₹299 per month and an enterprise B2B campus
portal that boosts college NAAC retention ratings, BackLift AI is lifting
students out of backlog paralysis and guiding them across the graduation stage.
Thank you!"

2. TOP 5 EVALUATION PANEL QUESTIONS & WINNING RESPONSES:
--------------------------------------------------------------------------------
Q1: "Isn't this just another ChatGPT wrapper or to-do list?"
A1: "Absolutely not. ChatGPT has zero awareness of university academic structures,
     credit weightings, or exam dates. Generic task tools like Notion are static
     and break when a day is missed. BackLift AI features two proprietary
     computational algorithms: our multi-factor Priority Index and our linear
     programming Missed-Day Rebalancer, grounded in 10-year past paper data."

Q2: "Does your AI promote academic cheating or essay writing?"
A2: "No. BackLift AI is explicitly built around Socratic remediation guardrails.
     LiftBot never provides direct exam solutions. Instead, it explains underlying
     theoretical concepts through analogies and guides students step-by-step
     through practice MCQs as an empathetic coach."

Q3: "How do you convince broke college students to pay ₹299/month?"
A3: "The cost of an uncleared backlog is ₹1.4 Lakhs to ₹3.2 Lakhs in lost
     placement salary and delayed graduation. ₹299/month is less than a single
     pizza, yet it protects placement eligibility. Our pilot shows an 8%
     conversion rate because the pain point is existential."

Q4: "Why would colleges buy the B2B Campus Enterprise portal?"
A4: "Under NIRF and NAAC accreditation in India, student retention and graduation
     rates carry up to 100 points in institutional scoring. A 10% drop in graduation
     rate directly lowers college rankings and government grants. BackLift Campus
     provides Deans with early-warning dropout analytics that prevent attrition."

Q5: "How do you handle syllabus changes across different universities?"
A5: "Our architecture uses modular JSON syllabus schemas. Ingesting a new
     university regulation takes under 30 minutes using our optical layout parser.
     Campus ambassadors also contribute verified question papers."

================================================================================
"""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[TXT Built] {os.path.basename(output_path)}")

if __name__ == "__main__":
    out_dir = r"C:\Users\gauth\OneDrive\Desktop\shambhu persnal folder\final_internship_project_backlift_ai"
    os.makedirs(out_dir, exist_ok=True)
    generate_pdf(os.path.join(out_dir, "14 Live Pitch Script & Defense Guide.pdf"))
    generate_txt(os.path.join(out_dir, "14 Live Pitch Script & Defense Guide.txt"))
