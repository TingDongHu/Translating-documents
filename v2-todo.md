# Translating Documents — v2 待解决问题

## 1. 端到端集成测试

当前缺少快速验证全管道连通性的手段。改了一个脚本的接口参数，无法在 CI 层面发现。

**方向：**
- 编写一个测试用的小型 DOCX 文件（3-5 段）
- 为每个 pipeline 脚本编写单元测试（assert 输入/输出契约）
- 编写一个端到端的集成测试脚本，从 extraction 到 final_audit 全流程跑通
- 集成到 CI（如 GitHub Actions）

## 2. 主 agent 同步阻塞

dispatch subagent 后必须等全部返回，超长文档时用户看不到批次内部实时进展。

**方向：**
- 评估 subagent 异步回调的可行性
- 或在前端实现 polling 机制，定时读取进度文件
- 批级进度报告已缓解但未完全解决

## 3. 术语发现易失

terminology_researcher 调研出的术语映射在任务结束后丢失，不会回写为永久资产。

**方向：**
- 翻译完成后，从源文-译文对齐中提取高置信度术语映射
- 追加写入 `knowledge/glossary/{source}_{target}.json`
- 需要设计置信度阈值和冲突解决策略

## 4. 单文件入口

只支持 DOCX，不支持 MD、PPTX、XLIFF 等译者常用格式。

**方向：**
- 抽象 extract/render 接口，按格式实现插件
- 支持 Markdown 输入输出（最低成本扩展）
- 支持 XLIFF（翻译行业标准交换格式）

## 5. worker 缺乏超时和降级

translator subagent 超时（如上下文窗口溢出）时，只有重试，没有自动降级策略。

**方向：**
- 实现超时检测（subagent 超时后自动终止）
- 自动减小 batch size 重新 dispatch
- 记录降级事件到 workflow_state
