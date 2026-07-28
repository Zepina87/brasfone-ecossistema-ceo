# Custo e modelos

## Três níveis

| Nível | Exemplo | Modelo |
|---|---|---|
| **Mecânico** | Procurar, formatar, extrair, verificar duplicados, converter | O mais rápido e barato |
| **Normal** | Analisar, escrever, pontuar, sintetizar | O da sessão |
| **Crítico** | Decisão difícil de reverter, output para fora, auditoria, gate | O melhor. Nunca baixar |

Classificar antes de delegar. Subir de nível exige uma linha de justificação, e baixar num passo
crítico não é uma opção mesmo quando a conta está alta.

## Onde o custo realmente está

A escolha do modelo é a decisão menos importante das três. Estas duas valem mais:

**Contexto.** Carregar ficheiros inteiros quando uma busca resolve é o desperdício mais comum e o
mais invisível. Máximo de três ficheiros de método por tarefa; precisar de mais exige justificar.

**Repetição.** Uma chamada por item dentro de um ciclo, quando existe forma de fazer em lote, custa
dez vezes mais e é dez vezes mais lento. Agregar as escritas no fim do passo.

Um agente que carrega tudo "para ter contexto" é mais caro **e** dá piores respostas, porque o que
importa fica diluído no que não importa. Não há troca aqui: menos contexto relevante é melhor em
ambas as dimensões.

## Compactar em bom sítio

Uma conversa longa acaba por ser resumida automaticamente, e o resumo automático corta onde calhar,
o que às vezes é no meio de um raciocínio.

Compactar de propósito numa fronteira de tarefa, quando acabaste uma coisa e vais começar outra, é
melhor. A skill `/strategic-compact` explica quando, e o `/context-budget` mostra onde está o
desperdício na sessão.

## O que não vale a pena optimizar

O custo de um agente bem desenhado é ordens de magnitude menor do que o custo de uma hora tua.
Optimizar tokens num agente que te poupa duas horas por semana é optimizar a coisa errada.

Vale a pena optimizar dois casos: o que corre **automaticamente**, muitas vezes, sem ninguém a
olhar; e o que corre **em massa** sobre muitos itens. Fora disso, escolhe pela qualidade da resposta.
