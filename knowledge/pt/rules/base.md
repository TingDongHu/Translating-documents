---
id: pt/rules/base
type: rules
target_lang: pt
name: Portuguese (Brazilian) Translation Rules
description: Base rules for translating documents into Brazilian Portuguese
---

## Formato numérico

### Números
- Separador decimal: vírgula (,)
- Separador de milhar: ponto (.)
- Exemplo: 1.234,56 (mil duzentos e trinta e quatro vírgula cinquenta e seis)
- Espaço antes de unidades: 100 km, 50 kg

### Porcentagens
- Com espaço antes do símbolo: 15,5 %
- Ou colado: 15,5% (ambas as formas são aceitáveis)

### Moeda
- Real brasileiro: R$ 1.000,00 (prefixo R$)
- Euro: 1.000,00 € (símbolo depois)
- Dólar: US$ 1.000,00 (prefixo US$)
- Espaço entre o símbolo e o valor: R$ 100,00

## Formato de datas

### Data completa
- 18 de maio de 2026
- dia 18 de maio de 2026

### Data curta
- 18/05/2026 (DD/MM/AAAA)
- 18.05.2026 (formato alternativo)

### Horário
- 14h30 / 14:30
- 14 horas e 30 minutos

## Pontuação

### Aspas
- Aspas principais: "..." (aspas retas) ou «...» (aspas angulares)
- Aspas simples: '...' (para citação dentro de citação)
- No Brasil, aspas retas são mais comuns; as angulares são mais formais

### Vírgula
- Vírgula antes de "que": «Ele disse que viria.» (sem vírgula antes de "que" em orações substantivas)
- Vírgula antes de "mas", "porém", "entretanto", "contudo": «Estudou, mas não passou.»
- Vírgula para separar orações coordenadas: «Ele chegou, sentou e começou a falar.»

### Ponto e vírgula
- Separar itens complexos em enumerações
- Separar orações coordenadas longas

### Dois-pontos
- Antes de citações diretas
- Antes de enumerações
- Antes de explicações

## Regras gramaticais

### Concorrência de gênero
- Usar o masculino como forma padrão quando o gênero é desconhecido ou misto
- Alternativas inclusivas: «prezados(as)», «cidadãos(ãs)»
- Evitar arroba (@) ou "x" em documentos formais

### Concorrência de número
- Adjetivos e particípios concordam com o substantivo
- «Os documentos anexados» (não «anexado»)
- «As informações fornecidas» (não «fornecida»)

### Tempos verbais
- Presente do indicativo para fatos atuais
- Pretérito perfeito para ações concluídas
- Futuro do presente para compromissos: «Entregaremos amanhã.»
- Modo subjuntivo para incerteza: «Caso necessário, entre em contato.»

### Pronomes de tratamento
- «Você» — informal, amplamente usado no Brasil
- «O senhor / A senhora» — formal
- «Vossa Excelência» — para autoridades (presidente, governador, juiz)
- «Vossa Senhoria» — para autoridades menores (diretores, gerentes)
- Em documentos formais, usar «o senhor / a senhora» ou «você» (dependendo do contexto)

## Estilo

### Clareza e concisão
- Frases curtas e diretas
- Evitar períodos longos (máximo 25 palavras por frase)
- Usar voz ativa quando possível
- Evitar nominalizações desnecessárias

### Formalidade
- Documentos jurídicos: linguagem formal, técnica
- Documentos comerciais: registro profissional, cortês
- Documentos administrativos: estilo impessoal, objetivo
- Documentos técnicos: precisão terminológica

### Paralelismo
- Manter estrutura paralela em listas e enumerações
- «A empresa deve: (a) apresentar o relatório; (b) assinar o contrato; (c) efetuar o pagamento.»

## OCR e inferência

### Marcadores de incerteza
- Texto claro: transcrever normalmente
- Texto parcialmente legível: `[inferido: texto]`
- Texto ilegível: `[ilegível]`
- Texto ausente (espaço em branco): `[espaço em branco]`
- Dados numéricos incertos: `[número inferido: 123]`

### Validação
- Verificar consistência de números e datas
- Confirmar nomes próprios com contexto
- Validar fórmulas e cálculos

## Tradução criativa

### Trocadilhos e jogos de palavras
- Preferir o sentido ao pé da letra
- Buscar equivalente criativo em português
- Se não houver equivalente: traduzir o sentido + anotar `[NT: jogo de palavras no original]`

### Slogans e frases de efeito
- Adaptar para o mercado brasileiro
- Manter o impacto e a memorabilidade
- Exemplo: «Think Different» → «Pense diferente» (Apple Brasil)

### Marcas e produtos
- Conter nomes de marcas sem tradução
- Traduzir nomes descritivos se necessário
- Verificar se a marca já tem versão em português

## Qualidade de fonte

### Fonte de baixa qualidade
- Aumentar tolerância para erros de OCR
- Anotar incertezas com `[inferido: ...]`
- Validar números e datas com cuidado extra
- Preferir tradução literal quando a precisão é duvidosa

### Fonte manuscrita
- Transcrever com máxima cautela
- Anotar ilegibilidades: `[ilegível]`
- Inferir pelo contexto quando possível
- Nunca inventar conteúdo

## Variantes do português

### Português brasileiro vs. europeu
- Este guia foca no português brasileiro (pt-BR)
- Diferenças principais:
  - Pronomes: «você» (BR) vs. «tu» (PT)
  - Gerúndio: «Estou fazendo» (BR) vs. «Estou a fazer» (PT)
  - Vocabulário: «ônibus» (BR) vs. «autocarro» (PT)
  - «Celular» (BR) vs. «Telemóvel» (PT)
- Se o documento for para Portugal, adaptar a variante
