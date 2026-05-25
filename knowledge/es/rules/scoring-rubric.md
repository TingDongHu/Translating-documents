---
id: es/rules/scoring-rubric
type: rules
target_lang: es
name: Criterios de evaluacion de calidad de traduccion al espanol
description: Criterios estandarizados de evaluacion segun seis parametros de calidad para el espanol
---

## Escala de puntuacion (Scoring Bands)

| Puntaje | Significado | Accion requerida |
|---------|-------------|------------------|
| 100 | Impecable | Ninguna |
| 90-99 | Problemas menores sin impacto en la comprension | Opcional |
| 70-89 | Varios problemas, requiere correccion | Recomendado corregir |
| 50-69 | Problemas sistematicos, requiere reelaboracion | Obligatorio corregir |
| <50 | Fracaso en este parametro | Retraduccion completa |

Cualquier traduccion con un error **critico** no puede obtener una puntuacion global superior a 60.

---

## 1. Precision numerica (Numerical Accuracy) — peso 30 %

Parametro critico para el espanol. El formato numerico espanol (coma decimal, punto de miles) difiere radicalmente del ingles y de muchos otros idiomas. Los errores en numeros son inaceptables.

| Puntaje | Criterios |
|---------|-----------|
| 100 | Todos los valores numericos, unidades de medida, fechas, porcentajes y cantidades coinciden exactamente con el original. Los formatos numericos espanoles se aplican correctamente: coma como separador decimal, punto como separador de miles. |
| 90 | 1-2 diferencias menores de formato (p. ej., espacio antes de %, uso de semirraya en lugar de «de X a Y» en un rango) que no afectan al valor. |
| 80 | 1-2 incoherencias en el formato numerico (p. ej., en un lugar se usa el punto de miles y en otro no; uso inconsistente del signo menos). |
| 70 | 3-5 problemas de formato numerico O 1 valor incorrecto que no afecta al sentido general (p. ej., error mecanografico en un numero no esencial). |
| 60 | Mas de 1 discrepancia factual de valor; O 5+ problemas de formato; O cualquier error de interpretacion de fecha. |
| <50 | Cualquier error critico: cantidad incorrecta, formato de fecha erroneo, conversion de unidades sin autorizacion, moneda incorrecta. |

**Nivel cero de tolerancia (puntos especificos del espanol):**
- Uso de punto en lugar de coma como separador decimal (1.5 en lugar de 1,5) — **ERROR CRITICO**
- Uso de coma en lugar de punto como separador de miles (1,234,567 en lugar de 1.234.567) — **ERROR CRITICO**
- Formato de fecha incorrecto (03/15/2024 en lugar de 15/03/2024 o confusion de mes y dia) — **ERROR CRITICO**
- Omision de la n con virgulilla en palabras claves (nino en lugar de nino) — **ERROR CRITICO**
- Omision de tildes diacriticas que cambian el significado (esta vs. esta, si vs. si) — **ERROR GRAVE**
- Uso de guion en lugar de semirraya en rangos (5-10 en lugar de 5-10) — error grave
- Ausencia de espacio antes del signo % (15% en lugar de 15 %) — error de formato

---

## 2. Coherencia terminologica (Terminology Consistency) — peso 20 %

La terminologia tecnica y especializada en espanol debe ser coherente. No es aceptable utilizar distintos terminos espanoles para un mismo concepto del idioma original.

| Puntaje | Criterios |
|---------|-----------|
| 100 | Todos los terminos repetidos utilizan exactamente una opcion de traduccion; el glosario se cumple al 100 %. |
| 90 | 1-2 desviaciones terminologicas menores, justificadas por el contexto (p. ej., sinonimos para mejorar la legibilidad). |
| 80 | 1-2 divergencias terminologicas injustificadas; O 1 incumplimiento del glosario. |
| 70 | 3-5 divergencias terminologicas O 2-3 incumplimientos del glosario. |
| 60 | 5+ divergencias terminologicas; confusion sistematica de terminos clave. |
| <50 | El glosario se ignora sistematicamente; los terminos clave se traducen de forma distinta en cada caso, causando confusion. |

**Requisitos especificos del espanol:**
- Uso de anglicismos innecesarios donde existe un termino espanol estandar (p. ej., «feedback» en lugar de «comentarios/retroalimentacion», «email» en lugar de «correo electronico», «meeting» en lugar de «reunion») — **ERROR en documentos formales**
- Mezcla de variantes ortograficas del mismo termino (p. ej., «CD-ROM» vs. «cederrom» vs. «CD Rom») — requiere uniformidad
- Latinismos innecesarios: evitar latinismos cuando exista un termino espanol claro (p. ej., «id est» en lugar de «es decir»)
- Falsos amigos: confusion de «actualmente» por «actually», «asistir» por «assist», «exito» por «exit», «billon» por «billion»

**Variaciones contextuales vs. injustificadas:** Un termino puede variar legitimamente segun el contexto (p. ej., «run» -> «ejecutar» para comandos, «run» -> «gestionar» para proyectos, «run» -> «funcionar» para maquinas). Solo se penalizan los casos donde no existe una razon contextual para la diferencia.

---

## 3. Fidelidad semantica (Semantic Fidelity) — peso 25 %

| Puntaje | Criterios |
|---------|-----------|
| 100 | Equivalencia semantica total: sin omisiones, sin adiciones, sin distorsiones. |
| 90 | 1-2 reformulaciones menores que conservan el significado pero desplazan ligeramente el enfasis. |
| 80 | 1-2 casos de omision/adicion que no cambian el sentido general. |
| 70 | 3-5 omisiones o explicaciones anadidas menores; O 1 oracion con significado alterado. |
| 60 | Oraciones omitidas; contenido anadido que no aparece en el original; 2+ oraciones con significado incorrecto. |
| <50 | Parrafos con significado fundamentalmente incorrecto; perdida de informacion clave; omisiones sistematicas. |

**Aspectos especificos del espanol:**
- Atencion al modo subjuntivo: el espanol requiere subjuntivo en contextos donde el ingles usa indicativo.
  - `I hope you come` -> `Espero que vengas` (subjuntivo), no `Espero que vienes`
- Ser vs. Estar: la distincion es esencial y no existe en muchos idiomas.
- Preposiciones: errores en el regimen preposicional pueden cambiar el significado.
- Tiempos verbales: el preterito perfecto compuesto es mas frecuente en Espana que en America.

**Metodo de verificacion:** Leer el parrafo original y luego el parrafo traducido. Responden a la misma pregunta? Anade la traduccion informacion que no esta en el original? Omite detalles importantes?

---

## 4. Cumplimiento de formato (Format Compliance) — peso 10 %

Verificacion del cumplimiento de las normas tipograficas y de formato espanolas (RAE, Ortografia de la lengua espanola 2010, normas ISO aplicables).

| Puntaje | Criterios |
|---------|-----------|
| 100 | Todos los formatos numericos, direcciones, puntuacion y tipografia siguen las convenciones espanolas. Se utilizan las comillas latinas « », la raya (—) correcta, los separadores adecuados y los signos de apertura ┬┐ ┬í. |
| 90 | 1-2 desviaciones menores de las normas tipograficas espanolas (p. ej., un caso de comillas inglesas en lugar de latinas, un espacio superfluo). |
| 80 | 2-3 incoherencias en el formato o mezcla de convenciones espanolas y extranjeras dentro del mismo documento. |
| 70 | 4-5 problemas de formato; uso sistematico del formato del idioma original (p. ej., comillas inglesas en todo el documento, punto como separador decimal). |
| 60 | Problemas de formato numerosos; estilo de puntuacion inconsistente en todo el documento. |
| <50 | El formato hace que el documento parezca no profesional; violaciones criticas de las convenciones espanolas. |

**Verificaciones principales para el espanol:**
- **Signos de interrogacion/exclamacion**: uso obligatorio de ┬┐ y ┬í de apertura — **ERROR CRITICO** si faltan
- **Comillas**: usar « » (comillas latinas), no "comillas inglesas" ni « comillas invertidas » — **ERROR CRITICO** en documentos formales
- **Raya (—)**: usar la raya para dialogos e incisos, no el guion (-) — error grave
- **Separador decimal**: coma (,), no punto (.) — **ERROR CRITICO**
- **Separador de miles**: punto (.), no coma
- **Fecha**: formato DD/MM/AAAA
- **Hora**: formato 24h (15:30), no AM/PM
- **Espacio antes de %**: 15 %, no 15%
- **Simbolo de moneda**: despues de la cantidad (100 €), no antes
- **Direccion**: orden calle -> numero -> piso -> ciudad -> provincia -> CP -> pais
- **Guion vs. semirraya vs. raya**: guion (-) para palabras compuestas, semirraya (–) para rangos, raya (—) para dialogos e incisos
- **Mayusculas en titulos**: solo la primera palabra y los nombres propios (no capitalizacion completa como en ingles)

---

## 5. Integridad (Completeness) — peso 10 %

| Puntaje | Criterios |
|---------|-----------|
| 100 | Cada parrafo esta traducido; todos los marcadores [Pn] estan presentes; no hay secciones omitidas. |
| 90 | 1-2 parrafos con fragmentos sin traducir; O 1 marcador [Pn] ausente sin espacio. |
| 80 | 1-2 parrafos completamente sin traducir; O subtitulo sin traducir. |
| 70 | 3-5 parrafos sin traducir o ausentes; O una seccion omitida. |
| 60 | 5+ parrafos sin traducir; O contenido truncado en los limites del documento. |
| <50 | Faltan secciones importantes; el documento esta incompleto; omisiones sistematicas. |

**Nota:** Para la traduccion al espanol, prestar especial atencion a la integridad de la traduccion de todas las abreviaturas y siglas en su primera aparicion. Las siglas en ingles deben mantenerse con su equivalente en espanol entre parentesis en la primera mencion (p. ej., «CEO (director ejecutivo)»).

---

## 6. Calidad de la restauracion / OCR (Inference/OCR Quality) — peso 5 %

| Puntaje | Criterios |
|---------|-----------|
| 100 | Todos los marcadores de restauracion son razonables, bien fundamentados y estan correctamente formateados con la etiqueta `[restaurado: ...]`. |
| 90 | 1 marcador de restauracion con argumentacion ligeramente debil pero aun defendible. |
| 80 | 1-2 casos donde la restauracion puede ser erronea, pero esta claramente indicada; O 1 caso donde la restauracion deberia haberse aplicado pero no se aplico. |
| 70 | 2-3 restauraciones dudosas; O 2 restauraciones no marcadas que deberian haber sido indicadas. |
| 60 | Multiples restauraciones dudosas; adivinacion sistematica sin marcadores. |
| <50 | Contenido inventado presentado como traduccion; numeros o hechos fabricados. |

**Requisitos especificos del espanol:**
- Restauracion de la virgulilla de la n (n): esencial en espanol; su omision puede cambiar el significado
  - `ano` (ano) vs. `ano` (year) — restauracion critica
  - `senor` vs. `senor` — restauracion critica
  - `espanol` vs. `espanol`
- Restauracion de tildes: critico para diferenciar palabras:
  - `esta` (this) vs. `esta` (is) — tildes diacriticas
  - `sí` (yes) vs. `si` (if)
  - `el` (the) vs. `él` (he)
  - `solo` (alone) vs. `solo` (only) — la RAE recomienda la tilde en casos de ambiguedad
- Restauracion de la dieresis (u): `pingueino`, `cigueena`, `vergüenza`, `averiguue`
- Distincion de caracteres latinos: Latin `o` vs Spanish `o`, Latin `a` vs Spanish `a`
- Restauracion de la cedilla (c): aunque poco frecuente en espanol moderno, aparece en extranjerismos adaptados

**Principio:** Es mejor marcar el contenido dudoso como restaurado que adivinar en silencio. La marcacion correcta con reconocimiento de incertidumbre NO es un defecto, sino una buena practica.

---

## Tabla resumen (Summary Table)

| No. | Dimension | Peso | Errores criticos en espanol (zero-tolerance items) |
|-----|-----------|------|-----------------------------------------------------|
| 1 | Precision numerica | 30 % | Punto en lugar de coma decimal, coma en lugar de punto de miles, formato de fecha incorrecto |
| 2 | Coherencia terminologica | 20 % | Anglicismos injustificados, mezcla de variantes de terminos, falsos amigos |
| 3 | Fidelidad semantica | 25 % | Distorsion del modo subjuntivo, confusion ser/estar, regimen preposicional erroneo |
| 4 | Cumplimiento de formato | 10 % | Ausencia de signos ┬┐ ┬í, comillas incorrectas, raya vs. guion, mayusculas en titulos |
| 5 | Integridad | 10 % | Omision de secciones, parrafos sin traducir |
| 6 | Calidad de restauracion | 5 % | Datos inventados presentados como traduccion |

## Mapa rapido de errores inadmisibles (Quick Zero-Tolerance Map)

| Error | Dimension | Gravedad |
|-------|-----------|----------|
| 1,5 -> 1.5 (punto en lugar de coma decimal) | Precision numerica | CRITICO |
| 1.234.567 -> 1,234,567 (comas en lugar de puntos de miles) | Precision numerica | CRITICO |
| 15/03/2024 -> 03/15/2024 (formato de fecha) | Precision numerica | CRITICO |
| 15 % -> 15% (falta espacio antes de %) | Precision numerica | Grave |
| nino por nino (falta virgulilla de la n) | Precision numerica | CRITICO |
| Falta ┬┐ o ┬í de apertura | Cumplimiento de formato | CRITICO |
| «Texto» -> "Texto" (comillas incorrectas) | Cumplimiento de formato | CRITICO |
| — (raya) -> - (guion) | Cumplimiento de formato | CRITICO |
| 100 € -> €100 (moneda antes de la cantidad) | Cumplimiento de formato | Grave |
| «feedback» en lugar de «comentarios/retroalimentacion» | Coherencia terminologica | Grave (documentos formales) |
| «actualmente» por «actually» (falso amigo) | Coherencia terminologica | Grave |
| Parrafo sin traducir | Integridad | CRITICO |
| Datos inventados | Calidad de restauracion | CRITICO |

## Regla global: error critico -> maximo 60

Si una traduccion contiene UN SOLO error critico entre los listados anteriormente, la puntuacion global maxima que puede recibir es **60**, independientemente de la calidad del resto de la traduccion. Esto refleja el caracter vinculante de las convenciones de formato y numericas del espanol.

---

**Historial de cambios**
| Fecha | Version | Cambio |
|-------|---------|--------|
| 2026-05-25 | 1.0 | Creacion inicial — Criterios de evaluacion para es-ES / espanol internacional |
