#!/usr/bin/env python3
"""Converte MANUAL_MARKDOWN.md em um PDF estilizado."""

import markdown
from weasyprint import HTML

SRC = "MANUAL_MARKDOWN.md"
OUT = "MANUAL_MARKDOWN.pdf"

CSS = """
@page {
    size: A4;
    margin: 2cm 2.2cm;
    @bottom-center {
        content: "Página " counter(page) " de " counter(pages);
        font-size: 9px;
        color: #888;
    }
}
body {
    font-family: "DejaVu Sans", "Helvetica", sans-serif;
    font-size: 11px;
    line-height: 1.55;
    color: #24292e;
}
h1, h2, h3, h4, h5, h6 { color: #1a1a1a; line-height: 1.25; margin-top: 1.2em; }
h1 { font-size: 26px; border-bottom: 2px solid #e1e4e8; padding-bottom: .2em; }
h2 { font-size: 20px; border-bottom: 1px solid #e1e4e8; padding-bottom: .2em; }
h3 { font-size: 16px; }
h4 { font-size: 14px; }
a { color: #0366d6; text-decoration: none; }
code {
    font-family: "DejaVu Sans Mono", monospace;
    background: #f3f4f6;
    padding: .15em .35em;
    border-radius: 4px;
    font-size: 9.5px;
    color: #d6336c;
}
pre {
    background: #f6f8fa;
    border: 1px solid #e1e4e8;
    border-radius: 6px;
    padding: 12px;
    overflow-x: auto;
    page-break-inside: avoid;
}
pre code { background: none; color: #24292e; padding: 0; }
blockquote {
    border-left: 4px solid #dfe2e5;
    margin: .8em 0;
    padding: .2em 1em;
    color: #6a737d;
    background: #fafbfc;
}
table { border-collapse: collapse; width: 100%; margin: 1em 0; }
th, td { border: 1px solid #dfe2e5; padding: 6px 12px; }
th { background: #f6f8fa; }
tr:nth-child(even) { background: #fafbfc; }
hr { border: none; border-top: 1px solid #e1e4e8; margin: 1.5em 0; }
img { max-width: 100%; }
ul, ol { padding-left: 1.6em; }
"""

with open(SRC, encoding="utf-8") as f:
    text = f.read()

html_body = markdown.markdown(
    text,
    extensions=["fenced_code", "tables", "footnotes", "toc", "md_in_html"],
)

html_doc = f"""<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="utf-8">
<style>{CSS}</style></head>
<body>{html_body}</body></html>"""

HTML(string=html_doc).write_pdf(OUT)
print(f"PDF gerado: {OUT}")
