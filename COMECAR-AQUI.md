# Começar aqui

Uma página. Três marcos. O dia 30 é o critério pelo qual esta entrega deve ser julgada.

---

## Dia 1, cerca de uma hora

**Objectivo: sair com um resultado útil, não com um ambiente configurado.**

1. Passos 1 a 4 do [README](README.md). Instalar, preencher quem tu és, instalar os comandos.
2. `/cerebro` e uma **pergunta real de trabalho**. Não um teste.
3. Repara na linha `🧭 ROTA:` que ele escreve antes de responder. Se escolheu o modo errado, diz lhe.

Se ao fim da hora tiveres uma resposta que ias pedir a alguém, o dia 1 correu bem.

---

## Dia 7, tornar teu

**Objectivo: sair da minha estrutura e entrar na tua.**

1. **Lê as três fichas** em `fichas/`. Cinco minutos cada. Se um dos problemas não é teu, ignora a.
2. **Forja o primeiro.** O que te fizer mais falta:

   ```
   /cerebro
   > oficina, forja o Painel
   ```

   Ele entrevista te em cinco perguntas, verifica se algo que já tens cobre aquilo, escreve o,
   pontua o com SPAR, instala o, testa com um caso real, e no fim explica te três decisões de
   desenho que tomou e uma que rejeitou.

3. **Repara na pergunta que ele te faz sobre a falha.** *"Como é que tu sabes que ele falhou?"* É a
   pergunta que ninguém faz e é a que separa um agente que melhora de um que estagna.

4. **Calibra o ambiente.** Quando algo te irritar, `/cerebro` e "calibra: ele faz sempre X e eu
   quero Y". Na maior parte dos casos o problema não está no agente, está no `CLAUDE.md`.

---

## Dia 30, o critério

Três coisas devem ser verdade. Se não forem, a entrega falhou e quero saber.

| Critério | Como verificas |
|---|---|
| **Existe pelo menos um agente que eu não escrevi** | `cerebro/ECOSYSTEM.md` tem uma linha com o teu nome na coluna "criado por" |
| **Deixaste de pedir a alguém coisas que já tens** | Conta as vezes que pediste um número este mês |
| **A memória tem coisas tuas** | `core.md` e `prefs.md` têm regras que nasceram de correcções, não do template |

O primeiro é o que importa mais. Se ao fim de um mês a pasta `agentes/` estiver vazia, ou o método
está mal explicado, ou eu escolhi as fichas erradas. Nos dois casos é comigo.

---

## Os comandos que vais usar

| Comando | Para quê |
|---|---|
| `/cerebro` | O ponto de entrada. Pede em português, ele despacha e diz o que escolheu |
| `/fact-check` | Antes de sair algo com números ou nomes |
| `/ghost-check` | Antes de sair algo que se lê como texto teu |
| `/impeccable` `/taste` | Quando algo se vê e tem de estar bem |
| `/grill-me` | Antes de construir algo grande. Ele interroga te as assunções |
| `/dream` `/learn` | Memória: consolidar, e extrair o padrão do que resolveste |

O índice completo dos dezassete está em [skills/README.md](skills/README.md).

---

## Duas coisas antes de começar

**O que corre sozinho e o que pára** está em
[metodo/04-AUTONOMIA-E-RARV.md](metodo/04-AUTONOMIA-E-RARV.md). Resumo: o que é reversível corre, o
que se vê de fora pára e espera pela tua palavra. O critério é a reversibilidade, não a importância.

**Antes de instalares qualquer coisa que encontres na internet**, lê
[seguranca/02-REPOS-EXTERNOS.md](seguranca/02-REPOS-EXTERNOS.md). São oito minutos e é o único
documento aqui que descreve um ataque que funciona contra ti mesmo que faças tudo o resto bem.
