---
name: loop-engineering
description: Skill de Loop Engineering (prática Anthropic 2026) — desenhar o loop iterativo que corre um agente autonomamente em vez de o promptar passo a passo. Usar em orquestrações de vários passos, runs longos que atravessam sessões, e agentes que correm sem ninguém à frente.
---

# Loop Engineering — a prática Anthropic
**Fontes oficiais:** Anthropic Engineering — "Building agents with the Claude Agent SDK" + "Effective harnesses for long-running agents" + "Effective context engineering for AI agents". Termo "loop engineering" cunhado em Junho 2026 (Boris Cherny/Anthropic, Peter Steinberger, Addy Osmani).

> **Ideia central (Boris Cherny): "I don't prompt Claude anymore."**
> Deixas de ser a pessoa na caixa de chat e passas a ser a pessoa que constrói a máquina que corre a caixa de chat. A unidade de trabalho deixa de ser o prompt e passa a ser o **ciclo**: agir → observar feedback → decidir → repetir até condição de terminação.

---

## 1. O loop fundamental Anthropic (Claude Code e Agent SDK usam o MESMO)

```
GATHER CONTEXT → TAKE ACTION → VERIFY WORK → REPEAT
```

- **Gather context:** o agente vai buscar e ACTUALIZA o próprio contexto (ficheiros, pesquisa, estado) — não recebe tudo à cabeça.
- **Take action:** ferramentas são os blocos primários de execução; dar poucas e boas, não muitas.
- **Verify work:** sinal de verificação DETERMINÍSTICO (teste, status 200, registo visível, GET de confirmação) — **nunca o auto-relato do modelo**. Geração e avaliação SEPARADAS: um agente avalia sempre o próprio trabalho com demasiada generosidade; um avaliador independente céptico é muito mais fiável.
- **Repeat:** até condição de terminação explícita.

## 2. As 4 camadas (cada uma embrulha a anterior)

| Camada | Foco |
|---|---|
| Prompt engineering | as palavras que escreves |
| Context engineering | a informação que o modelo vê na inferência |
| Harness engineering | o ambiente completo à volta do agente (gates, tools, permissões, recovery) — "98.4% infra, 1.6% AI" |
| **Loop engineering** | o ciclo iterativo que conduz ao objectivo sem humano no meio |

## 3. Os 5 movimentos de um turno de loop

1. **DISCOVERY** — objectivo testável com critério de sucesso claro (se não é verificável, não entra no loop).
2. **HANDOFF** — equipar o agente com ferramentas que tocam o ambiente REAL (API, terminal, testes) e o contexto MÍNIMO — nunca o histórico completo.
3. **VERIFICATION** — feedback determinístico externo; proibido "parece-me bem".
4. **PERSISTENCE** — estado FORA do contexto (ficheiros): o contexto morre, o estado sobrevive.
5. **SCHEDULING** — lógica de terminação + gates de escalação + detecção de não-progresso (stall).

## 4. Harness para runs longos multi-sessão (Anthropic, agentes de longa duração)

- **Sessão 1 = Initializer** (prepara ambiente + expande o pedido em lista discreta de features testáveis); **sessões seguintes = Worker** (progresso incremental).
- **Ficheiros de estado:** `progress` (o que cada sessão fez) + `feature_list` (cada item passing/failing) + script de arranque/verificação rápida.
- **Uma feature de cada vez** — nunca tentar o projecto inteiro numa sessão.
- **Ritual de arranque de cada sessão:** confirmar onde estás → ler progress/git log → escolher a próxima feature incompleta de maior prioridade → smoke test end-to-end ANTES de trabalho novo.
- **Checkpoint após cada feature** (commit/registo com mensagem descritiva) → rollback possível.
- **É inaceitável remover ou editar testes** para os fazer passar — isso esconde funcionalidade partida.
- Marcar completude no ficheiro de estado, não por sensação — impede declaração prematura de "terminado".

## 5. Regras de ouro

- **Single-agent primeiro.** Multi-agente tem a complexidade dos microserviços + não-determinismo. Só orquestrar quando 1 loop bem afinado não chega.
- **Papéis separados quando escalar:** Planner (expande em spec) ≠ Generator (executa) ≠ Evaluator (testa e dá feedback céptico).
- **Detecção de stall:** sem progresso em 2 iterações → replan, nunca repetir com mais força.
- **Terminação explícita** (sucesso verificado / stall / budget / gate humano / erro irrecuperável) — um loop sem condição de saída é um bug.

## 6. Mapa para este ecossistema

| Conceito Anthropic | Onde vive aqui |
|---|---|
| Gather, Act, Verify, Repeat | O RARV do Cérebro. O V nunca é opcional |
| Verificação determinística | "Nunca assumir sucesso, confirmar o resultado real" |
| Persistência do estado em ficheiros | O blackboard `cerebro/memory/state.md` e a secção `## RUNS` |
| Agendamento e terminação | As cinco condições de saída do Modo 5, mais o contador de falhas |
| Inicializador e trabalhador | Caderno de tarefa (fixo) e caderno de progresso (por passo) |
| Lista de funcionalidades a passar | Plano numerado com critério de sucesso por passo |
| Gerador diferente do avaliador | Os gates correm em passo separado de quem escreveu |
| Uma coisa de cada vez | "um passo é um agente e uma saída verificável" |

**Aplicar quando:** desenhares um loop (Modo 6), retomares um run em `## RUNS`, montares uma
orquestração de três ou mais passos, ou criares qualquer rotina que corra sem ti à frente.

*Skill loop-engineering v1.0 | 2026-07-06 | fontes: anthropic.com/engineering (Agent SDK, long-running harnesses, context engineering)*
