# Claude Skills: The Complete Developer Guide to Building Reusable AI Workflows (With Code) - Practical AI, Copilot & Modern Development Insights

Estimated reading time: 8 minutes

Claude Skills are structured Markdown-based instruction bundles that turn Claude into a specialist for any domain — from generating Word documents and PDFs to building MCP servers, creating generative art, automating Slack GIFs, and more. This guide covers all 17 available skills with practical code samples you can use today.

## Table of contents

-   [Introduction: What Are Claude Skills and Why Should Developers Care?](https://aidevme.com/claude-skills-complete-developer-guide/#h-introduction-what-are-claude-skills-and-why-should-developers-care)

-   [How Skills Work: Architecture and SKILL.md Format](https://aidevme.com/claude-skills-complete-developer-guide/#h-how-skills-work-architecture-and-skill-md-format)
-   [Document Automation Skills](https://aidevme.com/claude-skills-complete-developer-guide/#h-document-automation-skills)
    -   [docx — Word Document Generation](https://aidevme.com/claude-skills-complete-developer-guide/#h-docx-word-document-generation)
    -   [pdf — All PDF Operations](https://aidevme.com/claude-skills-complete-developer-guide/#h-pdf-all-pdf-operations)
    -   [pptx — Presentation Automation](https://aidevme.com/claude-skills-complete-developer-guide/#h-pptx-presentation-automation)
    -   [xlsx — Spreadsheet Generation](https://aidevme.com/claude-skills-complete-developer-guide/#h-xlsx-spreadsheet-generation)
    -   [Design and Frontend Skills](https://aidevme.com/claude-skills-complete-developer-guide/#h-design-and-frontend-skills)
-   [Creative & Media Skills](https://aidevme.com/claude-skills-complete-developer-guide/#h-creative-amp-media-skills)
    -   [algorithmic-art — Generative Art with p5.js](https://aidevme.com/claude-skills-complete-developer-guide/#h-algorithmic-art-generative-art-with-p5-js)
    -   [slack-gif-creator — Animated GIFs for Slack](https://aidevme.com/claude-skills-complete-developer-guide/#h-slack-gif-creator-animated-gifs-for-slack)
    -   [canvas-design — Python Canvas Artwork](https://aidevme.com/claude-skills-complete-developer-guide/#h-canvas-design-python-canvas-artwork)
-   [Developer & Agent Skills](https://aidevme.com/claude-skills-complete-developer-guide/#h-developer-amp-agent-skills)
    -   [mcp-builder — Build MCP Servers End-to-End](https://aidevme.com/claude-skills-complete-developer-guide/#h-mcp-builder-build-mcp-servers-end-to-end)
    -   [web-artifacts-builder — Complex Claude.ai Artifacts](https://aidevme.com/claude-skills-complete-developer-guide/#h-web-artifacts-builder-complex-claude-ai-artifacts)
    -   [skill-creator — Build and Evaluate Skills](https://aidevme.com/claude-skills-complete-developer-guide/#h-skill-creator-build-and-evaluate-skills)
-   [Productivity & Communication Skills](https://aidevme.com/claude-skills-complete-developer-guide/#h-productivity-amp-communication-skills)
    -   [doc-coauthoring — Structured Document Writing](https://aidevme.com/claude-skills-complete-developer-guide/#h-doc-coauthoring-structured-document-writing)
    -   [internal-comms — Communication Templates](https://aidevme.com/claude-skills-complete-developer-guide/#h-internal-comms-communication-templates)
    -   [product-self-knowledge — Anthropic Product Facts](https://aidevme.com/claude-skills-complete-developer-guide/#h-product-self-knowledge-anthropic-product-facts)
    -   [benepass-reimbursement — Browser Automation](https://aidevme.com/claude-skills-complete-developer-guide/#h-benepass-reimbursement-browser-automation)
-   [Skills vs MCP: When to Use Each](https://aidevme.com/claude-skills-complete-developer-guide/#h-skills-vs-mcp-when-to-use-each)

-   [Building Your Own Skill: Step-by-Step](https://aidevme.com/claude-skills-complete-developer-guide/#h-building-your-own-skill-step-by-step)
-   [Referenced Documents, Articles & Links](https://aidevme.com/claude-skills-complete-developer-guide/#h-referenced-documents-articles-amp-links)
    -   [Official Anthropic Documentation](https://aidevme.com/claude-skills-complete-developer-guide/#h-official-anthropic-documentation)
    -   [Model Context Protocol (MCP)](https://aidevme.com/claude-skills-complete-developer-guide/#h-model-context-protocol-mcp)
    -   [npm Packages Referenced](https://aidevme.com/claude-skills-complete-developer-guide/#h-npm-packages-referenced)
    -   [Python Packages Referenced](https://aidevme.com/claude-skills-complete-developer-guide/#h-python-packages-referenced)
    -   [CDN & Frontend Libraries](https://aidevme.com/claude-skills-complete-developer-guide/#h-cdn-amp-frontend-libraries)
    -   [Community Articles & Tutorials](https://aidevme.com/claude-skills-complete-developer-guide/#h-community-articles-amp-tutorials)
    -   [System Tools Referenced](https://aidevme.com/claude-skills-complete-developer-guide/#h-system-tools-referenced)

## Introduction: What Are Claude Skills and Why Should Developers Care?

In October 2025, Anthropic shipped a feature called **Skills** — and while it was initially framed as a productivity tool for knowledge workers, it’s one of the most developer-relevant releases in Claude’s history.

Here’s the core idea: instead of re-explaining a complex workflow to Claude every time you start a conversation, you package that workflow into a **Skill** — a folder containing a `SKILL.md` file (with YAML frontmatter and instructions), supporting scripts, and reference documents. Claude discovers relevant skills dynamically based on your request, loads only what it needs, and executes with the precision of a specialist rather than a generalist.

Markdown

```
your-project/
└── .claude/
    └── skills/
        ├── docx/
        │   └── SKILL.md
        ├── mcp-builder/
        │   ├── SKILL.md
        │   └── reference/
        │       ├── mcp_best_practices.md
        │       └── node_mcp_server.md
        └── pdf/
            ├── SKILL.md
            ├── FORMS.md
            └── REFERENCE.md
```

**Why this matters for developers:**

-   **No more prompt repetition.** Your conventions, patterns, and domain rules live in the skill, not in every conversation.

-   **Composable.** Multiple skills can activate together for complex tasks.
-   **Team-shareable.** Skills are just files — commit them, version them, distribute them.

-   **MCP-compatible.** Skills can reference and orchestrate MCP tool connections.

There are currently **17 skills** available — 6 public (shipping with Claude.ai) and 11 examples (demonstrating patterns you can adapt). This guide walks through every one of them with working code.

## How Skills Work: Architecture and SKILL.md Format

Every skill is a folder with at minimum one file: `SKILL.md`. The format uses YAML frontmatter for metadata and Markdown for instructions.

Markdown

```
---
name: my-skill
description: "Use this skill when the user asks to... [trigger conditions]. Do NOT use for..."
license: MIT
---

# My Skill Title

## Overview
What this skill does and how it works.

## Quick Reference
| Task | Approach |
|------|----------|
| Create X | Use tool Y |
| Edit X  | Unpack → modify → repack |

## Step-by-Step Instructions
...

## Code Examples
...

## Dependencies
- **tool-name**: purpose
```

**Progressive disclosure** is built in: Claude loads only the `name` and `description` at startup (a few dozen tokens per skill), then loads the full skill content on demand when it detects a match. This keeps context lean for unrelated tasks.

The `description` field is the most critical part — it’s the classifier that determines when the skill fires. Write it like a trigger specification: what to do, what NOT to do, and edge cases.

## Document Automation Skills

### docx — Word Document Generation

**Primary library:** `docx` (npm)  
**Supporting tools:** LibreOffice, pandoc, Poppler (pdftoppm)

The `docx` skill enables Claude to generate, edit, and validate Word `.docx` files using the `docx` npm package for creation and direct XML manipulation for editing existing documents.

**Install the dependency:**

Bash

```
npm install -g docx
```

#### Creating a document — minimal working example:

JavaScript

```
const { Document, Packer, Paragraph, TextRun, Table, TableRow,
        TableCell, HeadingLevel, BorderStyle, WidthType, ShadingType,
        LevelFormat, AlignmentType } = require('docx');
const fs = require('fs');

// CRITICAL: Always set US Letter explicitly — docx defaults to A4
const doc = new Document({
  numbering: {
    config: [{
      reference: "bullets",
      levels: [{ level: 0, format: LevelFormat.BULLET, text: "•",
        alignment: AlignmentType.LEFT,
        style: { paragraph: { indent: { left: 720, hanging: 360 } } }
      }]
    }]
  },
  sections: [{
    properties: {
      page: {
        size: { width: 12240, height: 15840 }, // US Letter in DXA (1440 DXA = 1 inch)
        margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 }
      }
    },
    children: [
      new Paragraph({
        heading: HeadingLevel.HEADING_1,
        children: [new TextRun({ text: "API Reference", bold: true })]
      }),
      new Paragraph({
        children: [new TextRun("The following endpoints are available:")]
      }),
      // Proper bullet list — never use unicode bullet characters directly
      new Paragraph({
        numbering: { reference: "bullets", level: 0 },
        children: [new TextRun("GET /users — list all users")]
      }),
      new Paragraph({
        numbering: { reference: "bullets", level: 0 },
        children: [new TextRun("POST /users — create a user")]
      }),
      // Table with dual-width (required for cross-platform compatibility)
      new Table({
        width: { size: 9360, type: WidthType.DXA }, // content width = 12240 - 2×1440
        columnWidths: [3120, 3120, 3120],
        rows: [
          new TableRow({
            children: ["Endpoint", "Method", "Auth"].map(text =>
              new TableCell({
                width: { size: 3120, type: WidthType.DXA },
                shading: { fill: "2E75B6", type: ShadingType.CLEAR },
                margins: { top: 80, bottom: 80, left: 120, right: 120 },
                children: [new Paragraph({
                  children: [new TextRun({ text, bold: true, color: "FFFFFF" })]
                })]
              })
            )
          })
        ]
      })
    ]
  }]
});

Packer.toBuffer(doc).then(buffer => fs.writeFileSync("output.docx", buffer));
```

**Key rules the skill enforces:**

-   Always use `WidthType.DXA` — `WidthType.PERCENTAGE` breaks in Google Docs.

-   Tables need **dual widths**: `columnWidths` array on the table AND `width` on each cell.
-   Never use `\n` inside `TextRun` — use separate `Paragraph` elements.

-   Use `ShadingType.CLEAR`, never `SOLID` (avoids black cell backgrounds).
-   `PageBreak` must live inside a `Paragraph`, not standalone.

**Editing existing documents follows a 3-step pattern:**

Bash

```


# Step 1: Unpack the ZIP/XML
python scripts/office/unpack.py document.docx unpacked/

# Step 2: Edit XML directly in unpacked/word/document.xml


# (Add tracked changes, comments, images, etc.)

# Step 3: Repack with validation and auto-repair
python scripts/office/pack.py unpacked/ output.docx --original document.docx
```

### pdf — All PDF Operations

**Primary libraries:** `pypdf`, `pdfplumber`, `reportlab`, `pypdfium2`, `pdf-lib` (JS), `pdfjs-dist` (JS)  
**OCR support:** `pytesseract` + `pdf2image`

Bash

```
pip install pypdf pdfplumber pypdfium2 reportlab pdf2image pytesseract --break-system-packages
```

#### **Merging PDFs:**

Python

```
from pypdf import PdfWriter, PdfReader

writer = PdfWriter()
for path in ["report.pdf", "appendix.pdf", "charts.pdf"]:
    writer.append(PdfReader(path))

with open("combined.pdf", "wb") as f:
    writer.write(f)
```

#### **Extracting tables from PDFs:**

Python

```
import pdfplumber
import pandas as pd

with pdfplumber.open("financial_report.pdf") as pdf:
    all_tables = []
    for page in pdf.pages:
        tables = page.extract_tables()
        for table in tables:
            df = pd.DataFrame(table[1:], columns=table[0])
            all_tables.append(df)

combined = pd.concat(all_tables, ignore_index=True)
combined.to_csv("extracted_tables.csv", index=False)
```

#### **Creating a PDF from scratch with reportlab:**

Python

```
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

doc = SimpleDocTemplate("report.pdf", pagesize=letter)
styles = getSampleStyleSheet()
story = []

story.append(Paragraph("Quarterly Report", styles['Heading1']))
story.append(Spacer(1, 12))

data = [["Metric", "Q3", "Q4"], ["Revenue", "$1.2M", "$1.8M"], ["Users", "4,200", "6,100"]]
t = Table(data)
t.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#2E75B6')),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#F0F4FF')]),
]))
story.append(t)
doc.build(story)
```

**Note:** ReportLab does NOT support Unicode subscripts directly. Use `<sub>` and `<super>` tags in Paragraph XML markup, not Unicode characters like ₂ or ².

### pptx — Presentation Automation

**Primary libraries:** `pptxgenjs` (npm), `markitdown[pptx]` (Python for extraction)

Bash

```
npm install -g pptxgenjs react react-dom react-icons sharp
pip install "markitdown[pptx]" Pillow --break-system-packages
```

#### Creating a slide deck programmatically:

JavaScript

```
const pptxgen = require("pptxgenjs");
const prs = new pptxgen();

// Define a reusable slide layout
prs.defineLayout({ name: "WIDE", width: 13.33, height: 7.5 });
prs.layout = "WIDE";

// Title slide
const slide1 = prs.addSlide();
slide1.background = { color: "1C2B4A" };
slide1.addText("Claude Skills", {
  x: 1, y: 2.5, w: 11, h: 1.5,
  fontSize: 48, bold: true, color: "FFFFFF", align: "center"
});
slide1.addText("A Complete Developer Guide", {
  x: 1, y: 4.2, w: 11, h: 0.6,
  fontSize: 20, color: "A8C4E8", align: "center"
});

// Content slide with table
const slide2 = prs.addSlide();
slide2.addText("Skill Categories", {
  x: 0.5, y: 0.3, w: 12, h: 0.7,
  fontSize: 28, bold: true, color: "1C2B4A"
});

const tableData = [
  [{ text: "Category", options: { bold: true, fill: "1C2B4A", color: "FFFFFF" } },
   { text: "Skills", options: { bold: true, fill: "1C2B4A", color: "FFFFFF" } }],
  ["Document Automation", "docx, pdf, pptx, xlsx"],
  ["Design & Frontend", "frontend-design, brand-guidelines, theme-factory"],
  ["Developer & Agent", "mcp-builder, web-artifacts-builder, skill-creator"],
  ["Creative & Media", "algorithmic-art, slack-gif-creator, canvas-design"],
];

slide2.addTable(tableData, {
  x: 0.5, y: 1.2, w: 12, h: 4,
  border: { type: "solid", color: "CCCCCC", pt: 0.5 },
  rowH: 0.65
});

prs.writeFile({ fileName: "claude-skills-overview.pptx" });
```

#### Extracting text from an existing PPTX:

Python

```
from markitdown import MarkItDown

md = MarkItDown()
result = md.convert("existing_deck.pptx")
print(result.text_content)
```

The pptx skill requires **visual QA** via subagents — it uses LibreOffice to render slides to images (`pdftoppm`) and inspects the output before finalizing. Never skip the visual check step.

### xlsx — Spreadsheet Generation

**Primary libraries:** `openpyxl` (create/format), `pandas` (data analysis)  
**Formula recalc:** LibreOffice via `scripts/recalc.py`

Bash

```
pip install openpyxl pandas --break-system-packages
```

#### Creating a financial model with proper Excel formulas:

Python

```
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, numbers
from openpyxl.utils import get_column_letter

wb = Workbook()
ws = wb.active
ws.title = "Revenue Model"

# Color convention: blue=inputs, black=formulas, green=cross-sheet, red=external
INPUT_FILL  = PatternFill("solid", fgColor="DDEEFF")
FORMULA_FILL = PatternFill("solid", fgColor="FFFFFF")
HEADER_FILL  = PatternFill("solid", fgColor="1C2B4A")

# Headers
headers = ["Metric", "Q1", "Q2", "Q3", "Q4", "FY Total"]
for col, header in enumerate(headers, 1):
    cell = ws.cell(row=1, column=col, value=header)
    cell.font = Font(bold=True, color="FFFFFF")
    cell.fill = HEADER_FILL

# Input rows (blue)
inputs = [
    ("Monthly Active Users", 4200, 4800, 5500, 6100),
    ("ARPU ($)",             12,   13,   14,   14),
]
for row_idx, (label, *values) in enumerate(inputs, start=2):
    ws.cell(row=row_idx, column=1, value=label)
    for col_idx, val in enumerate(values, start=2):
        cell = ws.cell(row=row_idx, column=col_idx, value=val)
        cell.fill = INPUT_FILL  # blue = user input

# Formula row (black) — always use Excel formulas, not Python-computed values
ws.cell(row=4, column=1, value="Revenue ($)")
for col in range(2, 6):
    col_letter = get_column_letter(col)
    # Formula references input cells — recalculated by Excel/LibreOffice
    cell = ws.cell(row=4, column=col,
                   value=f"={col_letter}2*{col_letter}3")
    cell.number_format = '#,##0'
    cell.fill = FORMULA_FILL

# FY Total column — SUM formula
ws.cell(row=4, column=6, value="=SUM(B4:E4)")
ws.cell(row=4, column=6).number_format = '#,##0'

# Column widths
for col in range(1, 7):
    ws.column_dimensions[get_column_letter(col)].width = 18

wb.save("revenue_model.xlsx")
```

### Design and Frontend Skills

#### frontend-design — Production-Grade UIs

The `frontend-design` skill is a guidance-only skill — no dependencies to install. It shapes how Claude approaches any UI generation task, enforcing a philosophy of **bold, distinctive aesthetics** over generic AI-generated output.

The skill explicitly bans:

-   **Inter, Roboto, Arial** as primary fonts (too generic).

-   **Purple gradients on white backgrounds** (overused AI cliché).
-   Centered hero layouts with identical padding (cookie-cutter pattern)

**What it encourages:**

JSX

```
// Example: A component styled with deliberate aesthetic choices
// (not generic Tailwind defaults)
import { useState } from "react";

export default function DataCard({ title, value, trend }) {
  const [hovered, setHovered] = useState(false);

  return (
    <div
      onMouseEnter={() => setHovered(true)}
      onMouseLeave={() => setHovered(false)}
      style={{
        // Distinctive: asymmetric layout, editorial typography, sharp contrast
        fontFamily: "'Playfair Display', serif",
        background: hovered ? "#0F1923" : "#131E2B",
        color: "#F0EDE6",
        borderLeft: "3px solid #D97757", // Anthropic orange as accent
        padding: "24px 28px",
        transition: "background 0.2s ease",
        transform: hovered ? "translateY(-2px)" : "none",
      }}
    >
      <div style={{ fontSize: "11px", letterSpacing: "0.15em",
                    color: "#788C5D", textTransform: "uppercase" }}>
        {title}
      </div>
      <div style={{ fontSize: "42px", fontWeight: "700", lineHeight: 1.1,
                    marginTop: "8px" }}>
        {value}
      </div>
      <div style={{ fontSize: "13px", color: trend > 0 ? "#6A9BCC" : "#D97757",
                    marginTop: "6px" }}>
        {trend > 0 ? "↑" : "↓"} {Math.abs(trend)}% vs last period
      </div>
    </div>
  );
}
```

#### brand-guidelines — Consistent Branding

A constants-only skill encoding Anthropic’s official brand palette and typography. Useful when building Claude-adjacent tools, demos, or documentation.

CSS

```
/* Anthropic Brand Colors */
:root {
  --color-dark:    #141413;  /* Primary dark */
  --color-light:   #FAF9F5;  /* Off-white background */
  --color-orange:  #D97757;  /* Primary accent */
  --color-blue:    #6A9BCC;  /* Secondary accent */
  --color-green:   #788C5D;  /* Tertiary accent */
}

/* Anthropic Typography */
/* Headings: Poppins */
/* Body: Lora */
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&family=Lora:ital,wght@0,400;0,600;1,400&display=swap');

body {
  font-family: 'Lora', serif;
  background: var(--color-light);
  color: var(--color-dark);
}

h1, h2, h3 {
  font-family: 'Poppins', sans-serif;
}
```

#### theme-factory — Pre-built Color Themes

Ten ready-to-apply design themes, each with a complete palette and font pairing. Reference them when building artifacts or UI components.

| **Theme** | **Primary** | **Accent** | **Vibe** |
| Ocean Depths | Deep navy | Cyan | Professional, calm |
| Sunset Boulevard | Warm amber | Coral | Energetic, warm |
| Arctic Frost | Ice white | Electric blue | Clean, modern |
| Botanical Garden | Forest green | Sage | Natural, organic |
| Desert Rose | Sand | Dusty rose | Minimal, earthy |
| Forest Canopy | Dark green | Gold | Rich, authoritative |
| Golden Hour | Warm gold | Terracotta | Luxurious |
| Midnight Galaxy | Deep purple | Violet | Creative, bold |
| Modern Minimalist | Pure white | Charcoal | Ultra-clean |
| Tech Innovation | Dark grey | Neon green | Developer-friendly |

### algorithmic-art — Generative Art with p5.js

**CDN dependency:** `https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.7.0/p5.min.js`

This two-phase skill generates interactive generative art artifacts. It first reads the `templates/viewer.html` file (mandatory step), then writes a p5.js sketch into it.

**Minimal working p5.js generative art sketch:**

HTML

```
<!DOCTYPE html>
<html>
<head>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.7.0/p5.min.js"></script>
</head>
<body>
<script>
// Seeded random for reproducibility
let seed = 42;
let particles = [];

function setup() {
  createCanvas(800, 600);
  randomSeed(seed);
  noiseSeed(seed);
  background(20, 20, 30);
  noStroke();

  // Initialize particles
  for (let i = 0; i < 300; i++) {
    particles.push({
      x: random(width),
      y: random(height),
      size: random(2, 8),
      speed: random(0.5, 2),
      hue: random(180, 260) // blue-purple range
    });
  }
}

function draw() {
  // Fade background each frame for trail effect
  fill(20, 20, 30, 15);
  rect(0, 0, width, height);

  for (let p of particles) {
    // Flow field using Perlin noise
    let angle = noise(p.x * 0.003, p.y * 0.003, frameCount * 0.005) * TWO_PI * 3;
    p.x += cos(angle) * p.speed;
    p.y += sin(angle) * p.speed;

    // Wrap around edges
    if (p.x < 0) p.x = width;
    if (p.x > width) p.x = 0;
    if (p.y < 0) p.y = height;
    if (p.y > height) p.y = 0;

    // Draw with color variation
    let alpha = map(p.size, 2, 8, 100, 200);
    fill(p.hue * 0.8, p.hue * 0.4, 255, alpha);
    ellipse(p.x, p.y, p.size);
  }
}
</script>
</body>
</html>
```

**The skill’s viewer template adds a fixed sidebar with Anthropic branding, seed controls, and real-time parameter adjustments — all built around this sketch as the core.**

### slack-gif-creator — Animated GIFs for Slack

**Dependencies:**

Bash

```
pip install pillow imageio imageio-ffmpeg numpy anthropic mcp --break-system-packages


# requirements.txt pinned versions:


# anthropic>=0.39.0


# mcp>=1.1.0


# pillow>=10.0.0


# imageio>=2.31.0


# imageio-ffmpeg>=0.4.9


# numpy>=1.24.0
```

**Two output formats:**

-   **Emoji:** 128×128 px

-   **Message GIF:** 480×480 px

**Working GIF generation example (Python):**

Python

```
from PIL import Image, ImageDraw
import imageio
import numpy as np

def create_pulse_gif(output_path: str, size: int = 128, frames: int = 20):
    """Create a pulsing circle GIF suitable for Slack emoji."""
    images = []

    for frame in range(frames):
        # Easing: sine wave for smooth pulse
        t = frame / frames
        scale = 0.6 + 0.35 * np.sin(t * 2 * np.pi)

        img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)

        radius = int(size * scale * 0.4)
        center = size // 2
        bbox = [center - radius, center - radius,
                center + radius, center + radius]

        # Outer glow
        glow_r = radius + 6
        draw.ellipse([center - glow_r, center - glow_r,
                      center + glow_r, center + glow_r],
                     fill=(106, 155, 204, 60))  # Anthropic blue, low alpha

        # Main circle
        draw.ellipse(bbox, fill=(217, 119, 87, 230))  # Anthropic orange

        images.append(np.array(img))

    imageio.mimsave(output_path, images, fps=24, loop=0)
    print(f"GIF saved: {output_path} ({size}×{size}, {frames} frames)")

create_pulse_gif("pulse_emoji.gif", size=128, frames=20)
```

### canvas-design — Python Canvas Artwork

Generates visual design philosophy expressed as PNG or PDF artwork using Python canvas tools (matplotlib/Pillow). Useful for design system documentation, cover images, and data-driven artwork.

Python

```
from PIL import Image, ImageDraw, ImageFont
import numpy as np

def generate_gradient_poster(width=1200, height=800, title="System Architecture"):
    img = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(img)

    # Gradient background
    for y in range(height):
        t = y / height
        r = int(20 + t * 10)
        g = int(20 + t * 15)
        b = int(30 + t * 40)
        draw.line([(0, y), (width, y)], fill=(r, g, b))

    # Grid overlay (subtle)
    for x in range(0, width, 80):
        draw.line([(x, 0), (x, height)], fill=(255, 255, 255, 15))
    for y in range(0, height, 80):
        draw.line([(0, y), (width, y)], fill=(255, 255, 255, 15))

    # Title text (would use a loaded font in production)
    draw.text((60, 60), title, fill=(240, 237, 230))
    draw.text((60, 110), "Generated with Claude Canvas Design Skill",
              fill=(120, 140, 93))  # Anthropic green

    img.save("poster.png", quality=95)

generate_gradient_poster()
```

## Developer & Agent Skills

### mcp-builder — Build MCP Servers End-to-End

This is the most technically sophisticated skill in the library. It guides Claude through a 4-phase MCP server build: **Research → Implement → Review → Evals**.

**Reference sources it fetches at runtime:**

-   MCP spec: `[https://modelcontextprotocol.io/sitemap.xml](https://modelcontextprotocol.io/sitemap.xml)`

-   TypeScript SDK: `[https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/README.md](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/README.md)`
-   Python SDK: `[https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/main/README.md](https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/main/README.md)`

**TypeScript MCP server (HTTP/Streamable transport):**

TypeScript

```
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StreamableHTTPServerTransport } from "@modelcontextprotocol/sdk/server/streamableHttp.js";
import { z } from "zod";
import express from "express";

const server = new McpServer({
  name: "dataverse-search",
  version: "1.0.0"
});

// Define a tool with Zod schema validation
server.tool(
  "search_accounts",
  "Search Dataverse accounts by name or email",
  {
    query: z.string().describe("Search term for name or email"),
    top: z.number().int().min(1).max(50).default(10)
         .describe("Max number of results to return"),
  },
  async ({ query, top }) => {
    const encoded = encodeURIComponent(query);
    const url = `https://your-org.crm.dynamics.com/api/data/v9.2/accounts` +
                `?$filter=contains(name,'${encoded}') or contains(emailaddress1,'${encoded}')` +
                `&$top=${top}&$select=name,emailaddress1,telephone1`;

    const resp = await fetch(url, {
      headers: {
        "Authorization": `Bearer ${process.env.DATAVERSE_TOKEN}`,
        "OData-MaxVersion": "4.0",
        "Accept": "application/json"
      }
    });

    if (!resp.ok) {
      throw new Error(`Dataverse API error: ${resp.status} ${resp.statusText}`);
    }

    const data = await resp.json();
    return {
      content: [{
        type: "text",
        text: JSON.stringify(data.value, null, 2)
      }]
    };
  }
);

// HTTP transport setup
const app = express();
app.use(express.json());

app.post("/mcp", async (req, res) => {
  const transport = new StreamableHTTPServerTransport({ sessionIdGenerator: undefined });
  await server.connect(transport);
  await transport.handleRequest(req, res, req.body);
});

const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`MCP server running on http://localhost:${port}/mcp`);
});
```

**Python MCP server (FastMCP, stdio transport):**

Python

```
from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel, Field
from typing import Optional
import httpx

mcp = FastMCP("dataverse-search")

class SearchParams(BaseModel):
    query: str = Field(..., description="Search term for name or email")
    top: int = Field(10, ge=1, le=50, description="Max results")

@mcp.tool()
async def search_accounts(query: str, top: int = 10) -> str:
    """Search Dataverse accounts by name or email."""
    encoded = query.replace("'", "''")
    url = (f"https://your-org.crm.dynamics.com/api/data/v9.2/accounts"
           f"?$filter=contains(name,'{encoded}')"
           f"&$top={top}&$select=name,emailaddress1")

    async with httpx.AsyncClient() as client:
        resp = await client.get(url, headers={
            "Authorization": f"Bearer {_get_token()}",
            "OData-MaxVersion": "4.0"
        })
        resp.raise_for_status()
        return resp.text

if __name__ == "__main__":
    mcp.run()
```

**Evaluation harness** (the skill ships a full evaluation framework):

Python

```


# Run the eval suite against your MCP server


# The skill connects to a running server, sends test cases, grades responses
python scripts/evaluation.py \
  -t http \
  -u http://localhost:3000/mcp \
  -m claude-sonnet-4-20250514 \
  --test-cases tests/search_accounts.json
```

**MCP naming conventions the skill enforces:**

-   Tools: `verb_noun` — `search_accounts, create_lead, get_invoice`

-   Server names: `service_name-mcp — dataverse-mcp, github-mcp, jira-mcp`
-   Use `_` not `-` in tool names; use `-` in server names

### web-artifacts-builder — Complex Claude.ai Artifacts

**Tech stack:** React 18 + TypeScript + Tailwind CSS + shadcn/ui  
**shadcn/ui docs:** `https://ui.shadcn.com/docs/components`

This skill produces self-contained `bundle.html` files — single-file artifacts that can be dropped into Claude.ai conversations or served standalone.

Bash

```


# Initialize a new artifact project
bash scripts/init-artifact.sh my-dashboard

# After development, bundle to single HTML
bash scripts/bundle-artifact.sh src/ bundle.html
```

**`shadcn/ui` component example (from within an artifact):**

TypeScript

```
import { useState } from "react";
import { Alert, AlertDescription, AlertTitle } from '@/components/ui/alert';
import { Badge } from '@/components/ui/badge';

interface SkillCardProps {
  name: string;
  category: string;
  dependencies: string[];
  status: "active" | "loading" | "error";
}

export function SkillCard({ name, category, dependencies, status }: SkillCardProps) {
  const [expanded, setExpanded] = useState(false);

  return (
    <div className="rounded-lg border border-slate-200 p-4 hover:shadow-md transition-shadow">
      <div className="flex items-center justify-between">
        <div>
          <h3 className="font-semibold text-slate-900">{name}</h3>
          <Badge variant="outline" className="mt-1 text-xs">{category}</Badge>
        </div>
        <div className={`w-2 h-2 rounded-full ${
          status === "active" ? "bg-green-500" :
          status === "loading" ? "bg-yellow-500 animate-pulse" : "bg-red-500"
        }`} />
      </div>

      {expanded && (
        <Alert className="mt-3">
          <AlertTitle>Dependencies</AlertTitle>
          <AlertDescription>
            {dependencies.join(", ")}
          </AlertDescription>
        </Alert>
      )}

      <button
        onClick={() => setExpanded(!expanded)}
        className="mt-2 text-xs text-slate-500 hover:text-slate-700"
      >
        {expanded ? "Hide" : "Show"} dependencies
      </button>
    </div>
  );
}
```

**Design rules the skill enforces:**

-   No purple gradients (overused).

-   No Inter as the only font (generic).
-   No centered-everything layouts (boring).

-   Always use Tailwind core utilities only — no compiler required in artifacts

### skill-creator — Build and Evaluate Skills

**The meta-skill for building other skills. It provides a full evaluation loop:**

Markdown

```
Draft SKILL.md
     ↓
Run eval (spawn subagents with/without skill)
     ↓
Generate comparison report (eval-viewer/generate_review.py)
     ↓
Human review
     ↓
Improve description / instructions
     ↓
Re-run eval → iterate until pass rate ≥ threshold
     ↓
Package skill (scripts/package_skill.py)
```

**Running an evaluation:**

Bash

```


# Run benchmark comparing with-skill vs without-skill
python scripts/run_eval.py \
  --skill-path .claude/skills/my-skill \
  --test-cases tests/my-skill-cases.json \
  --model claude-sonnet-4-20250514

# Generate visual HTML report
python eval-viewer/generate_review.py \
  --results results/my-skill-eval.json \
  --output report.html
```

The grader agent (`agents/grader.md`) scores each output on accuracy, completeness, and adherence to skill instructions. The comparator agent (`agents/comparator.md`) produces side-by-side diffs. The analyzer agent (`agents/analyzer.md`) synthesizes patterns across failures.

## Productivity & Communication Skills

### doc-coauthoring — Structured Document Writing

**A process-only skill (no dependencies) that enforces a 3-stage writing workflow:**

1.  **Context Gathering** — Claude interviews you about purpose, audience, constraints, and key messages before writing a word.
2.  **Refinement** — Iterative drafting with structured feedback loops.
3.  **Reader Testing** — Claude reads the draft as the target audience and reports what’s confusing, missing, or over-explained.

Best used for: RFPs, architecture decision records (ADRs), technical specifications, white papers, and any document where precision matters.

### internal-comms — Communication Templates

**Pre-built templates for four communication types:**

-   **3P Updates** (Third-Party stakeholder updates).

-   **Company Newsletter** sections.
-   **FAQ Answers** (structured Q&A format).

-   **General Comms** (announcements, policy changes)

Each template follows a consistent structure: headline → context → what changed → impact → next steps → contact.

### product-self-knowledge — Anthropic Product Facts

A live-documentation skill — it fetches current Anthropic docs before answering any product question, rather than relying on potentially stale training data.

**Key URLs it always consults:**

| **Topic** | **Source** |
| **Claude API** | `https://docs.claude.com/en/api/overview` |
| **Claude Code** | `https://docs.anthropic.com/en/docs/claude-code/overview` |
| **Claude.ai Help** | `https://support.claude.com` |
| **Claude Code npm** | `https://www.npmjs.com/package/@anthropic-ai/claude-code` |

Useful when building integrations, pricing calculators, or feature-gating logic that depends on current plan limits or API capabilities.

### benepass-reimbursement — Browser Automation

A browser automation skill targeting `https://app.getbenepass.com`. It demonstrates the pattern for any authenticated web workflow:

1.  Navigate to the target URL.
2.  Authenticate via SSO/OAuth (with explicit user confirmation).
3.  Fill in expense form fields.
4.  Upload receipt via file input.
5.  Submit (with user confirmation before final click)

This pattern applies to any enterprise portal, HRIS, or internal tool that lacks an API.

## Skills vs MCP: When to Use Each

A common point of confusion — here’s the clear mental model:

|  | **MCP Server** | **Claude Skill** |
| **What it is** | A tool/API connector | A workflow instruction set |
| **Purpose** | Gives Claude *access* to data/systems | Tells Claude *what to do* with that access |
| **Lifecycle** | Always-on once connected | Dynamically loaded per-task |
| **Contents** | Tool definitions, schemas, auth | Markdown instructions, scripts, examples |
| **Analogy** | The aisle of tools in a hardware store | The expert who knows which tool to grab |

## Building Your Own Skill: Step-by-Step

Here’s a minimal template to create a custom skill for, say, a TypeScript code reviewer:

**Decision table:**

**1\. Create the folder structure:**

Markdown

```
.claude/
└── skills/
    └── ts-code-reviewer/
        ├── SKILL.md
        └── reference/
            └── conventions.md
```

**2\. Write `SKILL.md`:**

Markdown

```
---
name: ts-code-reviewer
description: "Use this skill when the user asks to review, audit, or critique TypeScript
  code. Also use when they say 'review my PR', 'check my types', or 'improve this
  component'. Do NOT use for JavaScript-only files, Python, or infrastructure code."
license: MIT
---

# TypeScript Code Reviewer

## Review Checklist

Run through all of these before giving feedback:

1. **Type safety** — No `any` types without explicit justification. Prefer `unknown` for
   external data, then narrow with type guards.
2. **Null safety** — Every nullable access uses optional chaining (`?.`) or null checks.
3. **Error handling** — All async functions have try/catch. Errors are typed, not `catch(e: any)`.
4. **Naming** — Interfaces use `I` prefix only for ambient declarations. Generic types use
   descriptive names (`TItem` not `T`).
5. **Performance** — No inline object/array creation in render functions without `useMemo`.
6. **Test coverage** — Every exported function has at least one test.

## Output Format

Respond with:
1. A summary score (0–10) with one-sentence rationale
2. Critical issues (blocking) — must fix before merge
3. Suggestions (non-blocking) — nice to have
4. One specific refactoring example showing before/after

## Reference

See reference/conventions.md for project-specific patterns.
```

**3\. Write `reference/conventions.md`** with any project-specific rules.

**4\. Test it:**

Markdown

```


# In Claude Code CLI
claude "Review this TypeScript function for me: [paste code]"


# Claude should auto-detect and load the skill
```

**5\. Evaluate and iterate** using the `skill-creator` skill.

---

Found this useful? Share it with your team or drop a comment below.

## Referenced Documents, Articles & Links

### Official Anthropic Documentation

-   [Claude API Overview](https://docs.claude.com/en/api/overview)

-   [Claude API Docs Map](https://docs.claude.com/en/docs_site_map.md)
-   [Claude Code Overview](https://docs.anthropic.com/en/docs/claude-code/overview)

-   [Claude Code Docs Map](https://docs.anthropic.com/en/docs/claude-code/claude_code_docs_map.md)
-   [Claude.ai Help Center](https://support.claude.com/)

-   [Claude Code npm Package](https://www.npmjs.com/package/@anthropic-ai/claude-code)
-   [Anthropic Product News](https://www.anthropic.com/news)

-   [Anthropic Enterprise Sales](https://www.anthropic.com/contact-sales)

### Model Context Protocol (MCP)

-   [MCP Official Site & Sitemap](https://modelcontextprotocol.io/sitemap.xml)

-   [MCP Specification (Draft)](https://modelcontextprotocol.io/specification/draft.md)
-   [TypeScript SDK (GitHub README)](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/README.md)

-   [Python SDK (GitHub README)](https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/main/README.md)

### npm Packages Referenced

-   [`docx` — Word document generation](https://www.npmjs.com/package/docx)

-   [`pptxgenjs` — PowerPoint generation](https://www.npmjs.com/package/pptxgenjs)
-   [`pdf-lib` — PDF creation & manipulation (JS)](https://www.npmjs.com/package/pdf-lib)

-   [`pdfjs-dist` — PDF rendering (JS)](https://www.npmjs.com/package/pdfjs-dist)
-   [`@modelcontextprotocol/sdk` — MCP TypeScript SDK](https://www.npmjs.com/package/@modelcontextprotocol/sdk)

-   [`zod` — TypeScript schema validation](https://www.npmjs.com/package/zod)
-   [`express` — HTTP server framework](https://www.npmjs.com/package/express)

-   [`axios` — HTTP client](https://www.npmjs.com/package/axios)
-   [`sharp` — High-performance image processing](https://www.npmjs.com/package/sharp)

-   [`react-icons` — Icon library for React](https://www.npmjs.com/package/react-icons)

### Python Packages Referenced

-   [`pypdf` — PDF reading, merging, splitting](https://pypi.org/project/pypdf/)

-   [`pdfplumber` — PDF table/text extraction](https://pypi.org/project/pdfplumber/)
-   [`pypdfium2` — PDF rendering (PDFium bindings)](https://pypi.org/project/pypdfium2/)

-   [`reportlab` — PDF generation from Python](https://pypi.org/project/reportlab/)
-   [`pdf2image` — PDF to image conversion](https://pypi.org/project/pdf2image/)

-   [`pytesseract` — OCR via Tesseract](https://pypi.org/project/pytesseract/)
-   [`openpyxl` — Excel file creation & editing](https://pypi.org/project/openpyxl/)

-   [`pandas` — Data analysis & tabular manipulation](https://pypi.org/project/pandas/)
-   [`Pillow` — Python Imaging Library (PIL fork)](https://pypi.org/project/Pillow/)

-   [`imageio` — Image/GIF/video I/O](https://pypi.org/project/imageio/)
-   [`numpy` — Numerical computing](https://pypi.org/project/numpy/)

-   [`anthropic` — Anthropic Python SDK](https://pypi.org/project/anthropic/)
-   [`mcp` — MCP Python SDK (FastMCP)](https://pypi.org/project/mcp/)

-   [`pydantic` — Data validation](https://pypi.org/project/pydantic/)
-   [`httpx` — Async HTTP client](https://pypi.org/project/httpx/)

-   [`markitdown` — Markdown extraction (incl. PPTX)](https://pypi.org/project/markitdown/)
-   [`defusedxml` — Safe XML parsing](https://pypi.org/project/defusedxml/)

### CDN & Frontend Libraries

-   [p5.js v1.7.0 (CDN)](https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.7.0/p5.min.js)

-   [shadcn/ui Component Docs](https://ui.shadcn.com/docs/components)
-   [shadcn/ui JSON Schema](https://ui.shadcn.com/schema.json)

### Community Articles & Tutorials

-   [Claude Got Skills! Here’s How I Used It to Automate My Entire SEO Workflow](https://aimaker.substack.com/p/what-are-claude-skills-ai-workflow-automation)

-   [37 Claude Skills Examples to Transform How You Work (From 23 Creators)](https://aiblewmymind.substack.com/p/claude-skills-36-examples)
-   [Building Production-Ready AI Agents with Claude Skills and MCP: A Complete Tutorial](https://medium.com/@jageenshukla/build-production-ai-agents-with-claude-skills-mcp-882d70ffe9ee)

-   [Claude Code to AI OS Blueprint: Skills, Hooks, Agents & MCP Setup in 2026](https://dev.to/jan_lucasandmann_bb9257c/claude-code-to-ai-os-blueprint-skills-hooks-agents-mcp-setup-in-2026-46gg)
-   [MCP Skill Hub: A Production-Ready Server for Managing Claude Skills](https://medium.com/@srprasanna/mcp-skill-hub-a-production-ready-server-for-managing-claude-skills-0fe4b4899e7b)

-   [Beyond Deadwoodworks: How Claude Code Skills Super-charge MCP Servers](https://dev.to/fourixai/beyond-deadwoodworks-how-claude-code-skills-super-charge-mcp-servers-and-everyday-workflows-69)
-   [Claude Code Capabilities with Skills and MCP Servers](https://medium.com/@moelkholy1995/claude-code-capabilities-with-skills-and-mcp-servers-2b5e87ea8e0d)

-   [Specializing Claude Code: Agent Skills and MCP on Databricks](https://medium.com/@hiydavid/specializing-claude-code-a-quick-guide-to-agent-skills-and-mcp-on-databricks-c0cfdd43637d)
-   [AI-Assisted Development Workflows with Claud](https://dev.to/tim_derzhavets/ai-assisted-development-workflows-with-claude-code-and-mcp-10og)[e](https://dev.to/tim_derzhavets/ai-assisted-development-workflows-with-claude-code-and-mcp-10og) [Code and MCP](https://dev.to/tim_derzhavets/ai-assisted-development-workflows-with-claude-code-and-mcp-10og)

-   [The 10 Must-Have MCP Servers for Claude Code (2025 Developer Edition)](https://roobia.medium.com/the-10-must-have-mcp-servers-for-claude-code-2025-developer-edition-43dc3c15c887)
-   [I Ran Claude SEO on My Sites — Here’s What It Found](https://mejba.me/index.php/blog/claude-seo-toolkit-guide)

### System Tools Referenced

-   **LibreOffice (soffice)** — [DOCX/PPTX/XLSX conversion and formula recalculation](https://www.libreoffice.org/download/download-libreoffice/)

-   **pandoc** — [Universal document converter (DOCX text extraction)](https://pandoc.org/installing.html)
-   **Poppler (pdftoppm)** — [PDF-to-image rendering](https://poppler.freedesktop.org/)

-   **Tesseract OCR** — [Optical character recognition for scanned PDFs](https://github.com/tesseract-ocr/tesseract)

### *Related*

[![Comic-style illustration of a Power Platform developer using AI-assisted coding, showing human and AI collaboration in enterprise software development](https://i0.wp.com/aidevme.com/wp-content/uploads/2026/01/welcome-to-aidevme-feature.png?fit=1200%2C800&ssl=1&resize=350%2C200)](https://aidevme.com/welcome-to-ai-dev-me-power-platform-development-with-ai-tools/ "Welcome to AI Dev Me: Power Platform Development with AI Tools")

#### [Welcome to AI Dev Me: Power Platform Development with AI Tools](https://aidevme.com/welcome-to-ai-dev-me-power-platform-development-with-ai-tools/ "Welcome to AI Dev Me: Power Platform Development with AI Tools")

Where Microsoft Technology Meets Intelligent Coding I’m Zsolt Zombik, a senior Power Platform developer at ELCA Informatik AG, working at the intersection of Microsoft Power Platform and AI-assisted software development. This blog is not about shortcuts, hype, or “10x developer” promises. It is about building real, enterprise-grade Power Platform solutions—applications…

January 5, 2026

In "AI in Development"

---
> **Note:** This page contains 4 cross-origin iframe(s) that could not be accessed due to browser security policies. Some content may be missing. Links to these iframes have been preserved where possible.


---
Source: [Claude Skills: The Complete Developer Guide to Building Reusable AI Workflows (With Code)](https://aidevme.com/claude-skills-complete-developer-guide/)