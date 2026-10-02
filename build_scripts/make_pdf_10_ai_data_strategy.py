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
        title="10 AI & Data Strategy Blueprint",
        subtitle="RAG Pipeline, Algorithmic Engines, Model Selection, and Data Governance",
        category_tag="DELIVERABLE 10 — AI / DATA STRATEGY",
        meta_info="BackLift AI  |  Technical Architecture & Machine Learning"
    ))
    story.append(Spacer(1, 14))

    # Executive Summary
    story.append(Paragraph("1. AI System Overview & Strategic Objective", styles['Heading1']))
    story.append(Paragraph(
        "<b>BackLift AI</b> does not treat Artificial Intelligence as a superficial wrapper or a generic chatbot. "
        "AI is deployed as an integrated cognitive infrastructure across three critical layers: "
        "<b>(1) Algorithmic Prioritization & Schedule Rebalancing</b>; <b>(2) Historical Past-Paper Recurrence Heuristics</b>; "
        "and <b>(3) Contextual Socratic Remediation via AI LiftBot</b>. "
        "Our objective is to deliver sub-500ms real-time tutoring while maintaining strict academic integrity, "
        "ensuring zero hallucination on university syllabus requirements.",
        styles['Body']
    ))
    story.append(Spacer(1, 10))

    # Input -> Processing -> Output Architecture
    story.append(Paragraph("2. Input → Processing → Output Pipeline Architecture", styles['Heading1']))
    
    pipeline_data = [
        [
            Paragraph("<b>Pipeline Stage</b>", styles['TableHeader']),
            Paragraph("<b>Data Elements & Ingestion Layer</b>", styles['TableHeader']),
            Paragraph("<b>Transformation & AI Logic</b>", styles['TableHeader']),
            Paragraph("<b>Output & User Experience</b>", styles['TableHeader'])
        ],
        [
            Paragraph("<b>1. Syllabus & Paper Ingestion</b>", styles['TableCellBold']),
            Paragraph("Raw university syllabus PDFs, 10-year question papers, marking schemes.", styles['TableCell']),
            Paragraph("Layout-aware optical parsing, regex unit segmentation, mathematical expression extraction.", styles['TableCell']),
            Paragraph("Structured JSON syllabus tree; 80/20 high-frequency question database.", styles['TableCell'])
        ],
        [
            Paragraph("<b>2. Student Academic State</b>", styles['TableCellBold']),
            Paragraph("Backlog subjects, credits, exam dates, prior attempts, daily study hours.", styles['TableCell']),
            Paragraph("Multi-factor <b>Backlog Priority Engine</b> computes Urgency × Credits × PrepGap.", styles['TableCell']),
            Paragraph("Ranked backlog queue with critical priority badges and countdown clocks.", styles['TableCell'])
        ],
        [
            Paragraph("<b>3. Adaptive Study Scheduling</b>", styles['TableCellBold']),
            Paragraph("Available daily hours, completed tasks, missed study intervals.", styles['TableCell']),
            Paragraph("Linear programming schedule optimizer + <b>Missed-Day Recovery Engine</b>.", styles['TableCell']),
            Paragraph("Dynamic 7-day study plan with automatically redistributed buffer slots.", styles['TableCell'])
        ],
        [
            Paragraph("<b>4. Socratic AI LiftBot</b>", styles['TableCellBold']),
            Paragraph("Student queries, uploaded class notes, past paper questions.", styles['TableCell']),
            Paragraph("Gemini 1.5 Flash via RAG pipeline with prompt engineering for analogy-based pedagogy.", styles['TableCell']),
            Paragraph("Instant conceptual explanations, step-by-step math proofs, and memory hooks.", styles['TableCell'])
        ],
        [
            Paragraph("<b>5. Diagnostic Verification</b>", styles['TableCellBold']),
            Paragraph("Quiz response logs, MCQ option selections, time-to-answer.", styles['TableCell']),
            Paragraph("Error pattern classifier tags recurring conceptual weaknesses.", styles['TableCell']),
            Paragraph("Updated Academic Recovery Score (ARS) & targeted remedial resource recommendations.", styles['TableCell'])
        ]
    ]

    t_pipe = Table(pipeline_data, colWidths=[100, 130, 140, 134])
    t_pipe.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), COLOR_PRIMARY),
        ('GRID', (0, 0), (-1, -1), 0.5, COLOR_BORDER),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, COLOR_LIGHT_BG])
    ]))
    story.append(t_pipe)
    story.append(Spacer(1, 14))

    # Model Selection & RAG
    story.append(Paragraph("3. AI Model Selection & Hybrid Inference Strategy", styles['Heading1']))
    story.append(Paragraph(
        "To balance low latency, computational cost, and academic precision, BackLift AI implements a tiered model routing architecture:",
        styles['Body']
    ))

    model_points = [
        ("<b>Tier 1: Google Gemini 1.5 Flash (Conversational & Quiz Inference):</b> Deployed for real-time AI LiftBot chat, Socratic analogies, and on-demand MCQ generation. Delivers ultra-low latency (<450ms) at $0.075 / 1M input tokens, allowing 90%+ gross margins on Pro subscriptions.", styles['Bullet']),
        ("<b>Tier 2: Gemini 1.5 Pro / Claude 3.5 Sonnet (Deep Paper Analysis):</b> Deployed asynchronously for complex engineering math derivations, optical past-paper layout parsing, and multi-step theorem verification.", styles['Bullet']),
        ("<b>Tier 3: text-embedding-004 + pgvector (Semantic Syllabus Search):</b> 768-dimensional embeddings of all university curriculum units stored in PostgreSQL via pgvector, enabling sub-20ms semantic retrieval of relevant topper notes and past questions.", styles['Bullet'])
    ]
    for text, s in model_points:
        story.append(Paragraph(text, s))
    story.append(Spacer(1, 12))

    # Ethical AI & Academic Integrity
    story.append(Paragraph("4. Ethical AI, Academic Integrity, and Compliance", styles['Heading1']))
    story.append(Paragraph(
        "Unlike generic LLM tools that facilitate assignment copying, BackLift AI is strictly engineered around <b>Ethical Remediation Guardrails</b>:<br/>"
        "• <b>Socratic Guidance, Never Direct Exam Solutions:</b> LiftBot is system-prompted to guide students through derivations step-by-step using questions, rather than spitting out complete assignment answers.<br/>"
        "• <b>Zero Real-Time Exam Assistance:</b> The platform detects and blocks live exam cheating queries via prompt inspection heuristics.<br/>"
        "• <b>Data Privacy & Security:</b> Fully compliant with the Indian Digital Personal Data Protection (DPDP) Act and global FERPA equivalents. Student test attempts and marks are encrypted at rest (AES-256) and never used to train public foundation models.",
        styles['Body']
    ))
    story.append(Spacer(1, 8))

    story.append(create_callout(
        "<b>Architectural Moat:</b> By pairing fine-tuned syllabus metadata with past-paper recurrence heuristics, BackLift AI generates study roadmaps that are 10x more targeted to passing supplementary exams than generic LLM queries.",
        title="Key AI Advantage",
        style="success"
    ))

    build_pdf_document(output_path, story, "10 AI Data Strategy — BackLift AI")

if __name__ == "__main__":
    out_dir = r"C:\Users\gauth\OneDrive\Desktop\shambhu persnal folder\final_internship_project_backlift_ai"
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, "10 AI Data Strategy.pdf")
    generate_pdf(out_file)
