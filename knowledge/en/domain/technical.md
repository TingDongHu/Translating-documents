---
id: en/domain/technical
type: domain
target_lang: en
name: Technical Documents
description: Translation rules for manuals, specifications, and scientific papers into English
---

## Reader Model

**Who reads this document and what do they expect?**

Technical document readers are engineers, technicians, operators, and maintenance personnel who consult the document to perform tasks correctly and safely. They expect:

- **Precision above all** — every measurement, tolerance, and specification must be exactly as the source intended. A single incorrect value can cause equipment damage, safety incidents, or product failure.
- **Consistent terminology** — if a component is called "actuator" on page 5, it must not become "drive" on page 20. Readers rely on term stability to find information quickly.
- **Clarity in procedures** — step-by-step instructions must be unambiguous. Readers should never have to guess the next action or infer a critical safety precaution.
- **Standard conventions** — units, symbols, abbreviations, and formatting follow established engineering standards (ISO, IEC, ANSI). Deviations erode reader confidence.

**What would break their trust?**
- A mistranslated model or part number that leads to ordering the wrong component.
- An incorrect safety warning level (e.g., "Caution" where "DANGER" is required).
- An unconverted or incorrectly converted measurement that causes a fit failure.
- Inconsistent cross-references that send the reader to the wrong section.

## Decision Framework

### 1. Units and Measurements

| Condition | Decision |
|---|---|
| Source contains a measurement with unit | Preserve the exact numerical value; convert unit formatting to English conventions (e.g., space between number and unit). |
| Source uses a non-SI unit | Keep the original unit and value. Do NOT convert to SI unless the client explicitly instructs otherwise in the project brief. |
| Source mixes unit systems (e.g., metric and imperial) | Preserve the mix exactly as in the source. Do not normalize. |
| Temperature is given in Celsius | Keep Celsius. Add Fahrenheit in parentheses only if specified in the project brief. |
| A compound unit appears (e.g., N-m, kg/m^3) | Preserve the unit symbol exactly. Use standard engineering notation per ISO 80000. |

### 2. Safety Warnings (ANSI Z535)

| Condition | Decision |
|---|---|
| Signal word indicates immediate hazard with risk of death/serious injury | Map to **DANGER** (white text on red background implied by markup). |
| Signal word indicates potential hazard with risk of serious injury | Map to **Warning** (black text on orange background implied by markup). |
| Signal word indicates minor/moderate injury risk or property damage | Map to **Caution** (black text on yellow background implied by markup). |
| Source contains a safety symbol or pictogram | Preserve the symbol reference exactly. Translate only the accompanying text. |

### 3. Cross-References

| Condition | Decision |
|---|---|
| Reference to another section by number | Keep the section number exactly as in the source. |
| Reference to another section by name | Translate the section name using consistent terminology. |
| Reference to a figure, table, or diagram | Keep the figure/table number exactly. Translate the caption if present. |
| Page number reference | Preserve the original page number (or target-layout page number if a DTP reflow has occurred). |

### 4. UI Labels and Control Indicators

| Condition | Decision |
|---|---|
| Label on a physical button, switch, or indicator | Translate to the standard English UI term (e.g., "ON/OFF", "STOP", "RESET"). |
| Software UI string embedded in documentation | Translate the string; note in brackets if the software itself is not localized. |
| Label includes a keyboard shortcut | Keep the shortcut key combination exactly. Translate the action description. |

## Error Pattern Library

### Critical Errors (zero tolerance)

| Error | Why It Is Critical |
|---|---|
| **Model/part number changed or mistranslated** | Leads to ordering wrong parts, equipment incompatibility, returns, and delays. |
| **Unit conversion performed without authorization** | Changes the engineering specification; can cause mechanical failure or safety incidents. |
| **Safety level signal word mismatch** | Undermines the hazard communication system; creates legal liability. |
| **Tolerance value altered** | Every tolerance is an engineering requirement. A 0.01 mm change can render a part unusable. |
| **Numerical value modified** | Any change to a dimension, rating, or specification value is unacceptable. |

### Common Errors (frequent in practice)

| Error | Guidance |
|---|---|
| **Inconsistent naming of the same component** | Use a glossary or term base. When in doubt, prefer the first-established term. |
| **Active/passive voice mixing in procedures** | Use imperative mood for instructions ("Press the button"). Use passive voice for descriptions ("The valve is operated by..."). Do not switch between the two in adjacent steps. |
| **Compound unit improperly formatted** | Follow ISO 80000 or ANSI Y14.5M for unit formatting. Use a solidus (/) for division or negative exponents. |
| **Acronym translated instead of preserved** | Industry acronyms (PLC, HMI, CNC, PID) and standard abbreviations (max, min, avg, ref) are international. Keep them in their standard English form. |

### Subtle Errors (easy to miss)

| Error | Guidance |
|---|---|
| **False friends in technical English** | Some English-looking terms have different meanings in technical contexts. Verify every term against a domain glossary. |
| **Decimal comma versus decimal dot** | Some source locales use a decimal comma (e.g., 3,14). Convert to decimal dot for English output: 3.14. |
| **Thousands separator ambiguity** | A space or dot used as a thousands separator in the source must be converted to a comma or removed according to English convention. |
| **Date format ambiguity** | Dates in technical documents (e.g., revision history) must use an unambiguous format: "2025-04-30" or "30 April 2025", never "04/05/2025". |

## Domain-Specific Reference

### Standard Unit Abbreviations

| Quantity | Unit | Abbreviation |
|---|---|---|
| Length | millimeter, centimeter, meter, kilometer | mm, cm, m, km |
| Mass | gram, kilogram, tonne | g, kg, t |
| Volume | liter, milliliter | L, mL |
| Temperature | degree Celsius | degC (or "deg C" in running text) |
| Time | second, minute, hour | s, min, h |
| Electric current | ampere | A |
| Voltage | volt | V |
| Power | watt, kilowatt | W, kW |
| Pressure | bar, pascal, pounds per square inch | bar, Pa, psi |
| Force | newton | N |
| Torque | newton-meter | N-m |
| Frequency | hertz | Hz |
| Rotational speed | revolutions per minute | rpm |

### Standards Bodies

| Acronym | Full Name | Usage |
|---|---|---|
| ISO | International Organization for Standardization | Preserve acronym; translate full name if spelled out |
| IEC | International Electrotechnical Commission | Preserve acronym |
| ANSI | American National Standards Institute | Preserve acronym |
| UL | Underwriters Laboratories | Preserve acronym |
| FCC | Federal Communications Commission | Preserve acronym |
| CE | Conformite Europeenne (European Conformity) | Preserve marking as-is |

### Troubleshooting Table Columns

| Source Label | English Translation |
|---|---|
| Symptom | Symptom |
| Cause | Cause |
| Solution | Solution |
| Error Code | Error Code |
| Possible Reason | Possible Reason |
| Corrective Action | Corrective Action |
