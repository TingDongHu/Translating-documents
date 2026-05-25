---
id: pt/domain/legal
type: domain
target_lang: pt
name: Documentos juridicos (portugues)
description: Terminologia e regras para documentos juridicos traduzidos para portugues brasileiro e portugues europeu. Cobertura do Codigo Civil, estrutura contratual, diferencas PT vs BR e vocabulario forense.
---

# Reader Model: Leitor de Documentos Juridicos

## Perfil do Leitor (Brasil)

| Atributo | Descricao |
|---|---|
| Formacao | Advogados, juizes, procuradores, tabeliaes, servidores do judiciario |
| Nivel de especializacao | Alto — dominio do vocabulario tecnico-juridico brasileiro |
| Expectativa principal | Fidelidade absoluta ao sentido juridico original, conformidade com o Codigo Civil |
| Sensibilidade a erros | Extremamente alta — um termo juridico incorreto pode invalidar clausulas |
| Variante preferida | Portugues juridico brasileiro formal, com terminologia do Codigo Civil (Lei 10.406/2002) |
| Contexto de leitura | Contratos, peticoes, pareceres, sentencas, documentos societarios |

## Perfil do Leitor (Portugal)

| Atributo | Descricao |
|---|---|
| Formacao | Advogados, magistrados, notarios, conservadores, juristas de empresa |
| Nivel de especializacao | Alto — dominio do vocabulario juridico portugues |
| Expectativa principal | Conformidade com o Codigo Civil portugues (DL 47344/66) e legislacao europeia |
| Sensibilidade a erros | Extremamente alta — especialmente em conceitos processuais |
| Variante preferida | Portugues juridico europeu formal |
| Contexto de leitura | Contratos, estatutos, procuracoes, pareceres, regulamentos |

## Hierarquia de Necessidades do Leitor

1. Precisao terminologica juridica (termos de arte do direito)
2. Estrutura formal e clausal adequada ao ordenamento juridico de destino
3. Forca vinculante preservada (deve/pode/fara/podera)
4. Referencias normativas e numeracao preservadas exatamente
5. Equivalencia funcional entre sistemas juridicos (common law vs civil law)

## Comportamento de Leitura

- Leitura analitica e desconfiada — cada palavra pode ser objeto de disputa judicial
- Atencao concentrada em verbos modais (deve, podera, fica obrigado)
- Busca por definicoes e condicoes (clausulas definitorias e condicionantes)
- Verificacao cruzada com legislacao aplicavel
- Precedentes e jurisprudencia sao consultados paralelamente
- Expectativa de clareza absoluta: ambiguidade e inaceitavel em documentos juridicos

---

# Decision Framework: Traducao Juridica PT

## Tabela 1: Verbos Modais e Obrigacoes

| Termo Fonte | BR | PT | Forca Juridica | Notas |
|---|---|---|---|---|
| shall | deve | deve | Obrigacao absoluta | Nao usar 'podera' |
| shall not | nao deve | nao deve | Proibicao absoluta | Equivalente a vedado |
| may | pode | pode | Permissao | Faculdade, nao obrigacao |
| may not | nao pode | nao pode | Proibicao | Menos forte que shall not |
| must | deve / e obrigatorio | deve / e obrigatorio | Obrigacao enfatica | Usar em clausulas de garantia |
| must not | nao pode / e vedado | nao pode / e vedado | Proibicao absoluta | Uso em compliance |
| will | fara / devera | fara / devera | Obrigacao futura | Menos forte que shall |
| should | deveria / recomenda-se | deveria / recomenda-se | Recomendacao | Nao cria obrigacao |
| would | faria / poderia | faria / poderia | Condicional | Usar em hipoteses |
| can | pode | pode | Capacidade/Permissao | Menos formal que may |
| entitled to | tem direito a | tem direito a | Direito subjetivo | Preciso em clausulas |
| undertakes to | obriga-se a | obriga-se a | Obrigacao assumida | Termo contratual classico |

## Tabela 2: Estrutura de Contratos

| Elemento Fonte | BR | PT | Observacao |
|---|---|---|---|
| Agreement | Contrato / Instrumento Particular | Contrato | BR: Instrumento Particular e formal |
| Party | Parte | Parte / Contraente | PT usa Contraente em alguns contextos |
| First Party | Primeira Parte / Contratante | Primeiro Contraente | Nomear partes idealmente |
| Whereas | Considerando que | Considerando que | Clausulas de preambulo |
| Now, therefore | Resolvem as partes | Resolvem as partes | Formula de transicao |
| Clause | Clausula | Clausula | Identico |
| Section | Secao | Secao | Identico |
| Paragraph | Paragrafo | Paragrafo | Identico |
| Item | Item / Alinea | Alinea | BR: item numerado |
| Annex | Anexo | Anexo / Apendice | PT distingue anexo de apendice |
| Schedule | Anexo / Quadro | Mapa / Anexo | PT: Mapa em contratos financeiros |
| Appendix | Apendice | Apendice | Mesmo termo |
| Addendum | Aditivo / Termo Aditivo | Adenda | BR: Aditivo; PT: Adenda |
| Amendment | Emenda / Alteracao | Alteracao / Modificacao | PT prefere Alteracao |
| Exhibit | Anexo / Documento | Documento anexo | BR: Anexo |

## Tabela 3: Termos de Responsabilidade e Garantia

| Termo Fonte | BR | PT | Notas |
|---|---|---|---|
| liability | responsabilidade | responsabilidade | Mesmo termo |
| limited liability | responsabilidade limitada | responsabilidade limitada | Ltda. / Lda. |
| unlimited liability | responsabilidade ilimitada | responsabilidade ilimitada | Raro |
| joint liability | responsabilidade solidaria | responsabilidade solidaria | Importante: distinto de conjunta |
| several liability | responsabilidade individual | responsabilidade individual | Oposta a solidaria |
| joint and several | solidaria | solidaria | BR e PT: solidaria |
| indemnification | indenizacao | indemnizacao | BR: indenizacao; PT: indemnizacao |
| hold harmless | isentar de responsabilidade | isentar de responsabilidade | Termo composto |
| warranty | garantia | garantia | Mesmo termo |
| representation | declaracao | declaracao | Representacao e termo diferente |
| covenant | obrigacao / convenio | obrigacao / convenio | Contextual |
| condition precedent | condicao suspensiva | condicao suspensiva | Mesmo termo tecnico |
| condition subsequent | condicao resolutiva | condicao resolutiva | Mesmo termo tecnico |
| breach | violacao / inadimplemento | violacao / incumprimento | BR: inadimplemento; PT: incumprimento |
| default | inadimplemento | incumprimento | Diferenca regional crucial |
| material breach | violacao essencial | violacao essencial | Tambem: violacao substancial |

## Tabela 4: Resolucao de Conflitos e Foro

| Termo Fonte | BR | PT | Observacao |
|---|---|---|---|
| governing law | lei aplicavel | lei aplicavel / lei reguladora | PT: lei reguladora (tambem usado) |
| jurisdiction | jurisdisco | jurisdisco | Mesmo termo |
| venue | foro | foro / tribunal competente | BR: foro |
| arbitration | arbitragem | arbitragem | Mesmo termo |
| mediation | mediacao | mediacao | Mesmo termo |
| conciliation | conciliacao | conciliacao | Mesmo termo |
| arbitration clause | clausula compromissoria | clausula compromissoria | BR e PT: mesma terminologia |
| arbitration agreement | convencao de arbitragem | convencao de arbitragem | Termo do direito processual |
| arbitrator | arbitro | arbitro | Mesmo termo |
| award | sentenca arbitral | decisao arbitral | BR: sentenca; PT: decisao |
| court | tribunal | tribunal | Mesmo termo |
| court of appeals | tribunal de justica / TRF | tribunal da relacao | Diferenca estrutural |
| supreme court | STF / STJ | Supremo Tribunal de Justica | BR: STF (constitucional), STJ (infraconstitucional) |
| injunction | liminar / tutela provisoria | providencia cautelar | BR: liminar; PT: providencia cautelar |
| damages | danos / perdas e danos | danos | BR: perdas e danos (completo) |

## Tabela 5: Diferencas BR vs PT — Vocabulario Juridico

| Conceito | BR | PT | Impacto |
|---|---|---|---|
| Contract breach | inadimplemento contratual | incumprimento contratual | Alto — termo central |
| Indemnification | indenizacao | indemnizacao | Ortografia |
| Lawsuit | acao judicial | accao judicial | Ortografia (Acordo 1990) |
| Plaintiff | autor / requerente | autor / demandante | Mesmo termo |
| Defendant | reu | reu / demandado | Mesmo termo |
| Attorney | advogado | advogado / mandatario | Mandatario e mais formal em PT |
| Power of attorney | procuraco | procuraco | Mesmo termo |
| Notary public | tabeliao | notario | BR: tabeliao; PT: notario |
| Witness | testemunha | testemunha | Mesmo termo |
| Affidavit | declaracao jurada | declaracao sob compromisso | BR: jurada (formal) |
| Oath | juramento | juramento / compromisso de honra | PT: compromisso de honra |
| Sworn statement | declaracao jurada | declaracao com compromisso | PT evita juramento religioso |
| Domicile | domicilio | domicilio | Mesmo termo |
| Residence | residencia | residencia | Mesmo termo |
| Legal entity | pessoa juridica | pessoa colectiva | PT: colectiva (distinto) |
| Merger | fusao | fusao | Mesmo termo |
| Spin-off | cisao | cisao | Termo do direito societario |

## Tabela 6: Conceitos de Common Law sem Equivalente Direto

| Termo | Problema | Solucao Recomendada | Exemplo |
|---|---|---|---|
| Trust | Inexistente no direito civil | Manter "trust" em ingles + nota explicativa | "trust (figura fiduciaria anglo-saxonica)" |
| Equity | Multiplos significados | Traduzir conforme contexto | equity = "participacao societaria" ou "patrimonio liquido" |
| Estoppel | Inexistente | Manter + glosa | "estoppel (preclusao pelo comportamento)" |
| Consideration | Troca de valor | "contraprestacao" (contratual) | Nao confundir com "consideracao" |
| Injunction | Ordem judicial | "ordem judicial" / "liminar" | Contextual |
| Specific performance | Execucao especifica | "execucao especifica" ou "cumprimento forçado" | BR: execucao especifica |
| Class action | Acao coletiva | "acao civil publica" (BR) / "acao coletiva" (PT) | Estrutura diferente |
| Discovery | Revelacao de provas | "producao de provas" / "disclosure" | Sem equivalente direto |
| Cross-examination | Interrogatorio | "interrogatorio cruzado" / "contra-interrogatorio" | PT: contra-interrogatorio |
| Due process | Devido processo legal | "devido processo legal" | Consagrado |
| Common law | Sistema juridico | "common law" (manter) | Sem traducao consagrada |

## Tabela 7: Linguagem Processual

| Termo Fonte | BR | PT | Notas |
|---|---|---|---|
| complaint / petition | peticao inicial | peticao inicial | Mesmo conceito |
| answer | contestacao | contestacao | Mesmo termo |
| counterclaim | reconvencao | reconvencao | Mesmo termo |
| pleading | peca processual | peca processual | Mesmo termo |
| motion | peticao / requerimento | requerimento | BR: peticao intermediaria |
| deposition | depoimento | deposicao / depoimento | PT: deposicao |
| evidence | prova | prova | Mesmo termo |
| exhibit | documento / prova documental | documento / meio de prova | Contextual |
| hearing | audiencia | audiencia | Mesmo termo |
| trial | julgamento | julgamento | Mesmo termo |
| verdict | veredito | veredito | Mesmo termo |
| sentence | sentenca | sentenca | Mesmo termo |
| appeal | recurso | recurso | Mesmo termo |
| appeal court | tribunal de segundo grau | tribunal da relacao | Estrutura diferente |
| stay of proceedings | suspensao do processo | suspensao da instancia | PT: instancia |
| statute of limitations | prescricao | prescricao / caducidade | PT distingue prescricao de caducidade |

## Tabela 8: Direito Societario e Empresarial

| Termo Fonte | BR | PT | Observacao |
|---|---|---|---|
| corporation | sociedade anonima (S.A.) | sociedade anonima (S.A.) | Estrutura similar |
| limited liability company | sociedade limitada (Ltda.) | sociedade por quotas (Lda.) | BR: Ltda.; PT: Lda. |
| sole proprietorship | empresario individual | empresario em nome individual | PT: ENI |
| partnership | sociedade de pessoas | sociedade em nome colectivo | Estruturas diferentes |
| joint venture | joint venture / consorcio | joint venture / consorcio | Ambos usam joint venture |
| subsidiary | subsidiaria / filial | subsidiaria / filial | PT distingue subsidiaria (controlada) de filial (sucursal) |
| branch | filial / sucursal | sucursal | PT: sucursal |
| holding company | holding | sociedade gestora de participacoes sociais (SGPS) | PT usa SGPS |
| board of directors | conselho de administracao | conselho de administracao | Mesmo termo |
| shareholder | acionista | accionista | Ortografia (Acordo 1990) |
| share | acao | accao | Ortografia (Acordo 1990) |
| quota | quota | quota | Ltda. / Lda. |
| dividend | dividendo | dividendo | Mesmo termo |
| meeting of shareholders | assembleia geral | assembleia geral | Mesmo termo |
| by-laws | estatuto social | estatutos | BR: singular; PT: plural |
| articles of incorporation | contrato social | pacto social / contrato de sociedade | BR: contrato social; PT: pacto social |
| corporate purpose | objeto social | objeto social | Mesmo termo |
| capital stock | capital social | capital social | Mesmo termo |

## Tabela 9: Documentos Notariais e Registro

| Termo Fonte | BR | PT | Observacao |
|---|---|---|---|
| notary public | tabeliao de notas | notario | Diferenca de nomenclatura |
| notary office | cartorio | cartorio notarial | PT: cartorio notarial |
| deed | escritura publica | escritura publica | Mesmo conceito |
| registration | registro | registo | Ortografia (Acordo 1990) |
| property registration | registro de imoveis | registo predial | PT: registo predial |
| commercial registry | Junta Comercial | Registo Comercial / Conservatoria | Estrutura diferente |
| certificate | certidao | certidao | Mesmo termo |
| certified copy | copia autenticada | copia certificada | PT: certificada (distinto) |
| apostille | apostila de Haia | apostila de Haia | Mesmo termo |
| authentication | autenticacao / reconhecimento de firma | autenticacao / reconhecimento presencial | BR: reconhecimento de firma (2 tipos: simples e autentico) |
| signature | assinatura | assinatura | Mesmo termo |
| legalization | legalizacao | legalizacao | Mesmo termo |
| public instrument | instrumento publico | instrumento publico | Mesmo conceito |

## Tabela 10: Diferencas Ortograficas e Gramaticais (Direito)

| Regra | BR | PT | Exempl0 |
|---|---|---|---|
| Prefixo co- (sem hifen) | coobrigacao | co-obrigacao | PT mantem hifen |
| Prefixo anti- (com hifen antes de h) | anti-horario | anti-horario | Igual |
| Palavra 'acao' | acao | accao | PT: cc |
| Palavra 'contrato' | contrato | contrato | Identico |
| Palavra 'direito' | direito | direito | Identico |
| Palavra 'tribunal' | tribunal | tribunal | Identico |
| Palavra 'recurso' | recurso | recurso | Identico |
| Palavra 'indenizacao' | indenizacao | indemnizacao | PT: mn |
| Palavra 'excecao' | excecao | excecao | PT: cc |
| Palavra 'notificacao' | notificacao | notificacao | Identico |
| Preposicao (aquisitivo) | a | a | Mesmo uso |
| Pronome obliquo (enfase) | "lhe" | "lhe" | Uso similar |
| Colocacao pronominal | Proclise (padrao) | Enclise (padrao) | Diferenca sintatica relevante |
| Uso de "o mesmo" | "o mesmo" (evitar) | "o mesmo" (mais aceito) | BR considera vicio de linguagem |

## Tabela 11: Formulas de Cortesia e Protocolo

| Contexto | BR | PT | Notas |
|---|---|---|---|
| Excelentissimo (juiz) | Excelentissimo Senhor Juiz | Merito/Excelencia | PT: Merito para juizes |
| Vossa Excelencia | Vossa Excelencia (V. Exa.) | Vossa Excelencia (V. Exa.) | Ambos usam |
| Doutor (advogado) | Doutor (uso generalizado) | Doutor (uso formal) | BR: mais amplo |
| Ilustrissimo | Ilustrissimo Senhor | Ilustrissimo Senhor | Uso em correspondencia oficial |
| Prezado (carta formal) | Prezado Senhor | Exmo. Senhor / Caro | PT prefere Exmo. |
| Saudacao inicial | Senhor Juiz, | Merito/ Excelencia, | Diferenca de protocolo |
| Fecho (carta) | Atenciosamente | Com os melhores cumprimentos | PT: mais formal |
| Fecho (peticao) | Nestes termos, pede deferimento | Termos em que requer deferimento | Formulas diferentes |
| Data em documentos | [Cidade], [dia] de [mes] de [ano] | [Cidade], [dia] de [mes] de [ano] | Identico |

## Tabela 12: Contratos Internacionais e Bilingues

| Elemento | Decisao | Exemplo |
|---|---|---|
| Cliula de prevalencia | Definir lingua prevalente | "Em caso de duvida, prevalece a versao em portugues" |
| Estrutura bilingue | Clausula por clausula (nao pagina por pagina) | Secao 1 em PT / Secao 1 em EN |
| Definicoes | Definir termos em ambas as linguas | "Party / Parte significa..." |
| Numeracao | Manter identica nas duas versoes | Artigo 1 = Article 1 |
| Referencias legais | Preservar sistema juridico de origem | "segundo a lei do Estado de Nova York" |
| Moeda | Definir moeda + codigo ISO | "Dolar dos Estados Unidos (USD)" |
| Foro | Definir foro com clareza | "Fica eleito o foro da Comarca de Sao Paulo" |
| Lei aplicavel | Especificar | "Este contrato sera regido pelas leis da Republica Federativa do Brasil" |

## Tabela 13: Pesquisa e Verificacao Terminologica

| Contexto | Acao | Ferramenta / Fonte |
|---|---|---|
| Termo juridico desconhecido | Verificar em legislacao brasileira | Planalto.gov.br (legislacao federal) |
| Termo juridico PT | Verificar em legislacao europeia | Diario da Republica Eletronico (dre.pt) |
| Jurisprudencia BR | Pesquisar acordaos | STJ / STF sites |
| Jurisprudencia PT | Pesquisar acordaos | dgsi.pt (base do Ministerio da Justica) |
| Dicionario juridico BR | Consultar terminologia | Dicionario Juridico (Maria Helena Diniz) |
| Dicionario juridico PT | Consultar terminologia | Dicionario Juridico (Jorge Miranda / Jose Almeida) |
| Codigo Civil BR | Consultar texto oficial | Lei 10.406/2002 |
| Codigo Civil PT | Consultar texto oficial | DL 47344/66 |
| Vocabulario juridico comparado | Verificar equivalencia | Vocabulario Juridico (Deocleciano Torrieri) |

## Tabela 14: Cliulas Contratuais Especificas

| Tipo de Clausula | BR | PT | Observacao |
|---|---|---|---|
| Confidentiality | Confidencialidade | Confidencialidade | NDA = Acordo de Confidencialidade |
| Non-compete | Nao concorrencia | Nao concorrencia | Ambos usam |
| Non-solicitation | Nao aliciamoento | Nao aliciamoento | Ambos usam |
| Termination for cause | Rescisao por justa causa | Resolucao por justa causa | PT: resolucao |
| Termination for convenience | Rescisao sem justa causa | Denuncia | PT: denuncia contratual |
| Force majeure | Forca maior | Forca maior | Mesmo termo |
| Hardship | Onerosidade excessiva | Alteracao das circunstancias | BR: teoria da imprevisao |
| Entire agreement | Integralidade | Acordo pleno / clausula de integralidade | BR: clausula de integralidade |
| Severability | Nulidade parcial | Reducao / separabilidade | PT: separabilidade |
| Waiver | Renuncia | Renuncia | Mesmo termo |
| Notice | Notificacao / Comunicacao | Notificacao | Ambos usam |
| Assignment | Cessao | Cessao | "Cessao de direitos" |
| Subcontracting | Subcontratacao | Subcontratacao | Mesmo termo |
| Survival | Sobrevivencia | Subsistencia | PT: subsistencia (clausulas que sobrevivem ao termino) |

## Tabela 15: Numeracao e Formatacao de Documentos Juridicos

| Elemento | Formato BR | Formato PT | Exemplo |
|---|---|---|---|
| Artigo (principal) | Artigo 1. | Artigo 1. | Com ponto apos numeral |
| Artigo (secundario) | Artigo 1 - A | Artigo 1 - A | Letra maiuscula |
| Paragrafo | Paragrafo unico | Numero unico | BR usa por extenso |
| Inciso | I - | a) | BR: romanos; PT: letras |
| Alinea | a) | a) | Ambos: letras minusculas |
| Item | 1. | 1. | Numerico |
| Clausula (contrato) | Clausula Primeira | Clausula Primeira | BR: ordinal ate 10 |
| Clausula (numerica) | Clausula 1.1 | Clausula 1.1 | Hierarquica |
| Referencia cruzada | nos termos do Artigo 3 | nos termos do Artigo 3 | Mesmo formato |
| Enumarcao | (i) / (ii) / (iii) | (i) / (ii) / (iii) | Romano em ambos |

---

# Standards: Padroes para Documentos Juridicos em Portugues

## Sistema Juridico Brasileiro

### Codigos e Legislacao Principal

- **Constituicao Federal de 1988**: Lei fundamental do ordenamento juridico brasileiro
- **Codigo Civil (Lei 10.406/2002)**: Direito privado, obrigacoes, contratos, sociedades, familia, sucessoes
- **Codigo de Processo Civil (Lei 13.105/2015)**: Processo judicial civil
- **Codigo Penal (DL 2848/1940)**: Direito penal material
- **Codigo de Processo Penal (DL 3689/1941)**: Processo penal
- **Codigo Tributario Nacional (Lei 5172/1966)**: Direito tributario
- **CLT (DL 5452/1943)**: Consolidacao das Leis do Trabalho
- **Codigo de Defesa do Consumidor (Lei 8078/1990)**: Protecao do consumidor
- **Lei das S.A. (Lei 6404/1976)**: Sociedades por acoes
- **Lei de Arbitragem (Lei 9307/1996)**: Arbitragem nacional e internacional
- **Lei de Introducao as Normas do Direito Brasileiro (LINDB - DL 4657/1942)**: Normas de aplicacao do direito
- **Lei Geral de Protecao de Dados (LGPD - Lei 13.709/2018)**: Dados pessoais

### Estrutura do Poder Judiciario

- **STF** (Supremo Tribunal Federal): guardiao da Constituicao
- **STJ** (Superior Tribunal de Justica): uniformizacao da legislacao infraconstitucional
- **TST** (Tribunal Superior do Trabalho): justica do trabalho
- **TSE** (Tribunal Superior Eleitoral): justica eleitoral
- **STM** (Superior Tribunal Militar): justica militar
- **TRFs** (Tribunais Regionais Federais): 2 grau da justica federal
- **TJ**s (Tribunais de Justica): 2 grau da justica estadual
- **TRTs** (Tribunais Regionais do Trabalho): 2 grau da justica trabalhista

### Orgaos Essenciais

- **OAB** (Ordem dos Advogados do Brasil): regulamentacao da advocacia
- **MP** (Ministerio Publico): fiscal da lei e acao penal publica
- **DP** (Defensoria Publica): assistencia juridica gratuita
- **DPU** (Defensoria Publica da Uniao): assistencia federal
- **DPE** (Defensoria Publica Estadual): assistencia estadual
- **AGU** (Advocacia-Geral da Uniao): representacao judicial da Uniao
- **PGE** (Procuradoria-Geral do Estado): representacao do estado
- **PGM** (Procuradoria-Geral do Municipio): representacao do municipio

### Formacao dos Profissionais

- **Bacharel em Direito**: curso superior de 5 anos
- **Exame de Ordem (OAB)**: requisito para exercicio da advocacia
- **Concurso publico**: ingresso na magistratura, ministerio publico, defensoria
- **Juiz de Direito**: ingressa por concurso, carreira de entrancia inicial a final
- **Desembargador**: juiz promovido ao tribunal de segundo grau
- **Ministro**: juiz dos tribunais superiores (STJ, STF, etc.)

## Sistema Juridico Portugues

### Codigos e Legislacao Principal

- **Constituicao da Republica Portuguesa (1976)**: Lei fundamental
- **Codigo Civil (DL 47344/66)**: Direito privado (anterior ao BR mas reformado)
- **Codigo de Processo Civil (Lei 41/2013)**: Processo civil
- **Codigo Penal (DL 48/95)**: Direito penal
- **Codigo de Processo Penal (DL 78/87)**: Processo penal
- **Codigo das Sociedades Comerciais (DL 262/86)**: Direito societario
- **Codigo do Trabalho (Lei 7/2009)**: Direito do trabalho
- **Codigo dos Contratos Publicos (DL 18/2008)**: Contratacao publica
- **Regime do Arrendamento Urbano (Lei 6/2006)**: Arrendamentos
- **Lei da Arbitragem Voluntaria (Lei 63/2011)**: Arbitragem
- **Regulamento Geral de Protecao de Dados (RGPD)**: Regulamento EU 2016/679
- **Lei de Enquadramento Orcamental (Lei 91/2001)**: Financas publicas

### Estrutura do Poder Judiciario

- **Supremo Tribunal de Justica**: maximo tribunal judicial
- **Tribunal Constitucional**: fiscalizacao da constitucionalidade (separado do STJ)
- **Tribunal de Contas**: fiscalizacao das financas publicas
- **Relacao** (Tribunal da Relacao): 2 grau (5 tribunais: Lisboa, Porto, Coimbra, Guimaraes, Evora)
- **Tribunal de 1 Instancia**: juizo de base (civel, penal, trabalho, familia, comercio)
- **Juizo de Paz**: pequenas causas (conciliacao)
- **Tribunal Arbitral**: arbitragem voluntaria e necessaria

### Orgaos Essenciais

- **OA** (Ordem dos Advogados): regulamentacao da advocacia
- **CN** (Conservatoria dos Registos Centrais): registos
- **IRN** (Instituto dos Registos e do Notariado): registos e notariado
- **PGR** (Procuradoria-Geral da Republica): ministerio publico
- **IGF** (Inspecao-Geral de Financas): fiscalizacao financeira
- **CMVM** (Comissao do Mercado de Valores Mobiliarios): supervisao de mercado

### Formacao dos Profissionais

- **Licenciatura em Direito**: curso de 4 anos (pos-Bolonha)
- **Exame Nacional de Acesso a Advocacia (ENAA)**: 2 fases (escrita e oral)
- **Estagio** (OA): estagio profissional de 12-18 meses
- **Juiz**: ingressa por concurso curricular + CRP (Centro de Estudos Judiciarios)
- **Procurador**: ingressa por concurso + CRP
- **Notario**: concurso publico + estagio

## Convencoes de Traducao Juridica

### Regras de Ouro

1. **Preservar a numeracao**: artigos, clausulas, itens, paragrafos devem manter a numeracao original
2. **Verbete juridico correto**: cada termo deve corresponder ao conceito juridico do ordenamento de destino
3. **Modalidade preservada**: shall = deve (obrigacao), may = pode (permissao), must = e obrigatorio
4. **Nao interpretar**: o tradutor juridico nao e o interprete do direito; traduz o texto, nao o aplica
5. **Notas do tradutor**: incluir notas explicativas para conceitos sem equivalente direto
6. **Bilinguismo**: em contratos bilingues, numeracao e estrutura devem ser paralelas

### Erros Graves a Evitar

- "Consideration" traduzido como "consideracao" (deve ser "contraprestacao")
- "Discovery" traduzido como "descobrimento" (deve ser "producao de provas")
- "Liability" confundido com "liberdade" (responsabilidade, nao liberdade)
- "Execution" confundido apenas com "execucao" (pode ser "assinatura" do contrato)
- "Assignment" confundido com "atribuicao" (deve ser "cessao" de direitos)
- "Indemnification" confundido com "indenizacao" (BR) vs "indemnizacao" (PT) — grafia correta

### Fontes de Consulta Obrigatorias

- Planalto.gov.br (legislacao brasileira oficial)
- DRE.pt (Diario da Republica Eletronico — legislacao portuguesa oficial)
- STJ.jus.br (jurisprudencia do STJ brasileiro)
- DGsi.pt (base de jurisprudencia portuguesa)
- Dicionarios juridicos especializados (Deocleciano Torrieri, Maria Helena Diniz, Jorge Miranda)
- Vocabulario Juridico (Academia Brasileira de Letras Juridicas)
- Guia de Traducao Juridica (CEJ — Centro de Estudos Judiciarios de Portugal)
- EUR-Lex (legislacao da Uniao Europeia)

### Regras de Estilo

- **Formalidade**: usar linguagem formal, sem contracoes, sem gírias
- **Impessoalidade**: "comunica-se", "informa-se", "requer-se"
- **Precisao**: evitar pronomes ambiguos, preferir repetir o sujeito
- **Clareza**: frases curtas, periodos bem pontuados, paragrafos organizados
- **Tradicao juridica brasileira**: proclise pronominal preferencial ("lhe comunica", nao "comunica-lhe")
- **Tradicao juridica portuguesa**: enclise pronominal preferencial ("comunica-lhe", nao "lhe comunica")
