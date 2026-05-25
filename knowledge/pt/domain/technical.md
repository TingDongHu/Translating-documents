---
id: pt/domain/technical
type: domain
target_lang: pt
name: Documentos técnicos (português)
description: Terminologia e regras para documentos técnicos traduzidos para português brasileiro e português europeu. Cobertura de normas ABNT (BR), NP (PT), padrões ISO/IEC, segurança, unidades SI e redação técnica.
---

# Reader Model: Leitor de Documentos Técnicos

## Perfil do Leitor (Brasil)

| Atributo | Descrição |
|---|---|
| Formação | Engenheiros, técnicos, operadores especializados, gestores de qualidade |
| Nível de escolaridade | Superior completo ou técnico especializado |
| Expectativa principal | Precisão terminológica absoluta, rastreabilidade normativa |
| Sensibilidade a erros | Extremamente baixa — um termo errado pode causar falha de equipamento |
| Variante preferida | Português brasileiro formal com terminologia ABNT |
| Contexto de leitura | Manual de instruções, norma técnica, laudo, especificação |

## Perfil do Leitor (Portugal)

| Atributo | Descrição |
|---|---|
| Formação | Engenheiros, técnicos certificados, laboratórios acreditados |
| Nível de escolaridade | Superior completo ou equivalente |
| Expectativa principal | Conformidade com normas NP (Normas Portuguesas) e EN |
| Sensibilidade a erros | Alta — especialmente em unidades e valores numéricos |
| Variante preferida | Português europeu formal com terminologia NP |
| Contexto de leitura | Especificação técnica, relatório de ensaio, ficha de segurança |

## Hierarquia de Necessidades do Leitor

1. Exatidão de valores, unidades e parâmetros numéricos
2. Correspondência normativa (ABNT NBR / NP / ISO / IEC)
3. Clareza procedural (passos inequívocos e ordenados)
4. Consistência terminológica intra-documento
5. Estilo técnico direto (imperativo para instruções, voz passiva para descrições)

## Comportamento de Leitura

- Leitores técnicos frequentemente **scanning** em busca de parâmetros específicos
- Tabelas, diagramas e listas numeradas são preferidos a prosa contínua
- Notas de rodapé e referências cruzadas são consultadas ativamente
- Qualquer erro numérico ou de unidade quebra a confiança imediatamente

---

# Decision Framework: Tradução Técnica PT

## Tabela 1: Preservação de Valores e Unidades

| Contexto | Decisão | Exemplo BR | Exemplo PT | Notas |
|---|---|---|---|---|
| Valor numérico puro | Preservar exatamente | 12,5 mm | 12,5 mm | Sem arredondamento |
| Unidade SI | Preservar com espaço | 10 kW | 10 kW | Espaço entre número e unidade |
| Unidade não-SI | Preservar, adicionar SI entre parênteses se necessário | 5 psi (34,5 kPa) | 5 psi (34,5 kPa) | Opcional, verificar requisito |
| Temperatura °C | Preservar | 150 °C | 150 °C | Espaço antes de °C |
| Temperatura °F | Preservar, converter °C | 212 °F (100 °C) | 212 °F (100 °C) | Conversão entre parênteses |
| Data (ISO 8601) | Preservar | 2026-05-25 | 2026-05-25 | Formato internacional |
| Hora | Preservar | 14:30 | 14:30 | Formato 24h |
| Milhar decimal | Converter para formato local | 1.234,56 (BR) | 1 234,56 (PT) | BR: ponto milhar / PT: espaço milhar |
| Medidas imperiais | Preservar, converter SI | 3/8" (9,525 mm) | 3/8" (9,525 mm) | Polegadas fracionárias |

## Tabela 2: Terminologia de Normas e Certificações

| Termo Fonte | Decisão BR | Decisão PT | Notas |
|---|---|---|---|
| ISO 9001 | ISO 9001 | ISO 9001 | Preservar número exato |
| CE marking | Marcacao CE | Marcacao CE | Manter CE |
| UL certification | Certificacao UL | Certificacao UL | Manter UL |
| INMETRO | INMETRO | N/A | Especifico Brasil |
| IPOO (Portugal) | N/A | IPOO | Especifico Portugal |
| standard (documento) | Norma (ABNT NBR ...) | Norma (NP ...) | Contexto normativo |
| compliance | Conformidade | Conformidade | Mesmo termo |
| certification body | Organismo certificador | Entidade certificadora | Diferenca regional |
| type approval | Aprovacao de modelo | Aprovacao de tipo | Diferenca terminologica |
| declaration of conformity | Declaracao de conformidade | Declaracao de conformidade | Mesmo termo |

## Tabela 3: Verbos e Modos em Instrucoes

| Tipo de Texto | Voz/Modo | Exemplo BR | Exemplo PT |
|---|---|---|---|
| Instrucao direta | Imperativo | Pressione o botao | Prima o botao |
| Procedimento sequencial | Imperativo numerado | 1. Abra a valvula | 1. Abra a valvula |
| Especificacao tecnica | Presente do indicativo | O motor opera a 60 Hz | O motor opera a 60 Hz |
| Advertencia de perigo | Imperativo + atencao | Atencao: Desligue a energia | Atencao: Desligue a energia |
| Nota informativa | Presente indicativo | Nota: O sistema reinicia | Nota: O sistema reinicia |
| Condicao | Se + presente | Se a temperatura exceder... | Se a temperatura exceder... |
| Lista de materiais | Frase nominal | Parafuso M8 x 30 mm | Parafuso M8 x 30 mm |
| Resultado esperado | Futuro do presente | O LED acendera | O LED acendera |

## Tabela 4: Seguranca e Sinalizacao

| Termo Fonte | BR | PT | Observacao |
|---|---|---|---|
| Danger | Perigo | Perigo | Nivel maximo |
| Warning | Atencao | Aviso | Uso diferente BR vs PT |
| Caution | Cuidado | Cuidado | Nivel medio |
| Notice | Nota | Nota | Nivel informativo |
| safety | seguranca | seguranca | Mesmo termo |
| safety device | dispositivo de seguranca | dispositivo de seguranca | Mesmo termo |
| protective equipment | equipamento de protecao | equipamento de protecao | Abreviacao EPI (BR) |
| guard / shield | protecao / blindagem | resguardo / protecao | PT prefere resguardo |
| lockout-tagout | bloqueio e etiquetagem | bloqueio e etiquetagem | Termo tecnico |
| emergency stop | parada de emergencia | parada de emergencia | Botoes vermelhos |
| hazardous area | area classificada | zona classificada | PT: zona; BR: area |
| PPE (Personal Protective Equipment) | EPI (Equipamento de Protecao Individual) | EPI (Equipamento de Protecao Individual) | Sigla universal |

## Tabela 5: Elementos Mecanicos e Fabricacao

| Termo Fonte | BR | PT | Observacao |
|---|---|---|---|
| welding | soldagem | soldadura | PT prefere soldadura |
| machining | usinagem | maquinacao | Diferenca significativa |
| casting | fundicao | fundicao | Mesmo termo |
| forging | forjamento | forjamento | Mesmo termo |
| thread | rosca | rosca | Mesmo termo |
| bearing | rolamento | rolamento | Mesmo termo |
| gasket | junta / vedacao | junta / vedante | PT: vedante |
| shaft | eixo | veio | PT: veio (distinto) |
| gear | engrenagem | engrenagem | Mesmo termo |
| bolt | parafuso | parafuso | Especificar tipo |
| nut | porca | porca | Mesmo termo |
| washer | arruela | anilha | PT: anilha (distinto) |
| seal | selo / retentor | retentor | PT prefere retentor |
| valve | valvula | valvula | Mesmo termo |
| pipe | tubo | tubo / conduta | PT pode usar conduta |

## Tabela 6: Eletrica e Eletronica

| Termo Fonte | BR | PT | Observacao |
|---|---|---|---|
| voltage | tensao | tensao | Mesmo termo |
| current | corrente | corrente | Mesmo termo |
| resistance | resistencia | resistencia | Mesmo termo |
| power | potencia | potencia | Mesmo termo |
| frequency | frequencia | frequencia | Mesmo termo |
| ground / earth | terra | terra | BR: terra; PT: terra |
| fuse | fusivel | fusivel | Mesmo termo |
| circuit breaker | disjuntor | disjuntor | Mesmo termo |
| relay | rele | rele | Mesmo termo |
| transformer | transformador | transformador | Mesmo termo |
| capacitor | capacitor | condensador | PT: condensador (tradicional) |
| resistor | resistor | resistencia | PT: resistencia (componente) |
| diode | diodo | diodo | Mesmo termo |
| transistor | transistor | transistor | Mesmo termo |
| integrated circuit | circuito integrado | circuito integrado | Mesmo termo |
| printed circuit board | placa de circuito impresso | placa de circuito impresso | PCI (ambos) |
| wiring diagram | diagrama eletrico | esquema eletrico | PT prefere esquema |

## Tabela 7: Software e Tecnologia da Informacao

| Termo Fonte | BR | PT | Observacao |
|---|---|---|---|
| bug | bug / defeito | bug / erro | Preferir bug como termo tecnico |
| debug | depuracao | depuracao | PT pode usar depuracao |
| deploy | implantar | implementar | PT: implementar |
| release | versao | versao | Mesmo termo |
| build | compilacao | compilacao / build | PT pode usar build |
| feature | funcionalidade | funcionalidade | Mesmo termo |
| end user | usuario final | utilizador final | PT: utilizador |
| login | login / autenticacao | autenticacao / inicio de sessao | PT: inicio de sessao |
| logout | logout / saida | fim de sessao | PT: fim de sessao |
| backup | copia de seguranca | copia de seguranca / backup | Ambos usam backup |
| cloud | nuvem | nuvem | Computacao em nuvem |
| database | banco de dados | base de dados | PT: base de dados |
| server | servidor | servidor | Mesmo termo |
| firewall | firewall | firewall | Termo universal |
| malware | malware | malware | Termo universal |
| patch | patch / correcao | patch / atualizacao | Ambos usam patch |
| API | API | API | Sigla universal |
| framework | framework | framework | Termo universal |

## Tabela 8: Dispositivos Medicos e Saude

| Termo Fonte | BR | PT | Observacao |
|---|---|---|---|
| medical device | dispositivo medico | dispositivo medico | Mesmo termo |
| IVD (in vitro diagnostic) | diagnostico in vitro | diagnostico in vitro | Sigla DIV |
| clinical trial | ensaio clinico | ensaio clinico | Mesmo termo |
| adverse event | evento adverso | evento adverso | Mesmo termo |
| dosage | dosagem | dosagem | Mesmo termo |
| contraindication | contraindicacao | contraindicacao | Mesmo termo |
| ANVISA | ANVISA | N/A | Orgao regulador BR |
| INFARMED | N/A | INFARMED | Orgao regulador PT |
| CE marking (medical) | Marcacao CE (ANVISA) | Marcacao CE (INFARMED) | Diferenca regulatoria |
| sterility | esterilidade | esterilidade | Mesmo termo |
| biocompatibility | biocompatibilidade | biocompatibilidade | Mesmo termo |
| validation | validacao | validacao | Mesmo termo |
| verification | verificacao | verificacao | Mesmo termo |

## Tabela 9: Normas Tecnicas e Orgaos Reguladores

| Orgao/ Norma | BR | PT | Abrangencia |
|---|---|---|---|
| ABNT | Associacao Brasileira de Normas Tecnicas | N/A | Brasil |
| INMETRO | Instituto Nacional de Metrologia | N/A | Brasil |
| ANVISA | Agencia Nacional de Vigilancia Sanitaria | N/A | Brasil |
| ANATEL | Agencia Nacional de Telecomunicacoes | N/A | Brasil |
| ANP | Agencia Nacional do Petroleo | N/A | Brasil |
| IPQ | N/A | Instituto Portugues da Qualidade | Portugal |
| ISQ | N/A | Instituto de Soldadura e Qualidade | Portugal |
| INFARMED | N/A | Autoridade Nacional do Medicamento | Portugal |
| NR | Norma Regulamentadora | N/A | Seguranca do trabalho BR |
| NP | N/A | Norma Portuguesa | Portugal |
| EN | EN | EN | Europeia (ambos) |
| ISO | ISO | ISO | Internacional (ambos) |

## Tabela 10: Formatacao de Documento Tecnico

| Elemento | Formato BR | Formato PT | Notas |
|---|---|---|---|
| Numeracao de pagina | Pagina 10 de 50 | Pagina 10 de 50 | Mesmo formato |
| Numeracao de figura | Figura 1 - Diagrama | Figura 1 - Diagrama | Ou Fig. 1 |
| Numeracao de tabela | Tabela 1 - Especificacoes | Quadro 1 - Especificacoes | PT: Quadro (preferencial) |
| Referencia cruzada | conforme Figura 3 | conforme Figura 3 | Mesmo formato |
| Lista de materiais | Item | Referencia | PT: Referencia |
| Revisao do documento | Rev. A / Revisao 1 | Rev. A / Revisao 1 | Identico |
| Data de revisao | 25/05/2026 | 25/05/2026 | Formato dd/mm/aaaa |
| Nota de rodape | Numeracao sobrescrita | Numeracao sobrescrita | Identico |
| Aviso legal | Reservados todos os direitos | Reservados todos os direitos | Mesmo texto |
| Marcacao de revisao | Linha vertical na margem | Linha vertical na margem | Tracejado ou linha |

## Tabela 11: Glossario de Precisao e Qualidade

| Termo Fonte | BR | PT | Definicao |
|---|---|---|---|
| accuracy | exatidao | exatidao | Proximidade do valor verdadeiro |
| precision | precisao | precisao | Repetibilidade de medicoes |
| tolerance | tolerancia | tolerancia | Faixa admissivel de variacao |
| calibration | calibracao | calibracao | Comparacao com padrao |
| uncertainty | incerteza | incerteza | Duvida na medicao |
| repeatability | repetitividade | repetibilidade | Mesmo operador, mesmo instrumento |
| reproducibility | reprodutividade | reprodutibilidade | Operadores diferentes |
| traceability | rastreabilidade | rastreabilidade | Cadeia ininterrupta de calibracoes |
| validation | validacao | validacao | Confirmacao por evidencia objetiva |
| verification | verificacao | verificacao | Confirmacao de requisitos atendidos |
| quality control | controle de qualidade | controlo de qualidade | PT: controlo (distinto) |
| quality assurance | garantia da qualidade | garantia da qualidade | Mesmo termo |

## Tabela 12: Traducao de Conectivos Tecnicos

| Conectivo Fonte | Traducao | Uso recomendado |
|---|---|---|
| therefore | portanto / por conseguinte | Formal, documentos normativos |
| however | contudo / no entanto | Meio de frase ou inicio |
| in order to | para / a fim de | "A fim de evitar danos..." |
| such that | de modo que | Condicoes tecnicas |
| provided that | desde que | Condicoes restritivas |
| as per | conforme / de acordo com | Referencia normativa |
| in accordance with | em conformidade com | Mais formal que "de acordo com" |
| with respect to | em relacao a | Preferir a "com respeito a" |
| whereby | pelo qual / mediante o qual | Linguagem juridico-tecnica |
| hereinafter | doravante / adiante designado | Contratos e normas |

---

# Standards: Padroes para Documentos Tecnicos em Portugues

## ABNT NBR (Brasil)

### Normas Gerais de Documentacao

- **ABNT NBR 6022**: Informacao e documentacao — Artigo em publicacao periodica tecnica e/ou cientifica
- **ABNT NBR 6023**: Referencias — Elaboracao
- **ABNT NBR 6024**: Numeracao progressiva das secoes de um documento
- **ABNT NBR 6027**: Sumario — Apresentacao
- **ABNT NBR 6028**: Resumo — Apresentacao
- **ABNT NBR 14724**: Trabalhos academicos — Apresentacao
- **ABNT NBR 15287**: Projeto de pesquisa — Apresentacao
- **ABNT NBR 10520**: Citacoes em documentos — Apresentacao
- **ABNT NBR 12256**: Apresentacao de originais
- **ABNT NBR 9578**: Normas para desenho tecnico

### Normas de Seguranca (NR)

- **NR-6**: Equipamento de Protecao Individual (EPI)
- **NR-10**: Seguranca em instalacoes e servicos em eletricidade
- **NR-11**: Transporte, movimentacao, armazenagem e manuseio de materiais
- **NR-12**: Seguranca no trabalho em maquinas e equipamentos
- **NR-17**: Ergonomia
- **NR-20**: Seguranca e saude no trabalho com inflamaveis e combustiveis
- **NR-23**: Protecao contra incendios
- **NR-26**: Sinalizacao de seguranca
- **NR-33**: Seguranca e saude nos trabalhos em espacos confinados
- **NR-35**: Trabalho em altura

### Normas de Qualidade

- **ABNT NBR ISO 9001**: Sistema de gestao da qualidade
- **ABNT NBR ISO 14001**: Sistema de gestao ambiental
- **ABNT NBR ISO 45001**: Sistema de gestao de saude e seguranca no trabalho
- **ABNT NBR ISO 17025**: Requisitos gerais para competencia de laboratorios de ensaio e calibracao
- **ABNT NBR ISO 13485**: Dispositivos medicos — Sistema de gestao da qualidade
- **ABNT NBR IEC 62304**: Software de dispositivo medico — Processo de ciclo de vida
- **ABNT NBR ISO 14971**: Dispositivos medicos — Aplicacao de gerenciamento de risco

### Normas de Metrologia

- **ABNT NBR ISO 10012**: Sistema de gestao de medicoes
- **ABNT NBR ISO 5725**: Exatidao (veracidade e precisao) de metodos e resultados de medicao
- **ABNT NBR IEC 60068**: Ensaios ambientais
- **ABNT NBR NM 213**: Transformadores de potencial
- **INMETRO Portaria 236**: Requisitos de seguranca para dispositivos medicos

### Simbologia e Desenho Tecnico

- **ABNT NBR 8196**: Desenho tecnico — Emprego de escalas
- **ABNT NBR 8402**: Execucao de caractere para escrita em desenhos tecnicos
- **ABNT NBR 8403**: Aplicacao de linhas em desenhos — Tipos e larguras
- **ABNT NBR 10067**: Principios gerais de representacao em desenho tecnico
- **ABNT NBR 10126**: Cotagem em desenho tecnico
- **ABNT NBR ISO 5457**: Formatos e leiaute de folhas de desenho tecnico

## NP / IPQ (Portugal)

### Normas Portuguesas de Documentacao

- **NP 405**: Documentacao — Referencias bibliograficas
- **NP 629**: Documentos — Apresentacao de teses e relatorios
- **NP 370**: Numeracao de divisoes de um documento escrito
- **NP 319**: Sumario — Apresentacao
- **NP 373**: Resumo — Apresentacao

### Normas Europeias Adotadas (NP EN)

- **NP EN ISO 9001**: Sistema de gestao da qualidade
- **NP EN ISO 14001**: Sistema de gestao ambiental
- **NP EN ISO 45001**: Sistema de gestao da saude e seguranca no trabalho
- **NP EN ISO 17025**: Requisitos gerais para laboratorios de ensaio e calibracao
- **NP EN ISO 13485**: Dispositivos medicos — Sistema de gestao da qualidade
- **NP EN ISO 14971**: Dispositivos medicos — Gestao de riscos

### Seguranca no Trabalho (Portugal)

- **Lei 102/2009**: Regime juridico da promocao da seguranca e saude no trabalho
- **Portaria 1456-A/2009**: Sinalizacao de seguranca no trabalho
- **Decreto-Lei 50/2005**: Equipamentos de protecao individual
- **NP EN 349**: Seguranca de maquinas — Distancias minimas para evitar esmagamento
- **NP EN 418**: Equipamento de paragem de emergencia

## Sistemas de Unidades e Notacao

### Regras SI para Textos Tecnicos

| Grandeza | Unidade SI | Simbolo | Notas de uso |
|---|---|---|---|
| Comprimento | metro | m | Sem ponto apos simbolo |
| Massa | quilograma | kg | Prefixo k minusculo |
| Tempo | segundo | s | Nao usar seg. |
| Corrente eletrica | ampere | A | Maiusculo |
| Temperatura | kelvin | K | Sem grau |
| Quantidade | mole | mol | Sem ponto |
| Intensidade luminosa | candela | cd | Minusculo |
| Forca | newton | N | Maiusculo |
| Pressao | pascal | Pa | Maiusculo |
| Energia | joule | J | Maiusculo |
| Potencia | watt | W | Maiusculo |
| Frequencia | hertz | Hz | Maiusculo |
| Tensao eletrica | volt | V | Maiusculo |
| Resistencia | ohm | Omega | Simbolo grego |

### Regras de Formatacao Numerica

- BR: separador decimal = virgula; separador milhar = ponto (1.234,56)
- PT: separador decimal = virgula; separador milhar = espaco (1 234,56)
- Porcentagem: 15,5 % (espaco antes de % no Brasil, sem espaco em Portugal — verificar)
- Tolerancias: 10 mm +/- 0,5 mm ou 10 (+/- 0,5) mm
- Intervalos: de 10 mm a 50 mm (nao usar travesao)
- Precedencia de operadores: espaços ao redor de sinais (a = b + c)

### Prefixos SI

| Multiplo | Prefixo | Simbolo | Exemplo |
|---|---|---|---|
| 10^9 | giga | G | GHz |
| 10^6 | mega | M | MW |
| 10^3 | quilo | k | kg (NOTA: k minusculo) |
| 10^2 | hecto | h | hPa |
| 10^1 | deca | da | dag |
| 10^-1 | deci | d | dL (BR) / dL (PT) |
| 10^-2 | centi | c | cm |
| 10^-3 | mili | m | mm |
| 10^-6 | micro | micro | microF |
| 10^-9 | nano | n | nm |
| 10^-12 | pico | p | pF |

## Glossario de Termos Problematicos

| Termo Ingles | Problema | Solucao BR | Solucao PT |
|---|---|---|---|
| lead | Polissemico (chumbo, condutor, avancar) | chumbo (metal) / condutor (eletrico) | chumbo (metal) / condutor (eletrico) |
| spring | Polissemico (mola, primavera, fonte) | mola (mecanica) | mola (mecanica) |
| seal | Polissemico (selo, vedacao, foca) | vedacao / retentor | vedante / retentor |
| bushing | Termo variavel | bucha / casquilho | casquilho |
| sleeve | Termo variavel | luva / manga | manga / camisa |
| jack | Polissemico | conector / macaco (ferramenta) | conector / macaco (ferramenta) |
| terminal | Polissemico | terminal (eletrico) / borne | terminal (eletrico) / borne |
| clip | Termo variavel | clipe / grampo | clipe / presilha |
| bus | Polissemico | barramento (eletrico) / onibus | barramento (eletrico) / autocarro |
| bit | Polissemico | bit (informatica) / broca (ferramenta) | bit (informatica) / broca (ferramenta) |

## Padroes de Redacao Tecnica

### Instrucoes e Procedimentos

1. **Use o imperativo** para acoes do usuario: "Pressione o botao START para iniciar."
2. **Use voz passiva** para descricao de processos: "A peca e usinada em alta velocidade."
3. **Ordene logicamente** as etapas de procedimentos numerados.
4. **Uma acao por passo**: cada passo deve conter uma unica acao.
5. **Advertências antes da acao**: "Atencao: Desligue a alimentacao antes de abrir o painel."

### Especificacoes

1. **Parametros com unidade**: "Tensao nominal: 220 Vca / 60 Hz"
2. **Tabelas para multiplos parametros**: preferir tabelas a listas para conjuntos de dados.
3. **Tolerâncias explicitas**: "Diametro: 50,00 mm +/- 0,05 mm"
4. **Condicoes ambientais**: "Temperatura de operacao: 0 a 40 graus C"
5. **Referencias normativas**: "Conforme ABNT NBR ISO 9001:2015"

### Emprego de Siglas

1. **Definir na primeira ocorrencia**: "O Equipamento de Protecao Individual (EPI) deve ser certificado."
2. **Usar a sigla consistemente apos definicao**: evitar alternar entre sigla e termo extenso.
3. **Criar lista de siglas** no inicio ou fim de documentos extensos.
4. **Evitar siglas regionais** em documentos para audiencia mista BR+PT.

### Correcao Linguistica

1. **Acentuacao**: respeitar o novo Acordo Ortografico de 1990 (vigente em ambos os paises).
2. **Crase**: usar crase quando ha fusao de preposicao a + artigo a (ex.: "a valvula" vs. "a valvula").
3. **Concordância**: verificar concordância nominal e verbal em frases tecnicas longas.
4. **Estrangeirismos**: preferir termos vernaculos quando existem (ex.: "software" e aceito, "folder" deve ser "pastinha" ou "diretorio").
5. **Neologismos**: verificar se o termo tecnico ja possui traducao consagrada antes de criar neologismo.

## Referencias Normativas para Tradutores Tecnicos

### Brasil

- Vocabulario Ortografico da Lingua Portuguesa (VOLP) - Academia Brasileira de Letras
- Manual de Redacao da Presidencia da Republica
- Normas ABNT NBR (serie completa) - www.abnt.org.br
- Portarias INMETRO - www.inmetro.gov.br
- Normas Regulamentadoras (NR) - Ministerio do Trabalho
- Guia de terminologia tecnica - SENAI / SENAC

### Portugal

- Acordo Ortografico de 1990 (implementado) - conforme deliberacao do IPQ
- Normas Portuguesas NP - IPQ (Instituto Portugues da Qualidade) - www.ipq.pt
- Guia do CTIC - Centro de Terminologia e Industrias da Cultura
- Normas NP EN adotadas do CEN/CENELEC
- Sistema Portugues da Qualidade (SPQ)
- Vocabulario Tecnico do ISQ

### Internacionais

- ISO/IEC Directives, Part 2: Principles and rules for the structure and drafting of ISO and IEC documents
- SI Brochure (BIPM): The International System of Units
- IEV (International Electrotechnical Vocabulary) - IEC 60050 series
- ISO 704: Terminology work — Principles and methods
- ISO 24610: Language resource management
- IUPAC Quantities, Units and Symbols in Physical Chemistry (Green Book)
