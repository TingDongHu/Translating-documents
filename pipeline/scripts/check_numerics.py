import argparse
import json
import re
from pathlib import Path

TOKEN_RE = re.compile(
    r'GB/T\d+-\d+|ISO\s?\d+:\d+|IS0\d+:\d+|Q\d+[A-Z]?|E\d+[A-Z]?|'
    r'\d{4}/\d{2}/\d{2}|\d{2}/\d{2}/\d{4}|\d+\*\d+(?:\*\d+)?|'
    r'\d+(?:[.,]\d+)?a|\d+(?:[.,]\d+)?'
)
TAG_RE = re.compile(r'^\[([^\]]+)\]\s?(.*)$')


def load_tagged(path):
    data = {}
    with open(path, encoding='utf-8') as handle:
        for line in handle:
            match = TAG_RE.match(line.rstrip('\n'))
            if match:
                data[match.group(1)] = match.group(2)
    return data


def norm_date(token):
    if re.fullmatch(r'\d{4}/\d{2}/\d{2}', token):
        year, month, day = token.split('/')
        return f'{day}/{month}/{year}'
    return token


def norm_token(token):
    value = norm_date(token.strip())
    value = value.replace('IS0', 'ISO').replace('ISO ', 'ISO')
    if re.fullmatch(r'\d+[.,]\d+', value):
        value = value.replace(',', '.')
    if re.fullmatch(r'\d+[.,]\d+a', value):
        value = value.replace(',', '.')
    return value


def multiset(tokens):
    result = {}
    for token in tokens:
        result[token] = result.get(token, 0) + 1
    return result


def compare(source, translation):
    rows = []
    for tag in sorted(source, key=lambda item: (item[0], int(re.search(r'\d+', item).group()) if re.search(r'\d+', item) else -1)):
        source_tokens = [norm_token(token) for token in TOKEN_RE.findall(source.get(tag, ''))]
        translation_tokens = [norm_token(token) for token in TOKEN_RE.findall(translation.get(tag, ''))]
        source_counts = multiset(source_tokens)
        translation_counts = multiset(translation_tokens)
        missing = []
        extra = []
        for token, count in source_counts.items():
            if translation_counts.get(token, 0) < count:
                missing.extend([token] * (count - translation_counts.get(token, 0)))
        for token, count in translation_counts.items():
            if source_counts.get(token, 0) < count:
                extra.extend([token] * (count - source_counts.get(token, 0)))
        if missing or extra:
            rows.append({
                'tag': tag,
                'source_text': source.get(tag, ''),
                'translation_text': translation.get(tag, ''),
                'source_tokens': source_tokens,
                'translation_tokens': translation_tokens,
                'missing_or_changed': missing,
                'extra': extra,
            })
    return rows


def write_markdown(rows, path):
    with open(path, 'w', encoding='utf-8') as handle:
        handle.write('# Numerical Zero-Tolerance Check\n\n')
        handle.write('| Location | Source Text | Translation Text | Source Numeric Tokens | Translation Numeric Tokens | Missing/Changed | Extra |\n')
        handle.write('|---|---|---|---|---|---|---|\n')
        for row in rows:
            handle.write(
                f"| {row['tag']} | {row['source_text']} | {row['translation_text']} | "
                f"{', '.join(row['source_tokens'])} | {', '.join(row['translation_tokens'])} | "
                f"{', '.join(row['missing_or_changed'])} | {', '.join(row['extra'])} |\n"
            )
        handle.write(f'\nTotal flagged rows: {len(rows)}\n')


def main():
    parser = argparse.ArgumentParser(description='Run numerical zero-tolerance check on tagged translation files.')
    parser.add_argument('--source', required=True)
    parser.add_argument('--translation', required=True)
    parser.add_argument('--markdown-output', required=True)
    parser.add_argument('--json-output', required=True)
    args = parser.parse_args()

    rows = compare(load_tagged(args.source), load_tagged(args.translation))
    Path(args.markdown_output).parent.mkdir(parents=True, exist_ok=True)
    write_markdown(rows, args.markdown_output)
    score = {
        'passed': len(rows) == 0,
        'flagged_rows': len(rows),
        'critical_count': len(rows),
        'report_path': args.markdown_output,
    }
    Path(args.json_output).write_text(json.dumps(score, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f"Numerical check flagged {len(rows)} rows")


if __name__ == '__main__':
    main()
