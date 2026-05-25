#!/usr/bin/env python3
"""Render translated text back into a plain text document."""

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


def build_block_lookup(paragraphs):
    """Build {block: {tag, original}} lookup from extraction."""
    lookup = {}
    for p in paragraphs:
        lookup[p['location']['block']] = {'tag': p['tag'], 'original': p['text']}
    return lookup


def split_into_paragraphs(lines):
    """Split source lines into paragraph blocks.

    Returns list of (start_line, end_line_exclusive, line_count)
    and set of blank line indices.
    """
    blocks = []
    blanks = set()
    current_start = None
    current_count = 0

    for i, raw_line in enumerate(lines):
        if raw_line.strip():
            if current_start is None:
                current_start = i
            current_count += 1
        else:
            if current_start is not None:
                blocks.append((current_start, i, current_count))
                current_start = None
                current_count = 0
            blanks.add(i)

    if current_start is not None:
        blocks.append((current_start, len(lines), current_count))

    return blocks, blanks


def main():
    parser = argparse.ArgumentParser(
        description='Render translated text into a plain text document.'
    )
    parser.add_argument('--template', required=True)
    parser.add_argument('--extraction', required=True)
    parser.add_argument('--translation', required=True)
    parser.add_argument('--output', required=True)
    parser.add_argument('--render-log', required=True)
    args = parser.parse_args()

    translations = load_translations(args.translation)
    extraction = json.loads(Path(args.extraction).read_text(encoding='utf-8'))
    paragraphs = extraction.get('paragraphs', [])
    block_lookup = build_block_lookup(paragraphs)

    source_text = Path(args.template).read_text(encoding='utf-8')
    lines = source_text.splitlines(keepends=True)
    para_blocks, blank_indices = split_into_paragraphs(lines)

    line_map = {}
    for start, end, line_count in para_blocks:
        entry = block_lookup.get(start)
        if entry and entry['tag'] in translations:
            translated = translations[entry['tag']]
            t_lines = translated.split('\n')
            for j, tl in enumerate(t_lines):
                line_map[start + j] = tl + '\n'
            for j in range(len(t_lines), line_count):
                line_map[start + j] = '\n'
        else:
            for j in range(start, end):
                line_map[j] = lines[j]

    for idx in blank_indices:
        line_map[idx] = '\n'

    output_text = ''.join(line_map.get(i, lines[i]) for i in range(len(lines)))

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(output_text, encoding='utf-8')

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
