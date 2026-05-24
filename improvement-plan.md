# Translating Documents Skill — 改进计划

基于对 1,446 段咖啡机说明书（中译英，专业级）的完整实践，提出以下改进项，按优先级排序。

---

## P0 — 大文档分块翻译（高优先级）

### 问题
当前整个文档（1,446 段/112KB）一次性发给翻译子代理。大文档容易触及上下文窗口上限，后半段翻译质量可能衰减。

### 方案
在 `SKILL.md` 的 Workflow > 1. Translate 中增加分块逻辑：

```
### 1. Translate (Large Document Mode)

如果源文档段落数 > 200 或字符数 > 30KB：
  1. 将标注后的源文本按章节或固定大小（如 200 段/批）分割
  2. 每批作为一个独立翻译任务发给子代理
  3. 每批翻译时携带前一批的最后 5 段作为上下文重叠（context overlap）
  4. 合并所有批次的翻译结果，验证 [Pn] 标记的连续性
```

### 文件修改
`SKILL.md` — Translate 章节新增 Large Document Mode 小节

---

## P1 — 领域知识文件去法文化（高优先级）

### 问题
`en/domain/technical.md`、`en/domain/commercial.md` 等文件的 `term_mappings` 全部是法文→英文映射（`notice d'utilisation`, `devis`, `savoir-faire` 等）。进行中译英时这些映射不适用，反而占用上下文。

### 方案
方案 A（推荐）：将 term_mappings 改为通用技术/商业术语，不绑定源语言。

```
# en/domain/technical.md 改进后
term_mappings:
  "user manual": "user manual"
  "specifications": "specifications"
  "spare part": "spare part"
  "component": "component"
  "tolerance": "tolerance"
```

方案 B：按源语言分支存放 — `en/domain/from_chinese/technical.md`、`en/domain/from_french/technical.md`。

### 文件修改
- `knowledge/en/domain/technical.md` — 替换 term_mappings 为通用术语
- `knowledge/en/domain/commercial.md` — 替换 term_mappings 为通用术语
- `knowledge/en/domain/administrative.md` — 同上
- `knowledge/en/domain/financial.md` — 同上
- `knowledge/en/domain/legal.md` — 同上

---

## P2 — 翻译进度报告（高优先级）

### 问题
翻译 1,446 段用时 3 分多钟，用户无可见进度。只能干等。

### 方案
在子代理调度模式中增加进度回调约定。在 `SKILL.md` 的 Subagent Dispatch Pattern 中新增：

```
### Progress Reporting (Large Documents)

当翻译文档段落数 > 200：
- 翻译子代理每完成一批（~200段），写一个临时进度文件
- 主 agent 定期检查进度文件，向用户输出：
  "翻译进度: 400/1446 (28%) — 已完成「菜单设置」章节"
```

### 文件修改
`SKILL.md` — 新增 Progress Reporting 小节

---

## P3 — 一致性检查与质检合并（中优先级）

### 问题
Consistency Checker 和 Inspector 存在功能重叠。这次实践中：
- Consistency Checker 发现 6 个问题
- Inspector 重新发现其中 4 个
- 两轮扫描同一份文档，浪费 token

### 方案
将两个角色重新分工：

```
### 2. Terminology Scan (原 Consistency Checker 精简版)
只做三件事：
- 提取源文中所有重复出现的术语
- 对照译文检查同一术语是否统一翻译
- 对照术语表检查合规性
输出：纯数据表（无评分、无建议）

### 3. Quality Inspection (原 Inspector 增强版)
基于 Terminology Scan 的数据表 + 完整原文译文做：
- 语义忠实度检查（逐段）
- 数值准确性检查（含零容忍清单）
- 格式规范性检查
- 完整性检查
- 综合评分
```

### 文件修改
- `knowledge/roles/consistency_checker.md` — 缩减为纯数据角色
- `knowledge/roles/inspector.md` — 吸收原 CC 的分析职责
- `knowledge/tasks/consistency_checker.md` — 对应调整
- `knowledge/tasks/inspector.md` — 对应调整
- `SKILL.md` — Workflow 章节合并 CC→Inspect 步骤

---

## P4 — 质检评分客观标尺（中优先级）

### 问题
六个维度评分靠子代理主观判断，不同运行结果可能差异很大。

### 方案
在 `knowledge/rules/scoring-rubric.md` 中新增评分细则：

```yaml
Numerical Accuracy:
  100: 所有数值、单位、日期完全匹配
  80: 1-2处数值格式不一致（如空格、单位大小写）
  60: 3-5处数值有误
  <40: 5处以上数值错误（一票否决，直接送修订）

Terminology Consistency:
  100: 所有术语统一，术语表 100% 遵守
  80: 1-2处术语不一致，但不影响理解
  60: 3-5处术语不一致或术语表违反
  <40: 系统性术语混乱

Semantic Fidelity:
  100: 无遗漏、无添加、无歧义
  80: 1-2处可接受的意译偏离
  60: 有遗漏句子或多余添加
  <40: 段落含义错误
  ...
```

### 文件修改
- 新增 `knowledge/en/rules/scoring-rubric.md`
- 新增 `knowledge/zh/rules/scoring-rubric.md`（中文翻译版，供从中文质检时使用）
- `SKILL.md` — Knowledge Loading 步骤增加可选加载评分标尺

---

## P5 — 修订后自动重建 DOCX（中优先级）

### 问题
当前 revise 步骤后只输出修订版译文文本，docx 不同步。

### 方案
在 `SKILL.md` 的 Revise 步骤末尾增加：

```
6. **Rerender DOCX**: After revision is complete, re-run the DOCX rendering 
   script (from Output → Rendering phase) with the revised translation to 
   produce an updated `{original_filename}_translated.docx`.
```

### 文件修改
`SKILL.md` — Workflow > 4. Revise 末尾追加步骤

---

## P6 — Professional 级别强制一轮修订（中优先级）

### 问题
当前决策逻辑是"有 critical 才 revise"。但对 professional 级别，即使 0 critical，warnings 也值得处理（用户需要主动要求全面检查才能发现这些问题）。

### 方案
修改 Decision point 逻辑：

```
**Decision point:**
- If quality level is **standard** → output, done.
- If quality level is **high** AND report has critical issues → proceed to Revise.
- If quality level is **professional**:
  - ALWAYS proceed to at least 1 round of revision (even if 0 critical issues)
  - Warnings and info items from the inspector are treated as revision targets
  - Max 2 rounds
```

### 文件修改
`SKILL.md` — Workflow > Inspect > Decision point

---

## P7 — 多领域加载标准化（低优先级）

### 问题
用户要求同时加载 technical + commercial 领域时，无标准流程，靠手动合并。

### 方案
修改 Knowledge Loading 的 Step 2：

```
### Step 2: Load domain rules (supports multiple domains)
- Domain can be a single value or an array: domain=technical or domain=[technical, commercial]
- For arrays, load ALL matching domain files in order
- Multiple domain rules are merged; if conflicting rules exist, the last-loaded domain takes priority
```

### 文件修改
`SKILL.md` — Before Starting > Domain 说明

---

## P8 — 自动构建中英术语表（低优先级）

### 问题
`glossary/zh_en.json` 不存在。这次翻译了 46 个部件名、20+ 按键名等高频术语，全部没有被收录，下次中译英无法复用。

### 方案
在翻译完成后增加 Glossary 自动构建：

```
### Glossary Auto-Build (first-time use)

If `glossary/{src}_{tgt}.json` does not exist:
1. After translation is complete, extract all recurring source terms (≥3 occurrences)
2. Map to their translations via the [Pn] alignment
3. Auto-generate the glossary file with high-confidence mappings
4. Write to `knowledge/glossary/{src}_{tgt}.json`
5. Inform user: "Auto-built glossary with {N} entries"
```

### 文件修改
`SKILL.md` — Output Details 之后新增一节

---

## 实施路线图

| 批次 | 内容 | 工作量估算 | 实际状态 |
|------|------|-----------|---------|
| **批1** | P0 大文档分块 + P2 进度报告 | 2 天 | P0：`split_batches.py` 的 `[CONTEXT]` overlap 机制已实现；P2：✅ 已实现（批级进度报告已加入 SKILL.md） |
| **批2** | P1 领域知识去法文化（5 个文件） | 1 天 | ⏸️ 已评估，待后续体系化更新知识库时一并处理 |
| **批3** | P3 合并 CC+Inspect + P4 评分标尺 | 2 天 | P3：已评估，两者分工合理无需合并；P4：✅ 评分标尺文件已存在，inspector 已强制使用标尺评分 + 标准报告模板 |
| **批4** | P5 修订后重建 DOCX + P6 Professional 强制修订 | 0.5 天 | 评估后无需改动：管道本身就是翻译修订结束后才 render DOCX；professional 级别多轮修订逻辑已满足需求 |
| **批5** | P7 多领域 + P8 自动术语表 | 1 天 | P7：✅ 已实现（domain 为 array 类型，knowledge_loader 逐 domain 加载）；P8：可选待定（terminology_researcher 已做任务级术语调研，写回永久术语表未实现） |
| **批6** | P9 基于源文内容的术语缺口分析 | 0.5 天 | ✅ 已实现——`terminology_research` 阶段在翻译前提取高频词、对照知识库/术语表、调研未覆盖术语，与 P9 方案一致 |

---

## P9 — 基于源文内容的术语缺口分析（高优先级）

### 问题
Knowledge Auto-Completion 只检查"文件是否存在"，不检查"文件内容是否覆盖了当前要翻译的术语"。比如之前翻译咖啡机说明书时，`technical.md` 存在所以没触发补全，但文件里并没有咖啡机相关的术语（豆仓、冲泡组、蒸汽棒等）。文件存在 ≠ 知识覆盖。

### 方案
在 Knowledge Loading 之后、Translate 之前，新增一个 **Terminology Gap Analysis** 步骤：

1. 从源文中提取高频领域术语（N≥3）
2. 对照已加载的知识库 + 术语表，检查哪些术语已有映射
3. 对未覆盖的术语，派发 research subagent 搜索权威译法
4. 生成 Supplementary Terminology Table 传递给 translator

### 文件修改
- `SKILL.md` — Workflow 新增 `### 0. Terminology Gap Analysis (pre-translate)` 步骤
- `SKILL.md` — Subagent Dispatch Pattern 新增 Supplementary Terminology 段落
