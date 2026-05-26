import argparse
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description='Merge translated batches and remove context lines.')
    parser.add_argument('--manifest', required=True)
    parser.add_argument('--translated-dir', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()

    manifest = json.loads(Path(args.manifest).read_text(encoding='utf-8'))
    translated_dir = Path(args.translated_dir)
    merged = []
    missing_batches = []
    batch_details = []

    # Support both split-style manifests (with 'batches') and job-style manifests
    if 'batches' in manifest:
        batch_list = manifest['batches']
    else:
        # Scan translated directory for batch_{n:03d}_translated.txt files
        batch_files = sorted(translated_dir.glob('batch_*_translated.txt'))
        batch_list = []
        for bf in batch_files:
            # Extract batch number from filename
            try:
                batch_no = int(bf.stem.split('_')[1])
            except (IndexError, ValueError):
                continue
            batch_list.append({'batch': batch_no})

    for batch in batch_list:
        batch_no = batch['batch']
        translated_path = translated_dir / f'batch_{batch_no:03d}_translated.txt'
        if not translated_path.exists():
            missing_batches.append(batch_no)
            batch_details.append({'batch': batch_no, 'status': 'missing', 'path': str(translated_path)})
            continue
        lines = translated_path.read_text(encoding='utf-8').splitlines()
        non_context = [line for line in lines if not line.startswith('[CONTEXT]')]
        merged.extend(non_context)
        batch_details.append({'batch': batch_no, 'status': 'merged', 'lines': len(non_context)})

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text('\n'.join(merged) + ('\n' if merged else ''), encoding='utf-8')

    status = {
        'stage': 'merge_batches',
        'status': 'failed' if missing_batches else 'completed',
        'outputs': {'merged_translation': str(output)},
        'metrics': {'merged_lines': len(merged), 'missing_batches': missing_batches, 'total_batches': len(batch_list)},
        'batch_details': batch_details,
    }
    status_path = output.with_suffix('.status.json')
    status_path.write_text(json.dumps(status, ensure_ascii=False, indent=2), encoding='utf-8')
    if missing_batches:
        raise SystemExit(f"Missing translated batches: {', '.join(str(b) for b in missing_batches)}")
    print(f"Merged {len(merged)} lines")


if __name__ == '__main__':
    main()
