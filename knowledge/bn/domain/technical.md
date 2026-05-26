---
id: bn/domain/technical
type: domain
target_lang: bn
name: Domain: Technical (Bengali — BN)
description: Translation rules for technical and IT documents into Bengali
---

## Reader Model

**Who reads this document and what do they expect?**

Technical document readers in Bengali are IT professionals, software developers, engineers, system administrators, and technical managers. They read the document to understand technical specifications, procedures, or product documentation. They expect:

- **Precise technical terminology** — the same technical concept must use the same Bengali term throughout.
- **Consistent code and command preservation** — code snippets, commands, and URLs must NOT be translated.
- **Clear, accessible language** — technical Bengali should be understandable to the target audience without being overly simplified.
- **Standard formatting** — code blocks, technical references, and UI elements follow established conventions.
- **Appropriate register** — formal but clear. Not legalistic, but not casual.

**What would break their trust?**
- A mistranslated technical term that changes the meaning of a specification.
- Translating code, commands, or URLs.
- Inconsistent terminology for the same technical concept.
- Overly literal translations that make technical instructions confusing.

## Decision Framework

### 1. IT Terminology in Bengali

| Source Term | Bengali Decision |
|---|---|
| Software | সফটওয়্যার (preserve — no established Bengali equivalent) |
| Hardware | হার্ডওয়্যার (preserve) |
| Database | ডেটাবেস (preserve) |
| Server | সার্ভার (preserve) |
| Cloud Computing | ক্লাউড কম্পিউটিং (preserve) |
| Artificial Intelligence | কৃত্রিম বুদ্ধিমত্তা |
| Machine Learning | মেশিন লার্নিং (preserve) |
| Internet | ইন্টারনেট (preserve) |
| Website | ওয়েবসাইট (preserve) |
| Application | অ্যাপ্লিকেশন (preserve) |
| API | এপিআই (preserve acronym) |
| User Interface | ব্যবহারকারী ইন্টারফেস |
| Password | পাসওয়ার্ড (preserve) |
| Login | লগইন (preserve) |
| Logout | লগআউট (preserve) |
| Download | ডাউনলোড (preserve) |
| Upload | আপলোড (preserve) |
| Error | ত্রুটি / সমস্যা |
| Bug | বাগ (preserve) |
| Feature | ফিচার / বৈশিষ্ট্য |
| Framework | ফ্রেমওয়ার্ক (preserve) |
| Plugin | প্লাগইন (preserve) |
| Update | আপডেট (preserve) |
| Backup | ব্যাকআপ (preserve) |
| Firewall | ফায়ারওয়াল (preserve) |
| Encryption | এনক্রিপশন (preserve) |
| Bandwidth | ব্যান্ডউইথ (preserve) |
| Latency | লেটেন্সি (preserve) |
| Scalability | স্কেলেবিলিটি / বিস্তারযোগ্যতা |
| Repository | রিপোজিটরি (preserve) |
| Commit | কমিট (preserve) |
| Branch | ব্রাঞ্চ (preserve) |
| Merge | মার্জ (preserve) |

### 2. Code and Commands

| Source Element | Bengali Decision |
|---|---|
| Code snippets | NEVER translate. Preserve exactly as-is. |
| Command-line commands | NEVER translate. Preserve exactly as-is. |
| URLs | NEVER translate. Preserve exactly as-is. |
| File paths | NEVER translate. Preserve exactly as-is. |
| Variable names | NEVER translate. Preserve exactly as-is. |
| Function names | NEVER translate. Preserve exactly as-is. |
| Error messages (in code) | Preserve original. Add Bengali explanation in surrounding text if needed. |
| API endpoints | NEVER translate. Preserve exactly as-is. |

### 3. Technical Documentation Register

| Source Register | Bengali Decision |
|---|---|
| API documentation | Formal: use আপনি register, precise terminology, consistent formatting. |
| User guide | Semi-formal: use আপনি register, clear and accessible language. |
| Technical specification | Formal: use আপনি register, precise terminology, structured format. |
| README / developer docs | Semi-formal: may use তুমি register for open-source projects. |
| Error message explanations | Formal: use আপনি register, clear and helpful. |

### 4. UI Element Translation

| Source Element | Bengali Decision |
|---|---|
| Button labels | Concise: `সংরক্ষণ` (Save), `বাতিল` (Cancel), `মুছুন` (Delete) |
| Menu items | Standard terms: `ফাইল` (File), `সম্পাদনা` (Edit), `দেখুন` (View) |
| Tooltips | Clear and brief |
| Error messages | `ত্রুটি:` prefix, followed by clear explanation |
| Success messages | `সফল:` prefix |
| Confirmation dialogs | Clear question with action buttons |

### 5. Bengali Technical Writing Conventions

| Convention | Description |
|---|---|
| Passive voice | Technical Bengali uses passive voice for procedures: `পাসওয়ার্ড লিখুন` (Enter password — imperative) or `পাসওয়ার্ড লেখা হয়` (Password is entered — passive). |
| Imperative for instructions | Use formal imperative: `ক্লিক করুন` (Click), `টাইপ করুন` (Type). |
| Code references in text | Wrap in backticks or use quotation marks: `git commit` কমান্ড ব্যবহার করুন. |
| Technical abbreviations | Preserve English abbreviations with Bengali expansion on first use: `ইউজার ইন্টারফেস (UI)`. |

## Error Pattern Library

### Critical Errors (zero tolerance)

| Error | Why It Is Critical |
|---|---|
| **Translating code** | Translating code, commands, or variable names breaks functionality. |
| **Mistranslating technical terms** | Wrong technical terms confuse developers and may cause implementation errors. |
| **Inconsistent terminology** | Using different Bengali terms for the same concept creates confusion. |
| **Translating URLs** | URLs are machine-readable. Translating them breaks links. |

### Common Errors (frequent in practice)

| Error | Guidance |
|---|---|
| **Overly literal translation** | Technical instructions should be translated for clarity, not word-for-word. |
| **Missing backticks for code references** | Code references in running text should be visually distinct. |
| **Inconsistent UI terminology** | The same button or menu item must use the same Bengali term throughout. |

### Subtle Errors (easy to miss)

| Error | Guidance |
|---|---|
| **Missing English term in parentheses** | When introducing a Bengali technical term for the first time, include the English term in parentheses. |
| **Wrong register for target audience** | Developer docs may use slightly less formal register than user guides. |
| **Altered screenshot text** | If screenshots contain English text, note that the UI is not localized. |

## Domain-Specific Reference

### Common Technical Terms (English–Bengali)

| English | Bengali |
|---|---|
| Function | ফাংশন |
| Variable | ভ্যারিয়েবল / চলরাশি |
| Array | অ্যারে / সারণি |
| Loop | লুপ / পুনরাবৃত্তি |
| Conditional | শর্তমূলক |
| Return | রিটার্ন |
| Parameter | প্যারামিটার / চলক |
| Argument | আর্গুমেন্ট / যুক্তি |
| Module | মডিউল |
| Library | লাইব্রেরি / গ্রন্থাগার |
| Class | ক্লাস |
| Object | অবজেক্ট / বস্তু |
| Method | মেথড / পদ্ধতি |
| Interface | ইন্টারফেস / কাঠামো |
| Dependency | নির্ভরতা |
| Configuration | কনফিগারেশন / বিন্যাস |
| Deployment | ডিপ্লয়মেন্ট / মোতায়েন |
| Testing | পরীক্ষা |
| Debugging | ডিবাগিং / ত্রুটি নির্ণয় |
| Version | সংস্করণ |
| Release | রিলিজ / প্রকাশ |

### Technical Documentation Template

```
# [বিষয়]

## ভূমিকা
[বিষয়ের সংক্ষিপ্ত বিবরণ]

## পূর্বশর্ত
- [পূর্বশর্ত ১]
- [পূর্বশর্ত ২]

## ধাপসমূহ
### ধাপ ১: [ধাপের নাম]
[বিস্তারিত নির্দেশনা]

```bash
[কমান্ড]
```

### ধাপ ২: [ধাপের নাম]
[বিস্তারিত নির্দেশনা]

## সমস্যা সমাধান
| সমস্যা | সমাধান |
|---|---|
| [সমস্যা ১] | [সমাধান ১] |
```

### Number Format in Technical Documents

| Element | Convention |
|---|---|
| Version numbers | Preserve as-is: `v2.5.1`, `3.0.0` |
| Port numbers | Digits: `পোর্ট 80`, `পোর্ট 443` |
| IP addresses | Preserve as-is: `192.168.1.1` |
| File sizes | Preserve units: `100 MB`, `1.5 GB` |
| Timeouts | Preserve units: `30 সেকেন্ড`, `5 মিনিট` |
| Quantities | Digits: `5 থ্রেড`, `10 কানেকশন` |
