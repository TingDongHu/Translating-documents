---
id: hi/adapt/from_en
type: adapt
target_lang: hi
source_lang: en
name: English to Hindi Adaptation
description: Target-specific adaptation rules for translating English documents into Hindi
---

## Formality and Address

- **English "you" → Hindi आप / तुम / तू distinction**
  - Source: "You are required to..." → Target: "आपको यह करना आवश्यक है..." (formal आप)
  - Source: "You may proceed" → Target: "आप आगे बढ़ सकते हैं" (formal register for business/tech)
  - Source: "You (singular, intimate)" → Target: "तू" (only for very close relationships, divine reference)
  - Source: "You all" → Target: "आप सब" / "आप लोग" (formal plural)
  - Context: Business, official, and technical documents always use आप — never तुम or तू
- **English "your" → Hindi आपका / तुम्हारा / तेरा**
  - Source: "Your application" → Target: "आपका आवेदन" (formal)
  - Source: "Your order" → Target: "आपका ऑर्डर"
  - Source: "Your sincerely" → Target: "आपका भवदीय" (letter closing)
- **English "Dear Sir / Dear Madam" → Hindi प्रिय महोदय / आदरणीय महोदया**
  - Source: "Dear Sir" → Target: "प्रिय महोदय" or "आदरणीय महोदय"
  - Source: "Dear Madam" → Target: "प्रिय महोदया" or "आदरणीय महोदया"
  - Source: "Dear Sir or Madam" → Target: "प्रिय महोदय / महोदया"
  - Note: Hindi formal letters use प्रिय (dear) or आदरणीय (respected) — आदरणीय is more formal
- **English "Dear Mr. / Ms." → Hindi प्रिय / आदरणीय श्री / श्रीमती**
  - Source: "Dear Mr. Sharma" → Target: "प्रिय श्री शर्मा" or "आदरणीय श्री शर्मा जी"
  - Source: "Dear Ms. Patel" → Target: "प्रिय सुश्री पटेल"
  - Note: Hindi adds "जी" as an honorific suffix (optional in formal letters)
- **English "To whom it may concern" → Hindi equivalent**
  - Source: "To whom it may concern" → Target: "जिनको यह सरोकार हो" / "संबंधित व्यक्ति के लिए"
- **English title "Mr." → Hindi श्री**
  - Source: "Mr. Sharma" → Target: "श्री शर्मा" (never "मिस्टर शर्मा" in formal Hindi)
  - Source: "Mr. John Smith" → Target: "श्री जॉन स्मिथ"
- **English title "Mrs." → Hindi श्रीमती**
  - Source: "Mrs. Sharma" → Target: "श्रीमती शर्मा"
- **English title "Ms." → Hindi सुश्री** (or श्रीमती if marital status known)
  - Source: "Ms. Patel" → Target: "सुश्री पटेल"
- **English "Dr." → Hindi डॉ.** (same, used as prefix)
  - Source: "Dr. Singh" → Target: "डॉ. सिंह" or "डॉक्टर सिंह"
- **English "Professor" → Hindi प्रोफ़ेसर** (or प्राध्यापक in formal contexts)
  - Source: "Professor Sharma" → Target: "प्रोफ़ेसर शर्मा" / "प्राध्यापक शर्मा"
- **English imperative mood → Hindi आप-imperative (formal)**
  - Source: "Click here" → Target: "यहाँ क्लिक करें" (formal imperative, plural)
  - Source: "Enter your password" → Target: "अपना पासवर्ड दर्ज करें"
  - Source: "Please wait" → Target: "कृपया प्रतीक्षा करें"
  - Note: Hindi technical docs use आप-form (formal) by default
- **English "please" → Hindi कृपया**
  - Source: "Please find attached..." → Target: "कृपया संलग्न देखें..." / "संलग्न है..."
  - Source: "Please confirm receipt" → Target: "कृपया प्राप्ति की पुष्टि करें"
  - Note: कृपया is more frequent in formal Hindi than "please" in formal English
- **English "we" → Hindi हम (inclusive)**
  - Source: "We are pleased to inform you" → Target: "हमें आपको सूचित करते हुए प्रसन्नता है"
  - Source: "We hereby confirm" → Target: "हम इसके द्वारा पुष्टि करते हैं"
- **English gender-neutral language → Hindi (Hindi is gender-marked by default)**
  - Source: "The applicant must submit his/her form" → Target: "आवेदक को अपना फ़ॉर्म जमा करना होगा" (Hindi uses neutral participle or marks both)
  - Source: "Each employee should check his email" → Target: "प्रत्येक कर्मचारी को अपना ईमेल जाँचना चाहिए" (Hindi possessive अपना is gender-neutral)
  - Note: Hindi verb gender follows the subject's natural gender; use masculine as default for generic references

## Number and Date Conventions

- **English decimal point (.) → Hindi decimal point (.)** — same, NO change needed
  - Source: "3.14" → Target: "3.14" (Hindi uses the same decimal convention as English)
  - Important: Unlike European languages that use comma as decimal, Hindi uses period — so no conversion
- **English thousands separator (,) → Indian comma format (lakh/crore grouping)**
  - Source: "12,345,678" → Target: "1,23,45,678" (Indian grouping)
  - Source: "1,000,000" → Target: "10,00,000"
  - Source: "100,000" → Target: "1,00,000"
  - Source: "50,000" → Target: "50,000" (first three digits then two)
  - Note: Indian system groups the first three digits from right, then every two digits
- **English "billion" (1,000,000,000) → Hindi अरब**
  - Source: "$5 billion" → Target: "5 अरब डॉलर" or "US$5 अरब"
  - Note: Hindi system: 1,00,00,00,000 = 1 अरब (same as English billion, different grouping)
- **English "million" (1,000,000) → Hindi लाख (10,00,000)**
  - Source: "$5 million" → Target: "50 लाख डॉलर" or "US$50,00,000"
  - Source: "2.5 million" → Target: "25 लाख" (25,00,000)
- **English "trillion" (10¹²) → Hindi खरब**
  - Source: "$2 trillion" → Target: "2 खरब डॉलर" (1 खरब = 1,00,00,00,00,000)
- **English "lakh/crore" → Hindi लाख/करोड़** (these terms are already Hindi, use with Indian numerals)
  - Source: "5 lakh" → Target: "5 लाख" or "5,00,000"
  - Source: "10 crore" → Target: "10 करोड़" or "10,00,00,000"
- **English date format: Month DD, YYYY or MM/DD/YYYY → Hindi: DD/MM/YYYY**
  - Source: "January 15, 2024" → Target: "15 जनवरी 2024" (in text) or "15/01/2024" (numeric)
  - Source: "12/31/2023" → Target: "31/12/2023" (**CRITICAL**: swap month and day!)
  - Source: "2023-12-31" → Target: "31/12/2023" (ISO can be kept in technical contexts)
  - This is the most common numeric error — ZERO TOLERANCE
- **English 12h time (AM/PM) → Hindi 12h or 24h (both accepted)**
  - Source: "3:00 PM" → Target: "3:00 अपराह्न" or "15:00" (24h in formal/technical contexts)
  - Source: "12:00 AM" → Target: "12:00 पूर्वाह्न" (midnight) or "0:00"
  - Source: "12:00 PM" → Target: "12:00 मध्याह्न" (noon) or "12:00"
  - Source: "9:30 AM" → Target: "9:30 पूर्वाह्न" or "09:30"
  - Note: Hindi uses पूर्वाह्न (AM) and अपराह्न (PM); 24h format is preferred in government/railway contexts
- **English week format** → Hindi सप्ताह / हफ़्ता
  - Source: "week of March 5" → Target: "5 मार्च से शुरू सप्ताह"
  - Source: "Monday through Friday" → Target: "सोमवार से शुक्रवार तक"
- **Hindi days of the week** (for reference):
  - Monday → सोमवार, Tuesday → मंगलवार, Wednesday → बुधवार
  - Thursday → गुरुवार, Friday → शुक्रवार, Saturday → शनिवार
  - Sunday → रविवार
- **English months** → Hindi month names
  - January → जनवरी, February → फ़रवरी, March → मार्च, April → अप्रैल
  - May → मई, June → जून, July → जुलाई, August → अगस्त
  - September → सितंबर, October → अक्टूबर, November → नवंबर, December → दिसंबर
- **English century format** → Hindi सदी / शताब्दी
  - Source: "21st century" → Target: "21वीं सदी" or "इक्कीसवीं सदी"
  - Source: "early 20th century" → Target: "20वीं सदी की शुरुआत"
- **English decades** → Hindi दशक
  - Source: "the 1990s" → Target: "1990 का दशक" or "नब्बे का दशक"
- **English "midnight" / "noon"** → Hindi "मध्यरात्रि" / "दोपहर"
  - Source: "The report is due by midnight" → Target: "रिपोर्ट मध्यरात्रि तक जमा करनी है"
- **English fiscal year notation** → Hindi वित्तीय वर्ष
  - Source: "FY 2023-2024" → Target: "वित्तीय वर्ष 2023-24"
  - Note: India's fiscal year is April 1 to March 31
- **English "INR" vs numeric formats** → Hindi रुपया / ₹
  - Source: "INR 500" → Target: "500 रुपये" or "₹500"
  - Source: "USD 100" → Target: "100 अमेरिकी डॉलर" or "US$100"
  - Note: Hindi text typically places the currency symbol before the number: ₹500

### Indian Numbering System (English → Hindi)

| English | Value | Indian System | Hindi (words) |
|---------|-------|---------------|---------------|
| Ten | 10 | 10 | दस |
| Hundred | 100 | 100 | सौ |
| Thousand | 1,000 | 1,000 | हज़ार |
| Ten thousand | 10,000 | 10,000 | दस हज़ार |
| Lakh | 100,000 | 1,00,000 | एक लाख |
| Million | 1,000,000 | 10,00,000 | दस लाख |
| Ten million | 10,000,000 | 1,00,00,000 | एक करोड़ |
| Hundred million | 100,000,000 | 10,00,00,000 | दस करोड़ |
| Billion | 1,000,000,000 | 1,00,00,00,000 | एक अरब |
| Trillion | 1,000,000,000,000 | 1,00,00,00,00,000 | एक खरब |

## Cultural References

- **English idiomatic expressions → Hindi मुहावरे (idiomatic equivalents)**
  - Source: "It's raining cats and dogs" → Target: "मूसलाधार बारिश हो रही है" (idiomatic, not literal)
  - Source: "The ball is in your court" → Target: "अब आपकी बारी है"
  - Source: "To cut a long story short" → Target: "लंबी कहानी को संक्षेप में"
  - Source: "Break the ice" → Target: "बातचीत की शुरुआत करना" / "माहौल को सहज बनाना"
  - Source: "When in Rome, do as the Romans do" → Target: "जैसा देश वैसा भेष" (equivalent Hindi proverb)
  - Source: "Every cloud has a silver lining" → Target: "हर अंधेरे का उजाला होता है"
  - Source: "Burning the midnight oil" → Target: "रात-रात भर जागना" / "देर रात तक काम करना"
  - Source: "The early bird catches the worm" → Target: "सवेरे का सूरज ढलता नहीं" / "जल्दी उठने वाले को सफलता मिलती है"
  - Source: "Don't count your chickens before they hatch" → Target: "अंडे फूटने से पहले मुर्गी की टाँके मत गिनो"
  - Source: "A piece of cake" → Target: "बहुत आसान" / "नारियल फोड़ना" (very easy)
  - Source: "Once in a blue moon" → Target: "कभी-कभार" / "कभी कभी"
  - Source: "Better late than never" → Target: "देर से ही सही, मगर आना तो चाहिए"
  - Source: "Actions speak louder than words" → Target: "बोलने से करना बड़ा है" / "कर दिखाना बड़ी बात है"
  - Source: "Kill two birds with one stone" → Target: "एक पंथ दो काज"
  - Source: "The pen is mightier than the sword" → Target: "कलम तलवार से अधिक शक्तिशाली है"
  - Source: "Let sleeping dogs lie" → Target: "सोते को जगाना ठीक नहीं"
- **English common law concepts → Hindi descriptive translation**
  - Source: "common law" → Target: "सामान्य विधि" / "प्रीसेडेंट-आधारित विधि" (with explanation if needed)
  - Source: "equity" (legal) → Target: "न्यायसंगत अधिकार"
  - Source: "trust" (legal) → Target: "ट्रस्ट" / "न्यास"
  - Note: Indian legal system is common-law based, so many English terms have established Hindi equivalents
- **English corporate concepts → Hindi equivalents**
  - Source: "Limited Liability Company (LLC/ Pvt. Ltd.)" → Target: "प्राइवेट लिमिटेड कंपनी"
  - Source: "Corporation (Inc.)" → Target: "निगम" / "कॉरपोरेशन"
  - Source: "Public Limited Company (PLC)" → Target: "सार्वजनिक लिमिटेड कंपनी"
  - Source: "Board of Directors" → Target: "निदेशक मंडल"
  - Source: "CEO" → Target: "मुख्य कार्यकारी अधिकारी (CEO)"
  - Source: "CFO" → Target: "मुख्य वित्तीय अधिकारी (CFO)"
  - Source: "Shareholder" → Target: "शेयरधारक" / "अंशधारक"
  - Source: "Dividend" → Target: "लाभांश"
- **English academic concepts → Hindi adaptation**
  - Source: "Bachelor's degree" → Target: "स्नातक डिग्री" / "बैचलर डिग्री"
  - Source: "Master's degree" → Target: "परास्नातक डिग्री" / "मास्टर डिग्री"
  - Source: "PhD" → Target: "पीएचडी" / "डॉक्टरेट"
  - Source: "GPA" → Target: "ग्रेड पॉइंट एवरेज (GPA)" (keep acronym; explain if needed)
  - Source: "University" → Target: "विश्वविद्यालय"
  - Source: "College" → Target: "महाविद्यालय"
- **English measurement system (imperial) → Indian metric system**
  - Source: "5 miles" → Target: "8 किमी" (convert to metric)
  - Source: "10 feet" → Target: "3 मीटर" or "3.05 मीटर"
  - Source: "1 gallon" → Target: "3.78 लीटर"
  - Source: "32°F" → Target: "0°C"
  - Source: "1 pound" → Target: "0.45 किग्रा"
  - Note: India uses metric system; imperial should always be converted
- **English culturally specific terms → keep with Hindi explanation**
  - Source: "Thanksgiving" → Target: "थैंक्सगिविंग (अमेरिकी धन्यवाद पर्व)" (keep with explanation)
  - Source: "Halloween" → Target: "हैलोवीन"
  - Source: "Social Security Number (SSN)" → Target: "सामाजिक सुरक्षा नंबर (SSN)" (explain if needed)
  - Source: "IRS" → Target: "अमेरिकी आंतरिक राजस्व सेवा (IRS)"
- **English names of international organizations → official Hindi names (or keep English)**
  - Source: "United Nations" → Target: "संयुक्त राष्ट्र (UN)"
  - Source: "World Health Organization" → Target: "विश्व स्वास्थ्य संगठन (WHO)"
  - Source: "International Monetary Fund" → Target: "अंतर्राष्ट्रीय मुद्रा कोष (IMF)"
  - Source: "World Bank" → Target: "विश्व बैंक"
  - Source: "NATO" → Target: "नाटो (NATO)"
  - Source: "World Trade Organization" → Target: "विश्व व्यापार संगठन (WTO)"
  - Note: Hindi-English bilingual naming is common; both can appear together
- **English holidays → Hindi or transliterated names**
  - Source: "Christmas" → Target: "क्रिसमस" / "बड़ा दिन"
  - Source: "Easter" → Target: "ईस्टर"
  - Source: "Diwali" → Target: "दिवाली" (already Hindi)
  - Source: "New Year" → Target: "नव वर्ष"
- **English proverb style → Hindi कहावत style**
  - Source: "Where there's a will, there's a way" → Target: "जहाँ चाह वहाँ राह"
  - Source: "All that glitters is not gold" → Target: "चमकती चीज़ हमेशा सोना नहीं होती"
  - Source: "Rome wasn't built in a day" → Target: "राम राम भरोसे, रावण मरे पछताए" / "कोई काम एक दिन में नहीं बनता"
  - Source: "Practice makes perfect" → Target: "अभ्यास से निपुणता आती है"
- **English "God" / religious references**: In Hindi, contextually adapt for Indian religions
  - Source: "Thank God" → Target: "भगवान का शुक्र है" / "ईश्वर का धन्यवाद"
  - Source: "Oh my God!" → Target: "हे भगवान!" / "हे राम!"
  - Note: Use भगवान (generic) or specific names depending on context

## Terminology

- **English IT terminology → Hindi IT terminology**
  - Source: "computer" → Target: "कंप्यूटर" (common) / "संगणक" (formal, government use)
  - Source: "software" → Target: "सॉफ़्टवेयर" (common) / "क्रमादेश" (rare, very formal)
  - Source: "hardware" → Target: "हार्डवेयर" (common) / "यंत्रोपकरण" (very formal)
  - Source: "internet" → Target: "इंटरनेट"
  - Source: "website" → Target: "वेबसाइट" / "जालपृष्ठ" (formal)
  - Source: "email" → Target: "ईमेल" / "डाक" (in postal context: "ई-पत्र")
  - Source: "database" → Target: "डेटाबेस" / "आँकड़ा-कोष" (formal)
  - Source: "network" → Target: "नेटवर्क" / "संजाल"
  - Source: "server" → Target: "सर्वर"
  - Source: "password" → Target: "पासवर्ड" / "कूटशब्द" (formal)
  - Source: "username" → Target: "उपयोगकर्ता नाम" / "यूज़रनेम"
  - Source: "login" → Target: "लॉगिन" / "प्रवेश"
  - Source: "cloud computing" → Target: "क्लाउड कम्प्यूटिंग" / "मेघ संगणना"
  - Source: "machine learning" → Target: "मशीन लर्निंग" / "यंत्र अधिगम"
  - Source: "artificial intelligence" → Target: "कृत्रिम बुद्धिमत्ता (AI)"
  - Source: "big data" → Target: "बड़ा डेटा"
  - Source: "blockchain" → Target: "ब्लॉकचेन"
  - Source: "cybersecurity" → Target: "साइबर सुरक्षा"
  - Note: In modern Hindi, English loanwords (कंप्यूटर, सॉफ़्टवेयर) are far more common than Sanskritized alternatives (संगणक, क्रमादेश). Use the common form unless translating for a government/public-sector audience.
- **English technical terms → Hindi technical terms**
  - Source: "torque" → Target: "बलाघूर्ण" / "टॉर्क"
  - Source: "stress" → Target: "प्रतिबल" / "स्ट्रेस" (mechanical)
  - Source: "voltage" → Target: "वोल्टेज" / "विभवांतर"
  - Source: "current" → Target: "धारा" / "करंट" (electrical)
  - Source: "frequency" → Target: "आवृत्ति" / "फ़्रीक्वेंसी"
  - Source: "temperature" → Target: "तापमान"
  - Source: "pressure" → Target: "दबाव" / "दाब"
- **English legal terminology → Hindi equivalents**
  - Source: "force majeure" → Target: "अप्रत्याशित घटना" / "फ़ोर्स मेज़र"
  - Source: "indemnification" → Target: "क्षतिपूर्ति"
  - Source: "warranty" → Target: "वारंटी" / "गारंटी"
  - Source: "breach of contract" → Target: "अनुबंध का उल्लंघन"
  - Source: "liquidated damages" → Target: "निर्धारित हर्जाना" (not "तरल क्षति")
  - Source: "intellectual property" → Target: "बौद्धिक संपदा / संपत्ति"
  - Source: "confidentiality" → Target: "गोपनीयता"
  - Source: "non-disclosure agreement (NDA)" → Target: "गोपनीयता समझौता (NDA)"
  - Source: "arbitration" → Target: "मध्यस्थता" / "आर्बिट्रेशन"
  - Source: "jurisdiction" → Target: "अधिकारिता" / "क्षेत्राधिकार"
  - Source: "plaintiff" → Target: "वादी"
  - Source: "defendant" → Target: "प्रतिवादी"
  - Source: "affidavit" → Target: "शपथपत्र"
  - Source: "notary" → Target: "नोटरी" / "नोटरी पब्लिक"
  - Note: Indian legal system is English common-law based; many terms have well-established Hindi equivalents
- **English financial terminology → Hindi equivalents**
  - Source: "revenue" → Target: "राजस्व" / "आय"
  - Source: "profit" → Target: "लाभ"
  - Source: "net income" → Target: "शुद्ध लाभ"
  - Source: "EBITDA" → Target: "EBITDA" (keep acronym; explain if needed)
  - Source: "accounts receivable" → Target: "प्राप्य खाते"
  - Source: "accounts payable" → Target: "देय खाते"
  - Source: "goodwill" → Target: "ख्याति" / "गुडविल"
  - Source: "asset" → Target: "संपत्ति" / "परिसंपत्ति"
  - Source: "liability" → Target: "दायित्व"
  - Source: "equity" → Target: "इक्विटी" / "स्वामित्व हिस्सा"
  - Source: "depreciation" → Target: "ह्रास" / "मूल्यह्रास"
  - Source: "audit" → Target: "लेखापरीक्षा" / "ऑडिट"
  - Source: "balance sheet" → Target: "तुलन पत्र" / "बैलेंस शीट"
- **English administrative terminology → Hindi equivalents**
  - Source: "stakeholder" → Target: "हितधारक" / "हितबद्ध पक्ष"
  - Source: "policy" → Target: "नीति"
  - Source: "regulation" → Target: "नियमन" / "विनियम"
  - Source: "guideline" → Target: "दिशानिर्देश"
  - Source: "compliance" → Target: "अनुपालन"
  - Source: "implementation" → Target: "कार्यान्वयन"
  - Source: "procedure" → Target: "प्रक्रिया"
  - Source: "protocol" → Target: "प्रोटोकॉल" / "कार्यविधि"
  - Source: "memorandum" → Target: "ज्ञापन" / "मेमो"
  - Source: "agenda" → Target: "कार्यसूची" / "एजेंडा"
  - Source: "minutes (of meeting)" → Target: "कार्यवृत्त" / "मिनट्स"
  - Source: "notification" → Target: "अधिसूचना" / "सूचना"
  - Source: "certificate" → Target: "प्रमाणपत्र"
- **English medical terminology → Hindi equivalents**
  - Source: "diagnosis" → Target: "निदान"
  - Source: "symptom" → Target: "लक्षण"
  - Source: "treatment" → Target: "उपचार" / "चिकित्सा"
  - Source: "surgery" → Target: "शल्यक्रिया" / "सर्जरी"
  - Source: "prescription" → Target: "नुस्ख़ा" / "प्रिस्क्रिप्शन"
- **English SI unit names → Hindi (same symbols)**
  - Source: "100 km/h" → Target: "100 किमी/घंटा" (किमी प्रति घंटा)
  - Source: "50 MPa" → Target: "50 एमपीए"
  - Source: "10 kWh" → Target: "10 किलोवाट-घंटा"
  - Source: "5 kg" → Target: "5 किग्रा" or "5 किलो"
  - Source: "2 m" → Target: "2 मीटर"
  - Note: Hindi uses the same SI symbols, but full-unit names are in Hindi
- **False friends caution**: English words that sound like Hindi but mean different things
  - English "none" → NOT Hindi "नोन" (salt); translate as "कोई नहीं"
  - English "boot" (computer) → NOT Hindi "बूट" (shoe); translate as "बूट करना"
  - English "meter" → NOT Hindi "मीटर" (metric unit is same, but "मीटर" also means "meter" as measuring device — check context)
  - English "bank" → Hindi "बैंक" (financial institution) is the same; but "नदी तट" for river bank
  - Note: False friends between English and Hindi are minimal; focus on natural Hindi phrasing

## Administrative/Legal Style

- **English "shall" in legal/technical texts → Hindi आवश्यक है / अनिवार्य है / obligatory present**
  - Source: "The Contractor shall deliver..." → Target: "ठेकेदार को वितरित करना आवश्यक है..." (not future tense)
  - Source: "The Employer shall pay..." → Target: "नियोक्ता भुगतान करेगा" (obligation in Hindi often uses करेगा as formal obligation)
  - Source: "No modification shall be made without..." → Target: "बिना... कोई संशोधन नहीं किया जा सकता"
  - Source: "The parties shall comply with..." → Target: "पक्षकारों को अनुपालन करना अनिवार्य है"
  - Note: Hindi expresses obligation through करना होगा, करना चाहिए, or करेगा (future used as obligation in legal Hindi)
- **English "must" → Hindi अनिवार्य है / आवश्यक है**
  - Source: "You must register" → Target: "पंजीकरण करना अनिवार्य है"
  - Source: "All documents must be signed" → Target: "सभी दस्तावेज़ों पर हस्ताक्षर होना आवश्यक है"
- **English "should" → Hindi चाहिए / उचित है**
  - Source: "You should review the terms" → Target: "आपको शर्तों की समीक्षा करनी चाहिए"
  - Source: "The report should include..." → Target: "रिपोर्ट में शामिल होना चाहिए..."
- **English "may" (permission) → Hindi सकते हैं / की अनुमति है**
  - Source: "You may proceed" → Target: "आप आगे बढ़ सकते हैं"
  - Source: "The parties may agree" → Target: "पक्षकार सहमत हो सकते हैं"
- **English "hereby/hereinafter/hereunder" → Hindi formal connectors**
  - Source: "The parties hereby agree" → Target: "पक्षकार इसके द्वारा सहमत होते हैं"
  - Source: "hereinafter referred to as..." → Target: "इसके बाद ... कहा जाएगा"
  - Source: "as defined hereunder" → Target: "जैसा कि नीचे परिभाषित किया गया है"
  - Source: "hereto" → Target: "इससे संबंधित"
- **English passive voice → Hindi passive (कर्मवाच्य)**
  - Source: "The report was submitted on time" → Target: "रिपोर्ट समय पर प्रस्तुत की गई"
  - Source: "It is recommended that..." → Target: "यह अनुशंसित है कि..."
  - Source: "The document is attached" → Target: "दस्तावेज़ संलग्न है"
  - Note: Hindi uses passive less than English; active voice often sounds more natural
- **English "pursuant to" → Hindi के अनुसार / के तहत**
  - Source: "pursuant to Section 5" → Target: "धारा 5 के अनुसार"
  - Source: "pursuant to the agreement" → Target: "समझौते के तहत"
- **English "in accordance with" → Hindi के अनुसार / के अनुरूप**
  - Source: "in accordance with the terms" → Target: "शर्तों के अनुसार"
- **English "notwithstanding" → Hindi के बावजूद / के होते हुए भी**
  - Source: "Notwithstanding the foregoing..." → Target: "उपरोक्त के बावजूद..."
  - Source: "Notwithstanding any other provision" → Target: "किसी अन्य प्रावधान के होते हुए भी"
- **English "subject to" → Hindi के अधीन / की शर्त के साथ**
  - Source: "Subject to the terms..." → Target: "शर्तों के अधीन..."
  - Source: "Subject to approval" → Target: "अनुमोदन की शर्त के साथ"
- **English "whereas" clauses (recitals) → Hindi formal connectors**
  - Source: "WHEREAS, the Company wishes to engage..." → Target: "जबकि, कंपनी ... को नियुक्त करना चाहती है"
  - Note: Hindi contracts use चूँकि / जबकि for whereas clauses
- **English "witnesseth" → Hindi प्रमाणित करता है**
  - Source: "This Agreement witnesseth..." → Target: "यह समझौता प्रमाणित करता है..."
- **English letter closing → Hindi letter closing**
  - Source: "Sincerely," → Target: "भवदीय" / "आपका भवदीय"
  - Source: "Best regards," → Target: "सादर" / "भवदीय"
  - Source: "Yours faithfully," → Target: "आपका विश्वासी" / "भवदीय"
  - Source: "Yours truly," → Target: "आपका आज्ञाकारी" (formal) / "भवदीय"
  - Note: Hindi has more gradation of closings than English:
    - भवदीय (standard formal)
    - आपका भवदीय (more formal)
    - सादर (with regards)
    - आपका विश्वासी (Yours faithfully)
    - आपका आज्ञाकारी (Yours obediently — subordinate to superior)
- **English "Attached please find..." → Hindi संलग्न है / साथ संलग्न**
  - Source: "Please find attached the contract" → Target: "अनुबंध संलग्न है"
  - Source: "Attached is the report" → Target: "रिपोर्ट संलग्न की गई है"
- **English section references → Hindi conventions**
  - Source: "Section 5.2" → Target: "धारा 5.2" or "अनुच्छेद 5.2"
  - Source: "Appendix A" → Target: "परिशिष्ट A" / "अनुबंध A"
  - Source: "Clause 3.1" → Target: "खंड 3.1"
  - Source: "Paragraph 4" → Target: "पैराग्राफ 4" / "अनुच्छेद 4"
- **English references to laws → Hindi reference style**
  - Source: "pursuant to Section 5 of the Securities Act" → Target: "प्रतिभूति अधिनियम की धारा 5 के अनुसार"
  - Source: "under the laws of India" → Target: "भारत के कानूनों के तहत"
  - Note: Hindi word order for citations: Act Name + की + Section + के अनुसार
- **English bullet list conventions → Hindi conventions**
  - Source: Bullet items starting with capital letter → Target: Hindi may start with lowercase or verb stem
  - Source: Bullets ending with semicolons → Target: Hindi bullets typically end with semicolon (;) and last with full stop (।)
- **English numbering in legal docs** → Hindi (same hierarchical numbering)
  - Source: "1.1, 1.2, 1.2.1" → Target: "१.१, १.२, १.२.१" (can use Devanagari numerals)
  - Note: Legal documents may use Devanagari numerals or Arabic, but must be consistent

### Tense and Aspect Notes

- **English present perfect → Hindi past tense or present perfect**
  - Source: "The test has been completed" → Target: "परीक्षण पूर्ण हो गया है"
  - Source: "The data has been analyzed" → Target: "डेटा का विश्लेषण कर लिया गया है"
- **English present continuous → Hindi present progressive**
  - Source: "The system is running" → Target: "सिस्टम चल रहा है"
  - Source: "We are working on it" → Target: "हम इस पर काम कर रहे हैं"
- **English future tense (will) → Hindi future (same)**
  - Source: "The report will be delivered tomorrow" → Target: "रिपोर्ट कल दी जाएगी"
  - Note: Hindi future also expresses obligation in legal contexts (करेगा = shall/will)
- **English "used to" / habitual past → Hindi habitual past**
  - Source: "The system used to run on Windows" → Target: "सिस्टम पहले विंडोज़ पर चलता था"

## Punctuation Conversion

- **English quotation marks "" → Hindi ""** (same symbol, but Hindi uses different nesting conventions)
  - Source: 'He said "This is important"' → Target: 'उसने कहा, "यह महत्वपूर्ण है"'
  - Source: 'The term "interface" refers to...' → Target: 'शब्द "इंटरफ़ेस" का अर्थ है...'
  - Note: Hindi uses the same double-quote marks as English, but spacing follows Hindi word boundaries
- **English inner quotation marks '' → Hindi ''** (same nesting: outer "", inner '')
  - Source: 'She said "He told me \'Go now\'"' → Target: 'उसने कहा, "उसने मुझसे कहा, \'अभी जाओ\'"'
- **Hindi full stop । (purnaviram) → can substitute English period in formal Hindi**
  - Source: "This is a sentence. This is another." → Target: "यह एक वाक्य है। यह दूसरा वाक्य है।"
  - Note: The purnaviram (।) is the traditional Hindi full stop and should be used in formal/pure Hindi text
  - In mixed Hindi-English text, the Latin period (.) may be used for consistency
  - Consistency is critical: choose one style and stick with it throughout the document
- **Hindi comma (,)** — same symbol as English, half-width
  - Source: "apples, oranges, and bananas" → Target: "सेब, संतरे और केले"
  - Note: Hindi does not consistently use the Oxford comma before और (and)
  - Source: "first, second, third" → Target: "पहले, दूसरे, तीसरे"
- **Hindi question mark (?)** — same as English
  - Source: "Is this correct?" → Target: "क्या यह सही है?"
  - Note: Hindi puts the question mark at the end, same as English
  - Older Hindi typography used ॥ (double danda) for questions, but modern Hindi uses ?
- **Hindi exclamation mark (!)** — same as English
  - Source: "Great!" → Target: "बहुत अच्छा!"
  - Source: "Congratulations!" → Target: "बधाई हो!"
- **Hindi semicolon (;)** — same usage as English
  - Source: "Complete the first step; then proceed" → Target: "पहला चरण पूरा करें; फिर आगे बढ़ें"
- **Hindi colon (:)** — same as English
  - Source: "The following items:" → Target: "निम्नलिखित वस्तुएँ:"
- **English em dash (—) → Hindi em dash (—)** — same symbol, but Hindi uses spaces around it
  - Source: "Three components—CPU, RAM, and storage—are critical" → Target: "तीन घटक — CPU, RAM और स्टोरेज — महत्वपूर्ण हैं"
  - Note: Hindi uses spaces before and after em dash (not always in English)
- **English en dash (–) for ranges → Hindi en dash (–)** — same
  - Source: "pages 10–20" → Target: "पृष्ठ 10–20"
  - Source: "2010–2020" → Target: "2010–2020"
- **English hyphen (-)** in compounds → Hindi may or may not use hyphen
  - Source: "decision-making" → Target: "निर्णय-निर्माण" (Hindi uses hyphen in compounds)
  - Source: "state-of-the-art" → Target: "अत्याधुनिक" (single word, no hyphen)
  - Source: "well-known" → Target: "सुप्रसिद्ध" / "जाना-माना" (sometimes hyphenated)
  - Note: Hindi uses hyphen (योजक चिह्न) in some compound words
- **English ellipsis ... (3 dots) → Hindi ... (3 dots)** — same
  - Source: "and so on..." → Target: "इत्यादि..." / "वगैरह..."
  - Note: Hindi uses 3 dots like English; avoid 6 dots used in Chinese
- **English apostrophe (') → Hindi usage varies**
  - Source: "O'Brien" → Target: "ओ'ब्रायन" (kept for foreign names)
  - Source: "don't" → Target: "नहीं" (contractions do not exist in Hindi, expand to full form)
  - Source: "it's" → Target: "यह है" (expand contraction)
  - Note: Hindi does not use contractions with apostrophes; always expand them
- **English percent sign with/without space → Hindi (no space before %)**
  - Source: "50%" → Target: "50%" (no space before %, unlike French)
  - Source: "a 10% increase" → Target: "10% की वृद्धि"
- **English slash (/)** → Hindi same slash
  - Source: "and/or" → Target: "और/या" (same usage)
  - Source: "input/output" → Target: "इनपुट/आउटपुट"
- **English/Devanagari digits**: Can use Devanagari numerals (०१२३४५६७८९) or Arabic (0123456789)
  - Source: "2024" → Target: "2024" or "२०२४"
  - Source: "Page 5" → Target: "पृष्ठ 5" or "पृष्ठ ५"
  - Note: In formal Hindi text, Devanagari numerals are preferred but Arabic numerals are very common
  - Consistency is key: choose one numeral system for the entire document

### Hindi Punctuation Marks (विराम चिह्न) Summary

| English | Hindi | Name in Hindi | Notes |
|---------|-------|---------------|-------|
| . (full stop) | । | पूर्णविराम (purnaviram) | Traditional Hindi full stop |
| . | . | लाटीन पूर्णविराम | Latin period — use in mixed text |
| , | , | अल्पविराम (alpaviram) | Same comma |
| ? | ? | प्रश्नवाचक चिह्न | Same question mark |
| ! | ! | विस्मयादिबोधक चिह्न | Same exclamation mark |
| : | : | निर्देशक चिह्न | Same colon |
| ; | ; | अर्धविराम (ardhaviram) | Same semicolon |
| " " | " " | उद्धरण चिह्न | Quotation marks (same) |
| ' ' | ' ' | एकल उद्धरण चिह्न | Single quotes (same) |
| — | — | डैश (dash) | Em dash (same, Hindi spaces around) |
| - | - | योजक चिह्न (yojak chihn) | Hyphen (same) |
| ... | ... | लोप चिह्न (lop chihn) | Ellipsis (same) |
| ( ) | ( ) | कोष्ठक (koshtak) | Parentheses (same) |
| ऽ | ऽ | अवग्रह (avagraha) | Avagraha — Hindi-specific elision mark |
| ॥ | ॥ | दोहरा दंड (dohra dand) | Double danda — end of verse/paragraph in religious/poetic text |
| । | । | खड़ी पाई (khadī pāī) / दंड (dand) | Single danda — Hindi full stop |

### Special Hindi Typographic Rules

- **Word spacing**: Hindi uses spaces between words (unlike Chinese). Always insert proper word boundaries
  - Source: "Pleaseconfirmreceipt" (English: "Please confirm receipt") → Target: "कृपया प्राप्ति की पुष्टि करें" (spaces between words)
- **Non-breaking spaces**: Hindi does not have the same extensive non-breaking space rules as European languages
  - Number and unit: "5 किग्रा" (normal space is fine)
  - Date and month: "15 जनवरी" (normal space)
- **Abbreviations**: Hindi uses abbreviations with periods
  - "डॉ." (Dr.), "प्रो." (Prof.), "श्री" (Mr. — no period needed for श्री)
  - "आदि" (etc.), "इत्यादि" (etc.)
  - "सं." (नं. for number), "पृ." (page)
- **Hindi numeral comma** uses the Indian grouping system:
  - 1,23,45,678 (not 12,345,678)
  - This applies to all large numbers in Hindi text
- **Colon usage in Hindi**: Hindi uses colon (:) before lists and explanations, similar to English
  - Hindi also uses colon after salutations in letters: "प्रिय महोदय:" (Dear Sir:)
- **The खड़ी पाई / purnaviram (।)**:
  - Used as the full stop in formal Hindi
  - Not used in mixed Hindi-English text
  - Must not be confused with the Latin period
  - Key differences from Latin period: है। (Hindi) vs. hai. (English transliteration)
- **Avagraha (ऽ)**: Used rarely in modern Hindi, appears in Sanskritized text to mark vowel elision
  - Example: "क्वऽपि" (kvā'pi, "somewhere")
  - Avoid unless the text is highly Sanskritized formal/legal Hindi
- **Mathematical operators** in Hindi: same spacing as English
  - Source: "5 + 3 = 8" → Target: "5 + 3 = 8" (same spacing)
