---
id: pt/rules/base
type: rules
target_lang: pt
name: Regras de Traducao para Portugues (PT-BR / PT-PT)
description: Portuguese base translation rules
---

# Regras de Traducao para Portugues (PT-BR / PT-PT)

## 1. Formatação Numerica

### 1.1 Separador Decimal e de Milhares

O portugues utiliza o sistema europeu continental para numeros:

| Componente | Regra | Exemplo PT-BR | Exemplo PT-PT |
|---|---|---|---|
| Decimal | Sempre virgula | 3,14 | 3,14 |
| Milhares | Sempre ponto | 1.000 | 1.000 |
| Milhoes | Ponto separador | 1.000.000 | 1.000.000 |

### 1.2 Numeros Negativos

- Utilizar o sinal de menos (hifen) antes do numero, sem espaco: -5, -3,14
- Em contexto financeiro, parenteses podem ser usados: (R$ 100,00)
- Nunca utilizar o simbolo de menos Unicode (U+2212); usar o hifen comum (-)

### 1.3 Porcentagens

- O simbolo % e separado do numero por um espaco: 25 %, 3,5 %
- Excecao: em tabelas com espaco limitado, pode-se usar 25% sem espaco (consistente na mesma tabela)
- Decimal em porcentagem usa virgula: 12,5 %
- Aumento de 0,5 ponto percentual (p.p.) e diferente de 0,5 % de aumento

### 1.4 Ordinais

- 1.º / 1.ª (masculino/feminino)
- 2.º / 2.ª
- Evitar forma abreviada em textos formais; preferir "primeiro", "segunda"

### 1.5 Numeros por Extenso

- Até dez (10): escrever por extenso em textos corridos
- Acima de dez: usar algarismos
- Exceção: valores monetários, datas, horários, porcentagens — sempre em algarismos
- Exceção: início de frase — sempre por extenso

### 1.6 Frações

- Usar virgula: 1/2 = 0,5
- Frações comuns por extenso: um meio, três quartos

### 1.7 Escalas e Unidades

- Espaço entre número e unidade: 10 km, 5 kg, 3 m
- Prefixos do SI sem espaço: 5MHz (exceto em textos técnicos que seguem norma do INMETRO/IPO)
- Temperatura: 25 °C (espaço entre número e unidade, exceto o símbolo ° que fica junto do C)

---

## 2. Formatação Monetaria / Moeda

### 2.1 Real Brasileiro (BRL)

- Simbolo: R$
- Posicao: **antes** do valor, sem espaco: R$ 100,00
- Centavos: sempre dois digitos após a virgula: R$ 50,00, R$ 0,50
- Milhares: R$ 1.000,00, R$ 1.000.000,00
- Valores inteiros podem omitir ",00" em contextos informais, mas recomenda-se manter em documentos formais
- Uso de "cento e" (nao "cem") para valores como R$ 110,00: "cento e dez reais"

### 2.2 Euro (EUR)

- Simbolo: €
- Posicao: **depois** do valor, com espaco: 100,00 €
- Centavos: sempre dois dígitos: 50,00 €, 0,50 €
- Milhares: 1.000,00 €
- Variante PT-PT: 100,00€ (sem espaço) e aceitavel em contextos informais, mas o padrão formal e com espaço

### 2.3 Outras Moedas

| Moeda | Simbolo | Formato PT-BR | Formato PT-PT |
|---|---|---|---|
| Dolar americano | US$ | US$ 100,00 | 100,00 US$ |
| Dolar canadense | CA$ | CA$ 100,00 | 100,00 CA$ |
| Libra esterlina | £ | £ 100,00 | 100,00 £ |
| Iene | ¥ | ¥ 100 | 100 ¥ |
| Peso argentino | AR$ | AR$ 100,00 | — |

- ISO 4217 deve ser usado em contextos formais/técnicos: BRL 100,00 (sempre depois do valor com espaço)
- Ao traduzir valores em moeda estrangeira, manter o valor original e adicionar conversão aproximada entre parenteses, se relevante: US$ 50,00 (aproximadamente R$ 250,00)

### 2.4 Centavos

- Sempre separados por virgula
- Um centavo = R$ 0,01 (nao R$ 0,01)
- Valores abaixo de 1 real: R$ 0,50 (informal: "cinquenta centavos")

### 2.5 Cambio e Conversao

- Usar "R$ 1,00 = US$ 0,19" ou "cotacao do dolar a R$ 5,20"
- Datas de cotacao: "Cotacao de 15 de marco de 2026"

---

## 3. Formatação de Data e Hora

### 3.1 Datas — Formato Numerico

| Componente | PT-BR | PT-PT |
|---|---|---|
| Ordem | DD/MM/AAAA | DD/MM/AAAA |
| Exemplo | 25/12/2026 | 25/12/2026 |
| ISO 8601 | 2026-12-25 (uso técnico) | 2026-12-25 (uso técnico) |
| Separador | Barra (/) | Barra (/) ou hifen (-) |

- **Nunca** usar MM/DD/AAAA (formato americano) — erro grave com tolerancia zero
- Ao ler datas numericas de fontes, verificar sempre se o formato original nao e americano

### 3.2 Datas — Formato Extenso

| Elemento | PT-BR | PT-PT |
|---|---|---|
| Ordem | dia de mes de ano | dia de mes de ano |
| Exemplo | 25 de dezembro de 2026 | 25 de Dezembro de 2026 |
| Artigo | "O dia 25 de marco..." | "O dia 25 de Marco..." |
| Meses | *minúscula* (obrigatorio) | *maiúscula* (tradicional, mas o AO 1990 permite minúscula) |

### 3.3 Nomes dos Meses

| Mes | PT-BR | PT-PT | Abrev. PT-BR | Abrev. PT-PT |
|---|---|---|---|---|
| Janeiro | janeiro | Janeiro | jan. | Jan. |
| Fevereiro | fevereiro | Fevereiro | fev. | Fev. |
| Marco | marco | Marco | mar. | Mar. |
| Abril | abril | Abril | abr. | Abr. |
| Maio | maio | Maio | maio | Maio |
| Junho | junho | Junho | jun. | Jun. |
| Julho | julho | Julho | jul. | Jul. |
| Agosto | agosto | Agosto | ago. | Ago. |
| Setembro | setembro | Setembro | set. | Set. |
| Outubro | outubro | Outubro | out. | Out. |
| Novembro | novembro | Novembro | nov. | Nov. |
| Dezembro | dezembro | Dezembro | dez. | Dez. |

### 3.4 Nomes dos Dias da Semana

| Dia | PT-BR | PT-PT | Abrev. |
|---|---|---|---|
| Segunda-feira | segunda-feira | Segunda-feira | seg. |
| Terca-feira | terca-feira | Terca-feira | ter. |
| Quarta-feira | quarta-feira | Quarta-feira | qua. |
| Quinta-feira | quinta-feira | Quinta-feira | qui. |
| Sexta-feira | sexta-feira | Sexta-feira | sex. |
| Sabado | sabado | Sabado | sab. |
| Domingo | domingo | Domingo | dom. |

- PT-BR: dias da semana em minúscula
- PT-PT: dias da semana tradicionalmente com maiúscula inicial

### 3.5 Horas

| Formato | PT-BR | PT-PT |
|---|---|---|
| 24h (padrao) | 14:30 | 14:30 |
| 12h (informal) | 2:30 da tarde | 2:30 da tarde |
| Separador | dois-pontos (:) | dois-pontos (:) |
| Meia-noite | 00:00 | 00:00 |
| Meio-dia | 12:00 | 12:00 |

- O formato 24h e obrigatório em contextos formais em ambos os países
- O formato 12h com "AM/PM" **nunca** deve ser usado em portugues; substituir por "da manha", "da tarde", "da noite"

### 3.6 Intervalos

- Com "a" (sem hifen): "das 14:00 as 16:00", "de 10 a 15 de marco"
- Com travessão em contextos compactos: "14:00–16:00", "10–15/03/2026"
- Nunca usar hifen simples para intervalos em textos formais

### 3.7 Diferencas Regionais Importantes

| Situacao | PT-BR | PT-PT |
|---|---|---|
| Primeiro dia do ano | 1.º de janeiro | 1 de Janeiro |
| Seculo | seculo XX | seculo XX |
| Era | 2026 d.C. | 2026 d.C. |
| Semanas | "semana do dia 5" | "semana de 5" |
| Fuso horario | Brasilia (UTC-3) | Lisboa (UTC+0 / UTC+1) |

---

## 4. Formatação de Endereços

### 4.1 Endereco Brasileiro (PT-BR)

**Estrutura hierarquica:**

```
[Tipo de logradouro] [Nome], [numero]
[Bairro]
[Cidade] - [UF]
[CEP]
```

**Exemplo completo:**
```
Rua Augusta, 1500
Consolacao
Sao Paulo - SP
01304-001
```

**Abreviaturas comuns:**

| Termo | Abrev. |
|---|---|
| Avenida | Av. |
| Rua | R. |
| Travessa | Trav. |
| Praca | Pc. |
| Bairro | — (nao abreviar) |
| Apartamento | Ap. / Apto. |
| Sala | Sl. |
| Conjunto | Cj. |
| Lote | Lt. |
| Quadra | Qd. |
| Bloco | Bl. |
| Andar | — (escrever por extenso: "10.º andar") |

**CEP:** Formato 00000-000 (hifen entre os ultimos tres dígitos)

**UF (Unidades da Federacao):** Sempre com duas letras maiúsculas e sem ponto:
AC, AL, AP, AM, BA, CE, DF, ES, GO, MA, MT, MS, MG, PA, PB, PR, PE, PI, RJ, RN, RS, RO, RR, SC, SP, SE, TO

**Complementos:** "Ap. 42", "Bl. C", "Casa 2", "Fundos"

### 4.2 Endereco Portugues (PT-PT)

**Estrutura hierarquica:**

```
[Tipo de logradouro] [Nome], [numero]
[Andar / Complemento]
[Localidade]
[Codigo-Postal] [Localidade]
```

**Exemplo completo (Lisboa):**
```
Rua Garrett, 45
2.º Direito
1200-273 Lisboa
```

**Exemplo completo (Porto):**
```
Avenida dos Aliados, 100
3.º Frente
4000-067 Porto
```

**Abreviaturas comuns em PT-PT:**

| Termo | Abrev. |
|---|---|
| Rua | R. |
| Avenida | Av. |
| Praca | Pc. |
| Largo | Lg. |
| Beco | — |
| Travessa | Tv. |
| Andar | — (por extenso: "2.º andar") |
| Direito | Dto. / D. |
| Esquerdo | Esq. / E. |
| Frente | Fr. |
| Traseiras | Tr. |
| Habitacao | Hbt. |

**Codigo postal:** Formato 0000-000 (quatro dígitos + hifen + tres dígitos)

**Nota sobre freguesias:** Desde a reorganizacao administrativa de 2013, muitas freguesias foram agrupadas. Preferir a freguesia oficial atual.

### 4.3 Enderecos em Documentos Traduzidos

- Ao traduzir um documento que contem enderecos estrangeiros, manter o endereco original e adicionar traducao entre parenteses se necessario
- Nao traduzir nomes de ruas, cidades ou países (exceto quando houver forma consagrada em portugues: "Nova Iorque", "Londres", "Paris")
- Nao traduzir "Street" para "Rua" em enderecos estrangeiros — manter o original

### 4.4 Formatos de Endereco em Diferentes Países

| Pais | Formato | Exemplo |
|---|---|---|
| EUA | Number + Street, City, State ZIP | 350 5th Ave, New York, NY 10118 |
| Reino Unido | Number + Street, City, Postcode | 10 Downing St, London SW1A 2AA |
| Franca | Number + Rue, CEP City | 5 Rue de Rivoli, 75001 Paris |
| Alemanha | Street + Number, ZIP City | Unter den Linden 1, 10117 Berlin |

---

## 5. Nomes Proprios e Acentuacao

### 5.1 Acentuacao Grafica (Acentuacao)

Regras do Acordo Ortografico de 1990 (em vigor desde 2009 no Brasil, 2009 em Portugal, com periodo de adaptacao):

| Acento | Regra | Exemplo |
|---|---|---|
| Agudo (´) | Silaba tonica aberta | cafe, sofá, lápis, fácil |
| Circunflexo (^) | Silaba tonica fechada | você, tres, mês, ônibus |
| Til (~) | Nasalizacao | maçã, irmão, canção |
| Grave (`) | Crase (a + a) | à, às, àquele |
| Trema (¨) | Abolido pelo AO 1990 | aguentar (antes: agüentar) |

**Mudancas do Acordo Ortografico de 1990:**

| Antes | Depois | Observacao |
|---|---|---|
| idéia | ideia | Paroxitonas com ditongo aberto "ei" e "oi" perderam o acento |
| assembléia | assembleia | Mesmo caso |
| heróico | heroico | Paroxitonas com "oi" perderam o acento |
| vôo | voo | Palavras paroxitonas com "oo" perderam o circunflexo |
| enjôo | enjoo | Mesmo caso |
| pára (verbo) | para | Diferencial abolido (exceto pôr/pôde) |
| pêlo (substantivo) | pelo | Diferencial abolido |
| pêra (fruta) | pera | Diferencial abolido |
| côr (substantivo) | cor | Diferencial abolido |
| lingüiça | linguiça | Trema abolido |
| qüinqüênio | quinquenio | Trema abolido |
| argüir | arguir | Trema abolido |

**Acentos diferenciais que permanecem:**
- pôr (verbo) vs. por (preposicao)
- pôde (pretérito perfeito) vs. pode (presente)
- fôrma (substantivo, aceita forma)

### 5.2 Nomes Proprios em Portugues

- Nomes proprios brasileiros seguem as regras de acentuacao: Jose, Luís, Glaucia, Marcio
- Nomes proprios portugueses seguem as mesmas regras: Jose, Luis, Gloria
- Manter a grafia original do nome da pessoa, mesmo que nao siga as regras ortograficas atuais (ex: nomes registrados antes do AO 1990)

### 5.3 Nomes Estrangeiros

| Regra | Exemplo |
|---|---|
| Manter grafia original para nomes de pessoas e marcas | McDonald's, Nietzsche, Beyoncé |
| Nao traduzir nomes de pessoas | William Shakespeare (nao "Guilherme Shakespeare") |
| Traduzir nomes de papas e monarcas consagrados | Papa Francisco, Rei Carlos III |
| Traduzir nomes de santos consagrados | Sao Joao, Sao Paulo |
| Nomes de lugares consagrados traduzir | Nova Iorque, Londres, Tóquio, Moscou/BR, Moscovo/PT |
| Nao traduzir nomes de lugares sem forma consagrada | Brandemburgo (nao), Manhattan (sim) |

**Excecoes notaveis PT-BR vs PT-PT:**

| Original | PT-BR | PT-PT |
|---|---|---|
| Moscow | Moscou | Moscovo |
| Warsaw | Varsovia | Varsovia |
| London | Londres | Londres |
| New York | Nova York / Nova Iorque | Nova Iorque |
| Los Angeles | Los Angeles | Los Angeles |
| The Hague | Haia | Haia |
| East Timor | Timor-Leste | Timor-Leste |

### 5.4 Maiusculas em Nomes Proprios

- Nomes proprios sempre com inicial maiuscula
- Nomes de cidades, estados, paises: maiuscula initial
- Nomes de ruas, avenidas, pracas: maiuscula no primeiro elemento significativo (Rua Augusta, Avenida Paulista)
- Nomes de marcas: respeitar a grafia oficial da marca (iPhone, eBay, adidas)
- Nomes de instituicoes: cada palavra com inicial maiuscula (Universidade de Sao Paulo, Banco Central do Brasil)

### 5.5 Nomes com Artigo

| Contexto | Regra | Exemplo |
|---|---|---|
| Países em PT-BR | Sem artigo para alguns, com artigo para outros | Brasil (o Brasil), Portugal, Argentina (a Argentina) |
| Países em PT-PT | Similar ao PT-BR | O Brasil, Portugal, a Argentina |
| Estados | Com artigo em PT-BR | o Rio de Janeiro, a Bahia |
| Cidades | Geralmente sem artigo | Sao Paulo (mas: o Rio de Janeiro) |

---

## 6. Pontuacao

### 6.1 Aspas

| Contexto | PT-BR | PT-PT |
|---|---|---|
| Padrao | Aspas duplas " " | Aspas angulares « » |
| Alternativo | Aspas simples ' ' | Aspas duplas " " |
| Citacao dentro de citacao | "Ele disse 'sim'" | «Ele disse "sim"» |
| Uso em jornalismo | " " | « » |
| Uso em documentos formais | " " | « » |

**PT-BR:**
- Aspas duplas sao o padrao: O ministro disse "vamos aprovar a medida".
- Aspas simples para citacao dentro de citacao.
- Pontuacao final: colocar dentro das aspas se fizer parte da citacao, fora se nao fizer.

**PT-PT:**
- Aspas angulares (comilles / aspas retas) sao o padrao formal: O ministro disse «vamos aprovar a medida».
- Aspas duplas como alternativa ou em contextos informais.
- Espaco antes e depois das aspas angulares (em textos bem formatados): « texto ».

### 6.2 Travessao

| Tipo | Uso | Exemplo |
|---|---|---|
| Travessao (—) | Discurso direto, incisos | Ele disse — e fez uma pausa — que nao viria. |
| Meia-risca (–) | Intervalos numericos | 10–20, 2020–2026 |
| Hifen (-) | Palavras compostas, prefixos | segunda-feira, pré-história |

**Regras de espacamento do travessao:**
- Discurso direto: com espaco antes e depois (mais comum no Brasil) — Ele disse — ou sem espaco (mais comum em Portugal) — Ele disse—
- Incisos: com espacos — como neste exemplo — e obrigatorio

**Diferenca entre travessao e hifen em dialogos:**
```
PT-BR:
— Ola, como vai?
— Vou bem, obrigado.

PT-PT:
— Ola, como vai?
— Vou bem, obrigado.
```

### 6.3 Vírgula

**Regras gerais do portugues:**

| Uso | Exemplo |
|---|---|
| Separar itens em lista | Comprei pao, leite, queijo e ovos. |
| Antes de "mas", "porém", "contudo" | Queria ir, mas estava chovendo. |
| Separar adjunto adverbial longo | Na manha do dia seguinte, ele partiu. |
| Separar oracao explicativa | O presidente, que estava doente, nao compareceu. |
| Separar vocativo | Maria, venha aqui. |

**Diferenca PT-BR vs PT-PT:**
- PT-BR: Virgula antes de "e" em serie de mais de tres itens e opcional (virgula de Oxford e usada mas nao obrigatoria)
- PT-PT: Menor uso de virgula antes de oracoes adverbiais

### 6.4 Ponto e Vírgula

- Usado para separar itens complexos em listas
- Usado para separar oracoes com certa relacao, mas independentes
- Nunca usado no final de listas com bullet points (usar ponto final no ultimo item)

### 6.5 Dois-pontos

- Antes de citacoes, explicacoes, enumeracoes
- Após dois-pontos, usar minúscula se for explicacao, maiúscula se for citacao formal

### 6.6 Ponto Final

- Sempre ao final de frases declarativas
- Em abreviaturas: Dr., Sr., Sra., Av.
- Em siglas, nao usar pontos: ONU, USP, PT, PSDB

### 6.7 Exclamacao e Interrogacao

| Símbolo | Regra |
|---|---|
| ? e ! | Apenas no final, nunca no inicio como em espanhol |
| ?! | Pode ser usado para surpresa/pergunta retorica, mas evitar em textos formais |
| Combinacao | Evitar "???" ou "!!!" em textos formais |

**Particularidades:**
- PT-BR: uso mais frequente de "!" em contextos informais
- PT-PT: uso mais contido de "!" mesmo em contextos informais

### 6.8 Parenteses

- Usar parenteses curvos ( ) para incisos
- Usar colchetes [ ] para intervencoes em citacoes ou OCR restaurado
- Usar chaves { } apenas em contextos matematicos ou de programacao
- Pontuacao final: fora dos parenteses se o parentese for apenas parte da frase; dentro se for frase completa

### 6.9 Reticencias

- Sempre tres pontos (…), nunca mais
- Com espaco antes: "Ele disse que viria … "
- No final de frase: com ponto final se houver continuação implícita, sem ponto se for interrupcao abrupta

---

## 7. Formatacao Geral

### 7.1 Titulos e Subtítulos

**Maiusculas em titulos:**

| Elemento | PT-BR | PT-PT |
|---|---|---|
| Primeira palavra | Maiuscula | Maiuscula |
| Palavras significativas | Minuscula | Minuscula (apenas primeira palavra com maiuscula) |
| Nomes proprios | Maiuscula | Maiuscula |
| Artigos, preposicoes | Minuscula (exceto inicio) | Minuscula (exceto inicio) |

**Regra pratica:**
- PT-BR: "A Revolucao dos Bichos: Uma Historia de Animais"
- PT-PT: "A revolucao dos bichos: uma historia de animais"

### 7.2 Listas

**Listas ordenadas (numeradas):**
```
1. Primeiro item
2. Segundo item
3. Terceiro item
```

**Listas nao ordenadas (bullet points):**
```
- Item um
- Item dois
- Item tres
```

**Formatacao de listas:**
- Cada item comeca com minúscula (se for continuacao) ou maiúscula (se for frase completa)
- Consistencia: todos os itens no mesmo formato
- Sem pontuacao no final de itens curtos
- Ponto final no ultimo item se os itens forem frases completas
- Listas de pares chave-valor usar dois-pontos alinhados

### 7.3 Tabelas

- Linhas e colunas alinhadas
- Cabecalhos em negrito
- Alinhamento de numeros a direita
- Alinhamento de texto a esquerda
- Separador de milhares e decimal consistente com as regras da secao 1

**Exemplo de tabela formatada:**

| Produto | Quantidade | Preco Unitario | Total |
|---|---|---|---|
| Cadeira | 10 | R$ 150,00 | R$ 1.500,00 |
| Mesa | 5 | R$ 450,00 | R$ 2.250,00 |
| **Total geral** | | | **R$ 3.750,00** |

### 7.4 Destaque (Negrito e Italico)

- **Negrito:** para termos importantes, secoes, definicoes
- *Italico:* para estrangeirismos, titulos de obras, enfase suave, palavras mencionadas como palavras
- Sublinhado: evitar; usar negrito ou italico
- Em documentos formais, usar negrito com moderacao

### 7.5 Siglas e Abreviaturas

- Na primeira aparicao, escrever por extenso seguido da sigla entre parenteses: "Fundacao Oswaldo Cruz (Fiocruz)"
- Siglas de ate tres letras geralmente em maiusculas: ONU, OMS, USP
- Siglas com mais de tres letras pronunciaveis como palavra: Fiocruz, Petrobras, Unesco
- Siglas estrangeiras: manter a sigla original, mas explicar em portugues na primeira ocorrencia: "World Health Organization (WHO) — Organizacao Mundial da Saude (OMS)"

### 7.6 Numeros de Pagina

- "página 15" ou "p. 15"
- Intervalo: "pp. 15–20" (com meia-risca)
- "folha 15" (uso menos comum, preferir "página")

### 7.7 Notas de Rodape

- Numeracao: 1, 2, 3 (sequencial por capitulo ou por documento)
- Chamada: sobrescrito, antes da pontuacao final
- Texto da nota: ponto final ao final

---

## 8. Gramatica

### 8.1 Ordem das Palavras (SVO)

O portugues e uma lingua SVO (Sujeito-Verbo-Objeto), mas com mais flexibilidade que o ingles:

| Estrutura | Exemplo |
|---|---|
| SVO (neutro) | O gato comeu o rato. |
| SVO com adjuntos | O gato comeu o rato rapidamente. |
| Inversao interrogativa | Comeu o gato o rato? (formal) / O gato comeu o rato? (informal/coloquial) |
| Topicalizacao | O rato, o gato comeu. (enfase) |

- Em textos formais, preferir a ordem SVO direta
- Em interrogativas indiretas, nao inverter: "Perguntei se ele veio" (nao "Perguntei se veio ele")

### 8.2 Genero (Masculino e Feminino)

**Regras gerais:**

| Terminacao | Genero | Exemplo |
|---|---|---|
| -o | Masculino | o carro, o livro |
| -a | Feminino | a casa, a mesa |
| -e | Mas ou fem. (aprender) | o leite, a fonte |
| -ista | Comum de dois | o/a dentista |
| Consoante | Mas ou fem. (aprender) | o papel, a flor |

**Profissoes:**

| PT-BR | PT-PT |
|---|---|
| A juíza | A juíza |
| A médica | A médica |
| A engenheira | A engenheira |
| A presidente | A presidente / A presidenta (aceito, menos comum) |
| A chefe | A chefe |

- Usar o genero gramatical correto para a pessoa referida
- Em textos neutros, usar o masculino generico: "os alunos" (grupo misto)
- Evitar formas como "alunos e alunas" em textos formais (preferir "os alunos" ou "o corpo discente")

### 8.3 Artigos

| Artigo | Definido | Indefinido |
|---|---|---|
| Masculino singular | o | um |
| Feminino singular | a | uma |
| Masculino plural | os | uns |
| Feminino plural | as | umas |

**Contracoes:**

| Preposicao + Artigo | Contracao |
|---|---|
| de + o | do |
| de + a | da |
| em + o | no |
| em + a | na |
| a + o | ao |
| a + a | a (com crase) |
| por + o | pelo |
| per + o (arcaico) | pelo |

**Uso de artigo antes de nomes proprios:**
- PT-BR: "A Maria chegou" (coloquial, comum)
- PT-PT: "A Maria chegou" (padrao, formal)
- Em textos formais PT-BR, evitar artigo antes de nomes proprios

### 8.4 Verbos — Conjugacao

**Tres conjugacoes:**
- 1.ª: -ar (amar, falar, cantar)
- 2.ª: -er (comer, vender, aprender)
- 3.ª: -ir (partir, abrir, decidir)

**Modos verbais:**

| Modo | Uso principal |
|---|---|
| Indicativo | Fatos, certezas |
| Subjuntivo | Duvida, possibilidade, desejo |
| Imperativo | Ordens, pedidos |
| Condicional | Condicoes, cortesia |

**Tempos verbais — Indicativo:**

| Tempo | Exemplo (falar) | Uso |
|---|---|---|
| Presente | falo | Acao atual |
| Pret. Perfeito | falei | Acao concluida |
| Pret. Imperfeito | falava | Acao habitual no passado |
| Pret. Mais-que-perfeito | falara | Acao anterior a outra passada |
| Futuro do Presente | falarei | Acao futura |
| Futuro do Pretérito | falaria | Condicional |

**Tempos verbais — Subjuntivo:**

| Tempo | Exemplo (falar) | Uso |
|---|---|---|
| Presente | fale | Duvida atual, desejo |
| Pret. Imperfeito | falasse | Condicao irreal, duvida passada |
| Futuro | falar | Eventualidade futura |

**Diferencas PT-BR vs PT-PT:**

| Construcao | PT-BR | PT-PT |
|---|---|---|
| Gerundio | Estou falando (padrao) | Estou a falar (padrao) |
| Pret. Perfeito composto | Tenho falado (menos comum) | Tenho falado (comum) |
| Futuro imediato | Vou falar | Vou falar / Hei de falar |
| "Você" informal + verbo | Voce fala | Voce fala (uso crescente) / Tu falas (tradicional) |

### 8.5 Ser vs. Estar

| Verbo | Uso | Exemplo |
|---|---|---|
| Ser | Essencia, caracteristica permanente, identidade, origem, profissao, materia | Ela e medica. A mesa e de madeira. Ele e do Brasil. |
| Estar | Estado temporario, localizacao, condicao, resultado de acao | Ela esta doente. O livro esta na mesa. A porta esta aberta. |

**Casos especificos:**
- "E morto" vs. "esta morto": "E morto" (ser, mais formal/religioso), "Esta morto" (estar, estado atual)
- "E casado" vs. "esta casado": "E casado" (estado civil), "Esta casado" (encontra-se em uniao)
- "E bom" vs. "esta bom": "E bom" (qualidade inerente), "Esta bom" (suficiente, adequado)
- "E pronto" vs. "esta pronto": "E pronto" (carater), "Esta pronto" (finalizado)

### 8.6 Haver vs. Fazer (Tempo Decorrido)

| Construcao | Exemplo |
|---|---|
| Ha (tempo decorrido) | Ha tres anos que nao o vejo. |
| Faz (tempo decorrido, coloquial) | Faz tres anos que nao o vejo. |
| Haveria (futuro do pret.) | Haveria cinco pessoas na sala. |

- "Ha" e impessoal e invariável (nao se conjuga no plural: "ha pessoas" — nao "ham pessoas")

### 8.7 Pronomes Obliquos

| Pessoa | Reto | Obliquo átono | Obliquo tónico |
|---|---|---|---|
| 1.ª sing. | eu | me | mim, comigo |
| 2.ª sing. (tu) | tu | te | ti, contigo |
| 3.ª sing. | ele/ela/você | o/a, lhe | ele/ela, si, consigo |
| 1.ª pl. | nos | nos | nos, conosco/connosco |
| 2.ª pl. | vos | vos | vos, convosco |
| 3.ª pl. | eles/elas/você | os/as, lhes | eles/elas, si, consigo |

**Colocacao pronominal:**

| Contexto | PT-BR | PT-PT |
|---|---|---|
| Inicio de frase | Proclise (preferencial) | Proclise (formal) |
| Frase afirmativa | Proclise | Enclise (preferencial) |
| Frase negativa | Proclise | Proclise |
| Com adverbio | Proclise | Proclise |
| Futuro e particípio | Mesoclise (formal) | Mesoclise |
| Gerundio | Enclise | Enclise |

**Exemplos de colocacao:**

| Contexto | PT-BR | PT-PT |
|---|---|---|
| Neutro | Me empresta o livro? | Empresta-me o livro? |
| Negativo | Nao me emprestou. | Nao me emprestou. |
| Adverbio | Sempre me ajudou. | Sempre me ajudou. |
| Futuro | Emprestar-me-ia. (formal) | Emprestar-me-ia. |
| Gerundio | Ajudando-me, conclui. | Ajudando-me, conclui. |

### 8.8 Preposicoes

**Regencia preposicional comum:**

| Verbo | Preposicao | Exemplo |
|---|---|---|
| Gostar | de | Gosto de chocolate. |
| Precisar | de | Preciso de ajuda. |
| Lembrar-se | de | Lembro-me de tudo. |
| Esquecer-se | de | Esqueci-me do recado. |
| Confiar | em | Confio em voce. |
| Acreditar | em | Acredito em Deus. |
| Morar | em | Moro em Sao Paulo. |
| Ir | para / a | Vou para casa. / Vou a Lisboa. |
| Chegar | a / em | Cheguei a casa. / Cheguei em casa (coloquial BR). |

**Diferenca PT-BR vs PT-PT:**
- PT-BR: "Chegar em" e aceito coloquialmente, mas prefira "chegar a" em textos formais
- PT-PT: "Chegar a" e a unica forma correta

### 8.9 Concordancia Verbal

- Sujeito simples: verbo concorda em numero e pessoa com o nucleo do sujeito
- Sujeito composto antes do verbo: verbo no plural
- Sujeito composto depois do verbo: verbo pode concordar com o mais proximo
- Coletivos: verbo no singular (a multidão gritou)
- Coletivo + especificacao: verbo pode ir para o plural (um grupo de pessoas saiu/sairam)
- "A maioria de", "grande parte de": verbo no singular ou plural (a maioria aprovou/aprovaram)

### 8.10 Voz Passiva

| Tipo | Construcao | Exemplo |
|---|---|---|
| Analitica (com ser) | Sujeito + ser + particípio | A lei foi aprovada. |
| Sintetica (com se) | Verbo + se | Aprovou-se a lei. / Aprovaram-se as leis. |
| Passiva de "ter" | Ter + sido + particípio | A lei tem sido discutida. |

- A voz passiva sintetica com "se" e preferivel em textos formais PT-BR
- A voz passiva analitica e comum em ambos os países

---

## 9. Formalidade e Registro

### 9.1 Pronomes de Tratamento

| Pronome | Uso | Grau de Formalidade | Regiao |
|---|---|---|---|
| Você | Interlocutor unico, informal a semiformal | Medio | Brasil (padrao), Portugal (crescente) |
| Tu | Interlocutor unico, informal | Baixo | Portugal (padrao), regioes do Brasil (RS, PA, NE) |
| O senhor / A senhora | Interlocutor unico, formal | Alto | Ambos os países |
| Vossa Senhoria | Autoridades, correspondencia formal | Muito alto | Ambos (uso administrativo) |
| Vossa Excelência | Altas autoridades | Maximo | Ambos (uso protocolar) |
| Vossa Majestade | Realeza | Maximo | Ambos |
| Vocês | Plural de voce/tu (formal) | Medio | Ambos |
| Vós | Plural de tu (arcaico/regional) | — | Portugal (arcaico, religioso) |

### 9.2 Tu vs. Voce — Variacao Regional

**No Brasil:**

| Regiao | Uso predominante | Observacao |
|---|---|---|
| Sudeste (SP, RJ, MG) | Você | "Tu" e muito raro ou inexistente |
| Sul (RS, SC) | Tu (com conjugacao de 3.ª pessoa) | "Tu vai", "tu quer" (coloquial) |
| Nordeste (PE, BA, CE, MA) | Tu (com conjugacao de 3.ª pessoa) | Uso coloquial; "voce" tambem comum |
| Norte (PA, AM) | Tu e você | Variável |
| Centro-Oeste | Você | Padrao |

**Em Portugal:**
- "Tu" e o padrao informal em todo o pais
- "Voce" e semiformal e menos usado (considerado mais distante que "tu")
- "O senhor / A senhora" para formalidade

### 9.3 Registro Formal vs. Informal

| Situacao | Formal | Informal |
|---|---|---|
| Pronome | O senhor / A senhora | Você / Tu |
| Tratamento | "Prezado(a) Sr.(a) Silva" | "Oi, Joao" |
| Verbos | Todas as formas corretas | Possiveis reducoes |
| Contracoes | Padrao | Reducoes coloquiais (pra, pro, num) |
| Gerundio | "Estamos analisando" | "Tamo analisando" |
| Vocabulario | Evitar gírias | Gírias aceitaveis |
| Frases | Completas, bem estruturadas | Fragmentos, elipses |

### 9.4 Registro PT-PT Formal

Caracteristicas do portugues formal de Portugal:
- Enclise pronominal preferencial: "Envio-lhe o documento"
- Tratamento por "Vossa Excelência" em correspondencia oficial
- Uso de "Muito respeitosamente" em fechos de carta
- Uso de "com os melhores cumprimentos" como fecho semiformal
- Evitar anglicismos sempre que possivel (preferir "ponto de encontro" a "meeting point")
- Uso do futuro do presente em vez de "ir + infinitivo": "Enviar-me-ei" (formal) vs. "Vou enviar" (informal)

### 9.5 Registro PT-BR Formal

Caracteristicas do portugues formal do Brasil:
- Proclise pronominal preferencial mesmo em inicio de frase: "Me enviarei" (formal coloquial) ou "Enviar-me-ei" (muito formal)
- Tratamento por "Vossa Senhoria" em documentos oficiais
- Uso de "Atenciosamente" como fecho formal padrao
- Uso de "Cordialmente" como fecho semiformal
- Maior tolerancia a estrangeirismos, especialmente anglicismos tecnicos
- Uso de "você" como padrao semiformal, mesmo em contextos profissionais

### 9.6 Fecho de Correspondencia

| Nível | PT-BR | PT-PT |
|---|---|---|
| Muito formal | Respeitosamente, | Com os melhores cumprimentos, |
| Formal | Atenciosamente, | Com os melhores cumprimentos, |
| Semiformal | Cordialmente, | Com os meus cumprimentos, |
| Informal | Um abraco, | Um abraco, / Com um abraco, |
| Muito informal | Beijos, / Abraco, | Beijinhos, / Abraco, |

### 9.7 Titulos e Formas de Tratamento

| Abreviatura | Extenso | Uso |
|---|---|---|
| Sr. | Senhor | Formal |
| Sra. | Senhora | Formal |
| Sr.ª | Senhora | Formal (alternativa) |
| Dr. | Doutor | Profissional (medicos, advogados, academicos) |
| Dra. | Doutora | Profissional feminino |
| Prof. | Professor | Academico |
| Prof.ª | Professora | Academico feminino |
| Eng.º | Engenheiro | Profissional |
| Arq.º | Arquiteto | Profissional |

**PT-PT:** Doutor/Doutora e usado como tratamento generalizado para pessoas com curso superior, nao apenas pos-graduacao.

---

## 10. Artefatos de OCR (Optical Character Recognition)

### 10.1 Identificacao de Artefatos

Ao processar documentos digitalizados por OCR, os seguintes artefatos sao comuns:

| Artefato | Causa | Exemplo |
|---|---|---|
| Caracteres trocados | Fonte danificada | "cliente" viram "cliente" |
| Letras com acento perdidas | OCR nao detecta acentos | "cafe" em vez de "café" |
| Quebras de linha incorretas | Layout complexo | Palavras partidas no meio |
| Espacos duplicados | Ruido na imagem | "palavra  palavra" |
| Letras maiusculas/minusculas erradas | Fonte ilegivel | "RUA" em vez de "Rua" |
| Numeros confundidos | Fonte similar | "0" vs "O", "1" vs "l" |
| Pontuacao faltando | Imagem de baixa qualidade | Virgulas e pontos ausentes |
| Caracteres especiais errados | Codificacao | "ç" vira "c" ou "¢" |

### 10.2 Marcacao de Restauracao

Quando uma palavra ou trecho e corrigido manualmente apos OCR, usar o formato:

```
[restaurado: texto corrigido]
```

**Exemplos:**
- "O [restaurado: café] estava quente." (acento adicionado)
- "O valor era de [restaurado: R$ 1.500,00]." (numero corrigido)
- "A [restaurado: assembleia] foi convocada." (palavra corrigida conforme AO 1990)
- "O [restaurado: Instituto] Brasileiro de Geografia e Estatistica" (maiuscula corrigida)

**Regras de uso do marcador [restaurado:]:**

| Situacao | Marcar? | Exemplo |
|---|---|---|
| Acento faltante corrigido | Sim | [restaurado: café] |
| OCR trocou letra | Sim | [restaurado: cliente] |
| Palavra inteira ilegivel | Sim | [restaurado: previsão] |
| Espaco duplicado removido | Nao | — |
| Maiuscula corrigida | Sim, se duvidosa | [restaurado: Rua] |
| Pontuacao adicionada | Nao | — |
| Numeros corrigidos | Sim | [restaurado: R$ 1.500,00] |
| Palavra visivel mas duvidosa | Sim | [restaurado: provavelmente] |
| Palavra claramente legível | Nao | — |

### 10.3 Tratamento de Palavras com OCR Incerto

Niveis de confianca e tratamento:

| Confianca | Acao | Marcacao |
|---|---|---|
| Alta (>95%) | Nenhuma correcao | Sem marcacao |
| Media (80-95%) | Corrigir se necessario | [restaurado: texto] |
| Baixa (50-80%) | Corrigir e marcar | [restaurado: texto] |
| Muito baixa (<50%) | Marcar como ilegivel | [restaurado: ilegível] |

### 10.4 Padronizacao Pos-OCR

Apos a extracao por OCR, aplicar as seguintes correcoes de forma padronizada (sem necessidade de marcar cada uma):

1. Substituir "0" (zero) por "O" quando claramente for letra em nomes proprios
2. Substituir "1" (um) por "l" ou "I" quando apropriado
3. Remover espacos duplicados
4. Corrigir quebras de linha em meio a palavras (unir as partes)
5. Normalizar aspas para o padrao escolhido (secao 6.1)
6. Normalizar travessoes para o padrao escolhido (secao 6.2)
7. Corrigir acentuacao basica obvia

### 10.5 Documentos de Baixa Qualidade

Para documentos onde o OCR produziu resultado insatisfatorio:
- Priorizar a compreensao geral do texto sobre a fidelidade a cada caractere
- Usar [restaurado: ...] generosamente para alteracoes especulativas
- Se uma palavra nao pode ser restaurada com confianca minima, usar [restaurado: ilegível]
- Nao inventar numeros; se um valor numerico nao pode ser lido, marcar como [restaurado: valor ilegível]

---

## 11. Filosofia de Traducao

### 11.1 Principios Gerais

A traducao para o portugues deve priorizar:

1. **Naturalidade**: O texto traduzido deve soar como se tivesse sido originalmente escrito em portugues
2. **Fidelidade semantica**: Preservar o significado original, nao necessariamente a estrutura
3. **Consciencia regional**: Saber se o publico-alvo e PT-BR ou PT-PT e aplicar as convencoes correspondentes
4. **Consistencia**: Manter as mesmas escolhas tradutorias ao longo de todo o documento
5. **Clareza**: Quando houver conflito entre naturalidade e fidelidade literal, priorizar a compreensao

### 11.2 PT-BR vs. PT-PT: Consciencia Regional

Ao traduzir, considerar:

| Aspecto | PT-BR | PT-PT |
|---|---|---|
| Publico | Brasileiro | Portugues, PALOP, Timor-Leste |
| Vocabulario | "onibus", "trem", "abertura de fabrica" | "autocarro", "comboio", "abertura de fabrica" |
| Gramatica | Gerundio, proclise | "Estar a + infinitivo", enclise |
| Ortografia | Acordo Ortografico 1990 | Acordo Ortografico 1990 |
| Formalidade | "Voce" padrao semiformal | "Voce" semiformal, "tu" informal |
| Pontuacao | Aspas duplas | Aspas angulares preferidas |
| Medidas | Sistema metrico (padrao) | Sistema metrico (padrao) |

**Se o publico-alvo nao for especificado:**
- Manter consistencia com o tipo de documento
- Documentos juridicos: PT-PT tem tradicao juridica propria; preferir PT-BR ou PT-PT conforme o jurisdicao
- Documentos tecnicos: ambos sao similares; escolher pela maioria do publico
- Documentos literarios: PT-PT e PT-BR diferem significativamente; exigem traducao separada

### 11.3 Equivalencias Lexicais Comuns (PT-BR ↔ PT-PT)

| Ingles | PT-BR | PT-PT |
|---|---|---|
| Bus | onibus | autocarro |
| Train | trem | comboio |
| Cell phone | celular | telemovel |
| Computer | computador | computador |
| Mouse (computing) | mouse | rato |
| Keyboard | teclado | teclado |
| Screen | tela | ecra |
| Download | download (masculino) | descarregamento / download |
| Ice cream | sorvete | gelado |
| Juice | suco | sumo |
| Breakfast | cafe da manha | pequeno-almoco |
| Lunch | almoco | almoco |
| Dinner | jantar | jantar |
| Snack | lanche | lanche |
| Bathroom | banheiro | casa de banho |
| Driver's license | carteira de motorista | carta de conducao |
| ID card | RG / identidade | bilhete de identidade / CC |
| Line | fila | fila / bicha |
| Team | equipe / time | equipe |
| Meeting | reuniao | reuniao |
| Office | escritorio | escritorio |
| Floor (story) | andar | andar |
| Apartment | apartamento | apartamento |
| Elevator | elevador | elevador |

### 11.4 Estrangeirismos e Adaptacoes

| Principio | Exemplo |
|---|---|
| Preferir aportuguesamento quando consagrado | "estresse" (nao "stress") |
| Manter estrangeirismo quando nao ha equivalente | "software", "design" |
| Manter estrangeirismo quando e jargao tecnico | "compliance", "feedback" |
| PT-BR: maior tolerancia a anglicismos | "mouse", "download", "link" |
| PT-PT: maior resistencia a anglicismos | "rato", "descarregamento", "hiperligacao" |
| Traduzir quando ha equivalente claro | "data-driven" = "baseado em dados" |
| Em duvida, usar o termo mais amplamente compreendido | |

### 11.5 Expressoes Idiomaticas

- Traduzir o sentido, nao as palavras: "It's raining cats and dogs" → "Esta chovendo canivetes" (BR) / "Esta a chover a potes" (PT)
- Buscar equivalencia funcional: encontrar expressao em portugues que transmita o mesmo efeito
- Quando nao houver equivalente, traduzir literalmente e adicionar explicacao breve se necessario
- Evitar traduzir literalmente expressoes que perdem o sentido em portugues

### 11.6 Humor e Trocadilhos

- Priorizar o efeito comico sobre a fidelidade literal
- Se o trocadilho nao funciona em portugues, substituir por trocadilho equivalente ou compensar de outra forma
- Se nao e possivel preservar o humor, traduzir o significado e indicar "[trocadilho intraduzivel]" entre colchetes
- Nunca forcar um trocadilho em portugues que nao exista no original

### 11.7 Tom e Estilo

- Identificar o tom do original (formal, neutro, informal, humoristico, tecnico) e reproduzi-lo em portugues
- Manter o nivel de formalidade consistente (nao misturar "você" com "o senhor" no mesmo texto)
- Textos juridicos: tom formal, vocabulario preciso, construcoes complexas
- Textos de marketing: tom persuasivo, adaptado ao publico-alvo
- Textos tecnicos: tom neutro, terminologia precisa, frases claras
- Textos literarios: estilo elegante, respeitando a voz do autor

### 11.8 Revisao e Controle de Qualidade

Antes de finalizar uma traducao para o portugues, verificar:
1. Acentuacao: todas as palavras estao corretamente acentuadas?
2. Pontuacao: virgulas, travessoes e aspas seguem as convencoes?
3. Numeros: formato decimal e de milhares correto?
4. Datas: formato DD/MM/AAAA?
5. Terminologia: consistente ao longo de todo o documento?
6. Regional: PT-BR ou PT-PT aplicado consistentemente?
7. Gramatica: concordancia, regencia e colocacao pronominal corretas?
8. OCR: todas as correcoes de OCR estao marcadas com [restaurado:]?

### 11.9 Glossario Vivo

Manter um glossario vivo de termos e decisoas de traducao, documentando:
- Termo original
- Traducao escolhida
- Variante regional (se relevante)
- Contexto
- Data da decisao
- Justificativa

---

*Documento gerado em maio de 2026. As regras seguem o Acordo Ortografico de 1990, adotado tanto no Brasil quanto em Portugal.*
