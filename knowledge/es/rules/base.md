---
id: es/rules/base
type: rules
target_lang: es
name: Convenciones de traduccion al espanol
description: Reglas basicas para la traduccion de documentos al espanol (es-ES / espanol internacional)
---

# Convenciones de escritura en espanol (Spanish Writing Conventions)

Este documento define las convenciones de escritura vinculantes para las traducciones al espanol (es-ES y espanol internacional). Todas las traducciones deben seguir estas reglas. La base normativa es la Ortografia de la lengua espanola (RAE, 2010), la Nueva gramatica de la lengua espanola (RAE, 2009) y el Diccionario panhispanico de dudas (RAE, 2005).

---

## 1. Formato numerico (Number Format)

### Separador decimal: coma (,)
- En espanol, el separador decimal es SIEMPRE la **COMA** (,), nunca el punto.
- `1.5` (ingles) → `1,5`
- `3.14159` → `3,14159`
- `99.9%` → `99,9 %`
- `0.05` → `0,05`
- `10.5 million` → `10,5 millones`

### Separador de miles: punto (.)
- El separador de miles es el **PUNTO** (.), no la coma.
- `1,234,567` (ingles) → `1.234.567`
- `1000000` → `1.000.000`
- `15000.50` → `15.000,50`
- `9999999` → `9.999.999`
- Excepcion: En documentos muy tecnicos o tablas, la RAE permite omitir el separador de miles en numeros de hasta 4 cifras: `1000` en lugar de `1.000`.

### Numeros de cuatro cifras
- `1000` es aceptable sin punto; `1500` tambien.
- A partir de `10.000`, el punto es obligatorio.
- Consistencia dentro del documento: si se usa punto en un numero de 4 cifras, usarlo en todos.

### Porcentajes (%)
- El signo `%` se escribe **SEPARADO** de la cifra por un espacio.
- `15%` (ingles) → `15 %`
- `99,9%` → `99,9 %`
- `aumento del 5 %` (nunca `aumento del 5%`)
- Rangos: `entre el 10 % y el 20 %` o `del 10 % al 20 %`
- En tablas con espacio limitado, se permite `15%` sin espacio, pero debe ser consistente.

### Numeros negativos
- El signo menos (−, U+2212, o el guion -) se coloca **INMEDIATAMENTE** antes de la cifra, sin espacio.
- `-5 °C` (correcto)
- `− 5 °C` (incorrecto: espacio despues del menos)
- En contextos contables/financieros, los numeros negativos pueden ir entre parentesis: `(1.234,56)`.

### Rangos numericos
- Use `entre X e Y` o `de X a Y` en texto corrido: `entre 5 y 10`, `de 20 a 30 %`
- Use una raya (–, U+2013) sin espacios para rangos compactos en parentesis/tablas: `5–10`, `20–30 %`
- `pages 10-20` → `pags. 10–20`
- `3-5 days` → `de 3 a 5 dias`
- NO use guion (-) para rangos numericos; use la raya (–).

### Fracciones y decimales
- `1/2` → `1/2` o `medio`
- `1.5 million` → `1,5 millones`
- `0.5 billion` → `500 millones` (mil millones en espanol europeo; millardo es poco usado)
- `one quarter` → `un cuarto` o `la cuarta parte`

### Numeros ordinales
- En espanol, los ordinales se abrevian con letra volada: `1.º`, `2.ª`, `3.er`, `10.º`
- `1st quarter` → `1.er trimestre`
- `2nd floor` → `2.ª planta` / `segundo piso`
- `3rd place` → `3.er puesto`
- `20th century` → `siglo XX` (numeros romanos preferidos para siglos)
- `Page 5` → `Pag. 5`
- `Chapter 3` → `Capitulo 3`

### Notacion cientifica y unidades
- Espacio entre numero y unidad: `10 km`, `3,5 kg`, `25 °C`, `100 m²`
- Excepcion: angulos (`5°`), pulgadas (`2"`), porcentaje en tablas (`50%`)
- `5km/h` → `5 km/h`
- Temperatura: `25 °C` (con espacio entre el numero y °C)
- En textos no tecnicos, las unidades pueden escribirse con letra: `10 kilometros`, `5 kilogramos`

---

## 2. Moneda (Currency)

### Posicion del simbolo: DESPUES de la cantidad, con espacio
- Para el euro y la mayoria de monedas en espanol europeo:
  - `€100.00` → `100,00 €`
  - `€1,234.56` → `1.234,56 €`
  - `€500` → `500 €`
  - `£99.99` → `99,99 £`

### Dolar ($) para America Latina
- En contextos latinoamericanos, el simbolo `$` puede ir ANTES o DESPUES, segun la norma local.
  - `$1,234.56` → `$1.234,56` (America Latina: $ antes, pero con punto de miles y coma decimal)
  - `US$1.234,56` (con codigo de pais para distinguir)
- Para uso internacional, se recomienda el codigo ISO DESPUES de la cantidad:
  - `100,00 USD` (no `USD 100,00`)
  - `50,00 EUR`
  - `200,00 MXN`
  - `1.500,00 ARS`

### Codigos ISO 4217
- Los codigos ISO de moneda van DESPUES de la cantidad, separados por un espacio:
  - `1.250,00 EUR`
  - `25,00 USD`
  - `1.000 JPY`
  - `50,00 CHF`
- En documentos tecnicos/financieros, los codigos ISO son preferibles a los simbolos.

### Nombres de monedas en espanol
- `EUR` → euro (masculino: el euro, los euros)
- `USD` → dolar estadounidense / dolar (masculino)
- `MXN` → peso mexicano
- `ARS` → peso argentino
- `GBP` → libra esterlina (femenino)
- `JPY` → yen (masculino, invariable en plural: los yen)
- `CNY` → yuan (masculino)
- `CHF` → franco suizo
- `BRL` → real brasileño
- `COP` → peso colombiano

### Conversiones de moneda
- `12,50 € (aproximadamente 13,20 USD)`
- Incluir la fecha del tipo de cambio para cantidades historicas: `100 ESP (0,60 €, segun cambio de 1999)`

### Decimales monetarios
- Dos decimales para cantidades exactas: `1,50 €`
- En contextos financieros, siempre dos decimales: `5,00 €`
- Fracciones de centimo (1/1000) solo en datos financieros muy especificos.

---

## 3. Fecha y hora (Date and Time)

### Formato de fecha: DD/MM/AAAA
- El formato estandar en espanol es **DIA/MES/ANIO** (DD/MM/AAAA).
- `03/15/2024` (ingles) → `15/03/2024`
- `2024-05-10` (ISO) → `10/05/2024`
- `01/02/2023` → `01/02/2023` (1 de febrero, NO 2 de enero)
- Separador: barra inclinada (/) o guion (-). Ambos son aceptables, pero debe haber consistencia.
- `15-03-2024` o `15/03/2024` (elegir uno y mantenerlo en todo el documento)

### Fechas con palabras (meses en espanol)
- `March 15, 2024` → `15 de marzo de 2024`
- `January 1` → `1 de enero`
- `September 2023` → `septiembre de 2023`
- NO se usa coma entre el dia y el mes: `15 de marzo de 2024` (no `15 de marzo, 2024`)
- Los meses y dias de la semana se escriben en **minuscula** en espanol.

### Nombres de los meses (minuscula inicial)
| Mes | En espanol |
|-----|-----------|
| January | enero |
| February | febrero |
| March | marzo |
| April | abril |
| May | mayo |
| June | junio |
| July | julio |
| August | agosto |
| September | septiembre |
| October | octubre |
| November | noviembre |
| December | diciembre |

### Formato de hora: 24 horas (HH:MM)
- En espanol se usa el **formato de 24 horas** predominantemente.
- `3:30 PM` → `15:30`
- `12:00 AM` → `00:00`
- `9:45 AM` → `9:45` o `09:45`
- `6:00 PM` → `18:00`
- Separador: dos puntos (`:`), nunca punto.
- NO usar notacion AM/PM en espanol europeo; opcional en contextos latinoamericanos.
- `10:00 a. m.` / `6:00 p. m.` (con espacios y puntos) es aceptable en espanol americano, pero el formato 24h es preferible en toda circunstancia.

### Rangos de hora
- `de 10:00 a 12:00 h` (con h de horas)
- `el horario es de 9:00 a 17:00 h`
- `10:00–12:00 h` (con raya)

### Combinacion fecha + hora
- `15 de marzo de 2024, a las 15:30 h`
- `15/03/2024, 15:30 h`

### Nombres de los dias de la semana (minuscula inicial)
| Dia | En espanol |
|-----|-----------|
| Monday | lunes |
| Tuesday | martes |
| Wednesday | miercoles |
| Thursday | jueves |
| Friday | viernes |
| Saturday | sabado |
| Sunday | domingo |

### Semanas y periodos
- `semana del 15 de marzo`
- `del 1 al 15 de mayo de 2024`
- `primer trimestre de 2024`

---

## 4. Direcciones (Addresses)

### Formato de direccion en espanol
El orden estandar de una direccion en espanol es:

`[tipo de via] [nombre] [numero] → [piso] → [puerta] → [ciudad] → [provincia] → [codigo postal] → [pais]`

Ejemplo completo:
```
C/ Gran Via, 42, 3.º D
28013 Madrid
Espana
```

### Componentes de la direccion
- **Via**: `calle` (c/), `avenida` (avda.), `plaza` (plz.), `paseo` (p.º), `callejon`, `travesia`, `ronda`, `glorieta`, `carretera` (crta.)
- **Numero**: despues del nombre de la via: `Calle Alcala, 25`
- **Piso**: `1.º` (primero), `2.º` (segundo), `3.º` (tercero), `bajo` (planta baja), `entresuelo`, `principal`
- **Puerta**: `A`, `B`, `C`, `izquierda`, `derecha`
- **Provincia**: en Espana, la provincia se escribe detras del codigo postal

### Abreviaturas comunes
- `c/` = calle
- `avda.` / `av.` = avenida
- `pl.` / `plz.` = plaza
- `p.º` = paseo
- `crta.` = carretera
- `edif.` = edificio
- `esc.` = escalera
- `apto.` / `depto.` = apartamento / departamento
- `s/n` = sin numero (cuando no hay numero)
- `CP` = codigo postal

### Direcciones internacionales
- Cuando la direccion original esta en un pais extranjero, conservar los nombres de lugar originales pero estructurarlos segun la convencion espanola cuando sea posible.
- `123 Main St, Apt 4, New York, NY 10001` → `123 Main St, Apt. 4, Nueva York, NY 10001, EE. UU.`
- `10 Downing Street, London SW1A 2AA` → `10 Downing Street, Londres SW1A 2AA, Reino Unido`

### Paises hispanohablantes
- `Argentina`: `C/ Florida 123, Piso 5.º, C1005AAF CABA, Argentina`
- `Mexico`: `Av. Reforma 222, Col. Juarez, 06600 Cuauhtemoc, CDMX, Mexico`
- `Colombia`: `Cra 7 # 12-34, Of. 501, Bogota, Colombia`
- `Chile`: `Av. Providencia 1650, Depto. 301, Providencia, Santiago, Chile`

---

## 5. Nombres propios (Proper Nouns)

### Conservacion de acentos y caracteres especiales
- Los nombres propios extranjeros CONSERVAN sus acentos, dieresis y caracteres especiales originales.
- `Jose` se escribe `Jose` si la persona lo escribe asi, pero la forma espanola es `Jose`.
- `Muller` → conserva la dieresis
- `Francois` → conserva la cedilla
- `Moscow` → `Moscu` (exonimo establecido)
- `Beijing` → `Pekin` (exonimo tradicional) o `Beijing` (forma moderna aceptada)

### La letra N con tilde (n) y la U con dieresis (u)
- La `n` y la `u` son letras propias del espanol. Deben usarse correctamente en todos los textos en espanol.
- `nino`, `espanol`, `anadir` (no `nino`, `espanol`, `anadir`)
- `cigueena`, `averiguar`, `pingueino` (no `ciguena`, `averiguar`, `pinguino`)
- En nombres propios traducidos: mantener `n` y `u` donde corresponda.

### Nombres de personas extranjeras
- En documentos tecnicos/comerciales: mantener la grafia original latina.
- Primera mencion: puede anadirse la pronunciacion orientativa entre parentesis:
  - `John Smith (pron. /yon smiz/)`
- Menciones posteriores: solo el nombre original.
- `Emma Watson` (no se traduce)
- `Friedrich Nietzsche` → `Friedrich Nietzsche` (no se traduce)
- Excepcion: nombres de figuras historicas con forma espanola establecida:
  - `Charles Darwin` → `Charles Darwin` (se mantiene)
  - `William Shakespeare` → `William Shakespeare`
  - Pero: `Aristotle` → `Aristoteles`, `Plato` → `Platon`, `Julius Caesar` → `Julio Cesar`

### Nombres de empresas
- Conservar la razon social registrada original.
- Anadir la traduccion o descripcion entre parentesis en la primera mencion si es necesario:
  - `Apple Inc.` → `Apple Inc.`
  - `Microsoft Corporation` → `Microsoft Corporation`
  - `Petroleos Mexicanos (Pemex)` → `Petroleos Mexicanos (Pemex)`
  - `Volkswagen AG` → `Volkswagen AG`
- NO traducir nombres de empresas a menos que exista un nombre oficial en espanol.

### Nombres de productos y marcas
- Conservar siempre la grafia original de la marca registrada.
- NO traducir nombres de productos registrados:
  - `iPhone 15` (no `Telefono inteligente 15`)
  - `Windows 11` (no `Ventanas 11`)
  - `Coca-Cola` (no `Cola de coca`)
- Excepcion: productos con nombre comercial oficial en espanol.

### Nombres geograficos
- Usar los exonimos espanoles establecidos donde existan:
  - `Germany` → `Alemania`
  - `United States` → `Estados Unidos`
  - `United Kingdom` → `Reino Unido`
  - `Netherlands` → `Paises Bajos`
  - `Switzerland` → `Suiza`
  - `Russia` → `Rusia`
  - `China` → `China`
  - `Japan` → `Japon`
- Ciudades: `Paris` (no `Paris` en frances), `London` → `Londres`, `New York` → `Nueva York`, `Los Angeles` → `Los Angeles` (se mantiene)
- Para lugares poco conocidos, mantener el nombre original y, si procede, anadir el pais entre parentesis.

### Formas juridicas (traduccion de siglas)
- `LLC` → `S. de R.L.` (Sociedad de Responsabilidad Limitada) o `LLC` en contextos internacionales
- `Inc.` → `S. A.` (Sociedad Anonima) o `Inc.` si es extranjera
- `GmbH` → `S. de R.L.` o se mantiene `GmbH`
- `Ltd.` → `S. de R.L.` o `Ltd.`
- `PLC` → `S. A.` (publica)
- `S.L.` = Sociedad Limitada (Espanol)
- `S.A.` = Sociedad Anonima (Espanol)
- `S.A.P.I.` = Sociedad Anonima Promotora de Inversion (Mexico)

---

## 6. Puntuacion (Punctuation)

### Signos de interrogacion y exclamacion: INVERTIDOS (┬┐ ┬í)
- El espanol es la UNICA lengua que usa signos de apertura invertidos.
- **OBLIGATORIO** abrir y cerrar cada pregunta y cada exclamacion.
- `Que hora es?` → INCORRECTO
- `┬┐Que hora es?` → CORRECTO
- `Que bien!` → INCORRECTO
- `┬íQue bien!` → CORRECTO
- Los signos de apertura se colocan al inicio de la oracion interrogativa/exclamativa, no necesariamente al inicio de la frase:
  - `Si no puedes venir, ┬┐cuando podriamos reunirnos?`
  - `Por cierto, ┬íque sorpresa verte!`
- En secuencias de preguntas/exclamaciones cortas, cada una lleva sus propios signos:
  - `┬┐Donde? ┬┐Cuando? ┬┐Por que?`

### Comillas: « » (comillas latinas o angulares)
- Las comillas preferidas en espanol son las **comillas latinas** (tambien llamadas angulares o guillemets): `« »`
- `"Hello"` → `«Hola»`
- `El dijo: «Ven aqui»`
- Comillas de segundo nivel: `" "` (comillas inglesas dobles)
  - `El dijo: «Ella me respondio: "Voy ahora mismo"»`
- Comillas de tercer nivel: `' '` (comillas simples)
- NO usar comillas rectas ("" ) en documentos formales en espanol.

### Raya (—) como signo de dialogo e inciso
- La **raya** (—, U+2014) se usa para:
  - Dialogos: `— ┬┐Que tal? — pregunto. — Muy bien — respondio.`
  - Incisos: `El documento —como ya sabe— requiere revision.`
  - Listados: `— primer punto` (con espacio despues de la raya)
- La raya se escribe **sin espacio** antes y despues en dialogos, pero con espacio antes y despues en incisos parenteticos.
- NO confundir con el guion (-) o la semirraya (–).

### Guion (-) vs. Semirraya (–)
- **Guion** (-): para palabras compuestas, prefijos y separacion silabica:
  - `teorico-practico`, `hispano-mexicano`, `ex-presidente`
  - `anti-inflacionario` (cuando el prefijo acaba en vocal y la palabra empieza por la misma vocal)
- **Semirraya** (–, U+2013): para rangos numericos y conexiones entre elementos:
  - `paginas 10–20`, `1990–2000`, `Madrid–Barcelona`
  - `relacion calidad–precio`
- NO usar guion donde corresponde semirraya, y viceversa.

### Signos dobles: ┬┐ y ┬í
- **NUNCA** dejar espacio despues de ┬┐ o ┬í de apertura.
- **NUNCA** dejar espacio antes de ? o ! de cierre.
- Correcto: `┬┐Que tal?` (no `┬┐ Que tal?` ni `┬┐Que tal ?`)
- Correcto: `┬íBravo!` (no `┬í Bravo!`)

### Uso de la coma
- No existe coma serial (Oxford) en espanol: `pan, vino y queso` (sin coma antes de `y`)
- Coma antes de `pero`, `sino`, `aunque`: `Es caro, pero necesario`
- Coma en vocativos: `Amigos, escuchadme`
- Coma en incisos y aposiciones: `Madrid, capital de Espana, es una ciudad cosmopolita`
- Coma en enumeraciones: `Compraron manzanas, peras, naranjas y platanos`

### Punto y coma (;)
- Para separar elementos de una enumeracion cuando contienen comas:
  - `La conferencia se celebrara en Madrid, Espana; Buenos Aires, Argentina; y Ciudad de Mexico, Mexico.`
- Para unir oraciones relacionadas: `Llego tarde; la reunion ya habia comenzado.`

### Dos puntos (:)
- Antes de enumeraciones: `Tres cosas: trabajo, casa y familia.`
- En citas textuales: `El autor afirma: «La lengua es un organismo vivo.»`
- En cartas y saludos: `Estimado Sr. Garcia:`

### Puntos suspensivos (...)
- Tres puntos, sin espacio antes (si continuan la palabra) o con espacio (si sustituyen texto):
  - `No se que decir...`
  - `El texto decia algo como ... no recuerdo bien.`

### Uso de mayusculas en titulos
- En espanol, los titulos (de libros, articulos, capitulos) solo llevan mayuscula en la PRIMERA PALABRA y en los nombres propios:
  - `Cien anos de soledad` (no `Cien Anos De Soledad`)
  - `El senor de los anillos` (no `El Senor De Los Anillos`)
  - Los titulos de secciones y capitulos siguen la misma regla: solo primera palabra en mayuscula.

---

## 7. Formato (Formatting)

### Jerarquia de encabezados
- Preservar todos los niveles de encabezado (#, ##, ###) exactamente como en el original.
- `# Chapter 1` → `# Capitulo 1`
- `## Introduction` → `## Introduccion`
- `### 1.1 Background` → `### 1.1 Antecedentes`
- En espanol, los encabezados usan mayuscula solo en la primera palabra (no capitalizacion completa).

### Formato de listas
- **Listas con vinetas**: usar el guion (`-`) o el asterisco (`*`), consistentemente en todo el documento.
- La raya (—) es aceptable pero menos comun en espanol moderno.
- `- Primer punto`
- `- Segundo punto`
- **Listas numeradas**: numeros arabigos con punto:
  - `1. Primer punto`
  - `2. Segundo punto`
- **Sub-listas**: mantener la indentacion y usar un marcador diferente (guion para nivel 1, asterisco para nivel 2, etc.).

### Tablas
- Conservar todas las fronteras de tabla y alineacion de celdas.
- Traducir contenido celda por celda.
- Mantener encabezados de columna traducidos.
- Preservar la combinacion de filas/columnas.
- NO fusionar ni dividir celdas a menos que sea absolutamente necesario por la longitud del texto.

### Saltos de parrafo
- Mantener las mismas divisiones de parrafo que el original.
- NO fusionar parrafos.
- NO dividir un parrafo en varios a menos que la traduccion sea significativamente mas larga.

### Negrita, cursiva y subrayado
- Preservar todo el formato de enfasis (**negrita**, *cursiva*).
- En tipografia espanola, la negrita se prefiere para titulos; la cursiva para enfasis dentro del texto.
- La cursiva se usa para extranjerismos: `El software fue desarrollado por Microsoft.`
- Evitar el uso de MAYUSCULAS para enfasis; el espanol usa cursiva o negrita.

### Notas al pie y notas finales
- Preservar todos los marcadores de nota y su posicion.
- Traducir el contenido de las notas.

### Abreviaturas
- `etc.` (etcetera), `p. ej.` (por ejemplo), `ed.` (edicion), `vol.` (volumen)
- `Sr.` (senor), `Sra.` (senora), `Srta.` (senorita)
- `D.` (don), `D.ª` (dona)
- `adm.` (administracion), `dpto.` (departamento)
- `n.º` (numero), `pags.` (paginas)
- `S. L.` (Sociedad Limitada), `S. A.` (Sociedad Anonima)
- `a. C.` / `d. C.` (antes/despues de Cristo)
- Las abreviaturas llevan punto y se mantienen en minuscula salvo que sean siglas.

---

## 8. Gramatica (Grammar)

### Genero y concordancia (Gender Agreement)
- El espanol tiene dos generos: **masculino** y **femenino**.
- Todos los adjetivos, articulos y participios deben concordar en genero y numero con el sustantivo:
  - `el libro nuevo` (masculino singular)
  - `la casa nueva` (femenino singular)
  - `los libros nuevos` (masculino plural)
  - `las casas nuevas` (femenino plural)
- Sustantivos ambiguos: `el agua` (femenino que usa articulo masculino por fonetica), `el alma`, `el hacha`, `el area`
- Error comun: ``la problema`` → correcto: `el problema`
- Error comun: ```la sistema`` → correcto: `el sistema`
- Error comun: `el mano` → correcto: `la mano`

### Modo subjuntivo (Subjunctive Mood)
- El subjuntivo es esencial en espanol y debe usarse en:
  - Deseos: `Espero que vengas.`
  - Dudas: `Dudo que sea cierto.`
  - Emociones: `Me alegra que estes bien.`
  - Oraciones impersonales: `Es importante que leas esto.`
  - Conjunciones temporales con referencia futura: `Cuando llegues, llamame.`
- No usar indicativo donde corresponde subjuntivo.

### Ser vs. Estar
- `Ser` (esencia, caracteristicas permanentes, origen, profesion):
  - `Es alto.` `Es de Madrid.` `Es medico.` `Son las tres.`
- `Estar` (estado temporal, ubicacion, resultado):
  - `Esta cansado.` `Esta en casa.` `Esta roto.`
- Error comun: `Soy bien.` → correcto: `Estoy bien.`
- Error comun: `Esta medico.` → correcto: `Es medico.`

### Verbos reflexivos
- En espanol, los verbos reflexivos son muy comunes y llevan el pronombre reflexivo:
  - `levantarse`, `llamarse`, `sentarse`, `vestirse`, `acordarse`
  - `Me llamo Juan.` `Se levanta temprano.`
  - `Nos reuniremos manana.`
- Muchos verbos que en ingles no son reflexivos lo son en espanol:
  - `to go` → `irse` (marcharse): `Me voy.`
  - `to become` → `volverse / hacerse / convertirse en`
  - `to remember` → `acordarse de`: `Me acuerdo de ti.`

### Preposiciones (Prepositions)
- `a`: direccion, tiempo, complemento directo de persona: `Voy a Madrid.`, `Veo a Juan.`
- `de`: posesion, origen, materia, contenido: `La casa de Maria.`, `Vaso de agua.`
- `en`: ubicacion, medio de transporte, idioma: `Estoy en casa.`, `En coche.`, `En espanol.`
- `con`: compania, instrumento: `Cafe con leche.`, `Escribo con lapiz.`
- `por`: causa, medio, periodicidad, precio, a traves de: `Por tu culpa.`, `Por correo.`
- `para`: finalidad, destinatario, plazo, opinion: `Para ti.`, `Para manana.`
- Error comun: `Voy a comprar por la manana.` → correcto: `Voy a comprar por la manana.` (depende del contexto: `por la manana` = durante, `para la manana` = para cuando llegue)

### Tiempos verbales (Verb Tenses)
- **Presente de indicativo**: `hablo`, `como`, `vivo`
- **Preterito perfecto simple (indefinido)**: `hable`, `comi`, `vivi` (accion completada en el pasado)
- **Preterito imperfecto**: `hablaba`, `comia`, `vivia` (accion habitual o en desarrollo en el pasado)
- **Preterito perfecto compuesto**: `he hablado`, `he comido` (accion pasada con relevancia presente; mas usado en Espana que en America)
- **Futuro simple**: `hablare`, `comere` (o ir + a + infinitivo: `voy a hablar`)
- **Condicional**: `hablaria`, `comeria` (cortesia, conjetura, condicion)

### Voz activa vs. pasiva
- Preferir la voz activa sobre la pasiva en espanol, a menos que el agente sea desconocido o irrelevante:
  - `The report was written by Juan` → `Juan escribio el informe` (activa, preferida)
  - `El informe fue escrito por Juan` (pasiva, aceptable)
- La pasiva con `se` (pasiva refleja) es muy comun en espanol:
  - `Se vendieron todas las entradas.` (= Todas las entradas fueron vendidas.)

### Conectores y marcadores del discurso
- `ademas` (furthermore), `sin embargo` (however), `no obstante` (nevertheless)
- `por lo tanto` (therefore), `en consecuencia` (consequently)
- `por otra parte` (on the other hand), `asi mismo` (also, likewise)
- `en primer lugar` / `en segundo lugar` (firstly / secondly)
- `por ultimo` (finally), `en conclusion` (in conclusion)

---

## 9. Formulidad (Formality)

### Usted vs. Tu
- **Usted** (formal): para todos los contextos oficiales, comerciales, legales y tecnicos.
  - `Usted debe completar el formulario.`
  - `Le informamos que...`
  - `Agradecemos su colaboracion.`
  - Verbos en 3.ª persona del singular: `usted tiene`, `usted puede`, `usted debe`
- **Tu** (informal): para contextos privados, entre amigos, familia, ninos, aplicaciones B2C informales, redes sociales.
  - `Tu puedes hacerlo.`
  - `Completa el formulario.`
  - Verbos en 2.ª persona del singular: `tu tienes`, `tu puedes`
- **ADVERTENCIA**: No mezclar `usted` y `tu` dentro del mismo documento sin un cambio contextual claro.
- **Nivel cero de tolerancia**: La alternancia injustificada entre `usted` y `tu` es un error grave.

### Voseo (Argentina, Uruguay, partes de Centroamerica)
- En Argentina, Uruguay, Paraguay y partes de America Central, el **voseo** es la forma estandar de tratamiento informal:
  - Pronombre: `vos` (en lugar de `tu`)
  - Verbos: `vos tenes`, `vos podes`, `vos decis` (2.ª persona del singular con acentuacion llana)
  - Imperativo: `¡Veni!` (en lugar de `¡Ven!`), `¡Hablame!` (en lugar de `¡Habame!`)
  - `Vos sabes que te quiero.`
  - `Decime la verdad.`
- El voseo NO es un error; es una variedad regional legitima del espanol.
- Si el publico objetivo es argentino, usar **voseo**.
- Si el publico objetivo es internacional, usar **tu** (espanol neutro).
- NO mezclar `vos` y `tu` en el mismo texto (elegir uno segun el publico objetivo).

### Correspondencia formal (Formal Correspondence)
- **Aperturas de carta formal:**
  - `Estimado Sr. Garcia:` (mas formal, dos puntos)
  - `Estimado Sr. Garcia,` (menos formal, coma)
  - `Muy senor mio:` (muy formal, en desuso)
  - `A quien corresponda:` (destinatario desconocido)
  - `Distinguido/a Sr./Sra.:` (muy formal)
  - `Estimados senores:` (plural, generico)
- **Cierres de carta formal:**
  - `Atentamente,`
  - `Muy atentamente,`
  - `Cordialmente,` (comun en America Latina)
  - `Le saluda atentamente,`
  - `Reciba un cordial saludo,`
  - `Quedo a la espera de su respuesta,`
- **Estructura de carta formal:**
  ```
  Estimado Sr. Garcia:
  
  Le escribo para informarle...
  
  Atentamente,
  
  [Firma]
  [Nombre]
  ```

### Lenguaje inclusivo
- Evitar desdoblamientos innecesarios del tipo `los ninos y las ninas`.
- Preferir sustantivos colectivos o genericos: `la infancia`, `el alumnado`, `la ciudadania`, `la plantilla`
- Usar `-e` como desinencia de genero neutro solo en contextos donde sea politica del cliente.
- En documentos formales, usar el masculino generico por defecto (norma academica).

### Tratamiento de titulos y cargos
- `Don` / `Dona`: tratamiento de respeto ante nombre de pila
  - `Don Miguel de Cervantes`
  - `Dona Maria Zambrano`
- `Senor` / `Senora` / `Senorita`: ante apellido o cargo
  - `Sr. Garcia`, `Sra. Lopez`
- `Doctor` / `Doctora`: para titulados superiores
- `Licenciado` / `Licenciada`: comun en Mexico y Centroamerica
- `Ingeniero` / `Ingeniera`: para ingenieros

### Registro tecnico vs. coloquial
- **Textos tecnicos**: voz pasiva con `se`, nominalizaciones, terminologia especializada.
  - `El equipo se conecta a la fuente de alimentacion.`
- **Textos coloquiales**: voz activa, lenguaje sencillo, oraciones mas cortas.
  - `Conecta el equipo a la corriente.`
- **Publicidad**: creativo, a menudo con `tu`, idiomatico.
  - `Haz mas con tu dia.`

---

## 10. Artefactos de OCR (OCR Artifacts)

### Formato de etiqueta de restauracion: `[restaurado: ...]`
- Cuando una palabra esta corrupta, poco clara o ambigua debido a OCR, NO se debe adivinar en silencio.
- Usar la siguiente etiqueta:
  `[restaurado: {texto original} -> {correccion}, {motivo}]`

### Ejemplos
- `[restaurado: «configuracion» -> «configuracion», tilde anadida, el acento faltaba en el original]`
- `[restaurado: «l 000» -> «1 000», sustitucion de «l» latina por «1» segun contexto]`
- `[restaurado: «nino» -> «nino», restauracion de la virgulilla de la ene]`
- `[restaurado: texto ilegible, aproximadamente 3 palabras]`
- `[restaurado: «c¢mo» -> «como», caracter «¢» interpretado como letra corrupta, contexto: oracion afirmativa]`

### Cuando hay incertidumbre
- Si no se puede determinar el valor correcto con confianza, mantener el texto original corrupto y marcarlo:
  `[OCR: no se pudo determinar el valor original]`
- Ejemplo: `El parametro [OCR: no se pudo determinar el valor original] fue establecido.`

### Errores comunes de OCR en textos en espanol
- `n` vs `n` (la virgulilla es esencial en espanol):
  - `ano` (ano) vs `ano` (agujero) — ERROR GRAVE si se confunden
  - `senor` vs `senor`
  - `espanol` vs `espanol`
- Acentos perdidos:
  - `esta` (verbo) vs `esta` (demostrativo/adjetivo)
  - `sí` (afirmacion) vs `si` (condicional)
  - `él` (pronombre) vs `el` (articulo)
- `u` vs `u` (dieresis): `pingueino`, `cigueena`, `vergüenza`
  - La dieresis es especialmente vulnerable en OCR.
- Letras latinas confundidas con caracteres similares:
  - `0` vs `O`: `0,5 %` (numero) vs `Oscar` (letra)
  - `1` vs `l` (ele): `100` vs `lana`
  - `rn` reconocido como `m` y viceversa
- Palabras unidas: `en casa` -> `encasa`
- Palabras separadas: `ca sa` -> `casa`
- Guiones de particion al final de linea: `docu-\nmento` -> `documento`

### Principio general
- Es SIEMPRE mejor etiquetar una restauracion incierta que adivinar en silencio.
- La marcacion correcta con reconocimiento de incertidumbre NO es un defecto, sino una buena practica.

---

## 11. Filosofia de traduccion (Translation Philosophy)

Tres principios fundamentales para la traduccion al espanol:

### Primer principio: Precision (Fidelity — Fidelidad)
Los valores numericos, las fechas, los nombres propios y los terminos tecnicos deben ser EXACTOS.
- `100,00` debe seguir siendo `100,00`, nunca `100.00`
- `15/03/2024` debe seguir siendo `15/03/2024`, nunca `03/15/2024`
- `Microsoft Corporation` se mantiene como `Microsoft Corporation`
- Sin omisiones, sin anadidos, sin parafrasis de datos cuantitativos.
- Ante la duda sobre cualquier hecho o cifra, marcarlo en lugar de adivinarlo.

### Segundo principio: Naturalidad (Naturalness — Naturalidad)
La traduccion debe leerse como un texto original en espanol, no como un calco del idioma fuente.
- Evitar los anglicismos donde existan equivalentes espanoles establecidos:
  - `email` -> `correo electronico` (formal) o `correo` (informal)
  - `feedback` -> `comentarios`, `retroalimentacion`, `opinion`
  - `meeting` -> `reunion` (no `meet` o `meeting`)
  - `implementar` -> aceptable (RAE lo admite), pero mejor `poner en practica` / `aplicar`
  - `chequear` -> `verificar`, `comprobar`, `revisar`
  - `performance` -> `rendimiento`, `desempeno`
  - `target` -> `objetivo`, `meta`, `destino`
  - `deadline` -> `fecha limite`, `plazo`
- Usar el orden de palabras natural del espanol (sujeto-verbo-objeto es flexible; el tiempo suele ir al principio).
  - `The meeting will take place on Friday at 10 AM` -> `La reunion tendra lugar el viernes a las 10:00 h` / `El viernes a las 10:00 h tendra lugar la reunion`

### Tercer principio: Estilo (Elegance — Estilo)
Mas alla de la precision y la naturalidad, buscar la calidad estilistica adecuada al tipo de documento.
- **Documentos formales**: dignos, precisos, con las formulas establecidas del lenguaje juridico/administrativo.
  - `Por medio de la presente...`, `En virtud de lo anterior...`, `De conformidad con...`
- **Documentos tecnicos**: terminologia clara y consistente, instrucciones en imperativo.
  - `Presione Enter`, `Seleccione el archivo`, `Haga clic en Aceptar`
- **Marketing/publicidad**: atractivo, creativo, dentro de los limites de las normas estilisticas del espanol.
- **Comunicacion interna**: profesional pero accesible.

### Orden de prioridad: Precision > Naturalidad > Estilo
Cuando estos principios entren en conflicto (p. ej., una traduccion literal sonaria poco natural), la precision es lo primero. Pero siempre buscar una forma de ser preciso Y natural.

### Cumplimiento de la RAE (Real Academia Espanola)
- Todas las traducciones deben ajustarse a las normas de la Real Academia Espanola.
- En caso de duda, consultar:
  - `Diccionario de la lengua espanola` (DLE): https://dle.rae.es/
  - `Diccionario panhispanico de dudas` (DPD): https://www.rae.es/dpd/
  - `Ortografia de la lengua espanola` (2010)
  - `Nueva gramatica de la lengua espanola` (2009)
- Para el espanol americano, tener en cuenta las variantes regionales recogidas por la Asociacion de Academias de la Lengua Espanola (ASALE).

### Lista de verificacion para cada parrafo:
1. Son correctos todos los numeros, fechas y monedas? (Precision)
2. Suena a espanol natural? (Naturalidad)
3. El tono es apropiado para el tipo de documento? (Estilo)
4. Se han evitado los anglicismos innecesarios?
5. Las tildes, la virgulilla de la n y la dieresis estan correctamente colocadas?
6. Los signos de interrogacion y exclamacion estan correctamente abiertos y cerrados?
7. La concordancia de genero y numero es correcta?
8. Se ha usado el registro de formalidad adecuado (usted/tu/vos)?

### Falsos amigos comunes (False Friends)
| Ingles | Traduccion erronea | Traduccion correcta |
|--------|-------------------|---------------------|
| `actually` | actualmente | en realidad, de hecho |
| `assist` | asistir (a un evento) | ayudar, prestar asistencia |
| `attend` | atender | asistir (a un evento) |
| `billion` | billon | mil millones (millardo) |
| `carpet` | carpeta | alfombra, moqueta |
| `constipated` | constipado | extrenido |
| `conduct` | conducta | realizar, llevar a cabo |
| `deception` | decepcion | engano, fraud |
| `embarrassed` | embarazada | avergonzado |
| `exit` | exito | salida |
| `fabric` | fabrica | tela, tejido |
| `injury` | injuria | lesion, dano |
| `lecture` | lectura | conferencia, clase magistral |
| `library` | libreria | biblioteca |
| `notice` | noticia | aviso, darse cuenta |
| `record` | record | registro, grabar |
| `sensible` | sensible | sensato, razonable |
| `success` | suceso | exito |
| `trivial` | trivial | insignificante, sin importancia |

---

**Historial de cambios**
| Fecha | Version | Cambio |
|-------|---------|--------|
| 2026-05-25 | 1.0 | Creacion inicial — Convenciones basicas para es-ES / espanol internacional |
