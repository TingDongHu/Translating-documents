#!/usr/bin/env python3
"""extract_txt.py — Plain text extractor for translation pipelines.

Splits text into paragraphs by blank lines. Each non-empty paragraph
gets a [Pnnn] tag with its starting line number as location block.
"""

import argparse
import json
import os


def parse_args():
    parser = argparse.ArgumentParser(
        description="Extract translatable paragraphs from a text file."
    )
    parser.add_argument("--source", required=True)
    parser.add_argument("--extraction-output", required=True)
    parser.add_argument("--tagged-output", required=True)
    parser.add_argument("--report-output", required=True)
    return parser.parse_args()


def extract_from_txt(source_path):
    """Extract paragraphs from a text file.

    Returns (paragraphs, warnings).
    Each paragraph spans consecutive non-blank lines.
    Location.block = 0-based line number of the paragraph's first line.
    """
    paragraphs = []
    warnings = []

    with open(source_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    current_lines = []
    para_start = 0

    for i, raw_line in enumerate(lines):
        line = raw_line.rstrip("\r\n")
        if line.strip():
            if not current_lines:
                para_start = i
            current_lines.append(line)
        else:
            if current_lines:
                text = "\n".join(current_lines)
                paragraphs.append({
                    "tag": f"P{len(paragraphs)}",
                    "type": "paragraph",
                    "text": text,
                    "location": {"block": para_start},
                })
                current_lines = []

    if current_lines:
        text = "\n".join(current_lines)
        paragraphs.append({
            "tag": f"P{len(paragraphs)}",
            "type": "paragraph",
            "text": text,
            "location": {"block": para_start},
        })

    return paragraphs, warnings


def ensure_parent_dir(filepath):
    parent = os.path.dirname(filepath)
    if parent:
        os.makedirs(parent, exist_ok=True)


def main():
    args = parse_args()
    paragraphs, warnings = extract_from_txt(args.source)

    ensure_parent_dir(args.extraction_output)
    extraction = {"source": os.path.abspath(args.source), "paragraphs": paragraphs}
    with open(args.extraction_output, "w", encoding="utf-8") as f:
        json.dump(extraction, f, ensure_ascii=False, indent=2)

    ensure_parent_dir(args.tagged_output)
    with open(args.tagged_output, "w", encoding="utf-8") as f:
        for p in paragraphs:
            f.write(f"[{p['tag']}] {p['text']}\n")

    ensure_parent_dir(args.report_output)
    report = {
        "paragraph_count": len(paragraphs),
        "body_count": len(paragraphs),
        "warnings": warnings,
    }
    with open(args.report_output, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    print(f"Extraction complete: {report['paragraph_count']} paragraphs.")


if __name__ == "__main__":
    main()
