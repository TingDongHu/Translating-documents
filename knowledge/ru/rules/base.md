---
id: ru/rules/base
type: rules
target_lang: ru
name: Правила перевода на русский язык
description: Базовые правила перевода документов на русский язык
---

## 1. Number Format

- **Decimal separator: comma (,)** — In Russian, the decimal separator is always a COMMA, never a period.
  - `1.5` → `1,5`
  - `3.14159` → `3,14159`
  - `99.9%` → `99,9 %`
  - `0.05` → `0,05`

- **Thousands separator: non-breaking space ( )** — Group digits by 3 using a non-breaking space, not a comma or period.
  - `1,234,567` → `1 234 567`
  - `1000000` → `1 000 000`
  - `15000.50` → `15 000,50`
  - `9999999` → `9 999 999`

- **Percentage format: space before %** — A non-breaking space always precedes the percent sign.
  - `15%` → `15 %`
  - `99,9%` → `99,9 %`
  - `10-15%` → `от 10 до 15 %`
  - `5% increase` → `увеличение на 5 %`

- **Negative numbers: minus sign (−) or parentheses**
  - In running text, use the true minus sign (−): `−5 °C`, `−3,5 %`
  - In tables and accounting, parentheses are also common: `(5)`, `(1 234)`
  - Do NOT use a regular hyphen (-) for negative numbers
  - `-10` → `−10` (in text) or `(10)` (in tables)

- **Ranges (диапазоны)**
  - Use "от X до Y" in running text: `от 5 до 10`, `от 20 до 30 %`
  - Use an en-dash (–) without spaces for compact ranges in parentheses/tables: `5–10`, `20–30 %`
  - `pages 10-20` → `стр. 10–20`
  - `3-5 days` → `от 3 до 5 дней`
  - Do NOT use a hyphen for numeric ranges; use an en-dash (–)

- **Fractions and decimal fractions**
  - `1/2` → `½` (where typographic fraction available) or `1/2`
  - `1.5 million` → `1,5 млн`
  - `0.5 billion` → `0,5 млрд`

- **Ordinal numbers**
  - In Russian, ordinals use a period after the number: `1.` (первый), `2.` (второй)
  - `1st quarter` → `1-й квартал` or `I квартал`
  - `Page 5` → `Стр. 5`
  - `Chapter 3` → `Глава 3`
  - When using digit + grammatical ending: `1-й`, `2-я`, `3-е`, `10-го`

## 2. Currency

- **Symbol position: AFTER the amount, separated by a space**
  - `€100.00` → `100,00 €`
  - `$1,234.56` → `1 234,56 $`
  - `₽500` → `500 ₽`
  - `£99.99` → `99,99 £`

- **Currency names in Russian**
  - `€` → евро (indeclinable neuter noun: евро, of евро, to евро, etc.)
  - `$` → доллар (доллара, долларов, etc.)
  - `₽` / `руб.` → рубль (рубля, рублей, etc.)
  - `£` → фунт стерлингов
  - `¥` → иена (Japanese yen) / юань (Chinese yuan)
  - `CHF` → швейцарский франк

- **Currency abbreviations**
  - `100 USD` → `100 долл. США` or `100 $`
  - `50 EUR` → `50 евро`
  - `200 RUB` → `200 руб.` or `200 ₽`
  - In technical/financial documents, ISO codes (RUB, USD, EUR) are acceptable
  - In general text, use Russian names: рублей, долларов, евро

- **Example conversions**
  - `€1,500.50` → `1 500,50 €`
  - `$1,000,000` → `1 000 000 $` or `1 млн долларов`
  - `₽500.00` → `500,00 ₽`

## 3. Date and Time

- **Date format: ДД.ММ.ГГГГ** (day.month.year with dots, no spaces)
  - `03/15/2024` → `15.03.2024` (not 03/15/2024 or 15/03/2024)
  - `2024-05-10` → `10.05.2024`
  - `01/02/2023` → `02.01.2023` (2 January, not 1 February)
  - `Jan 5, 2024` → `05.01.2024`
  - Single-digit day/month: always two digits: `01.03.2024`, not `1.3.2024`

- **Written-out dates: month names in Russian**
  - `March 15, 2024` → `15 марта 2024 года`
  - `January 1` → `1 января`
  - `September 2023` → `сентябрь 2023 года`

- **Month names (genitive form used after dates)**
  - январь → января (January)
  - февраль → февраля (February)
  - март → марта (March)
  - апрель → апреля (April)
  - май → мая (May)
  - июнь → июня (June)
  - июль → июля (July)
  - август → августа (August)
  - сентябрь → сентября (September)
  - октябрь → октября (October)
  - ноябрь → ноября (November)
  - декабрь → декабря (December)

- **Time format: 24-hour (15:30)**
  - `3:30 PM` → `15:30`
  - `12:00 AM` → `00:00`
  - `9:45 AM` → `9:45` or `09:45`
  - `6:00 PM` → `18:00`
  - Time separator is colon (:), never period
  - Leading zero for hours is optional but recommended: `09:00` not `9:00`
  - Do NOT use AM/PM notation

- **Time ranges**
  - `10:00 AM - 12:00 PM` → `с 10:00 до 12:00`
  - `9:00-5:00` → `с 9:00 до 17:00`

- **Week/day combinations**
  - `Monday, June 5` → `понедельник, 5 июня`
  - `Friday 13th` → `пятница, 13-е`

- **Weekday names**
  - Monday → понедельник
  - Tuesday → вторник
  - Wednesday → среда
  - Thursday → четверг
  - Friday → пятница
  - Saturday → суббота
  - Sunday → воскресенье

## 4. Addresses

- **Russian address order** (largest → smallest unit):
  `страна → почтовый индекс → город → улица → дом → квартира`

- **Standard format:**
  `Россия, 101000, г. Москва, ул. Тверская, д. 1, кв. 5`

- **Component abbreviations:**
  - г. = город (city)
  - ул. = улица (street)
  - пр. = проспект (avenue)
  - пер. = переулок (lane)
  - д. = дом (building)
  - к. / корп. = корпус (building block)
  - кв. = квартира (apartment)
  - стр. = строение (structure)
  - обл. = область (region / oblast)
  - р-н = район (district)
  - пос. = посёлок (settlement)
  - дер. = деревня (village)

- **Examples:**
  - `123 Main St, Apt 4, New York, NY 10001` → `США, 10001, г. Нью-Йорк, ул. Мейн, д. 123, кв. 4`
  - `10 Downing Street, London SW1A 2AA` → `Великобритания, SW1A 2AA, г. Лондон, ул. Даунинг-стрит, д. 10`

- **International addresses**: When the original address is in a foreign country, keep the original place names but structure them according to Russian address conventions (largest → smallest).

## 5. Proper Nouns

- **Foreign personal names**
  - In technical/business documents: prefer to keep the original Latin spelling in parentheses after the Russian transliteration
  - First mention: `Джон Смит (John Smith)`
  - Subsequent mentions: `Дж. Смит` or `Джон Смит`
  - Use standard Russian transliteration rules (not phonetic free-for-all)
  - `Эмма Уотсон (Emma Watson)`
  - `Михаэль Шумахер (Michael Schumacher)`

- **Company names**
  - Keep the original registered name whenever possible
  - Add Russian translation or description in parentheses for clarity on first mention
  - `Apple Inc.` → `Apple Inc. (компания «Эппл»)`
  - `Microsoft Corporation` → `Microsoft Corporation (корпорация «Майкрософт»)`
  - `Газпром` → remains `Газпром` (Russian company, no change)
  - Do NOT translate company names unless an official Russian name exists

- **Chinese names: Palladius system (Система Палладия)**
  - Use the standard Palladius Cyrillic transliteration for Chinese names
  - `习近平` → `Си Цзиньпин`
  - `北京` → `Пекин` (established name) / `Бэйцзин` (direct transliteration)
  - `上海` → `Шанхай`
  - `广州` → `Гуанчжоу`
  - Keep the original Chinese characters or pinyin in parentheses on first mention if helpful

- **Product names / trademarks**
  - Always preserve the original trademark spelling
  - Do NOT translate trademarked names
  - `iPhone 15` → `iPhone 15` (not Айфон 15)
  - `Windows 11` → `Windows 11`
  - Exception: brands with established Russian names: `Coca-Cola` → `Кока-Кола`

- **Geographic names**
  - Use established Russian names where they exist
  - `Germany` → `Германия` (not «джермани»)
  - `Paris` → `Париж`
  - `London` → `Лондон`
  - `New York` → `Нью-Йорк`
  - `Beijing` → `Пекин`
  - For lesser-known places, use transliteration and keep original in parentheses

- **Legal entity forms translation**
  - `LLC` → `ООО` (Общество с ограниченной ответственностью)
  - `Inc.` → `корпорация`
  - `GmbH` → `ООО`
  - `Ltd.` → `ООО` or `Лтд`
  - `PLC` → `ПАО` (Публичное акционерное общество)
  - `S.A.` → `АО`

## 6. Punctuation

- **Quotation marks: «кавычки-ёлочки» (guillemets)**
  - Primary quotes: « » (guillemets, pointing outward)
  - `"Hello"` → `«Здравствуйте»`
  - `He said "come here"` → `Он сказал: «Подойдите сюда»`
  - Nested quotes: „ " (German-style inverted commas)
  - `He said "she told me 'come'"` → `Он сказал: «Она сказала мне: „Подойди"»`
  - Do NOT use "Straight quotes" or "curly quotes" (") for primary quotation in Russian

- **Dashes: em dash (—) for many uses**
  - Subject-predicate dash: `Москва — столица России.`
  - In lists: `— пункт первый` (bullet list item)
  - Parenthetical phrases: `Этот документ — как вы уже знаете — требует внимания.`
  - Dialogue: `— Здравствуйте, — сказал он.`
  - The em dash in Russian is always surrounded by thin spaces or regular spaces
  - Do NOT use hyphen (-) or en-dash (–) where Russian typography requires em dash (—)

- **Non-breaking space rules**
  - Between single-letter prepositions and following word: `в стране`, `на работе`
  - Before long dashes in running text (when dash is between words)
  - Between number and unit: `10 кг`, `5 м`
  - Between number and percent: `15 %`
  - Inside initials: `А. С. Пушкин` (spaces between initials)
  - After opening and before closing guillemets: « текст »

- **Semicolon usage**
  - Used in complex lists, especially when list items contain commas
  - `В отчете приведены данные по трем регионам: Москве, Московской области; Санкт-Петербургу, Ленинградской области; Краснодару, Краснодарскому краю.`
  - More common in Russian than in English for separating compound list items

- **Comma usage differences from English**
  - Russian uses a comma before `что` (that): `Я знаю, что это важно.`
  - Russian uses a comma before `как` in comparisons: `Он большой, как дом.`
  - Russian does NOT use a serial/Oxford comma before `и` in a list of three+: `яблоки, груши и бананы` (no comma before и)
  - Russian uses a comma before `а` (contrasting conjunction): `не сегодня, а завтра`

- **Period in abbreviations**
  - `и т.д.` (etc.), `и т.п.` (and so forth), `т.е.` (i.e.), `и др.` (and others)
  - `г.` (year/city), `стр.` (page), `рис.` (figure)
  - Abbreviations always take a period in Russian

## 7. Formatting

- **Heading hierarchy**: Preserve all heading levels (#, ##, ###) exactly as in the source. Do NOT flatten or re-level headings.
  - `# Chapter 1` → `# Глава 1`
  - `## Introduction` → `## Введение`
  - `### 1.1 Background` → `### 1.1 Предыстория`

- **List formatting: em dash (—) for bulleted lists**
  - Do NOT use asterisks (*), hyphens (-), or plus (+) for bullet lists in Russian typography
  - Preferred: `— первый пункт` (em dash + space + text)
  - `— Второй пункт списка`
  - `— Третий пункт`

- **Numbered lists**: Keep Arabic numerals with period
  - `1. Первый пункт`
  - `2. Второй пункт`
  - If items within a numbered list contain multiple sentences, capitalize the first word of each item

- **Table structure**: Preserve all table boundaries and cell alignment
  - Translate content cell by cell
  - Keep column headers translated
  - Preserve row/column span
  - Do NOT merge or split cells unless absolutely required by text length

- **Paragraph breaks**: Maintain the same paragraph divisions as the source
  - Do NOT merge paragraphs
  - Do NOT split a single paragraph into multiple unless the translation is significantly longer

- **Bold/italic formatting**
  - Preserve all emphasis formatting (**bold**, *italic*)
  - In Russian typography, bold is preferred for titles; italic for emphasis within text
  - Avoid using ALL CAPS for emphasis — Russian uses italic or spacing instead

- **Footnotes and endnotes**: Preserve all note markers and position

## 8. Grammar

- **Six grammatical cases (6 падежей)**
  When translating, ensure nouns, adjectives, and pronouns agree in case with their grammatical role:

  | Case | Russian name | Example (дом) | Usage |
  |------|-------------|---------------|-------|
  | Nominative | именительный | дом | Subject |
  | Genitive | родительный | дома | Possession, negation, after "нет" |
  | Dative | дательный | дому | Indirect object, recipient |
  | Accusative | винительный | дом | Direct object |
  | Instrumental | творительный | домом | Means, with "with" |
  | Prepositional | предложный | доме | Location, after "о", "в", "на" |

  - `I see a house` → `Я вижу дом` (accusative = nominative for inanimate masculine)
  - `No house` → `Нет дома` (genitive after negation)
  - `In the house` → `В доме` (prepositional for location)

- **Verb aspect (вид глагола)**
  - Совершенный вид (perfective) — completed action, single result
  - Несовершенный вид (imperfective) — ongoing, repeated, habitual action
  - `I wrote a letter (and finished)` → `Я написал письмо` (perfective)
  - `I was writing a letter` → `Я писал письмо` (imperfective)
  - `I used to write` → `Я писал (каждый день)` (imperfective, habitual)
  - Choose the correct aspect based on context — this is critical for natural Russian

- **Gender-number agreement (согласование в роде и числе)**
  - Adjectives, past-tense verbs, and some numerals must agree with the noun
  - `новый дом` (masculine), `новая книга` (feminine), `новое окно` (neuter)
  - `новые дома` (plural)
  - `Он пришёл` (male), `Она пришла` (female)
  - Pay special attention when the source language has no gender marking

- **Verbs of motion (глаголы движения)**
  - Russian has a complex system of motion verbs with directionality and aspect:
  - Unidirectional: `идти` (to go on foot, one direction)
  - Multidirectional: `ходить` (to go on foot, multiple directions / habitual)
  - `I am going to work (right now)` → `Я иду на работу` (unidirectional)
  - `I go to work (every day)` → `Я хожу на работу` (multidirectional, habitual)

- **Prepositional government (управление предлогов)**
  - Each preposition governs a specific case:
  - `без + genitive`: `без воды` (without water)
  - `для + genitive`: `для работы` (for work)
  - `к + dative`: `к дому` (toward the house)
  - `с + instrumental`: `с другом` (with a friend)
  - `о + prepositional`: `о работе` (about work)
  - Use a case-checking reference when uncertain

- **Active voice preference**
  - Prefer active voice over passive voice where natural in Russian
  - `The report was written by Ivan` → `Иван написал отчёт` (active) — preferred
  - `Отчёт был написан Иваном` (passive) — acceptable but less natural
  - However, passive is appropriate in formal/scientific writing where the agent is unknown or unimportant

## 9. Formality

- **Formal register: Вы with capital letter**
  - In all official, business, legal, and technical documents: use `Вы` (capitalized) for singular "you"
  - `You are required to...` → `Вы обязаны...`
  - `Your application` → `Ваше заявление`
  - `We kindly ask you` → `Убедительно просим Вас`

- **Imperative mood in technical documentation**
  - Instructions and commands use imperative mood (повелительное наклонение)
  - `Press Enter` → `Нажмите клавишу Enter`
  - `Select the file` → `Выберите файл`
  - `Click OK` → `Нажмите «OK»`
  - Use plural imperative form (e.g., `нажмите`, not `нажми`)

- **Formal letter openings and closings**
  - `Dear Sirs` → `Уважаемые господа!`
  - `Dear Mr. Ivanov` → `Уважаемый господин Иванов!`
  - `Dear Ms. Petrova` → `Уважаемая госпожа Петрова!`
  - `Sincerely` → `С уважением,`
  - `We hereby inform you` → `Настоящим уведомляем Вас`
  - `In accordance with` → `В соответствии с`
  - `Due to the above` → `На основании вышеизложенного`

- **Neutral/Informal register**
  - For internal documents, team communications, informal contexts: use `ты` (lowercase)
  - `Пожалуйста, проверь файл` (informal: ты)
  - Do NOT mix formal and informal registers within the same document

- **Legal obligations**
  - `shall` → `обязан` / `должен`
  - `The Contractor shall perform...` → `Подрядчик обязан выполнить...`
  - `must` → `должен` / `обязательно`
  - `may` → `может` / `вправе`
  - `is entitled to` → `имеет право`

- **Tone attributes for Russian formal text**
  - Use full words, not contractions: `и так далее` (not `и т.д.` in very formal text)
  - Avoid colloquialisms and slang
  - Avoid anglicisms where standard Russian terms exist
  - Maintain a respectful, distance-preserving tone

## 10. OCR Artifacts

- **Inference tag format** `[восстановлено: ...]`
  - When a word is corrupted, unclear, or ambiguous due to OCR, do NOT silently guess
  - Use the following tag format:
  - `[восстановлено: {оригинал} → {исправление}, {причина}]`

- **Examples:**
  - `[восстановлено: «настройи» → «настройки», исправление опечатки, буква «к» отсутствовала в оригинале]`
  - `[восстановлено: «l 000» → «1 000», замена латинской «l» на цифру «1» по контексту]`
  - `[восстановлено: «OOO» → «ООО», замена латинских букв на кириллицу, контекст — юридическое лицо]`

- **When uncertain:**
  - If you cannot determine the correct value with confidence, keep the original garbled text and flag it:
    - `[OCR: не удалось определить исходное значение]`
  - Example: `Параметр [OCR: не удалось определить исходное значение] был установлен.`

- **Common OCR errors in Russian texts**
  - Latin letters mistaken for Cyrillic: `l` vs `п`, `o` vs `о` (look similar but different Unicode)
  - Russian "о" vs Latin "o" — check context
  - Broken letters: `н` → `h`, `п` → `n`
  - Merged words: `вдоме` → `в доме`
  - Split words: `на ст ройка` → `настройка`
  - Numbers: `0` vs `О`, `1` vs `l`
  - Hyphenation artifacts: `доку-\nмент` → `документ`

- **General principle**: It is ALWAYS better to tag an uncertain restoration than to guess silently. Correct tagging is good practice, not a defect.

## 11. Translation Philosophy

The Three Principles of Russian Translation (три принципа перевода):

### Первый приоритет: Точность (信 — Faithfulness)
Numerical values, dates, proper nouns, and technical terms must be EXACT.
- `100,00` must stay `100,00`, never become `100.00`
- `15.03.2024` must stay `15.03.2024`, never become `03/15/2024`
- `Microsoft Corporation` stays `Microsoft Corporation`
- No omissions, no additions, no paraphrasing of quantitative data
- When in doubt about any fact or number, flag it rather than guessing

### Второй приоритет: Естественность (达 — Expressiveness)
The translation must read as natural, idiomatic Russian — not as a word-for-word calque from the source language.
- Avoid anglicisms where Russian equivalents exist
- `осуществлять поддержку` → better: `поддерживать`
- `был проведён анализ` → better: `мы проанализировали` (or just `анализ показал`)
- Use natural Russian word order (subject-verb-object is less rigid than English; time often comes first)
- `The meeting will take place on Friday at 10 AM` → `Совещание состоится в пятницу в 10:00` (or `В пятницу в 10:00 состоится совещание`)

### Третий приоритет: Стиль (雅 — Elegance)
Beyond accuracy and naturalness, pursue stylistic quality appropriate to the document type.
- **Formal documents**: dignified, precise, using established legal/business formulas
- **Technical documents**: clear, consistent terminology, imperative instructions
- **Marketing/advertising**: engaging, creative within the bounds of Russian stylistic norms
- **Internal communications**: professional yet approachable

### Priority order: Точность > Естественность > Стиль
When these principles conflict (e.g., a literal translation would sound unnatural), accuracy comes first — but always look for a way to be both accurate AND natural.

### Summary checklist for every paragraph:
1. Are all numbers and dates correct? (Точность)
2. Does this sound like natural Russian? (Естественность)
3. Is the tone appropriate for the document type? (Стиль)
