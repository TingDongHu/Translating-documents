# Translating Documents

A file-driven, quality-assured DOCX translation pipeline for [Claude Code](https://claude.ai/code). Orchestrates specialized subagents through extraction, terminology research, parallel translation, multi-round QA, revision, and final audit — all coordinated via JSON manifests and a validated workflow state machine.

## Features

- **14-stage canonical pipeline** — extraction → knowledge loading → terminology research → translation → marker integrity check → numerical check → terminology scan → inspection → revision → render → final audit
- **3 quality levels** — `standard`, `high`, `professional` with declarative stage mapping; professional enforces numerical zero-tolerance, mandatory revision, and reinspection
- **Parallel batch translation** — splits large documents into overlapping batches, dispatches up to 3 translators concurrently, reports per-wave progress
- **Multi-language knowledge base** — domain rules, adaptation guides, cultural references, and bilingual glossaries for en, zh, fr, pt, mn, tr, sv
- **Scoring rubric** — 6 inspection dimensions (numerical accuracy, terminology consistency, semantic fidelity, format compliance, completeness, inference/OCR quality) with 5-band scoring criteria
- **Recovery protocols** — 3-layer retry escalation, blocked communication protocol, batch retry, and final audit recovery with targeted gate diagnosis
- **JSON Schema-validated** — all manifests, scorecards, and state files validated against schemas before each stage dispatch

## Requirements

- Python 3.10+
- [python-docx](https://pypi.org/project/python-docx/) — DOCX extraction and rendering
- [lxml](https://pypi.org/project/lxml/) — XML processing for DOCX files

Install dependencies:

```bash
pip install python-docx lxml
```

## Installation

Clone the repository into your Claude Code skills directory:

```bash
# Clone into the skills directory
git clone https://github.com/TingDongHu/Translating-documents.git ~/.claude/skills/translating-documents
```

Claude Code will automatically discover the skill on next launch. Invoke it by describing a translation task or using `/translating-documents`.

## Usage

Start a translation job by describing your document to Claude Code. The skill will guide you through the required parameters:

1. **Source language** — language of the input document
2. **Target language** — desired output language
3. **Domain** — one or more of: `general`, `legal`, `financial`, `commercial`, `administrative`, `technical`
4. **Quality level** — `standard`, `high`, or `professional`

Example prompt:

```
Translate this DOCX contract from Chinese to English. It's a commercial agreement, professional quality.
```

The pipeline creates an isolated job directory and reports progress after each stage:

```
[extraction] done — 622 tagged entries (9 body, 601 table, 6 header, 6 footer)
[translation] progress — batches 1-3/6 complete (3/6 batch)
[translation] done — 622 tags translated across 6 batches
[merge_marker_check] done — passed, no missing or extra tags
[inspection_round1] done — score 87, 1 critical, 4 warnings, revision required
[revision_round1] done — 5 issues addressed, 0 unresolved
[final_audit] done — all gates passed
```

## Pipeline Overview

### Workflow

```
initialized → extraction → knowledge_loading → terminology_research → translation
  → merge_marker_check → [numerical_check] → terminology_scan → inspection_round1
  → [revision_round1] → [inspection_round2] → [revision_round2] → render → final_audit → completed
```

Stages in `[brackets]` are conditional based on quality level.

### Quality Level Mapping

| Stage | standard | high | professional |
|-------|----------|------|--------------|
| extraction | run | run | run |
| knowledge_loading | run | run | run |
| terminology_research | run | run | run |
| translation | run | run | run |
| merge_marker_check | run | run | run |
| numerical_check | skip | skip | mandatory |
| terminology_scan | run | run | run |
| inspection_round1 | run | run | run |
| revision_round1 | skip | if critical > 0 | mandatory |
| inspection_round2 | skip | if revised | mandatory |
| revision_round2 | skip | skip | max 2 |
| render | run | run | run |
| final_audit | run | run | run |

### Architecture

```
Main Agent (orchestrator)
  ├── Script Runner (Python pipeline scripts)
  │   ├── extract_docx.py       — DOCX → tagged text
  │   ├── split_batches.py      — batch splitting with [CONTEXT] overlap
  │   ├── merge_batches.py      — batch merge with missing-batch detection
  │   ├── check_markers.py      — [Pn] tag integrity gate
  │   ├── check_numerics.py     — numerical zero-tolerance check
  │   ├── render_docx.py        — tagged text → DOCX
  │   ├── final_audit.py        — final gate validation + report generation
  │   └── validate_workflow_state.py — state machine validation
  └── Language Worker (LLM subagents)
      ├── knowledge_loader.md
      ├── terminology_researcher.md
      ├── translator.md
      ├── consistency_checker.md
      ├── inspector.md
      └── reviser.md
```

## Project Structure

```
translating-documents/
├── SKILL.md                       # Main orchestrator contract
├── improvement-plan.md            # Improvement history and roadmap
├── v2-todo.md                     # Future development candidates
├── pipeline/
│   ├── scripts/                   # Python pipeline scripts
│   └── templates/                 # JSON Schema definitions
├── workers/                       # Subagent prompt templates
└── knowledge/                     # Multi-language knowledge base
    ├── {lang}/
    │   ├── rules/                 # Writing rules and scoring rubrics
    │   ├── domain/                # Domain-specific terminology
    │   └── adapt/                 # Source-to-target adaptation rules
    ├── culture/                   # Cultural reference guides
    └── glossary/                  # Bilingual glossaries
```

## License

MIT
