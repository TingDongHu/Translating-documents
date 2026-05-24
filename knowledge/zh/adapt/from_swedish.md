---
id: zh/adapt/from_swedish
type: adapt
target_lang: zh
source_lang: swedish
name: 瑞典语到中文适配
description: 瑞典语文档翻译为中文的目标语言特定适配规则
---

## 称呼和敬语

- 瑞典语正式书信使用简洁、直接的语气，不使用法语式的过度客套
- "Till den det vederbör" → "致相关人员" 或 "致相关方"
- "Vänliga hälsningar" → "此致敬礼" 或 "顺致敬意"
- "Jag får härmed bekräfta att..." → "兹确认……"
- 瑞典语无敬语敬称（无 vous/tu 区分），直接翻译为当代中文正式语气即可

## 法律和行政术语

- "Notarius Publicus" → 保留原文"Notarius Publicus"并加注"（公证人）"，或直接译为"公证人"
- "Apostille" → "附加证明书"（海牙公约术语）或保留"Apostille"
- "exp. nr." → "签章编号" 或 "证件编号"
- "utfärdats" → "签发"
- "bekräftelse" → "确认" 或 "证明"
- "denna dag" → "本日" 或 "于即日"

## 公证书格式适配

- 瑞典公证文书格式简洁，翻译为中文时保持简洁风格
- "Ang."（Angående）→ "事由：" 或 "关于"
- "Org. no." → "机构编号"
- "Registrerat kontor" → "注册办事处"
- "Mobil nr." → "手机号码"

## 数字和日期格式

- 瑞典日期 "den 20 maj 2026" → "2026年5月20日"
- 瑞典电话号码保留原格式：+46 738 39 30 08
- 瑞典机构编号保留原格式：556964-6374
- 瑞典邮编和地址的地名部分保留原文

## 地址和地名

- 街道名音译为中文 + "号"，保留门牌号数字
  - 示例：Jan Waldenströms gata 47 → 扬·瓦登斯特伦斯嘎塔 47 号
  - 示例：Celsiusgatan 13 A → 塞尔修斯嘎坦 13 A
  - 示例：Malmöhusvägen 1 → 马尔默胡斯韦根 1 号
- 瑞典地名使用通用中文译名：
  - Malmö → 马尔默
  - Stockholm → 斯德哥尔摩
  - Göteborg → 哥德堡
  - Lund → 隆德
  - Sverige → 瑞典
- 邮编保留原格式：SE-21118 Malmö → SE-21118 马尔默

## 商业实体名称和人名

- 人名音译为中文名，格式为 `音译中文名（原文）`
  - 示例：Malin Liljenberg → 玛琳·利延贝里（Malin Liljenberg）
  - 示例：Kristian Jonsson → 克里斯蒂安·约恩松（Kristian Jonsson）
- 品牌名音译为中文名 + 原文括号 + 实体类型翻译
  - 示例：Notar Advokatbyrå → 诺泰（Notar）律师事务所
- "AB"（Aktiebolag）→ 保留"AB"
- "Advokatbyrå" → "律师事务所"

## OCR 修正策略

- 瑞典语变音符号丢失时（ä→a, ö→o, å→a），根据上下文还原
- "Malmo" → "Malmö"（马尔默）
- "Vanliga"（意为"普通的"）在书信结尾中应为 "Vänliga"（意为"友好的"→"Vänliga hälsningar"）
- "Bekraftelse" → "Bekräftelse"（确认）
- "utfardats" → "utfärdats"（签发）
- 使用 `[推断: ...]` 标记所有 OCR 修正

## 瑞典语语法特点

- 瑞典语动词无变位，翻译时不受困扰
- 瑞典语定冠词后置（如 "dokumentet" = "the document"），翻译时不产生影响
- 瑞典语"härmed" = 英文 "hereby"，在正式文书中翻译为"兹"或"特此"
- 瑞典语"denna" = 英文 "this"，在法律文书中常用于指代当前文件或日期
