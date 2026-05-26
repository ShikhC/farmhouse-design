#!/usr/bin/env python3
"""
Generate a combined Hindi PDF from all farmhouse design documents.
Uses Chrome headless for HTML-to-PDF conversion with proper Devanagari support.
"""

import os
import re
import subprocess
from pathlib import Path

HINDI_DIR = Path("/Users/schowdhary/codebases/farmhouse_design/Farmhouse-Hindi")
OUTPUT_PDF = HINDI_DIR / "farmhouse-design-complete.pdf"
PRINT_HTML = HINDI_DIR / "farmhouse-design-print.html"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

def read_markdown(filepath):
    """Read markdown file and convert to basic HTML."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Convert markdown to HTML (basic conversion)
    lines = content.split('\n')
    html_lines = []
    in_code_block = False
    in_table = False
    table_header_done = False

    for line in lines:
        # Code blocks
        if line.strip().startswith('```'):
            if in_code_block:
                html_lines.append('</pre>')
                in_code_block = False
            else:
                html_lines.append('<pre class="code-block">')
                in_code_block = True
            continue

        if in_code_block:
            html_lines.append(line.replace('<', '&lt;').replace('>', '&gt;'))
            continue

        # Tables
        if '|' in line and line.strip().startswith('|'):
            cells = [c.strip() for c in line.split('|')[1:-1]]
            if all(set(c) <= set('- :') for c in cells):
                # Separator row - skip
                table_header_done = True
                continue
            if not in_table:
                html_lines.append('<table>')
                in_table = True
                table_header_done = False
            if not table_header_done:
                html_lines.append('<tr>' + ''.join(f'<th>{c}</th>' for c in cells) + '</tr>')
            else:
                html_lines.append('<tr>' + ''.join(f'<td>{c}</td>' for c in cells) + '</tr>')
            continue
        else:
            if in_table:
                html_lines.append('</table>')
                in_table = False
                table_header_done = False

        # Headers
        if line.startswith('# '):
            html_lines.append(f'<h1>{line[2:]}</h1>')
        elif line.startswith('## '):
            html_lines.append(f'<h2>{line[3:]}</h2>')
        elif line.startswith('### '):
            html_lines.append(f'<h3>{line[4:]}</h3>')
        elif line.startswith('#### '):
            html_lines.append(f'<h4>{line[5:]}</h4>')
        elif line.startswith('---'):
            html_lines.append('<hr>')
        elif line.startswith('> '):
            html_lines.append(f'<blockquote>{line[2:]}</blockquote>')
        elif line.startswith('- [ ] '):
            html_lines.append(f'<p class="checklist">☐ {line[6:]}</p>')
        elif line.startswith('- [x] '):
            html_lines.append(f'<p class="checklist">☑ {line[6:]}</p>')
        elif line.startswith('- ') or line.startswith('* '):
            html_lines.append(f'<p class="list-item">• {line[2:]}</p>')
        elif line.strip().startswith(('1.', '2.', '3.', '4.', '5.', '6.', '7.', '8.', '9.')):
            html_lines.append(f'<p class="numbered">{line.strip()}</p>')
        elif line.strip() == '':
            html_lines.append('<br>')
        else:
            # Bold
            line = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', line)
            # Inline code
            line = re.sub(r'`(.+?)`', r'<code>\1</code>', line)
            html_lines.append(f'<p>{line}</p>')

    if in_table:
        html_lines.append('</table>')
    if in_code_block:
        html_lines.append('</pre>')

    return '\n'.join(html_lines)


def extract_svgs_from_visualization():
    """Extract key SVG diagrams from the visualization HTML."""
    viz_path = HINDI_DIR / "visualization.html"
    with open(viz_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract SVGs between view divs
    svgs = {}
    view_names = ['ground', 'first', 'elevation', 'section', 'structure', 'electrical', 'plumbing', 'construction']

    for name in view_names:
        pattern = f'id="view-{name}".*?(<svg.*?</svg>)'
        match = re.search(pattern, content, re.DOTALL)
        if match:
            svg = match.group(1)
            # Only take the first SVG in each view (plan view)
            svgs[name] = svg

    return svgs


def build_combined_html():
    """Build the combined HTML document."""

    # Read all markdown files
    design_spec = read_markdown(HINDI_DIR / "design-spec.md")
    contractor_brief = read_markdown(HINDI_DIR / "contractor-brief.md")
    bill_of_quantities = read_markdown(HINDI_DIR / "bill-of-quantities.md")
    electrical_plumbing = read_markdown(HINDI_DIR / "electrical-plumbing.md")

    # Extract SVGs
    svgs = extract_svgs_from_visualization()

    html = f"""<!DOCTYPE html>
<html lang="hi">
<head>
<meta charset="UTF-8">
<style>
@page {{
    size: A4;
    margin: 1.5cm;
}}

body {{
    font-family: 'Noto Sans Devanagari', 'Devanagari MT', 'Kohinoor Devanagari', system-ui, sans-serif;
    font-size: 10pt;
    line-height: 1.5;
    color: #222;
}}

h1 {{
    font-size: 18pt;
    color: #c0392b;
    border-bottom: 2px solid #c0392b;
    padding-bottom: 5px;
    page-break-after: avoid;
    margin-top: 20px;
}}

h2 {{
    font-size: 14pt;
    color: #2c3e50;
    border-bottom: 1px solid #bdc3c7;
    padding-bottom: 3px;
    page-break-after: avoid;
    margin-top: 15px;
}}

h3 {{
    font-size: 12pt;
    color: #34495e;
    page-break-after: avoid;
    margin-top: 12px;
}}

h4 {{
    font-size: 11pt;
    color: #555;
    page-break-after: avoid;
}}

table {{
    width: 100%;
    border-collapse: collapse;
    margin: 8px 0;
    font-size: 9pt;
    page-break-inside: avoid;
}}

th, td {{
    border: 1px solid #bdc3c7;
    padding: 4px 6px;
    text-align: left;
}}

th {{
    background: #ecf0f1;
    font-weight: bold;
}}

tr:nth-child(even) {{
    background: #f9f9f9;
}}

pre.code-block {{
    background: #f4f4f4;
    border: 1px solid #ddd;
    padding: 8px;
    font-family: 'Courier New', monospace;
    font-size: 7.5pt;
    line-height: 1.3;
    overflow-wrap: break-word;
    white-space: pre-wrap;
    page-break-inside: avoid;
}}

code {{
    background: #f0f0f0;
    padding: 1px 4px;
    border-radius: 3px;
    font-size: 9pt;
}}

blockquote {{
    border-left: 3px solid #e74c3c;
    padding-left: 10px;
    margin: 8px 0;
    color: #c0392b;
    font-weight: bold;
}}

.checklist {{
    margin: 2px 0;
    padding-left: 15px;
}}

.list-item {{
    margin: 2px 0;
    padding-left: 10px;
}}

.numbered {{
    margin: 3px 0;
    padding-left: 10px;
}}

hr {{
    border: none;
    border-top: 1px solid #ccc;
    margin: 15px 0;
}}

.page-break {{
    page-break-before: always;
}}

.cover-page {{
    text-align: center;
    padding-top: 150px;
}}

.cover-page h1 {{
    font-size: 28pt;
    border: none;
    color: #2c3e50;
}}

.cover-page h2 {{
    font-size: 16pt;
    border: none;
    color: #7f8c8d;
    font-weight: normal;
}}

.toc {{
    page-break-after: always;
}}

.toc h2 {{
    text-align: center;
}}

.toc-item {{
    margin: 5px 0;
    font-size: 11pt;
}}

.svg-diagram {{
    text-align: center;
    margin: 15px 0;
    page-break-inside: avoid;
}}

.svg-diagram svg {{
    max-width: 100%;
    height: auto;
    border: 1px solid #ddd;
    background: white;
}}

.section-divider {{
    page-break-before: always;
    background: #2c3e50;
    color: white;
    padding: 20px;
    margin: 0 -1.5cm;
    text-align: center;
}}

.section-divider h1 {{
    color: white;
    border: none;
    font-size: 22pt;
}}

strong {{
    color: #c0392b;
}}
</style>
</head>
<body>

<!-- COVER PAGE -->
<div class="cover-page">
    <h1>खेत का गोदाम</h1>
    <h2>मिठनपुर उर्फ नईमतुल्ला नगर, मुरादाबाद, उत्तर प्रदेश</h2>
    <br><br>
    <p style="font-size: 14pt;">20 ft × 25 ft × 12 ft | 3 ft चबूतरा</p>
    <p style="font-size: 12pt; color: #888;">पूरा निर्माण विवरण — सिविल + बिजली + प्लंबिंग</p>
    <br><br><br>
    <p style="font-size: 10pt; color: #aaa;">तैयारी तिथि: मई 2026</p>
</div>

<!-- TABLE OF CONTENTS -->
<div class="page-break toc">
    <h2>विषय सूची</h2>
    <p class="toc-item"><strong>भाग 1:</strong> डिज़ाइन विवरण (नक्शे, काट, माप)</p>
    <p class="toc-item"><strong>भाग 2:</strong> ढांचा (पिलर, बीम, स्लैब)</p>
    <p class="toc-item"><strong>भाग 3:</strong> बिजली और प्लंबिंग</p>
    <p class="toc-item"><strong>भाग 4:</strong> सामान की सूची (मात्रा + अनुमानित खर्च)</p>
    <p class="toc-item"><strong>भाग 5:</strong> ठेकेदार के लिए निर्देश (चरण-दर-चरण)</p>
    <p class="toc-item"><strong>भाग 6:</strong> नक्शे / आरेख</p>
</div>

<!-- PART 1: DESIGN SPEC -->
<div class="section-divider">
    <h1>भाग 1: डिज़ाइन विवरण</h1>
</div>
{design_spec}

<!-- PART 2: ELECTRICAL + PLUMBING -->
<div class="page-break section-divider">
    <h1>भाग 2: बिजली और प्लंबिंग</h1>
</div>
{electrical_plumbing}

<!-- PART 3: BILL OF QUANTITIES -->
<div class="page-break section-divider">
    <h1>भाग 3: सामान की सूची</h1>
</div>
{bill_of_quantities}

<!-- PART 4: CONTRACTOR BRIEF -->
<div class="page-break section-divider">
    <h1>भाग 4: ठेकेदार के लिए निर्देश</h1>
</div>
{contractor_brief}

<!-- PART 5: DIAGRAMS -->
<div class="page-break section-divider">
    <h1>भाग 5: नक्शे / आरेख</h1>
</div>

<h2>भूतल नक्शा (Ground Floor Plan)</h2>
<div class="svg-diagram">
    {svgs.get('ground', '<p>SVG not available</p>')}
</div>

<div class="page-break"></div>
<h2>पहली मंजिल (First Floor Plan)</h2>
<div class="svg-diagram">
    {svgs.get('first', '<p>SVG not available</p>')}
</div>

<div class="page-break"></div>
<h2>सामने का दृश्य (Front Elevation)</h2>
<div class="svg-diagram">
    {svgs.get('elevation', '<p>SVG not available</p>')}
</div>

<div class="page-break"></div>
<h2>काट (Section)</h2>
<div class="svg-diagram">
    {svgs.get('section', '<p>SVG not available</p>')}
</div>

<div class="page-break"></div>
<h2>ढांचा — पिलर और बीम (Structure)</h2>
<div class="svg-diagram">
    {svgs.get('structure', '<p>SVG not available</p>')}
</div>

<div class="page-break"></div>
<h2>बिजली का नक्शा (Electrical Layout)</h2>
<div class="svg-diagram">
    {svgs.get('electrical', '<p>SVG not available</p>')}
</div>

<div class="page-break"></div>
<h2>प्लंबिंग का नक्शा (Plumbing Layout)</h2>
<div class="svg-diagram">
    {svgs.get('plumbing', '<p>SVG not available</p>')}
</div>

<div class="page-break"></div>
<h2>निर्माण के चरण (Construction Steps)</h2>
<div class="svg-diagram">
    {svgs.get('construction', '<p>SVG not available</p>')}
</div>

</body>
</html>"""

    return html


def main():
    print("📄 Building combined Hindi document...")
    html_content = build_combined_html()

    # Save print-ready HTML
    with open(PRINT_HTML, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"   HTML saved: {PRINT_HTML}")

    # Generate PDF using Chrome headless
    print("📑 Generating PDF with Chrome headless...")
    cmd = [
        CHROME,
        "--headless",
        "--disable-gpu",
        "--no-sandbox",
        f"--print-to-pdf={OUTPUT_PDF}",
        "--print-to-pdf-no-header",
        f"file://{PRINT_HTML}"
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)

    if result.returncode != 0 and not os.path.exists(OUTPUT_PDF):
        print(f"❌ Chrome failed: {result.stderr}")
        return

    file_size = os.path.getsize(OUTPUT_PDF) / (1024 * 1024)
    print(f"✅ PDF generated: {OUTPUT_PDF}")
    print(f"   Size: {file_size:.1f} MB")


if __name__ == "__main__":
    main()
