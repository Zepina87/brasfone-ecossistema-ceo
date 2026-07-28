---
name: strategic-compact
description: Compactação estratégica de contexto — explica quando fazer /compact manual em fronteiras lógicas de tarefa em vez de depender da auto-compactação arbitrária. Acompanha o hook suggest-compact.js (ecc-mined) que sugere /compact com base no tamanho real do contexto. Usar quando aparecer a sugestão [StrategicCompact] ou para decidir se é boa altura para compactar.
metadata:
  origin: ECC (affaan-m/ECC, MIT) — adaptado Brasfone 2026-07-04
---

# Strategic Compact — compactar em fronteiras lógicas

A auto-compactação dispara em pontos arbitrários (muitas vezes a meio de uma tarefa). A compactação estratégica acontece em fronteiras lógicas: depois da exploração e antes da execução; depois de um milestone e antes do próximo.

## O hook (já instalado)

`~/.claude/hooks/suggest-compact.js` — registado em `settings.json` (PreToolUse, matcher `Edit|Write`). Dois sinais:

1. **Tamanho de contexto (primário)** — lê o último registo `usage` do transcript e soma `input + cache_read + cache_creation` (tamanho real do contexto). Sugere `/compact` a 160k numa janela de 200k, 250k numa janela de 1M; repete a cada +60k de crescimento.
2. **Contagem de tool-calls (secundário)** — sugere às 50 chamadas, depois a cada 25.

### Configuração (env vars)

- `COMPACT_CONTEXT_THRESHOLD` — tokens antes da 1.ª sugestão (0 desactiva o sinal de contexto)
- `COMPACT_CONTEXT_INTERVAL` — crescimento antes de repetir (default 60000)
- `COMPACT_THRESHOLD` — tool calls antes da 1.ª sugestão (default 50)
- `COMPACT_STATE_TTL_DAYS` — retenção dos ficheiros de estado no temp dir (default 14)

## Guia de decisão

| Transição de fase | Compactar? | Porquê |
|---|---|---|
| Pesquisa → Planeamento | Sim | Contexto de pesquisa é volumoso; o plano é o destilado |
| Planeamento → Implementação | Sim | Plano está em ficheiro/tasks; libertar contexto p/ código |
| Implementação → Testes | Talvez | Manter se os testes referem código recente |
| Debugging → Feature seguinte | Sim | Traces de debug poluem trabalho não relacionado |
| A meio da implementação | **Não** | Perder nomes de variáveis/paths/estado parcial é caro |
| Depois de abordagem falhada | Sim | Limpar o raciocínio do beco sem saída |

## O que sobrevive à compactação

| Persiste | Perde-se |
|---|---|
| CLAUDE.md + memória persistente | Raciocínio intermédio |
| Blackboard (state.md do Cérebro) | Conteúdo de ficheiros já lidos |
| Task list | Contexto conversacional multi-passo |
| Git state + ficheiros em disco | Histórico de tool calls |

## Boas práticas

1. **Escrever antes de compactar** — despejar contexto importante para ficheiros/memória/state.md primeiro (regra do blackboard do Cérebro: actualizar após cada passo, não no fim)
2. **`/compact` com instrução** — ex.: `/compact foca no passo 4 do mining ECC`
3. **O hook diz *quando*, tu decides *se*** — a sugestão não é ordem
4. **Nunca a meio de uma edição multi-ficheiro**
