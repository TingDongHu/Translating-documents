---
id: ko/domain/administrative
type: domain
target_lang: ko
name: 행정 문서 번역 규정
description: 공문서, 행정 절차, 정부 양식, 공공 정책, 인증/허가 문서 번역 규칙
---

## Reader Model (독자 모델)

**누가 이 문서를 읽고 무엇을 기대하는가?**

행정 문서의 독자는 공무원, 행정 담당자, 민원인, 법률가, 규제 준수 담당자로서 문서를 통해 행정 절차를 이해하고 법적 효력을 판단한다. 다음을 기대한다:

- **정해진 서식과 양식 준수** — 한국 정부의 공문서는 행정안전부의 공문서 작성 규칙(행정안전부 예규)에 따라 정해진 형식이 있다. 번역 시 원본의 구조와 양식을 반드시 유지해야 한다.
- **법적 근거의 정확한 명시** — 모든 행정 처분은 법적 근거(법률, 시행령, 시행규칙, 조례)를 가지고 있다. 법률 조문 인용은 정확해야 하며, 약칭과 전체 이름을 구분해야 한다.
- **공식적인 격식 유지** — 공문서는 `합쇼체(습니다 체)`를 사용하며, 정형화된 문구(이에, 귀하, 외, 등)가 있다. 이러한 관행적 표현은 번역 시에도 반영되어야 한다.
- **명확한 수신자/발신자 체계** — 한국 공문서는 수신자, 발신자, 결재선, 시행일, 접수 번호 등 고유한 체계가 있다. 이 구조가 그대로 보존되어야 의미 전달이 가능하다.
- **고유한 행정 용어의 이해** — 한국 행정 체계 고유의 용어(주민등록번호, 행정동-법정동 구분, 토지대장, 등기부 등본 등)는 설명적 번역이 필요하다.

**무엇이 신뢰를 무너뜨리는가?**
- 공문서 형식(수신, 발신, 결재란)의 구조적 오류
- 법률 조문 인용의 부정확성
- 행정 처분의 법적 근거 누락
- 한국 행정 체계 고유 개념에 대한 설명 부재
- 공식 기관명의 비표준 번역
- 행정 절차 용어의 잘못된 대응어 사용

---

## Decision Framework (의사결정 체계)

### D1: 공문서 구조 번역

| 조건 | 결정 |
|------|------|
| 수신자 (받는 사람) | `To:` 또는 `[수신]` → `수신: [기관명/담당자]` |
| 발신자 (보내는 사람) | `From:` 또는 `[발신]` → `발신: [부서명/직책/성명]` |
| 결재란 | `Approval / Authorization` → `결재` (결제 아님! 결재 = approval, 결제 = payment 구분 필수) |
| 문서 번호 | `Document No.` → `문서 번호` 또는 관행적 약어 유지 |
| 시행일/발송일 | `Date of issue` → `시행일` |
| 접수 번호 | `Reception No.` → `접수 번호` |
| 참조 | `Reference / Re:` → `참조` |
| 첨부 | `Attachment / Enclosure` → `첨부` 또는 `붙임` |
| 공개 구분 | `공개(公開)` / `비공개(非公開)` — 문서의 공개 여부 표시 |
| 보존 연한 | `Retention period` → `보존 연한: 5년` |
| 시행/발신 구분 | `기안 → 검토 → 결재 → 시행` — 행정 절차 단계 구분 유지 |

### D2: 기관 및 부서명 번역

| 조건 | 결정 |
|------|------|
| 중앙 행정 기관 | 공식 영문 명칭이 있는 경우 해당 명칭 사용. `Ministry of [명칭]` 패턴 |
| 지방 자치 단체 | `[도/시/군/구]` — `Province / City / County / District` 체계 사용 |
| 부서명 | `Division → 과`, `Bureau → 국`, `Team → 팀`, `Office → 실` 또는 `처` |
| 위원회 | `Commission` 또는 `Committee` → `위원회` |
| 청 | `Service` / `Administration` → `청` (예: `기상청: Korea Meteorological Administration`) |
| 공사/공단 | `Corporation` / `Authority` → `공사` / `공단` |
| 직위명 | `Minister` → `장관`, `Vice Minister` → `차관`, `Director General` → `국장`, `Director` → `과장` |
| 위원/위원장 | `Commissioner / Chairperson` → `위원 / 위원장` |

### D3: 한국 행정 고유 개념 번역

| 개념 | 설명적 번역 | 비고 |
|------|-------------|------|
| 주민등록번호 | `Resident Registration Number (Korean SSN equivalent)` | 한국 고유 식별 번호. 번역 시 `(RRN)` 약어 사용 가능 |
| 주민등록등본 | `Certificate of Resident Registration` | 주소, 가족 관계 증명 |
| 가족관계증명서 | `Certificate of Family Relations` | 2008년 호적법 폐지 후 도입 |
| 등기부 등본 | `Certified Copy of Register` | 부동산 권리 관계 증명 |
| 토지대장 | `Land Register` / `Cadastral Register` | 토지의 행정적 기록 |
| 인감증명서 | `Certificate of Personal Seal Impression` | 한국 고유의 도장 인증 제도 |
| 확정일자 | `Confirmed Date Stamp` | 임대차 계약 확정일자 |
| 주택임대차신고서 | `Lease Registration Report` | 임대차 계약 신고 |
| 전입신고 | `Residence Registration Report` | 거주지 변경 신고 |

### D4: 법률 인용 및 준거

| 조건 | 결정 |
|------|------|
| 약칭 법률명 | 공식 약칭 사용. `Act on...` → `...법` |
| 법률 전체 인용 | `제X조 제Y항 제Z호` 형식. 예: `Article 3(2)(a)` → `제3조 제2항 제a호` |
| 시행령/시행규칙 | `Enforcement Decree` → `시행령`, `Enforcement Rule` → `시행규칙` |
| 조례/규칙 | `Ordinance` → `조례`, `Rule` → `규칙` |
| 고시/예규 | `Public Notice` → `고시`, `Directive` → `예규` |
| 법률 개정 사항 | `wholly amended` → `전부 개정`, `partially amended` → `일부 개정` |
| 시행일 | `effective date` → `시행일`, `promulgation date` → `공포일` |
| 부칙 | `Supplementary Provisions` → `부칙` |

### D5: 행정 절차 용어

| 조건 | 결정 |
|------|------|
| 허가/면허 | `permit / license` → `허가 / 면허` |
| 신고 | `report / registration` → `신고` (신고제: 행정법상 개념) |
| 인가 | `approval / authorization` → `인가` |
| 등록 | `registration` → `등록` |
| 취소/정지 | `revocation / suspension` → `취소 / 정지` |
| 과태료/과징금 | `administrative fine / penalty surcharge` → `과태료 / 과징금` (구분 번역 필요) |
| 이의 신청 | `objection` → `이의 신청` |
| 행정 심판 | `administrative appeal` → `행정 심판` |
| 행정 소송 | `administrative litigation` → `행정 소송` |
| 처분 | `disposition / administrative decision` → `처분` |
| 민원 | `civil complaint / petition` → `민원` |
| 제도/제재 | `system / sanction` → `제도 / 제재` |

### D6: 영문-한국어 행정 용어 대응

| 조건 | 결정 |
|------|------|
| Certificate of Employment | `재직 증명서` |
| Certificate of Career / Work Experience | `경력 증명서` |
| Certificate of Graduation / Diploma | `졸업 증명서` |
| Academic Transcript | `성적 증명서` |
| Certificate of Business Registration | `사업자 등록 증명원` |
| Certificate of Tax Payment | `납세 증명서` |
| Criminal Record Certificate | `범죄 경력 회보서` 또는 `기본 증명서` |
| Certificate of Marriage / Marriage Report | `혼인 관계 증명서` / `혼인 신고서` |
| Certificate of Nationality | `국적 증명서` |
| Certificate of Foreign Registration | `외국인 등록 증명서` (한국 거주 외국인용) |
| Passport / Visa | `여권` / `사증(Visa)` — 비자보다 사증이 공식 용어 |
| Certificate of Alien Registration | `외국인 등록 사실 증명` |

### D7: 행정 문서 문체 및 서식

| 조건 | 결정 |
|------|------|
| 공문서 본문 | `~합니다` 체(합쇼체) 유지 — 가장 격식 높은 어체 |
| 제목 | `[지역/기관명]` 형식. `제목: [문서 제목]` |
| 본문 첫 문장 | `이에 [내용]을 아래와 같이 알립니다/통지합니다/공고합니다.` 등 정형화된 서두 사용 |
| 항목 구분 | `가.`, `나.`, `다.` 또는 `1.`, `2.`, `3.` 체계 |
| 하위 항목 | `1)`, `2)`, `3)` 또는 `(가)`, `(나)`, `(다)` |
| 종결 어미 | `~합니다`, `~입니다`, `~이 있습니다` 등 합쇼체 일관 유지 |
| 기간 표현 | `~부터 ~까지` 또는 `~이내에` |
| 조건부 표현 | `~하는 경우`, `~하지 아니하는 경우` — 행정 문서의 전형적 조건문 |

### D8: 번역 시 한국어 맞춤법 및 편집

| 조건 | 결정 |
|------|------|
| 띄어쓰기 | 국립국어원 한글 맞춤법 규정 엄격 준수 |
| 외래어 표기 | 국립국어원 외래어 표기법에 따름. 예외: 기존에 통용되는 표기가 있는 경우 해당 표기 우선 |
| 숫자와 단위 사이 | 띄어쓰기. `30일`, `5년`, `100건` |
| 문장 부호 | 한국어 문장 부호 규정(국립국어원) 준수. 큰따옴표 `""` / 작은따옴표 `''` 올바르게 사용 |
| 가나다 순 정렬 필요 시 | 한글 자모 순서(가나다순)에 따라 정렬. 영문과 혼용 시 별도 정렬 규칙 확인 |
| 한자 사용 | 행정 문서에서 필요한 경우에만 한자 병기. 과도한 한자 사용 자제 |
| 로마자 표기 | 국립국어원 로마자 표기법 준수 (2000년 개정안). 인명 지명 등 고유 명사에 적용 |

---

## Standards (표준 및 참조)

### 공문서 관련 법규 및 기준

| 법규/규정 | 영문 명칭 | 적용 분야 |
|-----------|-----------|----------|
| **행정업무의 운영 및 혁신에 관한 규정** | Regulations on the Operation and Innovation of Administrative Work | 대통령령. 공문서 작성 기본 규칙 |
| **행정절차법** | Administrative Procedures Act | 행정 처분, 공고, 의견 청취 |
| **공공기관의 정보공개에 관한 법률** | Act on Information Disclosure by Public Institutions | 정보 공개 청구 |
| **민원 처리에 관한 법률** | Civil Petitions Treatment Act | 민원 처리 절차 |
| **개인정보 보호법** | Personal Information Protection Act | 개인 정보 보호 및 처리 |
| **전자 문서법** | Electronic Documents Act | 전자 문서 효력 및 관리 |
| **문서의 작성 등에 관한 규칙** | Rules on Document Preparation | 행정안전부 예규. 세부 서식 규정 |
| **행정 효율과 협업 촉진에 관한 규정** | Regulations on Administrative Efficiency and Collaboration Promotion | 기관 간 문서 협업 |

### 한국 정부 기관 체계

| 기관 유형 | 영문 번역 | 예시 |
|-----------|-----------|------|
| 부 (Ministry) | Ministry of... | 행정안전부 (Ministry of the Interior and Safety) |
| 처 (Office/Ministry) | Office/Ministry of... | 국무조정실 (Office for Government Policy Coordination) |
| 청 (Service/Administration) | Korea...Service / Administration | 경찰청 (Korean National Police Agency) |
| 위원회 (Commission/Committee) | ...Commission / Committee | 금융위원회 (Financial Services Commission) |
| 원 (Agency) | ...Agency | 국세청 (National Tax Service) |
| 특별지방행정기관 | Regional Administrative Agency | 지방경찰청, 교육청 |
| 지방자치단체 | Local Government | 서울특별시, 경기도, 제주특별자치도 |

### 한국 주소 체계 번역

| 구성 요소 | 영문 표기 | 설명 |
|-----------|-----------|------|
| 도로명 주소 | Road Name Address | 2014년 전면 시행. `도로명, 건물 번호` 체계 |
| 지번 주소 | Lot Number Address | 구 주소 체계. `동/리, 번지` |
| 시/도 | City / Province | `서울특별시, 경기도, 제주특별자치도` |
| 시/군/구 | City / County / District | `성남시, 고양시, 서초구` |
| 읍/면/동 | Eup/Myeon/Dong | 행정 구역 하위 단위. 로마자 표기 유지 권장 |
| 리 | Ri | 읍/면 하위 구역 |
| 길/Ro | Road / Street | 도로명 체계에서 자주 사용 |

### 행정 문서의 종류

| 문서 유형 | 영문 번역 | 특징 |
|-----------|-----------|------|
| 공고 | Public Notice / Announcement | 행정 기관이 일반인에게 알림 |
| 고시 | Official Notice / Public Notification | 법규적 효력이 있는 공고 |
| 훈령 | Directive / Administrative Directive | 내부적 규율 |
| 예규 | Instruction / Standard Operating Procedure | 처리 기준 명시 |
| 지침 | Guideline | 업무 수행 세부 기준 |
| 통지 | Notice / Notification | 특정인에 대한 통보 |
| 증명 | Certificate | 사실 증명 |
| 허가증 | Permit / License | 행위 허가 |

### 주요 주의사항

1. **결재와 결제 구분** — `결재(決裁)`는 상급자의 승인, `결제(決濟)`는 지급. 행정 문서에서는 `결재`가 대부분.
2. **수신자와 발신자** — 한국 공문서는 수신자가 발신자보다 우선. 문서 상단에 `수신: [기관명]`, 하단에 `발신: [기관명]` 또는 `[부서명]`.
3. **행정 문서의 날짜 기입** — 문서 상단 또는 하단에 `시행일: YYYY. MM. DD.` 형식.
4. **공개 구분 필수 포함** — `공개(公開)` 또는 `비공개(非公開)`를 문서 상단에 명시.
5. **기관명 번역 일관성** — 동일한 기관명은 문서 전체에서 동일한 영문 번역 사용. 공식 영문 명칭이 있는 경우 반드시 사용.
6. **한국 주소 번역** — 한국 주소는 영문 번역 시 거꾸로 (작은 단위 → 큰 단위) 순서 사용. 예: `(Dong, Gu, City, Province)`.
7. **외국인 관련 행정 용어** — `외국인 등록 번호`, `비자 사증 발급`, `체류 자격 변경` 등은 여권 정보와 일치해야 하며, 법무부 출입국 공식 용어 확인 필수.

## Error Pattern Library (오류 패턴 라이브러리)

### Critical Errors (제로 허용 오류)

| Error | Why It Is Critical |
|-------|-------------------|
| **기관명 오번역** | "행정안전부"를 "Ministry of Public Administration"이 아닌 공식 영문명 "Ministry of the Interior and Safety"로 번역해야 함. 비공식 명칭 사용 시 공식 기록에서 문서 식별 불가. |
| **참조 번호 변경/누락** | 문서번호, 접수번호, 공시번호 등 모든 참조 번호는 단일 문자도 변경 금지. 번호 누락은 문서의 행정적 추적을 불가능하게 함. |
| **공문서 구조 훼손** | 수신-발신-결재-시행 체계가 훼손되면 문서의 행정적 효력 상실. 행정안전부 공문서 규정에 따른 구조 유지. |
| **법률 조문 인용 오류** | 행정 처분의 법적 근거가 되는 조문 인용 오류는 처분 자체의 효력을 다투는 사유가 됨. 법률명, 조, 항, 호의 정확한 표기 필수. |
| **날인/도장 설명 누락** | 한국 공문서에서 공식 날인(직인, 인감)의 유무는 문서의 효력과 직결. 날인의 종류와 위치를 정확히 설명 또는 보존. |

### Common Errors (빈번한 오류)

| Error | Guidance |
|-------|----------|
| **결재와 결제 혼동** | "결재(決裁)"는 상급자의 승인. "결제(決濟)"는 대금 지급. 행정 문서에서는 99% "결재"가 맞는 표현. "approval"은 "결재"로 번역. |
| **공문서 서식 오류** | 한국 공문서는 제목(제목:), 수신, 발신, 결재란, 시행일, 문서번호 등이 정해진 위치에 있음. 이 구조를 유지하지 않으면 문서가 공문서로 인식되지 않음. |
| **행정 구역 명칭 오류** | "서울특별시"는 "Seoul", "경기도"는 "Gyeonggi-do", "제주특별자치도"는 "Jeju-do" 등 공식 로마자 명칭 확인 필수. |
| **공개 구분 누락** | 한국 공문서는 문서 상단에 "공개(公開)" 또는 "비공개(非公開)"를 반드시 표시. 번역 시에도 이 정보를 유지. |
| **보존 연한 정보 누락** | 공문서 하단의 "보존 연한: 5년" 등 기록물 보존 기간 정보를 번역에서 누락하지 않도록 주의. |
| **행정 용어의 비공식 번역** | "처분(disposition)", "고시(public notice)", "훈령(directive)" 등 행정법상 개념을 일반 용어로 대체하지 않음. |

### Subtle Errors (놓치기 쉬운 오류)

| Error | Guidance |
|-------|----------|
| **한국 주소 체계의 잘못된 순서** | 한국 주소는 큰 단위에서 작은 단위로(시/도 → 구 → 동 → 번지). 영문 번역 시 작은 단위에서 큰 단위로 순서 변경 필요. |
| **행정동 vs 법정동 구분** | 한국의 "동"은 행정동(administrative dong)과 법정동(legal dong)으로 구분됨. 주소 체계에서 이 차이를 인식하고 번역. |
| **주민등록번호 형식** | 한국 주민등록번호는 13자리(YYMMDD-SSSSSSC). 외국인등록번호는 다른 형식. 번역 시 형식을 변경하지 말고 그대로 보존. "RRN" 약어 설명 병기. |
| **도장 색상/형태 정보** | 한국 공문서의 빨간색 직인(관인), 검은색 일반 도장, 날인/서명의 차이는 법적 효력과 관련됨. 도장 종류와 위치를 설명. |
| **전자문서 vs 종이문서** | 한국 행정전자문서(온나라 시스템 등)와 종이문서의 형식이 다를 수 있음. 전자문서의 결재선, 전자서명 정보 보존. |
| **행정 예규 번호** | 행정안전부 예규, 기관별 고시/훈령 번호는 법적 효력을 가지므로 번호와 제목을 정확히 보존. |

## Domain-Specific Reference (분야별 참조)

### Korean Government Organizational Structure (한국 정부 조직 체계)

| Level | Korean | English | Examples |
|-------|--------|---------|----------|
| 1 | 부 (Ministry) | Ministry | 행정안전부, 기획재정부, 법무부 |
| 2 | 처 (Office) | Office / Ministry | 국무조정실, 법제처 |
| 3 | 청 (Service / Administration) | Service / Administration | 경찰청, 국세청, 관세청, 소방청 |
| 4 | 위원회 (Commission) | Commission / Committee | 금융위원회, 공정거래위원회 |
| 5 | 원 (Agency) | Agency | 국가인권위원회, 국민권익위원회 |
| 6 | 본부 (Headquarters) | Headquarters | 중앙재난안전대책본부 |
| 7 | 국 / 실 (Bureau / Office) | Bureau / Office | 운영지원과, 기획재정담당관 |
| 8 | 과 / 팀 (Division / Team) | Division / Team | 행정관리과, 인사팀 |

### 공문서 작성 표준 템플릿 (Official Document Template Elements)

| Korean Element | English Translation | Position |
|---------------|-------------------|----------|
| 문서번호 | Document Number | Top of document header |
| 시행일 | Date of Issue | Header, right side |
| 수신 | To (Recipient) | Header, top |
| 발신 | From (Sender) | Footer or header |
| 제목 | Subject / Title | Center, bold |
| 첨부 / 붙임 | Attachment(s) | Below subject line |
| 상기 | The Above / Said | Formal reference to above text |
| 이에 | Accordingly / Hereby | Formal opening of body text |
| 아래와 같이 | As follows | Introducing enumerated items |
| 귀하 | Dear Sir/Madam (formal) | Used in addressing the recipient |
| 외 | Etc. / And others | For multiple recipients or items |
| 끝 | End | Marks the end of document body |
| 결재 | Approval | Bottom, with approval line |
| 기안 | Draft | Individual who prepared the document |
| 검토 | Review | Reviewer before final approval |
| 협조 | Coordination | Cross-department collaboration note |

### Common Korean Administrative Forms (한국 행정 양식)

| Korean Form Name | English Translation | Issuing Authority |
|-----------------|-------------------|-------------------|
| 주민등록증 | Resident Registration ID Card | 행정안전부 |
| 운전면허증 | Driver's License | 경찰청 |
| 여권 | Passport | 외교부 |
| 사업자등록증 | Business Registration Certificate | 국세청 |
| 건강보험증 | Health Insurance Card | 국민건강보험공단 |
| 국민연금 가입자 증명서 | National Pension Enrollment Certificate | 국민연금공단 |
| 출입국사실증명서 | Certificate of Entry and Exit | 법무부 출입국 |
| 외국인등록증 | Alien Registration Card | 법무부 출입국 |
| 건축물대장 | Building Register | 지방자치단체 |
| 토지대장 | Land Cadastre | 지방자치단체 |

### 행정 절차 관련 용어 (Administrative Procedure Terms)

| English | Korean | Definition |
|---------|--------|------------|
| Permit / License | 허가 / 면허 | Administrative permission to conduct an activity |
| Registration | 등록 | Entry in an official register |
| Report / Declaration | 신고 | Notification to authorities |
| Approval | 인가 | Prior approval by authority |
| Authorization | 승인 | Official consent |
| Revocation | 취소 / 철회 | Withdrawal of administrative action |
| Suspension | 정지 | Temporary halt of permission |
| Disposition | 처분 | Administrative decision (broadest term) |
| Administrative Appeal | 행정심판 | Internal appeal against disposition |
| Administrative Litigation | 행정소송 | Court challenge of administrative action |
| Civil Petition | 민원 | Citizen request for service |
| Public Hearing | 공청회 | Public hearing before decision |
| Notice / Announcement | 공고 / 고시 | Public notification |
| Correction Order | 시정명령 | Order to remedy violation |
| Fine / Penalty | 과태료 / 과징금 | Administrative monetary penalty |

### 보유 기관별 증명서 (Certificates by Issuing Authority)

| Certificate | Korean | Issuing Agency |
|------------|--------|---------------|
| Certificate of Resident Registration | 주민등록초본 | 동사무소 / 구청 |
| Certificate of Family Relations | 가족관계증명서 | 동사무소 / 구청 |
| Certificate of Marriage | 혼인관계증명서 | 동사무소 / 구청 |
| Certificate of Business Registration | 사업자등록증명원 | 국세청 |
| Certificate of Tax Payment | 납세증명서 | 국세청 |
| Certified Copy of Register | 등기사항증명서(등기부등본) | 법원 등기소 |
| Certificate of Employment | 재직증명서 | Employers |
| Certificate of Career | 경력증명서 | Employers / Former employers |
| Certified Copy of Corporate Register | 법인등기사항증명서 | 법원 등기소 |
| Certificate of Seal Impression | 인감증명서 | 동사무소 / 구청 |
| Certificate of Nationality | 국적증명서 | 법무부 / 대사관 |
| Criminal Background Check | 범죄경력회보서(기본증명서) | 경찰청 |

### Number and Code Format Reference (번호 및 코드 형식 참조)

| Code Type | Korean Format | Example | Notes |
|-----------|--------------|---------|-------|
| Resident Registration Number (RRN) | 주민등록번호 | 000101-4xxxxxx | 13 digits with dash |
| Business Registration Number | 사업자 등록 번호 | 000-00-00000 | 10 digits with dashes |
| Corporate Registration Number | 법인 등록 번호 | 000000-0000000 | 13 digits |
| Foreign Registration Number | 외국인 등록 번호 | 000000-0000000 | 13 digits |
| Passport Number | 여권 번호 | M00000000 | Alphanumeric |
| Driver's License Number | 운전면허 번호 | 00-00-000000 | 11 digits with dashes |
| Real Estate Register Number | 등기 필증 번호 | 0000-0000-0000 | Alphanumeric |
| DART Filing Number | 공시 번호 | 20250000000 | Year-based sequential |
| Patent Number | 특허 번호 | 10-0000000-0 | Korean patent format |
| Postal Code | 우편번호 | 00000 | 5 digits |
