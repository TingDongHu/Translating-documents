import argparse
import json
import sys
from pathlib import Path

CANONICAL_STAGES = [
    'initialized', 'extraction', 'prepare_knowledge', 'knowledge_generation',
    'adaptation_research',
    'translation', 'professional_term_research',
    'merge_marker_check', 'numerical_check',
    'inspection_round1', 'revision_round1', 'inspection_round2', 'revision_round2',
    'render', 'final_audit',
    'completed',
]

STAGE_HISTORY_STATUSES = {'pending', 'in_progress', 'completed', 'skipped', 'failed'}

SCHEMA_DIR = Path(__file__).resolve().parent.parent / 'templates'
DEFAULT_SCHEMA = str(SCHEMA_DIR / 'workflow_state.schema.json')


def validate_required(state, schema):
    errors = []
    required = schema.get('required', [])
    for field in required:
        if field not in state:
            errors.append(f"Missing required field: {field}")
    return errors


def validate_types(state, schema_properties):
    errors = []
    type_map = {
        'string': str,
        'boolean': bool,
        'integer': int,
        'array': list,
        'object': dict,
    }
    for field, props in schema_properties.items():
        if field not in state:
            continue
        raw_type = props.get('type')
        if not raw_type:
            continue
        type_names = [raw_type] if isinstance(raw_type, str) else raw_type
        expected_types = [t for t in (type_map.get(n) for n in type_names) if t is not None]
        if not expected_types:
            continue
        if not any(isinstance(state[field], t) for t in expected_types):
            errors.append(f"Field '{field}': expected {raw_type}, got {type(state[field]).__name__}")
    return errors


def validate_current_stage(state):
    errors = []
    stage = state.get('current_stage')
    if stage and stage not in CANONICAL_STAGES:
        errors.append(f"Invalid current_stage: '{stage}'. Must be one of: {', '.join(CANONICAL_STAGES)}")
    return errors


def validate_stage_history(state):
    errors = []
    history = state.get('stage_history', [])
    if not isinstance(history, list):
        errors.append("stage_history must be an array")
        return errors
    for i, entry in enumerate(history):
        if not isinstance(entry, dict):
            errors.append(f"stage_history[{i}]: expected object, got {type(entry).__name__}")
            continue
        if 'stage' not in entry:
            errors.append(f"stage_history[{i}]: missing 'stage' field")
        if 'status' not in entry:
            errors.append(f"stage_history[{i}]: missing 'status' field")
        elif entry['status'] not in STAGE_HISTORY_STATUSES:
            errors.append(f"stage_history[{i}].status: '{entry['status']}' not in {sorted(STAGE_HISTORY_STATUSES)}")
    return errors


def main():
    parser = argparse.ArgumentParser(description='Validate workflow_state.json against schema and canonical rules.')
    parser.add_argument('--state', required=True, help='Path to workflow_state.json')
    parser.add_argument('--schema', default=DEFAULT_SCHEMA, help='Path to workflow_state.schema.json')
    args = parser.parse_args()

    state_path = Path(args.state)
    schema_path = Path(args.schema)

    if not state_path.exists():
        print(f"Error: state file not found: {state_path}")
        raise SystemExit(1)
    if not schema_path.exists():
        print(f"Error: schema file not found: {schema_path}")
        raise SystemExit(1)

    state = json.loads(state_path.read_text(encoding='utf-8'))
    schema = json.loads(schema_path.read_text(encoding='utf-8'))

    all_errors = []
    all_errors.extend(validate_required(state, schema))
    all_errors.extend(validate_types(state, schema.get('properties', {})))
    all_errors.extend(validate_current_stage(state))
    all_errors.extend(validate_stage_history(state))

    if all_errors:
        print(f"Validation FAILED — {len(all_errors)} error(s):")
        for err in all_errors:
            print(f"  - {err}")
        raise SystemExit(1)
    else:
        print("Workflow state validation passed.")


if __name__ == '__main__':
    main()
