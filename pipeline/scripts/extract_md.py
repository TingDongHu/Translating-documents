#!/usr/bin/env python3
"""
extract_md.py — Markdown text extractor for translation pipelines.

Processes a .md file line-by-line with regex patterns, identifying paragraphs,
headings, list items, table cells, blockquotes, link text, and alt text.
Skips code blocks, inline code, YAML frontmatter, and math equations.
"""

import argparse
import json
import os
import re


def parse_args():
    parser = argparse.ArgumentParser(
        description="Extract translatable text from a Markdown file."
    )
    parser.add_argument("--source", required=True, help="Path to source .md file")
    parser.add_argument(
        "--extraction-output", required=True, help="Path for extraction.json"
    )
    parser.add_argument(
        "--tagged-output", required=True, help="Path for source_tagged.txt"
    )
    parser.add_argument(
        "--report-output", required=True, help="Path for extraction_report.json"
    )
    return parser.parse_args()


def strip_inline_formatting(text):
    """Strip inline formatting markers from extracted text.

    Removes:
      - **bold** or __bold__
      - *italic* or _italic_
      - `inline code`
      - [link text](url) -> link text
      - ![alt](url) -> alt
    """
    # Remove images first: ![alt](url) -> alt
    text = re.sub(r'!\[([^\]]*)\]\([^)]*\)', r'\1', text)
    # Remove links: [text](url) -> text
    text = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', text)
    # Remove inline code: `code`
    text = re.sub(r'`[^`]*`', '', text)
    # Remove bold markers: **bold**, __bold__
    text = re.sub(r'\*\*([^*]+)\*\*', r'\1', text)
    text = re.sub(r'__([^_]+)__', r'\1', text)
    # Remove italic markers: *italic*, _italic_
    # Use lookarounds to avoid matching bold markers
    text = re.sub(r'(?<!\*)\*(?!\*)([^*]+)(?<!\*)\*(?!\*)', r'\1', text)
    text = re.sub(r'(?<!_)_(?!_)([^_]+)(?<!_)_(?!_)', r'\1', text)
    return text


def extract_cell_text(cell):
    """Extract and strip formatting from a single table cell.

    Each cell is independently trimmed (outer whitespace removed),
    but internal whitespace is preserved.
    """
    cell = cell.strip()
    return strip_inline_formatting(cell)


def is_table_separator_row(stripped):
    """Check if a table row is a separator (e.g. |---|---|).

    Separator rows contain only dashes, colons, pipes, and spaces.
    """
    parts = stripped.split("|")
    for part in parts:
        stripped_part = part.strip()
        if stripped_part and not re.match(r"^:?-+:?$", stripped_part):
            return False
    return True


def extract_from_md(source_path):
    """Extract translatable content from a Markdown file.

    Returns a tuple: (paragraphs, warnings)
    """
    paragraphs = []
    warnings = []

    with open(source_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    in_yaml = False
    in_code_block = False
    in_math_block = False
    # For tracking fenced code block fence character and minimum length
    fence_char = ""
    fence_min_len = 0

    for line_index, raw_line in enumerate(lines):
        line = raw_line.rstrip("\r\n")

        # ---- State machine for skip regions ----

        # YAML frontmatter: starts with --- on the very first line
        if line_index == 0 and line.strip() == "---":
            in_yaml = True
            continue

        if in_yaml:
            if line.strip() == "---":
                in_yaml = False
            continue

        # Fenced code blocks (```...``` or ~~~...~~~)
        # Allow up to 3 spaces of indentation before the fence
        code_fence_match = re.match(r"^ {0,3}(`{3,}|~{3,})", line)
        if code_fence_match and not in_code_block:
            in_code_block = True
            fence = code_fence_match.group(1)
            fence_char = fence[0]
            fence_min_len = len(fence)
            continue

        if in_code_block:
            # Closing fence must have at least as many characters as opening
            close_match = re.match(
                r"^ {0,3}(" + re.escape(fence_char) + r"{3,})", line
            )
            if close_match and len(close_match.group(1)) >= fence_min_len:
                in_code_block = False
                fence_char = ""
                fence_min_len = 0
            continue

        # Math blocks: $$ ... $$
        if line.strip() == "$$":
            if not in_math_block:
                in_math_block = True
            else:
                in_math_block = False
            continue
        if in_math_block:
            continue

        # ---- Extractable content ----

        stripped = line.strip()
        if not stripped:
            continue

        # Horizontal rules: ---, ***, ___ (3 or more chars)
        if re.match(r"^[-*_]{3,}\s*$", stripped):
            continue

        # Indented code blocks: lines starting with 4 spaces or 1 tab
        # Exception: NOT inside tables (line starts with | after stripping)
        if re.match(r"^(?:    |\t)", line) and not line.lstrip().startswith("|"):
            continue

        # --- Priority matching (most specific first) ---

        # 1. Headings: # to ######
        heading_match = re.match(r"^(#{1,6})\s+(.+)$", stripped)
        if heading_match:
            text = strip_inline_formatting(heading_match.group(2))
            if text:
                paragraphs.append({
                    "tag": f"P{len(paragraphs)}",
                    "type": "heading",
                    "text": text,
                    "location": {"block": line_index}
                })
            continue

        # 2. Blockquotes: > text
        bq_match = re.match(r"^>\s*(.*)$", stripped)
        if bq_match:
            text = strip_inline_formatting(bq_match.group(1))
            if text:
                paragraphs.append({
                    "tag": f"P{len(paragraphs)}",
                    "type": "blockquote",
                    "text": text,
                    "location": {"block": line_index}
                })
            continue

        # 3. List items: -, *, +, or 1. (ordered)
        list_match = re.match(r"^([-*+]|\d+\.)\s+(.*)$", stripped)
        if list_match:
            text = strip_inline_formatting(list_match.group(2))
            if text:
                paragraphs.append({
                    "tag": f"P{len(paragraphs)}",
                    "type": "list_item",
                    "text": text,
                    "location": {"block": line_index}
                })
            continue

        # 4. Image alt text: ![alt](url) -- standalone line
        img_match = re.match(r"^!\[([^\]]*)\]\([^)]*\)\s*$", stripped)
        if img_match:
            alt_text = img_match.group(1).strip()
            if alt_text:
                paragraphs.append({
                    "tag": f"P{len(paragraphs)}",
                    "type": "alt_text",
                    "text": alt_text,
                    "location": {"block": line_index}
                })
            continue

        # 5. Table cells: | cell |
        if stripped.startswith("|") and stripped.endswith("|"):
            # Skip separator rows (|---|---|)
            if is_table_separator_row(stripped):
                continue
            cells = stripped.split("|")
            # cells[0] is empty (before first |), cells[-1] is empty (after last |)
            inner_cells = cells[1:-1]
            for col_idx, cell in enumerate(inner_cells):
                cell_text = extract_cell_text(cell)
                if cell_text:
                    paragraphs.append({
                        "tag": f"P{len(paragraphs)}",
                        "type": "table",
                        "text": cell_text,
                        "location": {"block": line_index, "col": col_idx}
                    })
            continue

        # 6. Default: paragraph
        text = strip_inline_formatting(stripped)
        if text:
            paragraphs.append({
                "tag": f"P{len(paragraphs)}",
                "type": "paragraph",
                "text": text,
                "location": {"block": line_index}
            })

    return paragraphs, warnings


def count_by_type(paragraphs):
    """Count paragraphs by type."""
    counts = {
        "paragraph_count": len(paragraphs),
        "body_count": 0,
        "heading_count": 0,
        "table_count": 0,
        "list_item_count": 0,
        "blockquote_count": 0,
        "alt_text_count": 0,
    }
    for p in paragraphs:
        ptype = p["type"]
        if ptype == "paragraph":
            counts["body_count"] += 1
        elif ptype == "heading":
            counts["heading_count"] += 1
        elif ptype == "table":
            counts["table_count"] += 1
        elif ptype == "list_item":
            counts["list_item_count"] += 1
        elif ptype == "blockquote":
            counts["blockquote_count"] += 1
        elif ptype == "alt_text":
            counts["alt_text_count"] += 1
    return counts


def ensure_parent_dir(filepath):
    """Create parent directories for the given file path if they don't exist."""
    parent = os.path.dirname(filepath)
    if parent:
        os.makedirs(parent, exist_ok=True)


def main():
    args = parse_args()

    paragraphs, warnings = extract_from_md(args.source)

    # Generate extraction.json
    ensure_parent_dir(args.extraction_output)
    extraction = {
        "source": os.path.abspath(args.source),
        "paragraphs": paragraphs,
    }
    with open(args.extraction_output, "w", encoding="utf-8") as f:
        json.dump(extraction, f, ensure_ascii=False, indent=2)

    # Generate source_tagged.txt
    ensure_parent_dir(args.tagged_output)
    with open(args.tagged_output, "w", encoding="utf-8") as f:
        for p in paragraphs:
            f.write(f"[{p['tag']}] {p['text']}\n")

    # Generate extraction_report.json
    ensure_parent_dir(args.report_output)
    counts = count_by_type(paragraphs)
    report = {
        **counts,
        "warnings": warnings,
    }
    with open(args.report_output, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    print(f"Extraction complete: {report['paragraph_count']} paragraphs found.")
    print(f"  Body: {report['body_count']}")
    print(f"  Headings: {report['heading_count']}")
    print(f"  Table cells: {report['table_count']}")
    print(f"  List items: {report['list_item_count']}")
    print(f"  Blockquotes: {report['blockquote_count']}")
    print(f"  Alt texts: {report['alt_text_count']}")


if __name__ == "__main__":
    main()
