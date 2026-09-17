# ECOSYSTEM, o registo vivo

Este ficheiro é a lista do que existe. O Cérebro lê-o antes de forjar qualquer coisa, para não
criar um agente que já existe.

**Ele começa quase vazio de propósito.** No dia um tens um agente: o Cérebro. Os outros nascem na
Oficina, quando o uso os pedir. Se ao fim de um mês este ficheiro tiver quatro linhas escritas por
ti, a entrega funcionou. Se tiver zero, algo está errado e quero saber o quê.

---

## Agentes activos

| Agente | Comando | Missão numa linha | SPAR | Criado por | Data |
|---|---|---|---|---|---|
| O Cérebro | `/cerebro` | Orquestrador principal: responde do método, forja agentes, afina os que existem, calibra o ambiente | 33/35 | José Pina | 2026-07-28 |
| O Eco | `/eco` | GEO: mede e melhora a visibilidade da marca nas respostas de IA (ChatGPT, Perplexity, Gemini, Claude) | por pontuar | José Pina | 2026-09-17 |

---

## Gates de qualidade

Não são agentes. São filtros que correm por cima do que sai.

| Gate | Comando | Apanha |
|---|---|---|
| Fact check | `/fact-check` | Números sem fonte, nomes não confirmados, capacidades que não temos |
| Ghost check | `/ghost-check` | Texto que soa a máquina |
| Taste | `/taste` | Qualidade visual genérica |
| Deep research | `/deep-research` | Afirmar sobre o mundo sem verificar |

---

## Fichas de desenho, à espera da Oficina

Estes três não são agentes. São **desenhos**, com o problema, os modos propostos e as decisões
difíceis já mapeadas. Não os instalei porque um agente que eu adivinhei é um agente que usas duas
vezes e abandonas.

Quando um deles te fizer falta a sério, abres a ficha, dizes ao Cérebro `oficina, forja o Painel`,
e ele constrói-o contigo, entrevista incluída. O que sair vai ser diferente da ficha, e é esse o
objectivo: a ficha é o ponto de partida informado, não o produto.

| Ficha | O problema que resolve | Estado |
|---|---|---|
| [O Painel](../fichas/o-painel.md) | Os números das frentes do grupo num sítio, sem pedir a ninguém | ⬜ não forjado |
| [O Cronista](../fichas/o-cronista.md) | Reunião para decisões, o que prometi, o que me prometeram, riscos | ⬜ não forjado |
| [Design Pro](../fichas/design-pro.md) | Decks de board, dashboards e one pagers sem depender de designer | ⬜ não forjado |

O catálogo dos 25 agentes que já correm na Brasfone está em
[fichas/OS-25-DA-BRASFONE.md](../fichas/OS-25-DA-BRASFONE.md). Uma linha por agente. Serve para
roubar ideias, não para instalar.

---

## Como registar um agente novo

A Oficina faz isto por ti, no passo 5. Se escreveres à mão, o formato é o da tabela de cima, e as
três colunas que as pessoas se esquecem de preencher são as que interessam ao fim de seis meses:
**SPAR** (para saberes se ele foi auditado), **criado por** (para saberes a quem perguntar) e
**data** (para saberes se ainda faz sentido).

Regra: um agente sem SPAR pontuado não entra nesta tabela. Fica em rascunho até ser pontuado.
