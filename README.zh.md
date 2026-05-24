# Translating Documents — 文档翻译

基于文件的、质量受控的 DOCX 翻译管道，专为 [Claude Code](https://claude.ai/code) 设计。通过主编排器调度专业子代理，完成提取、术语研究、并行翻译、多轮质检、修订和最终审计——所有流程通过 JSON manifest 和经过校验的状态机协调。

## 特性

- **14 阶段标准化管道** — 提取 → 知识加载 → 术语研究 → 翻译 → 标记完整性检查 → 数值检查 → 术语扫描 → 质检 → 修订 → 渲染 → 最终审计
- **3 个质量等级** — `standard`（标准）、`high`（高）、`professional`（专业级），使用声明式阶段映射表；专业级强制数值零容忍检查、修订和复审
- **并行批量翻译** — 大文档自动拆分重叠批次，最多 3 个翻译子代理并发执行，每波次报告进度
- **多语言知识库** — 涵盖 en、zh、fr、pt、mn、tr、sv 的领域规则、语言适应指南、文化参考和双语术语表
- **评分标尺** — 6 个质检维度（数值准确性、术语一致性、语义忠实度、格式规范性、完整性、推断/OCR 质量），每维度 5 档评分标准
- **恢复协议** — 3 层重试升级机制、阻塞通信协议、批量重译、最终审计恢复（含定向门禁诊断）
- **JSON Schema 校验** — 所有 manifest、scorecard、状态文件在阶段分发前均经过 schema 校验

## 系统要求

- Python 3.10+
- [python-docx](https://pypi.org/project/python-docx/) — DOCX 提取和渲染
- [lxml](https://pypi.org/project/lxml/) — DOCX 文件 XML 处理

安装依赖：

```bash
pip install python-docx lxml
```

## 安装

将仓库克隆到 Claude Code 的技能目录：

```bash
git clone https://github.com/TingDongHu/Translating-documents.git ~/.claude/skills/translating-documents
```

下次启动 Claude Code 时技能会自动发现。通过描述翻译任务或使用 `/translating-documents` 来调用。

## 使用方法

向 Claude Code 描述你的文档翻译需求，技能会引导你完成必要参数：

1. **源语言** — 输入文档的语言
2. **目标语言** — 期望的输出语言
3. **领域** — 一个或多个：`general`（通用）、`legal`（法律）、`financial`（金融）、`commercial`（商务）、`administrative`（行政）、`technical`（技术）
4. **质量等级** — `standard`（标准）、`high`（高）、`professional`（专业级）

示例提示：

```
把这份中文合同翻译成英文，商务领域，专业级质量。
```

管道会创建独立的任务目录，并在每个阶段完成后报告进度：

```
[extraction] done — 622 tagged entries (9 body, 601 table, 6 header, 6 footer)
[translation] progress — batches 1-3/6 complete (3/6 batch)
[translation] done — 622 tags translated across 6 batches
[merge_marker_check] done — passed, no missing or extra tags
[inspection_round1] done — score 87, 1 critical, 4 warnings, revision required
[revision_round1] done — 5 issues addressed, 0 unresolved
[final_audit] done — all gates passed
```

## 管道概览

### 工作流

```
initialized → extraction → knowledge_loading → terminology_research → translation
  → merge_marker_check → [numerical_check] → terminology_scan → inspection_round1
  → [revision_round1] → [inspection_round2] → [revision_round2] → render → final_audit → completed
```

`[方括号]` 内的阶段根据质量等级条件执行。

### 质量等级映射

| 阶段 | standard | high | professional |
|-------|----------|------|--------------|
| extraction | 运行 | 运行 | 运行 |
| knowledge_loading | 运行 | 运行 | 运行 |
| terminology_research | 运行 | 运行 | 运行 |
| translation | 运行 | 运行 | 运行 |
| merge_marker_check | 运行 | 运行 | 运行 |
| numerical_check | 跳过 | 跳过 | 强制 |
| terminology_scan | 运行 | 运行 | 运行 |
| inspection_round1 | 运行 | 运行 | 运行 |
| revision_round1 | 跳过 | critical > 0 时 | 强制 |
| inspection_round2 | 跳过 | 已修订时 | 强制 |
| revision_round2 | 跳过 | 跳过 | 最多 2 轮 |
| render | 运行 | 运行 | 运行 |
| final_audit | 运行 | 运行 | 运行 |

### 架构

```
主编排器 (orchestrator)
  ├── 脚本执行器 (Python 管道脚本)
  │   ├── extract_docx.py       — DOCX → 带标签纯文本
  │   ├── split_batches.py      — 批次拆分（含 [CONTEXT] 重叠区域）
  │   ├── merge_batches.py      — 批次合并（含缺失检测）
  │   ├── check_markers.py      — [Pn] 标签完整性门禁
  │   ├── check_numerics.py     — 数值零容忍检查
  │   ├── render_docx.py        — 带标签纯文本 → DOCX
  │   ├── final_audit.py        — 最终门禁验证 + 报告生成
  │   └── validate_workflow_state.py — 状态机校验
  └── 语言子代理 (LLM subagents)
      ├── knowledge_loader.md   — 知识加载
      ├── terminology_researcher.md — 术语研究
      ├── translator.md         — 翻译
      ├── consistency_checker.md — 一致性检查
      ├── inspector.md          — 质量检查
      └── reviser.md            — 修订
```

## 项目结构

```
translating-documents/
├── SKILL.md                       # 主编排器合约
├── improvement-plan.md            # 改进历史和路线图
├── v2-todo.md                     # 未来开发候选
├── README.md                      # 英文说明
├── README.zh.md                   # 中文说明
├── pipeline/
│   ├── scripts/                   # Python 管道脚本
│   └── templates/                 # JSON Schema 定义
├── workers/                       # 子代理提示模板
└── knowledge/                     # 多语言知识库
    ├── {lang}/
    │   ├── rules/                 # 写作规则和评分标尺
    │   ├── domain/                # 领域术语
    │   └── adapt/                 # 源语言到目标语言适应规则
    ├── culture/                   # 文化参考指南
    └── glossary/                  # 双语术语表
```

## 许可

MIT
