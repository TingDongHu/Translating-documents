import argparse
import json
from pathlib import Path


def read_lines(path):
    return Path(path).read_text(encoding='utf-8').splitlines()


def main():
    parser = argparse.ArgumentParser(description='Split tagged source into translation batches.')
    parser.add_argument('--source', required=True)
    parser.add_argument('--output-dir', required=True)
    parser.add_argument('--batch-size', type=int, default=0)
    parser.add_argument('--overlap', type=int, default=0)
    parser.add_argument('--manifest-output', required=True)
    args = parser.parse_args()

    lines = read_lines(args.source)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    if args.batch_size <= 0:
        args.batch_size = len(lines)
    if args.overlap > 0 and args.batch_size >= len(lines):
        args.overlap = 0

    batches = []
    start = 0
    batch_number = 1
    while start < len(lines):
        end = min(start + args.batch_size, len(lines))
        context_start = max(0, start - args.overlap) if start else start
        batch_lines = []
        if context_start < start:
            batch_lines.extend(f'[CONTEXT] {line}' for line in lines[context_start:start])
        batch_lines.extend(lines[start:end])
        batch_path = output_dir / f'batch_{batch_number:03d}_source.txt'
        batch_path.write_text('\n'.join(batch_lines) + '\n', encoding='utf-8')
        batches.append({
            'batch': batch_number,
            'path': str(batch_path),
            'source_start_line': start + 1,
            'source_end_line': end,
            'context_lines': start - context_start,
            'translatable_lines': end - start,
        })
        start = end
        batch_number += 1

    manifest = {
        'source': args.source,
        'batch_size': args.batch_size,
        'overlap': args.overlap,
        'total_lines': len(lines),
        'batches': batches,
    }
    Path(args.manifest_output).parent.mkdir(parents=True, exist_ok=True)
    Path(args.manifest_output).write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f"Created {len(batches)} batches")


if __name__ == '__main__':
    main()
