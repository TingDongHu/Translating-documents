# Translating Documents — 文档翻译

[**English**](README.md) | Translating Documents — 文档翻译

基于文件的、质量受控的翻译管道，专为 [Claude Code](https://claude.ai/code) 设计。通过主编排器调度专业子代理，完成提取、知识加载、适配研究、并行翻译、专业术语研究、多轮质检、修订和最终审计——所有流程通过 JSON manifest 和经过校验的状态机协调。

## 特性

- **多格式支持** — DOCX、PPTX、XLSX、HTML、Markdown (.md)、纯文本 (.txt)
- **14 阶段标准化管道** — 提取 → 知识加载 → 适配研究 → 翻译（并行专业术语研究） → 标记完整性检查 → 数值检查 → 质检 → 修订 → 渲染 → 最终审计
- **3 个质量等级** — `standard`（标准）、`high`（高）、`professional`（专业级），使用声明式阶段映射表；数值零容忍检查在所有等级运行；修订按 critical 问题条件触发；专业级最多允许 2 轮修订
- **并行批量翻译** — 大文档自动拆分重叠批次，最多 3 个翻译子代理并发执行，每波次报告进度
- **多语言知识库** — 涵盖 24+ 种语言的领域规则、语言适应指南、文化参考和双语术语表：en、zh、ar、bn、da、de、es、fa、fi、fr、hi、hr、id、it、ja、ko、ms、nl、no、pl、pt、sv、th、tr、vi、mn
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

## 架构设计

### 设计理念

管道基于严格的**编排器-工作者**分离模式。主代理从不翻译、质检或修订——它只负责调度、读取轻量 JSON 状态文件、以及做流程决策。所有语言工作和脚本执行都委托给隔离的子代理。

这种设计的优势：
- **上下文隔离** — 每个子代理从零开始，阶段间不会产生幻觉传递
- **可审计** — 每个阶段都会写文件；完整的工作目录就是一条审计追溯链
- **确定性** — 确定性 Python 脚本处理结构化任务（提取、分块、标记检查、渲染）；LLM 判断力仅用于语言类任务

### 编排器

主代理以「读取-评估-调度」循环运行：

```
验证 workflow_state.json → 读取 manifests/scorecards →
  → 决定下一个阶段 → 调度子代理 →
  → 更新 workflow_state.json → 报告进度 → 重复
```

**主代理必须：**
- 收集源文件路径（仅 DOCX）、源/目标语言、领域和质量等级
- 创建隔离的任务目录，写入 `job_manifest.json` 和 `workflow_state.json`
- 在每次调度前通过 `validate_workflow_state.py` 验证工作流状态
- 每个阶段都调度子代理执行——绝不直接运行脚本或语言任务
- 每个阶段完成后更新 `workflow_state.json`
- 通过读取轻量 JSON 文件做流程决策（绝不通过聊天上下文传递完整报告）
- 每个阶段后报告进度；只有在最终审计通过后才做总结

**主代理禁止：**
- 直接翻译、修订、质检或撰写质量报告
- 直接运行管道脚本（必须通过脚本执行子代理）
- 将完整报告内容传入其他 worker 的提示
- 在最终审计通过前宣告完成

### 文件驱动的通信

所有阶段间的数据通过文件传递，绝不通过聊天上下文：

```
translation_job_{时间戳}_{源文件名}/
├── job_manifest.json              # 静态任务元数据（schema 校验）
├── workflow_state.json            # 管道状态的唯一可信源
├── extraction/
│   └── source_tagged.txt          # 带 [Pn] 标记的源文本
├── knowledge/
│   └── knowledge_manifest.json    # 知识文件的索引和章节偏移
├── translation/
│   ├── batch_001_translated.txt   # 每批的翻译结果
│   └── translated_merged.txt      # 合并后的完整译文
├── qa/
│   ├── marker_check.json          # 标记完整性门禁
│   ├── numerical_score.json       # 数值零容忍门禁
│   └── scorecard_round1.json      # 质检评分卡
├── revision/
│   └── revision_status_round1.json
├── render/
│   └── render_log.json            # 渲染状态
└── final/
    ├── final_manifest.json        # 最终门禁判定
    └── final_report.md            # 管道结果摘要
```

所有流程决策通过读取 JSON manifest 和 scorecard 完成。这使得每次运行都可复现、可调试——回放任务目录即可看到每个阶段发生的具体细节。

### 两种 Worker 类型

| | 脚本执行器 | 语言工作者 |
|---|---|---|
| **职责** | 执行 Python 管道脚本 | 执行基于 LLM 的语言判断任务 |
| **模板** | `workers/script_runner.md` | 特定 worker 模板（如 `workers/translator.md`） |
| **重试** | 3 次内部调试+重试 + 主代理层 + 用户层升级 | 通过重新调度重试 |
| **输出** | 退出码 + 输出文件的关键值 | 标准 JSON 报告格式：`{stage, status, outputs, metrics, warnings}` |
| **示例** | `extract_docx.py`, `check_markers.py`, `render_docx.py` | `translator.md`, `inspector.md`, `reviser.md` |

每个脚本执行器使用**全新的子代理**，确保调试循环不会污染主代理的上下文。

### 状态机

管道遵循标准的 14 阶段工作流：

```
initialized → extraction → prepare_knowledge → adaptation_research → translation
  → merge_marker_check → [numerical_check] → inspection_round1
  → [revision_round1] → [inspection_round2] → [revision_round2] → render → final_audit → completed
```

`[方括号]` 内的阶段根据质量等级条件执行。

`workflow_state.json` 追踪 `current_stage`、`completed_stages`、`stage_history`（含每条目的状态）、`blocked` 和 `requires_revision`。每次调度前，Python 校验脚本会根据 `workflow_state.schema.json` 和标准阶段列表检查状态。

### 质量等级阶段映射

| 阶段 | standard | high | professional |
|-------|----------|------|--------------|
| extraction | 运行 | 运行 | 运行 |
| prepare_knowledge | 运行 | 运行 | 运行 |
| adaptation_research | 运行 | 运行 | 运行 |
| translation | 运行 | 运行 | 运行 |
| professional_term_research | 运行（后台） | 运行（后台） | 运行（后台） |
| merge_marker_check | 运行 | 运行 | 运行 |
| numerical_check | 运行 | 运行 | 运行 |
| inspection_round1 | 运行 | 运行 | 运行 |
| revision_round1 | 跳过 | critical > 0 时 | critical > 0 时 |
| inspection_round2 | 跳过 | 已修订时 | 已修订时 |
| revision_round2 | 跳过 | 跳过 | 最多 2 轮，需用户批准 |
| render | 运行 | 运行 | 运行 |
| final_audit | 运行 | 运行 | 运行 |

### 质量门禁

管道禁止绕过的硬门禁：

- **标记检查** — 在进入 QA 前，所有 `[Pn]` 标签必须完整且正确配对
- **数值检查** — 零容忍：任何金额、日期或百分比的错误自动标记为严重（所有质量等级）
- **质检** — 没有 scorecard 不能进入修订；修订后未复审不能进入渲染
- **最终审计** — 所有门禁通过后管道才能报告完成

### 恢复架构

阶段失败时，系统通过三层升级：

1. **脚本执行器层** — 子代理内部诊断并重试最多 3 次（处理编码问题、缺失包、路径错误）
2. **主代理层** — 如果内部重试失败，主代理调度一个全新子代理再做一次 3 轮重试
3. **用户层** — 如果所有自动尝试都失败，主代理进入**阻塞通信协议**：报告阻塞原因，为用户提供 `[重试 / 跳过并记录原因 / 中止]` 选项

**批量翻译重试：** 当合并步骤检测到缺失批次时，仅重新调度缺失的批次——已翻译的批次保持不变。

**最终审计恢复：** 如果 `final_manifest.json` 报告 `status=blocked`，主代理诊断哪个具体门禁失败，并提供定向恢复选项（重试门禁、用户确认后跳过、接受部分输出、或中止）。

### 组件图

```
主编排器 (orchestrator)
  │
  ├── 脚本执行器 (Python 管道脚本)
  │   ├── extract_docx.py           — DOCX → 带 [Pn] 标记的纯文本
  │   ├── split_batches.py          — 批次拆分（含 [CONTEXT] 重叠区域）
  │   ├── merge_batches.py          — 批次合并（含缺失检测）
  │   ├── check_markers.py          — [Pn] 标签完整性门禁
  │   ├── check_numerics.py         — 数值零容忍检查
  │   ├── render_docx.py            — 带标签纯文本 → DOCX
  │   ├── final_audit.py            — 最终门禁验证 + 报告生成
  │   └── validate_workflow_state.py — 状态机校验
  │
  └── 语言子代理 (LLM subagents，通过提示模板调度)
      ├── 预处理:
      │   └── prepare_knowledge.py       — 索引知识库为 manifest（Python 脚本）
      ├── adaptation_researcher.md        — 研究源语言→目标语言适配规则（并行）
      ├── terminology_researcher.md       — 专业术语研究（与翻译并行）
      ├── translator.md                   — 翻译批次，保持 [Pn]/[CONTEXT] 标记
      ├── inspector.md                    — 6 维度质检评分（含术语扫描 + researcher 交叉核验）
      └── reviser.md                      — 根据质检报告修复问题
```

## 项目结构

```
translating-documents/
├── SKILL.md                       # 主编排器合约
├── README.md                      # 英文说明
├── README.zh.md                   # 中文说明
├── pipeline/
│   ├── scripts/                   # Python 管道脚本
│   └── templates/                 # JSON Schema 定义
├── workers/                       # 子代理提示模板
└── knowledge/                     # 多语言知识库
    ├── {lang}/                    # 24+ 语言目录
    │   ├── rules/                 # 写作规则和评分标尺
    │   ├── domain/                # 领域术语
    │   └── adapt/                 # 源语言到目标语言适应规则
    ├── culture/                   # 文化参考指南
    └── glossary/                  # 双语术语表（en_zh.json 等）
```

## 许可

MIT
