---
name: fact-check
description: Portão de verdade factual antes de qualquer coisa sair para fora. Extrai todas as afirmações verificáveis do texto (números, percentagens, nomes de clientes e parceiros, capacidades técnicas, resultados prometidos) e classifica cada uma como confirmada, a validar, ou sem fonte e portanto a cortar. Usar antes de enviar propostas, publicar, apresentar a um board, ou entregar qualquer documento com números. Complementa o ghost-check, que trata do estilo. Este trata da verdade.
---

# Fact check

O ghost check pergunta "isto soa a máquina?". Este pergunta uma coisa diferente e mais séria:
**"isto é verdade, e como é que eu sei?"**

Um documento de CEO com um número inventado não perde só esse número. Perde a credibilidade de
todos os outros números do documento, e a de quem o assinou. É um custo assimétrico: a afirmação
verosímil não te dá quase nada, e o erro tira te muito.

---

## Quando correr

Sempre que o texto vai sair do teu ecrã. Proposta, email a um cliente, publicação, deck de board,
relatório à administração, mensagem a um parceiro.

Não é preciso em notas para ti, rascunhos, ou perguntas de trabalho.

---

## Como corre

### Passo 1, extrair as afirmações verificáveis

Percorrer o texto e listar **tudo** o que pode ser verdadeiro ou falso. Cinco categorias:

| Categoria | Exemplos |
|---|---|
| **Números** | valores, percentagens, contagens, prazos, poupanças, crescimentos |
| **Nomes** | clientes, parceiros, fornecedores, pessoas, concorrentes |
| **Capacidades** | "integramos com X", "temos Y", "conseguimos fazer Z" |
| **Relações** | "somos parceiros de", "trabalhamos com", "implementámos em" |
| **Resultados** | "reduziu em", "aumentou", "poupou", "converteu" |

Opiniões e recomendações não entram. "Acho que devemos avançar" não é verificável e não precisa de
fonte. "Isto poupa 40 horas por mês" precisa.

### Passo 2, classificar cada uma

Três resultados possíveis, e só três:

| Classificação | Critério | O que fazer |
|---|---|---|
| ✅ **Confirmada** | Tem fonte: um dado teu, um cálculo visível no próprio documento, ou um ficheiro que se pode citar | Fica, e a fonte fica identificável |
| ⚠️ **A validar** | É provavelmente verdade mas ninguém verificou | Fica marcada "a confirmar", ou sai. Nunca fica como se fosse certa |
| ❌ **Sem fonte** | Não se consegue mostrar de onde vem | **Corta.** Sem discussão e sem excepção |

A tentação é passar as ⚠️ a ✅ porque "é obviamente verdade". É exactamente aí que os erros entram.
Se é obviamente verdade, mostrar a fonte custa dez segundos.

### Passo 3, os três testes que apanham a maior parte

**O teste do número redondo.** Qualquer número que acabe em zero ou em cinco e que não tenha um
cálculo ao lado é suspeito. Números reais são feios. "Poupa 40 horas por mês" quase sempre nasceu de
uma sensação, não de uma conta.

**O teste do nome.** Cada nome de cliente ou parceiro tem de estar na tabela de prova social
confirmada, abaixo. Não estar na tabela não significa que não exista. Significa que não sai hoje.

**O teste da capacidade.** "Integramos com X" é a afirmação mais perigosa de todas, porque a primeira
coisa que a pessoa do outro lado faz é perguntar como. A pergunta a fazer é: existe, hoje, a
funcionar, em produção, em alguém? Se a resposta tem um "estamos a" ou um "falta acertar", a
afirmação é falsa e tem de mudar de forma.

### Passo 4, o relatório

```
FACT CHECK: [nome do documento]

✅ CONFIRMADAS (n)
   · [afirmação] → fonte: [onde]

⚠️ A VALIDAR (n)
   · [afirmação] → falta: [o que é preciso para confirmar] → texto alternativo seguro: [...]

❌ A CORTAR (n)
   · [afirmação] → razão: [porquê] → substituir por: [o que dizer em vez disso]

VEREDICTO: pode sair / pode sair com as correcções / não pode sair
```

O veredicto é uma das três coisas. "Pode sair com reservas" não é um veredicto, é uma forma de não
decidir.

---

## A tua tabela de prova social

*Preenche isto. É a lista fechada dos nomes que podem sair num documento, e é a razão pela qual este
gate funciona. Sem a tabela, o gate é uma opinião.*

*A distinção entre cliente e parceiro é a que causa mais estragos quando se erra: chamar cliente a
um parceiro é uma afirmação falsa sobre a relação, e a pessoa em causa costuma descobrir.*

| Nome | Relação exacta | Pode sair? | Formulação obrigatória | O que nunca dizer |
|---|---|---|---|---|
| `[A PREENCHER]` | cliente / parceiro / fornecedor | ✅ ou ⬜ | `[a frase exacta que se usa]` | `[a formulação errada]` |

### Sector a sector

*Quando precisas de um exemplo de um sector, qual é o que podes nomear e qual é o que existe mas não
podes nomear.*

| Sector | Nome que posso usar | Existe mas não posso nomear |
|---|---|---|
| `[A PREENCHER]` | `[A PREENCHER]` | `[A PREENCHER]` |

### Nomes proibidos

*Nomes que apareceram em documentos, que soam certos, e que estão errados. Cada linha aqui nasceu de
um erro real, e é a secção mais útil da tabela ao fim de um ano.*

| Nome errado | Porquê | O correcto |
|---|---|---|
| `[A PREENCHER]` | `[A PREENCHER]` | `[A PREENCHER]` |

---

## Números, as três origens legítimas

Um número num documento que sai tem de vir de uma destas três, e o documento tem de deixar ver qual:

1. **Dado teu.** Do sistema, do relatório, da folha. Diz se de onde: "segundo o relatório de Junho".
2. **Cálculo à vista.** A conta aparece no documento: "12 pessoas × 3 horas por semana = 36 horas".
   Isto é melhor do que um número redondo, porque quem lê pode discutir a premissa em vez de
   acreditar ou não acreditar.
3. **Fonte citada.** Um estudo, um relatório público, um documento interno, com referência.

Não há uma quarta. "É o que costuma acontecer" não é uma origem, é uma intuição, e escreve se como
tal ou não se escreve.

---

## Regra final

Este gate tem autoridade para travar. Se o veredicto for "não pode sair", não sai, mesmo com pressa,
mesmo que a reunião seja daqui a dez minutos. A pressa é precisamente a condição em que os números
inventados entram nos documentos.

Quem assina és tu. O gate existe para que o que assinas seja defensável quando alguém perguntar
"de onde é que vem este número?", que é uma pergunta que alguém acaba sempre por fazer.
