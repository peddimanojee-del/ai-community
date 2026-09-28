from __future__ import annotations

from textwrap import indent

from .models import PageScript


def compile_prompt(page: PageScript, style: dict) -> str:
    ink = style["ink"]
    handwriting = style["handwriting"]
    total_pages = style["book"]["page_count"]
    guardrails = "\n".join(f"- {rule}" for rule in style["generation_guardrails"])
    panels = []
    for index, panel in enumerate(page.panels, 1):
        text = "\n".join(f"- {line}" for line in panel.copy)
        visual = f"\nVisual instruction: {panel.visual}" if panel.visual else ""
        panels.append(f"PANEL {index} — {panel.heading}\n{text}{visual}")

    code = "\n\n".join(page.code) if page.code else "No separate code box."
    important = "\n".join(f"• {item}" for item in page.important)
    summary = "\n".join(f"✓ {item}" for item in page.summary)
    checks = "\n".join(f"? {item}" for item in page.interview_checks)

    return f"""Create ONE finished handwritten educational notes page, page {page.page:02d} of {total_pages}.

HARD OUTPUT RULES
- A4 portrait, 210:297, high resolution, full page visible, no crop, no desk or hand in frame.
- Warm off-white real paper. Exceptionally neat HUMAN HANDWRITING—not a typeset infographic.
- This page is for a complete beginner. Use the supplied easy wording; never replace it with advanced jargon.
- All supplied wording and code must be spelled exactly and remain readable. Do not invent paragraphs.
- Main body ink: {ink['body']}. Main title: {ink['primary_heading']}.
- Secondary headings: {ink['secondary_heading']}. Borders: {ink['rules_and_borders']}.
- Writing character: {handwriting['character']}; compact but readable.
- Thin hand-drawn boxes, straight ruled tables, green arrows/check marks, purple underlines.
- Keep 4% safe margins. Put small page number “{page.page:02d} / {total_pages}” at bottom center.
- Avoid: {', '.join(handwriting['prohibited'])}.

KNOWN IMAGE-MODEL FAILURE GUARDRAILS — CHECK EVERY RULE BEFORE RENDERING
{guardrails}

MODULE: {page.module}
TITLE (large uppercase, centered, double-underlined): {page.title}
EASY DEFINITION (place directly below the title): {page.objective}
LAYOUT BLUEPRINT: {page.layout}

EXACT PAGE CONTENT
{indent(chr(10).join(panels), '  ')}

CODE BOXES (copy exactly, preserve punctuation)
{indent(code, '  ')}

FLOWCHART / DIAGRAM
{page.flowchart or 'Use only the panel-specific visual instructions.'}

IMPORTANT POINTS (lower-left, purple-underlined heading)
{important}

CHECK YOUR UNDERSTANDING (small bordered box)
{checks}

SUMMARY (lower-right cloud outline)
{summary}

FINAL PRE-RENDER AUDIT
1. Confirm canvas width is smaller than height and the whole A4 sheet is visible.
2. Compare every heading and bullet with the supplied content: no omission, duplication, fragment, or invented line.
3. Read code character-by-character: case, braces, line breaks, punctuation, and statement scope must match.
4. Confirm no instruction words leaked onto the page and body text remains sentence case.
5. Confirm version facts cannot visually attach to the wrong feature.
6. Confirm footer is exactly “{page.page:02d} / {total_pages}” and “Java Backend • Easy Notes”, with nothing else.
Only render after all six checks pass. The page should look like the supplied reference sheet with modern, technically correct content.
"""
