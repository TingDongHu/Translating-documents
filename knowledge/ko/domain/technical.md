---
id: ko/domain/technical
type: domain
target_lang: ko
name: 기술 문서 번역 규정
description: KS 표준, 기술 문서, 사용 설명서, 사양서, 과학 논문 번역 규칙
---

## Reader Model (독자 모델)

**누가 이 문서를 읽고 무엇을 기대하는가?**

기술 문서의 독자는 엔지니어, 기술자, 운영자, 유지보수 담당자로서 문서를 참고하여 작업을 정확하고 안전하게 수행한다. 다음을 기대한다:

- **정확성 최우선** — 모든 측정값, 공차, 사양은 원본과 정확히 일치해야 한다. 단일 오류는 장비 손상, 안전 사고 또는 제품 불량을 초래할 수 있다.
- **일관된 용어** — 어떤 부품이 5페이지에서 "액추에이터(actuator)"로 명명되었다면 20페이지에서 "구동기"로 바뀌지 않아야 한다. 독자는 용어 안정성에 의존하여 정보를 신속히 찾는다.
- **명확한 절차** — 단계별 지침은 모호함이 없어야 한다. 독자가 다음 동작을 추측하거나 중요한 안전 주의사항을 유추해야 해서는 안 된다.
- **표준 관행 준수** — 단위, 기호, 약어, 형식은 KS 표준 및 ISO/IEC 국제 표준을 따른다. 이탈 시 독자의 신뢰가 하락한다.

**무엇이 신뢰를 무너뜨리는가?**
- 모델 번호나 부품 번호 오번역으로 인한 잘못된 부품 주문
- 안전 경고 등급 오류 (예: "주의"가 필요한 곳에 "경고" 사용)
- 변환 누락 또는 잘못된 측정 단위 변환
- 일관성 없는 상호 참조로 인한 엉뚱한 섹션 참조

---

## Decision Framework (의사결정 체계)

### D1: 단위 및 측정

| 조건 | 결정 |
|------|------|
| 원본에 측정값과 단위가 포함된 경우 | 숫자 값을 정확히 보존하고, 한국어 형식(띄어쓰기) 적용. 예: `10 mm` → `10 mm` |
| 원본이 비SI 단위를 사용하는 경우 | 원래 단위와 값을 유지. 프로젝트에서 명시적으로 지시하지 않는 한 SI로 변환하지 않음 |
| 온도가 섭씨(°C)로 주어진 경우 | 섭씨 유지. 프로젝트 지시사항에 명시된 경우에만 화씨를 괄호로 추가 |
| 복합 단위가 나타나는 경우 (예: N-m, kg/m³) | 단위 기호를 정확히 유지. KS A ISO 80000 표기법 사용 |
| 단위가 숫자 뒤에 오는 경우 | 숫자와 단위 사이에 공백. 예: `10mm` → `10 mm` |
| 한국어 고유 단위(평, 돈, 근, 관)가 포함된 경우 | 원래 한국어 단위 유지 후, 괄호 안에 SI 환산값 병기 |
| % 기호 사용 | 숫자와 % 기호 사이 공백 없음 (KS 표준): `10%` |

### D2: 안전 경고 (KS S 기준)

| 조건 | 결정 |
|------|------|
| 즉각적인 위험(사망/중상)을 나타내는 신호어 | **위험** (DANGER) — 굵은 빨간색 글씨, 경고 삼각형 기호와 함께 사용 |
| 잠재적 위험(중상 가능)을 나타내는 신호어 | **경고** (WARNING) — 굵은 글씨, 주의 기호와 함께 사용 |
| 경미한 부상 또는 재산 피해 위험 | **주의** (CAUTION) — 일반 글씨, 안내 기호와 함께 사용 |
| 정보 제공 목적의 알림 | **참고** (NOTE) — 경고 기호 없이 사용 |
| 안전 기호 또는 픽토그램이 포함된 경우 | 기호 참조를 정확히 유지. 설명 텍스트만 번역 |
| 다단계 경고 메시지 | 위험/경고/주의 + 결과 설명 + 예방 조치 순서 유지 |

### D3: 상호 참조

| 조건 | 결정 |
|------|------|
| 다른 섹션 번호 참조 | 섹션 번호를 원본과 동일하게 유지. `See Section 3.1` → `제3.1절 참조` |
| 그림/표/다이어그램 참조 | 그림/표 번호를 정확히 유지. 캡션은 번역. `See Figure 5` → `그림 5 참조` |
| 페이지 번호 참조 | 원본 페이지 번호 유지(DTP 재배치 시 대상 레이아웃 페이지 번호 사용 가능) |
| 수식 참조 | 수식 번호 괄호 안에 유지. `See Equation (3)` → `수식 (3) 참조` |
| 부록 참조 | `See Appendix A` → `부록 A 참조` |
| 표준 문서 참조 | 전체 표준 번호를 포함. `per KS B ISO 2768-1` → `KS B ISO 2768-1에 따라` |

### D4: 사용자 인터페이스 라벨 및 컨트롤

| 조건 | 결정 |
|------|------|
| 물리적 버튼/스위치/표시기 라벨 | 한국어 표준 UI 용어로 번역. 예: `ON/OFF` → `켜기/끄기`, `STOP` → `정지`, `RESET` → `초기화` |
| 소프트웨어 UI 문자열 | 번역하되, 소프트웨어 자체가 현지화되지 않은 경우 대괄호로 원문 병기 |
| 키보드 단축키 포함 라벨 | 단축키 조합은 그대로 유지. 동작 설명만 번역 |
| 에러 메시지 | 코드는 유지, 메시지 본문만 번역. `Error 0xE4: Paper jam` → `오류 0xE4: 용지 걸림` |

### D5: 기술 용어 및 전문 용어

| 조건 | 결정 |
|------|------|
| 영어 약어/두문자어 | 한국어에서 통용되는 경우 그대로 유지. 첫 사용 시 한국어 설명 병기. 예: `PLC (Programmable Logic Controller)` → `PLC(프로그래밍 가능 논리 제어기)` |
| 한국어 대체 용어가 있는 약어 | 한국어 약어 사용. `CAD` → `CAD(컴퓨터 지원 설계)` 또는 `캐드` |
| 국립국어원 표준 용어가 있는 경우 | 국립국어원 한국어 기초사전 및 표준국어대사전 용어 우선 사용 |
| 업계 관행 용어 vs 표준 용어 | KS 표준 및 국립국어원 권장 용어 우선. 업계 관행 용어는 괄호로 병기 |
| 신조어/외래어 | 한글 표기를 원칙으로 하되, 필요시 원어를 괄호에 병기 |
| 단위 명칭 | 인명에서 유래한 단위: 한글 표기 + 기호. 예: `pascal → 파스칼(Pa)`, `watt → 와트(W)` |

### D6: 그림 및 표 캡션

| 조건 | 결정 |
|------|------|
| 그림 캡션 | `Figure 1 — System architecture` → `그림 1 — 시스템 아키텍처` |
| 표 캡션 | `Table 5 — Specifications` → `표 5 — 사양` 또는 `표 5 기술 사양` |
| 표 머리글 열 | 명사형, 단수형 사용. `Voltage (V)` → `전압(V)` |
| 여러 페이지에 걸친 표 | 다음 페이지 상단에 `표 5 (계속)` 표기, 헤더 행 반복 |
| 표 내 숫자 데이터 | 한국어 형식(쉼표 천 단위 구분, 마침표 소수점) 유지 |
| 그림 내 텍스트(flowchart 등) | 간결하게 번역(2-4단어, 명사형 종결) |

### D7: 절차 및 지침

| 조건 | 결정 |
|------|------|
| 명령형 지시 | 해라체(명령형 종결 어미) 사용. `Press the button` → `버튼을 누르십시오.` |
| 조건부 지시 | `If..., then...` → `...면, ...하십시오.` `If alarm sounds, stop the machine` → `경보가 울리면, 기계를 정지하십시오.` |
| 부정 명령 | `Do not...` → `...하지 마십시오.` `Do not touch rotating parts` → `회전 부품을 만지지 마십시오.` |
| 단계별 절차 | 번호 목록 사용. 각 단계는 동사로 시작. `1. 전원을 끄십시오. 2. 덮개를 여십시오.` |
| 참고 사항 | `참고:` 접두어 사용. 본문과 구분. `참고. 필요한 경우 반복하십시오.` |

### D8: 수식 및 과학 표기

| 조건 | 결정 |
|------|------|
| 수식 내 변수 | 라틴 문자 유지, 설명 텍스트만 번역. `where: F — force, m — mass` → `여기서: F — 힘, m — 질량` |
| 수식 이름 | `Formula 1 — Ohm's law` → `수식 1 — 옴의 법칙` |
| 수식 설명 | `where:` → `여기서:` (새 줄, 콜론) |
| 아래첨자/위첨자 | 라틴 문자 하첨자는 유지, 설명은 한글로. `T_max` → `T_최대` 또는 `T_max` 유지 후 한글 설명 |

### D9: 날짜 및 숫자 형식

| 조건 | 결정 |
|------|------|
| 날짜 표현 | `2025-04-30` 또는 `2025년 4월 30일` 형식 사용. `04/05/2025` 등 모호한 형식 금지 |
| 시간 표기 | 24시간제 사용. `3:00 PM` → `15:00` |
| 천 단위 구분 | 쉼표 사용. `1,000,000` |
| 소수점 | 마침표 사용. `3.14` |
| 통화 금액 | 원화는 `₩` 또는 `원`, 달러는 `USD` 또는 `$`, 숫자와 통화 기호 사이 공백 없음 |

### D10: 경어법 및 문체

| 조건 | 결정 |
|------|------|
| 기술 문서 본문 | 합니다체(합쇼체) 사용 — 공식적이고 격식 있는 문체 |
| 주의/경고문 | 명령형 또는 해야 한다 체계 사용 |
| 각주/참고 | 합니다체 유지 |
| 원문의 비공식적 문체 | 한국어 기술 문서 관행에 맞춰 격식체로 변환 |
| 번역자 주 | `- 번역자 주` 또는 `[TN: ...]` 형식으로 표시 |

---

## Standards (표준 및 참조)

### 한국 산업 표준 (KS) - 기술 문서 관련

| 표준 번호 | 명칭 | 적용 분야 |
|-----------|------|----------|
| **KS A ISO 80000-1** | 양 및 단위 - 제1부: 일반 | 단위 및 양의 표기법 |
| **KS A ISO/IEC Guide 51** | 안전 측면 - 표준에 포함할 지침 | 안전 경고 수준 분류 |
| **KS A 0001** | 표준 번호 체계 | KS 표준 번호 체계 |
| **KS A 1001** | 문서의 작성 및 서식 | 기술 문서 기본 서식 |
| **KS S 1003** | 한국어 기술 문서 작성 지침 | 한국어 기술 문서 용어 및 문체 |
| **KS X ISO 639-1** | 언어 부호 | 언어 코드 표기법 |
| **KS X ISO 3166-1** | 국가 부호 | 국가 코드 표기법 |
| **KS X ISO 8601** | 날짜 및 시간 형식 | 날짜/시간 표기법 |

### 한국어 기술 용어 관련 기관

| 기관 | 역할 | 참고 |
|------|------|------|
| **국립국어원** | 한국어 표준어 및 외래어 심의 | 표준국어대사전, 외래어 표기법 |
| **한국산업표준원 (KATS)** | KS 표준 제정 및 관리 | 산업 표준 총괄 |
| **국가기술표준원** | 기술 표준 및 적합성 평가 | KS 인증, 단위 표준 |
| **한국정보통신기술협회 (TTA)** | IT/통신 표준 | ICT 용어 표준화 |
| **대한기계학회** | 기계 분야 용어 표준 | 기계 기술 용어 |

### 기술 문서 번역 시 주요 준수 사항

1. **KS 표준 용어 우선** — KS 표준에 정의된 용어가 있으면 반드시 해당 용어 사용
2. **국립국어원 외래어 표기법 준수** — 외래어는 국립국어원 제정 외래어 표기법에 따라 표기
3. **한자어와 고유어 균형** — 기술 용어는 한자어를 우선하되, 지나친 한자어 사용 지양
4. **띄어쓰기 엄수** — 한글 맞춤법 띄어쓰기 규칙(국립국어원) 철저히 준수
5. **로마자 약어 유지** — 국제적으로 통용되는 기술 약어(PLC, HMI, CNC, PID 등)는 원형 유지
6. **단위 표기** — KS A ISO 80000에 따라 숫자와 단위 사이 공백, 올바른 단위 기호 사용
7. **도표/그림 캡션** — "그림 1 — ...", "표 1 — ..." 형식(그림/표 번호 뒤 공백 + 줄표)
8. **안전 문구** — KS S 기준 경고 등급(위험/경고/주의/참고) 정확히 매핑

### 측정 단위 한글 표기

| 영문 단위 | 한글 표기 | 기호 | 비고 |
|-----------|-----------|------|------|
| millimeter | 밀리미터 | mm | |
| centimeter | 센티미터 | cm | |
| meter | 미터 | m | |
| kilogram | 킬로그램 | kg | |
| liter | 리터 | L | |
| degree Celsius | 섭씨온도 | °C | |
| pascal | 파스칼 | Pa | |
| newton | 뉴턴 | N | |
| watt | 와트 | W | |
| hertz | 헤르츠 | Hz | |
| volt | 볼트 | V | |
| ampere | 암페어 | A | |
| revolution per minute | 알피엠 | r/min 또는 rpm | 관행적 rpm 허용 |

## Error Pattern Library (오류 패턴 라이브러리)

### Critical Errors (제로 허용 오류)

| Error | Why It Is Critical |
|-------|-------------------|
| **부품번호/모델번호 오번역** | OEM 부품 번호는 카탈로그 조회의 핵심 식별자. 한 글자만 달라도 다른 부품으로 인식되어 주문 오류 발생. 숫자와 영문자 혼동(0/O, 1/l/I)에 각별히 주의. |
| **안전 경고 레벨 불일치** | 위험/경고/주의는 산업안전보건법상 법적 효력이 다름. 레벨 오류는 법적 책임 문제로 이어짐. |
| **측정값/수치 변경** | 공차, 치수, 정격값 등 모든 수치는 엔지니어링 요구사항. 0.01mm 변경도 기계 가공 불량 초래 가능. |
| **단위 변환 무단 수행** | 비SI 단위를 SI로 변환하거나 반대로 변환하는 것은 사전 승인 없이 금지. 변환 오류는 안전 사고로 이어짐. |
| **검사 기준 오번역** | 합격/불합격 기준, AQL 값, 허용公差 등 품질 기준 오류는 제품 불량 및 클레임으로 이어짐. |

### Common Errors (빈번한 오류)

| Error | Guidance |
|-------|----------|
| **외래어 표기 불일치** | 동일한 영문 기술 용어가 문서 내에서 여러 형태로 표기됨 (예: 와셔/워셔, 커넥터/컨넥터). 프로젝트 내에서 한 가지 표기로 통일. 국립국어원 외래어 표기법 참조. |
| **능동태/수동태 혼용** | 지침은 명령형(~하십시오/~하세요)으로 작성. 사양 설명은 서술형(~된다/~되어 있다)으로 작성. 인접 단계에서 혼용 금지. |
| **약어 번역 오류** | 국제적 기술 약어(PLC, HMI, CNC, PID, PCB, LED)는 영문 그대로 유지. 첫 사용 시에만 한글 풀네임 병기. |
| **KS 표기법 오류** | KS 표준 번호는 `KS [분류문자] [번호]:[연도]` 형식. ISO, JIS, DIN 등 다른 국가 표준과 혼동 금지. |
| **단위 기호 형식 오류** | 숫자와 단위 사이 공백 필수(10 mm, 10 kg). % 기호는 숫자 뒤 공백 없음(10%). |

### Subtle Errors (놓치기 쉬운 오류)

| Error | Guidance |
|-------|----------|
| **겹낫표 vs 따옴표 오용** | 한국어 기술 문서에서 「」(겹낫표)는 장/절 이름에 사용. ""(큰따옴표)는 인용에 사용. 혼용 주의. |
| **차원 표기 × vs X** | 기술 도면과 사양서에서 차원 표기는 반드시 ×(곱하기 기호 U+00D7) 사용. 영문 X와 혼동 금지. |
| **일본식 기술 용어 잔재** | 일부 한국어 기술 용어에 일본어에서 유래한 표현이 남아 있음 (드라이버, 가스켓). 현대 문서에서는 영어 유래 외래어 사용 권장. |
| **날짜 형식 모호성** | "04/05/2025"는 4월 5일 또는 5월 4일로 해석 가능. "2025-04-30" 또는 "2025년 4월 30일" 사용. |
| **천단위 구분자 혼용** | 일부 유럽식 표기(점을 천단위 구분)가 혼입되지 않도록 주의. 한국어는 쉼표가 천단위 구분자. |
| **한자어와 고유어 혼동** | 일부 기술 용어는 한자어(전동기, 차단기)와 외래어(모터, 서킷브레이커)가 공존. 업계 관행 확인 후 선택. |

## Domain-Specific Reference (분야별 참조)

### KS Standard Divisions (한국산업표준 분류)

| Division Letter | Field | Example |
|----------------|-------|---------|
| KS A | Basic standards, terminology, units | KS A 0001 (standard dimensions) |
| KS B | Mechanical engineering | KS B 1002 (bolts, screws, nuts) |
| KS C | Electrical and electronics | KS C IEC 60034 (rotating electrical machines) |
| KS D | Metallurgy and materials | KS D 3503 (rolled steel) |
| KS E | Mining | KS E 0001 |
| KS F | Civil engineering and construction | KS F 2280 (ready-mixed concrete) |
| KS G | Architecture | KS G 2001 |
| KS H | Food and pharmaceuticals | KS H 2001 |
| KS K | Textiles | KS K 0001 |
| KS L | Ceramics | KS L 1001 |
| KS M | Chemicals | KS M 0001 |
| KS P | Pulp and paper | KS P 0001 |
| KS Q | Quality management and statistics | KS Q ISO 9001:2023 |
| KS R | Automotive | KS R 0001 |
| KS S | Safety and health | KS S 0001 |
| KS T | Mechanical tools | KS T 0001 |
| KS V | Shipbuilding | KS V 0001 |
| KS W | Aerospace | KS W 0001 |
| KS X | Information technology | KS X 0001 |

Note: KS standards are managed by KATS (국가기술표준원).

### Standard Unit Terms in Korean (표준 단위 한글 표기)

| Quantity | Unit | Korean (spelled out) | Abbreviation |
|----------|------|---------------------|--------------|
| Length | millimeter, centimeter, meter, kilometer | 밀리미터, 센티미터, 미터, 킬로미터 | mm, cm, m, km |
| Mass | gram, kilogram, tonne | 그램, 킬로그램, 톤 | g, kg, t |
| Volume | liter, milliliter | 리터, 밀리리터 | L, mL |
| Temperature | degree Celsius | 섭씨/도씨 (archaic) | °C |
| Time | second, minute, hour | 초, 분, 시간 | s, min, h |
| Electric current | ampere | 암페어 | A |
| Voltage | volt | 볼트 | V |
| Power | watt, kilowatt | 와트, 킬로와트 | W, kW |
| Pressure | pascal, bar | 파스칼, 바 | Pa, bar |
| Force | newton | 뉴턴 | N |
| Torque | newton-meter | 뉴턴미터 | N-m |
| Frequency | hertz | 헤르츠 | Hz |
| Rotational speed | revolutions per minute | 알피엠 | rpm |

### Korean Safety Warning Hierarchy (안전 경고 체계, 산업안전보건법 기준)

| Korean Signal Word | English Equivalent | Level | Meaning |
|-------------------|-------------------|-------|---------|
| 위험 | DANGER | Highest | Immediate hazard resulting in death or serious injury |
| 경고 | WARNING | High | Potential hazard that could result in death or serious injury |
| 주의 | CAUTION | Medium | Potential hazard that could result in minor or moderate injury |
| 참고 / 알림 | NOTICE / NOTE | Low | Important information but not hazard-related |
| 안전 지침 | SAFETY INSTRUCTION | — | Safety-related instruction that must be followed |

### Common Technical Loanword Orthography (기술 외래어 표준 표기)

| English Source | Standard Korean | Industry Notes |
|---------------|----------------|----------------|
| Actuator | 액추에이터 | Also "구동기" in some contexts |
| Bearing | 베어링 | Never "베아링" |
| Cable | 케이블 | Standard form |
| Capacitor | 커패시터 | Also "콘덴서" (older, from Japanese) |
| Circuit breaker | 차단기 | Also "서킷 브레이커" |
| Connector | 커넥터 | Never "컨넥터" |
| Controller | 컨트롤러 | Also "제어기" |
| Cylinder | 실린더 | Standard form |
| Diode | 다이오드 | Standard form |
| Fuse | 퓨즈 | Standard form |
| Gasket | 가스켓 | Standard form |
| Gauge | 게이지 | Never "게이지" (spelling) |
| Hydraulic | 유압 | Pure Korean preferred |
| Insulator | 절연체 | Pure Korean preferred |
| LED | LED | Keep English acronym |
| Motor | 모터 | More common than "전동기" |
| Nozzle | 노즐 | Standard form |
| Piston | 피스톤 | Standard form |
| Pneumatic | 공압 | Pure Korean preferred |
| Pump | 펌프 | Standard form |
| Relay | 릴레이 | Standard form |
| Sensor | 센서 | Standard form |
| Solenoid | 솔레노이드 | Standard form |
| Switch | 스위치 | Standard form |
| Valve | 밸브 | Standard form |

### Troubleshooting Table Columns (문제 해결 표 컬럼)

| Source Label | Korean Translation |
|-------------|-------------------|
| Symptom | 증상 |
| Cause | 원인 |
| Solution / Remedy | 조치 방법 / 해결 방법 |
| Error Code | 에러 코드 / 오류 코드 |
| Possible Reason | 예상 원인 |
| Corrective Action | 시정 조치 |
| Check Item | 확인 사항 |
| Inspection Method | 점검 방법 |
| Criterion / Standard | 기준 |
| Remark | 비고 |

### 표준 약어 목록 (Common Technical Abbreviations)

| Abbreviation | Full English | Korean Translation |
|-------------|--------------|-------------------|
| PLC | Programmable Logic Controller | 프로그래밍 가능 논리 제어기 |
| HMI | Human-Machine Interface | 인간-기계 인터페이스 |
| CNC | Computer Numerical Control | 컴퓨터 수치 제어 |
| PCB | Printed Circuit Board | 인쇄 회로 기판 |
| PID | Proportional-Integral-Derivative | 비례-적분-미분 제어 |
| SCADA | Supervisory Control and Data Acquisition | 감시 제어 및 데이터 수집 |
| ESD | Emergency Shut-Down | 비상 정지 |
| HVAC | Heating, Ventilation, and Air Conditioning | 냉난방 공조 |
| EMC | Electromagnetic Compatibility | 전자기 적합성 |
| EMI | Electromagnetic Interference | 전자기 간섭 |
| NDT | Non-Destructive Testing | 비파괴 검사 |
| FMEA | Failure Mode and Effects Analysis | 고장 모드 및 영향 분석 |
| MTTF | Mean Time To Failure | 평균 고장 시간 |
| MTBF | Mean Time Between Failures | 평균 고장 간격 |
| OEE | Overall Equipment Effectiveness | 전체 설비 효율 |
