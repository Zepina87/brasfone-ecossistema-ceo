# Qualidade

Um agente produz texto plausível por construção. Plausível não é verdadeiro, e a diferença só se
nota quando alguém do outro lado verifica. Os gates existem para verificar antes desse alguém.

## Os quatro

| Gate | Pergunta | Corre antes de |
|---|---|---|
| `/fact-check` | Isto é verdade, e como é que eu sei? | Tudo o que sai com números ou nomes |
| `/ghost-check` | Isto soa a máquina? | Tudo o que se lê como texto teu |
| `/taste` | Isto parece feito por alguém com opinião? | Tudo o que se vê |
| `/deep-research` | Estou a afirmar sem ter verificado? | Antes de escrever, não depois |

## A regra estrutural

**Quem escreve não avalia.** Se o mesmo agente gera e aprova, aprova sempre. O gate tem de correr
como passo separado, e é isso que o torna útil, não a lista de padrões que ele conhece.

Nas orquestrações: o passo de revisão vai a um agente diferente do que produziu.

## Números

Três origens legítimas, e o documento deixa ver qual:

1. **Dado teu**, com a referência: "segundo o relatório de Junho"
2. **Cálculo à vista** no próprio documento: "12 pessoas × 3 horas = 36 horas"
3. **Fonte citada**

Não há quarta. "É o que costuma acontecer" é uma intuição, e escreve se como tal ou não se escreve.

O cálculo à vista é melhor do que um número redondo, e não é só por honestidade: deixa quem lê
discutir a premissa em vez de acreditar ou não acreditar. Um número sozinho só admite fé ou dúvida.

## Zero invenção

A regra que está acima de todas: **sem fonte, dizer que não se sabe.**

Custa uma resposta. Poupa te a situação em que alguém age sobre uma informação que o agente
construiu por verosimilhança. E essa situação, quando acontece, não custa uma resposta: custa a
confiança em todas as outras.

O sinal de que um agente está a inventar não é o erro grosseiro. É a resposta que está sempre
completa, sempre confiante, sempre com o número certo de casas decimais.
