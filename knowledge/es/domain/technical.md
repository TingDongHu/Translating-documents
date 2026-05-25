# Domain: Technical (Spanish — ES)

## Reader Model

**Primary Reader:** Ingeniero técnico / Especialista en normalización (technical engineer or standardization specialist), 30–55 years old, familiar with UNE and ISO frameworks. Expects precise equivalents for technical concepts, SI-unit integrity, and formal register.  
**Secondary Reader:** Supervisor de calidad or regulatory auditor who cross-references the Spanish text against the original EN/ISO source. Looks for terminological consistency with existing UNE-EN ISO standards.  
**Tertiary Reader:** End-user or technician in a Taller mecánico / Laboratorio who requires unambiguous procedural language, warnings formatted to UNE-EN 82079-1, and zero ambiguity in measurements.

**Reader expectations:**
- Every technical term must map to its UNE-EN ISO equivalent where one exists (e.g., *resistencia a la tracción* not *fuerza de estiramiento*).
- SI units are never translated; they are preserved as-is with a non-breaking space before the unit symbol.
- Warnings follow the pyramid: PELIGRO > ADVERTENCIA > ATENCIÓN > AVISO, never mixing severity levels.
- Procedures use the impersonal *se* or infinitive, not *tú/usted* imperative.
- Passive constructions are avoided unless they appear in the source standard.

---

## Decision Framework

### Table T1: Standards designation — Translating standard references
| Source (EN) | Target (ES) | Rule |
|---|---|---|
| ISO 9001:2015 | ISO 9001:2015 | Standard numbers are never translated; keep original |
| EN 60204-1 | EN 60204-1 | Same rule applies to EN prefixes |
| IEC 61131-3 | IEC 61131-3 | International prefixes kept verbatim |
| ISO/TS 16949 | ISO/TS 16949 | All prefix variants (ISO/TS, ISO/IEC, ISO/TR) preserved |
| UNE-EN ISO 12100 | UNE-EN ISO 12100 | When cited in Spanish text the UNE prefix may be prepended |
| "shall comply with" | "deberá cumplir con" | *Shall* → *deberá* (obligation, not future tense) |
| "should be considered" | "debe considerarse" | *Should* → *debe* (recommendation, *debería* is weaker) |
| "may be used" | "podrá utilizarse" | *May* permission → *podrá* |
| "can cause" | "puede causar" | *Can* possibility → *puede* |
| "it is recommended" | "se recomienda" | Impersonal *se* for recommendations |
| "as specified in" | "según lo especificado en" | Standard cross-reference formula |
| "normative reference" | "referencia normativa" | Fixed term for standard bibliographies |
| "informative annex" | "anexo informativo" | *Annex* → *anexo* (not *apéndice*) |

### Table T2: Warning and safety signal words
| Source (EN) | Target (ES) | Usage context |
|---|---|---|
| DANGER | PELIGRO | Imminent hazard; death or serious injury |
| WARNING | ADVERTENCIA | Potential hazard; death or serious injury |
| CAUTION | ATENCIÓN | Minor or moderate injury |
| NOTICE | AVISO | Property damage only, no personal injury |
| "Do not" | "No" + infinitive | Prohibition: *No tocar*, *No desmontar* |
| "Keep away from" | "Mantener alejado de" | Safety distance instruction |
| "Read carefully" | "Leer atentamente" | Pre-operation instruction |
| "Ground connection required" | "Es necesaria la conexión a tierra" | Mandatory safety action |
| "Disconnect power" | "Desconectar la alimentación" | Procedural warning |
| "Hot surface" | "Superficie caliente" | Hazard label |
| "Wear protective" | "Usar equipo de protección" | PPE mandate: *protección* not *protector* |
| "Flammable material" | "Material inflamable" | *Inflamable* (false friend alert: not *inflamable* = *not flammable*) |
| "Toxic fumes" | "Gases tóxicos" | Health hazard warning |
| "Risk of electric shock" | "Riesgo de descarga eléctrica" | Electrical hazard |
| "Lockout/Tagout" | "Bloqueo/Etiquetado" | LOTO procedure translation |

### Table T3: Measurement and SI units
| Source (EN) | Target (ES) | Rule |
|---|---|---|
| 10 mm | 10 mm | Unit symbol unchanged; non-breaking space before symbol |
| 3.5 V | 3,5 V | Decimal comma (Spanish locale) for prose; keep dot in tables if source uses dot |
| 1,000 rpm | 1000 r/min | *rpm* is understood but *r/min* is SI-preferred in official standards |
| 20 °C | 20 °C | Degree symbol with NBSP; *Celsius* not *centígrados* |
| 100 kPa | 100 kPa | Pressure units preserved |
| 5 l/min | 5 l/min | Flow rate; *l/min* acceptable (SI: *L/min* or *l/min*) |
| 230 V AC | 230 V CA | *AC* → *CA* (corriente alterna); *DC* → *CC* (corriente continua) |
| 50/60 Hz | 50/60 Hz | Frequency preserved |
| N·m | N·m | Torque unit with centre-dot |
| mg/m³ | mg/m³ | Concentration units preserved |
| % RH | % HR | *RH* → *HR* (humedad relativa) |
| 24 h | 24 h | Hour remains *h* |
| IP54 | IP54 | IP rating codes preserved |
| "approximately" | "aproximadamente" | Rounding/estimation qualifier |
| "nominal value" | "valor nominal" | Specified vs measured distinction |

### Table T4: Technical verb selection
| Source (EN) | Target (ES) | Registers |
|---|---|---|
| to assemble | montar | Mechanical assembly |
| to install | instalar | Electrical/system installation |
| to connect | conectar | Electrical connection |
| to configure | configurar | Software / parameter settings |
| to adjust | ajustar | Mechanical/electronic adjustment |
| to calibrate | calibrar | Metrology contexts |
| to verify | verificar | Checking compliance (preferred over *comprobar* in standards) |
| to validate | validar | Formal validation |
| to measure | medir | Taking measurements |
| to calculate | calcular | Computation |
| to tighten | apretar | Fastener torque (not *estrechar*) |
| to loosen | aflojar | Opposite of tightening |
| to secure | fijar | Fastening in position |
| to remove | retirar | Disassembly / removal |
| to replace | sustituir | Replacement part contexts |
| to ensure | asegurarse de que | *Ensure* + clause (not *asegurar* alone) |

### Table T5: Technical nouns and false friends
| Source (EN) | Target (ES) | Notes |
|---|---|---|
| specification | especificación | Preferred over *especificación técnica* when clear |
| requirement | requisito | *Requisito* (not *requerimiento* in standards) |
| compliance | conformidad | *Conformidad* for standards; *cumplimiento* for legal |
| tolerance | tolerancia | Dimensional tolerance |
| deviation | desviación | Statistical or dimensional deviation |
| defect | defecto | Non-conformance |
| failure | fallo | Functional failure (not *falla*, which is LatAm) |
| component | componente | General part |
| assembly | conjunto | Assembled unit (not *ensamblaje*) |
| subassembly | subconjunto | Hierarchical part structure |
| drawing | plano | Engineering drawing (not *dibujo*) |
| dimension | dimensión / cota | *Cota* on drawings; *dimensión* in text |
| thread | rosca | Screw thread (not *hilo*) |
| fastener | elemento de fijación | Generic; *tornillo* for screw specifically |
| gasket | junta | Sealing gasket |
| bearing | rodamiento | Rolling bearing (not *cojinete* which is bushing) |
| current | corriente | Electrical current |
| voltage | tensión | *Tensión* (not *voltaje* in formal standards) |

### Table T6: Procedure and instruction style
| Aspect | Source (EN) style | Target (ES) style |
|---|---|---|
| Step header | "Step 1:" | "Paso 1:" or "1." |
| Action verb | "Turn the knob" | "Girar el mando" (infinitive) or "Gire el mando" (formal imperative) |
| Condition | "If X occurs" | "Si se produce X" |
| Result | "The light turns green" | "El indicador se pondrá en verde" |
| List item | Bullet-point action | Viñeta + infinitive or *se* impersonal |
| Precondition | "Before starting" | "Antes de comenzar" |
| Postcondition | "After completion" | "Una vez finalizado" |
| Note | "NOTE:" | "NOTA:" |
| Tip | "TIP:" | "CONSEJO:" |
| Caution | "CAUTION:" | "ATENCIÓN:" |
| Cross-ref | "See section 4.2" | "Véase la sección 4.2" |
| Figure callout | "See Figure 3" | "Véase la figura 3" |
| Table callout | "See Table 1" | "Véase la tabla 1" |
| Equation ref | "Equation (5)" | "Ecuación (5)" |

### Table T7: Technical abbreviations
| Source (EN) | Target (ES) | Notes |
|---|---|---|
| e.g. | p. ej. | *por ejemplo* |
| i.e. | es decir | *id est* → explanatory; avoid *o sea* |
| etc. | etc. | Same, but minimise in technical prose |
| vs. | frente a / vs. | *versus* — both used; *frente a* preferred in formal |
| max. | máx. | Abbreviation: *máximo* |
| min. | mín. | Abbreviation: *mínimo* |
| approx. | aprox. | *aproximadamente* |
| temp. | temp. | *temperatura* — acceptable in tables |
| no. | n.º | *número* with masculine ordinal indicator |
| Fig. | Fig. | *Figura* — same abbreviation |
| Sect. | Sec. | *Sección* |
| Chap. | Cap. | *Capítulo* |
| App. | Ap. | *Apéndice* (rare in standards; use *Anexo*) |
| OEM | OEM | Kept as-is |
| PLC | PLC | Kept as-is (programmable logic controller) |

### Table T8: Passive voice and impersonal constructions
| Source (EN) | Target (ES) | Notes |
|---|---|---|
| "The button is pressed" | "Se pulsa el botón" | Impersonal *se* preferred |
| "It is recommended" | "Se recomienda" | Standard impersonal formula |
| "It must be ensured" | "Debe asegurarse" | *Debe* + infinitive + *se* |
| "The machine is operated" | "La máquina se maneja" | Passive *se* |
| "The test was performed" | "Se realizó el ensayo" | Past impersonal |
| "Is used to" | "Sirve para / Se utiliza para" | Impersonal purpose |
| "Can be adjusted" | "Puede ajustarse" | *Puede* + infinitive + *se* |
| "Should be checked" | "Debe comprobarse" | Recommendation + *se* |
| "Was designed to" | "Se diseñó para" | Past impersonal |
| "Is known as" | "Se conoce como" | Impersonal naming |
| "Is defined as" | "Se define como" | Definition formula |
| "Is considered" | "Se considera" | Impersonal opinion |
| "Is required" | "Se requiere / es necesario" | Requirement expression |
| "Has been tested" | "Se ha ensayado" | Present perfect impersonal |

### Table T9: Punctuation and typography in technical Spanish
| Element | Rule | Example |
|---|---|---|
| Decimal separator | Comma in running text | 3,14 m (not 3.14 m) |
| Thousands separator | Period or space | 1.234 or 1 234 (never comma) |
| NBSP before unit | Non-breaking space | 25 °C, 10 mm, 5 kg |
| NBSP before % | Non-breaking space | 15 % (not 15%) |
| Lists | Semicolon after each item except last | "rojo; azul; y verde" |
| En-dash for ranges | En-dash without spaces | 10–20 mm |
| Degree symbol | NBSP + ° + C | 25 °C |
| Quotation marks | Spanish angular « » for titles | «Norma UNE-EN ISO 9001» |
| Parenthetical ( ) | As in English | (véase la tabla 2) |
| Capitalisation rules | Titles: sentence case; standards: title case on first word only | *Requisitos generales* not *Requisitos Generales* |
| Bold for warnings | Bold signal word | **PELIGRO:** or **ADVERTENCIA:** |
| Colon after signal word | Colon and space | "ADVERTENCIA: Riesgo de..." |

### Table T11: Electrical and electronic engineering terms
| Source (EN) | Target (ES) | Notes |
|---|---|---|
| circuit breaker | interruptor automático / disyuntor | *Interruptor magnetotérmico* (MCB); *disyuntor diferencial* (RCD) |
| switch | interruptor | General switch |
| selector switch | conmutador | Multi-position switch |
| push button | pulsador | Momentary contact |
| relay | relé | Electromechanical relay |
| contactor | contactor | Power switching |
| transformer | transformador | Voltage transformation |
| motor | motor | Electric motor |
| generator | generador / alternador | *Generador* (DC); *alternador* (AC) |
| sensor | sensor | Not *censor* |
| actuator | actuador | Motion/output device |
| transducer | transductor | Measurement converter |
| controller | controlador | *PLC* or *controlador lógico programable* |
| inverter | inversor | DC→AC conversion |
| rectifier | rectificador | AC→DC conversion |
| converter | convertidor | General power conversion |
| fuse | fusible | Overcurrent protection |
| overload relay | relé térmico / relé de sobrecarga | Motor protection |
| cable | cable | *Cable eléctrico* |
| conductor | conductor | Wire/cable conducting material |
| insulation | aislamiento | Dielectric insulation |
| grounding / earthing | toma de tierra / puesta a tierra | *Conexión a tierra* |
| bonding | conexión equipotencial | Equipotential bonding |
| shield | blindaje | EMI/RFI shielding |
| enclosure | envolvente / armario | *Grado de protección IP* |
| terminal block | regleta de bornes / bornero | Connection terminal |
| connector | conector | Plug/socket connector |

### Table T12: Mechanical engineering terms
| Source (EN) | Target (ES) | Notes |
|---|---|---|
| shaft | eje | Rotating shaft |
| axle | eje | Stationary axle (same word, context disambiguates) |
| gear | engranaje | Toothed wheel |
| gearbox | caja de engranajes / reductor | Speed reducer |
| belt drive | transmisión por correa | Belt system |
| chain drive | transmisión por cadena | Chain system |
| pulley | polea | Grooved wheel for belt |
| sprocket | rueda dentada / piñón | For chain |
| coupling | acoplamiento | Shaft coupling |
| clutch | embrague | Engaging/disengaging power |
| brake | freno | *Freno de disco / de tambor / electromagnético* |
| piston | pistón / émbolo | Reciprocating component |
| cylinder | cilindro | *Cilindro hidráulico / neumático* |
| valve | válvula | *Válvula de compuerta / de bola / de mariposa* |
| pump | bomba | *Bomba centrífuga / de engranajes / de pistones* |
| pipe | tubería | Piping system |
| tube | tubo | Small-diameter tube |
| flange | brida | Pipe connection flange |
| gasket | junta | Sealing element |
| seal | sello / retén | *Retén* for rotating shafts |
| bearing | rodamiento / cojinete | *Rodamiento* (rolling); *cojinete* (plain) |
| spring | muelle / resorte | *Muelle* more common in Spain |
| washer | arandela | *Arandela plana / de presión / Grower* |
| nut | tuerca | Hexagonal nut |
| bolt | tornillo | Bolt with nut |
| screw | tornillo | Screw (into threaded hole) |
| rivet | remache | Permanent fastener |
| weld | soldadura | *Soldadura por arco / MIG / TIG* |
| torque | par de apriete | Tightening torque |
| press fit | ajuste a presión | Interference fit |
| clearance | holgura | Clearance fit |

### Table T13: Quality control and inspection terminology
| Source (EN) | Target (ES) | Notes |
|---|---|---|
| quality assurance | aseguramiento de la calidad | QA — systemic |
| quality control | control de calidad | QC — product inspection |
| quality management system | sistema de gestión de la calidad | SGC / ISO 9001 |
| inspection | inspección | *Inspección visual / dimensional / funcional* |
| test | ensayo / prueba | *Ensayo* preferred in standards; *prueba* general |
| non-destructive testing | ensayos no destructivos (END) | *END* = NDT |
| destructive testing | ensayos destructivos | Mechanical/chemical |
| sampling | muestreo | Statistical sampling |
| acceptance criteria | criterios de aceptación | Pass/fail thresholds |
| non-conformance | no conformidad (NC) | *NC* abbreviation common |
| corrective action | acción correctiva | Root cause fix |
| preventive action | acción preventiva | Proactive measure |
| calibration | calibración | Instrument accuracy verification |
| traceability | trazabilidad | Measurement chain of custody |
| measurement uncertainty | incertidumbre de medida | Metrology concept |
| capability index | índice de capacidad | *Cp / Cpk* |
| control chart | gráfico de control | SPC tool |
| Pareto analysis | análisis de Pareto | 80/20 principle |
| Ishikawa diagram | diagrama de Ishikawa / causa-efecto | Fishbone diagram |
| FMEA | AMFE | *Análisis Modal de Fallos y Efectos* |
| PPAP | PPAP | *Proceso de Aprobación de Piezas de Producción* (kept in English) |
| APQP | APQP | *Planificación Avanzada de la Calidad* (kept in English) |
| 8D report | informe 8D | Problem-solving methodology |
| first article inspection | inspección de primera pieza | First-off inspection |

### Table T14: Software and IT technical terminology
| Source (EN) | Target (ES) | Notes |
|---|---|---|
| software | software | Masculine: *el software*; plural: *los software* |
| hardware | hardware | Masculine; *soporte físico* exists but rare |
| firmware | firmware | Kept as is |
| application | aplicación / programa | *App* for mobile (short form) |
| user interface | interfaz de usuario | *Interfaz* is feminine: *la interfaz* |
| graphical user interface | interfaz gráfica de usuario (GUI) | GUI |
| command line | línea de comandos | CLI |
| database | base de datos (BD) | *BD* abbreviation |
| server | servidor | Hardware or software context |
| client | cliente | *Arquitectura cliente-servidor* |
| network | red | *Red local (LAN) / Red de área amplia (WAN)* |
| protocol | protocolo | *Protocolo de comunicación* |
| encryption | cifrado / encriptación | *Cifrado* preferred in standards |
| decryption | descifrado | Reverse of encryption |
| authentication | autenticación | Identity verification |
| authorisation | autorización | Permission/access rights |
| backup | copia de seguridad / backup | *Copia de seguridad* preferred |
| restore | restauración | Data recovery |
| update | actualización | Software update |
| upgrade | actualización / mejora | Version upgrade |
| patch | parche | Security/functionality patch |
| debugging | depuración | *Depuración de código* |
| compilation | compilación | Code compilation |
| algorithm | algoritmo | Preserved |
| parameter | parámetro | Configuration variable |
| variable | variable | Programming variable |
| function | función | Programming function |
| subroutine | subrutina | Called routine |
| loop | bucle | Repetition structure |
| string | cadena | *Cadena de caracteres* |
| array | matriz / array | *Matriz* preferred; *array* understood |
| object | objeto | Object-oriented programming |
| class | clase | OOP class |
| instance | instancia | OOP instance |
| library | biblioteca | Code library |
| framework | marco de trabajo / framework | *Framework* common in IT |
| API | API (Interfaz de Programación de Aplicaciones) | *API* kept; define on first use |

### Table T15: Chemical and process engineering terms
| Source (EN) | Target (ES) | Notes |
|---|---|---|
| chemical substance | sustancia química | Preserved |
| compound | compuesto | Chemical compound |
| mixture | mezcla | Not *mixtura* (archaic) |
| solution | disolución | Liquid solution |
| solvent | disolvente | Dissolving medium |
| concentration | concentración | *g/L, mol/L, %* |
| pH | pH | Kept as *pH* |
| reaction | reacción | *Reacción química / exotérmica / endotérmica* |
| catalyst | catalizador | Reaction accelerator |
| inhibitor | inhibidor | Reaction retarder |
| corrosion | corrosión | Material degradation |
| oxidation | oxidación | Chemical oxidation |
| reduction | reducción | Chemical reduction |
| combustion | combustión | Burning process |
| explosion | explosión | *Atmósfera explosiva (ATEX)* |
| flammable limit | límite de inflamabilidad | *LIE / LSE* (lower/upper) |
| flash point | punto de inflamación | Ignition temperature |
| autoignition temperature | temperatura de autoignición | Self-ignition |
| toxicity | toxicidad | *Tóxico / muy tóxico* |
| carcinogenic | cancerígeno | Not *carcinogénico* (anglicism) |
| mutagenic | mutágeno | Genetic mutation risk |
| corrosive | corrosivo | Hazard class |
| irritant | irritante | Hazard class |
| safety data sheet | ficha de datos de seguridad (FDS) | MSDS/SDS |
| GHS | SGA | *Sistema Globalmente Armonizado* |
| hazard pictogram | pictograma de peligro | GHS symbols |
| H phrase | indicación de peligro / frase H | *Frases H* (Hazard statements) |
| P phrase | consejo de prudencia / frase P | *Frases P* (Precautionary statements) |

### Table T16: Technical drawing and CAD terminology
| Source (EN) | Target (ES) | Notes |
|---|---|---|
| technical drawing | dibujo técnico | Academic/engineering discipline |
| engineering drawing | plano técnico | Production drawing |
| CAD | CAD (Diseño Asistido por Ordenador) | *CAD* kept; define on first use |
| 2D drawing | dibujo 2D / plano 2D | Two-dimensional |
| 3D model | modelo 3D | Three-dimensional model |
| solid model | modelo sólido | Solid modelling |
| surface model | modelo de superficies | Surface modelling |
| assembly drawing | plano de conjunto | Multiple parts |
| detail drawing | plano de detalle | Single part |
| exploded view | vista explosionada | Assembly sequence |
| section view | vista en sección / corte | Cross-section |
| detail view | vista de detalle | Magnified area |
| dimension line | línea de cota | Measurement line |
| extension line | línea de referencia | Projection line |
| centre line | eje / línea de centro | Symmetry axis |
| hidden line | arista oculta | Dashed line convention |
| cutting plane | plano de corte | Section indicator |
| tolerance | tolerancia | *Tolerancia dimensional / geométrica* |
| GD&T | tolerancias geométricas | *ISO 1101* (not ASME Y14.5 in Spain) |
| surface finish | acabado superficial | *Rugosidad superficial / Ra* |
| welding symbol | símbolo de soldadura | Per ISO 2553 |
| datum | referencia / datum | Datum system per ISO 5459 |
| scale | escala | *Escala 1:1 / 1:2 / 2:1* |
| projection | proyección | *Método del primer diedro (ISO E)* |
| title block | cajetín / rótulo | Drawing information block |
| revision | revisión | Drawing revision letter/number |
| material specification | especificación de material | Material callout |
| Bill of Materials | lista de materiales / despiece | BOM |

### Table T17: Occupational safety and health (PRL)
| Source (EN) | Target (ES) | Notes |
|---|---|---|
| occupational safety | prevención de riesgos laborales (PRL) | *Ley 31/1995* |
| risk assessment | evaluación de riesgos | Mandatory per PRL law |
| hazard | peligro | Source of potential harm |
| risk | riesgo | Likelihood × severity |
| personal protective equipment | equipo de protección individual (EPI) | PPE |
| protective helmet | casco de protección | Head protection |
| safety glasses | gafas de seguridad | Eye protection |
| ear plugs | tapones auditivos | Hearing protection |
| respirator | mascarilla / respirador | Breathing protection |
| safety harness | arnés de seguridad | Fall protection |
| safety shoes | calzado de seguridad | Foot protection |
| protective gloves | guantes de protección | Hand protection |
| safety sign | señal de seguridad | *Señal de prohibición / obligación / advertencia / salvamento* |
| emergency exit | salida de emergencia | *Salida de emergencia* sign |
| fire extinguisher | extintor | Fire-fighting equipment |
| first aid | primeros auxilios | Medical assistance |
| emergency plan | plan de emergencia | *Plan de autoprotección* |
| evacuation | evacuación | Emergency evacuation |
| assembly point | punto de reunión | Post-evacuation meeting |
| work at height | trabajo en altura | Elevated work |
| confined space | espacio confinado | Limited access area |
| manual handling | manipulación manual de cargas | Ergonomics |
| repetitive strain injury | lesión por esfuerzo repetitivo | Ergonomics injury |
| noise exposure | exposición al ruido | *Nivel diario equivalente* |
| vibration | vibración | Hand-arm / whole-body |
| hazardous substance | sustancia peligrosa | Chemical risk |
| safety coordinator | coordinador de seguridad | Construction safety role |
| health surveillance | vigilancia de la salud | Medical monitoring |
| accident investigation | investigación de accidentes | Root cause analysis |
| near miss | incidente / casi accidente | *Cuasi accidente* |

### Table T10 (expanded): Materials and properties lexicon
| Source (EN) | Target (ES) | Notes |
|---|---|---|
| stainless steel | acero inoxidable | *AISI 304* → *1.4301* (EN 10027) |
| carbon steel | acero al carbono | Common structural steel |
| aluminium | aluminio | Note: US *aluminum* → ES *aluminio* |
| copper | cobre | Preserved |
| brass | latón | Copper-zinc alloy |
| bronze | bronce | Copper-tin alloy |
| plastic | plástico | Generic; specify polymer when known |
| rubber | caucho | Elastomeric material |
| ceramic | cerámica | Preserved |
| glass | vidrio | Not *cristal* for industrial glass |
| tensile strength | resistencia a la tracción | Mechanical property |
| hardness | dureza | Rockwell/Brinell/Vickers |
| yield strength | límite elástico | *Re* in standard notation |
| elongation | alargamiento | Percentage elongation at break |
| density | densidad | Mass per volume |
| viscosity | viscosidad | Fluid property |
| conductivity | conductividad | Thermal/electrical |

---

## Standard Conventions

1. **UNE standard reference formula:** Always cite as *UNE-EN ISO XXXX* when the Spanish adoption exists. The order of prefixes is UNE-EN-ISO (or UNE-EN when no ISO equivalent). When the Spanish adoption does not exist, cite the original ISO/EN number. Use *de fecha* for dated references: *Norma UNE-EN ISO 9001:2015*. For undated references omit the year. Never translate standard numbers, but the word *Norma* may precede the standard designation in running Spanish text.

2. **Shall/Should/May mapping:** *Shall* maps to *deberá* (future indicative of obligation, strong obligation per ISO/IEC Directives Part 2). *Should* maps to *debe* (present indicative, recommendation). *May* maps to *podrá* (future of permission, allowing an option). *Can* (possibility) maps to *puede*. This follows the UNE translation guidelines for ISO/IEC standards, which explicitly distinguish between requirement (*deberá*), recommendation (*debe*), permission (*podrá*), and possibility (*puede*). Never use *debería* for *should* in standards — it is too weak and non-standard.

3. **Safety signal word hierarchy:** DANGER → PELIGRO, WARNING → ADVERTENCIA, CAUTION → ATENCIÓN, NOTICE → AVISO. Never translate a lower-level word upward (e.g., CAUTION must never become PELIGRO). Signal words should appear in bold, all caps, followed by a colon. The hierarchy is defined in UNE-EN 82079-1 (preparation of instructions) and ANSI Z535 (adopted widely in Spain through UNE standards). For product labelling, also consider the GHS pictograms and H/P phrases for chemical products per *Reglamento (CE) 1272/2008 (CLP)*.

4. **Impersonal register:** Use *se* impersonal or infinitive for procedural steps; avoid second-person (*usted/tú*) unless the source is explicitly a user manual aimed at consumer goods where *usted* is conventional. For industrial and professional documentation, the impersonal register is non-negotiable. Examples: *Se debe conectar el cable* not *Usted debe conectar el cable*; *Ajustar el par a 10 N·m* not *Ajusta el par a 10 N·m*.

5. **SI-unit integrity:** Unit symbols are never localised (always *mm*, *kg*, *s*, *A*, *K*, *mol*, *cd*). Decimal comma applies in prose; decimal point is acceptable in tables when the source uses a point. Non-breaking space mandatory between numeric value and unit symbol. For derived units, the SI conventions apply: *N·m* (newton metre), *m/s²* (metre per second squared), *kg/m³* (kilogram per cubic metre). Prefixes are standard: *k* (kilo), *M* (mega), *G* (giga), *m* (milli), *µ* (micro), *n* (nano). Note: Spanish uses *hora* for hour but the symbol *h* remains unchanged.

6. **False friends — critical list for technical translators:** *Sensor* ≠ *censor* (censor); *eventualmente* ≠ *eventually* (it means *possibly*); *embarazada* never used technically; *fábrica* = factory, *fabricar* = to manufacture; *sensible* ≠ sensible (it means *sensitive*); *actual* ≠ actual (it means *current/prevailing*); *asistir* ≠ assist (it means *attend*); *constipación* ≠ constipation (it means *a cold*); *éxito* ≠ exit (it means *success*); *bombero* ≠ bomber (it means *firefighter*); *carpeta* ≠ carpet (it means *folder*); *mantel* ≠ mantle (it means *tablecloth*); *oficina* ≠ office *in the sense of function* (it means *physical office*); *pretender* ≠ pretend (it means *to attempt/to seek*).

7. **Terminological consistency:** Within a single document, the same English term must always map to the same Spanish term. A terminology table (glosario) must be created at project start and adhered to throughout. If the source uses *component*, *part*, and *piece* as synonyms, the target must not introduce three different Spanish terms unless they correspond to specific terms in the source. Use a bilingual concordance tool to verify 1:1 mapping.

8. **Abbreviations:** Always define on first use: "controlador lógico programable (PLC)". Use Spanish expansion when available; keep the abbreviation if it is universally known (PLC, LED, CAD, CNC, SCADA, HMI). Spanish-language acronyms should be created from the Spanish expansion if the abbreviation will appear repeatedly and the Spanish reader would not recognise the English acronym: e.g., *Sistema Globalmente Armonizado (SGA)* for GHS. However, for highly internationalised contexts, the English acronym is often preserved (e.g., *PLC*, *CNC*, *HMI*).

9. **Numerical ranges:** Use en-dash (–) without spaces: 10–20 mm, 230–400 V, –10 °C to +40 °C. For inclusive ranges in running text use "de 10 a 20 mm". Avoid using a hyphen for ranges, as it can be confused with a minus sign. For temperature ranges with negative values, use "de –10 °C a +40 °C" rather than "–10 – +40 °C".

10. **Cross-references:** Use *véase* (singular) or *véanse* (plural) for "see". Use *remítase a* for "refer to". Section numbers are written in lowercase: *sección 4.2.1*, *véase la sección 4.2.1*. Cross-references to standards follow the pattern *véase la norma UNE-EN ISO 12100*. For figures: *véase la figura 3*. For tables: *véase la tabla 1*. For equations: *véase la ecuación (5)*. For annexes: *véase el anexo A*.

11. **Punctuation in lists:** In vertical lists, each item starts with a lowercase letter (unless it is a complete sentence) and ends with a semicolon except the last, which ends with a period. Use *y* or *o* before the last item. Example: *El sistema incluye: a) el controlador; b) la interfaz de usuario; y c) los sensores.*

12. **Document numbering and revision:** Technical documents in Spain follow UNE 157001 (general criteria for technical reports) or UNE 166002 (R&D projects). Document numbers include project code, document type, and revision: *PROY-001-MN-01 Rev. A*. Revision letters: A (draft), B (first issue), C onwards (revisions). The revision block on drawings and documents must include: *Rev., Fecha, Descripción de la modificación, Realizado, Verificado, Aprobado*.

13. **Units of measurement for specific domains:** In construction: mm and m (not cm for primary dimensions except in finishes).  In thermodynamics: °C for Celsius, K for Kelvin (without degree symbol). In lighting: lm (lumen), lx (lux), cd (candela). In acoustics: dB(A) for sound pressure level. In hydraulics: bar (common) or Pa (SI). The use of *kgf/cm²* is deprecated; use bar or Pa.

14. **Typographic conventions for chemical formulas:** Chemical element symbols follow standard capitalisation (H₂O, CO₂, H₂SO₄). Subscripts and superscripts are preserved. Oxidation states in parentheses: *hierro (III)*. Use *→* for reaction arrows and *⇌* for equilibrium. Never translate chemical element names inside formulas: *NaCl* stays *NaCl* not *ClNa*.

15. **Gender of technical terms in Spanish:** Some technical terms have specific genders that may not be obvious: *el análisis* (masculine), *la base de datos* (feminine), *el calor* (masculine), *la corriente* (feminine), *el diagrama* (masculine), *la interfaz* (feminine), *el mapa* (masculine), *la red* (feminine), *el sistema* (masculine), *la tensión* (feminine). These must always be used with the correct article. When introducing acronyms, the gender follows the head noun: *la API* (la Interfaz de Programación), *el PLC* (el Controlador Lógico Programable).
