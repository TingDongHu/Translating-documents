---
id: sv/adapt/from_zh-CN
type: adapt
target_lang: sv
source_lang: zh-CN
name: "Swedish Adaptation Guide: Chinese → Swedish"
description: Chinese to Swedish language adaptation rules
---

# Swedish Adaptation Guide: Chinese to Swedish

This document provides comprehensive adaptation rules for translating Chinese
(simplified, zh-CN) content into Swedish (sv). It serves as a reference for
translators and automated adaptation pipelines, covering formality, numerals,
cultural references, terminology, administrative language, and punctuation.

---

## 1. Formality and Address

### 1.1 Pronouns: 您/你 → Ni/du

Chinese distinguishes formal address (您, nín) from informal address (你, nǐ).
Swedish has the same distinction but usage has shifted considerably.

| Chinese | Swedish (formal) | Swedish (informal) | Notes |
|---------|-------------------|---------------------|-------|
| 您 | Ni | du | Ni is declining; du is now standard in most workplaces |
| 你们 | Ni (plural) | ni | Ni (capitalised) was once the formal plural |
| 你 (informal) | du | ni | Use lowercase for informal plural |

**Guidelines:**

- **Business correspondence (new contacts):** Begin with "Ni" but switch to "du"
  once the relationship is established. Swedish business culture moved toward
  "du-reformen" (the du-reform) in the late 1960s, and today most companies
  use "du" from the first interaction.
- **Legal / official documents:** Use "Ni" for addressing parties where
  formality is required (court documents, government correspondence).
- **Marketing and UX copy:** Always use "du" — it is more natural and
  expected in Swedish digital contexts.
- **Internal company documents:** Use "du" unless the company style guide
  specifically mandates "Ni."

### 1.2 Title System

Chinese uses surname + title as a form of address (王总经理 → General Manager
Wang). Swedish follows a similar pattern but with different conventions:

| Chinese pattern | Swedish equivalent | Example |
|-----------------|---------------------|---------|
| 王总经理 | VD Wang / Generaldirektör Wang | Use Swedish title + surname |
| 李博士 | Dr. Lee / Doktor Lee | "Dr." or "Doktor" + surname |
| 张教授 | Professor Zhang | "Professor" + surname |
| 陈经理 | Chef Chen / Avdelningschef Chen | Use Swedish equivalent title |
| 刘工程师 | Ingenjör Liu | "Ingenjör" + surname |

**Key rules:**

- Swedish titles are rarely used as standalone forms of address in speech.
  In letters, use "Hej [Name]" or "Bästa [Name]" rather than "Hej Dr. Lee."
- In formal documents, title + surname is standard: "Professor Andersson."
- Never abbreviate Swedish titles in formal writing (use "Doktor" not "Dr."
  in formal contexts, though "Dr." is acceptable in academic circles).

### 1.3 Formal Closings

| Chinese closing | Swedish equivalent | Context |
|-----------------|---------------------|---------|
| 此致敬礼 | Med vänlig hälsning | Formal business letters |
| 此致敬礼 (very formal) | Vänliga hälsningar | Formal business letters |
| 祝好 | Med vänlig hälsning | Semi-formal |
| 顺祝商祺 | Med vänliga hälsningar | Business correspondence |
| 此致 | — | Not used as standalone in Swedish |
| 敬上 | [Name] | Just the name is sufficient in Swedish |

**Notes:**

- Swedish letter closings are less elaborate than Chinese ones. "Med vänlig
  hälsning" is the standard formal closing. "Vänliga hälsningar" is equally
  acceptable.
- For emails, "Med vänlig hälsning," "Vänliga hälsningar," or simply "Mvh"
  (abbreviation) are all common.
- Chinese closings often include well-wishes (祝身体健康). Swedish does not
  typically include such phrases in standard business correspondence. Omit
  them or translate as a brief, natural closing if context warrants it.

### 1.4 Subject Omission

Chinese frequently omits the subject when it is clear from context. Swedish
**requires** an explicit subject in most sentences.

| Chinese | Swedish |
|---------|---------|
| 已收到您的邮件 | Jag har mottagit ert e-postmeddelande / Vi har mottagit ert e-postmeddelande |
| 请尽快回复 | Vänligen svara snarast möjligt (no subject needed — imperative) |
| 正在处理中 | Det behandlas just nu / Vi behandlar det just nu |

**Rules:**

- Imperative sentences (requests, commands) often have no subject in Swedish
  either, so direct translation works: "Snälla svara" (Please reply).
- Declarative sentences must have an explicit subject. Determine whether the
  implied Chinese subject is first person (jag/vi), second person (du/Ni),
  or third person (han hon det den de) based on context.
- Passive constructions in Chinese (被/受 + verb) should be rendered as Swedish
  passive (see section 1.5).

### 1.5 Passive Voice: 被/受 → Swedish passive

Chinese uses 被 (bèi) and 受 (shòu) to form passive constructions. Swedish
has a productive passive formed with the -s suffix on the verb.

| Chinese active | Chinese passive | Swedish passive | Swedish active alternative |
|----------------|-----------------|------------------|---------------------------|
| 他批评了我 | 我被他批评了 | Jag kritiserades av honom | Han kritiserade mig |
| 政府批准了该计划 | 该计划被政府批准了 | Planen godkändes av regeringen | Regeringen godkände planen |
| 数据被删除了 | 数据被删除了 | Uppgifterna raderades | Någon raderade uppgifterna |

**Guidelines:**

- Swedish passive (-s suffix) is natural and preferred when the agent is
  omitted or unimportant: "Dokumentet har granskats" (The document has been
  reviewed).
- When the agent is important, Swedish often prefers active voice with a
  general subject: "Vi har granskat dokumentet" rather than "Dokumentet har
  granskats av oss."
- Avoid overusing passive in Swedish. It is generally less natural than in
  Chinese and should be used sparingly, mainly in formal/academic texts.
- 受 (shòu) constructions like 受欢迎 (popular) should be translated as
  active adjectives: "populär" rather than a passive construction.

---

## 2. Dates, Times, and Numbers

### 2.1 Date Format

Chinese dates follow year-month-day order (年月日). Swedish dates follow
day-month-year order.

| Chinese | Swedish | Notes |
|---------|---------|-------|
| 2025年1月15日 | 15 januari 2025 | Full format, no leading zeros |
| 2025年12月31日 | 31 december 2025 | |
| 2025年1月5日 | 5 januari 2025 | No leading zero on day |
| 2025/01/15 | 2025-01-15 | ISO format acceptable in technical contexts |
| 25年1月15日 | 15 jan 2025 | Abbreviated year is acceptable informally |

**Month names in Swedish:**

| English | Swedish |
|---------|---------|
| January | januari |
| February | februari |
| March | mars |
| April | april |
| May | maj |
| June | juni |
| July | juli |
| August | augusti |
| September | september |
| October | oktober |
| November | november |
| December | december |

**Day names:**

| English | Swedish |
|---------|---------|
| Monday | måndag |
| Tuesday | tisdag |
| Wednesday | onsdag |
| Thursday | torsdag |
| Friday | fredag |
| Saturday | lördag |
| Sunday | söndag |

### 2.2 Time Format

Chinese uses 12-hour or 24-hour time with periods (上午/下午). Swedish
overwhelmingly uses 24-hour format.

| Chinese | Swedish | Notes |
|---------|---------|-------|
| 下午3:30 | 15:30 | 24-hour format is standard |
| 上午9:00 | 09:00 | Leading zero on hours |
| 下午6:45 | 18:45 | |
| 凌晨2:00 | 02:00 | Late night / early morning |
| 中午12:00 | 12:00 | Noon — no special term needed |

**Time expressions:**

| Chinese | Swedish |
|---------|---------|
| 上午 | på morgonen / förmiddag |
| 下午 | på eftermiddagen / eftermiddag |
| 晚上 | på kvällen / kväll |
| 凌晨 | tidigt på morgonen / nattetid |
| 中午 | vid middagstid |

### 2.3 Numbers: 万/亿 Conversion

Chinese uses large number units of 万 (wàn = 10,000) and 亿 (yì = 100,000,000).
Swedish uses the standard Western system with thousands separators.

| Chinese | Numeric value | Swedish | Notes |
|---------|---------------|---------|-------|
| 1万 | 10,000 | 10 000 | Space as thousands separator |
| 35万 | 350,000 | 350 000 | |
| 100万 | 1,000,000 | 1 000 000 | "en miljon" |
| 1亿 | 100,000,000 | 100 000 000 | "hundra miljoner" |
| 35亿 | 3,500,000,000 | 3 500 000 000 | "tre och en halv miljard" |
| 13亿 | 1,300,000,000 | 1 300 000 000 | "en miljard och trehundra miljoner" |

**Rules:**

- Swedish uses spaces (not commas) as thousands separators: 1 000 000.
- Always convert 万 and 亿 into their full numeric equivalents.
- For very large numbers, Swedish words are preferred in running text:
  "tre miljarder" rather than "3 000 000 000."
- 千 (thousand) → use space-separated thousands or Swedish word "tusen."

### 2.4 Currency

| Chinese | Swedish | Notes |
|---------|---------|-------|
| 100元 | 100 CNY / 100 yuan | Keep CNY for financial contexts |
| 100元 (converted) | ca. 150 kronor | Approximate; check current rate |
| ¥100 | 100 CNY | Do not use ¥ in Swedish |
| 美元 | USD / amerikanska dollar | |
| 欧元 | EUR / euro | |

**Rules:**

- In business/financial documents, keep the original currency code (CNY,
  USD, EUR) with the amount.
- When conversion is appropriate or requested, use "kronor" (SEK) or
  "ca. [amount] kronor" for approximate values.
- Do not use the ¥ symbol in Swedish text — it is ambiguous (also used for
  Japanese yen). Use "CNY" or "yuan" instead.

### 2.5 Measure Words

Chinese requires measure words (量词) between numerals and nouns. Swedish has
no measure word system — use numeral + noun directly.

| Chinese | Swedish | Notes |
|---------|---------|-------|
| 三本书 | tre böcker | No measure word needed |
| 两台电脑 | två datorer | |
| 一个人 | en person / ett menneske | |
| 五条鱼 | fem fiskar | |
| 一匹马 | ett häst | |
| 三张纸 | tre ark papper | "ark" is the classifier but not obligatory |

**Note:** Some Swedish constructions use partitive or container nouns
similar to English (e.g., "ett glas vatten" = a glass of water), but these
are not obligatory classifiers as in Chinese.

### 2.6 Number Conventions Summary

| Feature | Chinese | Swedish |
|---------|---------|---------|
| Thousands separator | 逗号 , (rare) or none | Space (e.g., 1 000) |
| Decimal separator | 句号 . | Comma (e.g., 3,14) |
| Percentage | 百分之35 / 35% | 35 procent / 35 % |
| Ordinal prefix | 第 | -a/-e suffix (första, andra) |
| Negative numbers | 负 | minus |
| Phone numbers | 分组读 | Gruppera i 3s: 070-123 45 67 |

---

## 3. Cultural References and Idioms

### 3.1 Chinese 成语 (Chengyu) → Swedish Equivalents

Chinese 成语 (four-character idioms) often have direct Swedish equivalents
with similar meanings. When no equivalent exists, translate the meaning
explicitly.

| Chinese (chengyu) | Literal meaning | Swedish equivalent | Notes |
|--------------------|-----------------|---------------------|-------|
| 画蛇添足 | Draw a snake, add feet | att måla lejonet (to paint the lion) | Swedish: "måla lejonet" = doing something superfluous |
| 对牛弹琴 | Play the lute to a cow | att kasta pärlor för svin | Cast pearls before swine — identical meaning |
| 亡羊补牢 | Mend the pen after losing sheep | bättre sent än aldrig | Better late than never |
| 塞翁失马 | The old man lost his horse | varje olycka är god någonstans | Every cloud has a silver lining |
| 井底之蛙 | Frog at the bottom of a well | grodan i brunnen | Direct equivalent exists in Swedish |
| 守株待兔 | Wait by a tree stump for rabbits | att vänta vid floden efter en död fisk | Wait by the river for a dead fish — passive waiting |
| 自相矛盾 | Self-contradiction | att stå i konflikt med sig själv | Direct equivalent |
| 破釜沉舟 | Smash the pots and sink the boats | att bränna sina båtar | Burn one's boats — identical meaning |
| 画龙点睛 | Paint the dragon, dot the eyes | prippen på kaka | The icing on the cake — the final touch |
| 入乡随俗 | Enter a village, follow customs | when in Rome, do as the Romans do | Gör som romarna when in Rome |
| 一箭双雕 | One arrow, two hawks | att slå två flugor i en smäll | Kill two flies with one swat |
| 纸老虎 | Paper tiger | papperslöve | Direct equivalent (papperslöve) exists in Swedish |
| 黑马 | Dark horse | mörker häst / mörk häst | Dark horse — same concept exists |

### 3.2 Extended Idiom Reference

| Chinese | Swedish equivalent | Literal translation |
|---------|--------------------|---------------------|
| 塞翁失马焉知非福 | Olyckan kan vara en välsignelse i dold gestalt | Fortune and misfortune are two buckets in a well |
| 三个臭皮匠赛过诸葛亮 | Tre huvuden tänker bättre än ett | Three heads are better than one |
| 知己知彼百战不殆 | Känn dig själv och din fiende | Know yourself and your enemy |
| 老马识途 | En gammal häst känner vägen | An old horse knows the road |
| 狐假虎ٸ | Räven vinkar med den lilla ulven | The fox borrows the tiger's power |
| 画饼充饥 | Att måla bullar på väggen | Paint buns on the wall (empty promises) |
| 掩耳盗铃 | Att täppa för öronen och stjäla en klocka | Stop one's ears and steal a bell |
| 杯弓蛇影 | Att se en orm i skuggan av ett bågsvägg | See a snake in the shadow of a bow on the wall |

### 3.3 Cultural Context Notes

**When no direct equivalent exists:**

1. Translate the meaning explicitly rather than forcing an unnatural Swedish idiom.
   Example: 对牛弹琴 → "Det är som att kasta pärlor för svin" (full Swedish
   idiom) or simply explain: "försöka övertala någon som inte lyssnar" (trying
   to convince someone who won't listen).

2. For culturally specific Chinese references (festivals, customs, historical
   events), provide a brief parenthetical explanation on first occurrence:
   - 春节 (Chūn Jié) → "Kinesiska nyåret (Chūn Jié)"
   - 中秋节 → "Mitten av höstfesten (Zhōngqiū Jié)"

3. For literary references (四大名著, etc.), use established Swedish
   translations if they exist. If not, provide name + brief context.

---

## 4. Terminology and Technical Terms

### 4.1 Computing and Technology

| Chinese | Swedish | Notes |
|---------|---------|-------|
| 计算机 | dator | Not "datamaskin" (archaic) |
| 软件 | programvara | Not "mjukvara" (less common) |
| 硬件 | hårdvara | |
| 网络 | nätverk | |
| 互联网 | internet | Lowercase in Swedish |
| 电子邮件 | e-post | Not "mejl" in formal writing |
| 密码 | lösenord | Not "password" (anglicism) |
| 用户名 | användarnamn | |
| 数据库 | databas | |
| 网站 | webbplats | Not "hemsida" in formal contexts |
| 下载 | ladda ner | Two words, not "downloada" |
| 上传 | ladda upp | Two words, not "uploada" |
| 文件 | fil | |
| 文件夹 | mapp | |
| 打印机 | skrivare | Not "printare" (anglicism) |
| 键盘 | tangentbord | |
| 鼠标 | mus | Not "råtta" (literal translation) |
| 屏幕 | skärm | Not "skärm" + "display" redundancy |
| 应用程序 | applikation | "app" acceptable in informal contexts |
| 服务器 | server | |
| 云计算 | molnberäkning | |
| 人工智能 | artificiell intelligens | AI as abbreviation is also acceptable |
| 用户 | användare | |
| 界面 | gränssnitt | |
| 更新 | uppdatering | |
| 备份 | säkerhetskopia | "backup" acceptable in IT contexts |
| 错误 | fel | Not "felmeddelande" unless specifically an error message |
| 警告 | varning | |
| 配置 | konfiguration | |

### 4.2 General Technical Terms

| Chinese | Swedish | Notes |
|---------|---------|-------|
| 项目 | projekt | Not "projekt" (same spelling, check context) |
| 方案 | lösning / förslag | Context-dependent |
| 流程 | process / arbetsflöde | |
| 标准 | standard | |
| 系统 | system | |
| 数据 | data | "Data" is plural in Swedish |
| 信息 | information | "Information" is uncountable in Swedish |
| 功能 | funktion | |
| 性能 | prestanda | |
| 接口 | gränssnitt / anslutning | Depends on context |
| 安全 | säkerhet | |
| 模块 | modul | |
| 框架 | ramverk | |
| 部署 | distribution / utrullning | |
| 维护 | underhåll | |
| 测试 | test / provning | |
| 发布 | release / lansering | |
| 文档 | dokumentation | |

### 4.3 Industry-Specific Terms

| Domain | Chinese | Swedish |
|--------|---------|---------|
| Medical | 诊断 | diagnos |
| Medical | 处方 | recept |
| Medical | 手术 | operation |
| Legal | 合同 | kontrakt / avtal |
| Legal | 条款 | klausul / avtalspunkt |
| Legal | 仲裁 | skiljedom |
| Financial | 利率 | ränta |
| Financial | 资产 | tillgång |
| Financial | 负债 | skuld |
| HR | 劳动合同 | anställningsavtal |
| HR | 试用期 | provanställning |
| Marketing | 品牌 | varumärke |
| Marketing | 市场营销 | marknadsföring |

---

## 5. Administrative and Legal Language

### 5.1 Register and Tone

Chinese administrative and legal language is highly formal and formulaic.
Swedish legal/administrative language is also formal but less ornate. Aim
for clarity and precision rather than mimicking Chinese bureaucratic style.

| Chinese style | Swedish equivalent | Notes |
|---------------|---------------------|-------|
| Highly formal/bureaucratic | Saklig och formell (factual and formal) | Swedish law uses plain but formal language |
| Polite circumlocution | Direct statement | Swedish prefers directness even in formal contexts |
| Honorific prefixes | Omit or use title sparingly | Swedish legal language does not use honorifics |

### 5.2 Legal Formulas and Connectors

| Chinese | Swedish | Usage |
|---------|---------|-------|
| 根据 | i enlighet med / enligt | "In accordance with" |
| 鉴于 | med beaktande av / med hänsyn till | "Having regard to" |
| 特此 | härmed | "Hereby" — used to declare |
| 双方 | parterna | "The parties" |
| 一方 | en av parterna / den ena parten | "One of the parties" |
| 须 | ska | "Shall" (obligation) |
| 不得 | får inte | "Shall not" / "may not" |
| 应当 | bör / ska | "Should" (bör) or "shall" (ska) depending on strength |
| 有权 | har rätt att / är berättigad att | "Has the right to" |
| 无权 | har inte rätt att / är inte berättigad att | "Does not have the right to" |
| 负有义务 | är skyldig att | "Is obligated to" |
| 承担责任 | ansvarar för / är ansvarig för | "Is responsible for" |
| 违反 | bryter mot / överträder | "Breaches" / "violates" |
| 终止 | uppsäga / bringa till upphörande | "Terminate" |
| 不可抗力 | force majeure | Same term used in Swedish |

### 5.3 Contract Structure

| Chinese section | Swedish equivalent | Notes |
|-----------------|---------------------|-------|
| 首部 (preamble) | Inledning / Preamble | Contract header with parties and date |
| 条款 (clauses) | Avtalspunkter / Bestämmelser | Numbered contractual clauses |
| 附录 (appendices) | Bilagor | Supporting documents attached to contract |
| 定义 (definitions) | Definitioner | |
| 权利和义务 (rights and obligations) | Rättigheter och skyldigheter | |
| 违约责任 (liability for breach) | Ansvar för avtalsbrott | |
| 争议解决 (dispute resolution) | Tvistelösning | |
| 适用法律 (governing law) | Tillämplig lag | |
| 签署 (signature) | Underskrifter | |

### 5.4 Common Administrative Phrases

| Chinese | Swedish |
|---------|---------|
| 兹证明 | Härmed intygas / Härmed bekräftas |
| 特此通知 | Härmed meddelas |
| 特此批准 | Härmed godkänns |
| 请予审批 | Vänligen granska och godkänn |
| 请于...前回复 | Vänligen svar senast den [...] |
| 如有疑问，请联系 | Vid frågor, vänligen kontakta |
| 随函附上 | Bifogat finner ni / Som bifogat |
| 以上情况属实 | Ovanstående uppgifter är korrekta |
| 经双方协商一致 | Efter överenskommelse mellan parterna |
| 本合同一式两份 | Detta avtal upprättas i två exemplar |
| 各执一份，具有同等法律效力 | Varje part erhåller ett exemplar med lika juridiskt värde |

### 5.5 Government and Institutional Terms

| Chinese | Swedish | Notes |
|---------|---------|-------|
| 国务院 | Statsrådet | Swedish equivalent of cabinet |
| 人民代表大会 | Folkförsamlingen | People's assembly |
| 法院 | domstol | |
| 检察院 | åklagarmyndigheten | Prosecutor's office |
| 公安局 | polismyndigheten | Police authority |
| 工商行政管理局 | Bolagsverket / kommunen | Context-dependent |
| 税务局 | Skatteverket | Swedish Tax Agency |
| 海关 | Tullverket | Swedish Customs |

---

## 6. Punctuation

### 6.1 Full-Width vs. Half-Width

Chinese uses full-width punctuation (occupying the width of two characters).
Swedish uses standard half-width (Western) punctuation.

| Chinese punctuation | Swedish equivalent | Name | Notes |
|----------------------|---------------------|------|-------|
| ，（全角逗号） | , (half-width comma) | Comma | Always half-width |
| 。（全角句号） | . (half-width period) | Period/Full stop | Always half-width |
| ；（全角分号） | ; (half-width semicolon) | Semicolon | Always half-width |
| ：（全角冒号） | : (half-width colon) | Colon | Always half-width |
| ！（全角感叹号） | ! (half-width) | Exclamation mark | |
| ？（全角问号） | ? (half-width) | Question mark | |
| 、（顿号） | , (comma) | Serial comma | Use regular comma |
| （）（全角括号） | () (half-width) | Parentheses | Always half-width |
| 【】（全角方括号） | [] (half-width) | Square brackets | |
| 《》（全角书名号） | "" or '' (quotes) | Title marks | Use quotes for titles |
| ——（破折号） | — (en dash) | Dash | Single em dash, not double |
| ……（省略号） | ... (three periods) | Ellipsis | Three dots, not six |
| ・（中点） | · (middle dot) or - | Separator | Context-dependent |

### 6.2 Quotation Marks

| Chinese | Swedish | Usage |
|---------|---------|-------|
| ""（全角双引号） | "" (low-high quotation marks) | Primary quotes in Swedish |
| ''（全角单引号） | '' (single quotes) | Quotes within quotes |
| 「」（直角引号） | "" | Not used in standard Swedish |
| 『』（双直角引号） | '' | Not used in standard Swedish |

**Swedish quotation mark rules:**

- Primary quotation marks in Swedish are low opening: " and high closing: ".
  This differs from English " " and Chinese "".
- When quoting within a quote, use single quotation marks: "Han sa 'hej'."
- For titles of works, use italics in print or quotation marks in plain text.

### 6.3 Spacing Rules

| Rule | Chinese | Swedish |
|------|---------|---------|
| Space before punctuation | No (。！？) | Yes for some (: ! ?) — Swedish convention varies; no space before . , ; |
| Space after punctuation | No | Yes (standard Western spacing) |
| Space around dashes | No | Yes: word — word (with spaces around em dash) |
| Space after periods | Yes (full-width period) | Yes |
| Space between number and unit | No (35万) | Yes: 35 000, 35 %, 100 km |
| No-break space in numbers | N/A | Yes: 1 000 000 uses non-breaking spaces |

### 6.4 Chinese-Specific Punctuation Conversions

| Chinese construct | Swedish equivalent | Example |
|--------------------|---------------------|---------|
| 顿号列举（苹果、香蕉、橙子） | Comma-separated list | äpplen, bananer, apelsiner |
| 省略号（……） | Three dots with spaces | ... |
| 破折号解释（——即……） | Em dash with spaces | — det vill säga ... |
| 书名号（《红楼梦》） | Quotation marks or italics | "Drömmen om det röda rummet" |
| 直接引语（"你好"） | Low-high quotes | "Hej" |
| 间隔号（·，用于外国人名） | Space or hyphen | Jean-Paul Sartre |

### 6.5 Complete Punctuation Comparison Table

| # | Chinese | Unicode | Swedish | Unicode | Notes |
|---|---------|---------|---------|---------|-------|
| 1 | ， | U+FF0C | , | U+002C | Comma |
| 2 | 。 | U+3002 | . | U+002E | Period |
| 3 | ； | U+FF1B | ; | U+003B | Semicolon |
| 4 | ： | U+FF1A | : | U+003A | Colon |
| 5 | ！ | U+FF01 | ! | U+0021 | Exclamation |
| 6 | ？ | U+FF1F | ? | U+003F | Question mark |
| 7 | 、 | U+3001 | , | U+002C | Serial comma |
| 8 | "" | U+201C/U+201D | "" | U+201C/U+201D | Quotation marks |
| 9 | '' | U+2018/U+2019 | '' | U+2018/U+2019 | Single quotes |
| 10 | —— | U+2014 (doubled) | — | U+2014 (single) | Em dash |
| 11 | …… | U+2026 (doubled) | ... | U+002E (×3) | Ellipsis |
| 12 | （） | U+FF08/U+FF09 | () | U+0028/U+0029 | Parentheses |
| 13 | 《》 | U+300A/U+300B | "" | U+201C/U+201D | Title marks → quotes |
| 14 | 【】 | U+3010/U+3011 | [] | U+005B/U+005D | Square brackets |
| 15 | ～ | U+FF5E | – | U+2013 | Tilde → en dash (for ranges) |

---

## Appendix A: Quick Reference Checklist

When adapting Chinese content to Swedish, verify the following:

- [ ] **Pronouns:** Is the correct level of formality (du/Ni) chosen?
- [ ] **Titles:** Are Chinese titles converted to Swedish equivalents?
- [ ] **Dates:** Converted from 年月日 to dd month yyyy format?
- [ ] **Numbers:** 万/亿 fully converted? Space as thousands separator?
- [ ] **Currency:** Yuan/k yuan converted or coded as CNY?
- [ ] **Time:** 12-hour converted to 24-hour format?
- [ ] **Measure words:** Removed from numeral + noun constructions?
- [ ] **Idioms:** chengyu translated with Swedish equivalents or explanations?
- [ ] **Subjects:** All implicit Chinese subjects made explicit?
- [ ] **Passive voice:** 被/受 constructions converted to natural Swedish?
- [ ] **Punctuation:** All full-width characters replaced with half-width?
- [ ] **Quotation marks:** "" converted to Swedish "" (low-high)?
- [ ] **Spacing:** Proper spacing after punctuation and around dashes?
- [ ] **Technical terms:** Verified against Swedish computing/legal terminology?
- [ ] **Legal formulas:** 根据/鉴于/特此 converted to Swedish legal equivalents?

## Appendix B: Common Pitfalls

1. **Do not translate measure words literally.** Chinese 个/位/条 etc. have
   no Swedish equivalents. Just use numeral + noun: "三个朋友" → "tre vänner."

2. **Do not use full-width punctuation.** All punctuation must be half-width
   Western characters. Full-width characters will cause rendering issues.

3. **Do not confuse 万 with million.** 35万 = 350,000 (not 35 million).
   35万 = 350 000 in Swedish.

4. **Do not use English loanwords where Swedish terms exist.** Use "dator"
   not "computer," "programvara" not "software," "lösenord" not "password."

5. **Do not overuse passive voice.** Swedish passive (-s form) should be used
   sparingly. Prefer active voice where possible, especially in business
   communication.

6. **Do not translate 人民 literally.** In government context, translate
   according to Swedish institutional equivalents, not word-for-word.

7. **Watch for false friends.** 快速 (fast/quick) → "snabb" not "fort" (which
   is an adverb). 实际上 (actually) → "i själva verket" not "faktiskt" in
   formal contexts.

8. **Decimal and thousands separators.** Chinese uses . for decimals and , for
   thousands (sometimes). Swedish uses , for decimals and space for thousands.
   3.14 (Chinese) → 3,14 (Swedish). 1,000 (Chinese) → 1 000 (Swedish).

9. **Title marks.** 《》 must never appear in Swedish text. Convert to
   quotation marks or italics depending on context.

10. **Double punctuation.** Chinese sometimes doubles punctuation for emphasis
    or stylistic effect (！！！！). In Swedish, a single exclamation mark
    suffices. Multiple exclamation marks are considered unprofessional.
