import argparse
import json
from pathlib import Path


def load(path):
    with open(path, encoding='utf-8') as handle:
        return json.load(handle)


def generate_report(marker, numerical, scorecard, render, revision_rounds, output_path):
    lines = ['# Final Translation Report\n']
    lines.append(f'- Marker check: {"passed" if marker.get("passed") else "failed"}')
    lines.append(f'- Numerical check: {"passed" if numerical.get("passed") else "failed"}')
    lines.append(f'- Critical issues remaining: {scorecard.get("critical_count", 0)}')
    lines.append(f'- Revision rounds: {revision_rounds}')
    if render.get("layout_warnings"):
        lines.append(f'- Layout warnings: {len(render["layout_warnings"])}')
    lines.append('')
    Path(output_path).write_text('\n'.join(lines), encoding='utf-8')


def main():
    parser = argparse.ArgumentParser(description='Validate final translation pipeline gates.')
    parser.add_argument('--marker-check', required=True)
    parser.add_argument('--numerical-score', required=True)
    parser.add_argument('--scorecard', required=True)
    parser.add_argument('--render-log', required=True)
    parser.add_argument('--final-report', required=True)
    parser.add_argument('--output', required=True)
    parser.add_argument('--revision-rounds', type=int, required=True)
    args = parser.parse_args()

    marker = load(args.marker_check)
    numerical = load(args.numerical_score)
    scorecard = load(args.scorecard)
    render = load(args.render_log)

    if not Path(args.final_report).exists():
        generate_report(marker, numerical, scorecard, render, args.revision_rounds, args.final_report)

    final_report_exists = Path(args.final_report).exists()
    final_docx = render.get('output_docx', '')
    final_docx_exists = bool(final_docx) and Path(final_docx).exists()
    layout_warnings = render.get('layout_warnings', [])
    critical_remaining = scorecard.get('critical_count', 0)

    passed = (
        marker.get('passed') is True and
        numerical.get('passed') is True and
        critical_remaining == 0 and
        final_report_exists and
        final_docx_exists
    )

    manifest = {
        'status': 'completed' if passed else 'blocked',
        'final_docx': final_docx,
        'final_report': args.final_report,
        'revision_rounds': args.revision_rounds,
        'critical_issues_remaining': critical_remaining,
        'numerical_check_passed': numerical.get('passed') is True,
        'marker_check_passed': marker.get('passed') is True,
        'render_check_passed': final_docx_exists,
        'layout_warnings': layout_warnings,
    }

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    Path(args.output).write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f"Final audit status: {manifest['status']}")
    if not passed:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
