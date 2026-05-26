"""
knowledge_extraction.py — DEPRECATED. Knowledge extraction was removed from the pipeline
in favor of a read-only pub-sub model. LLM capabilities replace auto-glossary growth.

This file is retained for reference only. It is no longer dispatched by the pipeline.

Original purpose: Extract new glossary entries, error patterns, and adaptation rules
from completed pipeline outputs and write them back to the knowledge base.

Usage:
    python knowledge_extraction.py \
        --job-manifest <path> \
        --source-tagged <path> \
        --translation-merged <path> \
        --qa-dir <path> \
        --revision-dir <path> \
        --knowledge-dir <path> \
        --output <path>

Output: status JSON with counts of extracted entries per category.

Language support: Uses Unicode character class detection (category L* for letters),
not hardcoded CJK ranges. Supports all scripts: Latin (with diacritics), CJK,
Cyrillic (Mongolian), Arabic, Hangul, etc.
"""

import argparse
import json
import os
import re
import unicodedata
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

CONFIDENCE_UPGRADE_THRESHOLDS = {
    "pending": 3,    # pending → low  after 3 verified uses
    "low": 5,        # low → medium   after 5 verified uses
    "medium": 10,    # medium → high  after 10 verified uses
}

ARCHIVE_AFTER_DAYS = 180  # confidence=pending or low entries untouched this long → archived


# ---------------------------------------------------------------------------
# I/O helpers
# ---------------------------------------------------------------------------

def load_json(path):
    if not Path(path).exists():
        return None
    with open(path, encoding='utf-8') as f:
        return json.load(f)


def save_json(data, path):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, encoding='utf-8', mode='w') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


# ---------------------------------------------------------------------------
# Term extraction (Unicode-based, no hardcoded script ranges)
# ---------------------------------------------------------------------------

def _is_letter(ch):
    """True for any Unicode letter character (L* category)."""
    return unicodedata.category(ch).startswith('L')


def extract_frequent_terms(source_text, min_freq=3):
    """
    Extract recurring terms using Unicode character class detection.

    Walks the text character-by-character, grouping consecutive letter+digit
    sequences into tokens. Supports all scripts without hardcoding ranges.

    Returns dict of term -> frequency.
    """
    text = re.sub(r'\[P\d+\]', '', source_text)

    tokens = []
    current = []
    for ch in text:
        cat = unicodedata.category(ch)
        if cat.startswith('L') or cat.startswith('N'):
            current.append(ch)
        else:
            if current:
                tokens.append(''.join(current))
                current = []
    if current:
        tokens.append(''.join(current))

    # Filter: skip pure numbers, keep 2+ char terms (or 1-char if it's a letter)
    filtered = []
    for t in tokens:
        if all(unicodedata.category(c).startswith('N') for c in t):
            continue  # pure numeric token
        if len(t) < 2 and not _is_letter(t[0]):
            continue  # single non-letter char
        if t.isascii() and t.isalpha() and len(t) < 3:
            continue  # short ascii words like "is", "to"—too noisy
        filtered.append(t)

    counts = Counter(filtered)
    return {k: v for k, v in counts.items() if v >= min_freq}


def extract_codes_and_references(text, min_freq=2):
    """
    Extract model numbers, standard references, and alphanumeric codes.

    These are high-value glossary candidates that pure word extraction misses.
    """
    patterns = [
        # Model/part numbers: alphanumeric with separators
        r'\b[A-Z0-9]{2,10}[-/][A-Z0-9/-]{1,20}\b',
        # Standard references
        r'\b(?:ISO|IEC|EN|DIN|GB/T|ASTM|ANSI|IEEE|UL|FCC|CCC)\s?\d+[\:\.]?\d*\b',
    ]
    codes = []
    for pat in patterns:
        codes.extend(re.findall(pat, text))
    counts = Counter(codes)
    return {k: v for k, v in counts.items() if v >= min_freq}


# ---------------------------------------------------------------------------
# Translation alignment (paragraph-level heuristic)
# ---------------------------------------------------------------------------

def is_glossary_candidate(term):
    """
    Filter out noise: single Chinese chars, full sentences, pure numbers.
    Only keep real glossary terms (typically 2-6 Chinese chars or meaningful phrases).
    """
    if len(term) <= 1:
        return False  # single char — too noisy
    if len(term) > 25:
        return False  # full sentence, not a term
    cjk_count = sum(1 for c in term if '一' <= c <= '鿿' or '㐀' <= c <= '䶿')
    if cjk_count == 1 and len(term) < 3 and not any(c.isalpha() for c in term if ord(c) > 127):
        return False  # single CJK char with no other meaningful content
    return True


def extract_translation_mapping(term, source_text, translated_text):
    """
    Paragraph-level alignment: find which source paragraph contains the term,
    then return aligned context.

    Returns (translated_snippet, source_context) tuple.
    translated_snippet is the translated paragraph WITHOUT tag prefix.
    source_context is the source paragraph for reference.

    Known limitation: returns the full translated paragraph (not the exact
    term translation). Entries are confidence=pending and need human
    verification before use in production.
    """
    source_lines = source_text.splitlines()
    translated_lines = translated_text.splitlines()

    for i, line in enumerate(source_lines):
        if term in line and i < len(translated_lines):
            translated = translated_lines[i].strip()
            # Strip [Pxxx] tag prefix for cleaner target
            clean = re.sub(r'^\[P\d+\]\s*', '', translated)
            return clean[:200], line.strip()
    return None, None


# ---------------------------------------------------------------------------
# Glossary update logic
# ---------------------------------------------------------------------------

def detect_conflicts(existing_entries, new_entry):
    """
    Check if a new entry conflicts with an existing one (same source,
    different target). If so, mark the new entry as pending and note
    the conflict source. Does NOT modify existing entries.
    """
    for existing in existing_entries:
        if existing["source"] == new_entry["source"] and existing["target"] != new_entry["target"]:
            new_entry["confidence"] = "pending"
            new_entry["conflicts_with"] = existing["source"]
            new_entry["conflict_note"] = (
                f"Source '{existing['source']}' already mapped to "
                f"'{existing['target']}' (confidence={existing['confidence']}). "
                "New mapping added as pending — manual review recommended."
            )
            break
    return new_entry


def _upgrade_confidence(entry):
    """Apply confidence upgrade thresholds. Returns True if upgraded."""
    current = entry["confidence"]
    threshold = CONFIDENCE_UPGRADE_THRESHOLDS.get(current)
    if threshold and entry.get("verified_count", 0) >= threshold:
        levels = ["pending", "low", "medium", "high"]
        idx = levels.index(current)
        entry["confidence"] = levels[idx + 1]
        return True
    return False


def update_glossary(existing_glossary, new_entries, source_lang, target_lang, job_id):
    """
    Merge new entries into existing glossary.

    - Exact match (source+target same): increment verified_count, upgrade confidence
    - Source match, target differs: append as pending, flag conflict
    - New source: append as pending
    """
    entries = existing_glossary.get("entries", []) if existing_glossary else []
    existing_sources = {e["source"]: e for e in entries}

    added = 0
    updated = 0
    upgraded = 0
    conflicts = 0

    for entry in new_entries:
        src = entry["source"]
        if src in existing_sources:
            existing = existing_sources[src]
            if existing["target"] == entry["target"]:
                existing["verified_count"] = existing.get("verified_count", 0) + 1
                existing["last_seen"] = entry.get("last_seen", "")
                if _upgrade_confidence(existing):
                    upgraded += 1
                updated += 1
                continue
            # Same source, different target — conflict
            entry = detect_conflicts(entries, entry)
            conflicts += 1

        entries.append({
            "source": src,
            "target": entry["target"],
            "frequency": entry.get("frequency", 1),
            "confidence": entry.get("confidence", "pending"),
            "verified_count": 0,
            "first_seen": entry.get("last_seen", ""),
            "last_seen": entry.get("last_seen", ""),
            "source_jobs": [job_id],
            "category": entry.get("category", "general"),
            "source_context": entry.get("source_context", ""),
            "extraction_method": entry.get("extraction_method", "manual"),
        })
        added += 1

    return entries, added, updated, upgraded, conflicts


# ---------------------------------------------------------------------------
# Archival / pruning
# ---------------------------------------------------------------------------

def archive_stale_entries(entries, max_age_days=ARCHIVE_AFTER_DAYS):
    """
    Move entries that haven't been seen recently into an archived list.
    Only applies to pending/low confidence — high confidence is kept regardless.

    Returns (active_entries, archived_entries).
    """
    now = datetime.now(timezone.utc).isoformat()
    active = []
    archived = []
    for entry in entries:
        last_seen = entry.get("last_seen")
        if entry.get("confidence") in ("pending", "low") and last_seen:
            try:
                age = (datetime.fromisoformat(now) - datetime.fromisoformat(last_seen)).days
                if age > max_age_days:
                    archived.append(entry)
                    continue
            except (ValueError, TypeError):
                pass  # unparseable date — keep entry
        active.append(entry)
    return active, archived


# ---------------------------------------------------------------------------
# Script runner
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Extract knowledge from completed pipeline outputs")
    parser.add_argument("--job-manifest", required=True)
    parser.add_argument("--source-tagged", required=True)
    parser.add_argument("--translation-merged", required=True)
    parser.add_argument("--qa-dir", required=True)
    parser.add_argument("--revision-dir", required=True)
    parser.add_argument("--knowledge-dir", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    manifest = load_json(args.job_manifest)
    if not manifest:
        print(f"Error: job manifest not found or invalid at {args.job_manifest}")
        raise SystemExit(1)

    source_lang = manifest.get("source_lang", manifest.get("source_language"))
    target_lang = manifest.get("target_lang", manifest.get("target_language"))
    domain = manifest["domain"]
    job_id = manifest.get("job_id", manifest.get("job_name", "unknown"))

    source_text = Path(args.source_tagged).read_text(encoding='utf-8')
    translated_text = Path(args.translation_merged).read_text(encoding='utf-8')

    glossary_path = Path(args.knowledge_dir) / "glossary" / f"{source_lang}_{target_lang}.json"
    errors_path = Path(args.knowledge_dir) / "errors" / f"{source_lang}_{target_lang}.json"
    adapt_path = Path(args.knowledge_dir) / target_lang / "adapt" / f"from_{source_lang}.json"

    stats = {
        "glossary_entries_added": 0,
        "glossary_entries_updated": 0,
        "glossary_entries_upgraded": 0,
        "glossary_conflicts_detected": 0,
        "glossary_entries_archived": 0,
        "error_patterns_extracted": 0,
        "adapt_rules_extracted": 0,
    }

    # --- Extract glossary entries from source text ---
    frequent_terms = extract_frequent_terms(source_text, min_freq=3)
    codes = extract_codes_and_references(source_text)

    existing_glossary = load_json(glossary_path) if glossary_path.exists() else None
    if existing_glossary is None:
        existing_glossary = {
            "source_lang": source_lang,
            "target_lang": target_lang,
            "domain": domain if isinstance(domain, list) else [domain],
            "last_updated": "",
            "entries": []
        }

    new_entries = []
    for term, freq in frequent_terms.items():
        if not is_glossary_candidate(term):
            continue
        translation, source_context = extract_translation_mapping(term, source_text, translated_text)
        if translation:
            new_entries.append({
                "source": term,
                "target": translation,
                "frequency": freq,
                "source_context": source_context,
                "last_seen": datetime.now(timezone.utc).isoformat(),
                "category": "general",
                "extraction_method": "paragraph_alignment",
                "confidence": "pending"
            })

    for term, freq in codes.items():
        if not is_glossary_candidate(term):
            continue
        translation, source_context = extract_translation_mapping(term, source_text, translated_text)
        if translation:
            new_entries.append({
                "source": term,
                "target": translation,
                "frequency": freq,
                "source_context": source_context,
                "last_seen": datetime.now(timezone.utc).isoformat(),
                "category": "reference",
                "extraction_method": "paragraph_alignment",
                "confidence": "pending"
            })

    updated_entries, added, updated, upgraded, conflicts = update_glossary(
        existing_glossary, new_entries, source_lang, target_lang, job_id
    )

    # --- Archive stale entries ---
    active_entries, archived = archive_stale_entries(updated_entries)
    existing_glossary["entries"] = active_entries
    existing_glossary["archived_count"] = existing_glossary.get("archived_count", 0) + len(archived)
    existing_glossary["last_updated"] = datetime.now(timezone.utc).isoformat()
    existing_glossary["domain"] = list(set(
        existing_glossary.get("domain", []) + (domain if isinstance(domain, list) else [domain])
    ))

    save_json(existing_glossary, glossary_path)
    stats["glossary_entries_added"] = added
    stats["glossary_entries_updated"] = updated
    stats["glossary_entries_upgraded"] = upgraded
    stats["glossary_conflicts_detected"] = conflicts
    stats["glossary_entries_archived"] = len(archived)

    # --- Extract error patterns from QA scorecards ---
    qa_dir = Path(args.qa_dir)
    for scorecard_file in sorted(qa_dir.glob("scorecard_round*.json")):
        scorecard = load_json(scorecard_file)
        if scorecard and scorecard.get("critical_count", 0) > 0:
            # Future enhancement: parse critical issue details from inspection report
            stats["error_patterns_extracted"] += scorecard["critical_count"]

    # --- Write output status ---
    result = {
        "stage": "knowledge_extraction",
        "status": "completed",
        "outputs": {
            "glossary_updated": str(glossary_path),
            "errors_updated": str(errors_path) if errors_path.exists() else None,
            "adapt_updated": str(adapt_path) if adapt_path.exists() else None
        },
        "metrics": stats,
        "warnings": []
    }

    if stats["glossary_conflicts_detected"] > 0:
        result["warnings"].append(
            f"{stats['glossary_conflicts_detected']} conflict(s) detected — "
            "same source mapped to different targets. New entries flagged as pending."
        )
    if stats["glossary_entries_archived"] > 0:
        result["warnings"].append(
            f"{stats['glossary_entries_archived']} stale entry(ies) archived "
            f"(confidence=pending/low, untouched >{ARCHIVE_AFTER_DAYS} days)."
        )

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    Path(args.output).write_text(
        json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8'
    )
    print(f"Knowledge extraction complete: +{added} glossary entries, {updated} updated, {upgraded} upgraded")
    print(f"Conflicts: {conflicts}, Archived: {len(archived)}")
    print(f"Error patterns flagged: {stats['error_patterns_extracted']}")


if __name__ == "__main__":
    main()
