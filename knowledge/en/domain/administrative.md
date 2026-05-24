---
id: en/domain/administrative
type: domain
target_lang: en
name: Administrative Documents
description: Translation rules for government forms, regulatory filings, permits, and official correspondence into English
---

## Reader Model

**Who reads this document and what do they expect?**

Administrative document readers are government officials, regulatory reviewers, applicants, notaries, and regulated entities who use the document to verify compliance, process applications, or establish legal identity. They expect:

- **Process compliance** — forms, permits, and filings must follow the prescribed administrative procedure. Any deviation can cause rejection or delay.
- **Institutional recognition** — government body names, agency titles, and official designations must be immediately recognizable to the administering authority.
- **Traceability** — every reference number, filing code, case number, and date stamp must be preserved for audit and tracking.
- **Formal but clear language** — administrative English is direct and professional. It avoids the complexity of legal language while maintaining the formality required by official process.

**What would break their trust?**
- A translated institution name that cannot be matched to the official body.
- A missing or altered reference number that breaks the filing chain.
- A form field label that misrepresents the information required.
- An official seal or stamp description that omits key details.

## Decision Framework

### 1. Government Body Names

| Condition | Decision |
|---|---|
| Body has an established English name | Use the established English name (e.g., "Ministry of Finance"). Verify against official sources. |
| Body has no established English name | Keep the original name in full, then add a descriptive English translation in brackets on first mention. Subsequent mentions use the original name. |
| Body is a department or bureau within a ministry | Use the established hierarchical format: "[Department/Bureau/Division] of [Function]" or as documented by the government. |
| Acronym of the body name | Preserve the original acronym. If an English acronym is established, use that. |

### 2. Form Field Labels

| Condition | Decision |
|---|---|
| Field asks for personal identification information | Use standard English form labels: "Full Name", "Date of Birth", "Place of Birth", "Nationality", "Passport Number", "ID Number". |
| Field asks for contact information | Use standard labels: "Address", "Telephone", "Email", "Postal Code". |
| Field asks for a declaration or confirmation | Preserve the checkbox/declaration structure. Translate the statement exactly (e.g., "I hereby declare that..."). |
| Field has multiple-choice options | Translate each option exactly. Preserve the selection mechanism (checkbox, radio button, drop-down). |
| Field references another document or number | Preserve the reference. Do not translate reference numbers. |

### 3. Official Stamps and Seals

| Condition | Decision |
|---|---|
| Stamp contains text only | Translate the text. Describe the stamp format in brackets if needed for clarity (e.g., "[Circular stamp with official seal]"). |
| Stamp contains text and a logo or emblem | Translate the text. Describe the emblem type in brackets. Do not reproduce or modify the emblem. |
| Stamp contains a date | Preserve the date exactly. Convert to unambiguous format: "30 April 2025". |
| Handwritten annotation on the document | Transcribe the handwriting. Mark it clearly as "[Handwritten annotation]" and translate the text. |

### 4. Reference Numbers and Identifiers

| Condition | Decision |
|---|---|
| Any alphanumeric reference (case number, filing number, permit number, registration number) | Preserve exactly as in the source, including all characters, spaces, hyphens, and slashes. |
| Barcode or QR code description | Transcribe the code value if readable. Otherwise, note "[Barcode present]". |
| Date stamp | Preserve the date exactly. Add English translation of surrounding text. |

## Error Pattern Library

### Critical Errors (zero tolerance)

| Error | Why It Is Critical |
|---|---|
| **Translating institution names** | "Ministry of Industry" instead of the official "Ministry of Industry and Information Technology" makes the document untraceable in official records. |
| **Inconsistent document type terms** | Switching between "Certificate", "Certification", and "Certified Copy" for the same document type causes confusion. |
| **Losing reference numbers** | A missing case number can cause the document to be misfiled or rejected. |
| **Altering official seal or stamp description** | Omitting or misrepresenting details of a seal undermines the document's authenticity. |

### Common Errors (frequent in practice)

| Error | Guidance |
|---|---|
| **Inconsistent treatment of institution names** | On first mention, provide: Original Name [English Translation]. On subsequent mentions, use the original name consistently. |
| **Register mismatch** | Administrative documents require formal but not legalistic register. Avoid both casual language and overly complex legal phrasing. |
| **Form field misalignment** | When translating a fillable form, ensure the translated labels align with the correct input fields. Field order matters for form flow. |

### Subtle Errors (easy to miss)

| Error | Guidance |
|---|---|
| **Hyphenation or spacing in reference numbers** | "AB-123/45" is different from "AB12345". Copy alphanumeric references character by character. |
| **Date stamp vs handwritten date** | A stamped date and a handwritten date may differ. Preserve both and note the distinction. |
| **Seal color or format** | Red seals, embossed seals, and wet ink signatures all convey different levels of formality. Describe the seal type in brackets. |
| **Marginal notes and annotations** | Handwritten notes in margins, corrections with initials, and stamped annotations are part of the document. Transcribe, mark, and translate them. |

## Domain-Specific Reference

### Institution Name Format

| Context | Format |
|---|---|
| First mention in document | Original Name [English Translation] — e.g., "Ministerio de Hacienda [Ministry of Finance]" |
| Subsequent mentions | Original Name only |
| Acronym introduction | Add acronym in parentheses after full name on first mention |
| Well-known international bodies | Use the established English name directly (e.g., "World Health Organization") |

### Reference Number Preservation

| Reference Type | Preservation Rule |
|---|---|
| Case number | Preserve all characters including hyphens, slashes, dots, and spaces |
| Filing number | Preserve exactly; do not reorder segments |
| Permit / license number | Preserve alphanumeric string exactly |
| Registration number | Preserve including leading zeros |
| Document control number | Preserve including version or revision suffix |
| Tax ID / business registration | Preserve including country prefix or check digits |

### Document Type Terms

| Type | Usage |
|---|---|
| Certificate | Formal document attesting to a fact (birth, marriage, incorporation) |
| License | Permission granted by an authority to perform an activity |
| Permit | Authorization to do something subject to regulation |
| Registration | Entry in an official register |
| Notarization | Certification by a notary public |
| Affidavit | Written sworn statement |
| Power of Attorney | Authorization to act on someone's behalf |
| Decree | Order issued by an executive authority |
| Resolution | Formal decision by a body or official |

### Seal and Stamp Description

| Seal/Stamp Type | Description Convention |
|---|---|
| Round official stamp | "[Circular official stamp: [translated text]]" |
| Embossed seal | "[Embossed seal: [agency name]]" |
| Date stamp | "[Date stamp: 30 April 2025]" |
| Received stamp | "[Received stamp: [date]]" |
| Notary seal | "[Notary seal: [name, jurisdiction]]" |
| Company chop | "[Company stamp: [company name]]" |
