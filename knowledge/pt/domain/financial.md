---
id: pt/domain/financial
type: domain
target_lang: pt
name: Documentos financeiros (portugues)
description: Terminologia e regras para documentos financeiros traduzidos para portugues brasileiro e portugues europeu. Cobertura dos formatos BRL/EUR, balanco patrimonial, normas contabeis CPC (BR) e SNC (PT), relatorios financeiros, auditoria e tributacao.
---

# Reader Model: Leitor de Documentos Financeiros

## Perfil do Leitor (Brasil)

| Atributo | Descricao |
|---|---|
| Formacao | Contadores, auditores, analistas financeiros, investidores, CFOs, consultores |
| Nivel de especializacao | Alto — dominio de terminologia contabil e financeira brasileira (CPC) |
| Expectativa principal | Precisao absoluta em valores numericos, conformidade com CPC e IFRS |
| Sensibilidade a erros | Extrema — um valor incorreto pode distorcer demonstracoes financeiras |
| Variante preferida | Portugues brasileiro tecnico-contabil com terminologia CPC (Comite de Pronunciamentos Contabeis) |
| Contexto de leitura | Balanco patrimonial, DRE, notas explicativas, relatorios de auditoria, prospectos |

## Perfil do Leitor (Portugal)

| Atributo | Descricao |
|---|---|
| Formacao | Contabilistas certificados, auditores, analistas, gestores financeiros, investidores |
| Nivel de especializacao | Alto — dominio do SNC (Sistema de Normalizacao Contabilistica) |
| Expectativa principal | Conformidade com SNC e IAS/IFRS adotados pela Uniao Europeia |
| Sensibilidade a erros | Extrema — especialmente em classificacao de contas e valores |
| Variante preferida | Portugues europeu tecnico-contabil com terminologia SNC |
| Contexto de leitura | Demonstracoes financeiras, anexos, relatorios de auditoria, contas anuais |

## Hierarquia de Necessidades do Leitor

1. Exactidao absoluta de todos os valores numericos (tolerancia zero)
2. Classificacao contabil correta (ativo, passivo, receita, despesa, patrimonio liquido)
3. Conformidade com normas locais (CPC no BR, SNC em PT) e internacionais (IFRS/IAS)
4. Notas explicativas consistentes com os valores das demonstracoes
5. Terminologia consistente entre demonstracoes financeiras e notas anexas

## Comportamento de Leitura

- Leitura analitica extremamente detalhada — cada valor e verificado
- Comparacao inter-periodos e inter-demonstracoes (balanco vs DRE vs fluxo de caixa)
- Notas explicativas sao lidas em paralelo com as demonstracoes principais
- Qualquer inconsistencia numerica entre documentos e imediatamente detectada
- Auditores realizam leitura de validacao: conferencia de valores e normas

---

# Decision Framework: Traducao Financeira PT

## Tabela 1: Formatos Numericos e Monetarios

| Contexto | BR | PT | Observacao |
|---|---|---|---|
| Valor monetario | R$ 1.234,56 | 1.234,56 EUR | BR: R$ prefixo; PT: EUR sufixo |
| Milhar | 1.000 (ponto) | 1 000 (espaco) ou 1.000 | PT tradicional: espaco; uso de ponto tolerado |
| Decimal | 1,50 (virgula) | 1,50 (virgula) | Ambos usam virgula decimal |
| Valor negativo | (1.234,56) ou -1.234,56 | (1.234,56) ou -1.234,56 | Parenteses sao padrao contabil |
| Porcentagem | 15,5% | 15,5% | Mesmo formato |
| Milhoes BR | R$ 1,5 milhao | 1,5 milhoes EUR | BR: 1,5 milhao (singular) |
| Bilhoes | R$ 1,5 bilhao (BR = 10^9) | 1,5 mil milhoes (PT = 10^9) | ATENCAO: bilhao BR = mil milhoes PT |
| Cotacao de acoes | R$ 35,72 | 35,72 EUR | Mesmo formato |
| Indice financeiro | 1,23x | 1,23x | Multiplos |
| Data de demonstracoes | 31/12/2025 | 31/12/2025 | dd/mm/aaaa |
| Ano fiscal | Ano-calendario | Ano civil | BR: ano-calendario; PT: ano civil |
| Periodo | 1T2026 / 1o trimestre de 2026 | 1T2026 / 1 trimestre de 2026 | Mesmo formato |

## Tabela 2: Balanco Patrimonial — Ativo

| Termo Fonte | BR (CPC) | PT (SNC) | Observacao |
|---|---|---|---|
| Balance sheet | Balanco patrimonial | Balanco | PT: apenas "Balanco" |
| Assets | Ativo | Ativo | Mesmo termo |
| Current assets | Ativo circulante | Ativo corrente | BR: circulante; PT: corrente |
| Non-current assets | Ativo nao circulante | Ativo nao corrente | Diferenca regional |
| Fixed assets | Imobilizado | Ativo fixo tangivel | BR: imobilizado |
| Intangible assets | Intangivel | Ativo intangivel | Mesmo conceito |
| Property, plant and equipment | Imobilizado / PPE | Ativo fixo tangivel | Diferenca significativa |
| Cash and cash equivalents | Caixa e equivalentes de caixa | Caixa e seus equivalentes | Mesmo conceito |
| Accounts receivable | Contas a receber / Clientes | Clientes / Contas a receber | Ambos usam |
| Inventory | Estoques | Inventarios | BR: estoques; PT: inventarios |
| Prepaid expenses | Despesas antecipadas | Gastos diferidos | Diferenca regional |
| Investments | Investimentos | Investimentos financeiros | BR: Investimentos (ANC) |
| Deferred tax assets | Ativo fiscal diferido | Ativos por impostos diferidos | Mesmo conceito |
| Biological assets | Ativo biologico | Ativos biologicos | Agropecuaria |
| Construction in progress | Imobilizado em andamento | Imobilizacoes em curso | PT: em curso |

## Tabela 3: Balanco Patrimonial — Passivo e PL

| Termo Fonte | BR (CPC) | PT (SNC) | Observacao |
|---|---|---|---|
| Liabilities | Passivo | Passivo | Mesmo termo |
| Current liabilities | Passivo circulante | Passivo corrente | Diferenca regional |
| Non-current liabilities | Passivo nao circulante | Passivo nao corrente | Diferenca regional |
| Accounts payable | Contas a pagar / Fornecedores | Fornecedores / Contas a pagar | Ambos usam |
| Loans and financing | Emprestimos e financiamentos | Financiamentos obtidos | Diferenca de nomenclatura |
| Debentures | Debentures | Obrigacoes / Debentures | BR usa debentures; PT prefere obrigacoes |
| Provisions | Provisoes | Provisoes | Mesmo termo |
| Contingent liabilities | Passivo contingente | Passivos contingentes | Mesmo conceito |
| Deferred tax liabilities | Passivo fiscal diferido | Passivos por impostos diferidos | Mesmo conceito |
| Shareholders equity | Patrimonio liquido | Capital proprio | BR: PL; PT: capital proprio |
| Share capital | Capital social | Capital social / Capital realizado | Mesmo termo |
| Capital reserve | Reserva de capital | Reservas de capital | Mesmo conceito |
| Revenue reserve | Reserva de lucros | Resultados transitados | Diferenca significativa |
| Retained earnings | Lucros acumulados | Resultados transitados | BR: LA; PT: resultados transitados |
| Treasury shares | Acoes em tesouraria | Acoes proprias | PT: acoes proprias |
| Non-controlling interest | Participacao de nao controladores | Interesses minoritarios | BR: nao controladores; PT: minoritarios |
| Legal reserve | Reserva legal | Reserva legal | Mesmo termo |

## Tabela 4: Demonstracoes de Resultado

| Termo Fonte | BR (CPC) | PT (SNC) | Observacao |
|---|---|---|---|
| Income statement | Demonstracao do resultado do exercicio (DRE) | Demonstracao dos resultados | DRE (BR) / DR (PT) |
| Revenue | Receita liquida / Receita | Rendimentos / Vendas | Diferenca significativa |
| Net revenue | Receita liquida | Rendimentos liquidos | BR: receita liquida |
| Cost of goods sold | Custo dos produtos vendidos (CPV) | Custo das mercadorias vendidas (CMV) | Nomenclatura similar |
| Gross profit | Lucro bruto | Resultado bruto | BR: lucro; PT: resultado |
| Selling expenses | Despesas com vendas | Gastos de distribuicao | Diferenca significativa |
| General and administrative | Despesas gerais e administrativas | Gastos gerais e administrativos | BR: despesas; PT: gastos |
| Operating profit | Lucro operacional | Resultado operacional | BR: lucro; PT: resultado |
| Financial income | Receitas financeiras | Rendimentos financeiros | BR: receitas; PT: rendimentos |
| Financial expenses | Despesas financeiras | Gastos financeiros | BR: despesas; PT: gastos |
| Net income | Lucro liquido do exercicio | Resultado liquido do periodo | BR: lucro liquido |
| Net loss | Prejuizo liquido | Resultado liquido negativo | BR: prejuizo |
| EBITDA | EBITDA / Lucro antes de juros, impostos, deprec e amort | EBITDA / Resultado antes de deprec, amort, gastos financ e impostos | Sigla universal |
| EBIT | EBIT / Lucro operacional | EBIT / Resultado operacional | Sigla universal |
| Earnings per share | Lucro por acao (LPA) | Resultado por acao | BR: LPA; PT: resultado por accao |
| Dividends | Dividendos | Dividendos | Mesmo termo |

## Tabela 5: Demonstracao dos Fluxos de Caixa

| Termo Fonte | BR (CPC 03) | PT (SNC) | Observacao |
|---|---|---|---|
| Cash flow statement | Demonstracao dos fluxos de caixa (DFC) | Demonstracao dos fluxos de caixa | Mesmo termo |
| Operating activities | Atividades operacionais | Atividades operacionais | Mesmo termo |
| Investing activities | Atividades de investimento | Atividades de investimento | Mesmo termo |
| Financing activities | Atividades de financiamento | Atividades de financiamento | Mesmo termo |
| Direct method | Metodo direto | Metodo direto | Mesmo termo |
| Indirect method | Metodo indireto | Metodo indireto | Mesmo termo |
| Net cash flow | Fluxo de caixa liquido | Fluxo de caixa liquido | Mesmo termo |
| Free cash flow | Fluxo de caixa livre | Fluxo de caixa livre / Free cash flow | Ambos usam |
| Operating cash flow | Fluxo de caixa operacional | Cash flow operacional | BR: fluxo de caixa |
| Cash generated by operations | Caixa gerado pelas operacoes | Caixa gerado pelas operacoes | Mesmo termo |
| Changes in working capital | Variacao do capital circulante liquido | Variacao do fundo de maneio | Diferenca regional |

## Tabela 6: Normas Contabeis e Pronunciamentos

| Norma Internacional | BR (CPC) | PT (SNC / IAS) | Observacao |
|---|---|---|---|
| IAS 1 — Presentation of FS | CPC 26 (R1) | IAS 1 / SNC Estrutura Conceitual | Apresentacao das demonstracoes |
| IAS 2 — Inventories | CPC 16 (R1) | IAS 2 / SNC | Estoques (BR) / Inventarios (PT) |
| IAS 7 — Cash Flow | CPC 03 (R2) | IAS 7 / SNC | Fluxo de caixa |
| IAS 16 — PPE | CPC 27 | IAS 16 / SNC | Ativo imobilizado (BR) / Ativo fixo tangivel (PT) |
| IAS 17 — Leases | CPC 06 (R2) / IFRS 16 | IFRS 16 / SNC | Arrendamento (BR) / Locacao (PT) |
| IAS 19 — Employee Benefits | CPC 33 (R1) | IAS 19 / SNC | Beneficios a empregados |
| IAS 21 — FX Effects | CPC 02 (R2) | IAS 21 / SNC | Variacao cambial |
| IAS 23 — Borrowing Costs | CPC 20 (R1) | IAS 23 / SNC | Custos de emprestimos |
| IAS 32 — Financial Instruments | CPC 39 | IAS 32 / SNC | Instrumentos financeiros |
| IAS 36 — Impairment | CPC 01 (R1) | IAS 36 / SNC | Impairment / Perda por reducao ao valor recuperavel |
| IAS 37 — Provisions | CPC 25 | IAS 37 / SNC | Provisoes, passivos e ativos contingentes |
| IAS 38 — Intangibles | CPC 04 (R1) | IAS 38 / SNC | Ativo intangivel |
| IFRS 3 — Business Combinations | CPC 15 (R1) | IFRS 3 / SNC | Combinacao de negocios |
| IFRS 9 — Financial Instruments | CPC 48 | IFRS 9 / SNC | Instrumentos financeiros (novo) |
| IFRS 15 — Revenue | CPC 47 | IFRS 15 / SNC | Receita de contratos com clientes |
| IFRS 16 — Leases | CPC 06 (R2) | IFRS 16 / SNC | Arrendamentos / Locacoes |

## Tabela 7: Termos de Auditoria

| Termo Fonte | BR | PT | Observacao |
|---|---|---|---|
| Audit | Auditoria | Auditoria | Mesmo termo |
| External audit | Auditoria externa | Auditoria externa | Mesmo termo |
| Internal audit | Auditoria interna | Auditoria interna | Mesmo termo |
| Independent auditor | Auditor independente | Auditor externo / Revisor oficial de contas (ROC) | PT: ROC |
| Audit report | Relatorio de auditoria | Relatorio de auditoria | Mesmo termo |
| Unqualified opinion | Parecer sem ressalvas | Opiniao sem reservas | BR: sem ressalvas; PT: sem reservas |
| Qualified opinion | Parecer com ressalvas | Opiniao com reservas | Diferenca regional |
| Adverse opinion | Parecer adverso | Opiniao adversa | Mesmo conceito |
| Disclaimer of opinion | Abstencao de opiniao | Escusa de opiniao / Opiniao com abstencao | PT: escusa |
| Materiality | Materialidade | Materialidade | Mesmo termo |
| Audit evidence | Evidencia de auditoria | Prova de auditoria | BR: evidencia; PT: prova |
| Audit procedure | Procedimento de auditoria | Procedimento de auditoria | Mesmo termo |
| Internal controls | Controles internos | Controlo interno | PT: controlo |
| Risk assessment | Avaliacao de risco | Avaliacao de risco | Mesmo termo |
| Sampling | Amostragem | Amostragem | Mesmo termo |
| Going concern | Continuidade operacional | Continuidade / Empresa em continuidade | BR: continuidade operacional |
| Subsequent events | Eventos subsequentes | Eventos subsequentes | Mesmo termo |
| Management letter | Carta de recomendacao | Carta de recomendacao | Mesmo termo |
| Representation letter | Carta de confirmacao | Carta de representacao / Carta de confirmacao | PT: representacao |

## Tabela 8: Tributacao — Brasil

| Sigla | Nome Completo | Incidencia | Notas |
|---|---|---|---|
| IRPJ | Imposto de Renda Pessoa Juridica | Lucro | 15% + adicional de 10% sobre lucro que exceder R$ 240 mil/ano |
| CSLL | Contribuicao Social sobre o Lucro Liquido | Lucro | 9% (geral), 15% (instituicoes financeiras) |
| PIS | Programa de Integracao Social | Faturamento | 1,65% (nao cumulativo) / 0,65% (cumulativo) |
| COFINS | Contribuicao para Financiamento da Seguridade Social | Faturamento | 7,6% (nao cumulativo) / 3% (cumulativo) |
| ICMS | Imposto sobre Circulacao de Mercadorias e Servicos | Circulacao de mercadorias | Estadual, aliquota varia por estado (7% a 18%) |
| ISS | Imposto sobre Servicos | Servicos | Municipal, 2% a 5% |
| IPI | Imposto sobre Produtos Industrializados | Industrializacao | Federal, variavel |
| IOF | Imposto sobre Operacoes Financeiras | Operacoes financeiras | Federal, varia por operacao |
| ITR | Imposto sobre a Propriedade Territorial Rural | Propriedade rural | Federal |
| ITBI | Imposto sobre Transmissao de Bens Moveis | Compra e venda de imoveis | Municipal |
| ITCMD | Imposto sobre Transmissao Causa Mortis e Doacao | Heranca e doacao | Estadual |
| FGTS | Fundo de Garantia do Tempo de Servico | Folha de pagamento | 8% sobre salario |
| INSS | Instituto Nacional do Seguro Social | Folha de pagamento | 20% (empresa) + 8-11% (empregado) |

## Tabela 9: Tributacao — Portugal

| Sigla | Nome Completo | Incidencia | Notas |
|---|---|---|---|
| IRC | Imposto sobre o Rendimento das Pessoas Colectivas | Lucro | 21% (geral) + derrama estadual e municipal |
| IRS | Imposto sobre o Rendimento das Pessoas Singulares | Rendimento pessoal | Escaloes progressivos ate 48% (incluindo sobretaxa) |
| IVA | Imposto sobre o Valor Acrescentado | Consumo | 23% (normal), 13% (intermedia), 6% (reduzida) |
| IMI | Imposto Municipal sobre Imoveis | Propriedade imobiliaria | 0,3% a 0,45% (valor patrimonial) |
| IMT | Imposto Municipal sobre Transmissoes Onerosas | Transmissao de imoveis | Progressivo ate 8% |
| IS | Imposto do Selo | Documentos, operacoes | Taxa variavel |
| Derrama | Derrama estadual / municipal | Lucro | Adicional ao IRC (estadual: 3%; municipal: ate 1,5%) |
| TSU | Taxa Social Unica | Folha de pagamento | 23,75% (empresa) + 11% (trabalhador) |
| AIMI | Adicional ao IMI | Patrimonio imobiliario elevado | 0,4% a 0,7% |
| IRS Jovem | Regime especial IRS | Rendimento de jovens | Isencao parcial por 5 anos |

## Tabela 10: Mercado de Capitais

| Termo Fonte | BR | PT | Observacao |
|---|---|---|---|
| Stock exchange | Bolsa de valores | Bolsa de valores | Mesmo termo |
| B3 | B3 (Brasil, Bolsa, Balcao) | N/A | Bolsa brasileira |
| Euronext Lisbon | N/A | Euronext Lisbon | Bolsa portuguesa |
| IPO | Oferta publica inicial (IPO) | Oferta publica inicial (IPO) | Ambos usam IPO |
| Stock | Acao | Accao | Ortografia |
| Share | Acao / Papel | Accao | BR: papel (informal) |
| Common stock | Acao ordinaria (ON) | Accao ordinaria | BR: ON; PT: ordinaria |
| Preferred stock | Acao preferencial (PN) | Accao preferencial | BR: PN; PT: preferencial |
| Bond | Titulo de divida / Debenture | Obrigacao | BR: debenture; PT: obrigacao |
| Treasury bond | Titulo publico federal | Obrigacao do Tesouro / OT | BR: Tesouro Direto |
| CVM | Comissao de Valores Mobiliarios | N/A | Regulador BR |
| CMVM | N/A | Comissao do Mercado de Valores Mobiliarios | Regulador PT |
| CVM instruction | Instrucao CVM | Regulamento CMVM | Nomenclatura diferente |
| Prospectus | Prospecto | Prospecto | Mesmo termo |
| Material fact | Fato relevante | Facto relevante | Ortografia |
| Insider trading | Uso de informacao privilegiada | Abuso de informacao privilegiada | PT: abuso de mercado |
| Market maker | Formador de mercado | Market maker / Formador de mercado | Ambos usam |
| Underwriter | Subscritor / Coordenador | Subscritor / Colocador | BR: coordenador; PT: colocador |
| Asset management | Gestao de ativos | Gestao de ativos | Mesmo termo |
| Hedge fund | Fundo hedge / Fundo multimercado | Fundo de investimento alternativo | BR: multimercado |

## Tabela 11: Derivativos e Risco

| Termo Fonte | BR | PT | Observacao |
|---|---|---|---|
| Derivative | Derivativo | Derivado | BR: derivativo; PT: derivado |
| Futures contract | Contrato futuro | Contrato de futuros | Mesmo conceito |
| Options contract | Contrato de opcoes | Contrato de opcoes | Mesmo termo |
| Swap | Swap | Swap / Troca | Ambos usam swap |
| Forward | Contrato a termo | Contrato forward / Contrato a prazo | BR: a termo; PT: forward |
| Hedging | Hedge / Protecao | Cobertura / Hedging | BR: hedge; PT: cobertura |
| Speculation | Especulacao | Especulacao | Mesmo termo |
| Arbitrage | Arbitragem | Arbitragem | Mesmo termo |
| Collateral | Garantia / Colateral | Colateral / Garantia | Ambos usam |
| Margin | Margem | Margem | Mesmo termo |
| Mark-to-market | Ajuste a mercado / Mark-to-market | Valorizacao ao mercado | BR: ajuste a mercado |
| Credit risk | Risco de credito | Risco de credito | Mesmo termo |
| Market risk | Risco de mercado | Risco de mercado | Mesmo termo |
| Liquidity risk | Risco de liquidez | Risco de liquidez | Mesmo termo |
| Operational risk | Risco operacional | Risco operacional | Mesmo termo |
| Value at Risk (VaR) | Valor em risco (VaR) | Valor em risco (VaR) | Sigla universal |
| Stress testing | Teste de estresse | Teste de stress / Teste de esforco | Diferenca regional |

## Tabela 12: Estrutura Societaria — Contabil

| Termo Fonte | BR | PT | Observacao |
|---|---|---|---|
| Subsidiary | Controlada / Subsidiaria | Subsidiaria / Empresa participada | BR: controlada |
| Parent company | Controladora | Empresa-mae / Sociedade-mãe | BR: controladora |
| Associate | Coligada / Equivalencia | Associada / Empresa associada | BR: coligada |
| Joint venture | Joint venture / Empreendimento conjunto | Joint venture / Empreendimento conjunto | Ambos usam joint venture |
| Consolidation | Consolidacao | Consolidacao | Mesmo termo |
| Equity method | Metodo da equivalencia patrimonial (MEP) | Metodo da equivalencia patrimonial | BR: MEP |
| Full consolidation | Consolidacao integral | Consolidacao integral | Mesmo termo |
| Proportional consolidation | Consolidacao proporcional | Consolidacao proporcional | Mesmo termo |
| Goodwill | Agio / Goodwill | Trespass / Goodwill | Diferenca regional crucial |
| Bargain purchase | Compra vantajosa | Compra vantajosa | Mesmo termo |
| Non-controlling interest | Participacao de nao controladores | Interesses minoritarios | BR: nao controladores; PT: minoritarios |
| Business combination | Combinacao de negocios | Concentracao de atividades empresariais | Diferenca regional |
| Merger | Fusao | Fusao | Mesmo termo |
| Acquisition | Aquisicao | Aquisicao | Mesmo termo |
| Demerger | Cisao | Cisao | Mesmo termo |
| Spin-off | Cisao parcial | Cisao | Mesmo conceito |

## Tabela 13: Analise Financeira

| Termo Fonte | BR | PT | Observacao |
|---|---|---|---|
| Financial ratio | Indice financeiro | Ratio financeiro | BR: indice; PT: ratio |
| Liquidity ratio | Indice de liquidez | Ratio de liquidez | Diferenca regional |
| Current ratio | Liquidez corrente | Liquidez geral / Ratio do ativo corrente | BR: liquidez corrente |
| Quick ratio | Liquidez seca | Liquidez imediata / Ratio de liquidez reduzida | Diferenca regional |
| Debt-to-equity | Divida / PL | Ratio de endividamento / Passivo / Capital proprio | BR: divida sobre PL |
| Return on equity (ROE) | Retorno sobre o PL (ROE) | Rendibilidade dos capitais proprios (ROE) | BR: retorno; PT: rendibilidade |
| Return on assets (ROA) | Retorno sobre o ativo (ROA) | Rendibilidade do ativo (ROA) | Diferenca regional |
| EBITDA margin | Margem EBITDA | Margem EBITDA | Mesmo termo |
| Net margin | Margem liquida | Margem liquida | Mesmo termo |
| Gross margin | Margem bruta | Margem bruta | Mesmo termo |
| Working capital | Capital circulante liquido / Capital de giro | Fundo de maneio | Diferenca significativa |
| Leverage | Alavancagem | Alavancagem / Endividamento | Ambos usam alavancagem |
| Break-even point | Ponto de equilibrio | Ponto critico / Break-even | BR: ponto de equilibrio |
| CAGR | CAGR (taxa de crescimento anual composta) | CAGR (taxa de crescimento anual composta) | Sigla universal |
| Discounted cash flow (DCF) | Fluxo de caixa descontado | Fluxo de caixa descontado | Mesmo termo |

## Tabela 14: Orcamento e Planejamento Financeiro

| Termo Fonte | BR | PT | Observacao |
|---|---|---|---|
| Budget | Orcamento | Orcamento | Mesmo termo |
| Budgeting | Orcamentacao | Elaboracao do orcamento | BR: orcamentacao |
| Forecast | Previsao | Previsao | Mesmo termo |
| Projection | Projecao | Projeccao | Ortografia |
| Business plan | Plano de negocios | Plano de negocios | Mesmo termo |
| Financial planning | Planejamento financeiro | Planeamento financeiro | Ortografia |
| Cash budget | Orcamento de caixa | Orcamento de tesouraria | PT: tesouraria |
| Capital budget | Orcamento de capital | Orcamento de investimentos | BR: capital; PT: investimentos |
| Variance analysis | Analise de variacoes | Analise de desvios | BR: variacoes; PT: desvios |
| Actual vs budget | Realizado vs Orcado | Real vs Orcamento | Diferenca sutil |
| Rolling forecast | Previsao continua | Previsao continua / Rolling forecast | Ambos usam |
| Zero-based budgeting | Orcamento base zero | Orcamento de base zero | Mesmo conceito |
| Capex | CAPEX / Investimento em capital | CAPEX / Investimento | Sigla universal |
| Opex | OPEX / Despesa operacional | OPEX / Gasto operacional | Sigla universal |

## Tabela 15: Termos Bancarios e de Credito

| Termo Fonte | BR | PT | Observacao |
|---|---|---|---|
| Loan | Emprestimo | Emprestimo | Mesmo termo |
| Financing | Financiamento | Financiamento | Mesmo termo |
| Mortgage | Hipoteca / Financiamento imobiliario | Hipoteca / Credito hipotecario | BR: financiamento imobiliario |
| Collateral | Garantia | Garantia / Colateral | Mesmo termo |
| Guarantee | Aval / Fianca / Garantia | Aval / Garantia pessoal | BR: aval (titulos), fianca (contratos) |
| Interest rate | Taxa de juros | Taxa de juro | BR: juros (plural); PT: juro (singular) |
| Selic rate | Taxa Selic | N/A | Taxa basica BR |
| Euribor | N/A | Euribor | Taxa interbancaria europeia |
| CDI | Certificado de Deposito Interbancario | N/A | BR |
| Prime rate | Taxa preferencial | Prime rate | Mesmo conceito |
| Spread | Spread | Spread / Margem | Ambos usam spread |
| Amortization | Amortizacao | Amortizacao | Mesmo termo |
| Grace period | Carencia | Periodo de carencia | Mesmo termo |
| Default | Inadimplemento | Incumprimento | Diferenca regional crucial |
| Restructuring | Reestruturacao | Reestruturacao | Mesmo termo |
| Overdraft | Cheque especial | Descoberto bancario | BR: cheque especial |
| Credit card | Cartao de credito | Cartao de credito | Mesmo termo |
| Debit card | Cartao de debito | Cartao de debito | Mesmo termo |
| PIX | PIX | N/A | Sistema BR |
| MB Way | N/A | MB Way | Sistema PT |

---

# Standards: Padroes para Documentos Financeiros em Portugues

## Normas Contabeis no Brasil (CPC)

### Orgao Regulador

- **CPC (Comite de Pronunciamentos Contabeis)**: criado pela Resolucao CFC 1055/05, emite pronunciamentos tecnicos
- **CFC (Conselho Federal de Contabilidade)**: fiscalizacao da profissao contabil
- **CVM (Comissao de Valores Mobiliarios)**: regulacao do mercado de capitais
- **Receita Federal**: regulacao tributaria e fiscal

### Principais Pronunciamentos

| Numero | Tema | Equivalente IFRS |
|---|---|---|
| CPC 01 (R1) | Reducao ao valor recuperavel de ativos | IAS 36 |
| CPC 02 (R2) | Efeitos das mudancas nas taxas de cambio | IAS 21 |
| CPC 03 (R2) | Demonstracao dos fluxos de caixa | IAS 7 |
| CPC 04 (R1) | Ativo intangivel | IAS 38 |
| CPC 05 (R1) | Divulgacao sobre partes relacionadas | IAS 24 |
| CPC 06 (R2) | Arrendamentos | IFRS 16 |
| CPC 07 (R1) | Subvencoes e assistencia governamentais | IAS 20 |
| CPC 08 (R1) | Custos de transacao e premios na emissao de titulos | N/A |
| CPC 09 | Demonstracao do valor adicionado (DVA) | N/A (especifico BR) |
| CPC 10 (R1) | Pagamento baseado em acoes | IFRS 2 |
| CPC 11 | Seguros | IFRS 4 |
| CPC 12 | Ajuste a valor presente | N/A |
| CPC 13 (R1) | Adocao inicial da Lei 11.638/07 | N/A |
| CPC 14 (R1) | Estimativas contabeis, erro e mudanca | IAS 8 |
| CPC 15 (R1) | Combinacao de negocios | IFRS 3 |
| CPC 16 (R1) | Estoques | IAS 2 |
| CPC 17 (R1) | Contratos de construcao | IAS 11 (substituido) |
| CPC 18 (R2) | Investimento em coligada e em controlada | IAS 28 |
| CPC 19 (R1) | Negocios em conjunto | IFRS 11 |
| CPC 20 (R1) | Custos de emprestimos | IAS 23 |
| CPC 21 (R1) | Demonstracao intermediaria | IAS 34 |
| CPC 22 | Informacoes por segmento | IFRS 8 |
| CPC 23 | Politicas contabeis, mudancas de estimativa | IAS 8 |
| CPC 24 | Evento subsequente | IAS 10 |
| CPC 25 | Provisoes, passivos e ativos contingentes | IAS 37 |
| CPC 26 (R1) | Apresentacao das demonstracoes contabeis | IAS 1 |
| CPC 27 | Ativo imobilizado | IAS 16 |
| CPC 28 | Propriedade para investimento | IAS 40 |
| CPC 29 | Ativo biologico e produto agricola | IAS 41 |
| CPC 30 (R1) | Receitas | IFRS 15 (substituido) |
| CPC 31 | Ativo nao corrente mantido para venda | IFRS 5 |
| CPC 32 | Tributos sobre o lucro | IAS 12 |
| CPC 33 (R1) | Beneficios a empregados | IAS 19 |
| CPC 34 | Exploracao e avaliacao de recursos minerais | IFRS 6 |
| CPC 35 | Demonstracoes separadas | IAS 27 |
| CPC 36 (R3) | Demonstracoes consolidadas | IFRS 10 |
| CPC 37 (R1) | Adocao inicial das normas internacionais | IFRS 1 |
| CPC 38 | Instrumentos financeiros: reconhecimento e mensuracao | IAS 39 (substituido) |
| CPC 39 | Instrumentos financeiros: apresentacao | IAS 32 |
| CPC 40 (R1) | Instrumentos financeiros: evidenciacao | IFRS 7 |
| CPC 41 | Resultado por acao | IAS 33 |
| CPC 42 | Contabilidade e relatorio em economias hiperinflacionarias | IAS 29 |
| CPC 43 (R1) | Adocao inicial dos CPCs 38, 39 e 40 | N/A |
| CPC 44 | Demonstracoes combinadas | N/A |
| CPC 45 | Divulgacao de participacoes em outras entidades | IFRS 12 |
| CPC 46 | Mensuracao do valor justo | IFRS 13 |
| CPC 47 | Receita de contratos com clientes | IFRS 15 |
| CPC 48 | Instrumentos financeiros | IFRS 9 |

### Demonstracoes Financeiras Obrigatorias (BR)

1. Balanco Patrimonial (BP)
2. Demonstracao do Resultado do Exercicio (DRE)
3. Demonstracao do Resultado Abrangente (DRA)
4. Demonstracao dos Fluxos de Caixa (DFC) — metodo direto ou indireto
5. Demonstracao do Valor Adicionado (DVA) — obrigatoria para Cias Abertas
6. Demonstracao das Mutacoes do Patrimonio Liquido (DMPL)
7. Notas Explicativas (NE)
8. Relatorio da Administracao
9. Parecer dos Auditores Independentes

## Normas Contabeis em Portugal (SNC)

### Orgao Regulador

- **CNC (Comissao de Normalizacao Contabilistica)**: emissao de normas SNC
- **OCC (Ordem dos Contabilistas Certificados)**: regulamentacao da profissao
- **CMVM (Comissao do Mercado de Valores Mobiliarios)**: regulacao do mercado de capitais
- **AT (Autoridade Tributaria)**: regulacao fiscal

### Sistema de Normalizacao Contabilistica (SNC)

O SNC foi implementado pelo DL 158/2009, substituindo o POC (Plano Oficial de Contabilidade). Estrutura:

- **Estrutura Conceitual**: base conceitual para preparacao das demonstracoes financeiras
- **Modelos de Demonstracoes Financeiras (MDF)**: formatos oficiais
- **Codigo de Contas (CC)**: plano de contas oficial
- **NCRF (Normas Contabilisticas e de Relato Financeiro)**: 28 normas (numeracao de 1 a 28)
- **NCRF-PE (Norma para Pequenas Entidades)**: regime simplificado
- **NCRF-ME (Norma para Microentidades)**: regime ainda mais simplificado
- **NI (Normas Interpretativas)**: interpretacoes tecnicas

### Principais NCRF

| Numero | Tema | Equivalente IFRS |
|---|---|---|
| NCRF 1 | Estrutura e conteudo das demonstracoes financeiras | IAS 1 |
| NCRF 2 | Demonstracao dos fluxos de caixa | IAS 7 |
| NCRF 3 | Adocao pela primeira vez das NCRF | IFRS 1 |
| NCRF 4 | Politicas contabilisticas, alteracoes nas estimativas | IAS 8 |
| NCRF 5 | Activos fixos tangiveis | IAS 16 |
| NCRF 6 | Activos intangiveis | IAS 38 |
| NCRF 7 | Activos biologicos | IAS 41 |
| NCRF 8 | Propriedades de investimento | IAS 40 |
| NCRF 9 | Locações | IAS 17 (substituido) |
| NCRF 10 | Custos de emprestimos obtidos | IAS 23 |
| NCRF 11 | Inventarios | IAS 2 |
| NCRF 12 | Imposto sobre o rendimento | IAS 12 |
| NCRF 13 | Interesses em empreendimentos conjuntos | IAS 31 |
| NCRF 14 | Concentracoes de actividades empresariais | IFRS 3 |
| NCRF 15 | Investimentos em subsidiarias e associadas | IAS 27/28 |
| NCRF 16 | Exploracao e avaliacao de recursos minerais | IFRS 6 |
| NCRF 17 | Agricultura | IAS 41 |
| NCRF 18 | Contratos de construcao | IAS 11 |
| NCRF 19 | Rendimento | IAS 18 |
| NCRF 20 | Provisoes, passivos contingentes e activos contingentes | IAS 37 |
| NCRF 21 | Efeitos de alteracoes em taxas de cambio | IAS 21 |
| NCRF 22 | Subsidios do governo | IAS 20 |
| NCRF 23 | Beneficios dos empregados | IAS 19 |
| NCRF 24 | Divulgacao de partes relacionadas | IAS 24 |
| NCRF 25 | Imparidade de activos | IAS 36 |
| NCRF 26 | Instrumentos financeiros | IAS 32/39 |
| NCRF 27 | Relato por segmentos | IFRS 8 |
| NCRF 28 | Adocao pela primeira vez das NCRF-PE | N/A |

### Demonstracoes Financeiras Obrigatorias (PT)

1. Balanco (BL)
2. Demonstracao dos Resultados (DR) — por naturezas ou por funcoes
3. Demonstracao dos Resultados Abrangentes (DRA)
4. Demonstracao das Alteracoes no Capital Proprio (DACP)
5. Demonstracao dos Fluxos de Caixa (DFC)
6. Anexo (ANX)
7. Relatorio de Gestao
8. Parecer do Auditor / Revisor Oficial de Contas (ROC)

## Convencoes de Traducao Financeira

### Tolerancia Zero para Numeros

- Nenhum valor numerico pode ser alterado, arredondado, truncado ou modificado
- Verificar triplamente valores em tabelas: origem, traducao, destino
- Conferir totais e subtotais apos traducao para garantir consistencia

### Terminologia Critica

- "Goodwill" no BR = "agio" (ou goodwill); em PT = "trespass" (ou goodwill)
- "Revenue" no BR = "receita liquida"; em PT = "rendimentos" (depende do contexto)
- "Expenses" no BR = "despesas"; em PT = "gastos" (ou "custos")
- "Working capital" no BR = "capital circulante liquido / capital de giro"; em PT = "fundo de maneio"
- "Lease" no BR = "arrendamento"; em PT = "locacao"
- "Derivative" no BR = "derivativo"; em PT = "derivado"

### Referencias a Normas

- Quando um documento cita IAS/IFRS, manter o numero da norma internacional
- Em documentos BR, adicionar entre parenteses a referencia CPC correspondente
- Em documentos PT, adicionar entre parenteses a referencia NCRF correspondente
- Exemplo: "IAS 36 (CPC 01 R1)" para BR ou "IAS 36 (NCRF 25)" para PT

### Formatacao de Valores

- Balanco e DRE: valores em milhares ou milhoes, com indicacao clara no cabecalho
- Notas explicativas: valores em reais (R$) ou euros (EUR), com definicao da moeda
- Comparacao inter-periodos: colunas lado a lado com o ano mais recente a esquerda
- Valores negativos: entre parenteses ou com sinal de menos (consistente)

### Glossario de Termos Financeiros Problematicos

| Termo | Problema | Solucao BR | Solucao PT |
|---|---|---|---|
| Goodwill | Diferenca regional de traducao | Agio (ou goodwill) | Trespass (ou goodwill) |
| Revenue | Escopo semantico | Receita (liquida) | Rendimentos / Volume de negocios |
| Expense | Palavra vs escopo | Despesa | Gasto |
| Cost | Custo vs despesa | Custo | Custo |
| Lease | Termo juridico-contabil | Arrendamento | Locacao |
| Rent | Aluguel vs renda | Aluguel (pago) / Renda (recebida) | Renda (paga ou recebida) |
| Stock | Estoque vs acao | Estoque (inventario) / Acao (titulo) | Inventario / Accao |
| Bond | Titulo de divida | Debenture / Titulo | Obrigacao |
| Provision | Provisao vs reserva | Provisao | Provisao |
| Reserve | Reserva de lucros | Reserva | Reserva |
| Bill | Duplicata vs conta | Duplicata (titulo) / Conta (fatura) | Letra / Fatura |
| Merger | Consolidacao | Fusao | Fusao |
| Amortization | Depreciacao vs amortizacao | Amortizacao (intangivel) / Depreciacao (tangivel) | Amortizacao (ambos) |
| Impairment | Perda vs reducao | Perda por reducao ao valor recuperavel | Imparidade |
| Fair value | Valor de mercado | Valor justo | Valor justo / Justo valor |
| Disclosure | Divulgacao vs evidenciacao | Divulgacao | Divulgacao / Evidenciacao |
| Materiality | Relevancia | Materialidade | Materialidade |
| Contingency | Evento incerto | Contingencia | Contingencia |
