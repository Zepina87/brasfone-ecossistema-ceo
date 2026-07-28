---
name: ghost-check
description: Validação anti-IA de qualquer texto antes de sair. Audita texto PT-PT contra 40+ padrões de AI-slop — palavras proibidas, frases-template, formatação suspeita, ritmo uniforme. Reescreve para soar humano, Brasfone, José Pina. Usar antes de publicar posts LinkedIn, enviar cold mail, ou entregar qualquer output textual público.
---

# /ghost-check — Anti-IA Gate Brasfone

Última linha de defesa antes de qualquer texto sair da Brasfone. Baseado em `conorbronsdon/avoid-ai-writing` v3.3.1 + adaptação PT-PT + voz José Pina.

**Trigger:** `/ghost-check [texto]` ou "passa isto pelo ghost-check" ou "ghost this"

## Dois modos

### MODO 1 — REWRITE (padrão)
Detecta todos os AI-isms → reescreve em PT-PT humano Brasfone → mostra mudanças principais → **loop de self-critique**.

**Loop de self-critique (critério de paragem explícito):**
Após a 1ª reescrita, re-auditar o próprio output contra a `red-list.md`. Repetir reescrita+auditoria **até 0 flags P0/P1 OU 3 iterações** (o que vier primeiro). Parar sempre em 3 para não polir a voz até desaparecer. Reportar em que iteração fechou.
- Iteração 1: reescrita base
- Iteração 2+: só se restarem P0 (credibility killers) ou P1 (AI smell óbvio); P2 (polish) não obriga a nova volta
- Se aos 3 loops ainda houver P0 → assinalar "⚠️ residual persistente — revisão humana" em vez de forçar

### MODO 2 — DETECT (auditoria)
Só flagueia, não reescreve. Útil quando o texto já foi revisto mas queres sanity check.
Trigger: `/ghost-check detect [texto]`

---

## O que é AI-slop (a eliminar)

> **Todos os padrões a apanhar vivem na fonte única: `red-list.md`** (mesma pasta).
> Carregar `red-list.md` antes de auditar. Nunca copiar as listas para aqui — elas mudam só lá.

A red-list cobre 10 blocos:
1. **Tier 1** (SEMPRE substituir) — delve, alavancar, robusto, tapestry, seamless...
2. **Tier 2** (flag quando 2+ no parágrafo) — crucial, pivotal, transformador...
3. **Tier 3** (flag por densidade) — eficaz, importante, poderoso...
4. **Frases-template** — "It's not X, it's Y", "Não se trata apenas de..."
5. **Frases-assistente/chatbot** — "Espero que ajude", "Aqui está a questão", "A maioria das pessoas..."
6. **Formatação** — travessões, bold em massa, emoji, headers em post curto
7. **Hedging & hollow intensifiers** — "pode potencialmente", "verdadeiramente transformador"
8. **Advérbios-tique** — "X silenciosamente faz Y" → cortar advérbio ou trocar verbo
9. **Padrões estruturais** (SINAL #1) — ritmo uniforme, perguntas retóricas em sequência
10. **PT-slop específico** — "incrível" repetido, CTA genérica, "Estamos aqui para te ajudar"

Rigor por bloco: 1/4/5 = corte duro sempre. 2/3 = por densidade. 6-9 = julgamento (irregularidade humana é voz, não erro).

---

## Output do modo REWRITE

```
🔍 GHOST-CHECK — [N] padrões detectados

📋 ORIGINAL:
[texto tal como recebido]

✂️ PROBLEMAS ENCONTRADOS:
- [Tier 1] "alavancar" × 2 → substituir
- [Formatação] 4 travessões longos em 200 palavras → cortar 2
- [Estrutura] 3 parágrafos de ~30 palavras cada → variar
- [Template] "Não se trata apenas de..." → reescrever

✅ VERSÃO REESCRITA:
[texto limpo]

🔁 SEGUNDA PASSAGEM:
- [nada a reportar] OU
- [residuais encontrados + fix final]

📊 SUMÁRIO:
Patterns removidos: X
Palavras originais: Y → Z (diferença %)
Sound check: ✅ Soa humano / ⚠️ Ainda residuais
```

## Output do modo DETECT

```
🔍 GHOST-CHECK DETECT — [N] flags

🔴 P0 CREDIBILITY KILLERS:
- [pattern + linha + sugestão]

🟠 P1 OBVIOUS AI SMELL:
- [pattern + linha]

🟡 P2 POLISH:
- [pattern + linha]

Assessment: [Publicável / Revisão necessária / Reescrita necessária]
```

---

## Perfis de contexto

Ajustar rigor conforme o tipo de texto:

| Contexto | Rigor | Foco |
|---|---|---|
| Post LinkedIn Sombra | 🔴 Máximo | Voz José, variação de ritmo, zero slop |
| Cold mail | 🔴 Máximo | Curto, específico, zero template phrases |
| Blog técnico | 🟠 Alto | Permite alguns termos técnicos |
| Email interno | 🟡 Médio | Funcional |
| Documentação técnica | 🟢 Baixo | Tolerar jargão necessário |
| Proposta comercial | 🔴 Máximo | Credibilidade crítica |

## Onde encaixar

- **Antes de qualquer publicação** com o teu nome em cima
- **Em cada variante** de um texto que vai para fora, não só na primeira
- **Nos textos que um agente escreveu por ti**, sobretudo quando ficaram bons à primeira
- **Emparelhado com `/fact-check`:** este trata do estilo, o outro trata da verdade. Correr os dois

Regra de desenho: quem escreve não deve ser quem avalia. Se o mesmo agente gera e aprova, aprova
sempre. Correr o gate em passo separado é o que o torna útil.

## Princípio de ouro

> Escrita que soa a **pessoa** — directa, específica. A escrita deve **demonstrar** confiança, não **afirmar** confiança.
>
> Irregularidades humanas são **voz**, não erros. Não as polir até desaparecerem.

## Fonte & cross-refs
- Base: `conorbronsdon/avoid-ai-writing` (MIT) — https://github.com/conorbronsdon/avoid-ai-writing
- Complementa: Claude Secret Code `/ghost` (comando inline rápido)
- Alinhado com: `reference_claude-cowork-7-steps.md` (metodologia ABOUT ME)
