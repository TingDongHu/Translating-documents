---
id: pt/rules/scoring-rubric
type: rules
target_lang: pt
name: Rubrica de Pontuacao — Traducao para Portugues (PT-BR / PT-PT)
description: Portuguese translation quality scoring rubric
---

# Rubrica de Pontuacao — Traducao para Portugues (PT-BR / PT-PT)

## Estrutura da Rubrica

Esta rubrica avalia traducoes para o portugues em seis dimensões, cada uma com seis bandas de pontuacao. O total e calculado como soma ponderada das dimensoes.

### Bandas de Pontuacao

| Banda | Pontos | Descricao |
|---|---|---|
| A | 6 | Excelente — sem erros ou falhas minimas |
| B | 5 | Bom — pequenos problemas, sem comprometer a qualidade |
| C | 4 | Satisfatorio — alguns problemas, qualidade aceitavel |
| D | 3 | Insuficiente — problemas significativos |
| E | 2 | Ruim — grandes problemas |
| F | 1 | Critico — falhas graves e/ou generalizadas |
| Zero | 0 | Nao aplicavel / nao realizado |

---

## Dimensao 1: Precisao Numerica (Peso: 30 %)

Avalia a correta conversao e formatacao de todos os elementos numericos: numeros, moedas, datas, horarios, porcentagens, unidades de medida e intervalos.

| Banda | Criterio |
|---|---|
| 6 | Todos os numeros estao perfeitamente formatados: virgula decimal (3,14), ponto de milhar (1.000), R$ antes com espaco zero, € depois com espaco, datas DD/MM/AAAA, horas 24h, porcentagens com espaco antes de %. Nenhum erro. |
| 5 | Ate 2 erros numericos menores, todos em elementos de baixa visibilidade. Nenhum erro em valores monetarios ou datas. Formatacao geral correta. |
| 4 | Ate 4 erros numericos, incluindo ate 1 erro em valor monetario nao critico. Datas corretas. Percentual de acerto > 90 %. |
| 3 | De 5 a 8 erros numericos, ou ate 2 erros em valores monetarios, ou 1 erro de formato de data. |
| 2 | Mais de 8 erros numericos, ou 3+ erros em valores monetarios, ou 2+ erros de data. Compromete a compreensao de secoes do documento. |
| 1 | Erros numericos generalizados. Valores monetarios majoritariamente errados. Datas em formato incorreto (ex.: MM/DD/AAAA). Documento perde a utilidade. |

**Regras de tolerancia zero nesta dimensao:**
- Virgula decimal trocada por ponto (escrever 3.14 em vez de 3,14) → penalidade minima de -2 bandas por ocorrencia
- Data em formato MM/DD/AAAA → penalidade minima de -3 bandas por ocorrencia
- Simbolo monetario na posicao errada (€ antes do valor sem espaco) → -1 banda por ocorrencia

---

## Dimensao 2: Consistencia Terminologica (Peso: 20 %)

Avalia o uso coerente de terminologia ao longo de todo o documento, incluindo a escolha entre variantes PT-BR e PT-PT.

| Banda | Criterio |
|---|---|
| 6 | Terminologia perfeitamente consistente em todo o documento. Variante regional (PT-BR ou PT-PT) aplicada coerentemente do inicio ao fim. Nenhuma oscilacao. |
| 5 | Ate 2 inconsistencias terminologicas menores, todas dentro da mesma variante regional. Nenhuma oscilacao entre PT-BR e PT-PT. |
| 4 | Ate 4 inconsistencias, ou ate 2 oscilacoes entre PT-BR e PT-PT (ex.: usar "onibus" e "autocarro" no mesmo texto). Mais de 90 % dos termos sao consistentes. |
| 3 | De 5 a 8 inconsistencias, ou 3-4 oscilacoes entre variantes. A consistencia geral ainda e compreensivel, mas perceptivel. |
| 2 | Mais de 8 inconsistencias, ou 5+ oscilacoes entre PT-BR e PT-PT. Dificulta a leitura. O documento parece ter sido traduzido por múltiplas pessoas sem coordenacao. |
| 1 | Terminologia caotica. Oscilacao constante entre PT-BR e PT-PT. Termos tecnicos traduzidos de forma diferente a cada aparicao. Documento confuso. |

**Tolerancia a variante regional (politica de tolerancia):**
- Um documento pode usar exclusivamente PT-BR ou exclusivamente PT-PT — qualquer um e aceito
- Erro e misturar as duas variantes sem justificativa
- Se o documento e destinado a um publico misto (ex.: licitacao internacional), uma nota explicativa sobre a variante escolhida e recomendada
- Palavras que sao identicas em ambas as variantes (ex.: "computador") nao contam como inconsistencia
- Para termos com diferenca PT-BR/PT-PT, se o documento usa o termo de uma variante consistentemente, mesmo que "errado" para a outra, nao e penalizado

---

## Dimensao 3: Fidelidade Semantica (Peso: 25 %)

Avalia se o significado do texto original foi preservado na traducao, sem acrescimos, omissoes ou distorcoes.

| Banda | Criterio |
|---|---|
| 6 | Significado integralmente preservado. Nenhuma informacao adicionada, omitida ou distorcida. Nuances e tom do original mantidos. Traducao fluente e precisa. |
| 5 | Ate 2 pequenos desvios semanticos que nao alteram o sentido geral. Nenhuma omissao de informacao relevante. Tom do original preservado. |
| 4 | Ate 4 desvios, ou 1 omissao menor de informacao nao critica. Sentido geral ainda fiel. Mais de 95 % do conteudo semantico preservado. |
| 3 | De 5 a 8 desvios, ou 2-3 omissoes de informacoes secundarias. O sentido geral e compreensivel, mas ha perdas perceptiveis. |
| 2 | Multiplos desvios (9+) ou omissoes significativas (4+). Trechos do original mal compreendidos ou mal traduzidos. O sentido geral e prejudicado. |
| 1 | Traducao gravemente infiel. O significado do original foi distorcido ou perdido em secoes inteiras. A traducao nao reflete o documento original. |

**Casos especiais:**
- Traducao literal que funciona em portugues: aceita e geralmente preferivel
- Traducao literal que nao funciona em portugues (estrangeirismo): penalizado como desvio semantico
- Adaptacao necessaria por diferenca cultural: nao e penalizada se explicada em nota
- Expressoes idiomaticas: avaliar pela equivalencia funcional, nao pela traducao literal

---

## Dimensao 4: Conformidade com a Formatacao (Peso: 10 %)

Avalia se o documento traduzido segue o formato estrutural do original e as convencoes de formatacao do portugues.

| Banda | Criterio |
|---|---|
| 6 | Formatacao perfeitamente preservada e adaptada ao portugues. Estrutura de paragrafos, listas, tabelas, titulos, cabecalhos e rodapes identica ou adequadamente adaptada. Marcacao [restaurado:] usada corretamente quando necessario. |
| 5 | Ate 2 pequenos desvios de formatacao (ex.: uma quebra de linha extra, um recuo incorreto). Estrutura geral preservada. |
| 4 | Ate 4 desvios de formatacao, ou 1 elemento estrutural perdido (ex.: uma tabela desalinhada). Mais de 90 % da formatacao original preservada. |
| 3 | Desvios perceptiveis (5-8) ou 2 elementos estruturais perdidos. A formatacao ainda e funcional, mas com erros visiveis. |
| 2 | Multiplos desvios (9+) ou perda de 3+ elementos estruturais. A formatacao original e dificil de reconhecer. |
| 1 | Formatacao nao preservada. Estrutura do documento irreconhecivel. Listas, tabelas e titulos fora do lugar ou ausentes. |

**Elementos avaliados:**
- Preservacao da estrutura de paragrafos
- Fidelidade ao formato de listas (ordenadas e nao ordenadas)
- Manutencao de tabelas (numero de colunas/linhas, cabecalhos)
- Preservacao de titulos e subtitulos
- Manutencao de notas de rodape e chamadas
- Uso correto de marcador [restaurado:] para correcoes de OCR
- Manutencao de quebras de pagina (se relevantes)

---

## Dimensao 5: Completude (Peso: 10 %)

Avalia se todo o conteudo do documento original foi traduzido, sem omissoes ou acrescimos indevidos.

| Banda | Criterio |
|---|---|
| 6 | Documento 100 % completo. Todo o texto do original foi traduzido. Nenhuma secao, paragrafo, frase ou palavra omitida. Nenhum acrescimo indevido. |
| 5 | Ate 2 pequenas omissoes (ex.: uma legenda de tabela, uma linha de rodape). Ou ate 2 pequenos acrescimos (ex.: uma palavra explicativa). 99 %+ completo. |
| 4 | Ate 4 omissoes menores, ou 1 paragrafo omitido. Ou 3+ pequenos acrescimos. 97 %+ completo. |
| 3 | Ate 1 secao omitida, ou ate 8 omissoes menores (total < 5 % do documento). Ou acrescimos significativos (5+ linhas de texto adicional). |
| 2 | Uma ou mais secoes omitidas (5-15 % do documento). Ou acrescimos substanciais (paragrafo ou mais). A completude geral e prejudicada. |
| 1 | Mais de 15 % do documento omitido. Ou acrescimos que alteram significativamente o documento. O documento nao pode ser considerado uma traducao completa. |

**O que conta como omissao:**
- Paragrafos inteiros nao traduzidos
- Frases puladas
- Legendas de figuras e tabelas nao traduzidas
- Notas de rodape nao traduzidas
- Texto em imagens nao transcrito (se aplicavel)
- Numeros de pagina, cabecalhos e rodapes nao traduzidos

**O que conta como acrescimo indevido:**
- Paragrafos ou frases que nao existem no original
- Comentarios do tradutor sem marcacao (uso de [N.T.] e aceito e nao penalizado)
- Explicacoes extensas desnecessarias

---

## Dimensao 6: Qualidade de Inferencia / OCR (Peso: 5 %)

Avalia a qualidade do trabalho de restauracao de texto quando o documento de origem e uma digitalizacao com artefatos de OCR.

| Banda | Criterio |
|---|---|
| 6 | Todas as correcoes de OCR sao precisas e identificadas com [restaurado:]. Nenhum artefato de OCR remanescente. Inferencias bem fundamentadas no contexto. |
| 5 | Ate 2 correcoes de OCR incorretas (inferencia errada), ou ate 2 artefatos de OCR nao corrigidos. Todas as correcoes sao marcadas. |
| 4 | Ate 4 correcoes incorretas, ou ate 4 artefatos remanescentes. A maioria das correcoes esta correta e marcada. Qualidade geral aceitavel. |
| 3 | De 5 a 8 erros de OCR nao corrigidos ou corrigidos incorretamente. Marcacao [restaurado:] faltando em varios lugares. Qualidade prejudicada. |
| 2 | Multiplos erros de OCR (9+) nao corrigidos ou corrigidos incorretamente. Marcacao ausente na maioria dos casos. A compreensao do texto e dificultada. |
| 1 | Documento com artefatos de OCR generalizados. Inferencias incorretas ou ausentes. O texto e ininteligivel em diversas partes. |

**Boa pratica:**
- Inferir palavras com base no contexto, formato do documento e conhecimento do dominio
- Quando a palavra e completamente ilegivel, usar [restaurado: ilegível]
- Quando o valor numerico e ilegivel, usar [restaurado: valor ilegível]
- Nao inventar informacao que nao pode ser inferida com confianca

---

## Calculo da Pontuacao Final

### Formula

```
Pontuacao Final = (P1 × 0,30) + (P2 × 0,20) + (P3 × 0,25) + (P4 × 0,10) + (P5 × 0,10) + (P6 × 0,05)
```

Onde Pn = pontuacao da dimensao n (na escala 0-6).

### Interpretacao da Pontuacao Final

| Pontuacao Final | Classificacao | Acao |
|---|---|---|
| 5,5 a 6,0 | Excelente | Aprovado sem revisoes |
| 4,5 a 5,4 | Bom | Aprovado com revisoes minimas |
| 3,5 a 4,4 | Satisfatorio | Revisao necessaria |
| 2,5 a 3,4 | Insuficiente | Revisao substancial necessaria |
| 1,5 a 2,4 | Ruim | Retraducao recomendada |
| 0,0 a 1,4 | Critico | Retraducao obrigatoria |

### Regra de Teto Global (Global Cap)

Independentemente da pontuacao calculada:

- **Se qualquer dimensao individual receber pontuacao 1 (Critico)**: a pontuacao final nao pode exceder **4,0** (Satisfatorio)
- **Se duas ou mais dimensoes receberem pontuacao 1 (Critico)**: a pontuacao final nao pode exceder **3,0** (Insuficiente)
- **Se qualquer dimensao receber pontuacao 0 (Zero)**: a pontuacao final e **1,0** (Critico) — documento precisa ser totalmente refeito na dimensao faltante

### Violacoes de Tolerancia Zero (Zero-Tolerance Violations)

As seguintes violacoes resultam em penalidades automaticas:

| Violacao | Penalidade |
|---|---|
| Virgula decimal trocada por ponto (ex.: 3.14 para tres inteiros e catorze centesimos) | Dimensao 1 → banda minima 3 (independente dos acertos) |
| Data em formato MM/DD/AAAA | Dimensao 1 → banda maxima 2 |
| Uso inconsistente de voce/tu no mesmo documento sem justificativa | Dimensao 9 (na rubric: dimensao de formalidade) → banda maxima 3 |
| Simbolo monetario na posicao errada de forma inconsistente | Dimensao 1 → -1 banda por ocorrencia, sem limite |
| Porcentagem sem espaco antes de % de forma inconsistente | Dimensao 1 → -1 banda por ocorrencia |

### Exemplo de Calculo

| Dimensao | Pontos | Peso | Ponderado |
|---|---|---|---|
| 1. Precisao Numerica | 5 | 30 % | 1,50 |
| 2. Consistencia Terminologica | 4 | 20 % | 0,80 |
| 3. Fidelidade Semantica | 5 | 25 % | 1,25 |
| 4. Conformidade Formatacao | 4 | 10 % | 0,40 |
| 5. Completude | 6 | 10 % | 0,60 |
| 6. Qualidade Inferencia/OCR | 5 | 5 % | 0,25 |
| **Total** | | **100 %** | **4,80** |

Neste exemplo, a pontuacao final e 4,80 — classificacao "Bom" (aprovado com revisoes minimas).

---

## Guia Rapido de Avaliacao

### Pontos de Atencao Prioritarios

1. Todos os numeros estao no formato portugues (virgula decimal)?
2. Todas as datas estao em DD/MM/AAAA?
3. A variante regional e consistente (PT-BR ou PT-PT)?
4. O significado do original foi preservado?
5. O documento esta completo?
6. Artefatos de OCR foram tratados?

### Checklist de Verificacao Rapida

- [ ] Decimais com virgula (3,14 ✓ | 3.14 ✗)
- [ ] Milhares com ponto (1.000 ✓ | 1000 ✗)
- [ ] Datas DD/MM/AAAA (25/12/2026 ✓ | 12/25/2026 ✗)
- [ ] Horas 24h (14:30 ✓ | 2:30 PM ✗)
- [ ] Moeda: R$ antes, € depois
- [ ] Variante regional consistente
- [ ] Acentuacao correta (Acordo 1990)
- [ ] Pontuacao conforme norma (aspas, travessao)
- [ ] OCR tratado com [restaurado:]
- [ ] Nenhuma secao omitida
- [ ] Tom e formalidade consistentes
- [ ] Estrangeirismos adequados ou traduzidos

---

*Rubrica versao 1.0 — maio de 2026*
