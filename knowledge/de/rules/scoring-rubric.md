---
id: de/rules/scoring-rubric
type: rules
target_lang: de
---

# Scoring-Rubrik fur deutsche Ubersetzungen (de-DE)

## Bewertungssystem

Jede Dimension wird auf einer 6-stufigen Skala bewertet (100 / 90 / 80 / 70 / 60 / <50). Die gewichteten Punktzahlen werden summiert, um die Gesamtbewertung zu ermitteln.

### Bander (Scoring Bands)

| Band | Bedeutung | Schwellenwert |
|------|-----------|---------------|
| 100 | Perfekt -- keine Mangel | > 95 % |
| 90 | Exzellent -- minimale, vernachlassigbare Mangel | > 85 % |
| 80 | Gut -- leichte Mangel, leicht korrigierbar | > 75 % |
| 70 | Befriedigend -- mehrere Mangel, Uberarbeitung empfohlen | > 65 % |
| 60 | Ausreichend -- grundlegende Uberarbeitung notig | > 55 % |
| <50 | Mangelhaft -- vollstandige Neuubersetzung erforderlich | <= 55 % |

### Gewichtungen

| # | Dimension | Gewichtung |
|---|-----------|-----------|
| 1 | Zahlen- und Wahrungsgenauigkeit (Numerical Accuracy) | **30 %** |
| 2 | Terminologiekonsistenz (Terminology Consistency) | **20 %** |
| 3 | Semantische Treue (Semantic Fidelity) | **25 %** |
| 4 | Formatkonformitat (Format Compliance) | **10 %** |
| 5 | Vollstandigkeit (Completeness) | **10 %** |
| 6 | OCR-Qualitat / Inferenz (Inference & OCR Quality) | **5 %** |

**Gesamtpunktzahl (0 -- 100)** = gewichtete Summe aller sechs Dimensionen.

---

## Null-Toleranz-Regeln (Zero-Tolerance Items)

Die folgenden Fehler fuhren **automatisch** zu einer Ho chstbewertung von **maximal 60 Punkten** in der Gesamtbewertung, unabhangig von der Qualitat der ubrigen Dimensionen:

| Fehler | Beispiel (falsch) | Korrekt |
|--------|-------------------|---------|
| Datumsformat MM/DD statt TT.MM.JJJJ | `05/24/2026` | `24.05.2026` |
| Dezimalkomma als Punkt geschrieben | `3.14` | `3,14` |
| Tausendertrennzeichen als Komma | `1,000` | `1.000` |
| Falsche Sie/du-Verwendung | `Sie` in informellem Kontext oder `du` in formellem Kontext | Dem Register entsprechend |
| Wechsel zwischen Sie und du ohne Kontextwechsel | `Sie haben ... du hast ...` | Einheitlich Sie oder du |

### Globale Regel
- **Jeder kritische Null-Toleranz-Fehler** -> Gesamtbewertung auf **maximal 60** begrenzt.
- Bei **mehr als einem** Null-Toleranz-Fehler -> Gesamtbewertung **< 50** (Mangelhaft).

---

## Dimension 1: Zahlen- und Wahrungsgenauigkeit (Numerical Accuracy) -- 30 %

### Pruffragen
- Wird das **Dezimalkomma** (`,`) korrekt statt des Dezimalpunkts verwendet?
- Werden **Tausenderpunkte** (`.`) korrekt statt Kommas gesetzt?
- Steht das **Euro-Zeichen** nach dem Betrag mit Leerzeichen? (`12,50 €`)
- Werden **Datumsangaben** im Format TT.MM.JJJJ geschrieben?
- Werden **Uhrzeiten** im 24-Stunden-Format mit Doppelpunkt angegeben?
- Werden **Prozentangaben** mit Leerzeichen gesetzt? (`12,5 %`)
- Sind **Maßeinheiten** korrekt formatiert (Leerzeichen, keine Punkte)?

| Band | Kriterium |
|------|-----------|
| 100 | Alle Zahlen, Wahrungen, Daten und Uhrzeiten entsprechen zu 100 % den de-DE-Konventionen. Keine Abweichungen. |
| 90 | 1 minimale Abweichung (z. B. fehlendes Leerzeichen vor € in einem Fall, oder fehlende führende Null bei einstelligem Monat). |
| 80 | 2--3 Formatabweichungen, aber keine systematischen Fehler. Der Gesamteindruck ist noch deutsch. |
| 70 | 4--5 Formatfehler oder 1 systematischer Fehler (z. B. durchgangig Tausenderkomma statt -punkt). |
| 60 | Systematische Fehler in mehreren Kategorien. Mehrere Datums- oder Zahlenformate falsch. |
| <50 | Ausgangsformat vollstandig beibehalten (z. B. englisches Zahlenformat im gesamten deutschen Text). Keinerlei Anpassung. |

**Hinweis**: Aufgrund der Null-Toleranz-Regel (siehe oben) fuhrt bereits ein einziger Dezimalkomma/Dezimalpunkt-Fehler zu einer maximalen Gesamtbewertung von 60.

---

## Dimension 2: Terminologiekonsistenz (Terminology Consistency) -- 20 %

### Pruffragen
- Sind **Fachbegriffe** im gesamten Dokument konsistent ubersetzt?
- Werden **Eigennamen** korrekt beibehalten (nicht ubersetzt)?
- Werden etablierte **deutsche Exonyme** verwendet? (Munchen, Rom, Wien, Venedig)
- Werden **False Friends** vermieden? (z. B. `bekommen` = receive, nicht `become`)
- Sind **Komposita** korrekt gebildet?
- Ist die **Terminologie** mit eventuell vorhandenen Glossaren abgestimmt?

| Band | Kriterium |
|------|-----------|
| 100 | Terminologie absolut konsistent, Eigennamen korrekt, Fachbegriffe prazise, keine False Friends. |
| 90 | 1 terminologische Unscharfe (z. B. ein einmalig inkonsistenter Begriff oder ein ubersetzter Eigenname, der besser im Original geblieben ware). |
| 80 | 2--3 terminologische Abweichungen (z. B. zwei False Friends oder zwei inkonsistente Fachbegriffe). |
| 70 | Mehrere terminologische Fehler (4--5): False Friends, inkonsistente Fachbegriffe, ubersetzte Markennamen. |
| 60 | Systematische terminologische Probleme: False Friends durchgangig falsch, Eigennamen ubersetzt, Fachtermini unzuverlassig. |
| <50 | Terminologie vollstandig falsch oder ausgangssprachlich belassen ohne Anpassung. Text wirkt wie maschinelle Rohubersetzung. |

---

## Dimension 3: Semantische Treue (Semantic Fidelity) -- 25 %

### Pruffragen
- Wird die **Bedeutung** des Ausgangstextes prazise und vollstandig wiedergegeben?
- Bleibt die **Intention** des Autors erhalten (Informieren, Uberzeugen, Anleiten, Unterhalten)?
- Sind **Nuancen, Ironie, Tonfall** korrekt ubertragen?
- Wurden **kulturspezifische Konzepte** angemessen lokalisiert oder erklart?
- Ist der Satzbau **idiomatisch deutsch** (kein "Denglisch", keine wörtlichen Lehnubersetzungen)?
- Sind **Verbpositionen** korrekt (Hauptsatz Position 2, Nebensatz Verb-End)?

| Band | Kriterium |
|------|-----------|
| 100 | Bedeutung, Intention und Tonfall des Originals perfekt getroffen. Text liest sich wie im Original auf Deutsch geschrieben. |
| 90 | 1 minimale Nuance nicht ideal getroffen, aber die Aussage ist korrekt und die Intention bleibt erhalten. |
| 80 | 2--3 Stellen mit leichter semantischer Verschiebung oder unidiomatischer Konstruktion. Bedeutung noch korrekt. |
| 70 | Mehrere semantische Abweichungen (4--5). Teilweise unidiomatisch. Die Intention ist noch erkennbar, aber abgeschwacht. |
| 60 | Systematische semantische Probleme. Die Ubersetzung verfehlt haufig die originale Bedeutung oder wirkt durchgangig unidiomatisch. |
| <50 | Bedeutung des Originals nicht oder nur fragmentarisch erkennbar. Satzstruktur ist Wort-fur-Wort-Ubersetzung. |

---

## Dimension 4: Formatkonformitat (Format Compliance) -- 10 %

### Pruffragen
- Wurden **deutsche Anfuhrungszeichen** verwendet? (Gansefuchen: `„..."`)
- Sind **Gedankenstriche** korrekt gesetzt? (Halbgeviertstrich `--` mit Leerzeichen, nicht Bindestrich)
- Sind **Kommas** nach deutschen Regeln gesetzt? (Nebensatze immer abgetrennt)
- Entspricht die **Groß-/Kleinschreibung** den deutschen Regeln? (Alle Substantive groß)
- Sind **Uberschriften, Listen und Tabellen** korrekt formatiert?
- Sind **Ubersetzungsnotationen** wie `[wiederhergestellt: ...]` korrekt verwendet?
- Ist die **Seitenzahl, Kopf-/Fußzeilen-Struktur** erhalten oder sinngemaß ubertragen?

| Band | Kriterium |
|------|-----------|
| 100 | Durchgangig korrekte deutsche Formatierung: Anfuhrungszeichen, Gedankenstriche, Kommas, Großschreibung, Formatvorlagen. |
| 90 | 1--2 minimale Formatierungsmangel (z. B. ein falsches Anfuhrungszeichen oder ein fehlender Gedankenstrich). |
| 80 | 3--5 Formatierungsfehler (englische Anfuhrungszeichen, fehlende Kommas in Nebensatzen, falsche Gedankenstriche). |
| 70 | Mehr als 5 Formatierungsfehler oder systematische Mangel in einer Kategorie (z. B. durchgangig englische Anfuhrungszeichen). |
| 60 | Uberwiegend falsche Formatierung. Englische Zeichensetzung beibehalten, Großschreibung fehlerhaft, Gedankenstriche nicht vorhanden. |
| <50 | Keinerlei Anpassung an deutsche Formatierungsregeln. Vollstandig englische Interpunktion, Zeichensetzung und Formatierung. |

---

## Dimension 5: Vollstandigkeit (Completeness) -- 10 %

### Pruffragen
- Wurde der **gesamte Quelltext** ubersetzt (keine fehlenden Absatze, Satze oder Worter)?
- Sind alle **Abschnitte, Kapitel und Gliederungspunkte** vorhanden?
- Wurden **Fussnoten, Endnoten und Randbemerkungen** ubersetzt?
- Sind **Text in Abbildungen, Diagrammen, Grafiken** berucksichtigt?
- Wurden **Metadaten** (Dokumenttitel, Autor, Datum) ubertragen?
- Fehlen ganze **Seiten oder Abschnitte**?

| Band | Kriterium |
|------|-----------|
| 100 | Keine Fehlstellen. Der gesamte Text wurde vollstandig ubersetzt, inklusive aller Nebenelemente. |
| 90 | 1 isolierte Fehlstelle (z. B. ein einzelnes Wort in einer Fussnote nicht ubersetzt). |
| 80 | 2--3 kleinere Fehlstellen (z. B. ein Satz in einer Tabellenzelle oder eine Bildunterschrift fehlt). |
| 70 | 4--5 Fehlstellen oder eine ganze Fussnote/Endnote nicht ubersetzt. |
| 60 | Grobere Fehlstellen: Fehlende Absatze oder mehrere Satze. Die Vollstandigkeit ist deutlich beeintrachtigt. |
| <50 | Große Textpassagen fehlen. Ganze Abschnitte oder Seiten wurden nicht ubersetzt. |

---

## Dimension 6: OCR-Qualitat / Inferenz (Inference & OCR Quality) -- 5 %

### Pruffragen
- Wurden **OCR-Artefakte** erkannt und korrigiert? (Umlaute, ß, Trennstriche, Ligaturen)
- Sind **unsichere Stellen** korrekt mit `[wiederhergestellt: ...]` markiert?
- Wurden **weiche Trennstriche** (soft hyphens) und Zeilenumbrüche entfernt?
- Sind **Zahlen/Ziffern** korrekt von Buchstaben unterschieden? (0/O, 1/l)
- Wurden **Formatierungsartefakte** (erzwungene Umbrüche, falsche Spalten) behoben?

| Band | Kriterium |
|------|-----------|
| 100 | Alle OCR-Artefakte bereinigt. Wiederhergestellte Stellen korrekt markiert. Keine sichtbaren OCR-Spuren im Text. |
| 90 | 1 ubersehenes OCR-Artefakt (z. B. ein `Ae` statt `Ä` oder ein verbliebener weicher Trennstrich). |
| 80 | 2--3 OCR-Artefakte nicht korrigiert. Markierungen teilweise inkonsistent. |
| 70 | 4--5 OCR-Fehler oder systematisch falsch korrigierte Umlaute (z. B. `ss`/`ß`-Fehler). |
| 60 | Zahlreiche verbliebene OCR-Artefakte. Formatierungsartefakte nicht bereinigt. Qualitat der OCR-Nachbearbeitung unzureichend. |
| <50 | OCR-Artefakte weitgehend unbearbeitet. Keine Wiederherstellungsnotationen. Text entspricht weitgehend der rohen OCR-Ausgabe. |

---

## Gesamtbewertungslogik

### Berechnung

```
Gesamtpunktzahl = (D1_Bandwert x 0,30)
                 + (D2_Bandwert x 0,20)
                 + (D3_Bandwert x 0,25)
                 + (D4_Bandwert x 0,10)
                 + (D5_Bandwert x 0,10)
                 + (D6_Bandwert x 0,05)
```

### Notenschlussel

| Gesamtpunktzahl | Note | Bewertung |
|-----------------|------|-----------|
| 96 -- 100 | A+ | Perfekt -- keine Mangel |
| 86 -- 95 | A | Exzellent -- minimale Mangel |
| 76 -- 85 | B | Gut -- leichte Mangel, leicht korrigierbar |
| 66 -- 75 | C | Befriedigend -- mehrere Mangel, Uberarbeitung empfohlen |
| 56 -- 65 | D | Ausreichend -- grundlegende Uberarbeitung notig |
| 0 -- 55 | F | Mangelhaft -- vollstandige Neuubersetzung erforderlich |

### Globale Korrekturfaktoren

1. **Null-Toleranz-Verstoß**: Bei jedem Verstoß gegen die Null-Toleranz-Regeln wird die Gesamtpunktzahl auf **maximal 60** begrenzt.
   - Ein Verstoß: Gesamtpunktzahl = min(berechneter Wert, 60)
   - Zwei oder mehr Verstoße: Gesamtpunktzahl = min(berechneter Wert, 50)

2. **Minimale Schwellenwerte fur Abnahme**:
   - **Dimension 1 (Numerical Accuracy)** muss mindestens **70** erreichen.
   - **Keine Einzeldimension** darf unter **60** liegen.
   - Gesamtpunktzahl muss mindestens **66** (Note C) betragen.

3. **Rechtliche/finanzielle Inhalte** (z. B. Vertrage, Jahresabschlüsse, Borsenmitteilungen):
   - Dimension 1 (Numerical Accuracy) muss >= **90** erreichen.
   - Dimension 2 (Terminology Consistency) muss >= **80** erreichen.
   - Bei Unterschreitung: Keine Abnahme, auch wenn Gesamtpunktzahl ausreichend ist.

### Entscheidungsmatrix

| Bedingung | Ergebnis |
|-----------|----------|
| Alle Dimensionen >= 90, keine Null-Toleranz-Verstoße | Abnahme ohne Korrektur |
| Eine Dimension 70--89, keine Null-Toleranz-Verstoße | Abnahme mit leichter Korrektur |
| Eine Dimension 60--69 oder ein Null-Toleranz-Verstoß | Uberarbeitung erforderlich |
| Eine Dimension < 60 oder zwei+ Null-Toleranz-Verstoße | Vollstandige Neuubersetzung |

---

**Anderungshistorie**
| Datum | Version | Anderung |
|-------|---------|----------|
| 2026-05-24 | 1.0 | Ersterstellung -- Scoring-Rubrik fur de-DE |
