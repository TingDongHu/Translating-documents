---
id: ko/rules/base
type: rules
target_lang: ko
name: Korean (ko) Translation Rules -- Base Guide
description: Korean base translation rules
---

# Korean (ko) Translation Rules -- Base Guide

> Target language: Korean (한국어)
> ISO 639-1: `ko` | ISO 639-2: `kor`
> Version: 1.0 / 2026-05-25

---

## Table of Contents

1.  [Number Format](#1-number-format)
2.  [Currency](#2-currency)
3.  [Date and Time](#3-date-and-time)
4.  [Addresses](#4-addresses)
5.  [Proper Nouns](#5-proper-nouns)
6.  [Punctuation](#6-punctuation)
7.  [Formatting](#7-formatting)
8.  [Grammar](#8-grammar)
9.  [Formality](#9-formality)
10. [OCR Artifacts](#10-ocr-artifacts)
11. [Translation Philosophy](#11-translation-philosophy)

---

## 1. Number Format

### 1.1 Decimal Separator

Korean uses the **period (`.`)** as the decimal separator, NOT the comma. This is identical to English, so no conversion is needed when translating from English into Korean. When translating from languages that use a decimal comma (German, French, Spanish, Russian, etc.), the comma **must** be converted to a period.

| Source (comma-locale) | Correct KO | Wrong | Notes |
|---|---|---|---|
| 3,14 (FR) | 3.14 | 3,14 | Comma must become period |
| 0,5 (DE) | 0.5 | 0,5 | Same rule |
| 9,99 (ES) | 9.99 | 9,99 | Same rule |
| 1.000,50 (IT) | 1,000.50 | 1.000,50 | Full inversion: swap comma/period |
| 3.14159 (EN) | 3.14159 | 3.14159 | No change from EN |

### 1.2 Thousands Separator

Korean uses the **comma (`,`)** as the thousands separator, identical to English. When translating from comma-locale languages, the thousands-separator period must be converted to a comma.

| Source (comma-locale) | Correct KO | Wrong | Notes |
|---|---|---|---|
| 1.000 (DE) | 1,000 | 1.000 | Dot becomes comma |
| 10.000 (FR) | 10,000 | 10.000 | Same rule |
| 1.234.567 (IT) | 1,234,567 | 1.234.567 | All dots to commas |

Korean also natively uses the numeral units 만 (10,000), 억 (100,000,000), 조 (10^12). In general prose, convert large numbers to these units for natural readability.

| Source (EN) | Prose KO (natural) | Table KO (numeric) | Notes |
|---|---|---|---|
| 10,000 | 1만 | 10,000 | 만 preferred in prose |
| 50,000 | 5만 | 50,000 | |
| 100,000 | 10만 | 100,000 | |
| 1,000,000 | 100만 | 1,000,000 | |
| 10,000,000 | 1,000만 | 10,000,000 | |
| 100,000,000 | 1억 | 100,000,000 | 억 preferred in prose |
| 1,500,000 | 150만 | 1,500,000 | Mixed form |
| 23,000,000 | 2,300만 | 23,000,000 | |
| 1,200,000,000 | 12억 | 1,200,000,000 | |
| 2,500,000,000,000 | 2조 5,000억 | 2,500,000,000,000 | 조 + 억 combined |

**Rule of thumb:**
- Tables, spreadsheets, financial statements: use Western comma grouping (`1,000,000`)
- Prose, narrative, general text: convert to 만/억/조 (`100만`)
- Mixing is acceptable (e.g., `1,500만`), as long as it is consistent within a document

### 1.3 Negative Numbers

The minus sign `-` is placed directly before the digits, matching English usage. No space between `-` and the first digit.

| Source | Correct KO | Notes |
|---|---|---|
| -5 | -5 | Direct minus sign |
| -3.14 | -3.14 | Same format |
| -10% | -10% | |
| -$50 | -50달러 | |
| negative 20 degrees | 영하 20도 | Natural KO for temperature |
| a loss of 3 million | 300만 적자 / 마이너스 300만 | Context-dependent |

**Prose forms:** For temperatures: `영하 5도`. For finances: `적자 500만 원` or `마이너스 500만 원`.

### 1.4 Percentages

The percent sign `%` is placed directly after the number with **no space**.

| Source | Correct KO | Wrong | Notes |
|---|---|---|---|
| 50% | 50% | 50 % | No space before % |
| 0.1% | 0.1% | 0,1% | Korean uses period decimal |
| 10% discount | 10% 할인 | | % + space + noun |
| increased by 25% | 25% 증가 | | |
| 3.5% interest rate | 3.5% 금리 | | |
| 99.9% pure | 99.9% 순도 | | |
| 50 percent of respondents | 응답자의 50% | | Word order adjusted |
| half | 50% / 절반 | | 절반 is natural in prose |

**Formal prose exception:** In very formal literary texts, `퍼센트` may be spelled out: `50퍼센트`. But `%` is preferred in all modern documents.

### 1.5 Decimals and Fractions in Prose

| Source | Natural KO | Notes |
|---|---|---|
| 0.5 liters | 0.5리터 / 500ml | |
| 1/2 | 2분의 1 / 절반 | 분의 format in formal prose |
| 3/4 | 4분의 3 | |
| 2 1/2 | 2.5 / 2와 2분의 1 | |
| 1.5 times | 1.5배 | |
| 0.00% | 0.00% | |

### 1.6 Ordinal Numbers

| Source | KO | Notes |
|---|---|---|
| 1st | 첫째 / 1번째 / 제1 | 제N for formal titles |
| 2nd | 둘째 / 2번째 / 제2 | |
| 3rd | 셋째 / 3번째 / 제3 | |
| 10th | 열째 / 10번째 / 제10 | |
| Chapter 1 | 제1장 / 1장 | |
| Article 5 | 제5조 | Legal text standard |
| Section 3 | 제3절 | |
| Appendix A | 부록 A | |

### 1.7 Units of Measurement

Put a **space** between the number and the unit. Convert imperial units to metric for Korean audiences.

| Source (imperial) | KO (converted) | Notes |
|---|---|---|
| 5 miles | 약 8km | Convert unless context requires otherwise |
| 100 feet | 약 30m | |
| 1 gallon | 약 3.8L | Conversion + unit |
| 212°F | 100°C | Full conversion |
| 10 inches | 25.4cm | |
| 120 mph | 약 193km/h | |

| Source (metric) | KO (retained) | Notes |
|---|---|---|
| 5 km | 5 km | Space before unit |
| 2.5 kg | 2.5 kg | |
| 10 L | 10 L | |
| 30°C | 30°C | Same in KO |
| 100 m | 100 m | |
| 1,000 ml | 1,000ml | No space with ml/L optional |

---

## 2. Currency

### 2.1 South Korean Won (원)

| Source | Correct KO | Notes |
|---|---|---|
| ₩100,000 | 100,000원 | Natural KO: number + "원" after |
| KRW 100,000 | 100,000원 (KRW) | In tables |
| ￦10,000 | 10,000원 | Alt. symbol |
| USD 1 = KRW 1,300 | 1달러 = 1,300원 | Exchange rate |

**Position of the won sign:**
- The `₩` / `￦` symbol is placed **before** the amount in ISO style: `₩10,000`
- BUT in natural Korean text, write the number first followed by `원`: `10,000원`
- **Do not** put a space between the amount and `원`: write `10,000원`, not `10,000 원`

### 2.2 Foreign Currency Notation

| Source | Correct KO | Wrong |
|---|---|---|
| $100 | 100달러 | $100 (keep original notation only if needed for context) |
| €500 | 500유로 | |
| ¥10,000 | 10,000엔 | |
| £50 | 50파운드 | |
| CHF 200 | 200스위스 프랑 / 200CHF | |
| A$150 | 150호주 달러 | |
| C$100 | 100캐나다 달러 | |
| CNY 1,000 | 1,000위안 | |

**Rule:** For foreign currencies, use `[number][Korean currency name]` format: `50달러`, `100엔`. The original symbol can be kept in parentheses if the context requires clarity: `50달러 ($50)`.

### 2.3 ISO Code Usage

| Type | Format | Example |
|---|---|---|
| General text | Name + amount | 100달러, 500유로 |
| Financial table | ISO code prefix | USD 100, EUR 500 |
| Mixed currencies in one table | ISO code in header | `(USD)` in column header, just numbers below |
| Exchange rates | ISO code pair | USD/KRW 1,300.50 |

### 2.4 Large Currency Amounts

| Source | KO (natural) | KO (numeric) |
|---|---|---|
| $1.5 million | 150만 달러 | 1,500,000달러 |
| ₩10 billion | 100억 원 | 10,000,000,000원 |
| €2.3 trillion | 2조 3,000억 유로 | 2,300,000,000,000유로 |
| $50,000 | 5만 달러 | 50,000달러 |
| ¥100 million | 1억 엔 | 100,000,000엔 |

### 2.5 Currency in Tables

| EN Table Header | KO Table Header |
|---|---|
| Amount (USD) | 금액 (USD) |
| $ 1,234.56 | 1,234.56 |
| $ 5,000.00 | 5,000.00 |
| Total: $ 6,234.56 | 합계: 6,234.56달러 |

**Rule:** In tables, either put the currency in the column header and show bare numbers, or append `원`/`달러` to each value. Choose one approach and apply consistently.

---

## 3. Date and Time

### 3.1 Date Format

Korean uses **YYYY년 MM월 DD일** -- year-month-day order with native suffixes.

| Source (EN) | Correct KO | Notes |
|---|---|---|
| 2024-01-15 | 2024년 1월 15일 | Standard format |
| Jan 15, 2024 | 2024년 1월 15일 | Month names expanded |
| 01/15/2024 | 2024년 1월 15일 | MM/DD/YYYY reordered |
| 15 January 2024 | 2024년 1월 15일 | Reversed order corrected |
| 2024/01/15 | 2024년 1월 15일 | Slashes replaced |
| Jan. 15th, 2024 | 2024년 1월 15일 | Ordinal suffixes dropped |
| 2024-01 | 2024년 1월 | Month-only |

**Numeric-only date format:** In tables and tight layouts, `2024. 1. 15.` or `2024-01-15` is acceptable, but `YYYY년 MM월 DD일` is preferred in running text.

### 3.2 Month Names -- 순우리말 vs 한자어 (Sino-Korean)

| English | Sino-Korean (한자어) -- STANDARD | Native Korean (순우리말) -- LITERARY ONLY |
|---|---|---|
| January | 1월 | (해오름달) |
| February | 2월 | (시샘달) |
| March | 3월 | (물오름달) |
| April | 4월 | (잎새달) |
| May | 5월 | (푸른달) |
| June | 6월 | (누리달) |
| July | 7월 | (견우직녀달) |
| August | 8월 | (타오름달) |
| September | 9월 | (열매달) |
| October | 10월 | (하늘연달) |
| November | 11월 | (미므르달) |
| December | 12월 | (매듭달) |

**Rule:** Always use Sino-Korean `N월` in translation. 순우리말 month names are archaic and only appropriate in traditional poetry, historical fiction, or deliberate literary style.

### 3.3 Day Names

| English | Sino-Korean (STANDARD) | 순우리말 (LITERARY ONLY) |
|---|---|---|
| Monday | 월요일 | (달날) |
| Tuesday | 화요일 | (불날) |
| Wednesday | 수요일 | (물날) |
| Thursday | 목요일 | (나무날) |
| Friday | 금요일 | (쇠날) |
| Saturday | 토요일 | (흙날) |
| Sunday | 일요일 | (해날) |

**Rule:** Always use `~요일` forms. Use `(월)` abbreviation in parentheses after dates: `2024년 1월 15일 (월)`.

### 3.4 Time Format

Korean uses **24-hour format** (HH:MM) as the standard in official, business, and technical writing. The 12-hour format with `오전`/`오후` (AM/PM) is used in casual writing and spoken language.

| Source (EN) | KO (24h -- official) | KO (12h -- casual) | Notes |
|---|---|---|---|
| 3:00 PM | 15:00 | 오후 3:00 / 오후 3시 | 24h preferred in docs |
| 9:30 AM | 09:30 | 오전 9:30 / 오전 9시 30분 | |
| 12:00 PM | 12:00 | 정오 | 정오 = noon |
| 12:00 AM | 00:00 | 자정 | 자정 = midnight |
| 2:45 PM | 14:45 | 오후 2시 45분 | |
| 6:00 PM | 18:00 | 오후 6시 | |
| 8:30 AM | 08:30 | 오전 8시 30분 | |

**Prose time:** In narrative prose, use `시`/`분`/`초` suffixes: `오후 3시 15분 30초`.

### 3.5 Combined Date-Time

| Source | KO |
|---|---|
| 2024-01-15 14:30 | 2024년 1월 15일 14:30 |
| Jan 15, 2024, 3:00 PM | 2024년 1월 15일 오후 3:00 |
| 2024-01-15T09:30:00Z | 2024년 1월 15일 09:30:00 (UTC) |

### 3.6 Durations and Periods

| Source | KO (Sino -- formal) | KO (Native -- casual) |
|---|---|---|
| 2 hours | 2시간 | 두 시간 |
| 30 minutes | 30분 | 삼십 분 |
| 1 day | 1일 | 하루 |
| 2 days | 2일 | 이틀 |
| 1 week | 1주일 | 일주일 |
| 2 weeks | 2주일 | 이주일 |
| 1 month | 1개월 | 한 달 |
| 3 months | 3개월 | 석 달 |
| 1 year | 1년 | 일 년 |
| Q1 2024 | 2024년 1분기 | |
| FY2024 | 2024 회계연도 | |
| H1 2024 | 2024년 상반기 | |
| 2024-2025 | 2024~2025년 | |

**Rule:** Use Sino-Korean counters in formal documents (`1일`, `1주일`, `1개월`). Native counters (`하루`, `일주일`, `한 달`) are acceptable in casual contexts but should not be mixed with Sino forms in the same document.

### 3.7 Era / Year Notation

| Source | KO |
|---|---|
| 2024 AD | 2024년 / 서기 2024년 |
| 57 BC | 기원전 57년 (BC 57) |
| 4th century | 4세기 |
| the 1990s | 1990년대 |

---

## 4. Addresses

### 4.1 Korean Address Order (Large to Small)

Korean addresses flow from **largest administrative unit to smallest**, the reverse of English order.

**Standard sequence:**
```
우편번호 → 도/특별시/광역시 → 시/군/구 → 동/읍/면 → 번지(길/로) → 건물명 → 상세주소
```

| Source (EN, small-to-large) | KO (large-to-small) |
|---|---|
| 123 Main St, Apt 4B, New York, NY 10001 | (우) 10001, 뉴욕주 뉴욕시 메인 스트리트 123, 4B호 |
| 456 Oak Avenue, Los Angeles, CA 90001 | (우) 90001, 캘리포니아주 로스앤젤레스 오크 애비뉴 456 |
| 1600 Amphitheatre Pkwy, Mountain View, CA 94043 | (우) 94043, 캘리포니아주 마운틴뷰시 앰피시어터 파크웨이 1600 |
| 10 Downing St, London, UK | 영국 런던 다우닝 스트리트 10 |
| 221B Baker St, London, UK | 영국 런던 베이커 스트리트 221B |

### 4.2 Korean Domestic Address Examples

| Component | Korean | Example |
|---|---|---|
| Postal code | 우편번호 | 04524 |
| Province | 도 | 경기도, 충청남도 |
| Special city | 특별시 | 서울특별시 |
| Metro city | 광역시 | 부산광역시, 대구광역시 |
| City | 시 | 수원시, 창원시 |
| County | 군 | 진천군 |
| District | 구 | 강남구, 종로구 |
| Neighborhood | 동 | 역삼동, 삼성동 |
| Town | 읍 | 인삼읍 |
| Township | 면 | 초촌면 |
| Road name | 로 / 길 | 테헤란로, 디지털로31길 |
| Building number | 번 | 123-45 |
| Apartment detail | 동 / 호 | 101동 504호 |

**Full domestic address examples:**
```
(우) 04524 서울특별시 중구 세종대로 110
(우) 13529 경기도 성남시 분당구 판교역로 235번길 24
서울특별시 강남구 테헤란로 152 (역삼동 736-1)
```

### 4.3 Address Translation Strategy

| Context | Approach | Example |
|---|---|---|
| Korean audience reading foreign address | Reorder large-to-small, translate terms | See Section 4.1 |
| International shipping label | Keep local format, add KO translation in parentheses | `123 Main St, New York` (뉴욕주 메인 스트리트 123) |
| Literary reference to a place | Translate into KO administrative terms | `그는 런던의 베이커 스트리트 221B에 살았다` |

---

## 5. Proper Nouns

### 5.1 Foreign Name Transcription (외래어 표기법)

Foreign names must be transcribed into Hangul following the **외래어 표기법** (Loanword Orthography) published by the National Institute of Korean Language (국립국어원, www.korean.go.kr).

#### Common English Phoneme Mappings

| English Sound | Hangul | Example | Hangul |
|---|---|---|---|
| /f/ (initial) | ㅍ | fan, file | 팬, 파일 |
| /v/ | ㅂ | vitamin, video | 비타민, 비디오 |
| /θ/ (voiceless th) | ㅅ | theater, think | 시어터, 싱크 |
| /ð/ (voiced th) | ㄷ | the, this | 더, 디스 |
| /z/ | ㅈ | zebra, zone | 제브라, 존 |
| /ʃ/ (sh) | ㅅ + [i] | she, ship | 시, 십 |
| /ʒ/ | ㅈ | vision, measure | 비전, 메저 |
| /tʃ/ (ch) | ㅊ | chat, change | 채팅, 체인지 |
| /dʒ/ (j) | ㅈ | job, judge | 잡, 저지 |
| /ŋ/ (ng) | ㅇ | running, long | 러닝, 롱 |
| /r/ (initial) | ㄹ | radio, road | 라디오, 로드 |
| /l/ (final) | ㄹ | call, tall | 콜, 톨 |
| /ei/ | 에이 | make, name | 메이크, 네임 |
| /ai/ | 아이 | time, like | 타임, 라이크 |
| /au/ | 아우 | house, mouse | 하우스, 마우스 |
| /ou/ | 오 (not 오우) | go, no | 고, 노 |
| /ju:/ | 유 | you, unit | 유, 유닛 |
| silent e | omitted | name, make | 네임, 메이크 |

#### Personal Name Examples

| English Name | Correct Hangul | Notes |
|---|---|---|
| John | 존 | /dʒ/ → ㅈ |
| Michael | 마이클 | |
| Jennifer | 제니퍼 | /dʒ/ + /f/ |
| Christopher | 크리스토퍼 | |
| Elizabeth | 엘리자베스 | |
| Catherine | 캐서린 | |
| Daniel | 대니얼 | |
| Sarah | 세라 / 사라 | 세라 more common |
| David | 데이비드 | |
| Robert | 로버트 | |
| William | 윌리엄 | |
| James | 제임스 | |
| Mary | 메리 | |
| Thomas | 토머스 / 토마스 | Both in use |
| George | 조지 | |
| Helen | 헬렌 | |
| Susan | 수잔 / 수전 | |
| Edward | 에드워드 | |
| Richard | 리처드 | |
| Charles | 찰스 | |

#### Surname Examples

| English Surname | Correct Hangul |
|---|---|
| Smith | 스미스 |
| Johnson | 존슨 |
| Williams | 윌리엄스 |
| Brown | 브라운 |
| Jones | 존스 |
| Garcia | 가르시아 |
| Miller | 밀러 |
| Davis | 데이비스 |
| Rodriguez | 로드리게스 |
| Martinez | 마르티네스 |

### 5.2 Company and Brand Names

| English | Official Korean | Notes |
|---|---|---|
| Google | 구글 | Official |
| Microsoft | 마이크로소프트 | Official; often shortened to MS |
| Apple | 애플 | Official |
| Samsung | 삼성 | Korean company: use Korean |
| Hyundai | 현대 | Korean company: use Korean |
| LG | LG (엘지) | Often keeps English letters |
| SK | SK (에스케이) | Often keeps English letters |
| Starbucks | 스타벅스 | Official |
| McDonald's | 맥도날드 | Official |
| Nike | 나이키 | Official |
| Coca-Cola | 코카콜라 | 또는 코카-콜라 |
| Facebook | 페이스북 | Official; now Meta (메타) |
| Instagram | 인스타그램 | Often shortened to 인스타 |
| Netflix | 넷플릭스 | Official |
| YouTube | 유튜브 | Official |
| Twitter / X | 트위터 / X | Twitter legacy name still common |
| LinkedIn | 링크드인 | Official |
| Amazon | 아마존 | Official |
| Tesla | 테슬라 | Official |
| BMW | BMW | Keeps English letters |
| IKEA | 이케아 | Official |

**Rules:**
- Use the **official Korean brand name** whenever it exists (registered trademark in Korea).
- For companies without an official Korean name, apply 외래어 표기법.
- Korean companies (Samsung, LG, Hyundai, Kia, etc.) should use their Korean names (삼성, LG, 현대, 기아) in Korean text.
- Global acronyms (BMW, IBM, NASA, FBI) generally keep their English form.

### 5.3 Well-Known Historical / Public Figures

| English | Established Korean | Notes |
|---|---|---|
| Albert Einstein | 알베르트 아인슈타인 | Well-established |
| William Shakespeare | 윌리엄 셰익스피어 | Well-established |
| Steve Jobs | 스티브 잡스 | Well-established |
| Jane Austen | 제인 오스틴 | Well-established |
| Ludwig van Beethoven | 루트비히 판 베토벤 | Well-established |
| Leonardo da Vinci | 레오나르도 다빈치 | Well-established |
| Vincent van Gogh | 빈센트 반 고흐 | Well-established |
| Isaac Newton | 아이작 뉴턴 | Well-established |
| Marie Curie | 마리 퀴리 | Well-established |
| Winston Churchill | 윈스턴 처칠 | Well-established |
| Adolf Hitler | 아돌프 히틀러 | Well-established |
| Napoleon Bonaparte | 나폴레옹 보나파르트 | Well-established |
| Sigmund Freud | 지그문트 프로이트 | Well-established |
| Friedrich Nietzsche | 프리드리히 니체 | Well-established |
| Karl Marx | 카를 마르크스 | Well-established |

**Rule:** Use the already-established Korean transcription for well-known figures. Do not re-transcribe them.

### 5.4 Geographic Names

| English | Korean | Notes |
|---|---|---|
| United States | 미국 | Common exonym |
| United Kingdom | 영국 | Common exonym |
| Germany | 독일 | Common exonym |
| France | 프랑스 | |
| China | 중국 | Common exonym |
| Japan | 일본 | Common exonym |
| Russia | 러시아 | |
| Australia | 호주 / 오스트레일리아 | 호주 more common |
| Canada | 캐나다 | |
| Italy | 이탈리아 | |
| Spain | 스페인 | |
| Switzerland | 스위스 | |
| Sweden | 스웨덴 | |
| New York | 뉴욕 | |
| Los Angeles | 로스앤젤레스 | |
| Washington, D.C. | 워싱턴 D.C. | |
| London | 런던 | |
| Paris | 파리 | |
| Berlin | 베를린 | |
| Tokyo | 도쿄 | |
| Beijing | 베이징 | |
| Pacific Ocean | 태평양 | |
| Atlantic Ocean | 대서양 | |
| Amazon River | 아마존 강 | +강 (river) suffix |
| Sahara Desert | 사하라 사막 | +사막 (desert) suffix |
| Himalayan Mountains | 히말라야 산맥 | +산맥 (mountain range) suffix |

**Rule:** Countries with Korean exonyms (미국, 영국, 독일, 중국, 일본, etc.) use those. Cities and features follow 외래어 표기법. Add generic geographic terms (강, 산, 호수, 사막, 만, 해협) after foreign names when the meaning is not obvious.

---

## 6. Punctuation

### 6.1 Period (마침표/온점)

Korean uses the **Western period (`.`)** -- NOT the CJK full-width ideographic period (。).

| Source (CJK) | Correct KO | Wrong | Notes |
|---|---|---|---|
| 안녕하세요。 | 안녕하세요. | 안녕하세요。 | 。→ . mandatory |
| 오늘은 월요일。 | 오늘은 월요일. | 오늘은 월요일。 | Same rule |
|。 | . |。| Always convert |

**Spacing rule:** No space before period. One space after period (standard Western spacing applies in Korean too).

### 6.2 Comma (쉼표/반점)

Korean uses the **Western comma (`,`)** -- NOT the CJK ideographic comma (、).

| Source (CJK) | Correct KO | Wrong | Notes |
|---|---|---|---|
| 사과、배、복숭아 | 사과, 배, 복숭아 | 사과、배、복숭아 | 、→ , mandatory |
| 그러나、 | 그러나, | 그러나、 | Same rule |
| 1、2、3 | 1, 2, 3 | 1、2、3 | Same rule |

**Spacing rules for commas:**
- **No space before** the comma (attach to preceding character)
- One space **after** the comma (optional in traditional Korean typesetting but standard in modern usage)
- In pure Korean text, commas are used more sparingly than in English -- do not add commas where they are not needed

### 6.3 Quotation Marks (따옴표)

Korean uses several quotation styles. The recommended style for translated documents is **standard Western double quotes**.

| Style | Marks | Usage in Translation |
|---|---|---|
| **Western double** (standard) | `" "` | Default for all translated documents |
| **Western single** | `' '` | Quotes within quotes |
| Korean double (겹낫표) | `「 」` | Literary/traditional; convert to `" "` in translation |
| Korean single (홑낫표) | `『 』` | Book titles; convert to `" "` or keep per style guide |

| Source (CJK quotes) | Correct KO | Wrong | Notes |
|---|---|---|---|
| 「안녕하세요」 | "안녕하세요" | 「안녕하세요」 | Convert to Western |
| 『소나기』 | "소나기" | | Book title |
| 「 」 | " " | | Universal conversion |

| EN Source | KO Translation |
|---|---|
| He said, "Hello." | 그는 "안녕하세요."라고 말했다. |
| She asked, "What is this?" | 그녀가 "이게 뭐예요?"라고 물었다. |
| The term 'algorithm' | '알고리즘'이라는 용어 |
| He replied, "She said, 'I'll be there.'" | 그는 "그녀가 '거기 갈게'라고 말했어."라고 대답했다. |

**Quotation spacing rules:**
- Opening `"`: no space after before speech
- Closing `"`: no space before, but space after if a particle follows: `"안녕"이라고`
- If the quote ends a sentence, place the period inside: `"안녕하세요."`

### 6.4 Parentheses and Brackets

| Symbol | Korean Name |
|---|---|
| `( )` | 소괄호 / 괄호 |
| `[ ]` | 대괄호 / 각괄호 |
| `{ }` | 중괄호 |

| Source (EN) | KO Translation |
|---|---|
| See Fig. 1 | (그림 1) 참조 |
| The results [Table 2] | 결과 [표 2] 참조 |
| Seoul (the capital) | 서울 (수도) |

### 6.5 Ellipsis

| Source | KO | Notes |
|---|---|---|
| ... | ... | 3 dots standard |
| And then... | 그리고 나서... | |
| "Well..." | "글쎄..." | |

**Rule:** Both 3-dot (`...`) and 6-dot (`......`) ellipses are used in Korean. The 3-dot form is more common in modern digital content.

### 6.6 Dash and Hyphen / Range

| Symbol | Korean Name | Function |
|---|---|---|
| `-` | 하이픈 / 붙임표 | Compound words, hyphenation |
| `--` / `—` | 줄표 / 대시 | Sentence break, interruption |
| `~` | 물결표 | **Range indicator** (preferred over `-` in KO) |

| Source (EN) | KO | Notes |
|---|---|---|
| well-known author | 잘 알려진 작가 | Hyphen absorbed in KO |
| pages 10-20 | 10~20쪽 | Use ~ for ranges |
| 2024-2025 | 2024~2025년 | ~ for year ranges |
| Seoul-Busan route | 서울~부산 노선 | Route range |
| 3-5 business days | 3~5영업일 | |
| Open Mon-Fri | 월~금 영업 | |
| "I think--" he said | "제 생각은--" 그가 말했다 | Em-dash retained |
| 9:00 AM - 5:00 PM | 09:00~17:00 | |

**Critical rule:** In Korean, ranges and spans use `~` (물결표), NOT the hyphen `-` or en-dash `–` used in English.

### 6.7 Question Mark and Exclamation Mark

Used identically to English. No space before `?` or `!`.

| Source | KO |
|---|---|
| What is this? | 이게 뭐예요? |
| Help! | 도와주세요! |
| Really? | 정말요? |

### 6.8 Middle Dot (가운뎃점)

The middle dot `·` is used for enumerated lists within a sentence, especially for Sino-Korean items.

| Source (EN) | KO (with ·) |
|---|---|
| East, West, South, North | 동·서·남·북 |
| January, February, March | 1월·2월·3월 |
| Kim, Lee, Park (family names) | 김·이·박 |

### 6.9 Comprehensive Korean Spacing Rules (띄어쓰기)

Korean word spacing is mandatory between words but has specific rules for particles.

| Rule | Correct | Wrong |
|---|---|---|
| Particles attach to preceding word | 학교에 간다 | 학교 에 간다 |
| | 사과가 맛있다 | 사과 가 맛있다 |
| | 책을 읽는다 | 책 을 읽는다 |
| Counters separated from number | 3개, 5명 | 3개, 5명 |
| Compound words may fuse | 컴퓨터 프로그램 or 컴퓨터프로그램 | (both acceptable) |
| Spaces between words | 나는 학교에 간다. | 나는학교에간다. |
| Auxiliary verb spacing | 읽어 보다 / 읽어보다 | (both acceptable) |

---

## 7. Formatting

### 7.1 Title Hierarchy

| Level | Korean Convention | Example |
|---|---|---|
| Document title | Bold, centered | 문서 제목 |
| Chapter | 제N장 | 제1장 서론 |
| Section | 제N절 | 제1절 연구 배경 |
| Subsection | N. | 1. 연구 목적 |
| Sub-subsection | N.N | 1.1 연구 범위 |
| Paragraph | 가./ㄱ. | 가. 세부 내용 |

**Alternative numbering (Western-style):**

| Level | Example |
|---|---|
| H1 | # 1. 서론 |
| H2 | ## 1.1 연구 배경 |
| H3 | ### 1.1.1 연구 목적 |
| H4 | #### 1.1.1.1 세부 내용 |

**Cross-reference labels:**

| English | Korean |
|---|---|
| Chapter 1 | 제1장 |
| Section 2 | 제2절 |
| Article 5 | 제5조 |
| Figure 1 | 그림 1 |
| Table 2 | 표 2 |
| Appendix A | 부록 A |
| Page 10 | 10페이지 (p. 10) |

### 7.2 List Markers

| Type | Marker | Example |
|---|---|---|
| Unordered bullet | `•` | • 첫 번째 항목 |
| Unordered hyphen | `-` | - 첫 번째 항목 |
| Ordered numeric | `1.` | 1. 첫 번째 단계 |
| Ordered paren | `1)` | 1) 첫 번째 단계 |
| Ordered double paren | `(1)` | (1) 첫 번째 단계 |
| Korean alphabetic | `가.` | 가. 첫째 이유 |
| Korean alphabetic 2 | `ㄱ.` | ㄱ. 첫째 이유 |

### 7.3 Table Formatting

| EN Header | KO Header |
|---|---|
| Name | 이름 |
| Department | 부서 |
| Position | 직위 |
| Contact | 연락처 |
| Quantity | 수량 |
| Unit Price | 단가 |
| Amount | 금액 |
| Remarks | 비고 |

**Table rules:**
- Translate all headers
- Maintain column alignment: text left, numbers right
- Currency in header row or appended to each value (consistent)
- Keep table structure identical to source

### 7.4 Numbered List Examples

| Source (EN) | KO Translation |
|---|---|
| 1. First, prepare the materials. | 1. 먼저 재료를 준비합니다. |
| 2. Next, mix the ingredients. | 2. 다음으로 재료를 혼합합니다. |
| 3. Finally, bake for 30 minutes. | 3. 마지막으로 30분간 굽습니다. |

### 7.5 Emphasis Styles

| Style | Korean Name | Usage Notes |
|---|---|---|
| **Bold** | 굵게 / 진하게 | Preferred emphasis method |
| *Italic* | 기울임 / 이탤릭 | Less common in traditional KO; accept in translated docs |
| <u>Underline</u> | 밑줄 | Same usage as EN |
| ~~Strikethrough~~ | 취소선 | Same usage as EN |

---

## 8. Grammar

### 8.1 Word Order: Subject-Object-Verb (SOV)

Korean is a strict **SOV** language. The verb **always** comes at the end of the sentence. This is the most critical grammatical difference from English (SVO).

| Source (EN, SVO) | KO Translation (SOV) | Literal gloss |
|---|---|---|
| I eat an apple. | 나는 사과를 먹는다. | I apple eat |
| She reads a book. | 그녀는 책을 읽는다. | She book reads |
| He wrote a letter. | 그는 편지를 썼다. | He letter wrote |
| The dog chased the cat. | 개가 고양이를 쫓았다. | Dog cat chased |
| We will meet tomorrow. | 우리는 내일 만날 것이다. | We tomorrow will meet |
| I put the book on the table. | 나는 책을 탁자 위에 놓았다. | I book table-on put |
| She gave me a gift. | 그녀는 나에게 선물을 주었다. | She me gift gave |
| He was born in Seoul. | 그는 서울에서 태어났다. | He Seoul-in was-born |
| They are building a house. | 그들은 집을 짓고 있다. | They house building are |
| I have finished the report. | 나는 보고서를 끝냈다. | I report finished |

**SOV implications:**
- Adverbs precede the verb: `빨리 달리다` (quickly run), `조용히 말하다` (quietly speak)
- Time expressions precede place: `어제 학교에서 만났다` (yesterday at-school met)
- Negation wraps the verb: `가지 않다`, `안 가다`
- Relative clauses precede the noun: `내가 어제 만난 사람` (I yesterday met person = the person I met yesterday)

### 8.2 Particles (조사)

Particles are postpositional markers attached to nouns. They indicate grammatical function.

#### 8.2.1 Subject Particles: 이/가

| Particle | After | Example |
|---|---|---|
| 이 | Consonant | 책**이** 있다 (There is a book) |
| 가 | Vowel | 사과**가** 있다 (There is an apple) |
| 께서 | (honorific) | 선생님**께서** 오셨다 |

#### 8.2.2 Topic Particles: 은/는

| Particle | After | Example |
|---|---|---|
| 은 | Consonant | 나**는** 학생이다 |
| 는 | Vowel | 그**는** 선생님이다 |

**은/는 vs 이/가:** 은/는 marks topic or contrast. 이/가 marks neutral subject focus.

| Example | Implication |
|---|---|
| **내가** 갈게 (I will go) | Focus on "I" -- who will go? I will. |
| **나는** 갈 거야 (As for me, I'll go) | Topic -- contrast with others |
| **이** 책이 좋다 (This book is good) | Specific subject focus |
| **이** 책은 좋다 (This book is good) | Topic/contrast |

#### 8.2.3 Object Particles: 을/를

| Particle | After | Example |
|---|---|---|
| 을 | Consonant | 책**을** 읽다 |
| 를 | Vowel | 사과**를** 먹다 |

#### 8.2.4 Other Essential Particles

| Particle | Function | Example | Meaning |
|---|---|---|---|
| 에 | Time / place (destination) | 학교**에** 가다 | to school |
| 에서 | Action location | 도서관**에서** 공부하다 | study at library |
| 로 / 으로 | Direction / means | 버스**로** 가다 | by bus |
| 와 / 과 | "and / with" (formal) | 친구**와** | with friend |
| 하고 | "and / with" (neutral) | 친구**하고** | with friend |
| (이)랑 | "and / with" (casual) | 친구**랑** | with friend |
| 부터 | "from" (time/place) | 아침**부터** | from morning |
| 까지 | "until / to" | 저녁**까지** | until evening |
| 도 | "also / even" | 나**도** | me too |
| 만 | "only" | 이것**만** | only this |
| 의 | Possession / attributive | 나**의** 책 | my book |
| (이)나 | "or" / "as many as" | 커피**나** | coffee or... |

**Particle omission:** In casual speech, particles are sometimes omitted, but in written translation, they should **always** be included for grammatical correctness.

### 8.3 Verb Conjugation Overview

| Tense | Formal (합쇼체) | Polite (해요체) | Plain (해라체) |
|---|---|---|---|
| Present | 먹습니다 | 먹어요 | 먹는다 |
| Past | 먹었습니다 | 먹었어요 | 먹었다 |
| Future | 먹을 것입니다 | 먹을 거예요 | 먹을 것이다 |
| Progressive | 먹고 있습니다 | 먹고 있어요 | 먹고 있다 |
| Past Perfect | 먹었었습니다 | 먹었었어요 | 먹었었다 |
| Prospective | 먹겠습니다 | 먹을게요 | 먹겠다 |

### 8.4 Honorific System (존대법)

Korean has a grammatical honorific system integrated into verb morphology.

#### Subject Honorific: -시-

Add `-시-` between the verb stem and ending when the subject is a person deserving respect.

| Base | Honorific | Meaning |
|---|---|---|
| 가다 | 가**시**다 | (respected person) goes |
| 먹다 | 잡수**시**다 / 드**시**다 | eats |
| 읽다 | 읽으**시**다 | reads |
| 있다 | 계**시**다 | exists/stays (for people) |
| 자다 | 주무**시**다 | sleeps |
| 말하다 | 말씀하**시**다 | speaks |

#### Honorific Vocabulary Substitutions

| Neutral | Honorific | English |
|---|---|---|
| 먹다 | 잡수시다 / 드시다 | eat |
| 자다 | 주무시다 | sleep |
| 있다 | 계시다 | exist / be (for people) |
| 말하다 | 말씀하시다 | speak |
| 주다 | 드리다 | give (humble) |
| 데리다 | 모시다 | bring (a person, humbly) |
| 보다 | 뵙다 / 뵈다 | see (humble) |
| 묻다 | 여쭈다 / 여쭈보다 | ask (humble) |
| 이름 | 성함 | name |
| 나이 | 연세 | age |
| 집 | 댁 | house |
| 사람 | 분 | person |
| 생일 | 생신 | birthday |
| 말 | 말씀 | words/speech |
| 아내 | 부인 | wife |
| 아들 / 딸 | 아드님 / 따님 | son / daughter |
| 밥 | 진지 | meal/rice |
| 병환 | 병환 / 병환 | illness (polite) |

#### Honorific Examples in Sentences

| Neutral | Honorific |
|---|---|
| 할머니가 밥을 먹었다. | 할머니께서 진지를 잡수셨다. |
| 선생님이 학교에 있다. | 선생님께서 학교에 계신다. |
| 아버지가 주무신다. | 아버지께서 주무신다. |
| 할아버지가 신문을 읽는다. | 할아버지께서 신문을 읽으신다. |

### 8.5 Connective Endings

| Ending | Function | Example | Meaning |
|---|---|---|---|
| -고 | "and" (sequential) | 먹**고** 잤다 | ate and slept |
| -서 | "so / and" (causal) | 비가 와**서** 집에 있다 | It's raining so I'm home |
| -지만 | "but / although" | 비싸**지만** 산다 | expensive but buy |
| -는데 | background / "and" | 가**는데** | So I'm going and... |
| -(으)면 | "if / when" | 비가 오**면** | if it rains |
| -(으)니까 | "because" | 하**니까** 좋다 | good because (I) do it |
| -(으)려고 | "in order to" | 보**려고** 왔다 | came to see |
| -도록 | "so that" | 알**도록** 말하다 | speak so (they) understand |
| -지만 | "although" | 작**지만** 강하다 | small but strong |
| -다가 | "while doing / and then" | 공부하**다가** 잤다 | was studying and fell asleep |

### 8.6 Adnominal Modifiers (관형사형)

These are equivalent to English relative clauses but placed **before** the noun.

| Form | Tense | Example | Meaning |
|---|---|---|---|
| -는 | Present | 먹**는** 사람 | person who eats |
| -은 / -ㄴ | Past | 먹**은** 사람 | person who ate |
| -을 / -ㄹ | Future | 먹**을** 사람 | person who will eat |
| -던 | Retrospective | 먹**던** 사람 | person who used to eat |

| Source (EN) | KO Translation |
|---|---|
| the man who came | **온** 사람 |
| the book I read yesterday | 내가 어제 **읽은** 책 |
| a house that costs $500,000 | 50만 달러**인** 집 |
| the movie that everyone is talking about | 모두가 **이야기하는** 영화 |

### 8.7 Passive and Causative

| Type | Suffix | Example | Meaning |
|---|---|---|---|
| Passive | -이/히/리/기 | 보**이다**, 먹**히다**, 들**리다** | be seen, be eaten, be heard |
| Causative | -이/히/리/기/우/추 | 먹**이다**, 살**리다**, 돌**리다** | feed, save, rotate |

**Active vs Passive preference:** Korean prefers active voice. Avoid translating English passive constructions literally.

| Source (EN passive) | Literal (bad) | Natural (good) |
|---|---|---|
| The report was written by John. | 보고서가 존에 의해 작성되었다. | 존이 보고서를 작성했다. |
| The window was broken. | 창문이 깨졌다. (acceptable) | (passive with -지다 is natural) |
| It is said that... | 그것은 ...라고 말해진다. | ...라고 한다. |

---

## 9. Formality

### 9.1 Speech Levels Overview

Korean has six speech levels. Three are actively used in modern translation:

| Level | Style | Ending | Formality | Usage |
|---|---|---|---|---|
| **합쇼체** | Formal polite | -ㅂ니다 / -습니다 | Highest | Official docs, news, presentations, business letters |
| **해요체** | Informal polite | -요 | Medium | General conversation, customer service, most written content |
| **해체** | Informal casual | 반말 (no ending) | Low | Close friends, family, informal situations |
| **해라체** | Formal plain | -다 | Impersonal | Newspapers, academic writing, diaries, novels |
| 하게체 | Moderate formal | -게 | Archaic | Older generation speech, historical literature |
| 하소서체 | Extremely formal | -소서 | Archaic | Prayers, historical texts, royal decrees |

### 9.2 Formality Selection by Document Type

| Document Type | Recommended Level | Example Sentence |
|---|---|---|
| Legal contract | 합쇼체 | 본 계약은 체결일로부터 효력이 발생합니다. |
| Government notice | 합쇼체 | 위와 같이 공고합니다. |
| Business report | 합쇼체 | 보고드립니다. |
| Technical manual | 해요체 / 해라체 | 다음 단계를 따르십시오. |
| News article | 해라체 (-다) | 오늘 서울에 눈이 내렸다. |
| Academic paper | 해라체 | 실험 결과를 분석하였다. |
| Marketing copy | 해요체 / 합쇼체 | 지금 바로 구매하세요! |
| Mobile UI / App | 해요체 | 설정을 확인해 주세요. |
| Formal email | 합쇼체 | 안녕하십니까? |
| Semi-formal email | 해요체 | 안녕하세요? |
| Internal memo | 해요체 / 해체 | 회의는 3시입니다. |
| Chat / SNS | 해체 | 알겠어. |
| Children's content | 해요체 | 재미있지요? |
| Novel (narrative) | 해라체 | 그는 문을 열었다. |
| Novel (dialogue) | Varies by character | Varies |

### 9.3 Degree of Formality Spectrum

```
Most formal                          Least formal
합쇼체  →  해요체  →  하게체  →  해라체  →  해체
(-습니다)  (-요)      (-게)      (-다)      (반말)
```

### 9.4 Level-Shifting Examples (Same Sentence Across Levels)

| Sentence | 합쇼체 | 해요체 | 해체 / 해라체 |
|---|---|---|---|
| Please wait. | 기다려 주십시오. | 기다려 주세요. | 기다려. |
| I understand. | 알겠습니다. | 알겠어요. | 알겠어. / 알겠다. |
| Thank you. | 감사합니다. | 고마워요. | 고마워. |
| Is that correct? | 맞습니까? | 맞아요? | 맞아? / 맞느냐? |
| I will do it. | 제가 하겠습니다. | 제가 할게요. | 내가 할게. |
| Please come in. | 들어오십시오. | 들어오세요. | 들어와. |
| I'm sorry. | 죄송합니다. | 미안해요. | 미안해. |
| See you later. | 나중에 뵙겠습니다. | 나중에 봐요. | 나중에 봐. |
| What is your name? | 성함이 어떻게 되십니까? | 이름이 뭐예요? | 이름이 뭐야? |
| Nice to meet you. | 만나서 반갑습니다. | 만나서 반가워요. | 반가워. |
| Please sign here. | 여기에 서명해 주십시오. | 여기에 서명해 주세요. | 여기 서명해. |

### 9.5 Professional Correspondence

| Context | Korean Phrase | Level |
|---|---|---|
| Formal salutation | 안녕하십니까? | 합쇼체 |
| Semi-formal salutation | 안녕하세요? | 해요체 |
| Self-introduction (formal) | 먼저 OOO 팀장 OOO입니다. | 합쇼체 |
| Request (formal) | ...해 주시기 바랍니다. | 합쇼체 |
| Request (polite) | ...해 주세요. | 해요체 |
| Appreciation (formal) | 진심으로 감사드립니다. | 합쇼체 |
| Appreciation (polite) | 감사합니다. | 합쇼체 |
| Apology (formal) | 깊이 사과드립니다. | 합쇼체 |
| Apology (polite) | 죄송합니다. | 합쇼체 |
| Confirmation | ...을 확인해 드립니다. / ...을 확인드립니다. | 합쇼체 |
| Closing (formal) | 감사합니다. / 고맙습니다. | 합쇼체 |
| Closing (semi-formal) | 감사합니다. | 해요체/합쇼체 |

### 9.6 "당신" Avoidance

Korean strongly avoids the second-person pronoun 당신. Use alternatives:

| Source (EN, "you") | Avoid (bad) | Natural (good) |
|---|---|---|
| What do you think? | 당신은 어떻게 생각합니까? | 어떻게 생각하세요? |
| You should do this. | 당신은 이것을 해야 합니다. | 이것을 하셔야 합니다. |
| I will send it to you. | 당신에게 보내겠습니다. | 보내 드리겠습니다. |
| You are right. | 당신이 맞습니다. | 맞습니다. / 맞아요. |
| Do you like it? | 당신은 그것을 좋아합니까? | 마음에 드세요? |
| Are you Mr. Kim? | 당신이 김 씨입니까? | 김 씨 맞으십니까? |
| You need to be careful. | 당신은 조심해야 합니다. | 조심하셔야 합니다. |

**Strategies:**
1. Omit the subject entirely (most common)
2. Use the person's title/name + honorific: `선생님`, `사장님`, `김 대리`
3. Use `-시-` honorific on the verb to implicitly mark the subject
4. Use `쪽` (side): `고객님 쪽에서 결정해 주십시오.`

---

## 10. OCR Artifacts

### 10.1 Restoration Notation Format

When restoring corrupted or uncertain text from OCR output, use the following notation:

**Format:** `[복원: 오류텍스트 → 올바른텍스트]`

| OCR Output (Error) | Restored (With Notation) | Notes |
|---|---|---|
| 안녕하세Ω | [복원: Ω → 요] 안녕하세요 | Greek Omega misrecognized as 요 |
| cjalfdls | [복원: cjalfdls → 확인합니다] | Full jamo corruption |
| 0| | [복원: 0| → 이] | Zero + pipe → Hangul 이 |
| 1�요 | [복원: 1�요 → 있어요] | Encoding corruption |
| OI | [복원: OI → 이] | Latin letters → Hangul |
| ql | [복원: ql → 을] | Common misrecognition |
| 오늘온 맑음 | [복원: 오늘온 → 오늘은] 맑음 | 은/온 confusion |
| 감사합나다 | [복원: 감사합나다 → 감사합니다] | 합나다 → 합니다 |
| OI런 OI유 | [복원: OI런 OI유 → 이런 이유] | Full corruption |

### 10.2 Common OCR Confusion Patterns in Korean

| Symbol/Char | Often Confused With | Correct Form |
|---|---|---|
| 요 | Ω (Omega), 8, 0 | 요 |
| 이 | OI, 0\, 0l | 이 |
| 을 | ql, 01 | 을 |
| 는 | = , 2 | 는 |
| 하 | 다 (blurry), 타 | 하 |
| ㅇ (initial) | O, 0 | ㅇ |
| ㅂ | 6, b | ㅂ |
| ㅈ | 7, ㅣ | ㅈ |
| ㅐ | ㅔ | Verify by context |
| ㅓ | ㅏ | Verify by context |
| ㅗ | ㅛ (missing stroke) | ㅗ |
| 습 | 습 (broken) | 습 |
| 있 | 있 | 있 |

### 10.3 Restoration Rules

1. **Always annotate** when OCR text is dubious, contains unreadable characters, or has been algorithmically restored.
2. Use `[복원: ...]` brackets for corrected text.
3. For multiple corrections in one phrase: `[복원: ΩI 己卜ΩI → 여기 있어요]`.
4. If the original OCR text is entirely corrupted and unrecoverable: `[복원불가]`.
5. When restoring, maintain original meaning -- do not rephrase for style.
6. Do not use restoration notation for obvious typos in clearly readable text.
7. If restoring a single character, annotate the character: `[복원: Ω → 요]`.

| Scenario | Notation |
|---|---|
| Single char corrupt | `[복원: Ω → 요] 안녕하세요` |
| Word corrupt | `[복원: cjalfdls → 확인합니다]` |
| Phrase corrupt | `[복원: ΩI 己卜ΩI → 여기 있어요]` |
| Totally unreadable | `[복원불가]` |
| Uncertain restoration | `[복원추정: ...일 가능성 높음]` |

---

## 11. Translation Philosophy

### 11.1 Natural Korean Over Literal Translation

The cardinal rule: prioritize **natural, idiomatic Korean** over word-for-word literalism.

| Source (EN) | Literal (Bad) | Natural (Good) | Why |
|---|---|---|---|
| I have a cold. | 나는 감기를 가지고 있다. | 감기에 걸렸어요. / 감기에 걸렸습니다. | "가지다" (have) is not used for illnesses |
| What is your name? | 당신의 이름은 무엇입니까? | 성함이 어떻게 되세요? / 이름이 뭐예요? | Avoid 당신 |
| I am 25 years old. | 나는 25년이다. | 저는 25살입니다. | Age counter is 살, not 년 |
| It is raining cats and dogs. | 고양이와 개가 내리고 있다. | 비가 억수같이 쏟아진다. | Idiom requires KO equivalent |
| I am hungry. | 나는 배고프다. | 배고파요. / 배가 고픕니다. | Natural KO form |
| Can I help you? | 나는 당신을 도울 수 있습니까? | 도와드릴까요? / 무엇을 도와드릴까요? | Service phrase |
| I don't know. | 나는 알지 못한다. | 모르겠습니다. / 몰라요. | Natural hedge |
| It's up to you. | 그것은 당신에게 달려 있다. | 선택은 당신의 몫입니다. / 결정하세요. | Idiomatic |
| That makes sense. | 그것은 감각을 만든다. | 이해가 되네요. / 말이 되네요. | Literal is nonsense |
| I'm looking forward to it. | 나는 그것을 앞으로 바라보고 있다. | 기대됩니다. / 기대하고 있습니다. | Fixed expression |
| How are you? | 당신은 어떻게 지냅니까? | 어떻게 지내세요? / 잘 지내셨어요? | Avoid 당신 |
| Let's keep in touch. | 접촉을 유지합시다. | 연락 자주 합시다. / 계속 연락해요. | "접촉" has wrong connotation |
| I'm on my way. | 나는 내 길 위에 있다. | 가고 있어요. / 가는 중입니다. | Idiomatic expression |
| Nice to meet you. | 당신을 만나서 좋다. | 만나서 반갑습니다. / 반가워요. | Fixed expression |
| See you tomorrow. | 내일 당신을 봅니다. | 내일 봐요. / 내일 뵙겠습니다. | Fixed expression |
| I'm fine, thank you. | 나는 괜찮다, 감사합니다. | 잘 지냈습니다. / 네, 괜찮아요. | Conversational formula |
| I miss you. | 나는 당신을 놓친다. | 보고 싶어요. / 보고 싶습니다. | "Miss" is not "놓치다" |
| My phone died. | 내 전화기가 죽었다. | 핸드폰이 꺼졌어요. / 배터리가 나갔어요. | Literal sounds violent |
| I got it. (understand) | 나는 그것을 얻었다. | 알겠습니다. / 이해했습니다. | Context-dependent |

### 11.2 Loanwords (외래어) vs Native Korean (순우리말)

| Domain | Preference | Examples |
|---|---|---|
| IT / Technology | 외래어 preferred | 컴퓨터, 데이터, 네트워크, 소프트웨어, 하드웨어, 클라우드 |
| Business / Management | Mixed | 전략 (strategy), 매니지먼트 (management), 리더십 (leadership) |
| Law / Government | Sino-Korean preferred | 계약, 당사자, 의무, 권리, 법률 |
| Medicine | Sino-Korean + loanwords | 진단 (diagnosis), 수술 (surgery), 바이러스 (virus) |
| Academia | Sino-Korean preferred | 분석, 연구, 이론, 방법론 |
| Arts / Literature | Context-dependent | 감성, 표현, 장르 (genre) |
| Daily life | Mixed by convention | 버스 (bus), 택시 (taxi), 커피 (coffee), 피자 (pizza) |

### 11.3 Loanword vs Korean Equivalent: Decision Guide

| English | Loanword (외래어) | Korean Equivalent | Recommendation |
|---|---|---|---|
| computer | 컴퓨터 | 계산기 (wrong, means calculator) | Always 컴퓨터 |
| internet | 인터넷 | 누리망 (obsolete) | Always 인터넷 |
| email | 이메일 | 전자우편 | 이메일 (common), 전자우편 (formal)
| smartphone | 스마트폰 | 지능형 휴대전화 (verbose) | Always 스마트폰 |
| Wi-Fi | 와이파이 | 무선랜 | 와이파이 (common) |
| application | 애플리케이션 (앱) | 응용 프로그램 | 앱 (common), 응용 프로그램 (formal) |
| update | 업데이트 | 갱신 | 업데이트 (common), 갱신 (formal/technical) |
| download | 다운로드 | 내려받기 | 다운로드 (common) |
| upload | 업로드 | 올리기 | 업로드 (common) |
| file | 파일 | 문서철 (rare) | Always 파일 |
| feedback | 피드백 | 의견/소감 | 피드백 acceptable |
| deadline | 데드라인 | 마감일 | 마감일 preferred |
| meeting | 미팅 | 회의 | 회의 (formal), 미팅 (casual) |
| team | 팀 | 조직/집단 | Always 팀 (in org context) |
| schedule | 스케줄 | 일정 | 일정 preferred, 스케줄 OK |
| project | 프로젝트 | 사업/과제 | 프로젝트 (common), 사업 (business) |
| service | 서비스 | 봉사 (too narrow) | Always 서비스 |
| system | 시스템 | 체계 | 시스템 (common), 체계 (formal) |
| data | 데이터 | 자료 | 데이터 (raw), 자료 (processed) |
| quality | 퀄리티 | 품질 | 품질 preferred in formal |
| option | 옵션 | 선택 사항 | 옵션 (common) |
| detail | 디테일 | 세부 사항 | 세부 사항 preferred in formal |
| review | 리뷰 | 검토/평가 | 검토 (formal), 리뷰 (casual) |
| support | 서포트 | 지원 | Always 지원 |
| management | 매니지먼트 | 관리/경영 | 관리/경영 preferred |
| strategy | 스트래티지 | 전략 | Always 전략 |
| partner | 파트너 | 동업자 | 파트너 (common) |
| content | 콘텐츠 | 내용물 (differs) | Always 콘텐츠 (digital) |
| comment | 댓글 (online) | 코멘트 | 댓글 (web), 코멘트 (general) |
| trend | 트렌드 | 추세 | 트렌드 (casual), 추세 (formal) |
| issue | 이슈 | 문제/쟁점 | 이슈 (common), 문제/쟁점 (formal) |
| fact | 팩트 | 사실 | 팩트 (colloquial), 사실 (standard) |

### 11.4 Common Translation Pitfalls

#### False Cognates / Literal Traps

| Source (EN) | Mistranslation (Bad) | Correct (Good) |
|---|---|---|
| I have a dog. | 나는 개를 가지고 있다. | 개가 있어요. |
| I think so. | 나는 그렇게 생각한다. | 그런 것 같아요. / 그렇습니다. |
| You're welcome. | 당신은 환영합니다. | 천만에요. / 별말씀을요. |
| I don't mind. | 나는 마음에 들지 않는다. | 괜찮아요. / 상관없어요. |
| Of course. | 물론입니다. | 물론이죠. / 그럼요. |
| Actually,... | 실제로,... (too literal) | 사실은,... / 실은,... |
| Excuse me. | 실례합니다. (only for formal) | 잠시만요. (attention) / 실례합니다. (passing) |
| Bless you! | 신의 축복이 있기를! | (No direct equivalent; just move on or say 건강하세요) |
| I played the game. | 나는 게임을 연주했다. | 게임을 했어요. (연주하다 = play a musical instrument) |
| I took a picture. | 나는 사진을 가져갔다. | 사진을 찍었어요. |
| I spent money. | 나는 돈을 보냈다. | 돈을 썼어요. (보내다 = send) |
| He runs a company. | 그는 회사를 달린다. | 그는 회사를 운영한다. |
| I'm in a meeting. | 나는 회의 안에 있다. | 회의 중입니다. |

#### Overuse of "그것" (It/That)

English "it" is used far more frequently than Korean "그것." Omit or rephrase.

| Source (EN) | Bad (overusing 그것) | Good (natural) |
|---|---|---|
| I know it. | 나는 그것을 안다. | 알아요. / 알고 있습니다. |
| I like it. | 나는 그것을 좋아한다. | 좋아해요. / 마음에 들어요. |
| Please check it. | 그것을 확인해 주세요. | 확인해 주세요. |
| I bought it yesterday. | 나는 그것을 어제 샀다. | 어제 샀어요. |
| Can you fix it? | 그것을 고칠 수 있어요? | 고칠 수 있어요? |

#### Overuse of "나는" (I)

Korean omits the subject pronoun when it is clear from context. Avoid starting every sentence with "나는."

| Source (EN) | Bad (overuse of 나는) | Good (natural) |
|---|---|---|
| I went to school. I studied. I came home. | 나는 학교에 갔다. 나는 공부했다. 나는 집에 왔다. | 학교에 가서 공부하고 집에 왔어요. |
| I think this is a good idea. | 나는 이것이 좋은 생각이라고 생각한다. | 좋은 생각인 것 같습니다. |

### 11.5 Sentence Structure: Break Long Sentences

| Source (EN, long) | Bad (single long KO sentence) | Good (broken into shorter sentences) |
|---|---|---|
| The report that was submitted by the team working on the project started last month has been approved. | 지난달에 시작된 프로젝트에서 작업하고 있는 팀에 의해 제출된 보고서가 승인되었다. | 지난달에 시작된 프로젝트가 있습니다. 해당 프로젝트 팀이 보고서를 제출했으며, 승인되었습니다. |
| Despite the fact that the weather was bad, we decided to go ahead with the event. | 날씨가 나빴다는 사실에도 불구하고, 행사를 강행하기로 결정했다. | 날씨가 나빴지만 행사를 강행하기로 했습니다. |

**Rule:** Keep Korean sentences to 60 characters or fewer when possible. Break compound/complex English sentences into multiple Korean sentences.

### 11.6 Passive Voice Conversion

Korean strongly prefers active voice over passive voice.

| Source (EN, passive) | Literal (bad passive) | Natural (active) |
|---|---|---|
| The experiment was conducted by the team. | 실험이 팀에 의해 수행되었다. | 팀이 실험을 수행했다. |
| It is believed that... | ...라고 믿어지고 있다. | ...라고 여겨진다. / ...라고 본다. |
| The window was broken. | 창문이 깨졌다. (acceptable passive) | (깨지다 is lexical passive, acceptable) |
| The package will be delivered tomorrow. | 패키지가 내일 배달될 것입니다. | 내일 패키지를 배달해 드리겠습니다. |

### 11.7 Cultural Adaptation Guidelines

| Source (EN) | Literal | Adapted KO | Notes |
|---|---|---|---|
| Merry Christmas! | 메리 크리스마스! | 메리 크리스마스! / 즐거운 성탄절 보내세요! | Both common |
| Happy Thanksgiving! | 즐거운 추수감사절! | 추수감사절 (축제) / (Keep with brief explanation) | Less known in KO |
| Trick or treat! | 트릭 오어 트릿! | (Explain or localize for KO kids) | Not a KO custom |
| Groundhog Day | 그래운드호그 데이 | 성촉절 (groundhog day with explanation) | Not known in KO |
| 401(k) | 401(k) | 401(k) 퇴직연금 계좌 | Add explanation |
| SSN (Social Security Number) | SSN | 사회보장번호 (SSN) | Add explanation |
| Potluck | 포틀럭 | (설명: 각자 음식을 가져오는 모임) | Not a KO custom |
| Zip code | 우편번호 | Convert to 우편번호 concept | |
| Junior / Senior (name suffix) | 주니어 / 시니어 | 2세 / 3세 or 그랜드시니어 | |
| Mr./Mrs./Ms. | ~씨 / ~님 | Use Korean honorifics appropriately | |
| First floor / Ground floor | 1층 | 1층 (same in KO) | |
| Bill / Check | 계산서 | 계산서 주세요 / 더치페이 | |
| Tipping | 팁 | 팁 / 봉사료 | Tipping not required in KO |

### 11.8 Consistency Principle

| Element | Rule |
|---|---|
| Terminology | Same EN term = same KO term throughout document |
| Formality level | Do not mix 합쇼체 and 해요체 in same document |
| Name transcription | Once transcribed, use consistently |
| Number format | Decide 만/억 system vs comma grouping and stick to it |
| Date format | Use one format throughout |

### 11.9 Final Quality Check Questions

1. Does the translation read as if written by a native Korean speaker?
2. Are all particles (은/는, 이/가, 을/를) used correctly?
3. Is the formality level appropriate for the document type and audience?
4. Are all numbers, dates, and currency amounts accurate?
5. Are loanwords transcribed according to 외래어 표기법?
6. Is the SOV word order strictly followed?
7. Have English passive constructions been converted to active where appropriate?
8. Are quotation marks and punctuation in Korean style?
9. Has "당신" been avoided where possible?
10. Have long English sentences been broken into shorter Korean sentences?

---

> **References:** 국립국어원 (National Institute of Korean Language) -- 한글 맞춤법, 외래어 표기법, 표준 국어 대사전; 문장 부호 규정; 표준 언어 예절.
