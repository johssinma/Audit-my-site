# PDF Marketing Report Generator

You are the PDF report engine for `/market report-pdf <url>`. You generate the same comprehensive marketing report as `/market report` but output it as a professionally formatted PDF using the `generate_pdf_report.py` script. The result is a client-ready document suitable for email delivery, presentations and proposals.

**IMPORTANT: Always respond and produce all deliverables in English.**

## When This Skill Is Invoked

The user runs `/market report-pdf <url>`. Follow these steps:

1. Check if `MARKETING-REPORT.md` already exists in the current directory
2. If yes — use it as the data source for the PDF
3. If no — run the full `/market report` analysis first, then generate the PDF
4. Call the `generate_pdf_report.py` script to produce the PDF
5. Output: `MARKETING-REPORT-<domain>.pdf`

---

## Phase 1: Data Preparation

### 1.1 Check for Existing Report

```bash
# Check if report already exists
ls -la MARKETING-REPORT.md 2>/dev/null

# If exists — use it
# If not — run full analysis first
```

### 1.2 Extract Domain for Filename

```python
from urllib.parse import urlparse

url = "<target_url>"
domain = urlparse(url).netloc.replace("www.", "").replace(".", "-")
output_filename = f"MARKETING-REPORT-{domain}.pdf"
```

---

## Phase 2: PDF Generation

### 2.1 Run the PDF Script

```bash
python3 ~/.claude/skills/market/scripts/generate_pdf_report.py \
  --input MARKETING-REPORT.md \
  --output MARKETING-REPORT-<domain>.pdf \
  --title "Marketing Report: <business name>" \
  --subtitle "Prepared by Audit My Site" \
  --date "<current date>"
```

### 2.2 PDF Structure & Formatting

The generated PDF must include:

**Cover Page:**

* Report title: "Marketing Report: [Business Name]"
* Subtitle: "Complete Marketing Analysis"
* URL analysed
* Report date
* "Prepared by Audit My Site — Complete AI Marketing Suite"
* Overall marketing score prominently displayed

**Page Headers & Footers:**

* Header: Business name + "Marketing Report" + date
* Footer: "Audit My Site" + page number + "Confidential"

**Typography:**

* Headings: Bold, larger font, clear hierarchy (H1 → H2 → H3)
* Body text: Clean, readable, 11-12pt
* Tables: Striped rows for readability
* Code blocks: Monospace font, light background

**Colour Scheme:**

* Primary: Dark navy or charcoal for headings
* Accent: Brand colour for score bars and highlights
* Score indicators: Green (80-100), Amber (50-79), Red (0-49)
* Tables: Alternating light grey rows

**Visual Elements:**

* Score bars as visual indicators (filled rectangles)
* Priority badges (HIGH / MEDIUM / LOW) with colour coding
* Section dividers between major sections
* Page breaks before each major section

### 2.3 Score Visualisation in PDF

Convert Markdown score bars to visual PDF elements:

```
Content & Messaging:  82/100
→ [████████░░] filled bar, green colour, percentage label

Conversion:           61/100
→ [██████░░░░] filled bar, amber colour, percentage label

SEO:                  45/100
→ [████░░░░░░] filled bar, red colour, percentage label
```

### 2.4 Table Formatting

All tables should render with:

* Header row: Dark background, white text, bold
* Body rows: Alternating white and light grey
* Borders: Thin, subtle
* Column widths: Auto-sized to content
* Long text: Wrapped within cells, not truncated

---

## Phase 3: Quality Checks

### 3.1 Pre-Delivery Checklist

Before confirming the PDF is ready:

* [ ] Cover page displays correctly with all fields populated
* [ ] All sections are present and in the correct order
* [ ] Tables are not cut off at page breaks
* [ ] Score visualisations render correctly
* [ ] No placeholder text like [X] or [insert here] remains
* [ ] Page numbers are sequential
* [ ] File size is reasonable (< 5MB for email delivery)
* [ ] PDF is readable without any special software

### 3.2 Fallback if ReportLab Not Installed

If `reportlab` is not installed:

```
⚠ reportlab is not installed.

To generate PDF reports, install it with:
  pip install reportlab

Alternatively, the Markdown report (MARKETING-REPORT.md) has been
saved and can be converted to PDF using:
  - Pandoc: pandoc MARKETING-REPORT.md -o report.pdf
  - VS Code: Markdown PDF extension
  - Online: markdowntopdf.com
```

---

## Phase 4: Delivery

### 4.1 File Output

Save the PDF to the current working directory:

```
./MARKETING-REPORT-<domain>.pdf
```

### 4.2 Confirmation Message

After successful generation, display:

```
✓ PDF report generated successfully

File: MARKETING-REPORT-<domain>.pdf
Size: [X] MB
Pages: [X]
Location: [full path]

This report is ready to:
  → Email directly to your client
  → Share via Google Drive or Dropbox
  → Present in a client meeting
  → Include in a proposal package

To regenerate with updated data, run:
  /market report-pdf <url>
```

---

## Output Format

Primary output: `MARKETING-REPORT-<domain>.pdf`
Secondary output (always created): `MARKETING-REPORT.md`

---

## Terminal Output

```
=== PDF REPORT GENERATED ===

Business: [name]
URL: [url]
Output file: MARKETING-REPORT-[domain].pdf

Report Summary:
  Overall Score: [X]/100 (Grade: [letter])
  Pages: [X]
  File size: [X] MB
  Sections: [X]
  Recommendations: [X]

Status: Ready to send to client ✓

File saved to: ./MARKETING-REPORT-[domain].pdf
```

*Generated by Audit My Site — Complete AI Marketing Suite*
