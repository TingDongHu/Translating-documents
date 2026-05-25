---
id: ko/domain/financial
type: domain
target_lang: ko
name: 재무 문서 번역 규정
description: 재무제표, 회계 용어, 감사 보고서, 금융 계약, 증권 관련 문서 번역 규칙
---

## Reader Model (독자 모델)

**누가 이 문서를 읽고 무엇을 기대하는가?**

재무 문서의 독자는 회계사, 감사인, 재무 분석가, 투자자, 금융 규제 기관, 기업의 재무 담당자로서 문서를 통해 기업의 재무 상태와 성과를 평가한다. 다음을 기대한다:

- **한국채택국제회계기준(K-IFRS) 용어 사용** — 한국은 2011년부터 K-IFRS를 의무 채택하였으며, 모든 회계 용어는 K-IFRS에 정의된 대로 사용해야 한다. 일반 기업의 경우 한국채택국제회계기준(일반기업회계기준) 용어를 사용한다.
- **숫자 정보의 절대적 정확성** — 재무제표의 모든 숫자는 정확히 보존되어야 한다. 천 원 단위, 백만 원 단위 등 표시 단위(단위: 천 원)를 명확히 해야 한다.
- **일관된 계정과목명** — 동일한 계정과목(account title)은 모든 문서에서 동일하게 표기되어야 한다. 계정과목명의 불일치는 재무제표의 신뢰성을 훼손한다.
- **감사 의견의 정확한 전달** — 감사 의견(적정, 한정, 부적정, 의견거절)은 법적 효력을 가지므로 정확히 번역되어야 한다.
- **규제 준수 표현** — 금융감독원(DART 전자공시), 한국거래소 공시 규정에 따른 용어와 형식을 준수해야 한다.

**무엇이 신뢰를 무너뜨리는가?**
- K-IFRS 공식 용어와 다른 비표준 용어 사용
- 재무제표 주석의 숫자 불일치
- 감사 의견 등급 오역
- 계정과목명의 문서 내 불일치
- 통화 단위(천 원, 백만 원) 오기 또는 누락
- 한국 회계 기준과 국제 회계 기준 혼동

---

## Decision Framework (의사결정 체계)

### D1: 재무제표 명칭

| 조건 | 결정 |
|------|------|
| Balance Sheet | `재무상태표` (K-IFRS 공식 용어. 구: 대차대조표) |
| Income Statement / P&L | `손익계산서` 또는 `포괄손익계산서` (K-IFRS: `재무성과표` 개념 포함) |
| Statement of Cash Flows | `현금흐름표` (K-IFRS: 현금흐름표) |
| Statement of Changes in Equity | `자본변동표` |
| Notes to Financial Statements | `재무제표 주석` |
| Separate Financial Statements | `별도 재무제표` |
| Consolidated Financial Statements | `연결 재무제표` |
| Auditor's Report / Audit Opinion | `감사 보고서` / `감사 의견` |

### D2: 계정과목 번역

| 조건 | 결정 |
|------|------|
| Current assets | `유동자산` |
| Non-current assets | `비유동자산` (구: 고정자산) |
| Accounts receivable | `매출채권` |
| Accounts payable | `매입채무` |
| Accrued expenses | `미지급비용` |
| Deferred revenue / Unearned revenue | `선수수익` 또는 `선수금` |
| Revenue / Sales | `수익` 또는 `매출` |
| Cost of goods sold (COGS) | `매출원가` |
| Gross profit | `매출총이익` |
| Operating profit / Income from operations | `영업이익` |
| Net income / Net profit | `당기순이익` |
| Retained earnings | `이익잉여금` |
| Common stock / Share capital | `자본금` 또는 `보통주 자본금` |
| Additional paid-in capital | `주식발행초과금` (또는 `자본잉여금`) |
| Goodwill | `영업권` |
| Intangible assets | `무형자산` |
| Property, plant and equipment | `유형자산` |
| Depreciation | `감가상각비` |
| Amortization | `상각비` (무형자산) |
| Impairment loss | `손상차손` |
| Provision | `충당부채` (K-IFRS 용어. 충당금과 구분) |
| Contingent liability | `우발부채` |
| Deferred tax assets/liabilities | `이연법인세자산/이연법인세부채` |

### D3: 감사 의견 및 감사 용어

| 조건 | 결정 |
|------|------|
| Unqualified opinion | `적정 의견` — 감사인이 재무제표가 적정하다고 판단 |
| Qualified opinion | `한정 의견` — 일부 사항을 제외하고 적정 |
| Adverse opinion | `부적정 의견` — 재무제표가 중요하게 왜곡 표시됨 |
| Disclaimer of opinion | `의견 거절` — 감사인이 의견을 표명할 수 없음 |
| Emphasis of matter | `강조사항` — 감사인이 특별히 강조할 사항 |
| Key audit matters (KAM) | `핵심 감사 사항` — 신감사보고서 도입 사항 |
| Materiality | `중요성` — 재무 정보의 중요도 기준 |
| Audit scope | `감사 범위` |
| Internal control over financial reporting | `재무 보고에 대한 내부 통제` |
| Substantive procedures | `실증적 절차` |

### D4: K-IFRS 특화 용어

| 조건 | 결정 |
|------|------|
| K-IFRS 1109 (금융상품) | `Financial Instruments` → `금융상품`, `expected credit loss` → `기대 신용 손실` |
| K-IFRS 1116 (리스) | `Leases` → `리스`, `right-of-use asset` → `사용권 자산`, `lease liability` → `리스 부채` |
| K-IFRS 1115 (고객과의 계약) | `Revenue from Contracts with Customers` → `고객과의 계약에서 생기는 수익` |
| Fair value | `공정 가치` (시가 아님. 공정 가치가 표준 용어) |
| Present value | `현재 가치` |
| Discount rate | `할인율` |
| Effective interest method | `유효이자율법` |
| Impairment test | `손상 검사` |
| Recoverable amount | `회수가능액` |
| Cash-generating unit | `현금창출단위` |

### D5: 금융 및 투자 용어

| 조건 | 결정 |
|------|------|
| Equity securities / Debt securities | `지분 증권` / `채무 증권` |
| Derivatives | `파생상품` 또는 `파생 금융 상품` |
| Hedge accounting | `헤지 회계` |
| Futures / Forwards / Options / Swaps | `선물` / `선도` / `옵션` / `스왑` |
| IPO (Initial Public Offering) | `기업공개(IPO)` |
| Stock / Share | `주식` |
| Bond | `채권` |
| Dividend | `배당금` |
| Yield / Return | `수익률` |
| Principal | `원금` |
| Interest rate | `이자율` 또는 `금리` |
| Maturity | `만기` |
| Collateral | `담보` |

### D6: DART 전자공시 및 규제 용어

| 조건 | 결정 |
|------|------|
| Securities report | `증권 신고서` |
| Business report | `사업 보고서` (분기/반기/연간) |
| Material fact disclosure | `중요 사실 공시` |
| Insider trading | `내부자 거래` |
| Public disclosure | `공시` |
| Fair disclosure | `공정 공시` |
| Treasury stock / Treasury shares | `자기주식` 또는 `자사주` |
| Stock split | `주식 분할` 또는 `액면 분할` |
| Reverse stock split | `주식 병합` |
| Capital increase / Capital reduction | `증자` / `감자` |
| Free ride | `무상 증자` |

### D7: 세무 용어

| 조건 | 결정 |
|------|------|
| Corporate income tax | `법인세` |
| Withholding tax | `원천 징수` |
| Value-added tax (VAT) | `부가가치세(부가세)` |
| Transfer pricing | `이전 가격` |
| Taxable income | `과세 소득` |
| Tax deduction | `세금 공제` |
| Tax credit | `세액 공제` |
| Carryforward / Carryback | `이월 공제` / `소급 공제` |
| Deferred tax | `이연 법인세` |
| Permanent establishment | `고정 사업장` |

### D8: 재무제표 주석 번역

| 조건 | 결정 |
|------|------|
| Summary of significant accounting policies | `중요 회계 정책의 요약` |
| Basis of preparation | `작성 기준` |
| Use of estimates | `추정의 사용` |
| Segment information | `부문 정보` |
| Related party transactions | `특수 관계자 거래` |
| Contingencies and commitments | `우발 상황 및 약정` |
| Events after reporting period | `보고 기간 후 사건` |
| Earnings per share (EPS) | `주당 순이익(EPS)` |
| Comparative figures / Comparative information | `비교 정보` / `전기 대비` |
| Reclassification | `재분류` |

---

## Standards (표준 및 참조)

### 한국 회계 기준 체계

| 기준 | 명칭 | 적용 대상 |
|------|------|----------|
| **K-IFRS** | 한국채택국제회계기준 | 상장 기업 및 대형 비상장 기업 |
| **일반기업회계기준** | 한국채택국제회계기준(일반기업회계기준) | 비상장 중소기업 (K-IFRS 축약형) |
| **K-GAAP** | 기업회계기준 | K-IFRS 도입 이전 기준 (현재는 점진적 폐지) |
| **NPO 회계기준** | 비영리법인 회계기준 | 비영리 법인 |

### 금융 규제 기관

| 기관 | 영문 명칭 | 역할 |
|------|-----------|------|
| **금융감독원 (FSS)** | Financial Supervisory Service | 금융 감독, DART 전자공시 |
| **금융위원회 (FSC)** | Financial Services Commission | 금융 정책 수립 |
| **한국거래소 (KRX)** | Korea Exchange | 유가증권 시장, 코스닥 운영 |
| **예금보험공사** | Korea Deposit Insurance Corporation | 예금자 보호 |
| **한국회계기준원 (KAI)** | Korea Accounting Institute | K-IFRS 제정 |
| **한국공인회계사회 (KICPA)** | Korean Institute of Certified Public Accountants | 회계사 자격 및 윤리 |

### 감사 기준

| 기준 | 명칭 | 설명 |
|------|------|------|
| **K-SA** | 한국 감사 기준 (Korea Standards on Auditing) | 국제 감사 기준(ISA) 채택 |
| **K-SQC** | 한국 품질 관리 기준 | 감사 품질 관리 |
| **K-SRE** | 한국 검토 기준 | 검토 업무 기준 |
| **K-SAE** | 한국 확신 기준 | 확신 업무 기준 |
| **K-SRS** | 한국 관련 서비스 기준 | 관련 서비스 업무 기준 |

### 주요 주의사항

1. **K-IFRS 식별자** — K-IFRS 항목 번호는 국제 IFRS 번호와 다를 수 있음. 반드시 한국채택국제회계기준(K-IFRS)의 공식 번호 확인
2. **계정과목 한자 병기** — 중요 계정과목은 첫 출현시 한자 병기 `(예: 매출채권(賣出債權))`
3. **금액 단위 명시** — 재무제표 상단에 `(단위: 천 원)` 또는 `(단위: 백만 원)` 명시. 생략 시 대규모 오독 발생 가능
4. **부호의 방향** — 대차대조표 등에서 괄호 표시의 의미 확인. 한국은 `()`가 차변/대변을 나타낼 수 있음
5. **전기(前期) 대비** — 재무제표는 전기(previous period) 비교 표시가 기본. `전기`는 `전년도`가 아닌 직전 회계 기간 의미
6. **회계 정책 변경** — `change in accounting policy` → `회계 정책의 변경`, `change in accounting estimate` → `회계 추정의 변경` 구분 엄수
7. **중요성 판단** — `material`은 재무제표에서 `중요한`으로 번역. `중대한`은 부정적 의미를 내포하므로 상황에 따라 구분

## Error Pattern Library (오류 패턴 라이브러리)

### Critical Errors (제로 허용 오류)

| Error | Why It Is Critical |
|-------|-------------------|
| **숫자 값 변경** | 한 자릿수의 변경도 재무 상태를 왜곡하며 외부감사법 위반으로 이어질 수 있음. 재무제표의 모든 숫자는 법적으로 증빙 가능한 수치. |
| **소수점/천단위 구분자 오류** | 1,500(천오백)을 1.50(일점오영)으로 변경하면 값이 1/1000이 됨. 재무 번역에서 가장 빈번한 치명적 오류. |
| **통화 코드/기호 변경** | USD를 KRW로 오기하거나 원(\)을 달러($)로 잘못 표기하면 모든 금액의 실질 가치가 왜곡됨. |
| **금액 단위(원/천원/백만원) 변경** | 재무제표 상단에 명시된 금액 단위를 변경하면 모든 수치가 잘못 해석됨. (단위: 천 원)을 (단위: 원)으로 바꾸면 1,000배 차이. |
| **K-IFRS 용어 비표준 사용** | K-IFRS에서 정한 공식 계정과목명 대신 비표준 용어 사용 시 감사인이나 규제 기관이 문서를 인정하지 않을 수 있음. |
| **주석 참조 번호 불일치** | 재무제표 본문과 주석 간의 참조 번호가 일치하지 않으면 감사 추적 불가. 모든 주석 참조 번호 확인 필수. |

### Common Errors (빈번한 오류)

| Error | Guidance |
|-------|----------|
| **숫자 형식 변환 누락** | 유럽식 숫자 형식(점을 천단위 구분, 쉼표를 소수점)이 혼입되지 않도록 모든 숫자 확인. 한 표 내에서도 형식이 혼용될 수 있음. |
| **단위 표시 누락** | 재무제표 상단의 "(단위: 천 원)" 또는 "(단위: 백만 원)"이 누락되면 모든 수치가 잘못 해석됨. 표가 여러 페이지에 걸친 경우 모든 페이지에 단위 표시 필요. |
| **당기/전기 라벨 혼동** | Current Period(당기)와 Prior Period(전기)가 바뀌면 비교 재무제표 전체가 무의미해짐. |
| **날짜 형식 불일치** | 동일 문서 내에서 "2025-12-31", "2025.12.31.", "2025년 12월 31일"이 혼용되면 비전문적으로 보임. 하나의 형식으로 통일. |
| **재무제표 명칭 구형 사용** | K-IFRS 도입 전 용어(대차대조표 → 재무상태표, 손익계산서 유지)를 혼용하면 K-IFRS 준수 문서로 인정받지 못할 수 있음. |
| **감사 의견 등급 오역** | "unqualified opinion"("적정 의견")과 "qualified opinion"("한정 의견")을 혼동하면 감사 결과에 대한 법적 이해가 왜곡됨. |

### Subtle Errors (놓치기 쉬운 오류)

| Error | Guidance |
|-------|----------|
| **음수 표기 방식** | 한국 재무제표는 괄호를 음수 표기에 사용: (100,000). 원본이 마이너스(-) 부호를 사용하는 경우 한국 관행에 맞출지 스타일 가이드 확인. |
| **반올림/단위 표기** | "천원 미만은 반올림" 또는 "백만 원 단위로 표시" 등의 단위 설명을 주석에서 반드시 확인하고 보존. |
| **회계 정책 변경과 추정 변경의 구분** | "change in accounting policy" → "회계 정책의 변경", "change in estimate" → "회계 추정의 변경". 이 둘은 K-IFRS 1008에서 다르게 처리됨. |
| **연결 vs 별도 재무제표 구분** | "Consolidated"는 "연결", "Separate"는 "별도". 혼동 시 재무제표의 보고 범위가 완전히 달라짐. |
| **대차대조표 방정식 용어** | "Assets = Liabilities + Equity" → "자산 = 부채 + 자본". K-IFRS 용어로 일관되게 번역. "자본"은 "Equity"의 표준 용어. |
| **중요성 판단 용어** | "material"은 회계에서 "중요한". "유의적인"은 K-IFRS 일부 기준에서 사용되나 "중요한"이 일반적. "중대한"은 감사보고서에서 사용. |

## Domain-Specific Reference (분야별 참조)

### Key K-IFRS Standards Number Reference (주요 K-IFRS 번호)

| Standard | Title | Korean Title |
|----------|-------|-------------|
| K-IFRS 1001 | Presentation of Financial Statements | 재무제표 표시 |
| K-IFRS 1002 | Inventories | 재고자산 |
| K-IFRS 1007 | Statement of Cash Flows | 현금흐름표 |
| K-IFRS 1008 | Accounting Policies, Changes in Estimates and Errors | 회계정책, 회계추정의 변경 및 오류 |
| K-IFRS 1010 | Events After the Reporting Period | 보고기간 후 사건 |
| K-IFRS 1012 | Income Taxes | 법인세 |
| K-IFRS 1016 | Property, Plant and Equipment | 유형자산 |
| K-IFRS 1019 | Employee Benefits | 종업원급여 |
| K-IFRS 1021 | Effects of Changes in Foreign Exchange Rates | 환율변동효과 |
| K-IFRS 1024 | Related Party Disclosures | 특수관계자 공시 |
| K-IFRS 1027 | Separate Financial Statements | 별도재무제표 |
| K-IFRS 1036 | Impairment of Assets | 자산손상 |
| K-IFRS 1037 | Provisions, Contingent Liabilities and Contingent Assets | 충당부채, 우발부채 및 우발자산 |
| K-IFRS 1109 | Financial Instruments | 금융상품 |
| K-IFRS 1115 | Revenue from Contracts with Customers | 고객과의 계약에서 생기는 수익 |
| K-IFRS 1116 | Leases | 리스 |

### Common Financial Statement Analysis Ratios (주요 재무 비율)

| Ratio Name | Korean Name | Formula (Korean) |
|-----------|-------------|------------------|
| Current Ratio | 유동비율 | 유동자산 / 유동부채 |
| Quick Ratio | 당좌비율 | (유동자산 - 재고자산) / 유동부채 |
| Debt-to-Equity Ratio | 부채비율 | 부채총계 / 자본총계 × 100 |
| Gross Profit Margin | 매출총이익률 | 매출총이익 / 매출액 × 100 |
| Operating Profit Margin | 영업이익률 | 영업이익 / 매출액 × 100 |
| Net Profit Margin | 순이익률 | 당기순이익 / 매출액 × 100 |
| ROE (Return on Equity) | 자기자본이익률 | 당기순이익 / 자본총계 × 100 |
| ROA (Return on Assets) | 총자산순이익률 | 당기순이익 / 자산총계 × 100 |
| EPS (Earnings Per Share) | 주당순이익 | 당기순이익 / 가중평균유통주식수 |
| BPS (Book Value Per Share) | 주당순자산가액 | 자본총계 / 유통주식수 |
| PER (Price to Earnings Ratio) | 주가수익비율 | 주가 / 주당순이익 |
| PBR (Price to Book Ratio) | 주가순자산비율 | 주가 / 주당순자산가액 |
| Dividend Yield | 배당수익률 | 주당배당금 / 주가 × 100 |
| Interest Coverage Ratio | 이자보상비율 | 영업이익 / 이자비용 |

### Financial Instruments Korean Terminology (금융상품 용어)

| English | Korean | Notes |
|---------|--------|-------|
| Financial Asset | 금융자산 | |
| Financial Liability | 금융부채 | |
| Equity Instrument | 지분상품 | |
| Derivative | 파생상품 | K-IFRS 1109 |
| Amortized Cost | 상각후원가 | K-IFRS 1109 measurement category |
| Fair Value Through Profit or Loss (FVTPL) | 당기손익-공정가치 측정 항목 | FVTPL |
| Fair Value Through OCI (FVOCI) | 기타포괄손익-공정가치 측정 항목 | FVOCI |
| Expected Credit Loss (ECL) | 기대신용손실 | K-IFRS 1109 impairment model |
| Effective Interest Rate | 유효이자율 | |
| Derecognition | 제거 | Financial asset derecognition |
| Impairment | 손상 | |
| Hedge Accounting | 헤지회계 | K-IFRS 1109 |
| Cash Flow Hedge | 현금흐름위험회피 | |
| Fair Value Hedge | 공정가치위험회피 | |

### Tax Filing and Reporting Terms (세무 신고 용어)

| English | Korean | Period / Rate |
|---------|--------|--------------|
| Corporate Income Tax Return | 법인세 신고서 | Annually within 3 months of fiscal year end |
| Value-Added Tax Return | 부가가치세 신고서 | Quarterly (every 3 months) |
| Withholding Tax Report | 원천징수 신고서 | Monthly / Semi-annually |
| Comprehensive Income Tax Return | 종합소득세 신고서 | Annually (May for individuals) |
| Transfer Pricing Report | 이전가격 보고서 | Annually with CIT return |
| Tax Invoice | 세금계산서 | Issued for VAT purposes |
| Corporate Tax Rate (2025) | 법인세율 | 9% (first 200M KRW) to 24% |
| VAT Rate | 부가가치세율 | 10% |

### Financial Institution Types (금융 기관 유형)

| Korean | English | Characteristics |
|--------|---------|-----------------|
| 한국은행 | Bank of Korea (BOK) | Central bank of Korea |
| 은행 | Bank | Commercial banks, specialized banks |
| 증권사 | Securities Company | Brokerage and investment banking |
| 보험사 | Insurance Company | Life and non-life insurance |
| 자산운용사 | Asset Management Company | Fund management |
| 상호저축은행 | Mutual Savings Bank | Regional savings banks |
| 신용협동조합 | Credit Union | Member-owned financial cooperative |
| 새마을금고 | Community Credit Cooperative (MG) | Local community financial institution |
| 여신전문금융회사 | Specialized Credit Finance Company | Credit cards, leasing, installment |
| 금융투자회사 | Financial Investment Company | Investment services |
| 종합금융회사 | Comprehensive Finance Company | Merged into other institutions |
| 농협/수협 | Nonghyup / Suhyup | Agricultural / Fisheries cooperatives with banking |

### Korean Financial Disclosure Filing Types (전자공시 서류 유형)

| Filing Type | Korean | English | Deadline |
|------------|--------|---------|----------|
| Annual Business Report | 사업보고서 | Annual Report | Within 90 days of FY end |
| Semi-Annual Report | 반기보고서 | Semi-Annual Report | Within 45 days of half-year end |
| Quarterly Report | 분기보고서 | Quarterly Report | Within 45 days of quarter end |
| Material Facts Report | 주요사항보고서 | Material Event Disclosure | Promptly upon occurrence |
| Prospectus | 투자설명서 | Prospectus | Before securities offering |
| Securities Registration | 증권신고서 | Securities Registration Statement | Before public offering |
| Audit Report | 감사보고서 | Audit Report | With annual report |
| Internal Accounting Report | 내부회계관리제도 보고서 | Internal Control Report | Annually with audit report |
| Corporate Governance Report | 지배구조 보고서 | Corporate Governance Report | Annually |
