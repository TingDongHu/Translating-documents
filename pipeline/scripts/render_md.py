#!/usr/bin/env python3
"""Render translated text back into a Markdown document.

Reads an extraction.json (tag/location mapping), a translated_merged.txt
(tag -> translated text), and the original .md source, then rebuilds the
Markdown with translated text substituted at the correct line positions.

Structure markers (# heading, > blockquote, - list, | table |) are preserved
so the output remains valid Markdown. Inline formatting (**bold**, `code`)
from the original is lost during extraction and therefore not restored.

Usage:
    python pipeline/scripts/render_md.py \
      --template source.md \
      --extraction extraction/extraction.json \
      --translation translation/translated_merged.txt \
      --output translated.md \
      --render-log render_log.json
"""

import argparse
import json
import re
from pathlib import Path

TAG_RE = re.compile(r'^\[([^\]]+)\]\s?(.*)$')


def load_translations(path):
    """Load translation file into {tag: translated_text} dict."""
    data = {}
    with open(path, encoding='utf-8') as f:
        for line in f:
            m = TAG_RE.match(line.rstrip('\n'))
            if m:
                data[m.group(1)] = m.group(2)
    return data


def build_block_lookup(paragraphs):
    """Build {block_index: [entry, ...]} lookup from extraction paragraphs.

    Multiple entries can share a block (e.g. table cells in the same row).
    """
    lookup = {}
    for p in paragraphs:
        block = p['location']['block']
        if block not in lookup:
            lookup[block] = []
        lookup[block].append(p)
    return lookup


def render_line(raw_line, block_idx, block_entries, translations):
    """Render a single source line with translations applied.

    Args:
        raw_line: Original source line (may include trailing newline).
        block_idx: 0-based line index in the source file.
        block_entries: List of extraction entries for this block.
        translations: {tag: translated_text} dict.

    Returns:
        Translated line (with original trailing newline preserved).
    """
    has_newline = raw_line.endswith('\n')
    line = raw_line.rstrip('\r\n')

    # Separate table entries from non-table entries
    table_entries = [e for e in block_entries if e['type'] == 'table']
    non_table_entry = next((e for e in block_entries if e['type'] != 'table'), None)

    if table_entries:
        # Table row: replace individual cells
        cells = line.split('|')
        # cells[0] is empty (before first |), cells[-1] is empty (after last |)
        for entry in table_entries:
            col = entry['location'].get('col', 0)
            tag = entry['tag']
            inner_idx = col + 1
            if tag in translations and inner_idx < len(cells):
                cells[inner_idx] = translations[tag]
        result = '|'.join(cells)

    elif non_table_entry:
        tag = non_table_entry['tag']
        if tag not in translations:
            result = line
        else:
            translated = translations[tag]
            etype = non_table_entry['type']

            if etype == 'heading':
                # Preserve # prefix
                m = re.match(r'^(#+)', line)
                if m:
                    result = m.group(1) + ' ' + translated
                else:
                    result = translated

            elif etype == 'blockquote':
                # Preserve > prefix
                m = re.match(r'^(\s*>+\s*)', line)
                if m:
                    result = m.group(1) + translated
                else:
                    result = '> ' + translated

            elif etype == 'list_item':
                # Preserve indentation and list marker
                m = re.match(r'^(\s*)([-*+]|\d+\.)\s*', line)
                if m:
                    indent = m.group(1)
                    marker = m.group(2)
                    result = indent + marker + ' ' + translated
                else:
                    result = translated

            elif etype == 'paragraph':
                result = translated

            elif etype == 'alt_text':
                # Replace alt text within ![alt](url)
                result = re.sub(
                    r'(!\[)([^\]]*)(\]\([^)]*\))',
                    lambda m: m.group(1) + translated + m.group(3),
                    line,
                )

            else:
                result = translated
    else:
        result = line

    return result + '\n' if has_newline else result


def main():
    parser = argparse.ArgumentParser(
        description='Render translated text into a Markdown document.'
    )
    parser.add_argument('--template', required=True, help='Original .md source file')
    parser.add_argument('--extraction', required=True, help='extraction.json')
    parser.add_argument('--translation', required=True, help='translated_merged.txt')
    parser.add_argument('--output', required=True, help='Output translated .md file')
    parser.add_argument('--render-log', required=True, help='Path for render_log.json')
    args = parser.parse_args()

    # Load inputs
    translations = load_translations(args.translation)
    extraction = json.loads(Path(args.extraction).read_text(encoding='utf-8'))
    paragraphs = extraction.get('paragraphs', [])
    block_lookup = build_block_lookup(paragraphs)

    # Read original source
    source_text = Path(args.template).read_text(encoding='utf-8')
    original_lines = source_text.splitlines(keepends=True)

    # Render
    output_lines = []
    for block_idx, raw_line in enumerate(original_lines):
        if block_idx in block_lookup:
            rendered = render_line(
                raw_line, block_idx, block_lookup[block_idx], translations
            )
            output_lines.append(rendered)
        else:
            output_lines.append(raw_line)

    output_text = ''.join(output_lines)

    # Write output
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(output_text, encoding='utf-8')

    # Build render log
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
    log_path.write_text(
        json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8'
    )

    print(f"Applied {applied} logical tags; missing {len(missing)}")


if __name__ == '__main__':
    main()
