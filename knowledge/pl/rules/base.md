# Polish Language Knowledge Base — Base Rules

> This document defines the canonical Polish-language rules for document translation into Polish.
> All translators and reviewers MUST adhere to these rules unless explicitly overridden by a project style guide.
> Version: 1.0

---

## Table of Contents

1. [Number Format](#1-number-format)
2. [Currency](#2-currency)
3. [Date and Time](#3-date-and-time)
4. [Addresses](#4-addresses)
5. [Proper Nouns](#5-proper-nouns)
6. [Punctuation](#6-punctuation)
7. [Formatting](#7-formatting)
8. [Grammar](#8-grammar)
9. [Formality](#9-formality)
10. [OCR Artifacts](#10-ocr-artifacts)
11. [Translation Philosophy](#11-translation-philosophy)

---

## 1. Number Format

### 1.1 Decimal Separator

Polish uses the **comma** as the decimal separator.

| Correct          | Incorrect        |
|------------------|------------------|
| 3,14             | 3.14             |
| 0,99             | 0.99             |
| 10,5             | 10.5             |
| 1 234,56         | 1,234.56         |

> **Zero-tolerance rule**: Using a period as a decimal separator where a comma is required constitutes a critical error. See scoring-rubric.md.

### 1.2 Thousands Separator

The thousands separator is either a **period** or a **non-breaking space** (preferred in formal/technical texts). Never use a comma.

| Correct               | Incorrect         |
|-----------------------|-------------------|
| 1.000.000            | 1,000,000         |
| 1 000 000 (NBSP)     | 1,000,000         |
| 10.000               | 10,000            |

In contemporary Polish technical and business writing, the non-breaking space is increasingly preferred over the period for thousands separation. Use whichever convention the source document already follows; if none is established, prefer the non-breaking space.

### 1.3 Negative Numbers

The minus sign is placed directly before the digits with no space.

- −5 (use the minus sign U+2212, or a hyphen-minus if unavailable)
- −3,14
- −1.000

When a negative number appears in parentheses or brackets, no extra space is added inside the brackets: (−5).

### 1.4 Percentages

A space separates the number from the percent sign: **5 %**, **100 %**.

In statistical or technical texts, the percent sign may be attached directly to the number only when space is extremely constrained (tables, narrow columns). For all prose text, use the spaced form.

| Correct       | Incorrect     |
|---------------|---------------|
| 5 %           | 5%            |
| 0,5 %         | 0.5%          |
| 100 %         | 100%          |

### 1.5 Ordinal Numbers

Ordinals use a period after the number, followed by a space if a noun follows:

- 1. (pierwszy)
- 2. (drugi)
- 10. (dziesiąty)
- 21. (dwudziesty pierwszy) — no period after 21; the period replaces the word-final ending

When written with digits, ordinals may also use superscript endings in informal contexts, but plain number + period is preferred in formal documents.

### 1.6 Fractions

Fractions are written with a comma (decimal) or as common fractions using a slash:

- 1/2, 3/4, 7/8
- No space before or after the slash in common fractions.

### 1.7 Ranges and Approximations

- Range: 10–20 (using en-dash, no spaces around it)
- Approximate: ok. 50, około 50, ~50
- The word "około" is preferred over "~" in formal texts.

---

## 2. Currency

### 2.1 Polish Zloty (zł)

The symbol **zł** is placed **after** the amount, separated by a space.

| Correct           | Incorrect         |
|-------------------|-------------------|
| 100,00 zł         | zł 100,00         |
| 1.000,50 zł       | 1.000,50zł        |
| 5 zł              | 5zł               |

The full word **zloty** / **złote** / **złotych** is used in running text when the amount is written out:

- Jeden zloty
- Dwa złote
- Pięć złotych
- 100 złotych

The plural forms decline:

| Case         | Singular         | Plural           |
|--------------|------------------|------------------|
| Mianownik    | jeden złoty      | dwa złote        |
| Dopełniacz   | jednego złotego  | pięciu złotych   |
| Celownik     | jednemu złotemu  | pięciu złotym    |
| Biernik      | jeden złoty      | dwa złote        |
| Narzędnik    | jednym złotym    | pięciu złotymi   |
| Miejscownik  | jednym złotym    | pięciu złotych   |

### 2.2 Grosz (Subunit)

- 1 grosz
- 2 grosze
- 5 groszy
- 100,00 zł = 10.000 groszy

Grosz declines similarly: grosza (D.), groszowi (C.), groszem (N.), groszu (Ms.), groszy (D. pl.), groszom (C. pl.), groszami (N. pl.), groszach (Ms. pl.).

### 2.3 Foreign Currencies

The same **amount + space + symbol** rule applies:

| Correct           | Incorrect         |
|-------------------|-------------------|
| 100,00 €          | € 100,00          |
| 50,00 $           | $ 50,00           |
| 200,00 £          | £ 200,00          |

When ISO currency codes are used, place the code **after** the amount:

- 100,00 PLN
- 100,00 USD
- 100,00 EUR
- 100,00 GBP

### 2.4 Currency Names in Text

When writing currency names out in full, follow Polish declension:

- dolar (USD) — dolara, dolarów
- euro (EUR) — indeclinable in Polish ("euro" does not change)
- funt (GBP) — funta, funtów
- jen (JPY) — jena, jenów
- frank (CHF) — franka, franków

### 2.5 Currency Conversion Notes

When a translation involves currency conversion, preserve the original amount and add the Polish zloty equivalent in brackets or parentheses on first mention:

- 500,00 USD (ok. 2.000,00 PLN według kursu z dnia 2026-05-25)

---

## 3. Date and Time

### 3.1 Date Format

Polish uses the **DD.MM.YYYY** format. Leading zeros are required for single-digit days and months.

| Correct         | Incorrect       |
|-----------------|-----------------|
| 01.01.2025      | 01/01/2025      |
| 25.05.2026      | 05/25/2026      |
| 3.04.2024       | 04/03/2024      |

ISO format (YYYY-MM-DD) is acceptable in technical, database, or metadata contexts but DD.MM.YYYY is the standard for Polish documents.

### 3.2 Date Written Out

Month names are written in **lowercase** (except at the start of a sentence or in headings).

| Polish Month | Full Name     |
|--------------|---------------|
| 1            | styczeń       |
| 2            | luty          |
| 3            | marzec        |
| 4            | kwiecień      |
| 5            | maj           |
| 6            | czerwiec      |
| 7            | lipiec        |
| 8            | sierpień      |
| 9            | wrzesień      |
| 10           | październik   |
| 11           | listopad      |
| 12           | grudzień      |

Example: 25 maja 2026 roku / 25 maja 2026 r.

### 3.3 Month Names in Inflection

All month names except **luty** decline. The genitive form is the most common after day numbers.

| Nominative  | Genitive      | Example                      |
|-------------|---------------|------------------------------|
| styczeń     | stycznia      | 1 stycznia 2025 r.           |
| luty        | lutego        | 14 lutego 2025 r.            |
| marzec      | marca         | 21 marca 2025 r.             |
| kwiecień    | kwietnia      | 1 kwietnia 2025 r.           |
| maj         | maja          | 3 maja 2025 r.               |
| czerwiec    | czerwca       | 8 czerwca 2025 r.            |
| lipiec      | lipca         | 15 lipca 2025 r.             |
| sierpień    | sierpnia      | 1 sierpnia 2025 r.           |
| wrzesień    | września      | 1 września 2025 r.           |
| październik | października  | 11 października 2025 r.      |
| listopad    | listopada     | 1 listopada 2025 r.          |
| grudzień    | grudnia       | 25 grudnia 2025 r.           |

Month names appear in the genitive case after numeric day expressions. They take the locative case when preceded by "w" / "we" for months that are not followed by a specific day: "w styczniu", "w lutym", "w marcu".

### 3.4 Day of Week

- poniedziałek, wtorek, środa, czwartek, piątek, sobota, niedziela
- In letters: "W piątek, 25 maja 2026 r."

### 3.5 Time Format

Polish uses the **24-hour clock** in all formal and official writing.

| Correct      | Incorrect    |
|--------------|--------------|
| 14:30        | 2:30 PM      |
| 09:15        | 9:15 AM      |
| 00:00        | 12:00 AM     |
| 23:59        | 11:59 PM     |

The separator is a colon. Do not use a period or a slash. Hours are written with two digits (leading zero preferred) in technical contexts.

### 3.6 Combined Date-Time

- DD.MM.YYYY, godz. HH:MM
- Example: 25.05.2026, godz. 14:30

In formal correspondence, the format "dnia 25 maja 2026 roku o godzinie 14:30" is appropriate.

### 3.7 Duration and Time Periods

- od 10:00 do 12:00
- w dniach 1–5 czerwca 2025 r.
- w okresie od 1 stycznia do 31 grudnia 2025 r.
- kwartalnie (quarterly), półrocznie (semi-annually), rocznie (annually)

### 3.8 Centuries and Decades

- XX wiek / dwudziesty wiek (20th century)
- lata 90. XX wieku (the 1990s)
- w latach 1990–1999
- pierwsza połowa XIX wieku

---

## 4. Addresses

### 4.1 Standard Polish Address Format

Polish addresses follow this order:

```
ul. [nazwa ulicy] [numer budynku/lokalu]
[kod pocztowy] [miejscowość]
[województwo]
```

Example:
```
ul. Marszałkowska 15/3
00-001 Warszawa
woj. mazowieckie
```

### 4.2 Address Components

- **ul.** = ulica (street) — always abbreviated with a period
- **al.** = aleja (avenue) — always abbreviated with a period
- **pl.** = plac (square) — always abbreviated with a period
- **os.** = osiedle (housing estate)
- **Nr** or **nr** = number (apartment/house number) — may be abbreviated or written out

### 4.3 Postal Code Format

Polish postal codes use the format **XX-XXX** (two digits, hyphen, three digits). Always use leading zeros.

| Correct    | Incorrect  |
|------------|------------|
| 00-001     | 00001      |
| 30-001     | 30-1       |
| 50-001     | 50001      |

### 4.4 City and Voivodeship

- City name is always in the nominative case (Warszawa, Kraków, Wrocław)
- Voivodeship (województwo) is written in full or abbreviated as **woj.**
- The 16 Polish voivodeships:
  - dolnośląskie (Wrocław)
  - kujawsko-pomorskie (Toruń/Bydgoszcz)
  - lubelskie (Lublin)
  - lubuskie (Gorzów Wielkopolski/Zielona Góra)
  - łódzkie (Łódź)
  - małopolskie (Kraków)
  - mazowieckie (Warszawa)
  - opolskie (Opole)
  - podkarpackie (Rzeszów)
  - podlaskie (Białystok)
  - pomorskie (Gdańsk)
  - śląskie (Katowice)
  - świętokrzyskie (Kielce)
  - warmińsko-mazurskie (Olsztyn)
  - wielkopolskie (Poznań)
  - zachodniopomorskie (Szczecin)

### 4.5 International Addresses

When translating addresses from non-Polish sources, follow the local format of the source country but add the country name in Polish at the end:

```
ul. Baker Street 221B
Londyn
Wielka Brytania
```

For addresses that are kept in the original language within a Polish text, add [adres oryginalny] as a note if necessary.

### 4.6 Address Prepositions

When referring to locations:

- na ulicy / przy ulicy — "at/on the street" (locative)
- pod adresem — "at the address"
- w Warszawie — "in Warsaw" (locative)
- na Mokotowie — "in Mokotów" (district, locative)

---

## 5. Proper Nouns

### 5.1 Polish Diacritics

Polish uses the following diacritic characters. They MUST be preserved in all Polish text. Omitting diacritics changes meaning and is considered an error.

| Letter | Example                           |
|--------|-----------------------------------|
| ą      | książka, sąd, będą               |
| ć      | ćma, płeć                        |
| ę      | język, mięso, będą               |
| ł      | ławka, szkoła, Łódź              |
| ń      | koń, słońce, państwo             |
| ó      | ósmy, król, córka                |
| ś      | środa, śnieg, ślub               |
| ź      | źle, źrebak, jeździć             |
| ż      | żona, żółty, każdy               |

Capital diacritics: Ą, Ć, Ę, Ł, Ń, Ó, Ś, Ź, Ż.

> **Zero-tolerance rule**: Systematically dropping or misrepresenting Polish diacritics is a critical error.

### 5.2 Foreign Name Transcription

Foreign names (personal names, place names, brands) follow established Polish transcription conventions where a traditional Polish form exists:

**Personal names:**

| Source        | Polish Form        |
|---------------|--------------------|
| Shakespeare   | Szekspir           |
| Newton        | Newton (unchanged) |
| Washington    | Waszyngton (city) / Washington (person/surname) |
| London        | Londyn             |
| Paris         | Paryż              |
| New York      | Nowy Jork          |
| Los Angeles   | Los Angeles        |
| Chicago       | Chicago            |

**Guidelines:**
- If a well-established Polish exonym exists, use it (Londyn, Paryż, Rzym, Nowy Jork).
- If no established Polish form exists, preserve the original spelling.
- Modern surnames of living persons are generally NOT translated. Preserve the original spelling.
- Royal names and historical figures may have Polish forms: William Zdobywca (William the Conqueror), Karol Wielki (Charlemagne).

### 5.3 Company Forms

Polish legal entity forms are appended to company names:

| Abbreviation | Full Form                          |
|--------------|------------------------------------|
| Sp. z o.o.   | Spółka z ograniczoną odpowiedzialnością      |
| S.A.         | Spółka Akcyjna                     |
| Sp. j.       | Spółka Jawna                       |
| Sp. k.       | Spółka Komandytowa                 |
| Sp. z o.o. Sp. k. | Spółka z o.o. Spółka Komandytowa |
| P.P.U.H.     | Przedsiębiorstwo Produkcyjno-Usługowo-Handlowe |
| Fundacja     | Fundacja [name]                    |
| Stowarzyszenie | Stowarzyszenie [name]            |

Foreign equivalents (LLC, Ltd., Inc., GmbH, SAS, S.r.l.) are either:
- Translated to the closest Polish equivalent (recommended for Polish audiences), or
- Preserved in the original form with the Polish equivalent in parentheses on first use.

### 5.4 Geographical Names

- Continents, countries, and cities are capitalized (Europa, Polska, Warszawa).
- Adjectives derived from proper names are lowercase unless part of a proper name:
  - polski, niemiecki, francuski
  - Morze Bałtyckie (the Baltic Sea — proper name)
  - województwo mazowieckie (proper name but lowercase for the adjective)

### 5.5 Institutional Names

Official names of Polish institutions retain their original capitalization:
- Ministerstwo Finansów
- Główny Urząd Statystyczny
- Sąd Najwyższy
- Uniwersytet Warszawski
- Narodowy Bank Polski

When translating foreign institutional names, use the official Polish translation if one exists. For institutions without a Polish equivalent, provide a descriptive translation in brackets on first mention.

---

## 6. Punctuation

### 6.1 Quotation Marks

Polish uses **„..."** (low-high, also called przecinkowe/otwórz-zamknij) as the primary quotation marks. The opening mark is the lower double quotation mark „ (U+201E), and the closing mark is the regular upper double quotation mark " (U+201D).

| Correct                                          | Incorrect                                |
|--------------------------------------------------|------------------------------------------|
| „To jest cytat."                                 | "To jest cytat."                         |
| Powiedział: „Idziemy dziś do kina."              | Powiedział: "Idziemy dziś do kina."      |

**Nested quotes:** Use « » (angle quotes, U+00AB and U+00BB) for quotes within quotes, or switch to guillemets for the outer level and low-high for the inner level.

„Autor stwierdził: «To jest cytat w cytacie» – dodał."

**Guillemets** (» «) are also acceptable in Polish, particularly in typographically sophisticated publications, but the low-high quotation marks are the standard for general use.

Secondary quotation marks (for quotes within quotes): « » (angle quotation marks).

### 6.2 Em Dash / Myślnik

Polish uses the **em dash** (—, U+2014) as the primary dash. It is always surrounded by spaces.

| Correct                        | Incorrect                |
|--------------------------------|--------------------------|
| To — jak powiedział — jest ważne. | To —jak powiedział—jest ważne. |
| — To prawda — odparł.          | - To prawda - odparł.    |

Do not confuse the em dash with the hyphen (-, U+002D) or the en dash (–, U+2013).

- **Em dash (—):** Dialogue, parenthetical inserts, emphasis — spaced on both sides.
- **En dash (–):** Number ranges (10–20), connections (Warszawa–Londyn) — no spaces around it.
- **Hyphen (-):** Compound words (czarno-biały, anglo-polski) — no spaces around it.

### 6.3 Comma Rules

**General rule:** Commas separate clauses and list items, following the same general principles as other European languages.

**Key distinction:** Polish does NOT place a comma before **że** (that), **iż** (that), **aż** (until/when), **niż** (than), **jak** (as), or **ani** (nor) when they introduce a subordinate clause, if they begin the clause directly.

| Correct                                              | Incorrect                                   |
|------------------------------------------------------|---------------------------------------------|
| Myślę, że to prawda.                                 | Myślę, że, to prawda.                       |
| Jest wyższy niż myślałem.                            | Jest wyższy, niż myślałem.                  |
| Powiedział, iż przyjdzie.                            | Powiedział, iż, przyjdzie.                  |

However, commas ARE used before these conjunctions when they appear in compound sentences where the conjunction follows another clause element:

- Powiedział, że przyjdzie, ale się spóźni. (comma before "ale")
- Nie wiem, czy to zrobi, ani czy chce. (comma before "ani" in a compound structure)

Comma is used before **który** (which/who) and **gdzie** (where) when introducing a relative clause:

- To jest książka, którą czytałem.
- To jest miasto, gdzie się urodziłem.

### 6.4 Period

- Period ends declarative sentences.
- Abbreviations: dr (doktor), mgr (magister), prof. (profesor), itd. (i tak dalej), itp. (i tym podobne).
- When an abbreviation ends a sentence, one period suffices.

### 6.5 Colon and Semicolon

- **Colon (:)** Introduces lists, explanations, quotations. No space before, one space after.
- **Semicolon (;)** Separates complex list items or closely related clauses. No space before, one space after.

### 6.6 Ellipsis

Polish uses the ellipsis (..., U+2026) with no space before it in interrupted speech, but with a space before it when it indicates omitted text:

- Powiedział: „Przyszedłem, zobaczyłem..."
- To jest fragment tekstu ... i tutaj coś pominięto.

Three dots only; no more.

### 6.7 Parentheses and Brackets

- Round parentheses () are standard for asides and clarifications.
- Square brackets [] are used for editorial insertions, corrections, or OCR restorations (see Section 10).
- No space before the opening parenthesis/bracket; a space after the closing one (unless followed by punctuation).

### 6.8 Capitalization After Punctuation

- After a period, a new sentence begins with a capital letter.
- After a colon, the following text starts with a lowercase letter unless it is a proper noun, a complete quotation, or several full sentences.
- After an em dash introducing dialogue, the first word is capitalized.

---

## 7. Formatting

### 7.1 Title Capitalization

Polish uses **sentence-style capitalization** for titles. Only the first word and proper nouns are capitalized. This applies to:
- Book titles
- Article titles
- Chapter headings
- Section headings
- Film and play titles
- Song titles

| Correct (PL)                               | Incorrect (PL)                        |
|---------------------------------------------|---------------------------------------|
| Pan Tadeusz, czyli ostatni zajazd na Litwie | Pan Tadeusz, Czyli Ostatni Zajazd Na Litwie |
| Sto lat samotności                          | Sto Lat Samotności                    |
| W pustyni i w puszczy                       | W Pustyni I W Puszczy                 |

**Exception:** Proper nouns (names of people, places, institutions) within titles are capitalized normally.

### 7.2 Heading Hierarchy

Use a consistent hierarchy:

```
# Rozdział 1 (Heading 1)
## 1.1 Sekcja (Heading 2)
### 1.1.1 Podsekcja (Heading 3)
```

Headings are not followed by a period. They may be bold but should not use all-caps for emphasis.

### 7.3 Lists

**Unordered lists** use the en dash or bullet (consistent throughout the document):

- Pierwszy element
- Drugi element
  - Podpunkt
  - Podpunkt

**Ordered lists** use Arabic numerals followed by a period:

1. Pierwszy krok
2. Drugi krok
   2.1. Podkrok
   2.2. Podkrok

**List punctuation:**
- If list items are single words or short phrases, no period at the end.
- If list items are full sentences, each ends with a period.
- If list items complete the introductory sentence, the last item ends with a period and intermediate items end with semicolons or commas.

### 7.4 Tables

- Polish table headers use sentence-style capitalization.
- Numerical columns are right-aligned; text columns are left-aligned.
- Decimal numbers in tables must use commas (Section 1.1).
- Table footnotes are placed below the table, marked with superscript letters or asterisks.

### 7.5 Bold and Italic

- **Bold** for headings, emphasis, key terms.
- *Italic* for foreign words, titles (in running text), and emphasis.
- Underlining is avoided in formal texts (reserved for hyperlinks).

### 7.6 Abbreviations and Acronyms

On first use, write the full form followed by the abbreviation in parentheses:

- Polska Akademia Nauk (PAN)
- Złoty (PLN)

Common Polish abbreviations:

| Abbreviation | Full Form                                       |
|--------------|-------------------------------------------------|
| itd.         | i tak dalej                                     |
| itp.         | i tym podobne                                   |
| np.          | na przykład                                     |
| tzw.         | tak zwany / tak zwana / tak zwane               |
| tj.          | to jest                                         |
| ok.          | około                                           |
| ww.          | wyżej wymieniony / wyżej wymieniona / wyżej wymienione |
| r.           | rok                                             |
| godz.        | godzina                                         |
| nr           | numer                                           |
| pkt           | punkt                                           |

### 7.7 Spacing After Periods

Polish typography uses a single space after periods, not double spacing.

### 7.8 Page Numbers and Footers

- Page numbers: standard Arabic numerals, centered or right-aligned.
- Footers may include page X of Y format: Strona 1 z 10.
- Footnotes are numbered consecutively throughout the document.

---

## 8. Grammar

### 8.1 Word Order (SVO — Flexible)

Polish is an **SVO** (Subject-Verb-Object) language with flexible word order due to its case system. The neutral order is:

| Subject | Verb   | Object       |
|---------|--------|--------------|
| Jan     | czyta  | książkę.     |

Emphasis can shift order:

- **SVO:** Jan czyta książkę. (neutral)
- **OVS:** Książkę czyta Jan. (emphasizes that it's Jan who is reading the book)
- **VSO:** Czyta Jan książkę. (emphasizes the action)

### 8.2 The Seven Cases

Polish has seven grammatical cases. Every noun, adjective, pronoun, and numeral declines.

| Case (Polish)        | Case (English) | Example (pies) | Function                                |
|----------------------|----------------|----------------|-----------------------------------------|
| Mianownik (M.)       | Nominative     | pies           | Subject                                 |
| Dopełniacz (D.)      | Genitive       | psa            | Possession, negation, after certain prepositions |
| Celownik (C.)        | Dative         | psu            | Indirect object                         |
| Biernik (B.)         | Accusative     | psa            | Direct object (animate)                 |
| Narzędnik (N.)       | Instrumental   | psem           | With, by means of                       |
| Miejscownik (Ms.)    | Locative       | psie           | Location (after certain prepositions)   |
| Wołacz (W.)          | Vocative       | psie!          | Direct address                          |

**Critical for translation:** The case system means that prepositions govern specific cases. For example:

- **w** (in) + Miejscownik (locative): w Warszawie, w domu
- **na** (on) + Miejscownik: na stole, na ulicy
- **do** (to) + Dopełniacz (genitive): do Polski, do sklepu
- **z** (with) + Narzędnik (instrumental): z przyjacielem
- **o** (about) + Miejscownik: o książce

Negation always triggers the genitive case for the direct object:

- Mam książkę. (I have a book — accusative)
- Nie mam książki. (I don't have a book — genitive)

### 8.3 Gender

Polish has three genders in the singular:

| Gender | Example     | Adjective Ending |
|--------|-------------|------------------|
| Masculine (męski) | dobry pies    | -y / -i         |
| Feminine (żeński) | dobra książka | -a               |
| Neuter (nijaki)   | dobre dziecko | -e               |

In the plural, there is a distinction between:
- **Męskoosobowy** (masculine personal): dobrzy mężczyźni (good men)
- **Żeńsko-rzeczowy** / **niemęskoosobowy** (non-masculine personal): dobre kobiety, dobre psy

This affects adjectives, pronouns, and past-tense verb forms.

### 8.4 Verb Aspect (Perfective / Imperfective)

Every Polish verb exists in one of two aspects. This is a **critical** concept for translation; choosing the wrong aspect changes the meaning.

| Aspect        | Polish Term     | Meaning                                                  |
|---------------|-----------------|----------------------------------------------------------|
| Imperfective  | Niedokonany     | Ongoing, habitual, repeated, or incomplete action        |
| Perfective    | Dokonany        | Completed, single, or result-focused action              |

**Examples:**

| Imperfective (NDK)     | Perfective (DK)        |
|------------------------|------------------------|
| czytać (to read)       | przeczytać (to read through/completely) |
| pisać (to write)       | napisać (to write/compose)  |
| robić (to do)          | zrobić (to do/accomplish)  |
| jeść (to eat)          | zjeść (to eat up)          |

**Translation guidance:**
- If the source (e.g., English simple present) expresses habit or general truth, use **imperfective**.
- If the source expresses a single completed action (e.g., English present perfect or simple past with a result), consider **perfective**.
- Continuous/progressive forms (English -ing) typically map to **imperfective**.
- Negation of perfective verbs often implies the action didn't happen at all; negation of imperfective implies the action was not in progress.

### 8.5 Verb Conjugation

Polish verbs conjugate by person and number. There are three main conjugation classes.

**Conjugation I (-ę, -esz):** e.g., *pisać* (to write)

| Person | Singular | Plural   |
|--------|----------|----------|
| ja     | piszę    | piszemy  |
| ty     | piszesz  | piszecie |
| on/ona/ono | pisze  | piszą    |

**Conjugation II (-ę, -isz/-ysz):** e.g., *robić* (to do)

| Person | Singular | Plural   |
|--------|----------|----------|
| ja     | robię    | robimy   |
| ty     | robisz   | robicie  |
| on/ona/ono | robi  | robią    |

**Conjugation III (-am, -asz):** e.g., *czytać* (to read)

| Person | Singular | Plural   |
|--------|----------|----------|
| ja     | czytam   | czytamy  |
| ty     | czytasz  | czytacie |
| on/ona/ono | czyta | czytają |

Past tense verbs agree with the subject in gender:

| Gender   | Singular ("I read") | Plural ("we read") |
|----------|----------------------|---------------------|
| Masculine | czytałem            | czytaliśmy          |
| Feminine  | czytałam            | czytałyśmy          |
| Neuter    | czytałom            | (not typical)       |

### 8.6 Adjectives

Adjectives agree with nouns in case, number, and gender.

- dobry pies (M. lp, masculine)
- dobra książka (M. lp, feminine)
- dobre dziecko (M. lp, neuter)
- dobrzy ludzie (M. lm, masculine personal)
- dobre rzeczy (M. lm, non-masculine personal)

Adjectives precede the noun in neutral word order: *dobry człowiek* (a good person).

### 8.7 Prepositions

Key prepositions and their cases:

| Preposition | Case          | Example                          |
|-------------|---------------|----------------------------------|
| w           | Locative      | w domu / w Warszawie             |
| na          | Locative      | na stole / na ulicy              |
| do          | Genitive      | do Polski / do domu              |
| dla         | Genitive      | dla ciebie / dla mnie            |
| bez         | Genitive      | bez problemu                     |
| z           | Genitive      | z Polski (from Poland)           |
| z           | Instrumental  | z przyjacielem (with a friend)   |
| o           | Locative      | o książce (about a book)         |
| o           | Accusative    | o piątej (at five o'clock)       |
| przy        | Locative      | przy stole (by/near the table)   |
| przed       | Instrumental  | przed domem (in front of the house) |
| nad         | Instrumental  | nad morzem (above/at the sea)    |
| pod         | Instrumental  | pod stołem (under the table)     |
| między      | Instrumental  | między nami (between us)         |

### 8.8 Numerals and Agreement

Polish numerals govern the case of the noun that follows:

- **1:** Mianownik lp — jeden pies
- **2, 3, 4:** Mianownik lm — dwa psy, trzy psy, cztery psy
- **5+:** Dopełniacz lm — pięć psów, dziesięć psów
- **21:** Mianownik lp — dwadzieścia jeden psów (but "jeden" takes M. lp)
- **22, 23, 24:** Mianownik lm — dwadzieścia dwa psy

Collective numerals (dwoje, troje, czworo...) are used for mixed-gender groups and children: dwoje dzieci, troje studentów.

### 8.9 Negation

Double negation is **standard** and **required** in Polish:

| Polish (correct)                          | English (literal)                    |
|-------------------------------------------|--------------------------------------|
| Nigdy nic nie mówi.                       | Never nothing doesn't say. = He never says anything. |
| Nikt nie przyszedł.                       | Nobody didn't come. = Nobody came.   |
| Nic nie widzę.                            | Nothing I don't see. = I don't see anything. |

Each negative element (nikt, nic, nigdy, nigdzie, żaden) requires the **nie** particle before the verb.

---

## 9. Formality

### 9.1 Pan / Pani vs. ty

Polish has a grammatical distinction between formal and informal address. This is one of the most important sociolinguistic features of the language.

| Form        | Usage                                           | Verb Form   |
|-------------|--------------------------------------------------|-------------|
| ty          | Family, close friends, children, informal settings | 2nd person singular |
| Pan         | Formal address to a man                          | 3rd person singular |
| Pani        | Formal address to a woman                        | 3rd person singular |
| Państwo     | Formal address to a mixed or unknown group       | 3rd person plural |

**Examples:**

- Informal: "Czy **masz** długopis?" (Do you have a pen?)
- Formal (to a man): "Czy **ma Pan** długopis?"
- Formal (to a woman): "Czy **ma Pani** długopis?"
- Formal (to a group): "Czy **mają Państwo** długopis?"

> **Zero-tolerance rule**: Using "ty" verb forms where "Pan"/"Pani" is required in a formal document constitutes a critical error. This includes using 2nd person singular imperatives (e.g., "zrób" instead of "niech Pan zrobi").

### 9.2 Formal Correspondence

**Salutations and openings:**

| Context                           | Salutation                              |
|-----------------------------------|-----------------------------------------|
| Formal, recipient named (man)     | Szanowny Panie [Nazwisko]               |
| Formal, recipient named (woman)   | Szanowna Pani [Nazwisko]                |
| Formal, unnamed (man)             | Szanowny Panie!                         |
| Formal, unnamed (woman)           | Szanowna Pani!                          |
| General / Dear Sirs               | Szanowni Państwo!                       |
| Less formal, known recipient      | Drogi Panie / Droga Pani                |
| Official/institutional            | Szanowni Państwo,                       |

**Common opening phrases:**

- W związku z Państwa pismem z dnia...
- Odpowiadając na Państwa zapytanie...
- W nawiązaniu do naszej rozmowy...
- Uprzejmie informuję, że...
- Niniejszym potwierdzam otrzymanie...

**Closings:**

| Context                 | Closing                                   |
|-------------------------|-------------------------------------------|
| Standard formal         | Z poważaniem                              |
| Less formal             | Z wyrazami szacunku                       |
| Warm but professional   | Łączę wyrazy szacunku                     |
| Very formal             | Z głębokim szacunkiem                     |
| Business                | Z wyrazami szacunku                       |
| To a superior           | Z poważaniem / Z wyrazami szacunku        |

**Date in letters:**

- Warszawa, dnia 25 maja 2026 roku
- Warszawa, 25.05.2026 r.

### 9.3 Honorifics and Titles

In formal address, titles and academic degrees are used:

| Title    | Address Form                                  |
|----------|-----------------------------------------------|
| dr       | Szanowny Panie Doktorze / Szanowna Pani Doktor |
| prof.    | Szanowny Panie Profesorze / Szanowna Pani Profesor |
| mgr      | Szanowny Panie Magistrze / Szanowna Pani Magister |
| inż.     | Szanowny Panie Inżynierze / Szanowna Pani Inżynier |

Titles are generally declined (vocative case for direct address). In written correspondence, the vocative is used in the salutation.

### 9.4 Register Markers for Translation

When translating, determine the register of the source document and match it:

| Source Register | Polish Equivalent        | Key Markers                                    |
|-----------------|--------------------------|------------------------------------------------|
| Formal/Legal    | Formalny/prawny          | Pan/Pani, passive voice, specialized lexicon  |
| Business        | Biznesowy                | Pan/Pani, standard professional phrases       |
| Semi-formal     | Półformalny              | Pan/Pani, simpler structures                   |
| Informal        | Nieformalny              | ty forms, colloquial vocabulary                |
| Casual          | Potoczny                 | ty forms, slang, shortened forms               |

Register must remain consistent throughout the document. A shift from formal to informal mid-document is an error unless the source itself shifts register.

---

## 10. OCR Artifacts

### 10.1 Marking Recovered Text

When translating from a scanned document or OCR output where some text needed to be inferred or reconstructed, mark the restored content using the following convention:

```
[przywrócono: ...]
```

Examples:

- Original OCR: "Przychody netto ze sprzeda*y"
- Restored: "Przychody netto ze sprzeda[przywrócono: ży]"
- Original OCR: "zosta* złożony"
- Restored: "zosta[przywrócono: ł] złożony"

### 10.2 Unreadable Characters

For characters that are completely illegible and cannot be reconstructed, mark as:

```
[nierozpoznano]
```

If the approximate number of missing characters is known:

```
[nierozpoznano: ~3 znaki]
```

These markers are used ONLY in the translation output when the source text is itself a degraded scan or low-quality OCR. In normal translation from clean text, these markers are not needed.

### 10.3 Uncertain Transcription

When the transcription is uncertain, mark with:

```
[niejasne: proponowane odczytanie]
```

Example: C++ could be ambiguous in a poor scan → C[niejasne: ++] lub C[niejasne: #]

### 10.4 Reconstructed Page Breaks

When page breaks in the original are ambiguous, mark:

```
[przywrocono: nowa strona]
```

### 10.5 Handling OCR Artifacts in Translation

- OCR artifacts present in the original (extraneous characters, garbled text that is nonetheless readable) should be marked with **[błąd OCR]** if they cannot be resolved.
- If the OCR error is clearly identifiable (e.g., "r" instead of "n"), correct it silently and use **[przywrócono: ...]** for the corrected portion.

### 10.6 Image-Based or Low-Quality Source

For images within documents (diagrams, logos, handwritten text) that could not be OCR'd, use:

```
[obraz: treść niedostępna — opis w języku źródłowym: ...]
```

When possible, provide the original text from the image.

---

## 11. Translation Philosophy

### 11.1 Natural Polish Expression

The primary goal is to produce **natural-sounding Polish** that a native speaker would recognize as idiomatic. Avoid:

- **Calques** (literal translations of source-language structures that are unnatural in Polish):
  - EN: "It is important to note that..."
  - EN calque: "Jest ważne, aby zauważyć, że..." (unnatural)
  - Natural PL: "Należy zauważyć, że..." or "Warto podkreślić, że..."

- **False friends**:
  - EN: "eventually" → PL: "ostatecznie" (not "ewentualnie," which means "possibly")
  - EN: "actually" → PL: "tak naprawdę" (not "aktualnie," which means "currently")
  - EN: "sensible" → PL: "rozsądny" (not "sensowny," which means "meaningful")
  - EN: "sympathetic" → PL: "współczujący" (not "sympatyczny," which means "likable")

- **Preposition mismatches:** Polish prepositions often do not map one-to-one with English:
  - EN: "wait for" → PL: "czekać na" (+ Biernik), not "czekać dla"
  - EN: "think about" → PL: "myśleć o" (+ Miejscownik), not "myśleć około"
  - EN: "depend on" → PL: "zależeć od" (+ Dopełniacz), not "zależeć na"

### 11.2 Case System Accuracy

The Polish case system is the backbone of grammatical correctness. Every preposition, verb, and noun relationship must be checked for the correct case assignment.

**High-risk constructions:**
- After numbers 5+ (Dopełniacz required)
- After negation (Dopełniacz for direct objects)
- After prepositions (each governs specific cases — see Section 8.2)
- After comparative structures (niż + Mianownik, but careful with case governors)

**Case-checking workflow for translators:**
1. Identify the governing element (verb, preposition, numeral).
2. Determine the required case.
3. Apply correct endings to all declined elements (noun, adjective, pronoun, numeral).
4. Verify agreement across the noun phrase.

### 11.3 Aspectual Verb Choice

Selecting the correct verb aspect (perfective vs. imperfective) is essential and can be one of the hardest tasks for non-native translators.

**Decision framework:**

| Source Meaning                                                   | Polish Aspect |
|------------------------------------------------------------------|---------------|
| Habitual action ("I go to work every day")                       | Imperfective  |
| Action in progress ("I am reading")                              | Imperfective  |
| General statement ("Water boils at 100 degrees")                 | Imperfective  |
| Completed action ("I read the book")                             | Perfective    |
| Single occurrence ("I called him yesterday")                     | Perfective    |
| Resultative ("I have finished")                                  | Perfective    |
| Repeated/habitual in the past ("I used to go")                   | Imperfective  |
| Sudden change of state ("He realized")                           | Perfective    |
| Inception ("He started to...")                                   | Perfective (zacz±ć + infinitive) |
| Duration ("He kept reading")                                     | Imperfective  |

### 11.4 Sentence Structure Adaptation

English (and other source languages) may use structures that do not exist in Polish. These MUST be restructured:

- **English passive voice** is less common in Polish. Alternatives:
  - Reflexive passive: "To się robi..." (This is done...)
  - Impersonal: "Zrobiono..." (One did... / It was done...)
  - Active rephrasing: "Zrobiliśmy..." (We did...)

- **English gerunds** (-ing forms) often require a clause in Polish:
  - EN: "After finishing the report..."
  - PL: "Po ukończeniu raportu..." (gerund-like, using the noun form)
  - Or: "Kiedy skończyliśmy raport..." (finite clause)

- **English present perfect** has no direct equivalent in Polish. Use:
  - Present tense for continuing situations: "Mieszkam tu od 5 lat." (I have lived here for 5 years.)
  - Past tense (perfective) for completed actions: "Przeczytałem tę książkę." (I have read this book.)

- **English relative clauses** with prepositions at the end:
  - EN: "the person I was talking to" → PL: "osoba, z którą rozmawiałem" (preposition fronted before the relative pronoun)

### 11.5 Terminology Consistency

Within a single document, equivalent terms from the source language must be translated consistently. Do not use multiple Polish synonyms for the same source term unless the context genuinely requires it.

- Maintain a **terminology glossary** for each project.
- For ambiguous source terms, determine the correct Polish domain-specific equivalent (legal, medical, technical, financial) and stick with it.
- When multiple translations are possible, choose the one that is most widely accepted in the target domain.

### 11.6 Handling Ambiguity

When the source text is ambiguous, prefer:
1. The interpretation that is most natural in Polish.
2. A neutral rendering that preserves the ambiguity if it is intentional.
3. A footnote explaining the ambiguity if it is critical to meaning.

### 11.7 Fidelity to Meaning, Not Form

The translation should be faithful to the **meaning** of the source, not its surface structure. This means:

- Breaking long English sentences into shorter Polish sentences where needed.
- Combining short choppy sentences where Polish prefers subordination.
- Reordering information to follow Polish information structure (topic–comment).
- Adjusting paragraph breaks to match Polish discourse conventions.

### 11.8 Cultural Adaptation

- Measure: Translate to metric system (km, kg, °C) unless the original non-metric measurement is known to the Polish audience (e.g., inches in screen sizes).
- Proper names of cultural events, holidays, and institutions: use Polish equivalents where established.
- Legal references: adapt to Polish equivalents where a close match exists, or provide explanatory notes.
- Humor, idioms, and wordplay: prioritize equivalent effect over literal translation. Find a Polish idiom with the same function, not a calque of the source idiom.

### 11.9 Quality Checklist for Translation Output

Each translated segment should be checked against:

- [ ] Decimal commas used correctly, no decimal periods except in ISO contexts
- [ ] Polish quotation marks used („...")
- [ ] Sentence-style capitalization in titles
- [ ] Pan/Pani vs. ty matches source register
- [ ] Verb aspect (perfective/imperfective) correctly chosen
- [ ] Cases correctly assigned after prepositions and numerals
- [ ] Double negation applied where needed
- [ ] Month names in genitive case after day numbers
- [ ] DD.MM.YYYY date format
- [ ] zł placed after amount with space
- [ ] Diacritics present and correct
- [ ] False friends avoided
- [ ] Passive voice restructured as needed
- [ ] Terminology consistent with glossary

---

*This document is maintained as part of the Polish language knowledge base for the translating-documents skill. Updates should be reviewed by a Polish language expert before publication.*
