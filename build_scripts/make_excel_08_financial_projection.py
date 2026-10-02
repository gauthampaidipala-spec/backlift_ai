import os
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

def build_financial_model(output_path):
    wb = openpyxl.Workbook()
    # Remove default sheet
    wb.remove(wb.active)

    # Styling Palette
    FONT_FAMILY = "Segoe UI"
    font_title = Font(name=FONT_FAMILY, size=16, bold=True, color="1E1B4B")
    font_subtitle = Font(name=FONT_FAMILY, size=10, italic=True, color="64748B")
    font_section = Font(name=FONT_FAMILY, size=12, bold=True, color="1E293B")
    font_header = Font(name=FONT_FAMILY, size=10, bold=True, color="FFFFFF")
    font_body = Font(name=FONT_FAMILY, size=10, color="1E293B")
    font_body_bold = Font(name=FONT_FAMILY, size=10, bold=True, color="1E293B")
    font_kpi_num = Font(name=FONT_FAMILY, size=14, bold=True, color="1E1B4B")
    font_kpi_lbl = Font(name=FONT_FAMILY, size=9, bold=True, color="64748B")

    fill_header = PatternFill(start_color="1E1B4B", end_color="1E1B4B", fill_type="solid")
    fill_sub_header = PatternFill(start_color="312E81", end_color="312E81", fill_type="solid")
    fill_zebra = PatternFill(start_color="F8FAFC", end_color="F8FAFC", fill_type="solid")
    fill_total = PatternFill(start_color="E2E8F0", end_color="E2E8F0", fill_type="solid")
    fill_kpi = PatternFill(start_color="F0F9FF", end_color="F0F9FF", fill_type="solid")
    fill_accent = PatternFill(start_color="ECFDF5", end_color="ECFDF5", fill_type="solid")

    thin_border_side = Side(border_style="thin", color="CBD5E1")
    thick_bottom_side = Side(border_style="medium", color="1E1B4B")
    double_bottom_side = Side(border_style="double", color="1E1B4B")

    cell_border = Border(left=thin_border_side, right=thin_border_side, top=thin_border_side, bottom=thin_border_side)
    total_border = Border(top=thin_border_side, bottom=double_bottom_side)

    # -------------------------------------------------------------------------
    # TAB 1: EXECUTIVE KPI DASHBOARD
    # -------------------------------------------------------------------------
    ws1 = wb.create_sheet(title="Executive Summary")
    ws1.views.sheetView[0].showGridLines = True

    ws1["A1"] = "BackLift AI — 3-Year Financial Model & Key Performance Metrics"
    ws1["A1"].font = font_title
    ws1["A2"] = "BridgeAura Internship Project Submission  |  Commercial Projections (INR ₹ / USD $)"
    ws1["A2"].font = font_subtitle

    # KPI Summary Cards (Row 4 to Row 6)
    kpis = [
        ("INITIAL FUNDING ASK", "₹3,500,000", "$42,000 Seed Round", 1),
        ("BREAK-EVEN TIMELINE", "Month 14", "Q2 Year 2 (Operational)", 3),
        ("BLENDED CAC", "₹145", "$1.75 per User", 5),
        ("CUSTOMER LTV", "₹1,196", "$14.40 (Pro User)", 7),
        ("LTV:CAC RATIO", "8.25x", "Top-Decile SaaS Metric", 9),
    ]

    for title, val, sub, col_idx in kpis:
        c_title = ws1.cell(row=4, column=col_idx, value=title)
        c_val = ws1.cell(row=5, column=col_idx, value=val)
        c_sub = ws1.cell(row=6, column=col_idx, value=sub)

        ws1.merge_cells(start_row=4, start_column=col_idx, end_row=4, end_column=col_idx+1)
        ws1.merge_cells(start_row=5, start_column=col_idx, end_row=5, end_column=col_idx+1)
        ws1.merge_cells(start_row=6, start_column=col_idx, end_row=6, end_column=col_idx+1)

        c_title.font = font_kpi_lbl
        c_val.font = font_kpi_num
        c_sub.font = font_subtitle

        for r in range(4, 7):
            for c in range(col_idx, col_idx+2):
                cell = ws1.cell(row=r, column=c)
                cell.fill = fill_kpi
                cell.alignment = Alignment(horizontal="center", vertical="center")
                cell.border = cell_border

    # 3-Year Summary Comparison Table
    ws1["A8"] = "3-Year High-Level Financial Performance Summary"
    ws1["A8"].font = font_section

    headers1 = ["Metric", "Unit", "Year 1 (FY 2026-27)", "Year 2 (FY 2027-28)", "Year 3 (FY 2028-29)", "CAGR / Growth"]
    for col_idx, h in enumerate(headers1, start=1):
        cell = ws1.cell(row=9, column=col_idx, value=h)
        cell.font = font_header
        cell.fill = fill_header
        cell.alignment = Alignment(horizontal="center" if col_idx > 1 else "left", vertical="center")
        cell.border = cell_border

    data1 = [
        ("Registered Students (Total)", "Users", 15000, 75000, 250000, "+307%"),
        ("Active BackLift Pro Subscribers", "Subscribers", 1200, 6750, 25000, "+356%"),
        ("Paying College Institutional Partners", "Colleges", 2, 12, 45, "+374%"),
        ("Gross B2C Subscription Revenue", "₹ INR", 3590000, 20220000, 74800000, "+356%"),
        ("Gross B2B Institutional Revenue", "₹ INR", 920000, 6630000, 23700000, "+407%"),
        ("Total Gross Revenue", "₹ INR", 4510000, 26850000, 98500000, "+367%"),
        ("Cost of Goods Sold (Hosting, LLMs)", "₹ INR", 680000, 3100000, 9900000, "+281%"),
        ("Gross Profit", "₹ INR", 3830000, 23750000, 88600000, "+380%"),
        ("Gross Margin %", "%", "84.9%", "88.5%", "89.9%", "+500 bps"),
        ("Total Operating Expenses (OPEX)", "₹ INR", 4720000, 17330000, 50400000, "+226%"),
        ("EBITDA / Net Operating Profit", "₹ INR", -890000, 6420000, 38200000, "Profitable Y2"),
        ("Net Profit Margin %", "%", "-19.7%", "23.9%", "38.8%", "High Margin"),
        ("Monthly Cash Burn (Average)", "₹ INR", 295000, 0, 0, "Cash Flow Positive"),
        ("Cash Runway (from Seed Capital)", "Months", "18 Months", "Self-Sustaining", "Self-Sustaining", "Strong")
    ]

    for row_idx, row_data in enumerate(data1, start=10):
        is_highlight = row_data[0] in ["Total Gross Revenue", "Gross Profit", "EBITDA / Net Operating Profit"]
        for col_idx, val in enumerate(row_data, start=1):
            cell = ws1.cell(row=row_idx, column=col_idx, value=val)
            cell.font = font_body_bold if is_highlight else font_body
            if is_highlight:
                cell.fill = fill_accent if "Profit" in row_data[0] or "Revenue" in row_data[0] else fill_total
            elif row_idx % 2 == 1:
                cell.fill = fill_zebra
            
            if isinstance(val, (int, float)):
                cell.number_format = '#,##0'
                cell.alignment = Alignment(horizontal="right", vertical="center")
            elif col_idx > 1:
                cell.alignment = Alignment(horizontal="center", vertical="center")
            else:
                cell.alignment = Alignment(horizontal="left", vertical="center")
            cell.border = cell_border

    # -------------------------------------------------------------------------
    # TAB 2: SETUP & CAPEX COSTS
    # -------------------------------------------------------------------------
    ws2 = wb.create_sheet(title="Capex & Setup Costs")
    ws2.views.sheetView[0].showGridLines = True

    ws2["A1"] = "Initial Capital Expenditure & Startup Setup Costs (Capex & Assets)"
    ws2["A1"].font = font_title
    ws2["A2"] = "Bootstrap and Seed Stage Infrastructure Allocation"
    ws2["A2"].font = font_subtitle

    headers2 = ["Category", "Expense / Asset Item", "Description & Specifications", "Vendor / Provider", "Estimated Cost (INR ₹)", "Estimated Cost (USD $)"]
    for col_idx, h in enumerate(headers2, start=1):
        cell = ws2.cell(row=4, column=col_idx, value=h)
        cell.font = font_header
        cell.fill = fill_header
        cell.alignment = Alignment(horizontal="center" if col_idx >= 5 else "left", vertical="center")
        cell.border = cell_border

    capex_items = [
        ("Software Assets", "Core Prototype Development", "React 19, TypeScript, Tailwind, Priority Engine core", "In-house Core Team", 350000, 4200),
        ("Software Assets", "LLM Fine-Tuning & Vector DB Setup", "pgvector schema, semantic chunking pipelines", "Google Cloud / OpenAI", 180000, 2160),
        ("Hardware / Equipment", "Developer Workstations (3 Units)", "High-performance dev laptops for AI engineering", "Dell / Apple", 280000, 3360),
        ("IP & Legal", "Company Incorporation & Legal Docs", "Private Limited incorporation, founder agreements", "Legal Counsel", 65000, 780),
        ("IP & Legal", "Trademark & IP Filing", "BackLift AI trademark & algorithm copyright filing", "IP Attorney", 45000, 540),
        ("Branding & Assets", "Brand Identity, Logo & Design Tokens", "Professional design assets, pitch collateral", "Design Agency", 75000, 900),
        ("Licensing & Tools", "Enterprise Dev Tooling (Year 1)", "GitHub Enterprise, Figma Org, Postman, Sentry", "Tool Vendors", 120000, 1440),
        ("Cloud Infrastructure", "Initial Cloud Credits & Staging Servers", "Google Cloud Run, Cloud SQL, Vercel Pro setup", "Google Cloud", 150000, 1800),
        ("Content Assets", "Past Exam Paper Ingestion (100 Syllabi)", "Curating, digitizing and parsing university papers", "Student Interns", 135000, 1620),
        ("Cash Contingency", "Reserve Working Capital", "Unforeseen setup expenses & currency buffer", "Reserve Account", 100000, 1200),
    ]

    for row_idx, item in enumerate(capex_items, start=5):
        for col_idx, val in enumerate(item, start=1):
            cell = ws2.cell(row=row_idx, column=col_idx, value=val)
            cell.font = font_body
            if row_idx % 2 == 1:
                cell.fill = fill_zebra
            if col_idx in [5, 6]:
                cell.number_format = '#,##0'
                cell.alignment = Alignment(horizontal="right", vertical="center")
            else:
                cell.alignment = Alignment(horizontal="left", vertical="center")
            cell.border = cell_border

    tot_row2 = len(capex_items) + 5
    ws2.cell(row=tot_row2, column=1, value="TOTAL INITIAL SETUP & CAPEX ASSETS").font = font_body_bold
    ws2.cell(row=tot_row2, column=5, value="=SUM(E5:E14)").font = font_body_bold
    ws2.cell(row=tot_row2, column=6, value="=SUM(F5:F14)").font = font_body_bold
    ws2.cell(row=tot_row2, column=5).number_format = '₹#,##0'
    ws2.cell(row=tot_row2, column=6).number_format = '$#,##0'
    for c in range(1, 7):
        cell = ws2.cell(row=tot_row2, column=c)
        cell.fill = fill_total
        cell.border = total_border

    # -------------------------------------------------------------------------
    # TAB 3: 3-YEAR P&L INCOME STATEMENT
    # -------------------------------------------------------------------------
    ws3 = wb.create_sheet(title="3-Year P&L Statement")
    ws3.views.sheetView[0].showGridLines = True

    ws3["A1"] = "Comprehensive 3-Year Profit & Loss (P&L) Statement"
    ws3["A1"].font = font_title
    ws3["A2"] = "Detailed Revenue, COGS, OPEX, and EBITDA Projections (FY 2026-27 to FY 2028-29)"
    ws3["A2"].font = font_subtitle

    headers3 = ["Financial Line Item", "Category", "Year 1 (INR ₹)", "Year 2 (INR ₹)", "Year 3 (INR ₹)", "% of Revenue (Y3)"]
    for col_idx, h in enumerate(headers3, start=1):
        cell = ws3.cell(row=4, column=col_idx, value=h)
        cell.font = font_header
        cell.fill = fill_header
        cell.alignment = Alignment(horizontal="center" if col_idx >= 3 else "left", vertical="center")
        cell.border = cell_border

    pnl_data = [
        ("REVENUE STREAMS", "Category Header", "", "", "", ""),
        ("B2C Pro Monthly Subscriptions (₹299/mo)", "Operating Revenue", 2150000, 11400000, 39500000, "40.1%"),
        ("B2C Semester Recovery Passes (₹999/sem)", "Operating Revenue", 1250000, 7200000, 28500000, "28.9%"),
        ("Content Add-ons (Solved Paper Packs @ ₹149)", "Operating Revenue", 190000, 1620000, 6800000, "6.9%"),
        ("B2B Campus Enterprise Licenses ($3-5/student)", "Operating Revenue", 920000, 6630000, 23700000, "24.1%"),
        ("TOTAL REVENUE", "Total", 4510000, 26850000, 98500000, "100.0%"),
        
        ("COST OF GOODS SOLD (COGS)", "Category Header", "", "", "", ""),
        ("LLM API Token Consumption (Gemini / Claude)", "Direct Cost", 280000, 1450000, 4800000, "4.9%"),
        ("Cloud Infrastructure (Compute, Vector DB, CDN)", "Direct Cost", 220000, 980000, 3100000, "3.1%"),
        ("Payment Gateway & Banking Fees (2.0%)", "Direct Cost", 90000, 537000, 1970000, "2.0%"),
        ("Customer Support & Content Verification", "Direct Cost", 90000, 133000, 30000, "0.0%"),
        ("TOTAL COGS", "Total", 680000, 3100000, 9900000, "10.1%"),
        
        ("GROSS PROFIT", "Subtotal", 3830000, 23750000, 88600000, "89.9%"),
        
        ("OPERATING EXPENSES (OPEX)", "Category Header", "", "", "", ""),
        ("Engineering & AI Product Salaries (3 to 8 engineers)", "Personnel", 2400000, 8400000, 24000000, "24.4%"),
        ("Sales, Campus Ambassadors & Growth Marketing", "Marketing", 1250000, 4800000, 14200000, "14.4%"),
        ("Community & Student Success Operations", "Operations", 380000, 1500000, 4600000, "4.7%"),
        ("General & Administrative (Legal, SaaS, Office)", "G&A", 450000, 1630000, 4800000, "4.9%"),
        ("Depreciation & Amortization", "Non-Cash", 240000, 1000000, 2800000, "2.8%"),
        ("TOTAL OPERATING EXPENSES", "Total", 4720000, 17330000, 50400000, "51.2%"),
        
        ("EBITDA / OPERATING PROFIT", "Final", -890000, 6420000, 38200000, "38.8%"),
        ("Corporate Income Tax (25% on profit)", "Tax", 0, 1605000, 9550000, "9.7%"),
        ("NET PROFIT AFTER TAX (PAT)", "Final", -890000, 4815000, 28650000, "29.1%")
    ]

    for row_idx, item in enumerate(pnl_data, start=5):
        is_header = item[1] == "Category Header"
        is_total = item[1] in ["Total", "Subtotal", "Final"]
        
        for col_idx, val in enumerate(item, start=1):
            cell = ws3.cell(row=row_idx, column=col_idx, value=val)
            if is_header:
                cell.font = font_section
                cell.fill = fill_sub_header
                cell.font = Font(name=FONT_FAMILY, size=10, bold=True, color="FFFFFF")
            elif is_total:
                cell.font = font_body_bold
                cell.fill = fill_accent if "NET PROFIT" in item[0] or "GROSS PROFIT" in item[0] else fill_total
                cell.border = total_border
            else:
                cell.font = font_body
                if row_idx % 2 == 1:
                    cell.fill = fill_zebra
                cell.border = cell_border
                
            if isinstance(val, (int, float)):
                cell.number_format = '₹#,##0'
                cell.alignment = Alignment(horizontal="right", vertical="center")
            elif col_idx >= 3:
                cell.alignment = Alignment(horizontal="center", vertical="center")
            else:
                cell.alignment = Alignment(horizontal="left", vertical="center")

    # -------------------------------------------------------------------------
    # TAB 4: UNIT ECONOMICS & METRICS
    # -------------------------------------------------------------------------
    ws4 = wb.create_sheet(title="Unit Economics & CAC-LTV")
    ws4.views.sheetView[0].showGridLines = True

    ws4["A1"] = "Unit Economics, Customer Acquisition Cost (CAC), and Lifetime Value (LTV)"
    ws4["A1"].font = font_title
    ws4["A2"] = "Detailed Cohort Economics for B2C Student Pro & B2B Campus Enterprise"
    ws4["A2"].font = font_subtitle

    headers4 = ["Unit Economic Metric", "B2C Student Pro", "B2B Campus Enterprise", "Blended / Comments"]
    for col_idx, h in enumerate(headers4, start=1):
        cell = ws4.cell(row=4, column=col_idx, value=h)
        cell.font = font_header
        cell.fill = fill_header
        cell.alignment = Alignment(horizontal="center" if col_idx > 1 else "left", vertical="center")
        cell.border = cell_border

    unit_data = [
        ("Average Revenue Per User / Contract (ARPU)", "₹299 / month or ₹999 / sem", "₹525,000 / college / yr", "Strong dual monetization"),
        ("Average Customer Lifespan", "4.0 Months (Exam Cycle)", "36.0 Months (Multi-year contract)", "High B2B institutional stickiness"),
        ("Customer Lifetime Value (LTV)", "₹1,196 ($14.40)", "₹1,575,000 ($18,900)", "High lifetime margin"),
        ("Gross Margin %", "89.0%", "92.0%", "Pure software scalability"),
        ("Gross Profit LTV", "₹1,064", "₹1,449,000", "Strong unit profit"),
        ("Customer Acquisition Cost (CAC)", "₹145 ($1.75)", "₹115,000 ($1,385)", "Viral campus ambassadors keep CAC low"),
        ("LTV to CAC Ratio", "8.25x", "13.7x", "Well above 3.0x industry benchmark"),
        ("CAC Payback Period", "1.8 Months", "2.6 Months", "Rapid cash recovery"),
        ("Monthly Churn Rate (End of Exam Cycle)", "18.0%", "1.2%", "Natural exam completion churn in B2C"),
        ("Organic Referral Rate (K-factor)", "1.35 (Viral)", "0.45 (Word of mouth)", "Every student invites 1.35 batchmates")
    ]

    for row_idx, item in enumerate(unit_data, start=5):
        for col_idx, val in enumerate(item, start=1):
            cell = ws4.cell(row=row_idx, column=col_idx, value=val)
            cell.font = font_body
            if row_idx % 2 == 1:
                cell.fill = fill_zebra
            if col_idx > 1:
                cell.alignment = Alignment(horizontal="center", vertical="center")
            else:
                cell.alignment = Alignment(horizontal="left", vertical="center")
            cell.border = cell_border

    # Auto-adjust column widths for all sheets
    for ws in [ws1, ws2, ws3, ws4]:
        for col in ws.columns:
            max_len = max(len(str(cell.value or '')) for cell in col)
            col_letter = get_column_letter(col[0].column)
            ws.column_dimensions[col_letter].width = max(max_len + 4, 12)

    wb.save(output_path)
    print(f"[XLSX Built] {os.path.basename(output_path)} -> {os.path.getsize(output_path)} bytes")

if __name__ == "__main__":
    out_dir = r"C:\Users\gauth\OneDrive\Desktop\shambhu persnal folder\final_internship_project_backlift_ai"
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, "08 Financial Projection.xlsx")
    build_financial_model(out_file)
