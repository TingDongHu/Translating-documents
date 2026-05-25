---
id: ru/adapt/from_en
type: adapt
target_lang: ru
source_lang: en
name: English to Russian Adaptation
description: Target-specific adaptation rules for translating English documents into Russian
---

## Formality and Address

- **English "you" → Russian Вы/ты distinction**
  - Source: "You are required to..." → Target: "Вы обязаны..." (formal Вы singular or plural)
  - Source: "You may proceed" → Target: "Вы можете продолжить" (formal register for technical docs)
  - Context: Technical documentation, business correspondence, official documents always use Вы (capitalized in formal correspondence)
- **English "your" → Russian Ваш/твой**
  - Source: "Your application" → Target: "Ваше заявление" (formal)
  - Source: "Your order" → Target: "Ваш заказ"
- **English imperative mood**: polite/softened in Russian
  - Source: "Click here" → Target: "Нажмите здесь" (imperative, 2nd person plural)
  - Source: "Enter your password" → Target: "Введите пароль"
  - Note: Russian technical documentation uses imperative in Вы-form (plural) as standard, not infinitive as in some languages
- **English modals "must/should/may"** → Russian equivalents with different degrees of obligation
  - Source: "You must comply" → Target: "Вы обязаны соблюдать" (strong obligation)
  - Source: "You should check" → Target: "Вам следует проверить" (recommendation)
  - Source: "You may use" → Target: "Вы можете использовать" (permission)
- **English "please"** → Russian "пожалуйста" (less frequent than English "please")
  - Source: "Please find attached..." → Target: "Прилагаем..." (Russian omits "please" here; it is implied)
  - Source: "Please confirm receipt" → Target: "Просим подтвердить получение" (more natural than "Пожалуйста, подтвердите")
- **English titles (Mr/Ms/Dr)** → Russian equivalents
  - Source: "Mr. Smith" → Target: "Господин Смит" (not "Мистер" except in informal contexts or direct speech)
  - Source: "Dr. Johnson" → Target: "Доктор Джонсон"
  - Source: "Professor Brown" → Target: "Профессор Браун"
  - Note: Russian uses "господин/госпожа" in formal correspondence; academic titles are used more commonly than in English
- **English "Dear Sirs" / "To whom it may concern"** → Russian formulaic openings
  - Source: "Dear Sirs" → Target: "Уважаемые господа!" (exclamation mark, not comma)
  - Source: "To whom it may concern" → Target: "Заинтересованным лицам" or "Кому это может касаться"
  - Source: "Dear Mr. Ivanov" → Target: "Уважаемый господин Иванов!" (exclamation mark, not comma)
- **English conversational style** → Russian more reserved in formal writing
  - Source: "Let's get started" → Target: "Приступим" (neutral, not "Давайте начнём" which is too conversational for formal docs)

## Number and Date Conventions

- **English decimal point (.) → Russian comma (,)**
  - Source: "3.14" → Target: "3,14"
  - Source: "99.9%" → Target: "99,9 %"
  - Source: "0.5" → Target: "0,5" (also note the leading zero before decimal comma is kept)
  - This is the most common numeric error in English→Russian translation — ZERO TOLERANCE
- **English thousands separator (,) → Russian non-breaking space**
  - Source: "12,345,678" → Target: "12 345 678"
  - Source: "1,000" → Target: "1 000"
- **English "billion" (10⁹) → Russian "миллиард"**
  - Source: "$5 billion" → Target: "5 млрд долларов США" or "5 миллиардов долларов"
  - Note: UK English "billion" now also 10⁹ (no longer 10¹²)
- **English "trillion" (10¹²) → Russian "триллион"**
  - Source: "$2 trillion" → Target: "2 трлн долларов"
- **English "quadrillion" (10¹⁵) → Russian "квадриллион"** (same, but check context)
- **English date format: Month DD, YYYY or MM/DD/YYYY → Russian: ДД.ММ.ГГГГ**
  - Source: "January 15, 2024" → Target: "15 января 2024 г." (in text) or "15.01.2024" (numeric)
  - Source: "12/31/2023" → Target: "31.12.2023" (**critical**: swap month and day!)
  - Source: "2023-12-31" → Target: "31.12.2023" (ISO format can be kept in technical contexts)
  - This is the second most common numeric error — ZERO TOLERANCE
- **English 12h time (AM/PM) → Russian 24h time**
  - Source: "3:00 PM" → Target: "15:00"
  - Source: "12:00 AM" → Target: "0:00" (midnight)
  - Source: "12:00 PM" → Target: "12:00" (noon)
  - Source: "9:30 AM" → Target: "9:30"
- **English week format: "week of March 5" → Russian "неделя с 5 марта"**
- **English "midnight" / "noon"** → Russian "полночь" / "полдень"
  - Source: "The report is due by midnight" → Target: "Отчёт должен быть сдан до полуночи"
- **English century format** → Russian uses Roman numerals or words
  - Source: "21st century" → Target: "XXI век" (preferred) or "двадцать первый век"
  - Source: "early 20th century" → Target: "начало XX века"
- **English decades** → Russian
  - Source: "the 1990s" → Target: "1990-е гг." or "девяностые годы"

## Cultural References

- **English common law concepts** → no direct Russian equivalent; use descriptive translation
  - Source: "common law" → Target: "общее право" or "прецедентное право" (with пояснение if needed)
  - Source: "equity" (legal) → Target: "право справедливости"
  - Source: "trust" (legal) → Target: "траст" (with explanation: доверительная собственность)
- **English corporate concepts** → Russian equivalents
  - Source: "Limited Liability Company (LLC)" → Target: "Общество с ограниченной ответственностью (ООО)"
  - Source: "Corporation (Inc./Corp.)" → Target: "Акционерное общество (АО)" or "Корпорация"
  - Source: "Public Limited Company (PLC)" → Target: "Публичное акционерное общество (ПАО)"
  - Source: "Board of Directors" → Target: "Совет директоров"
  - Source: "CEO" → Target: "Генеральный директор" (not just "CEO")
- **English academic concepts** → Russian adaptation
  - Source: "Bachelor's degree" → Target: "степень бакалавра"
  - Source: "Master's degree" → Target: "степень магистра"
  - Source: "PhD" → Target: "доктор философии (PhD)" (note: not equivalent to Russian доктор наук)
  - Source: "GPA" → Target: "средний балл успеваемости" (GPA is not used in Russia; translate descriptively)
- **English measurement system (imperial)** → Russian measurement system (metric)
  - Source: "5 miles" → Target: "8 км" (convert to metric; add imperial in parentheses if needed for context)
  - Source: "10 feet" → Target: "3 м" or "3,05 м" (precise conversion where accuracy matters)
  - Source: "1 gallon" → Target: "3,78 л"
  - Source: "32°F" → Target: "0 °C"
  - Source: "1 pound" → Target: "0,45 кг"
  - Note: Converting imperial to metric is mandatory for technical documents. For literary texts, keep imperial with metric in parentheses.
- **English idiomatic expressions** → Russian equivalents with similar meaning (not literal)
  - Source: "It's raining cats and dogs" → Target: "Льёт как из ведра" (idiomatic equivalent, not literal)
  - Source: "The ball is in your court" → Target: "Теперь ход за Вами"
  - Source: "To cut a long story short" → Target: "Короче говоря"
- **English culturally specific terms** → keep with explanation or adapt
  - Source: "Thanksgiving" → Target: "День благодарения" (keep American cultural reference)
  - Source: "IRS" → Target: "Налоговая служба США (IRS)"
  - Source: "Social Security Number" → Target: "номер социального страхования (SSN)" (explain if context requires)
- **English names of international organizations** → use official Russian names
  - Source: "United Nations" → Target: "Организация Объединённых Наций (ООН)"
  - Source: "World Health Organization" → Target: "Всемирная организация здравоохранения (ВОЗ)"
  - Source: "International Monetary Fund" → Target: "Международный валютный фонд (МВФ)"
  - Source: "NATO" → Target: "НАТО" (but NATO) or "Организация Североатлантического договора" (full form)

### English Proper Names → Russian Cyrillic Transliteration

English proper names are transliterated into Russian Cyrillic using established rules based on phonetic mapping, not orthographic.

- **Key English→Russian transliteration rules**:
  - English "th" → Russian "з" (voiced, as in "the") or "с" (unvoiced, as in "thin")
    - Source: "Smith" → Target: "Смит" (not Смиθ)
    - Source: "Thompson" → Target: "Томпсон"
  - English "h" → Russian "х" (hard H, as in "house")
    - Source: "Harrison" → Target: "Харрисон"
    - Source: "Hilton" → Target: "Хилтон"
  - English "w" → Russian "у" (as in "Washington" → Вашингтон) or "в" (in some positions)
    - Source: "Washington" → Target: "Вашингтон"
    - Source: "West" → Target: "Уэст" or "Вест" (varies by established tradition)
    - Source: "Wales" → Target: "Уэльс"
  - English "j" → Russian "дж"
    - Source: "Johnson" → Target: "Джонсон"
    - Source: "Jackson" → Target: "Джексон"
  - English "ng" → Russian "нг" (hard g pronounced)
    - Source: "Washington" → Target: "Вашингтон" (г is pronounced)
  - English "sh" → Russian "ш"
    - Source: "Shakespeare" → Target: "Шекспир"
  - English "ch" → Russian "ч"
    - Source: "Churchill" → Target: "Черчилль"
  - English silent letters are NOT reflected in Russian transliteration
    - Source: "Knox" → Target: "Нокс" (k is silent in English, not pronounced in Russian either)
  - English doubled letters → typically single in Russian
    - Source: "Miller" → Target: "Миллер" (sometimes kept, varies)
- **Place names**: Use established Russian names where they exist
  - Source: "London" → Target: "Лондон"
  - Source: "New York" → Target: "Нью-Йорк"
  - Source: "Los Angeles" → Target: "Лос-Анджелес"
  - Source: "United Kingdom" → Target: "Соединённое Королевство" or "Великобритания"
  - Source: "Germany" → Target: "Германия"
- **Company/brand names**: Keep in Latin script for international brands; transliterate for local brands
  - Source: "Microsoft" → Target: "Microsoft" (kept in Latin) or "Майкрософт" (in Russian text contexts)
  - Source: "Apple Inc." → Target: "Apple Inc." or "компания Apple"
  - Trade publications tend to keep brand names in original Latin script

## Source-specific Terminology

- **English ISO terminology** → Russian ГОСТ/ГОСТ Р equivalents
  - Source: "ISO 9001:2015 Quality management systems" → Target: "ГОСТ Р ИСО 9001-2015 Системы менеджмента качества"
  - Source: "ISO 14001" → Target: "ГОСТ Р ИСО 14001"
  - Note: Many ISO standards are adopted as GOST R (national Russian standards) with a different number — always verify the GOST R equivalent
  - Source: "ISO 2768-1" → Target: "ГОСТ 30893.1" (example of different numbering)
- **English technical terms → Russian technical terms**
  - Source: "torque" → Target: "крутящий момент"
  - Source: "stress" → Target: "напряжение" (mechanical)
  - Source: "strain" → Target: "деформация"
  - Source: "fatigue" → Target: "усталость" (material fatigue)
  - Source: "yield strength" → Target: "предел текучести"
  - Source: "tensile strength" → Target: "предел прочности при растяжении"
- **English IT terminology → Russian IT terminology**
  - Source: "cloud computing" → Target: "облачные вычисления"
  - Source: "machine learning" → Target: "машинное обучение"
  - Source: "artificial intelligence" → Target: "искусственный интеллект (ИИ)"
  - Source: "deep learning" → Target: "глубокое обучение"
  - Source: "big data" → Target: "большие данные"
  - Source: "software" → Target: "программное обеспечение (ПО)" (prefer translated form over "софт")
  - Source: "hardware" → Target: "аппаратное обеспечение" or "аппаратура"
  - Source: "firmware" → Target: "встроенное ПО" or "прошивка"
- **English legal terminology → Russian equivalents**
  - Source: "force majeure" → Target: "форс-мажор" or "обстоятельства непреодолимой силы"
  - Source: "indemnification" → Target: "возмещение убытков"
  - Source: "warranty" → Target: "гарантия"
  - Source: "breach of contract" → Target: "нарушение договора"
  - Source: "liquidated damages" → Target: "неустойка" (not "ликвидированные убытки")
  - Source: "intellectual property" → Target: "интеллектуальная собственность"
  - Source: "confidentiality" → Target: "конфиденциальность"
  - Source: "non-disclosure agreement (NDA)" → Target: "соглашение о неразглашении (NDA)"
  - Source: "shall" → Target: "обязан" / "должен" (not будущее время)
- **English financial terminology → Russian equivalents**
  - Source: "revenue" → Target: "выручка" (not "доход" which is broader)
  - Source: "profit" → Target: "прибыль"
  - Source: "net income" → Target: "чистая прибыль"
  - Source: "EBITDA" → Target: "EBITDA" (keep acronym; пояснение: прибыль до вычета процентов, налогов и амортизации)
  - Source: "accounts receivable" → Target: "дебиторская задолженность"
  - Source: "accounts payable" → Target: "кредиторская задолженность"
  - Source: "goodwill" → Target: "гудвилл" or "деловая репутация"
- **English administrative terminology → Russian equivalents**
  - Source: "Stakeholder" → Target: "заинтересованная сторона" or "стейкхолдер"
  - Source: "Policy" → Target: "политика" (corporate policy) or "стратегия" (public policy)
  - Source: "Regulation" → Target: "нормативный акт" or "регламент"
  - Source: "Guideline" → Target: "руководящие указания" or "методические рекомендации"
  - Source: "Compliance" → Target: "соблюдение требований" or "комплаенс" (loanword gaining usage)
- **English SI unit names** → Russian (same symbols, Latin script kept, pronunciation differs)
  - Source: "100 km/h" → Target: "100 км/ч" (km/h is the same, but in Russian text this is fine)
  - Source: "50 MPa" → Target: "50 МПа"
  - Source: "10 kWh" → Target: "10 кВт·ч" (kettle with dot)

## Administrative/Legal Style

- **English passive voice** → Russian passive (страдательный залог) or active (действительный залог)
  - Source: "The report was submitted on time" → Target: "Отчёт был представлен вовремя" (Russian passive with был + краткое причастие)
  - Source: "It is recommended that..." → Target: "Рекомендуется..." (reflexive passive, very natural in Russian)
  - Source: "It was decided that..." → Target: "Было решено, что..." or "Решено..." (short form passive)
  - Source: "The document is attached" → Target: "Документ прилагается" (reflexive verb, most common technical form)
  - Note: Russian uses the reflexive passive (-ся verbs) much more than the compound passive (быть + причастие) in technical writing. The English "be + past participle" can often be translated as an -ся verb: "the form must be signed" → "форма должна подписываться"
- **English "shall" in legal/technical texts** → Russian obligations (not future tense!)
  - Source: "The Contractor shall deliver..." → Target: "Подрядчик обязан поставить..." (not "будет поставлять")
  - Source: "The Employer shall pay..." → Target: "Заказчик выплачивает..." (present tense, expressing obligation)
  - Source: "No modification shall be made without..." → Target: "Изменения не допускаются без..." (negative obligation)
- **English "hereby/hereinafter/hereunder"** → Russian formal connectors
  - Source: "The parties hereby agree" → Target: "Стороны настоящим соглашаются"
  - Source: "hereinafter referred to as..." → Target: "далее именуемый..." (cases agree with noun gender)
  - Source: "as defined hereunder" → Target: "как определено ниже"
- **English legal sentence structure**: long → Russian even longer (legal style)
  - Source: "Subject to the terms and conditions of this Agreement..." → Target: "При условии соблюдения положений настоящего Соглашения..."
  - Source: "Notwithstanding the foregoing..." → Target: "Независимо от вышеизложенного..." or "Вопреки вышеуказанному..."
- **English "whereas" clauses (recitals)** → Russian "принимая во внимание, что..." / "ввиду того, что..."
  - Source: "WHEREAS, the Company wishes to engage..." → Target: "ПРИНИМАЯ ВО ВНИМАНИЕ, что Компания желает привлечь..."
  - Note: Recitals in Russian contracts typically use "с одной стороны" / "с другой стороны" (stating parties), not "Whereas"
- **English bullet list punctuation** → Russian conventions
  - English: Each bullet ends with semicolon (except last) → Russian: Each bullet starts with lowercase, ends with semicolon or comma, last ends with period
  - English capitalizes first word of each bullet → Russian: lowercase (if list items complete the introductory phrase) or uppercase (if complete sentences)
- **English letter closing** → Russian letter closing
  - Source: "Sincerely," → Target: "С уважением,"
  - Source: "Best regards," → Target: "С уважением," (most common formal closing)
  - Source: "Yours faithfully," → Target: "С уважением," (same universal closing in Russian)
  - Note: Russian has few variants; "С уважением" is universal for formal correspondence
- **English "Attached please find..."** → Russian "Прилагаем..." / "К настоящему прилагается..."
  - Source: "Please find attached the contract" → Target: "К настоящему письму прилагается договор" or "Прилагаем договор"
- **English section references** → Russian conventions
  - Source: "Section 5.2" → Target: "Раздел 5.2" or "пункт 5.2"
  - Source: "Appendix A" → Target: "Приложение А"
  - Note: Russian standards use "пункт" (clause), "подпункт" (sub-clause), "раздел" (section), "статья" (article for laws)
- **English numbering in legal docs**: "1.1, 1.2" → Russian "1.1, 1.2" (same) or "1.1., 1.2." (with trailing period in some traditions)
- **English reference to laws** → Russian reference style
  - Source: "pursuant to Section 5 of the Securities Act" → Target: "в соответствии со статьёй 5 Закона о ценных бумагах"
  - Source: "under the laws of the State of New York" → Target: "в соответствии с законодательством штата Нью-Йорк"

### Passive Voice and Verb Aspect in Technical Texts

- **English simple present passive ("is done")** → Russian reflexive passive (-ся) or short passive participle
  - Source: "The system is configured" → Target: "Система настраивается" (reflexive) or "Система сконфигурирована" (short participle)
  - Source: "The valve is opened" → Target: "Клапан открывается" (present, process) or "Клапан открыт" (state)
- **English present perfect passive ("has been done")** → Russian past passive (short participle)
  - Source: "The test has been completed" → Target: "Тестирование завершено"
  - Source: "The data has been analyzed" → Target: "Данные проанализированы"
- **English modal passive ("can be done / must be done")** → Russian modal + infinitive or -ся form
  - Source: "This can be adjusted" → Target: "Это можно отрегулировать" (adverbial modal + infinitive)
  - Source: "The password must be changed" → Target: "Пароль необходимо сменить" (more natural than "должен быть сменён")
- **Verb aspect in technical instructions**:
  - **Perfective aspect (совершенный вид)** for completed actions / single instructions
    - Source: "Click the button" → Target: "Нажмите кнопку" (perfective)
  - **Imperfective aspect (несовершенный вид)** for processes / repeated actions
    - Source: "Hold the button" → Target: "Удерживайте кнопку" (imperfective)
    - Source: "Check the pressure regularly" → Target: "Регулярно проверяйте давление" (imperfective)
  - Note: Choosing the wrong aspect is a common error — perfective for single actions, imperfective for ongoing/process actions

### Articles

- **English definite article "the"** → Implied by Russian noun cases, word order, or omitted
  - Source: "The system shall operate at 50 Hz" → Target: "Система должна работать на частоте 50 Гц" (no article, case ending indicates definiteness)
  - Source: "The device has been tested" → Target: "Устройство протестировано" (definiteness from context and word order)
- **English indefinite article "a/an"** → Not expressed in Russian; indefinite meaning conveyed by:
  - Word order (indefinite often first mention, then definiteness implied)
  - Quantity words (один, какой-то, некий) when needed for clarity
  - Source: "A sensor detects the temperature" → Target: "Датчик определяет температуру" (first mention, no marker)
  - Source: "A certain Mr. Smith called" → Target: "Некий господин Смит звонил"
  - Source: "This is a sample" → Target: "Это образец" (no article equivalent)
- **English "the" in generic statements** → Omitted in Russian or uses plural generic
  - Source: "The elephant is a large mammal" → Target: "Слон — крупное млекопитающее" (generic singular, no article)
  - Source: "The internet has changed..." → Target: "Интернет изменил..." (proper-like noun, no article)

## Punctuation Conversion

- **English quotation marks "" → Russian guillemets «»** (first level)
  - Source: 'He said "This is important"' → Target: 'Он сказал: «Это важно»'
  - Source: 'The term "interface" refers to...' → Target: 'Термин «интерфейс» означает...'
- **English inner quotation marks '' → Russian inner ""** (second level, used inside «»)
  - Source: 'She said "He told me \'Go now\'"' → Target: 'Она сказала: «Он сказал мне: "Иди сейчас"»'
  - Source: 'The "so-called \'expert\'" arrived' → Target: 'Прибыл так называемый «эксперт»'
- **English question marks** — same symbol ? but Russian does not use space before ?
- **English exclamation marks** — same symbol ! but Russian uses it in formal salutations
  - Source: "Dear Mr. Smith," → Target: "Уважаемый господин Смит!" (exclamation mark in Russian, comma in English)
  - Source: "Sincerely," → Target: "С уважением," (comma, same as English)
- **English em dash (—)** → Russian em dash (—) with spacing rules
  - English em dash often without spaces ("word—word") → Russian always uses spaces ("слово — слово")
  - Source: "Three components—CPU, RAM, and storage—are critical" → Target: "Три компонента — ЦП, ОЗУ и накопитель — являются критическими"
- **English en dash (–) for ranges** → Russian en dash (–) same, but check spacing
  - Source: "pages 10–20" → Target: "стр. 10–20" (no spaces around en dash in both languages)
  - Source: "2010–2020" → Target: "2010–2020 гг." (add "гг." for years range in Russian)
- **English hyphen (-) in compound words** → Russian may use hyphen differently
  - Source: "decision-making" → Target: "принятие решений" (no hyphen, separate words)
  - Source: "state-of-the-art" → Target: "современный" or "передовой" (descriptive, not hyphenated)
  - Source: "well-known" → Target: "хорошо известный" (adverb + adjective, no hyphen)
  - Note: Russian compound adjectives are often hyphenated where English has separate words: "научно-исследовательский" (research and development); "учебно-методический" (educational-methodological)
- **English serial comma (Oxford comma)** → Russian uses comma the same way (optional in both, but consistent within document)
  - Source: "apples, oranges, and bananas" → Target: "яблоки, апельсины и бананы" (comma before "и" is optional in Russian, same as Oxford comma conventions)
- **English colon** → same : in Russian (half-width in both)
  - Source: "The following items:" → Target: "Следующие пункты:"
  - Note: Russian uses colon before lists more consistently than modern English
- **English semicolon** → same ; in Russian, but used less frequently
  - Russian legal texts use semicolons in long enumerations, similar to English
- **English ellipsis ... (3 dots)** → Russian ... (3 dots, same)
  - Source: "and so on..." → Target: "и так далее..." (same)
- **English apostrophe '** → rarely used in Russian; appears only in loanwords
  - Source: "O'Brien" → Target: "О'Брайен" (kept for foreign names)
  - Source: "don't" → Target: "не" (contraction doesn't exist in Russian; write as separate word)
- **English percent sign** with no space → Russian with non-breaking space
  - Source: "50%" → Target: "50 %"
  - Source: "a 10% increase" → Target: "увеличение на 10 %"
- **English degrees** no space → non-breaking space in Russian
  - Source: "25°C" → Target: "25 °C"
  - Source: "90° angle" → Target: "угол 90°" (degrees without C: "90°" can stay without space)
- **English spacing after period** (one space) → Russian (one space, same — both use single space)
  - Note: Double spaces after period (typewriter convention) should always be reduced to single
- **English mathematical operators spacing** → same in Russian
  - Source: "5 + 3 = 8" → Target: "5 + 3 = 8" (spaces around operators)
- **English slash** in alternatives → same / in Russian
  - Source: "and/or" → Target: "и/или" (same usage)
  - Source: "input/output" → Target: "ввод/вывод"

### Special Russian Typographic Rules

- **Non-breaking spaces (неразрывный пробел)**: Used more broadly in Russian than in English
  - Between single-letter prepositions and following word: "в стране", "о решении", "с учётом"
  - Between initials and surname: "А. С. Пушкин"
  - Between number and unit: "10 кг", "50 м", "100 %"
  - In dates: "15 января 2024 г."
  - After "г." in years: "2024 г." (non-breaking space before "г.")
- **Reduction conventions**: Russian uses abbreviations with periods more extensively than English
  - "и т.д." (etc.), "и т.п." (and so on), "и др." (and others)
  - "т.е." (i.e.), "т.к." (because), "т.н." (so-called)
  - "г." (year), "гг." (years), "стр." (page), "п." (clause/paragraph)
- **Letter (Ё)** : Optional but encouraged in contexts where ambiguity may arise (e.g., все vs всё, небо vs нёбо). Should be preserved in proper names (e.g., "Пётр", not "Петр").
