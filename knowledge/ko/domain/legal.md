---
id: ko/domain/legal
type: domain
target_lang: ko
name: 법률 문서 번역 규정
description: 법률 문서, 법원 서류, 계약서, 특허 문서, 공증 번역 규칙
---

## Reader Model (독자 모델)

**누가 이 문서를 읽고 무엇을 기대하는가?**

법률 문서의 독자는 변호사, 판사, 법무 담당자, 계약 당사자, 특허 변리사로서 문서를 통해 권리, 의무 및 법적 결과를 판단한다. 다음을 기대한다:

- **모호함은 곧 위험** — 모든 단어는 소송에서 정밀하게 검토될 수 있다. 번역자는 법적 의도를 정확히 보존하고 해석의 여지를 남기지 않아야 한다.
- **격식체 유지** — 한국어 법률 문서는 정형화된 문체와 어휘 규칙을 따른다. 구어체나 비격식 표현은 계약의 집행 가능성을 훼손한다.
- **법적 구조 보존** — 전문(recitals), 조항(operative clauses), 정의(definitions), 서명란(signatures), 부속서(schedules)는 각각 고유한 기능을 가지며 그 구조를 유지해야 한다.
- **정의된 용어의 일관성** — 정의된 용어는 모든 출현에서 동일하게 표기되어야 한다. 변형은 의도치 않게 새로운 의미를 창출할 수 있다.
- **법체계 인식** — 한 법체계에 존재하는 개념이 다른 법체계에 직접적 대응어가 없을 수 있다. 번역자는 오해를 불러일으키지 않으면서 연결해야 한다.
- **공증 번역 인증** — 한국 법원 제출용 번역은 대한민국 대사관/영사 확인 또는 공증 번역사 인증이 필요할 수 있다.

**무엇이 신뢰를 무너뜨리는가?**
- 위험/책임 주체를 변경하는 의무 조항 오번역
- 대상 법체계에 근거가 없는 조작된 법적 개념
- 모호함을 초래하는 불일치 정의 용어
- 조항을 무효화할 수 있는 날짜, 참조 번호 또는 서명란 오류
- 한국 민법/상법 개념을 영미법 개념으로 부적절하게 대체

---

## Decision Framework (의사결정 체계)

### D1: 의무 조항 번역

| 조건 | 결정 |
|------|------|
| 원문의 binding obligation (shall) | `~해야 한다` 또는 `~한다` (의무형). 예: `The Lessee shall pay` → `임차인은 임차료를 지급해야 한다` |
| 원문의 prohibition (shall not) | `~해서는 아니 된다` 또는 `~하지 못한다`. 예: `The Tenant shall not sublease` → `임차인은 전대해서는 아니 된다` |
| 원문의 permission/discretion (may) | `~할 수 있다`. 예: `The Company may terminate` → `회사는 계약을 해지할 수 있다` |
| 원문의 declaration/fact | 현재형 사실 문장. `The parties agree that...` → `당사자는 ...에 동의한다` |
| Conditional obligation | `~하는 경우, ~해야 한다` / `~에 따라` |
| 강한 금지 (must not) | `~해서는 절대 아니 된다` (가장 강한 금지 표현) |
| 권고 (should) | `~하는 것이 바람직하다` 또는 `~하여야 한다` (약한 의무) |

### D2: 법체계 간 개념 대응

| 조건 | 결정 |
|------|------|
| 영미법 개념이 한국법에 직접적 대응어가 있는 경우 | 한국 민법/상법 용어 사용. 예: `consideration` → `약인(約因)` (설명 필요) |
| 영미법 개념이 한국법에 없는 경우 | 설명적 등가어 사용, 첫 출현 시 괄호로 영문 원어와 설명 병기 |
| 법인 유형 (Ltd., Inc., LLC, GmbH) | 한국어 법인 유형으로 부적절하게 대체하지 않음. 원래 약어 유지 후 첫 출현 시 `(유한회사)` 등 설명 추가 |
| 법원 이름이 특정 국가에 고유한 경우 | 원래 이름 유지, 첫 출현 시 한국어 설명 병기 |
| 한국법 고유 개념 (전세권, 저당권, 근저당 등) | 영문 번역 시 설명적 번역 필요, 한국어 원문에서는 그대로 사용 |
| 조약/국제협약 명칭 | 공식 한국어 번역명이 있는 경우 해당 명칭 사용 |

### D3: 문서 구조 유지

| 조건 | 결정 |
|------|------|
| 전문 (WHEREAS / Recitals) | `WHEREAS` → `...에 비추어` 또는 `...에 의하여` (법률 문서 격식 유지) |
| 조항/항/호/목 | 체계적 번호 부여 유지. `Clause 1.2(a)` → `제1조 제2항 제a호` |
| 정의 조항 | 정의된 용어는 전체 문서에서 완전히 동일하게 표기, 따옴표 또는 굵은 글씨 유지 |
| 서명란 | 레이아웃 정확히 유지. 직함 번역. 성명은 원어 유지 |
| 부속서/별지 | `Schedule` → `부속서` 또는 `별지`. `Appendix` → `부록`. 일관성 유지 |

### D4: 날짜 및 숫자 형식 (법률 문서)

| 조건 | 결정 |
|------|------|
| 날짜 표현 | `2025년 4월 30일` 형식 (년 월 일 순). 숫자만으로 된 모호한 형식 금지 |
| 계약 기간 | `2025. 4. 30.부터 2026. 4. 29.까지` |
| 통화 금액 | 숫자와 한글 병기. `금 오십만 원정(\500,000)` — 한국 법률 문서 관행 |
| 지급 기한 | `...까지` 또는 `...이내에` |
| 백분율 | 숫자와 % 기호. `연 5%` |

### D5: 법률 용어 및 전문 용어 선택

| 조건 | 결정 |
|------|------|
| 양도/양수 | `assignor/assignee` → `양도인/양수인` |
| 임대인/임차인 | `lessor/lessee` → `임대인/임차인` 또는 `임대차` 맥락에 따라 구분 |
| 채권자/채무자 | `creditor/debtor` → `채권자/채무자` |
| 불가항력 | `force majeure` → `불가항력` (영문 병기 선택 사항) |
| 손해배상 | `indemnification` → `손해배상` 또는 `면책` (맥락에 따라 구분) |
| 중재 | `arbitration` → `중재`, `mediation` → `조정`, `conciliation` → `알선` |
| 지식재산권 | `intellectual property` → `지식재산권` (지적재산권보다 지식재산권 권장) |
| 기밀유지 | `confidentiality` → `기밀유지` 또는 `비밀유지` |

### D6: 법률 문서 경어법 및 문체

| 조건 | 결정 |
|------|------|
| 계약서 본문 | `~한다` 체(평서체) 사용 — 한국 계약서 표준 문체 |
| 법원 제출 문서 | `~합니다` 체(합쇼체) 사용 — 법원 제출 문서 격식 |
| 전문(前文) | `~에 비추어`, `~에 의하여` 등 정형화된 문구 사용 |
| 고유 명사 (당사자명) | 왜곡 없이 원문 유지, 영문 표기 그대로 사용 |
| 법률 인용 | 법률명은 정확한 한국어 법률명 사용. `Act on...` → `...법` |

### D7: 공증 및 인증 번역

| 조건 | 결정 |
|------|------|
| 공증 번역 대상 문서 | 원문 그대로의 충실한 번역. 첨삭이나 의역 금지 |
| 번역인 확인 문구 | `이 번역은 원문과 상위 없음을 확인합니다.` 또는 `I hereby certify that this translation is true and accurate.` |
| 공증인 서명란 | 번역사 성명, 서명, 날짜, 연락처 포함 |
| 제출 용도 명시 | 법원 제출용, 대사관 제출용 등 용도에 따라 추가 요구사항 확인 |
| 인증 번역사 표기 | 번역사 자격증 번호, 인증 기관명 기재 |

### D8: 특허 문서 번역

| 조건 | 결정 |
|------|------|
| 특허 청구항 | `claim 1` → `청구항 1`, `The method of claim 1` → `제1항에 따른 방법` |
| 명세서 | `specification` → `명세서`, `drawings` → `도면` |
| 배경기술 | `background art` → `배경 기술` |
| 발명의 상세한 설명 | `detailed description` → `발명의 상세한 설명` |
| 특허 협력 조약(PCT) 관련 용어 | PCT 용어의 한국어 표준 번역 사용 (특허청 용어집 참조) |
| 선행 기술 | `prior art` → `선행 기술` |

---

## Standards (표준 및 참조)

### 주요 법률 참조

| 법률/규정 | 영문 명칭 | 적용 분야 |
|-----------|-----------|----------|
| **민법** | Civil Act | 계약, 채권, 물권 일반 |
| **상법** | Commercial Act | 회사, 보험, 해상, 상행위 |
| **민사소송법** | Civil Procedure Act | 소송 절차 |
| **대한민국 헌법** | Constitution of the Republic of Korea | 헌법 관련 |
| **특허법** | Patent Act | 특허/지식재산권 |
| **상표법** | Trademark Act | 상표 관련 |
| **근로기준법** | Labor Standards Act | 노동/고용 관련 |
| **국제사법** | Private International Law | 국제 계약 준거법 관련 |
| **외국법자문사법** | Foreign Legal Consultant Act | 외국법 번역 관련 |

### 법률 용어 표준화 기관

| 기관 | 역할 |
|------|------|
| **대한민국 법원 (행정처)** | 법원 제출 문서 양식 및 용어 표준 |
| **법제처** | 법령 용어 표준화 및 심의 |
| **대한변호사협회** | 법률 용어 및 번역 가이드라인 |
| **한국특허정보원 (KIPI)** | 특허 분야 용어 표준 |
| **특허청 (KIPO)** | 지식재산권 관련 용어 표준 |
| **한국법제연구원 (KLRI)** | 법률 번역 및 비교법 연구 |
| **국립국어원** | 법률 분야 한국어 용어 정비 |

### 법률 문서 번역 원칙

1. **원문 충실성** — 법률 번역의 제1원칙. 모든 요소를 빠짐없이 번역하고 의역 금지
2. **일관된 용어 사용** — 동일한 용어는 전체 문서에서 동일하게 번역
3. **정의된 용어 보호** — 정의 조항에 명시된 용어는 정의된 대로만 사용
4. **조약/협약의 공식 번역명 사용** — 대한민국이 비준한 조약은 관보 게재 공식 번역명 사용
5. **법률 인용 시 정확성** — 법률명, 조문 번호, 시행령 등 모든 참조의 정확성 검증
6. **이중 번역 금지** — 이미 한국어 법률 용어가 있는 경우 외국어 표현을 그대로 사용하지 않음
7. **한자 병행 표기** — 중요 법률 용어는 첫 출현 시 한자 병행 (예: `채권자(債權者)`)
8. **문서 유형별 관행 준수** — 계약서, 소장, 판결문, 특허 명세서 등 각 문서 유형의 관행적 형식 준수

## Error Pattern Library (오류 패턴 라이브러리)

### Critical Errors (제로 허용 오류)

| Error | Why It Is Critical |
|-------|-------------------|
| **법인 유형 오번역** | Ltd., Inc., GmbH 등 외국 법인 유형을 한국어 법인 유형(유한회사, 주식회사)으로 대체하는 것은 법인격 자체를 변경하는 것. 원래 약어 유지 후 괄호 설명. |
| **계약 의무 조항 오역** | "shall"을 "할 수 있다"로 번역하면 의무가 권한으로 바뀜. 의무/권리/금지의 구분은 계약 해석의 핵심. |
| **정의 용어 불일치** | 정의된 용어가 두 가지 다른 형태로 나타나면 두 개의 잠재적 의미가 생김. 모든 출현에서 완전히 동일하게 표기. |
| **조문 번호 변경** | 교차 참조는 정확한 조문 번호에 의존. 번호 변경은 전체 참조 체계를 무너뜨림. |
| **날짜 형식 모호성** | "04/05/2025"는 관할권에 따라 5월 4일 또는 4월 5일로 해석. 한국 법률 문서에서는 "2025년 4월 30일" 형식 사용. |
| **한국 고유 법률 개념 오역** | 전세권, 저당권, 근저당 등 한국 민법 고유 개념은 영미법 개념으로 부적절하게 대체 금지. 설명적 번역 필요. |

### Common Errors (빈번한 오류)

| Error | Guidance |
|-------|----------|
| **문체 일관성 부족** | 계약서는 `~한다` 체(평서체) 일관 유지. 법원 제출 문서는 `~합니다` 체(합쇼체) 일관 유지. 한 문서 내 혼용 금지. |
| **~한다 체와 ~하다 체 혼동** | 한국 계약서는 `~한다` 체가 표준. `~하다` 체는 부자연스러움. 예: "임차인은 지급한다" (O), "임차인은 지급하다" (X). |
| **영미법 개념의 무분별한 한국어 대체** | Consideration을 "대가"로 번역하는 것은 정확하지만 영미법적 의미를 완전히 전달하지 못함. 필요시 설명 추가. |
| **서명란 형식 변경** | 서명란의 레이아웃, 날짜 줄, 증인 줄의 정확한 배치 유지. 형식적 요소도 법적 효력의 일부. |
| **부속서/별지 참조 불일치** | 본문에서 "부속서 A"로 참조하면서 실제 부속서 제목이 "Schedule A"인 경우 불일치 발생. 본문과 부속서의 참조 일치 확인. |

### Subtle Errors (놓치기 쉬운 오류)

| Error | Guidance |
|-------|----------|
| **법체계 간 허위 등가어** | 외형상 동일해 보이는 용어도 다른 법체계에서는 다른 법적 결과를 가짐. 대상 법체계에서의 개념을 반드시 연구. |
| **첫 출현 시 설명 주석 누락** | 한국법에 없는 개념(trust, consideration, estoppel 등)은 첫 출현 시 괄호 설명 필수. 이후 출현에서는 용어만 사용. |
| **정의 용어의 단수/복수 변경** | 영어에서 정의된 용어가 단수로 정의되었다면 한국어 번역에서도 단수 유지. 복수 변경 시 정의 범위가 의도치 않게 확대/축소됨. |
| **한자 병기 생략** | 중요 법률 용어는 첫 출현 시 한자 병기(예: 채권자(債權者), 채무자(債務者))가 관행. 생략 시 전문성 저하. |
| **법률 약칭 사용 오류** | "상법"은 "상법"이 공식 약칭이지만, "민법"은 "민법"이 정식 명칭. 약칭 사용 전 공식 약칭을 법제처 사이트에서 확인. |
| **준거법 조항의 국제사법 인식 부족** | 한국 국제사법에 따른 준거법 결정 규칙을 이해하고 번역에 반영. "Governing Law"는 "준거법"이 표준 번역. |

## Domain-Specific Reference (분야별 참조)

### Korean Court Structure (한국 법원 체계)

| Court Level | Korean Name | English Name |
|-------------|-------------|--------------|
| Supreme Court | 대법원 | Supreme Court of Korea |
| High Court | 고등법원 | High Court |
| District Court | 지방법원 | District Court |
| Branch Court | 지원 | Branch Court of District Court |
| Family Court | 가정법원 | Family Court |
| Administrative Court | 행정법원 | Administrative Court |
| Patent Court | 특허법원 | Patent Court |
| Constitutional Court | 헌법재판소 | Constitutional Court of Korea |
| Municipal Court | 시법원 | Municipal Court (abolished, now under District Court) |

### Common Korean Contract Types (주요 계약 유형)

| Korean Name | English Equivalent | Characteristics |
|-------------|-------------------|----------------|
| 매매계약 | Sales Contract / Purchase Agreement | 가장 기본적인 계약 유형 |
| 임대차계약 | Lease Agreement | 부동산 임대차 (전세/월세 포함) |
| 도급계약 | Contract for Work | 건설 공사 등 작업 완료 계약 |
| 위임계약 | Mandate / Service Agreement | 업무 위임 계약 |
| 조합계약 | Partnership Agreement | 공동 사업 조합 |
| 보증계약 | Guarantee Agreement | 채무 보증 계약 |
| 화해계약 | Settlement Agreement | 분쟁 해결을 위한 계약 |
| 양도계약 | Assignment Agreement | 권리/채권 양도 계약 |
| 라이선스계약 | License Agreement | 지식재산권 사용 허락 계약 |
| NDA (비밀유지계약) | Non-Disclosure Agreement | 기밀 유지 계약 |

### Korean Legal Document Types (한국 법률 문서 유형)

| Korean Name | English Translation | Purpose |
|-------------|-------------------|---------|
| 소장 | Complaint / Statement of Claim | 법원에 소송 제기 문서 |
| 답변서 | Answer / Response | 피고의 답변 |
| 준비서면 | Preliminary Brief | 변론 준비 서면 |
| 항소장 | Notice of Appeal | 항소 제기 문서 |
| 판결문 | Judgment / Court Decision | 법원의 판결 |
| 화해권고결정 | Recommendation for Settlement | 법원의 화해 권고 |
| 지급명령 | Payment Order | 소액 채무 지급 명령 |
| 가압류 신청서 | Application for Provisional Seizure | 재산 가압류 신청 |
| 가처분 신청서 | Application for Preliminary Injunction | 잠정 처분 신청 |
| 등기 신청서 | Application for Registration | 부동산 등기 신청 |
| 상속 포기 신고서 | Report of Renunciation of Inheritance | 상속 포기 신고 |
| 인감증명서 발급 신청서 | Application for Certificate of Seal Impression | 도장 인증 신청 |

### Common Korean Legal Terminology (주요 법률 용어)

| English | Korean | Context |
|---------|--------|---------|
| Plaintiff / Defendant | 원고 / 피고 | Civil litigation |
| Prosecutor / Accused | 검사 / 피고인 | Criminal litigation |
| Claimant / Respondent | 청구인 / 피청구인 | Administrative litigation |
| Appellant / Appellee | 항소인 / 피항소인 | Appeal |
| Creditor / Debtor | 채권자 / 채무자 | Obligations |
| Mortgagor / Mortgagee | 저당권설정자 / 저당권자 | Real estate security |
| Lessor / Lessee | 임대인 / 임차인 | Lease |
| Transferor / Transferee | 양도인 / 양수인 | Assignment |
| Guarantor / Beneficiary | 보증인 / 피보증인 | Guarantee |
| Trustee / Trustor | 수탁자 / 위탁자 | Trust (if applicable) |
| Notary Public | 공증인 | Notarization |
| Legal Representative | 법정대리인 | Minor/incapacitated person |
| Attorney-in-fact | 임의대리인 | Power of attorney |
| Statutory Agent | 법률상 대리인 | Corporate representation |

### Key Korean Acts Frequently Referenced (번역 시 자주 인용되는 법률)

| Full Korean Name | Abbreviation | English Name |
|-----------------|-------------|--------------|
| 민법 | 민법 | Civil Act |
| 상법 | 상법 | Commercial Act |
| 민사소송법 | 민소법 | Civil Procedure Act |
| 형법 | 형법 | Criminal Act |
| 형사소송법 | 형소법 | Criminal Procedure Act |
| 근로기준법 | 근기법 | Labor Standards Act |
| 근로자퇴직급여 보장법 | 퇴직급여법 | Employee Retirement Benefit Security Act |
| 산업안전보건법 | 산안법 | Occupational Safety and Health Act |
| 개인정보 보호법 | 개인정보법 | Personal Information Protection Act |
| 부동산등기법 | 등기법 | Real Estate Registration Act |
| 가족관계의 등록 등에 관한 법률 | 가족관계등록법 | Act on Registration of Family Relations |
| 외국인토지법 | — | Foreigner's Land Acquisition Act |
| 국제사법 | 국제사법 | Private International Law |
| 자본시장과 금융투자업에 관한 법률 | 자본시장법 | Financial Investment Services and Capital Markets Act |

### 인감 및 공증 관련 용어 (Seal and Notarization Terms)

| Korean | English | Notes |
|--------|---------|-------|
| 인감 (도장) | Registered Seal / Personal Seal | 한국 고유의 도장 인증 제도 |
| 인감증명서 | Certificate of Personal Seal Impression | 구청/동사무소 발급 |
| 사용인감 | Company Use Seal | 회사 업무용 도장 |
| 법인인감 | Corporate Registered Seal | 법인 등기 시 등록된 도장 |
| 직인 | Official Company Seal | 회사 공식 도장 |
| 날인 | Affix Seal / Seal Impression | 도장을 찍는 행위 |
| 서명 | Signature | 자필 서명 |
| 간인 | Countersign / Initial Seal | 문서 간 도장 일치 표시 |
| 공증 | Notarization | 공증인에 의한 인증 |
| 공증인 | Notary Public | 공증 업무 수행자 |
| 아포스티유 | Apostille | 국제 공문서 인증 (헤이그 협약) |
| 영사 확인 | Consular Legalization | 대사관/영사관 인증 |
| 법무사 | Legal Scrivener / Judicial Scrivener | 법원/검찰 서류 작성 대행 |
| 변호사 | Attorney / Lawyer | 법률 전문가 |
| 법무법인 | Law Firm | 법률 사무소 |
