#!/usr/bin/env python3
"""Render translated text back into an XLSX spreadsheet.

Reads an extraction.json, translated_merged.txt, and the original .xlsx,
then writes a translated copy with cell text replaced. Formula cells
are preserved (not overwritten).
"""

import argparse
import json
import re
from pathlib import Path

TAG_RE = re.compile(r'^\[([^\]]+)\]\s?(.*)$')


def load_translations(path):
    data = {}
    with open(path, encoding='utf-8') as f:
        for line in f:
            m = TAG_RE.match(line.rstrip('\n'))
            if m:
                data[m.group(1)] = m.group(2)
    return data


def build_lookup(paragraphs):
    """Build {(sheet, row, col): tag} lookup."""
    lookup = {}
    for p in paragraphs:
        loc = p['location']
        lookup[(loc['sheet'], loc['row'], loc['col'])] = p['tag']
    return lookup


def main():
    parser = argparse.ArgumentParser(
        description='Render translated text into an XLSX spreadsheet.'
    )
    parser.add_argument('--template', required=True)
    parser.add_argument('--extraction', required=True)
    parser.add_argument('--translation', required=True)
    parser.add_argument('--output', required=True)
    parser.add_argument('--render-log', required=True)
    args = parser.parse_args()

    import openpyxl

    translations = load_translations(args.translation)
    extraction = json.loads(Path(args.extraction).read_text(encoding='utf-8'))
    paragraphs = extraction.get('paragraphs', [])
    loc_lookup = build_lookup(paragraphs)

    wb = openpyxl.load_workbook(args.template)

    for entry in paragraphs:
        tag = entry['tag']
        if tag not in translations:
            continue
        loc = entry['location']
        sheet_idx = loc['sheet']
        row = loc['row']
        col = loc['col']

        ws = wb.worksheets[sheet_idx]
        cell = ws.cell(row=row + 1, column=col + 1)

        if isinstance(cell.value, str) and cell.value.startswith('='):
            continue

        cell.value = translations[tag]

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    wb.save(str(output_path))
    wb.close()

    applied = sum(1 for p in paragraphs if p['tag'] in translations)
    missing = [p['tag'] for p in paragraphs if p['tag'] not in translations]
    report = {
        'logical_tags_applied': applied,
        'missing': missing,
        'output_path': str(output_path),
        'layout_warnings': [],
    }
    log_path = Path(args.render_log)
    log_path.parent.mkdir(parents=True, exist_ok=True)
    log_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f"Applied {applied} logical tags; missing {len(missing)}")


if __name__ == '__main__':
    main()
