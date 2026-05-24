---
id: zh/adapt/from_turkish
type: adaptation
target_lang: zh
source_lang: tr
name: 土耳其语→中文翻译适配规则
description: 将土耳其语行政/法律文件译为中文时的特殊处理策略
---

## 语言结构差异

### 土耳其语特点
- 黏着语：通过后缀表达语法关系（如 -nın 属格、-e 与格、-de 位格）
- 语序：主语-宾语-谓语 (SOV)，中文为 SVO，翻译时需要调整语序
- 长定语前置：土耳其语定语从句在被修饰词之前，中文需后置或用"的"字结构
- 无性别的第三人称代词 "o"：中文可译为"其/该人/此人"

### 被动语态
土耳其行政公文大量使用被动语态（-il/-ıl 后缀），中文应转换为：
- "tespit edilmiş olup" → "经查明……并"
- "anlaşılmıştır" → "已确认"
- "düzenlenmiş olup" → "系由……出具"
- 被动转主动或判断句："bulunduğu tespit edilmiştir" → "查明存在"

### 官方表达
土耳其语行政文件的特征表达：
- "Bilgi edinilmesini arz ederim." → "特此告知。" 或 "敬请知悉。"
- "Gereğini arz ederim." → "特此申请。" 
- "İLGİLİ MAKAMA" → "致相关机构"（不译为英文 "To whom it may concern" 对应的"敬启者"，行政公文用"致相关机构"）

## 词汇翻译策略

### 社保专有名词
- SGK (Sosyal Güvenlik Kurumu) → 社会保障机构（首次出现可加注 SGK）
- 4/a (SSK) → 第4条(a)项（受雇者保险）
- 4/b (Bağ-Kur) → 第4条(b)项（自雇人士保险）
- 4/c (Emekli Sandığı) → 第4条(c)项（公务员退休基金）
- 保留 4a/4b/4c 代码，首次出现时加括号注释

### 机构名称
- 全部大写机构名 → 中文正式名称
- "EMEKLİLİK HİZMETLERİ GENEL MÜDÜRLÜĞÜ" → "退休服务总局"
- "SOSYAL GÜVENLİK KURUMU BAŞKANLIĞI" → "社会保障机构主席办公室"

### 人名处理
- 土耳其人名保留原文拼写，不音译为中文
- Adı / Soyadı 格式保留，标注"姓名"即可
- 地名采用通用中文译名（İstanbul→伊斯坦布尔），小地名保留原文

### 数字和代码
- T.C. Kimlik No：保留为"T.C. 身份证号"
- Sicil No：社保登记号
- 4-digit codes (1479, 4690, etc.) 保留数字
- 月份格式 YYYY/MM 保留
- 土耳其里拉金额 → 标注 "TRY" 或"土耳其里拉"

## 表格翻译策略

### 表头
SGK 服务记录的列标题（缩写）：
- Sgrt Kolu → 保险类型
- Sgrt Kodu → 保险代码
- Statü → 身份/状态
- Sicil No → 登记号
- Meslek Kodu → 职业代码
- İşyeri/Kurum/Sandık No → 工作场所/机构/基金编号
- Ünite → 单位
- Dönem → 期间
- Belge Türü → 文件类型
- Belge Kd/Drc → 文件等级/状态
- Giriş Tarihi → 起始日期
- Gün → 天数
- PEK/Bsmk → 保费基数/收入阶梯
- Bsmk/ Gösterge → 阶梯/指标
- Çıkış Tarihi → 退出日期
- Eksik Gün → 缺勤天数
- İşten Çıkış Nedeni → 离职原因

### 汇总行
- "TOPLAM YYYY" → "YYYY年度合计"
- 汇总行中 Gün=0 保留原值（表示该年无缴费天数）

### 身份列内容
- "Şirket Ortağı" → "公司合伙人"
- "Terk Koduyla" → "以退出代码"（指以特定退出代码注销登记）
