---
name: Translating Documents
description: Runs document translation jobs through a file-driven quality-assured pipeline. Use when translating text or documents between languages, preserving document format, with quality inspection, revision, and numerical zero-tolerance checks.
---

# Translating Documents

Run document translation jobs through a file-driven, auditable pipeline. Supports DOCX, HTML, Markdown (.md), TXT, XLSX, and PPTX source files.

The main agent is an orchestrator. Specialized workers and scripts perform extraction, knowledge loading, professional term research (parallel with translation), translation, QA, revision, rendering, and final audit. All stages write to `pipeline.log` for diagnostics and replay debugging.

## Main Agent Contract

The main agent MUST:

- collect source file path (DOCX, HTML, Markdown (.md), TXT, XLSX, or PPTX format);
- collect source language, target language, domain, and quality level;
- create an isolated job directory;
- write `job_manifest.json`;
- initialize `workflow_state.json`;
- dispatch workers with file paths and key parameters;
- read lightweight JSON files for flow decisions;
- write timestamped entries to `pipeline.log` after each dispatch, complete, failure, skip, and stall event;
- update `workflow_state.json` after every stage;
- report stage progress to the user after each stage completes (see Progress Reporting);
- summarize final results only after `final/final_manifest.json` reports `status=completed`.

The main agent MUST NOT:

- translate source content;
- revise translation content;
- write quality reports manually;
- merge large translation batches manually;
- inspect semantic fidelity directly;
- pass full reports by copying contents into another worker prompt;
- run pipeline scripts directly (always dispatch to a script runner subagent);
- debug script errors (script runners handle their own debugging);
- declare completion before final audit passes.

## Main Agent Tools

The main agent uses these tools directly:

- **Read** — read JSON status files, manifests, and scorecards for flow decisions.
- **Write** — create job directory, write `job_manifest.json`, `workflow_state.json`, and `pipeline.log`.
- **Edit** — update `workflow_state.json` after each stage, append entries to `pipeline.log`.
- **Bash** — execute safe deterministic pipeline scripts directly (see "Safe Scripts" below). NOT for general shell commands.
- **Agent** — dispatch script runner or language worker subagents.

## Required User Parameters

Ask one question at a time until these parameters are known:

1. source language;
2. target language;
3. domain, as one or more of `general`, `legal`, `financial`, `commercial`, `administrative`, `technical`;
4. quality level: `standard`, `high`, or `professional`.

If the user already provided a parameter, do not ask again.

## Job Directory Contract

Every translation job MUST create an isolated job directory:

```text
translation_job_{timestamp}_{source_basename}/
  job_manifest.json
  workflow_state.json
  pipeline.log
  extraction/
  knowledge/
  translation/
  qa/
  revision/
  render/
  final/
```

Large content MUST be exchanged through files. Flow decisions MUST use JSON manifests, scorecards, and status files.

## Core Files

Required core files:

- `job_manifest.json` — static job metadata;
- `workflow_state.json` — single source of truth for current stage;
- `extraction/source_tagged.txt` — tagged source text;
- `extraction/extraction.json` — source location mapping;
- `extraction/extraction_report.json` — paragraph count and type summary for batch strategy decisions; report contents vary by format (DOCX/HTML/MD: body_count, heading_count, table_count; TXT: body_count; XLSX: table_count; PPTX: body_count, table_count);
- `pipeline.log` — append-only structured event log for diagnostics;
- `knowledge/knowledge_manifest.json` — index of produced bundles;
- `knowledge/bundle_universal.md` — target-language writing rules;
- `knowledge/bundle_domain.md` — domain-specific decision frameworks;
- `knowledge/bundle_glossary.json` — bilingual glossary subset;
- `knowledge/bundle_adapt.json` — adaptation rules (if exists);
- `knowledge/bundle_errors.json` — error patterns (if exists);
- `knowledge/bundle_culture.md` — source culture rules (if exists);
- `knowledge/bundle_quality.md` — scoring rubric (if exists, for inspectors);
- `knowledge/adaptation_notes.json` — adaptation research output;
- `knowledge/research_reference.json` — professional term research output for inspector (if research completed);
- `knowledge/research_heartbeat.json` — researcher heartbeat for stall detection (if research dispatched);
- `translation/translated_merged.txt` — merged current translation;
- `translation/marker_check.json` — marker integrity gate;
- `qa/numerical_score.json` — numerical gate;
- `qa/scorecard_roundN.json` — inspection scorecard;
- `revision/revision_status_roundN.json` — revision status;
- `render/render_log.json` — rendering status;
- `final/final_manifest.json` — final completion gate;
- `final/final_report.md` — pipeline outcome brief, auto-generated by `final_audit.py` from gate results. Used by the main agent for final user summary.

JSON schema templates live in `pipeline/templates/`.

Reusable deterministic scripts live in `pipeline/scripts/`.

## Workflow State Machine

Canonical stages:

```text
initialized
  -> extraction
  -> knowledge_loading
  -> adaptation_research
  [parallel fork]
  -> translation (foreground)
  -> adaptation_research (background)
  -> professional_term_research (background)
  [parallel join]
  -> merge_marker_check
  -> numerical_check
  -> inspection_round1
  -> revision_round1
  -> inspection_round2
  -> revision_round2
  -> render
  -> final_audit
  -> completed
```

Skipped stages MUST be recorded in `workflow_state.json` with a reason.

### Stage Dispatch Method

Every stage is dispatched to an isolated subagent. The main agent never runs scripts or language tasks directly.

| Stage | Worker Type | Worker Template | Script | Dependencies |
|-------|-------------|----------------|--------|--------------|
| extraction | script runner | `workers/script_runner.md` | `pipeline/scripts/extract_{source_format}.py` | — |
| knowledge_loading | language worker | `workers/knowledge_loader.md` | — | — |
| professional_term_research | language worker (background) | `workers/terminology_researcher.md` | — | runs parallel with translation |
| adaptation_research | language worker (background) | `workers/adaptation_researcher.md` | — | runs parallel with translation |
| translation | language worker (parallel by batch) | `workers/translator.md` | — | — |
| merge_marker_check | main agent orchestrated | `workers/script_runner.md` | `merge_batches.py` → `check_markers.py` (sequential, see subflow) | — |
| numerical_check | script runner | `workers/script_runner.md` | `pipeline/scripts/check_numerics.py` | — |
| inspection_roundN | language worker | `workers/inspector.md` | — | writes scorecard + detailed QA report per round |
| revision_roundN | language worker | `workers/reviser.md` | — | — |
| render | script runner | `workers/script_runner.md` | `pipeline/scripts/render_{source_format}.py` | — |
| final_audit | script runner | `workers/script_runner.md` | `pipeline/scripts/final_audit.py` | — |

**Format dispatching:** The `{source_format}` placeholder is resolved from `job_manifest.source_format` at dispatch time. Supported values: `docx`, `html`, `md`, `txt`, `xlsx`, `pptx`. The main agent constructs the script path by interpolating `source_format` into the script name (e.g. `extract_docx.py`, `extract_html.py`, `extract_md.py`, `extract_txt.py`, `extract_xlsx.py`, `extract_pptx.py`).

**Script runner** = a subagent that executes a Python script, debugs encoding/path/import errors, retries up to 3 times, and returns only exit status and key output values. Each script gets a fresh subagent so debugging loops never pollute the main agent's context.

**Language worker** = a subagent with the corresponding worker template, receiving file paths and key parameters.

### Safe Scripts

Some deterministic Python scripts run **directly via Bash** (not through a script runner subagent) to avoid the ~10-15s subagent dispatch overhead for <1s scripts.

**Safe scripts** (eligible for direct Bash execution):

| Category | Script | Fallback |
|----------|--------|----------|
| Workflow validation | `validate_workflow_state.py` | script runner if failed |
| Marker integrity | `check_markers.py` | script runner if failed |
| Numerical check | `check_numerics.py` | script runner if failed |
| Final audit | `final_audit.py` | script runner if failed |
| Batch splitting | `split_batches.py` | script runner if failed |

**Script runner required** (too complex or I/O-heavy for direct execution):

`extract_*.py`, `render_*.py`, `merge_batches.py`

**Safe script execution rules:**

1. Construct the command: `python pipeline/scripts/{script}.py {args}`.
2. Run via Bash tool. One attempt only — no debug loop.
3. If exit code is 0: read output files, log complete, proceed.
4. If exit code is non-zero: fall back to script runner subagent for one attempt with debugging.
5. Log the event to pipeline.log. Record whether Bash direct or fallback was used.

`merge_marker_check` 在一个 stage 内依次运行两个脚本。两个步骤使用独立的 script runner subagent，避免上下文污染。

1. **merge_batches** — dispatch script runner 运行 `merge_batches.py`：
   - `--manifest {job_manifest}`
   - `--translated-dir translation/`
   - `--output translation/translated_merged.txt`
   - 如果失败：读取 `.status.json` 的 `metrics.missing_batches`，按 **Batch Translation Retry** 协议处理缺失批次，重新 dispatch translator，然后重试 merge。
   - 如果成功：进入步骤 2。

2. **check_markers** — dispatch script runner 运行 `check_markers.py`：
   - `--source extraction/source_tagged.txt`
   - `--translation translation/translated_merged.txt`
   - `--output translation/marker_check.json`
   - 如果失败：stage blocked，按 **Blocked Communication Protocol** 处理（marker_check 是 hard gate）。
   - 如果成功：stage completed，更新 `translation/marker_check.json` 到 workflow_state。

### adaptation_research

**Position**: `knowledge_loading → [parallel fork: adaptation_research + translation + professional_term_research]`

**Purpose**: Research known pitfalls and adaptation rules for the specific source→target language pair.

**Inputs**:
- source_lang, target_lang, domain
- `knowledge/bundle_adapt.json` (existing adaptation rules, if any)
- `knowledge/bundle_errors.json` (existing error patterns, if any)

**Process**:
1. Load existing adapt and error pattern knowledge.
2. Filter by domain (only inject relevant entries).
3. Evaluate coverage — identify categories with weak coverage.
4. For weak categories, research using web if needed.
5. Merge existing + new rules into adaptation_notes.json.
6. Write adaptation_notes.json to `knowledge/adaptation_notes.json`.

**Error handling**: Non-hard gate. If web research fails, use only existing knowledge. If no adaptation knowledge exists at all, inject only base.md rules and flag the gap.

**Output**: `knowledge/adaptation_notes.json`

## Quality Levels

`standard`:

- extraction;
- knowledge loading;
- translation;
- merge_marker_check;
- numerical check (zero-tolerance gate);
- inspection_round1;
- render;
- final audit.

`high`:

- all `standard` stages;
- revise if any critical issue exists;
- reinspect after revision.

`professional`:

- all `high` stages;
- revision triggered if critical > 0 (same as high);
- maximum two revision rounds unless the user approves more.

### Quality Level Stage Mapping

| Stage | standard | high | professional |
|-------|----------|------|--------------|
| extraction | run | run | run |
| knowledge_loading | run | run | run |
| adaptation_research | run | run | run |
| translation | run | run | run |
| professional_term_research | run (background) | run (background) | run (background) |
| merge_marker_check | run | run | run |
| numerical_check | run | run | run |
| inspection_round1 | run | run | run |
| revision_round1 | skip | if critical > 0 | if critical > 0 |
| inspection_round2 | skip | if revised | if revised |
| revision_round2 | skip | skip | max 2, user approval |
| render | run | run | run |
| final_audit | run | run | run |

## Worker Bundle Mapping

| Worker | Bundles Received |
|--------|-----------------|
| translator | universal + domain + adapt + glossary + errors + culture + supplementary_terms + adaptation_notes |
| professional_term_researcher | source_tagged.txt |
| adaptation_researcher | adapt + errors |
| inspector | universal + domain + glossary + quality + adaptation_notes + research_reference |
| reviser | universal + domain + adapt + adaptation_notes |
| knowledge_loader | universal (for itself) |

## Pipeline Log

Every job directory contains `pipeline.log` — an append-only structured event log for diagnostics.

### Log Format

```
2026-05-26T10:30:00.123 | INFO  | extraction        | dispatch
2026-05-26T10:30:05.456 | INFO  | extraction        | complete  | 622 entries (elapsed: 5.3s)
2026-05-26T10:30:06.000 | INFO  | knowledge_loading | dispatch
2026-05-26T10:30:21.789 | INFO  | knowledge_loading | complete  | 6 bundles (elapsed: 15.8s)
2026-05-26T10:30:22.000 | INFO  | translation       | dispatch  | wave 1/2 (batches 1-3)
2026-05-26T10:30:22.001 | INFO  | research          | dispatch  | background, parallel with translation
2026-05-26T10:31:00.000 | WARN  | research          | stalled   | no heartbeat for 60s
2026-05-26T10:31:05.000 | INFO  | translation       | complete  | wave 1/2 done (elapsed: 43.0s)
```

Format: `timestamp | level | stage | event | details`

### Log Event Types

| Event | When | Level |
|-------|------|-------|
| `dispatch` | Before Agent tool call | INFO |
| `complete` | Subagent/script returned success | INFO |
| `failed` | Subagent/script returned failure | ERROR |
| `skipped` | Stage skipped by quality level | INFO |
| `stalled` | Heartbeat not updated for 60s | WARN |
| `retry` | Retry triggered | WARN |
| `recovered` | Retry succeeded | INFO |
| `parallel_fork` | Parallel branch started | INFO |
| `parallel_join` | Parallel branches merged | INFO |

### Log Management

The pipeline.log uses a sentinel marker for efficient appending, avoiding O(n) read/write on every entry.

1. Initialize pipeline.log with `__LOG_END__` as the last line.
2. To append: use the Edit tool to replace `__LOG_END__` with:
   ```
   {new_log_line}
   __LOG_END__
   ```
3. This avoids reading and rewriting the entire file — replaces only the sentinel line.
4. The `__LOG_END__` marker is always the last line of the file.

Mandatory log points:
- Before every subagent dispatch → `dispatch`
- After every subagent completes → `complete` or `failed`
- Before every skip decision → `skipped`
- On heartbeat stall detection → `stalled`
- On parallel fork/join → `parallel_fork` / `parallel_join`

## 异步调度与心跳检测

### Background Agent Dispatch

`professional_term_research` 使用 `Agent(run_in_background=true)` 调度。主 agent 在 dispatch 后立即启动 translation，不等待 research 返回。

```text
# Dispatch research (non-blocking)
Agent tool:
  description: "Professional term research"
  prompt: @workers/terminology_researcher.md (new professional term researcher, parameters filled)
  run_in_background: true

# Immediately start translation (foreground)
Agent tool:
  description: "Translation batch 1"
  prompt: @workers/translator.md
  # No run_in_background → synchronous
```

### Heartbeat Contract

Researcher subagent 每完成 5 条术语调研，写一次 `knowledge/research_heartbeat.json`：

```json
{
  "stage": "professional_term_research",
  "terms_found": 0,
  "terms_selected": 0,
  "terms_completed": 0,
  "current_term": "",
  "timestamp": "2026-01-01T00:00:00.000"
}
```

### Stall Detection

主 agent 在翻译及 post-processing 全部完成后, 在 dispatch inspection 之前执行 stall 检测：

1. **Research 已完成** — `knowledge/research_reference.json` 存在 → 正常使用，日志 `complete`
2. **Research 仍在运行** — 只有 heartbeat，timestamp 在 60s 内 → 一行日志 `waiting`，最多等待 30 秒
3. **Research 悬挂** — heartbeat timestamp 超过 60s 未更新 → 日志 `WARN | research | stalled`，继续不阻塞
4. **无任何输出** — heartbeat 和 reference 都不存在 → 日志 `WARN | research | no_output`，判定悬挂/未启动

Research 在任何情况下都不是 hard gate。pipeline 永远不会因为 research 未完成而阻塞。

## Batch Strategy

After extraction completes, read `extraction/extraction_report.json` to get `paragraph_count`. Use it to decide batch splitting:

| paragraph_count | --batch-size | --overlap | Result |
|-----------------|-------------|-----------|--------|
| ≤ 1000 | omit (default: single batch) | omit | 1 batch, no split |
| 1001–3000 | 1000 | 10 | 2–3 batches |
| > 3000 | 1500 | 10 | 3+ batches |

Rationale: typical tagged source averages ~5 tokens per line. 1000 lines ≈ 5000 source tokens + knowledge bundle ≈ well within modern context windows. Over-splitting wastes dispatch rounds; under-splitting risks context overflow.

### Translation Parallelism

After `knowledge_loading` (and `adaptation_research` if applicable), the pipeline forks into two parallel tracks:

**Track A — Translation (sliding window, foreground):**
翻译阶段使用滑动窗口，最多同时 dispatch 3 个 translator subagent。每收到一个 completion 立即 dispatch 下一个 batch，减少空闲等待。

1. 初始 dispatch 前 3 个 batch（`run_in_background=true`）。
2. 每收到一个 completion notification:
   a. 标记该 batch 完成。如该 batch 失败，记录 batch 号，稍后重试。
   b. 如果还有未 dispatch 的 batch，立即 dispatch 下一个（`run_in_background=true`）。
   c. 报告进度：`翻译进度: {completed_batches}/{total_batches} 批完成，{active_batches} 批进行中`
3. 所有 batch dispatch 完成后，等待剩余的活跃 batch。
4. 检查是否有失败的 batch，按 **Batch Translation Retry** 协议处理（逐批重试，最多 3 次）。
5. 所有 batch 完成后报告：`翻译进度: 全部 {total_batches} 批完成（{elapsed:.1f}s）`

**Track B — Professional Term Research (background, parallel):**
As soon as translation starts, dispatch `professional_term_research` via `run_in_background=true`:

```
Agent tool:
  description: "Professional term research"
  prompt: workers/terminology_researcher.md (with source file and paths filled in)
  run_in_background: true
```

Research runs entirely in parallel with translation. The main agent does NOT wait for it.

**Parallel join (before inspection):**
After translation and all post-processing (merge_marker_check, numerical_check) complete, the main agent checks research status before dispatching inspection:

1. Read `knowledge/research_reference.json` — if it exists, research completed normally.
2. If not found, read `knowledge/research_heartbeat.json` — if heartbeat exists and timestamp is within 60 seconds, wait up to 30 more seconds.
3. If heartbeat timestamp is > 60 seconds old or neither file exists, log `WARN | research | stalled` to pipeline.log and proceed without research reference.
4. Research is NOT a hard gate — the pipeline never blocks on research completion.

Translation progress reporting is unchanged. Research reports only on completion or stall:

- `[professional_term_research] done — 15 terms researched, 10 with official translations`
- `[professional_term_research] skipped — no professional terms found`
- `[professional_term_research] stalled — no heartbeat for 60s, proceeding without reference`

每个 translator 使用独立的 subagent，不共享上下文。

## Worker Dispatch Contract

All stages are dispatched to isolated subagents. The main agent never runs scripts or language tasks directly.

Two worker types:

**Script runner** — executes a Python pipeline script, debugs runtime errors (encoding, paths, missing deps), retries up to 3 times, returns only exit status and key output values. Uses `workers/script_runner.md`.

**Language worker** — performs a language judgment task (translation, inspection, revision, etc.). Receives file paths and key parameters, writes outputs to files, returns only paths, counts, scores, and status summaries. Uses the corresponding worker template in `workers/`.

### Language Worker Report Format

所有 language worker 返回给 main agent 的结果（subagent chat response 尾部）必须遵循以下结构：

```json
{
  "stage": "{stage_name}",
  "status": "completed",
  "outputs": {
    "key": "/path/to/output_file"
  },
  "metrics": {
    "key": 0
  },
  "warnings": []
}
```

各 worker 的 `outputs` 和 `metrics` 具体字段见对应模板的 Workflow 和 JSON Format 章节。每个 worker 必须按自己的 JSON Format 报告，不要返回模板中未定义的字段。

## Quality Gates

The pipeline MUST NOT enter:

- QA without a passing marker check;
- revision without scorecard;
- render after revision without reinspection;
- final without final audit.

Professional jobs differ from high only in allowing up to 2 revision rounds (with user approval). All quality levels share the same mandatory hard gates: marker_check, numerical_check, inspection, final_audit.

## Progress Reporting

After each stage completes, the main agent MUST report a one-line progress update to the user. Format:

```text
[stage_name] done — <1-2 key facts from stage output>
```

Examples:

- `[extraction] done — 622 tagged entries (9 body, 601 table, 6 header, 6 footer)`
- `[translation] done — 622 tags translated across 4 batches`
- `[professional_term_research] done — 15 terms researched, 10 with official translations`
- `[professional_term_research] stalled — no heartbeat for 60s, proceeding without reference`
- `[merge_marker_check] done — passed, no missing or extra tags`
- `[inspection_round1] done — score 87, 1 critical, 4 warnings, revision required`
- `[revision_round1] done — 5 issues addressed, 0 unresolved`

If a stage is skipped, report that too:

- `[numerical_check] done — passed, all numbers verified`
- `[numerical_check] done — 2 mismatches found, revision required`

Do not report before a stage completes. Do not report full report contents.

## Recovery Rules

If a stage fails:

- set `workflow_state.json.blocked = true`;
- record failed stage and reason;
- do not skip ahead;
- retry only the failed stage when possible;
- preserve previous outputs.

### Workflow State Validation

Before each stage dispatch, the main agent MUST validate `workflow_state.json` directly:

1. Read `workflow_state.json` using the Read tool.
2. Verify all 7 required fields exist: `current_stage`, `completed_stages`, `blocked`, `requires_revision`, `critical_issues`, `next_stage`, `stage_history`.
3. Verify `current_stage` is in the canonical stage list.
4. Verify each `stage_history` entry has `stage` and `status` fields; `status` is one of `pending/in_progress/completed/skipped/failed`.
5. Verify `blocked` and `requires_revision` are booleans.

If all checks pass → proceed with the stage dispatch.

If any check fails:
1. Fall back to the script runner for detailed diagnostics: `python pipeline/scripts/validate_workflow_state.py --state workflow_state.json`.
2. Read the error report for specific field errors.
3. Fix each error by editing `workflow_state.json`.
4. Re-run the manual checks. Repeat up to 3 times total.
5. If still failing after 3 attempts: enter **Blocked Communication Protocol** with reason `"internal pipeline error: workflow_state validation failed"`.

### Retry Escalation

When a script runner reports failure after its 3 internal retries:

1. **Script runner layer** — 3 internal debug+retries passes (existing).
2. **Main agent layer** — dispatch a **fresh** script runner subagent for one more attempt (3 more internal retries). Use a new subagent so previous failures don't pollute context.
3. **User layer** — if the fresh attempt also fails, enter **Blocked Communication Protocol**.

Transient failures (encoding, paths, missing packages) typically resolve at layer 2 without user interruption.

### Blocked Communication Protocol

When a stage is blocked after retries, the main agent MUST:

1. Report the block to the user: `[stage_name] blocked — <reason>`
2. Present the user with options:
   - **Retry** — dispatch a fresh subagent for the failed stage.
   - **Skip with reason** — only if the stage is not a hard gate (e.g., professional_term_research can be skipped with a reason recorded in workflow_state.json).
   - **Abort** — stop the pipeline. Previous outputs are preserved in the job directory.
3. Wait for the user's decision before proceeding.

Hard gates that MUST NOT be skipped: marker_check, numerical_check, inspection, final_audit.

### Batch Translation Retry

When the merge step reports missing batches, the main agent MUST:

1. Identify the missing batch numbers from the script runner's report.
2. Re-dispatch translation worker subagents for only the missing batches.
3. Re-run the merge step after the missing batches are produced.
4. Do not re-translate already-completed batches.

### Final Audit Recovery

When `final/final_manifest.json` reports `status=blocked`, the main agent MUST diagnose which gate failed and present targeted options:

1. Read `final_manifest.json` to identify failing gates:
   - `marker_check_passed: false` → marker integrity lost.
   - `numerical_check_passed: false` → numerical mismatch.
   - `render_check_passed: false` → render output missing.
   - `critical_issues_remaining > 0` → unresolved quality issues.

2. Offer the user a targeted recovery choice:
   - **Retry gate** — re-dispatch the failing gate stage (e.g., re-run `merge_marker_check` if markers failed, re-run `render` if output missing).
   - **Skip gate with override** — only if the user explicitly confirms overriding the gate.
   - **Accept partial output** — if only `render` failed, offer `final_audit` accepts the merged translation text as final output.
   - **Abort** — stop the pipeline. Outputs preserved.

3. Hard gates remain non-skippable without user override: `marker_check`, `numerical_check`, `inspection`, `final_audit`.

## User Summary Rules

The main agent may summarize only after final audit passes.

The final user summary should include:

- source language;
- target language;
- domain;
- quality level;
- revision rounds;
- whether critical issues remain;
- numerical check status;
- marker check status;
- output file paths;
- important layout warnings.

## Knowledge Base Maintenance

The knowledge base is read-only and maintained manually. Pipeline workers consume existing knowledge bundles but never write back. LLM capabilities provide up-to-date domain knowledge for each job.

| Limit | Value | Behavior |
|-------|-------|----------|
| Max entries per glossary file | 5000 | Warning emitted in extraction manifest when exceeded |
| Stale pending/low entry auto-archival | 180 days | Entries with no update in 180 days auto-archived |
| Archived storage location | `knowledge/archived/{source}_{target}.json` | Preserved for recovery, not injected into workers |
| Conflicting entry review trigger | Detected in extraction | Flagged in manifest warnings[] for manual review |

Archived entries remain on disk in `knowledge/archived/` but are NOT included in bundle_glossary.json during knowledge_loading.
