import argparse
import json
import re
from pathlib import Path

TAG_RE = re.compile(r'^\[([^\]]+)\]')


def read_tags(path):
    tags = []
    empty_tags = []
    with open(path, encoding='utf-8') as handle:
        for line_no, line in enumerate(handle, 1):
            match = TAG_RE.match(line.rstrip('\n'))
            if not match:
                continue
            tag = match.group(1)
            tags.append(tag)
            text = line.rstrip('\n')[match.end():].strip()
            if not text:
                empty_tags.append(tag)
    return tags, empty_tags


def duplicates(tags):
    seen = set()
    dupes = []
    for tag in tags:
        if tag in seen and tag not in dupes:
            dupes.append(tag)
        seen.add(tag)
    return dupes


def main():
    parser = argparse.ArgumentParser(description='Check tagged translation marker integrity.')
    parser.add_argument('--source', required=True)
    parser.add_argument('--translation', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()

    source_tags, source_empty = read_tags(args.source)
    translation_tags, translation_empty = read_tags(args.translation)

    source_set = set(source_tags)
    translation_set = set(translation_tags)
    source_empty_set = set(source_empty)
    translation_empty_set = set(translation_empty)
    content_dropped = sorted(translation_empty_set - source_empty_set)
    result = {
        'passed': source_set == translation_set and not duplicates(source_tags) and not duplicates(translation_tags) and not content_dropped,
        'source_tag_count': len(source_tags),
        'translation_tag_count': len(translation_tags),
        'missing_tags': sorted(source_set - translation_set),
        'extra_tags': sorted(translation_set - source_set),
        'duplicate_source_tags': duplicates(source_tags),
        'duplicate_translation_tags': duplicates(translation_tags),
        'empty_source_tags': source_empty,
        'empty_translation_tags': translation_empty,
        'content_dropped_tags': content_dropped,
    }

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f"Marker check passed: {result['passed']}")


if __name__ == '__main__':
    main()
