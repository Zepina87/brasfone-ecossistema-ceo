---
name: context-budget
description: Audita o consumo de context window do Claude Code (agentes, skills, MCP servers, CLAUDE.md, rules). Identifica bloat, componentes redundantes e produz recomendações priorizadas de poupança de tokens. Usar para "context budget", "auditoria de tokens", "quanto contexto estou a gastar", ou antes de instalar mais skills/MCPs.
metadata:
  origin: ECC (affaan-m/ECC, MIT) — adaptado Brasfone 2026-07-04
---

# Context Budget — Auditoria de overhead de contexto

Analisa o overhead de tokens de todos os componentes carregados numa sessão Claude Code e produz optimizações accionáveis. Liga directamente ao objectivo Token Burn da Brasfone.

## Quando usar

- Sessões lentas ou qualidade a degradar (pressão de contexto)
- Depois de instalar skills, agentes ou MCP servers novos
- Antes de adicionar mais componentes ("tenho espaço?")
- Auditoria periódica do ecossistema (24 agentes + 60+ skills instaladas)

## Como funciona

### Fase 1: Inventário

Faz scan e estima tokens por componente (prosa: `palavras × 1.3`; código: `chars / 4`):

- **Agentes** — `~/.claude/agents/*.md`: flag ficheiros >200 linhas; descriptions >30 palavras (a description carrega em TODAS as invocações do Agent tool, mesmo sem usar o agente)
- **Skills** — `~/.claude/skills/*/SKILL.md`: flag ficheiros >400 linhas; descriptions inchadas (a lista de skills carrega em cada sessão)
- **MCP servers** — `~/.claude/settings.json` (bloco `mcpServers`) + MCPs claude.ai: contar tools; estimar ~500 tokens de schema por tool. Flag: servers >20 tools, servers que embrulham CLIs simples
- **CLAUDE.md** — cadeia projecto + user: flag total >300 linhas
- **MEMORY.md** — índice de memória: flag se voltar a crescer além de ~1 linha/entrada

### Fase 2: Classificar

| Bucket | Critério | Acção |
|--------|----------|-------|
| **Sempre necessário** | Referenciado no CLAUDE.md, suporta comando activo | Manter |
| **Às vezes** | Específico de domínio, não referenciado | Lazy-load / on-demand |
| **Raramente** | Sem referência, conteúdo sobreposto | Remover ou desactivar |

### Fase 3: Padrões de problema

- Descriptions de agentes inchadas (>30 palavras)
- Agentes pesados (>200 linhas)
- Componentes redundantes (skills que duplicam agentes; rules que duplicam CLAUDE.md)
- MCP over-subscription (>10 servers; servers que embrulham CLIs gratuitos) — **é a maior alavanca**: um server de 30 tools custa mais do que todas as skills juntas
- CLAUDE.md com explicações verbosas ou secções obsoletas

### Fase 4: Relatório

```
Context Budget Report
═══════════════════════════════════════
Overhead total estimado: ~XX.XXX tokens
Contexto efectivo disponível: ~XXX.XXX tokens (XX%)

Breakdown: Agentes / Skills / MCP tools / CLAUDE.md / Memória

⚠️ Problemas encontrados (N): [ordenados por poupança]

Top 3 optimizações:
1. [acção] → poupa ~X.XXX tokens
2. ...
Poupança potencial: ~XX.XXX tokens (XX% do overhead)
```

Modo verbose: contagens por ficheiro, breakdown dos mais pesados, lista de tools MCP com tamanho de schema por tool.

## Boas práticas

- **MCP é a maior alavanca** — cada tool ≈ 500 tokens de schema
- **Auditar depois de cada instalação** — apanhar creep cedo (regra INSPIRA: avaliar custo de contexto antes de instalar)
- **Verbose só para debugging** — não para auditorias regulares
