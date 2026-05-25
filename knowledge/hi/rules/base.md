# Hindi Translation Knowledge Base — Base Rules

## 1. Number Format

### 1.1 Decimal Point
- Use the decimal point (.) as the decimal separator in Hindi translations.
- Examples: 3.14, 0.5, 99.99
- Do NOT use a decimal comma (,), which is the convention in some European languages.
- In official Hindi (राजभाषा), the decimal point is the standard.

### 1.2 Thousands Separator
- Use the comma (,) as the thousands separator.
- Examples: 1,234 | 45,678 | 9,87,654 (Indian grouping — see 1.3)
- Standard international grouping: 1,000,000 (million)

### 1.3 Indian Numbering System (लाख/करोड़)
- Hindi prefers the Indian numbering system over the international system.
- Use the following Indian number words:
  - 1,00,000 = एक लाख (1 lakh)
  - 10,00,000 = दस लाख (10 lakh)
  - 1,00,00,000 = एक करोड़ (1 crore)
  - 10,00,00,000 = दस करोड़ (10 crore)
  - 1,00,00,00,000 = एक अरब (1 arab)
  - 10,00,00,00,000 = दस अरब (10 arab)
  - 1,00,00,00,00,000 = एक खरब (1 kharab)
- When writing numerals in Indian style, group digits in lakh/crore pattern:
  - 12,34,567 (not 1,234,567)
  - 1,23,45,678 (not 12,345,678)
- **Zero-tolerance rule**: Mixing lakh/crore with million/billion is a critical error.
- When the source text uses million/billion, convert to lakh/crore/arab in Hindi.

### 1.4 Negatives
- Use the minus sign (−) or the word ऋण for negative numbers.
- In financial contexts, parentheses may also indicate negative values: (1,000).
- Examples: −5, ऋण १,०००
- Avoid using the hyphen (-) as a minus sign in numerals.

### 1.5 Percentages
- Use the percent sign (%) after the number with a space: ५०%
- Alternatively, प्रतिशत may follow the number: ५० प्रतिशत
- Be consistent within a document — do not mix % and प्रतिशत arbitrarily.
- For fractional percentages: ३.५% or ३.५ प्रतिशत

### 1.6 Ordinal Numbers
- Use Devanagari ordinal markers: पहला/पहली (1st), दूसरा/दूसरी (2nd), तीसरा/तीसरी (3rd)
- For higher ordinals: चौथा, पाँचवाँ, छठा, etc.
- Match gender of the noun being modified.

## 2. Currency

### 2.1 Rupee Symbol and Position
- Place the ₹ symbol BEFORE the amount: ₹ 100.00
- Maintain a non-breaking space between ₹ and the numeral.
- For paise (पैसे), use decimal format: ₹ 125.50 (125 rupees and 50 paise)

### 2.2 ISO Currency Codes
- Use INR for Indian Rupee, USD for US Dollar, EUR for Euro.
- In running Hindi text, write the code without spaces: १०० INR
- Currency codes are written in uppercase Latin script even in Hindi text.

### 2.3 Currency Names in Hindi
- रुपया (masculine) for rupee, डॉलर for dollar, यूरो for euro
- Plural: रुपए (or रुपये), डॉलर, यूरो
- Paise: पैसा (singular), पैसे (plural)
- Examples: ५० रुपए | १०० डॉलर | २० यूरो

### 2.4 Financial Notation
- Large currency amounts use Indian numbering: ₹ ५ लाख, ₹ १ करोड़
- In tables: ₹ in header, numerals in cells
- Cents/paisa: ५० पैसे, ₹ ०.५०

## 3. Date and Time

### 3.1 Date Format
- Use DD/MM/YYYY format: २५/१२/२०२४
- This is the standard in India (both Hindi and English contexts).
- Do NOT use MM/DD/YYYY (US format).
- **Zero-tolerance rule**: MM/DD/YYYY is a critical error in Hindi translation.

### 3.2 Written Dates in Hindi
- Use cardinal numbers with month name: २५ दिसंबर २०२४
- Do NOT use ordinal dates (25th December) in Hindi.
- Month name may precede or follow the day number; day-number-first is more common.

### 3.3 Hindi Month Names — Two Systems

#### 3.3.1 Gregorian Month Names (Standard Hindi)
These are the commonly used month names in official Hindi:
- जनवरी (January)
- फरवरी (February)
- मार्च (March)
- अप्रैल (April)
- मई (May)
- जून (June)
- जुलाई (July)
- अगस्त (August)
- सितंबर (September)
- अक्टूबर (October)
- नवंबर (November)
- दिसंबर (December)

#### 3.3.2 Hindu Calendar Month Names (Vikram Samvat)
Used in religious/agricultural contexts:
- चैत्र (Chaitra) — March-April
- वैशाख (Vaishakha) — April-May
- ज्येष्ठ (Jyeshtha) — May-June
- आषाढ़ (Ashadha) — June-July
- श्रावण (Shravana) — July-August
- भाद्रपद (Bhadrapada) — August-September
- आश्विन (Ashwina) — September-October
- कार्तिक (Kartika) — October-November
- मार्गशीर्ष/अगहन (Margashirsha/Agrahayana) — November-December
- पौष (Pausha) — December-January
- माघ (Magha) — January-February
- फाल्गुन (Phalguna) — February-March

**Rule**: Use Gregorian names for general/official documents. Use Hindu calendar names only when the source explicitly references the Hindu calendar or the context is religious/traditional.

### 3.4 Time Format
- Use 24-hour format: १४:३०, ०९:१५
- 12-hour format is acceptable only in informal or literary contexts.
- Use HH:MM format with a colon separator.
- For seconds: HH:MM:SS

### 3.5 Time Expressions
- Use Hindi time words: सुबह (morning), दोपहर (afternoon), शाम (evening), रात (night)
- Half-past: साढ़े (saaṛhe): साढ़े तीन बजे (3:30)
- Quarter-past: सवा: सवा चार बजे (4:15)
- Quarter-to: पौने: पौने पाँच बजे (4:45)
- O'clock: बजे

## 4. Addresses

### 4.1 Indian Address Format
Hindi addresses follow a bottom-up hierarchical order (specific to general):

1. **Name** (नाम) — Recipient's full name
2. **House/Plot Number** (मकान/प्लॉट संख्या)
3. **Street/Road** (गली/सड़क)
4. **Locality/Area** (क्षेत्र/मोहल्ला)
5. **City/Town** (शहर/नगर)
6. **State** (राज्य)
7. **PIN Code** (पिन कोड)

Example:
```
श्री राम कुमार
मकान संख्या ४२
गली नंबर ७, पॉश गार्डन
साकेत
नई दिल्ली — ११००१७
दिल्ली
```

### 4.2 Address Vocabulary
- मकान संख्या / घर नंबर — House number
- गली — Lane/alley
- सड़क — Road
- मार्ग — Road/avenue
- क्षेत्र / इलाका — Area/locality
- नगर / शहर — City
- राज्य — State
- पिन कोड — PIN code (Postal Index Number)
- ज़िला / जिला — District
- प्रांत — Province

### 4.3 Abbreviations in Addresses
- Keep standard address abbreviations in Latin script when universally recognized: Rd., St., Nagar, Extn.
- Or transliterate to Devanagari: सड़क, मार्ग, नगर, विस्तार
- PIN code is always written as PIN or पिन.

## 5. Proper Nouns

### 5.1 Devanagari Script for Hindi Names
- Personal names, place names, and organizational names should be rendered in Devanagari script.
- Follow standard Hindi transliteration conventions (not Sanskritized or overly Anglicized).

### 5.2 Foreign Name Transliteration (हिंदीकरण / Hindization)
- Foreign names should be transliterated phonetically into Devanagari.
- Use the closest Hindi approximation of the original pronunciation.
- Principles:
  - Map foreign phonemes to the nearest Devanagari equivalent.
  - Preserve syllable structure where possible.
  - Avoid conjunct clusters that are unpronounceable in Hindi.

Examples:
| English | Hindi |
|---|---|
| Johnson | जॉनसन |
| Elizabeth | एलिज़ाबेथ |
| McDonald's | मैकडॉनल्ड्स |
| Washington | वॉशिंगटन |
| Germany | जर्मनी |
| Paris | पेरिस |

### 5.3 Consistent Transliteration
- Once a transliteration is chosen for a name, use it consistently throughout the document.
- For well-known names, follow established Hindi usage (e.g., अमेरिका not यूनाइटेड स्टेट्स unless the context requires the full form).
- Use standard transliteration references when available (e.g., government gazette, official Hindi name).

### 5.4 Honorifics and Titles
- **श्री** (Shri) — Mr. / male honorific
- **श्रीमती** (Shrimati) — Mrs. / married female honorific
- **सुश्री** (Sushri) — Ms. / female honorific (marital status neutral)
- **कु.** (Kumari) — Miss / unmarried female (official contexts)
- **डॉ.** (Dr.) — Doctor
- **प्रो.** (Prof.) — Professor

Usage rules:
- Honorifics precede the name: श्री रमेश शर्मा
- In official Hindi, honorifics are used more frequently than in English.
- Avoid English honorifics (Mr./Mrs./Ms.) in Hindi text.
- For joint names: श्री रमेश एवं श्रीमती सीता शर्मा

### 5.5 Place Names
- Use standard Hindi names for Indian places: मुंबई (not Bombay), चेन्नई (not Madras), कोलकाता (not Calcutta)
- For foreign places, use standard Hindi transliteration: लंदन, पेरिस, टोक्यो
- When a Hindi name exists alongside an English name, prefer the Hindi form.

### 5.6 Organization Names
- Translate the generic part of organization names: भारतीय स्टेट बैंक (State Bank of India)
- Keep branded/named entities in transliteration: गूगल, माइक्रोसॉफ्ट, टाटा कंसल्टेंसी सर्विसेज़
- For acronyms, keep the Latin script acronym if widely recognized: RBI, WHO, UNO

### 5.7 Retained English Terms
- Some terms are commonly retained in English even in Hindi text: software, internet, email, website
- Use Devanagari transliteration when the term has gained Hindi acceptance: सॉफ़्टवेयर, इंटरनेट, ईमेल, वेबसाइट
- When in doubt, prefer the Devanagari form for technical terms.

## 6. Punctuation

### 6.1 Purnaviram (पूर्णविराम) — Full Stop
- Hindi uses the danda (।) as the sentence-ending punctuation: पूर्णविराम
- This is the traditional Hindi full stop.
- **However**, in modern Hindi (especially official/document Hindi), the Latin period (.) is also widely accepted.
- Consistency rule: pick one style (। or .) and use it throughout the document.
- For government documents, । is preferred.

### 6.2 Comma (,)
- The comma in Hindi serves the same function as in English — list separation, clause separation.
- In Devanagari text, use the standard Latin comma (,).
- There is no special Devanagari comma character in common use.
- Do NOT use the Latin semicolon as a Hindi comma.

### 6.3 Quotation Marks
- For direct speech and quotations, use "double quotes" ( " " ) or 'single quotes' ( ' ' ).
- In Hindi, the use of quotation marks follows the same conventions as English.
- For nested quotations, alternate between double and single quotes.
- Some Hindi texts use गूल (Chinese-style quotes) but this is rare in modern Hindi.

### 6.4 Hindi-Specific Punctuation

| Symbol | Hindi Name | Usage |
|---|---|---|
| । | पूर्णविराम | Sentence end (traditional) |
| , | अल्पविराम | Comma / list separator |
| ; | अर्धविराम | Semicolon (same as English) |
| : | कोलन / अपूर्णविराम | Colon (same as English) |
| — | डैश / योजक चिह्न | Dash / parenthetical |
| - | हाइफ़न / विभाजक चिह्न | Hyphen / compound joiner |
| … | लोप चिह्न | Ellipsis |

### 6.5 Parentheses
- Use standard parentheses ( ) as in English.
- Use brackets [ ] for editorial insertions or clarifications.

### 6.6 Abbreviation Punctuation
- Hindi abbreviations do not require a period after each letter.
- Examples: भा.स.बैं. (abbreviated), or simply भारतीय स्टेट बैंक

### 6.7 Number and Punctuation
- In Devanagari numerals, commas follow the same grouping rules: १२,३४,५६७
- Decimal point is standard: ३.१४

## 7. Formatting

### 7.1 Title Capitalization
- Hindi does not use capitalization (uppercase/lowercase distinction).
- **Rule**: Do not attempt to emulate English title case in Hindi.
- Use bold, underline, or increased font size for titles instead.
- In transliterated titles, follow the original capitalization.

### 7.2 Headings and Subheadings
- Hindi headings should be marked by formatting (bold, larger font) rather than capitalization.
- Numbering in headings: १. / १.१ / १.१.१ (using Devanagari or Arabic numerals consistently)

### 7.3 Lists
- Bulleted lists: Use the same bullet style as the source (•, -, *).
- Numbered lists: Use १, २, ३ or 1, 2, 3 — be consistent.
- For nested lists, maintain the hierarchy visually with indentation.

### 7.4 Tables
- Table headers should be translated fully.
- Preserve the table structure (columns, rows, merged cells).
- Align numbers to the right, text to the left (or as per source).
- Currency columns: right-aligned with ₹ symbol in header or first cell.

### 7.5 Devanagari Spacing

#### 7.5.1 Word Spacing
- Hindi word spacing follows the same rule as English: one space between words, no space before punctuation.
- Devanagari script does **not** have uppercase/lowercase, so spacing carries more visual weight for readability.

#### 7.5.2 Conjunct Consonants
- Conjuncts (संयुक्त व्यंजन) should be rendered correctly using halant (्).
- Examples: क्य (क् + य), त्र (त् + र), ज्ञ (ज् + ञ)
- Ensure proper rendering: कर्म (not कर्म), सत्य (not सत्‍य)

#### 7.5.3 Shirorekha (शिरोरेखा)
- The horizontal line (shirorekha) connects characters in a word.
- Ensure that words are properly segmented — the shirorekha should not connect across word boundaries.
- Font selection matters: some Devanagari fonts have continuous shirorekha, others have segmented.

### 7.6 Emphasis
- Bold for headings and strong emphasis.
- Italics for secondary emphasis or foreign terms (if the font supports Devanagari italics).
- Underline sparingly (mostly in official/legal documents).

### 7.7 Line Breaks and Paragraphs
- Paragraphs in Hindi follow the same paragraph conventions as English.
- Do not break a word across lines arbitrarily — split at syllable boundaries if needed.
- Avoid orphaned lines.

## 8. Grammar

### 8.1 Sentence Structure (SOV)
- Hindi follows Subject-Object-Verb (SOV) word order.
- English is SVO (Subject-Verb-Object).
- **Transformation rule**: Move the verb to the end of the clause/sentence in Hindi.
- Examples:
  - English (SVO): "Ram eats an apple."
  - Hindi (SOV): "राम सेब खाता है।" (Ram apple eats.)

### 8.2 Word Order Hierarchy
- Standard Hindi sentence: Subject + Time + Manner + Place + Object + Verb
- Example: मैं कल बस से स्कूल जाऊँगा। (I tomorrow bus by school will-go.)
- Modifiers precede the noun: बड़ा घर (big house), not घर बड़ा

### 8.3 Grammatical Gender (पुल्लिंग / स्त्रीलिंग)

Hindi has two grammatical genders:

#### 8.3.1 Masculine (पुल्लिंग)
- Typically ends in -आ: लड़का, कुत्ता, घर
- Masculine declension: लड़का → लड़के (oblique/plural)

#### 8.3.2 Feminine (स्त्रीलिंग)
- Typically ends in -ई or -इया: लड़की, बिल्ली, चिड़िया
- Consonant-ending words may also be feminine: किताब, भाषा

#### 8.3.3 Gender Agreement
- Adjectives agree with the noun in gender and number:
  - बड़ा लड़का (big boy) — masculine singular
  - बड़ी लड़की (big girl) — feminine singular
  - बड़े लड़के (big boys) — masculine plural
  - बड़ी लड़कियाँ (big girls) — feminine plural
- Verbs agree with the subject in gender and number (except in perfective transitive with ने).

### 8.4 Number (एकवचन / बहुवचन)

#### 8.4.1 Singular (एकवचन)
- One entity: एक लड़का, एक किताब

#### 8.4.2 Plural (बहुवचन)
- Multiple entities: लड़के, किताबें
- Plural markers:
  - Masculine -आ → -ए: लड़का → लड़के
  - Feminine -ई → -इयाँ: लड़की → लड़कियाँ
  - Neuter/other: -एँ, -ें, or unchanged depending on the word

### 8.5 Postpositions (परसर्ग)
Hindi uses postpositions (after the noun) rather than prepositions (before the noun).

| Postposition | English equivalent | Example |
|---|---|---|
| ने | (ergative marker) | राम ने किया (Ram did) |
| को | to, at | राम को दो (Give to Ram) |
| से | from, with, by | राम से कहो (Tell Ram) |
| का/के/की | of | राम का घर (Ram's house) |
| में | in | घर में (in the house) |
| पर | on, at | मेज़ पर (on the table) |
| तक | until, up to | शाम तक (until evening) |
| के लिए | for | राम के लिए (for Ram) |
| के साथ | with | राम के साथ (with Ram) |
| के बिना | without | पानी के बिना (without water) |

### 8.6 Oblique Case (तिर्यक/विभक्ति)
- When a noun is followed by a postposition, it goes into the oblique case.
- Oblique forms:
  - Masculine -आ → -ए: लड़का → लड़के को
  - Feminine -ई → -ई (unchanged in singular): लड़की → लड़की को
  - Masculine plural -ए → -ओं: लड़के → लड़कों को
  - Feminine plural -इयाँ → -इयों: लड़कियाँ → लड़कियों को

### 8.7 Verb Conjugation

#### 8.7.1 Present Tense
| Person | करना (to do) — Masculine | करना — Feminine |
|---|---|---|
| मैं (I) | करता हूँ | करती हूँ |
| तू (you, intimate) | करता है | करती है |
| तुम (you, familiar) | करते हो | करती हो |
| आप (you, formal) | करते हैं | करती हैं |
| वह (he/she) | करता है | करती है |
| वे (they) | करते हैं | करती हैं |

#### 8.7.2 Perfective Tense (with ने for transitive)
- Transitive verbs in perfective use ने marker and verb agrees with object:
  - राम ने सेब खाया। (Ram ate an apple — apple is masculine)
  - राम ने रोटी खाई। (Ram ate bread — bread is feminine)
- Intransitive verbs agree with subject:
  - राम आया। (Ram came — masculine)
  - सीता आई। (Sita came — feminine)

#### 8.7.3 Future Tense
| Person | करना (to do) — Masc Sg | करना — Fem Sg |
|---|---|---|
| मैं | करूँगा | करूँगी |
| तू | करेगा | करेगी |
| तुम | करोगे | करोगी |
| आप / वह | करेंगे / करेगा | करेंगी / करेगी |
| हम | करेंगे | करेंगी |

### 8.8 Copula (होना)
- Present: है / हैं (is/are)
- Past: था / थी / थे / थीं (was/were)
- Future: होगा / होगी / होंगे (will be)
- Subjunctive: हो / होऊँ / होएँ (may be)

### 8.9 Negation
- नहीं — primary negator (before the verb): मैं नहीं जाऊँगा।
- न — used with subjunctive/imperative: मत जाओ! (Don't go!)
- कभी नहीं — never
- कोई नहीं — no one
- कुछ नहीं — nothing

### 8.10 Question Formation
- Yes/no questions: rising intonation + क्या at the beginning: क्या वह आएगा?
- WH questions: क्या (what), कौन (who), कहाँ (where), कब (when), क्यों (why), कैसे (how), कितना (how much/many)

## 9. Formality

### 9.1 The Three Levels of Address

Hindi has three second-person pronouns reflecting social distance and respect:

| Pronoun | Level | Usage |
|---|---|---|
| तू | Intimate / vulgar | Used for children, close friends, deities; or as an insult |
| तुम | Familiar / informal | Used for peers, colleagues, subordinates in informal settings |
| आप | Formal / respectful | Used for superiors, elders, strangers, official contexts |

#### 9.1.1 Rules
- **In translation**, default to आप unless the source explicitly indicates intimacy/familiarity.
- **Zero-tolerance rule**: Using तू when आप is expected is a critical register error.
- तुम is acceptable for peer-to-peer, casual, or familial contexts (among equals).
- तू should almost never appear in formal/official translated documents.

### 9.2 Formal Register (औपचारिक शैली)

#### 9.2.1 Verb Forms for Formal Register
- Use आप with plural verb forms (even for singular referent):
  - आप कहाँ जा रहे हैं? (Where are you going? — formal)
  - Not: आप कहाँ जा रहा है?
- औपचारिक शैली uses:
  - आप + verb in -एँ / -ें / -इए form
  - का/के/की → the oblique form of the noun

#### 9.2.2 Honorific Verbs
- Some verbs have special honorific forms:
  - बैठना → बिराजना / पधारना (to sit, formal)
  - जाना → पधारना (to go, formal)
  - खाना → भोजन ग्रहण करना (to eat, formal)
  - कहना → कहना (same, but with respectful tone)
  - देना → प्रदान करना (to give, formal)
- Use these sparingly — only in highly formal/official contexts.

#### 9.2.3 Formal Vocabulary Choices
- Use Sanskrit-derived (तत्सम) words for formal register:
  - कार्य (not काम) for work
  - पत्र (not चिट्ठी) for letter
  - आरंभ (not शुरू) for start
  - निवास (not घर) for residence
  - भोजन (not खाना) for food
  - जल (not पानी) for water
- In official Hindi (राजभाषा), this register is standard.

### 9.3 Official Hindi (राजभाषा)

#### 9.3.1 Characteristics
- Heavily Sanskritized vocabulary (तत्सम preference)
- Complex compound formations
- Formal sentence structures
- Minimal English loanwords
- Use of government-approved terminology

#### 9.3.2 Official Hindi Markers
- कृपया (please) — used formally
- कार्यालय (office), विभाग (department), अनुभाग (section)
- आदेश (order), निर्देश (instruction), अनुमोदन (approval)
- प्रस्तुत (submitted), संलग्न (enclosed/attached)
- दिनांक (date) in place of तारीख

#### 9.3.3 When to Use
- Government documents, legal texts, official notifications
- Corporate communications in Hindi
- Academic writing
- Formal speeches

### 9.4 Informal Register
- Use tadbhav words (Hindi-vernacular):
  - काम (not कार्य)
  - चिट्ठी (not पत्र)
  - खाना (not भोजन)
  - पानी (not जल)
- तुम is acceptable
- Shorter sentences, more loanwords from English, Urdu, Persian

### 9.5 Register Matching
- The register of the translation must match the register of the source text.
- A formal English document → formal Hindi
- A casual English blog → informal/colloquial Hindi
- Mixed register is a translation error.

## 10. OCR Artifacts

### 10.1 Identification of OCR Artifacts
- Devanagari OCR has specific failure modes distinct from Latin script OCR.
- Common artifacts include:
  - Shirorekha splitting/merging across words
  - Conjunct consonant misrecognition (क्ष → कष, त्र → तर, ज्ञ → जञ)
  - Halant (्) loss or insertion
  - Matra (vowel sign) misplacement: ि vs ी, ु vs ू
  - Nukta (़) loss: क़ vs क, फ़ vs फ
  - Confusion between similar characters: द vs ड, भ vs म, त vs थ

### 10.2 Restoration Format
- When restoring uncertain/illegible text, use the format:
  `[पुनर्स्थापित: <restored text>]`
- Example: `[पुनर्स्थापित: कार्यालय]`
- Use this for:
  - Characters obscured by physical damage to source
  - Text that is illegible in the original
  - Sections where OCR confidence is below threshold

### 10.3 Common Devanagari OCR Errors

| Correct | Common OCR Error | Notes |
|---|---|---|
| क्ष | क्ष → कष | Conjunct break |
| त्र | त्र → तर | Halant loss |
| ज्ञ | ज्ञ → जञ | Conjunct break |
| श्र | श्र → सर | Shirorekha issue |
| क़ | क → no nukta | Nukta loss |
| फ़ | फ → no nukta | Nukta loss |
| ग़ | ग → no nukta | Nukta loss |
| ज़ | ज → no nukta | Nukta loss |
| ड़ | ड | Nuqta vs dot |
| ढ़ | ढ | Nuqta vs dot |
| ं (anusvara) | ं → no anusvara | Nasalization loss |
| ः (visarga) | ः → no visarga | Visarga loss |
| ँ (chandrabindu) | ँ → no chandrabindu | Nasalization loss |

### 10.4 OCR Correction Guidelines
- Verify all conjunct consonants (संयुक्त अक्षर) in the output.
- Check that the shirorekha connects components of the same word only.
- Verify nukta characters (क़, ख़, ग़, ज़, फ़, ड़, ढ़) — especially for Urdu/Persian loanwords.
- Confirm vowel sign placement (the matra is attached to the correct consonant).
- Check for missing anusvara (ं) and chandrabindu (ँ) which change meaning.
- Run a spell-check if tools are available.

### 10.5 Special Cases
- **Date strings**: OCR may confuse १ (1) and १, check digit recognition.
- **Punctuation**: danda (।) may be OCR'd as period (.) — restore based on context.
- **Numbers**: Devanagari numerals (१ २ ३) may be confused with English digits (1 2 3) — maintain the source's numeral system.
- **Multiple pages**: Check for repeated text at page boundaries (OCR duplicating page headers/footers).

### 10.6 Quality Check for OCR
For each OCR'd page:
1. Verify 5 random conjunct consonants.
2. Check 5 nukta characters.
3. Confirm shirorekha integrity for 3 long words.
4. Validate all numerals (Devanagari vs Arabic).
5. Check punctuation consistency (। vs .).

## 11. Translation Philosophy

### 11.1 Natural Hindi (स्वाभाविक हिंदी)
- The primary goal is to produce Hindi that reads naturally to a native speaker.
- Avoid literal/word-for-word translation from English (अंग्रेज़ी-अनुवादित हिंदी).
- A good Hindi translation should not sound like a translation at all.
- Prioritize idiomatic Hindi expressions over calques from English.

### 11.2 Shuddh Hindi vs. Hindustani

#### 11.2.1 Shuddh Hindi (शुद्ध हिंदी)
- Highly Sanskritized vocabulary
- Used in: formal/official/government contexts, academic writing
- Features: तत्सम words, complex compounds, minimal loanwords
- Examples: आकाश (sky), अग्नि (fire), जल (water), पृथ्वी (earth)
- Preferred for: official documents (राजभाषा), high-formality registers

#### 11.2.2 Hindustani (हिंदुस्तानी / खड़ी बोली)
- The everyday spoken language that mixes Hindi (Sanskrit-derived) and Urdu (Perso-Arabic-derived) vocabulary
- Features: tadbhav words, Urdu/Persian loanwords, English code-mixing
- Examples: आसमान (sky), आग (fire), पानी (water), ज़मीन (earth)
- Preferred for: general translation, journalism, creative writing

#### 11.2.3 Selection Rule
- Match the source text's register and vocabulary level.
- Government/legal/academic source → शुद्ध हिंदी
- General/casual/popular source → Hindustani
- Literary/poetic → may use either depending on the work's tradition

### 11.3 Tatsam vs. Tadbhav Vocabulary

| Tatsam (तत्सम) | Tadbhav (तद्भव) | Meaning |
|---|---|---|
| कार्य | काम | work |
| भोजन | खाना | food |
| जल | पानी | water |
| गृह | घर | home |
| पत्र | चिट्ठी | letter |
| रात्रि | रात | night |
| दिवस | दिन | day |
| हस्त | हाथ | hand |
| नेत्र | आँख | eye |
| कर्ण | कान | ear |

**Rule**: Tatsam words elevate the register; tadbhav words are everyday. Choose based on the required formality level.

### 11.4 Loanword Management

#### 11.4.1 English Loanwords
- Many English words are fully integrated into Hindi: बस, स्कूल, स्टेशन, डॉक्टर
- Use the standard Devanagari spelling for these.
- Avoid unnecessary Sanskritization of common English terms.

#### 11.4.2 Urdu/Persian Loanwords
- Hindi incorporates many Urdu/Persian words: किताब (book), दुनिया (world), शहर (city)
- These are standard Hindi vocabulary, not foreign words.
- Use nukta where required: ज़रूरत, ख़ास, ग़रीब

#### 11.4.3 When to Translate vs. Transcribe
- **Translate** when there is a standard Hindi term: computer → संगणक (rare) or कंप्यूटर (common)
- **Transcribe** when there is no standard Hindi term, or the English term is universally used
- For specialized/technical terms, research the standard Hindi equivalent

### 11.5 Handling English Sentence Structures
- Break long English sentences into shorter Hindi sentences.
- Convert passive voice to active where natural in Hindi (though passive is used in formal Hindi).
- Move relative clauses to precede the noun (Hindi: "the book that I read" → "जो किताब मैंने पढ़ी").
- Ensure postpositions are correctly placed after their objects.

### 11.6 Cultural Adaptation
- Adapt culturally specific references:
  - "Thanksgiving" → explain or omit in Hindi contexts
  - "Baseball" → keep or use a generic equivalent
  - Western measurements → convert to metric where appropriate
  - Western date conventions → Indian conventions
- Do NOT culturalize inappropriately — do not add Hindu references to a neutral text.

### 11.7 Consistency Across Translations
- Maintain a terminology glossary for each project.
- Use the same Hindi term for the same English term throughout.
- Avoid synonym variation in technical terms (do not use कार्य and काम interchangeably for "work" in the same document).

### 11.8 Editing and Revision Priority
1. **Accuracy**: All information is preserved.
2. **Grammar**: Hindi grammar is correct (gender, number, postpositions, verb agreement).
3. **Naturalness**: The Hindi reads naturally.
4. **Register**: The formality level matches.
5. **Formatting**: Document structure is preserved.
6. **Terminology**: Terms are consistent with the glossary.

### 11.9 Common Pitfalls
- **False friends**: English-like Hindi calques: "गिफ्ट बॉक्स" (fine) vs "उपहार पेटिका" (overly Sanskritized)
- **Over-Sanskritization**: Making simple text unnecessarily formal
- **Under-Sanskritization**: Using English/Urdu words in formal contexts where Sanskrit equivalents exist
- **Gender errors**: Incorrect gender agreement in verbs and adjectives
- **Postposition errors**: Missing or incorrect ने, को, से, का
- **Register mismatch**: Using casual language in a formal document
- **Inconsistent transliteration**: Spelling the same name differently in different places
