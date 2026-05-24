# Translating Documents

[**中文版**](README.zh.md) | Translating Documents — 文档翻译

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

## Architecture

### Design Philosophy

The pipeline is built around a strict **orchestrator‑worker** separation. The main agent never translates, inspects, or revises — it only dispatches, reads lightweight JSON status files, and makes flow decisions. All language work and script execution is delegated to isolated subagents.

This design ensures:
- **Context isolation** — each subagent starts fresh, no hallucination carry‑over between stages
- **Auditability** — every stage writes files; the full job directory is a complete audit trail
- **Determinism** — deterministic Python scripts handle structural tasks (extraction, batching, marker checks, rendering); LLM judgment is reserved for language tasks

### Orchestrator

The main agent runs as a read‑evaluate‑dispatch loop:

```
Validate workflow_state.json → Read manifests/scorecards → 
  → Decide next stage → Dispatch subagent → 
  → Update workflow_state.json → Report progress → Repeat
```

**The main agent MUST:**
- collect source file path (DOCX only), source/target language, domain, and quality level
- create an isolated job directory with `job_manifest.json` and `workflow_state.json`
- validate workflow state via `validate_workflow_state.py` before each stage dispatch
- dispatch every stage to a subagent — never run scripts or language tasks directly
- update `workflow_state.json` after every stage
- read lightweight JSON files for flow decisions (never pass full reports via chat context)
- report progress after each stage; summarize only after final audit passes

**The main agent MUST NOT:**
- translate, revise, inspect, or write quality reports directly
- run pipeline scripts directly (always use a script runner subagent)
- pass full report contents into another worker's prompt
- declare completion before final audit passes

### File‑Driven Communication

All data between stages flows through files, never through chat context:

```
translation_job_{timestamp}_{source}/
├── job_manifest.json              # Static job metadata (schema‑validated)
├── workflow_state.json            # Single source of truth for pipeline state
├── extraction/
│   └── source_tagged.txt          # Tagged source text with [Pn] markers
├── knowledge/
│   └── knowledge_bundle.md        # Assembled rules for workers
├── translation/
│   ├── batch_001_translated.txt   # Per‑batch translations
│   └── translated_merged.txt      # Merged full translation
├── qa/
│   ├── marker_check.json          # Marker integrity gate
│   ├── numerical_score.json       # Numerical zero‑tolerance gate
│   ├── terminology_score.json     # Terminology scan data
│   └── scorecard_round1.json      # Inspection scorecard
├── revision/
│   └── revision_status_round1.json
├── render/
│   └── render_log.json            # Rendering status
└── final/
    ├── final_manifest.json        # Final gate verdict
    └── final_report.md            # Pipeline outcome summary
```

All flow decisions are made by reading JSON manifests and scorecards. This makes every run reproducible and debuggable — replay the job directory to see exactly what happened at each stage.

### Two Worker Types

| | Script Runner | Language Worker |
|---|---|---|
| **What** | Executes a Python pipeline script | Performs an LLM‑based language judgment task |
| **Template** | `workers/script_runner.md` | Worker‑specific template (e.g., `workers/translator.md`) |
| **Retry** | 3 internal debug+retry cycles + main agent layer + user layer escalation | Retry via re‑dispatch |
| **Output** | Exit status + key values from output files | JSON report in standardised format: `{stage, status, outputs, metrics, warnings}` |
| **Examples** | `extract_docx.py`, `check_markers.py`, `render_docx.py` | `translator.md`, `inspector.md`, `reviser.md` |

Each script runner gets a **fresh subagent** so debugging loops never pollute the main agent's context.

### State Machine

The pipeline follows a canonical 14‑stage workflow:

```
initialized → extraction → knowledge_loading → terminology_research → translation
  → merge_marker_check → [numerical_check] → terminology_scan → inspection_round1
  → [revision_round1] → [inspection_round2] → [revision_round2] → render → final_audit → completed
```

Stages in `[brackets]` are conditional based on quality level.

`workflow_state.json` tracks `current_stage`, `completed_stages`, `stage_history` (with status per entry), `blocked`, and `requires_revision`. Before every stage dispatch, a Python validation script checks the state against `workflow_state.schema.json` and the canonical stage list.

### Quality Level Stage Mapping

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
| revision_round2 | skip | skip | max 2, user approval |
| render | run | run | run |
| final_audit | run | run | run |

### Quality Gates

Hard gates that the pipeline MUST NOT bypass:

- **Marker check** — all `[Pn]` tags must be present and correctly paired before QA
- **Numerical check** (professional only) — zero‑tolerance: any amount, date, or percentage mismatch is automatically critical
- **Inspection** — no revision without a scorecard; no render after revision without reinspection
- **Final audit** — all gates must pass before the pipeline reports completion

### Recovery Architecture

When a stage fails, the system escalates through three layers:

1. **Script runner layer** — the subagent diagnoses and retries up to 3 times internally (handles encoding issues, missing packages, path errors)
2. **Main agent layer** — if internal retries fail, the main agent dispatches a fresh subagent for one more 3‑retry attempt
3. **User layer** — if all automated attempts fail, the main agent enters **Blocked Communication Protocol**: reports the block and offers the user `[Retry / Skip with reason / Abort]`

**Batch Translation Retry:** When a merge step detects missing batches, only the missing batches are re‑dispatched — already‑translated batches are preserved.

**Final Audit Recovery:** If `final_manifest.json` reports `status=blocked`, the main agent diagnoses which specific gate failed and offers targeted recovery (retry gate, skip with override, accept partial output, or abort).

### Component Map

```
Main Agent (orchestrator)
  │
  ├── Script Runner (Python pipeline scripts)
  │   ├── extract_docx.py           — DOCX → tagged text with [Pn] markers
  │   ├── split_batches.py          — Batch splitting with [CONTEXT] overlap
  │   ├── merge_batches.py          — Batch merge with missing‑batch detection
  │   ├── check_markers.py          — [Pn] tag integrity gate
  │   ├── check_numerics.py         — Numerical zero‑tolerance check
  │   ├── render_docx.py            — Tagged text → DOCX
  │   ├── final_audit.py            — Final gate validation + report generation
  │   └── validate_workflow_state.py — State machine validation against schema
  │
  └── Language Worker (LLM subagents, dispatched via prompt templates)
      ├── knowledge_loader.md       — Assembles domain rules + glossary into knowledge bundle
      ├── terminology_researcher.md — Extracts recurring terms, researches uncovered ones
      ├── translator.md             — Translates batches preserving [Pn]/[CONTEXT] markers
      ├── consistency_checker.md    — Scans full document for terminology consistency
      ├── inspector.md              — 6‑dimension quality scoring using rubric
      └── reviser.md                — Fixes issues identified by inspection
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
