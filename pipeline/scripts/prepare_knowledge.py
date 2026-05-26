"""
prepare_knowledge.py — Replace knowledge_loader LLM worker.

Reads the skill knowledge directory and produces a knowledge_manifest.json
with file paths, frontmatter, section indexes, and filtered glossary entries.

Designed for direct Bash execution (<50ms). No LLM involved.
"""
import argparse
import json
import os
import re
from pathlib import Path


def parse_frontmatter(filepath):
    """Parse YAML-like frontmatter from an MD file. Returns (frontmatter_dict, body_line_start)."""
    path = Path(filepath)
    if not path.exists():
        return {}, 1
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}, 1

    lines = text.splitlines()
    end = 1
    while end < len(lines) and lines[end] != "---":
        end += 1
    if end >= len(lines):
        return {}, 1

    fm_lines = lines[1:end]
    fm = {}
    for line in fm_lines:
        m = re.match(r'^(\w[\w_]*)\s*:\s*(.*)', line)
        if m:
            key = m.group(1)
            val = m.group(2).strip()
            if val.startswith('"') and val.endswith('"'):
                val = val[1:-1]
            fm[key] = val
        elif line.startswith("  ") and "prev_key" in locals():
            # Handle indented list items (simple list in term_mappings)
            val = line.strip()
            if val.startswith('"') and val.endswith('"'):
                val = val[1:-1]
            if isinstance(fm.get(prev_key), list):
                fm[prev_key].append(val)
            elif prev_key in fm:
                fm[prev_key] = [fm[prev_key], val]

    return fm, end + 2


def parse_term_mappings(filepath):
    """Parse term_mappings from a domain MD file frontmatter."""
    text = Path(filepath).read_text(encoding="utf-8")
    m = re.search(r'term_mappings:\n((?:\s+(?:"[^"]*"|\S+):\s*(?:"[^"]*"|\S*)\n?)+)', text)
    if not m:
        return {}
    mappings = {}
    for line in m.group(1).strip().splitlines():
        tm = re.match(r'\s+(?:"([^"]+)"|([^:]+)):\s*(?:"([^"]*)"|(\S*))', line)
        if tm:
            key = tm.group(1) or tm.group(2).strip()
            val = tm.group(3) or tm.group(4) or ""
            mappings[key] = val
    return mappings


def detect_sections(filepath, body_start):
    """Detect ## heading sections with line numbers."""
    path = Path(filepath)
    if not path.exists():
        return []
    lines = path.read_text(encoding="utf-8").splitlines()
    sections = []
    current_title = None
    current_start = body_start

    for i in range(body_start - 1, len(lines)):
        line = lines[i]
        m = re.match(r'^##\s+(.+)$', line)
        if m:
            if current_title:
                sections.append({
                    "title": current_title,
                    "line_start": current_start,
                    "line_end": i + 1
                })
            current_title = m.group(1).strip()
            current_start = i + 1

    if current_title:
        sections.append({
            "title": current_title,
            "line_start": current_start,
            "line_end": len(lines)
        })

    return sections


def build_file_entry(filepath, file_type, required=False, sections=True):
    """Build a manifest entry for an MD file."""
    path = Path(filepath)
    if not path.exists():
        return None

    fm, body_start = parse_frontmatter(filepath)
    line_count = len(path.read_text(encoding="utf-8").splitlines())

    entry = {
        "path": str(path.resolve()),
        "name": fm.get("name", path.stem),
        "description": fm.get("description", ""),
        "type": file_type,
        "required": required,
        "line_count": line_count,
    }

    if sections:
        entry["sections"] = detect_sections(filepath, body_start)

    if file_type == "domain":
        entry["term_mappings"] = parse_term_mappings(filepath)

    return entry


def load_and_filter_glossary(glossary_path, quality):
    """Load glossary and filter by confidence based on quality level."""
    path = Path(glossary_path)
    if not path.exists():
        return None, 0, 0, ""

    data = json.loads(path.read_text(encoding="utf-8"))

    # Confidence filter rules:
    # standard:   remove pending
    # high:       remove pending, low
    # professional: keep only high
    if quality == "standard":
        kept = [e for e in data.get("entries", []) if e.get("confidence") != "pending"]
        note = "removed pending entries"
    elif quality == "high":
        kept = [e for e in data.get("entries", []) if e.get("confidence") not in ("pending", "low")]
        note = "removed pending and low confidence entries"
    elif quality == "professional":
        kept = [e for e in data.get("entries", []) if e.get("confidence") == "high"]
        note = "kept only high confidence entries"
    else:
        kept = data.get("entries", [])
        note = "no quality filter"

    total = len(data.get("entries", []))
    filtered = len(kept)

    return kept, total, filtered, note


def main():
    parser = argparse.ArgumentParser(
        description="Prepare knowledge manifest for translation pipeline"
    )
    parser.add_argument("--knowledge-dir", required=True)
    parser.add_argument("--target-lang", required=True)
    parser.add_argument("--source-lang", required=True)
    parser.add_argument("--domain", required=True, help="Comma-separated domain list")
    parser.add_argument("--quality", required=True, choices=["standard", "high", "professional"])
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    knowledge_dir = Path(args.knowledge_dir)
    target_lang = args.target_lang
    source_lang = args.source_lang
    domains = [d.strip() for d in args.domain.split(",")]
    quality = args.quality

    if not knowledge_dir.exists():
        print(f"Error: knowledge directory not found at {knowledge_dir}")
        raise SystemExit(1)

    files = {}
    missing = []  # Track missing files for knowledge_generation trigger

    # rules/base.md — always required
    rules_base = knowledge_dir / target_lang / "rules" / "base.md"
    entry = build_file_entry(rules_base, "rules", required=True)
    if entry:
        files["rules"] = entry
    else:
        missing.append({"type": "rules", "path": str(rules_base), "reason": "rules/base.md not found"})

    # rules/scoring-rubric.md — for inspector (fallback to en/ if target lang version missing)
    rubric = knowledge_dir / target_lang / "rules" / "scoring-rubric.md"
    entry = build_file_entry(rubric, "quality", required=False)
    if not entry:
        rubric = knowledge_dir / "en" / "rules" / "scoring-rubric.md"
        entry = build_file_entry(rubric, "quality", required=False)
    if entry:
        files["quality"] = entry

    # domain files — match requested domains
    for domain in domains:
        domain_file = knowledge_dir / target_lang / "domain" / f"{domain}.md"
        entry = build_file_entry(domain_file, "domain", required=False)
        if entry:
            files[f"domain_{domain}"] = entry
        else:
            missing.append({"type": "domain", "path": str(domain_file), "reason": f"domain/{domain}.md not found"})

    # adapt files — source_lang → target_lang
    # Try ISO code first, then full language name variants
    LANG_NAME_MAP = {
        "en": "english", "fr": "french", "de": "german", "es": "spanish",
        "it": "italian", "pt": "portuguese", "ru": "russian", "ja": "japanese",
        "ko": "korean", "zh": "chinese", "ar": "arabic", "nl": "dutch",
        "pl": "polish", "tr": "turkish", "vi": "vietnamese", "th": "thai",
        "hi": "hindi", "id": "indonesian", "sv": "swedish", "mn": "mongolian",
        "ms": "malay", "bn": "bengali", "fa": "persian", "da": "danish",
        "no": "norwegian", "fi": "finnish",
    }
    full_name = LANG_NAME_MAP.get(source_lang.lower(), "")
    adapt_paths = [
        knowledge_dir / target_lang / "adapt" / f"from_{source_lang}.md",
        knowledge_dir / target_lang / "adapt" / f"from_{source_lang.lower()}.md",
        knowledge_dir / target_lang / "adapt" / f"from_{source_lang.replace('-', '_')}.md",
    ]
    if full_name:
        adapt_paths.append(knowledge_dir / target_lang / "adapt" / f"from_{full_name}.md")
    adapt_found = False
    for adapt_path in adapt_paths:
        entry = build_file_entry(adapt_path, "adapt", required=False)
        if entry:
            files["adapt"] = entry
            adapt_found = True
            break
    if not adapt_found:
        expected = str(knowledge_dir / target_lang / "adapt" / f"from_{source_lang}.md")
        missing.append({"type": "adapt", "path": expected, "reason": f"adapt/from_{source_lang}.md not found"})

    # culture reference for source language
    culture_paths = [
        knowledge_dir / "culture" / f"{source_lang}.md",
        knowledge_dir / "culture" / f"{source_lang.lower()}.md",
    ]
    for cp in culture_paths:
        entry = build_file_entry(cp, "culture", required=False)
        if entry:
            files["culture"] = entry
            break

    # glossary
    glossary_path = knowledge_dir / "glossary" / f"{source_lang}_{target_lang}.json"
    glossary_entries, total_entries, filtered_entries, filter_note = load_and_filter_glossary(
        glossary_path, quality
    )
    if glossary_entries is not None:
        files["glossary"] = {
            "path": str(glossary_path.resolve()),
            "type": "glossary",
            "total_entries": total_entries,
            "filtered_entries": filtered_entries,
            "filter_note": filter_note,
            "required": False,
            "confidence_criteria": {
                "standard": "remove pending",
                "high": "remove pending, low",
                "professional": "keep only high",
            }.get(quality, ""),
        }

    # errors (if exist)
    errors_path = knowledge_dir / "errors" / f"{source_lang}_{target_lang}.json"
    if errors_path.exists():
        errors_data = json.loads(errors_path.read_text(encoding="utf-8"))
        files["errors"] = {
            "path": str(errors_path.resolve()),
            "type": "errors",
            "entries": errors_data.get("entries", []),
            "required": False,
        }

    manifest = {
        "schema_version": "2.0",
        "target_lang": target_lang,
        "source_lang": source_lang,
        "domain": domains,
        "quality": quality,
        "files": files,
        "missing": missing,
    }

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    Path(args.output).write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    file_count = len([k for k in files if k != "glossary"]) + (1 if "glossary" in files else 0)
    gloss_count = files.get("glossary", {}).get("filtered_entries", 0)
    if missing:
        missing_types = [m["type"] for m in missing]
        print(f"prepare_knowledge complete — {file_count} files, {gloss_count} glossary entries, {len(missing)} missing: {', '.join(missing_types)}")
    else:
        print(f"prepare_knowledge complete — {file_count} files, {gloss_count} glossary entries")


if __name__ == "__main__":
    main()
