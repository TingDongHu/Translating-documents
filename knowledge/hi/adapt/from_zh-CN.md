---
id: hi/adapt/from_zh-CN
type: adapt
target_lang: hi
source_lang: zh-CN
name: Chinese (Simplified) to Hindi Adaptation
description: Target-specific adaptation rules for translating Chinese (Simplified) documents into Hindi
---

## Formality and Address

- **Formal second person**: Chinese 您 → Hindi आप (formal/polite)
  - Source: "请您确认" → Target: "कृपया आप पुष्टि करें"
  - Source: "您" → Target: "आप" / "आपको" / "आपसे" (declined by case)
  - Source: "您好" → Target: "नमस्ते" / "आपको नमस्कार" (formal greeting)
- **Informal second person**: Chinese 你 → Hindi तुम (informal) / आप (formal, context-dependent)
  - Source: "你好" → Target: "नमस्ते" (neutral; not "तू" which is too intimate)
  - Source: "你的" → Target: "तुम्हारा" / "आपका" (depending on register)
  - Note: Hindi तू is reserved for very close relationships, deities, or condescension — never use in business
- **Chinese honorific titles** → Hindi श्री / श्रीमती + name
  - Source: "王总" → Target: "श्री वांग" (श्री + surname, as Hindi does not use "General Manager" as title)
  - Source: "李经理" → Target: "श्री ली, प्रबंधक" or "प्रबंधक ली जी"
  - Source: "张教授" → Target: "प्रोफ़ेसर झांग"
  - Source: "刘老师" → Target: "श्री/सुश्री लियू" (or "गुरु जी" in educational context)
- **Chinese bureaucratic titles** → Hindi functional equivalents
  - Source: "董事长" → Target: "अध्यक्ष (निदेशक मंडल के)" or "चेयरमैन"
  - Source: "总经理" → Target: "महाप्रबंधक" or "जनरल मैनेजर"
  - Source: "处长" → Target: "विभागाध्यक्ष"
  - Source: "局长" → Target: "निदेशक" / "आयुक्त"
- **Collective address**: Chinese 各位 → Hindi प्रिय / आदरणीय + plural
  - Source: "各位同事" → Target: "प्रिय सहकर्मियों"
  - Source: "各位代表" → Target: "आदरणीय प्रतिनिधिगण"
  - Source: "各位来宾" → Target: "आदरणीय अतिथिगण"
- **Chinese self-deprecation**: Hindi does not use self-deprecating forms — translate neutrally
  - Source: "鄙人" → Target: "मैं" (neutral first person)
  - Source: "拙见" → Target: "मेरी राय" (neutral, not "humble opinion")
  - Source: "寒舍" → Target: "मेरा घर" (neutral, not "my humble abode")
- **Chinese honorific prefix "贵"** → Hindi सम्माननीय / आपका (formal marker)
  - Source: "贵公司" → Target: "आपकी कंपनी" (formal)
  - Source: "贵国" → Target: "आपका देश" / "सम्माननीय देश"
- **Chinese "小" (self-deprecating prefix)**: → Hindi neutral form
  - Source: "小店" → Target: "हमारी दुकान" (not "small shop")
  - Source: "小公司" → Target: "हमारी कंपनी"

## Number and Date Conventions

- **Chinese 万 (10,000)** → Hindi 10,000 / 1 लाख (in Indian number system)
  - Source: "五万" → Target: "50,000" or "50 हज़ार"
  - Source: "人口十万" → Target: "जनसंख्या 1,00,000" (Indian comma format)
  - Source: "二十万" → Target: "2,00,000" (2 लाख)
- **Chinese 亿 (100,000,000)** → Hindi 10,00,00,000 (10 करोड़ / crore)
  - Source: "十四亿" → Target: "1,40,00,00,000 (140 करोड़)"
  - Source: "一亿" → Target: "10,00,00,000 (10 करोड़)"
  - Note: 亿 = 100 million = 10 crore in Indian system — CRITICAL to convert correctly
- **Chinese 千 (1,000)** → Hindi 1,000 / 1 हज़ार
  - Source: "三千" → Target: "3,000" or "3 हज़ार"
  - Source: "九千五百" → Target: "9,500" or "9,500"
- **Chinese 百万 (million)** → Hindi 10,00,000 (दस लाख)
  - Source: "五百万" → Target: "50,00,000 (पचास लाख)"
- **Chinese 千万 (ten million)** → Hindi 1,00,00,000 (एक करोड़)
  - Source: "五千万" → Target: "5,00,00,000 (पाँच करोड़)"
- **Chinese decimal point** (.) → Hindi decimal point (.) — same symbol, unlike European languages
  - Source: "3.14" → Target: "3.14"
  - Source: "0.5%" → Target: "0.5%"
- **Chinese thousands separator** (,) → Indian comma format (lakh/crore grouping)
  - Source: "12,345,678" → Target: "1,23,45,678" (Indian grouping: crore-lakh-thousand)
  - Source: "1,000,000" → Target: "10,00,000" (Indian grouping)
  - Source: "100,000" → Target: "1,00,000"
  - Note: Indian system groups the first three digits, then every two digits: 1,23,45,678
- **Chinese date format**: YYYY年M月D日 → Hindi: DD/MM/YYYY or DD माह YYYY
  - Source: "2024年1月15日" → Target: "15/01/2024" or "15 जनवरी 2024"
  - Source: "2023年12月" → Target: "दिसंबर 2023"
  - Source: "2024年" → Target: "वर्ष 2024" or "2024"
- **Chinese week references** → Hindi दिन
  - Source: "本周一" → Target: "इस सोमवार"
  - Source: "上周五" → Target: "पिछले शुक्रवार"
  - Source: "下周" → Target: "अगले सप्ताह"
- **Chinese time format**: 24h → Hindi 24h (matches, same convention)
  - Source: "下午3点" → Target: "15:00" or "दोपहर 3 बजे" (12h also acceptable in informal Hindi)
  - Source: "上午9时30分" → Target: "9:30 पूर्वाह्न" or "09:30"
  - Source: "晚上8点" → Target: "20:00" or "रात 8 बजे"
- **Devanagari digits**: Chinese uses Arabic numerals (0-9) → Hindi can use Devanagari numerals (०-९) or Arabic numerals
  - Source: "2024年1月15日" → Target: "१५/०१/२०२४" (Devanagari digits in traditional Hindi contexts)
  - Source: "50%" → Target: "५०%" (Devanagari in formal Hindi text)
  - Note: For business/technical documents, Arabic numerals (0-9) are preferred in Hindi
- **Chinese financial uppercase numerals** (壹贰叁) → Hindi words (अंक शब्दों में)
  - Source: "壹万元整" → Target: "दस हज़ार रुपये मात्र" (amount in words)
  - Source: "伍佰元" → Target: "पाँच सौ रुपये"
- **Chinese percentages** → Hindi प्रतिशत
  - Source: "50%" → Target: "50%" or "५० प्रतिशत"
  - Source: "同比增长5%" → Target: "वर्ष-दर-वर्ष 5% वृद्धि"

### Indian Numbering System Reference

| Chinese | Value | Indian System | Hindi (words) |
|---------|-------|---------------|---------------|
| 十 | 10 | 10 | दस |
| 百 | 100 | 100 | सौ |
| 千 | 1,000 | 1,000 | हज़ार |
| 万 | 10,000 | 10,000 | दस हज़ार |
| 十万 | 100,000 | 1,00,000 | एक लाख |
| 百万 | 1,000,000 | 10,00,000 | दस लाख |
| 千万 | 10,000,000 | 1,00,00,000 | एक करोड़ |
| 亿 | 100,000,000 | 10,00,00,000 | दस करोड़ |
| 十亿 | 1,000,000,000 | 1,00,00,00,000 | एक अरब |

## Cultural References

- **关系 (guanxi)** → संपर्क / सिफ़ारिश / रिश्ते (context-dependent)
  - Source: "靠关系办事" → Target: "सिफ़ारिश से काम कराना"
  - Source: "关系网" → Target: "संपर्कों का जाल" / "नेटवर्क"
  - Source: "有关系好办事" → Target: "अच्छे संपर्क होने से काम आसान हो जाता है"
  - Note: Avoid transliteration "गुआनक्सी" without explanation; prefer semantic translation
- **面子 (miànzi)** → प्रतिष्ठा / सम्मान / इज़्ज़त
  - Source: "给面子" → Target: "सम्मान देना" / "इज़्ज़त रखना"
  - Source: "丢面子" → Target: "बेइज़्ज़ती होना" / "प्रतिष्ठा खोना"
  - Source: "保全颜面" → Target: "सम्मान बचाना"
  - Note: Hindi इज़्ज़त concept closely parallels Chinese 面子; use it in relevant contexts
- **一带一路 (Belt and Road Initiative)** → बेल्ट एंड रोड पहल / एक पट्टी एक सड़क
  - Source: "一带一路倡议" → Target: "बेल्ट एंड रोड पहल (BRI)"
  - Source: "一带一路项目" → Target: "बीआरआई परियोजनाएँ"
  - Note: Hindi media uses both "एक पट्टी एक सड़क" and "बेल्ट एंड रोड पहल"
- **双碳目标 (Dual Carbon Goals)** → दोहरे कार्बन लक्ष्य
  - Source: "双碳目标" → Target: "दोहरे कार्बन लक्ष्य (कार्बन तटस्थता लक्ष्य)"
  - Source: "碳达峰" → Target: "कार्बन उत्सर्जन शिखर"
  - Source: "碳中和" → Target: "कार्बन तटस्थता"
- **乡村振兴** → ग्रामीण पुनरोद्धार
  - Source: "乡村振兴战略" → Target: "ग्रामीण पुनरोद्धार रणनीति"
- **内卷 (involution)** → अतिरंजित प्रतिस्पर्धा / आंतरिक संघर्ष
  - Source: "教育内卷" → Target: "शिक्षा में अतिरंजित प्रतिस्पर्धा"
  - Source: "内卷化" → Target: "आंतरिक संघर्ष की स्थिति"
- **共同富裕 (Common Prosperity)** → साझा समृद्धि
  - Source: "共同富裕" → Target: "साझा समृद्धि"
- **国企改革** → सार्वजनिक उद्यम सुधार (SOE reform)
  - Source: "国企改革" → Target: "सार्वजनिक क्षेत्र के उद्यमों में सुधार"
- **中国特色的社会主义** → चीनी विशेषताओं वाला समाजवाद
  - Note: Established fixed term in Hindi political discourse
- **Chinese idioms (成语) → Hindi समानार्थक मुहावरे** (idiomatic equivalents)
  - Source: "画蛇添足" → Target: "नमक में मिर्च डालना" (adding extra/unnecessary)
  - Source: "井底之蛙" → Target: "कुएँ का मेंढक" (similar idiom exists in Hindi too!)
  - Source: "对牛弹琴" → Target: "गधे को बांसुरी सुनाना" (preaching to the deaf)
  - Source: "亡羊补牢" → Target: "अब पछताए होत क्या, जब चिड़िया चुग गई खेत" (too late)
  - Source: "塞翁失马" → Target: "हर संकट में अवसर छिपा है" (blessing in disguise)
  - Source: "百闻不如一见" → Target: "सौ सुनने से एक देखना भला" (seeing is believing)
  - Source: "一举两得" → Target: "एक पंथ दो काज" (kill two birds with one stone)
  - Source: "半途而废" → Target: "आधा छोड़ना" / "बीच में ही छोड़ देना" (give up halfway)
  - Source: "心想事成" → Target: "मनोकामना पूर्ण हो" (may your wishes come true)
  - Source: "一帆风顺" → Target: "सफलता प्राप्त हो" / "शुभ यात्रा" (bon voyage / smooth sailing)
- **Chinese holidays and festivals** → keep Chinese name + Hindi explanation
  - Source: "春节" → Target: "चीनी नव वर्ष (बसंत पर्व)"
  - Source: "国庆节" → Target: "चीनी राष्ट्रीय दिवस (1 अक्टूबर)"
  - Source: "中秋节" → Target: "मध्य-शरद पर्व (मून फेस्टिवल)"
  - Source: "端午节" → Target: "ड्रैगन बोट पर्व"
- **Chinese administrative divisions** → Hindi descriptive terms
  - Source: "省" → Target: "प्रांत"
  - Source: "自治区" → Target: "स्वायत्त क्षेत्र"
  - Source: "直辖市" → Target: "केंद्र-शासित नगर" / "सीधे-शासित नगर"
  - Source: "特别行政区" → Target: "विशेष प्रशासनिक क्षेत्र"
  - Source: "市" → Target: "शहर" / "नगर"
  - Source: "县" → Target: "ज़िला"

## Terminology

- **统一社会信用代码** → एकीकृत सामाजिक क्रेडिट कोड (18-अंकीय USCC)
  - Source: "统一社会信用代码" → Target: "एकीकृत सामाजिक क्रेडिट कोड (USCC)"
- **营业执照** → व्यावसायिक लाइसेंस / उद्यम पंजीकरण प्रमाणपत्र
  - Source: "营业执照" → Target: "व्यावसायिक लाइसेंस"
  - Source: "营业执照号" → Target: "व्यावसायिक लाइसेंस संख्या"
- **法定代表人** → वैधानिक प्रतिनिधि (legal representative in Chinese corporate law)
  - Source: "法定代表人" → Target: "वैधानिक प्रतिनिधि" (not to be confused with न्यायिक व्यक्ति / legal entity)
- **注册资本** → पंजीकृत पूंजी (registered capital)
  - Source: "注册资本" → Target: "पंजीकृत पूंजी"
- **CCC认证** → CCC प्रमाणन (चीन अनिवार्य प्रमाणन)
  - Source: "CCC认证" → Target: "CCC प्रमाणन"
- **GB标准** → GB मानक (चीनी राष्ट्रीय मानक)
  - Source: "GB/T 12345-2020" → Target: "GB/T 12345-2020 मानक" (keep GB code, add explanation if needed)
- **增值税专用发票** → विशेष वैट चालान (वैट विशेष चालान)
  - Source: "增值税专用发票" → Target: "विशेष वैट चालान"
  - Source: "普通发票" → Target: "सामान्य चालान"
- **五险一金** → पाँच सामाजिक बीमाएँ और एक आवास निधि
  - Source: "五险一金" → Target: "पाँच सामाजिक बीमाएँ (पेंशन, चिकित्सा, बेरोज़गारी, कार्य चोट, मातृत्व) और आवास निधि"
- **户口 (hùkǒu)** → घरेलू पंजीकरण प्रणाली / हुकोऊ
  - Source: "户口" → Target: "घरेलू पंजीकरण प्रणाली (हुकोऊ)" (keep term with explanation on first use)
- **学区房** → स्कूल ज़ोन में आवासीय संपत्ति
  - Source: "学区房" → Target: "अच्छे स्कूल क्षेत्र में स्थित घर"
- **有关部门** → संबंधित विभाग / सक्षम प्राधिकारी
  - Source: "报有关部门审批" → Target: "संबंधित विभागों की मंज़ूरी हेतु प्रस्तुत करें"
- **国家发展改革委** → राष्ट्रीय विकास एवं सुधार आयोग (NDRC)
- **中国人民银行** → चीनी जनता बैंक (पीपुल्स बैंक ऑफ़ चाइना)
- **国务院** → चीनी राज्य परिषद (स्टेट काउंसिल)
- **电脑 / 计算机** → कंप्यूटर (preferred) / संगणक (formal)
  - Source: "电脑" → Target: "कंप्यूटर" (more common in Hindi)
  - Source: "计算机科学" → Target: "कंप्यूटर विज्ञान" / "संगणक विज्ञान"
- **软件** → सॉफ़्टवेयर (preferred) / संगणक क्रमादेश (rare, very formal)
  - Source: "软件" → Target: "सॉफ़्टवेयर"
  - Note: Sanskritized Hindi terms (संगणक, क्रमादेश) are used in government/formal contexts but कंप्यूटर/सॉफ़्टवेयर are more common in daily use
- **互联网 / 网络** → इंटरनेट / नेटवर्क
  - Source: "互联网" → Target: "इंटरनेट"
  - Source: "局域网" → Target: "स्थानीय क्षेत्र नेटवर्क (LAN)"
- **手机 / 移动电话** → मोबाइल फ़ोन / सेलफ़ोन
  - Source: "手机" → Target: "मोबाइल फ़ोन" (चलभाष is rare)
- **数据库** → डेटाबेस / आँकड़ा-कोष
  - Source: "数据库" → Target: "डेटाबेस"
- **人工智能** → कृत्रिम बुद्धिमत्ता (AI)
  - Source: "人工智能" → Target: "कृत्रिम बुद्धिमत्ता (AI)"
- **大数据** → बड़ा डेटा / विशाल आँकड़े
  - Source: "大数据" → Target: "बड़ा डेटा"
- **云计算** → क्लाउड कम्प्यूटिंग / मेघ संगणना
  - Source: "云计算" → Target: "क्लाउड कम्प्यूटिंग"
- **机器学习** → मशीन लर्निंग / यंत्र अधिगम
  - Source: "机器学习" → Target: "मशीन लर्निंग"
- **False friends / potential confusion**: No direct false friends between Chinese and Hindi, but be aware of context
  - Chinese 银行 (yínháng, bank) → Not to be confused with Hindi which uses बैंक
  - Chinese 公司 (gōngsī, company) → Hindi कंपनी
  - Chinese 合同 (hétóng, contract) → Hindi अनुबंध / कॉन्ट्रैक्ट
  - Note: False friends are less of an issue between CN→HI; focus instead on ensuring terminology is natural in Hindi

## Administrative/Legal Style

- **特此通知** → इसके द्वारा सूचित किया जाता है
  - Source: "特此通知" → Target: "इसके द्वारा सूचित किया जाता है"
  - Source: "特此通知如下" → Target: "इसके द्वारा निम्नानुसार सूचित किया जाता है"
- **经研究决定** → विचारोपरांत निर्णय लिया गया
  - Source: "经研究决定" → Target: "विचारोपरांत निर्णय लिया गया"
  - Source: "经研究，现决定如下" → Target: "समीक्षा के बाद निम्नानुसार निर्णय लिया गया:"
- **望周知** → सामान्य जानकारी हेतु सूचित किया जाता है
  - Source: "望周知" → Target: "सामान्य जानकारी हेतु सूचित किया जाता है"
- **遵照执行** → अनुपालन और कार्यान्वयन करें
  - Source: "请遵照执行" → Target: "कृपया अनुपालन करें"
  - Source: "以上规定，请遵照执行" → Target: "कृपया उपरोक्त नियमों का अनुपालन करें"
- **根据...规定** → के अनुसार / के आधार पर / के तहत
  - Source: "根据《中华人民共和国合同法》规定" → Target: "चीनी जनवादी गणराज्य के अनुबंध कानून के अनुसार"
  - Source: "根据有关规定" → Target: "संबंधित नियमों के अनुसार"
  - Source: "根据以上情况" → Target: "उपरोक्त स्थिति के आधार पर"
  - Note: Hindi uses के अनुसार (according to) and के आधार पर (based on) where Chinese uses 根据
- **按照** → के अनुसार / के अनुसार
  - Source: "按照合同约定" → Target: "अनुबंध की शर्तों के अनुसार"
- **通过** → के द्वारा / के माध्यम से
  - Source: "通过双方协商" → Target: "दोनों पक्षों की आपसी सहमति से"
  - Source: "通过法律途径" → Target: "कानूनी माध्यमों से"
- **为了** → के लिए / हेतु / के उद्देश्य से
  - Source: "为了进一步合作" → Target: "आगे के सहयोग हेतु"
- **特此** → इसके द्वारा / इससे
  - Source: "特此证明" → Target: "इसके द्वारा प्रमाणित किया जाता है"
  - Source: "特此声明" → Target: "इसके द्वारा घोषित किया जाता है"
- **兹有** → इसके द्वारा प्रस्तुत है कि
  - Source: "兹有我公司..." → Target: "इसके द्वारा हमारी कंपनी..."
- **鉴于** → को ध्यान में रखते हुए / के मद्देनज़र
  - Source: "鉴于上述情况" → Target: "उपरोक्त स्थिति को ध्यान में रखते हुए"
  - Source: "鉴于甲方..." → Target: "यह ध्यान में रखते हुए कि पक्ष क..."
- **经...批准** → की मंज़ूरी से / के अनुमोदन से
  - Source: "经主管部门批准" → Target: "सक्षम प्राधिकारी की मंज़ूरी से"
- **依法** → कानून के अनुसार / विधि सम्मत
  - Source: "依法追究责任" → Target: "कानून के अनुसार उत्तरदायित्व निर्धारित करना"
- **自...之日起** → से प्रभावी / से लागू
  - Source: "自本合同签订之日起" → Target: "इस अनुबंध पर हस्ताक्षर की तिथि से प्रभावी"
  - Source: "自发布之日起施行" → Target: "प्रकाशन की तिथि से लागू होगा"
- **本办法** → ये नियम / यह विनियम
  - Source: "本办法自2024年1月1日起施行" → Target: "ये नियम 1 जनवरी 2024 से लागू होंगे"
- **Chinese law citation format** → Hindi legal citation
  - Source: "依照《中华人民共和国合同法》第一百二十条" → Target: "चीनी अनुबंध कानून की धारा 120 के अनुसार"
  - Note: Hindi citations follow format: कानून का नाम + धारा/अनुच्छेद संख्या
- **Official closing formulas** → Hindi equivalents
  - Source: "此致 敬礼" → Target: "सादर / भवदीय" (standard closing for letters)
  - Source: "特此报告" → Target: "प्रतिवेदन प्रस्तुत है"
  - Source: "请批示" → Target: "कृपया अनुमोदन प्रदान करें"
  - Source: "谢谢合作" → Target: "सहयोग के लिए धन्यवाद"
- **Chinese conditional clauses** → Hindi यदि / अगर
  - Source: "如发生争议" → Target: "यदि विवाद उत्पन्न होता है"
  - Source: "如有违反" → Target: "उल्लंघन की स्थिति में"
- **Chinese "应" (obligation)** → Hindi обязан / चाहिए / आवश्यक है
  - Source: "双方应..." → Target: "दोनों पक्षों को चाहिए..."
  - Source: "应遵守" → Target: "का पालन करना आवश्यक है"

## Punctuation Conversion

- **Chinese period 。 → Hindi purnaviram ।** (पूर्णविराम / खड़ी पाई)
  - Source: "请确认।谢谢。" → Target: "कृपया पुष्टि करें। धन्यवाद।"
  - Source: "您好।欢迎。" → Target: "नमस्ते। आपका स्वागत है।"
  - Note: Hindi uses the vertical line । (purnaviram) as full stop, NOT the Latin period . in formal Hindi text
  - Exception: For mixed English-Hindi text, the Latin period may be used for consistency
- **Chinese comma ， → Hindi comma ,**
  - Source: "第一，第二，第三" → Target: "पहले, दूसरे, तीसरे"
  - Source: "首先，其次" → Target: "पहला, दूसरा"
  - Note: Chinese uses full-width ，while Hindi uses half-width , — always convert to half-width
- **Chinese enumeration comma 、 → Hindi comma ,**
  - Source: "苹果、香蕉、橘子" → Target: "सेब, केले, संतरे"
  - Source: "北京、上海、广州" → Target: "बीजिंग, शंघाई, गुआंगझोऊ"
  - Note: Hindi has no equivalent of Chinese 顿号; all enumerations use regular commas
- **Chinese book title marks 《》 → Hindi double quotation marks ""**
  - Source: "《中华人民共和国宪法》" → Target: "'चीनी संविधान'" or "चीनी संविधान"
  - Source: "《合同法》" → Target: "'अनुबंध कानून'"
  - Source: "《红楼梦》" → Target: "'रेड मेंशन का सपना'"
  - Note: Hindi uses "" (उद्धरण चिह्न) for book titles, not angle brackets
- **Chinese quotation marks "" → Hindi ""** (same symbol but with spacing rules)
  - Source: "所谓「关系」" → Target: "तथाकथित 'संपर्क'"
  - Source: "他说："你好"" → Target: "उसने कहा, 'नमस्ते'"
  - Note: Hindi uses single quotes '' for inner quotes within double quotes ""
- **Chinese colon ： → Hindi colon :** (same function; full-width → half-width)
  - Source: "如下：" → Target: "निम्नानुसार:"
- **Chinese semicolon ； → Hindi semicolon ;** (full-width → half-width)
- **Chinese ellipsis …… (6 dots) → Hindi ... (3 dots)** — both are used, but Hindi prefers 3 dots
  - Source: "等等……" → Target: "इत्यादि..."
- **Chinese dash —— (em dash doubled) → Hindi — (single em dash)**
  - Source: "这就是——" → Target: "यानी —"
  - Note: Hindi uses a single em dash, not doubled
- **Chinese question mark ？→ Hindi ?** (full-width → half-width)
  - Source: "好吗？" → Target: "क्या आप ठीक हैं?"
  - Note: Hindi uses ? at the end, unlike Hindi's older convention of using ।। (double danda) for questions
- **Chinese exclamation mark ！→ Hindi !** (full-width → half-width)
  - Source: "太好了！" → Target: "बहुत अच्छा!"
- **Chinese parentheses （）→ Hindi half-width parentheses ()**
  - Source: "（以下简称甲方）" → Target: "(इसके बाद 'पक्ष क' कहा जाएगा)"
- **Chinese spacing**: Chinese has no spaces between characters → Hindi adds natural word spacing
  - Hindi text has spaces between words (unlike Chinese), so word boundaries must be created
  - Example: Chinese "请您确认参会" → Hindi "कृपया अपनी उपस्थिति की पुष्टि करें" (spaces between words)
- **Hindi पूर्णविराम usage rules**:
  - Hindi full stop । is used at the end of sentences (not paragraph marks)
  - In poetry and religious texts, double danda (॥) marks the end of a verse or section
  - In mixed Hindi-English text, the Latin period . may substitute for ।
  - Consistency is key: choose either । or . and use it throughout the document
- **Hindi comma usage**: Hindi uses comma (,) similarly to English — for enumerations and clause separation
  - Hindi comma is half-width, same as English
  - No Hindi equivalent of the Chinese enumeration comma (、)
  - Hindi does NOT use commas before conjunctions like और (and) in lists consistently
- **Hindi quotation marks convention**:
  - First level: " " (double quotes)
  - Second level: ' ' (single quotes, inside double quotes)
  - Hindi sometimes uses 「」 in traditional typography, but " " is standard in modern Hindi
  - Book titles can be in " " or without any quotation marks in plain text
- **Hindi ऽ (avagraha)** — used occasionally in Sanskritized Hindi to mark elision
  - Source: Chinese none → Hindi may add ऽ in formal/legal text for word fusion (e.g., भोऽन्य for भोः + अन्य)
  - Note: Rare in modern business Hindi; mainly in formal Sanskritic contexts
- **Hindi numeral punctuation**: Indian comma grouping uses commas differently
  - Source: "12,345" → Target: "12,345" (same, but grouping may be Indian: 12,345)
  - Source: "12345678" → Target: "1,23,45,678" (Indian grouping: thousand, lakh, crore)
- **Hindi decimal**: Uses period (.) same as English and Chinese, not comma as in European languages
  - Source: "3.14" → Target: "3.14" (no change needed for decimal symbol)
  - This is a key difference from European languages — Hindi uses the same decimal convention as Chinese and English

### Key Punctuation Differences Summary

| Chinese | Hindi (Devanagari) | Notes |
|---------|-------------------|-------|
| 。 (period) | । (purnaviram) | Vertical line full stop |
| ， (comma) | , (half-width) | Same function, different width |
| 、 (enumeration) | , (comma) | No enumeration comma in Hindi |
| 《》 (book marks) | " " (quotes) | No angle brackets in Hindi |
| "" (quotes) | " " / ' ' | Standard quotation marks |
| —— (dash) | — (single) | Single em dash |
| …… (6 dots) | ... (3 dots) | Standard ellipsis |
| full-width symbols | half-width | All punctuation to half-width |
| no spaces | word spaces | Hindi has inter-word spacing |
