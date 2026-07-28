---
name: dream
description: "Memory consolidation skill for Claude Code. Scans session transcripts for corrections, decisions, preferences, and patterns, then merges findings into persistent memory files. Auto-triggers via native Stop hook every 24hrs. Inspired by how sleep consolidates human memory."
tags: [memory, maintenance, consolidation, autonomous, hook]
---

> O agente consolida a memória enquanto dormes.

## How It Works

Dream corre 4 fases sequenciais. Executar por ordem. Não saltar fases.

```
ORIENT --> GATHER SIGNAL --> CONSOLIDATE --> PRUNE & INDEX
```

### Auto-trigger flow

```
Sessão termina
  --> Stop hook dispara should-dream.sh (~10ms)
  --> Verifica: passaram 24h?
  --> Se NÃO: termina silenciosamente, zero overhead
  --> Se SIM: cria ~/.claude/.dream-pending flag
Próxima sessão inicia
  --> Claude lê CLAUDE.md, vê .dream-pending existe
  --> Lança /dream como subagente em background
  --> Dream corre as 4 fases
  --> Escreve .last-dream timestamp, apaga .dream-pending
  --> Timer reinicia para próximas 24h
```

---

## Phase 1: ORIENT

**Objectivo:** Compreender o estado actual da memória antes de alterar qualquer coisa.

### Steps

1. Ler config:
```bash
cat ~/.claude/skills/dream/.dream-config 2>/dev/null || echo "DREAM_MEMORY_TYPE=native"
```

2. Listar directórios de memória:
```bash
ls -d ~/.claude/projects/*/memory/ 2>/dev/null
```

3. Ler `MEMORY.md` de cada projecto. Notar:
   - Quantos ficheiros de tópico existem
   - Total de linhas do MEMORY.md
   - Datas de última modificação
   - Entradas com datas relativas ("ontem", "semana passada")

4. Ler cada ficheiro de tópico para perceber o que já está guardado.

### Output desta fase
Mapa mental de:
- Quais projectos têm memória
- Que tópicos estão cobertos
- Tamanho dos ficheiros
- O que está potencialmente obsoleto ou contraditório

---

## Phase 2: GATHER SIGNAL

**Objectivo:** Extrair informação importante de sessões recentes sem ler tudo.

### Onde encontrar transcrições
```bash
find ~/.claude/projects/*/sessions/ -name "*.jsonl" -mtime -7 2>/dev/null | sort -t/ -k6 -r
```

### O que procurar (grep direccionado, não leitura completa)

**Correcções do utilizador** (prioridade máxima):
```bash
grep -il "actually\|no,\|wrong\|incorrect\|not right\|stop doing\|don't do\|correction" ~/.claude/projects/*/sessions/*.jsonl 2>/dev/null
```

**Preferências e configuração:**
```bash
grep -il "I prefer\|always use\|never use\|from now on\|going forward\|remember that\|keep in mind\|default to" ~/.claude/projects/*/sessions/*.jsonl 2>/dev/null
```

**Decisões importantes:**
```bash
grep -il "let's go with\|I decided\|we're using\|the plan is\|switch to\|decision\|we agreed" ~/.claude/projects/*/sessions/*.jsonl 2>/dev/null
```

**Padrões recorrentes:**
```bash
grep -il "again\|every time\|keep forgetting\|as usual\|same as before\|we always" ~/.claude/projects/*/sessions/*.jsonl 2>/dev/null
```

### O que extrair

Para cada descoberta, notar:
- **O facto** — o que foi dito ou decidido
- **A data** — derivar do timestamp do ficheiro de sessão
- **Confiança** — instrução explícita (alta) ou preferência implícita (média)?
- **Contradições** — conflita com algo já em memória?

---

## Phase 3: CONSOLIDATE

**Objectivo:** Fundir novas descobertas na memória existente.

### Regras

1. **Nunca duplicar.** Antes de adicionar, verificar se já existe. Se sim, actualizar entrada existente.

2. **Converter datas relativas em absolutas.** Se uma sessão de 15 de Março diz "ontem mudei a API key", escrever "2026-03-14: Mudou API key" na memória. Nunca guardar "ontem" ou "semana passada".

3. **Apagar factos contraditórios.** Se memória diz "X" mas sessão recente diz "não X", remover entrada antiga e escrever nova. Adicionar nota: `(Updated YYYY-MM-DD, previously: X)`.

4. **Organização por ficheiros de tópico:**
   - `feedback_*.md` — preferências, correcções, como o utilizador quer as coisas
   - `project_*.md` — decisões de projecto, contexto, estado
   - `reference_*.md` — tokens, URLs, IDs, credenciais
   - `learnings/` — padrões reutilizáveis, workarounds
   - Respeitar a estrutura já existente na memória

5. **Formato de entrada:**
```markdown
- [YYYY-MM-DD] O facto ou preferência. (source: session, confidence: high/medium)
```

---

## Phase 4: PRUNE & INDEX

**Objectivo:** Manter MEMORY.md como índice lean. Remover conteúdo obsoleto. Impor limite de 200 linhas.

### Regras MEMORY.md

MEMORY.md é um **ficheiro de índice**, não um repositório de conteúdo. Deve conter:
- Links/referências para ficheiros de tópico
- Resumo de uma linha do que cada ficheiro de tópico contém
- Data da última actualização de cada ficheiro

MEMORY.md **nunca** deve conter:
- Entradas completas de memória (essas vão para ficheiros de tópico)
- Descrições longas
- Conteúdo duplicado que já existe em ficheiros de tópico

### Limite: 200 linhas

Se MEMORY.md ultrapassar 200 linhas após consolidação:
1. Mover conteúdo inline para o ficheiro de tópico adequado
2. Substituir entradas longas por resumos de uma linha + links
3. Remover entradas que apontam para ficheiros eliminados ou vazios
4. Se ainda acima de 200 linhas, mover entradas mais antigas para `archive.md`

### Remover entradas obsoletas

Remover ou arquivar entradas:
- Com mais de 90 dias sem referências em sessões recentes
- Contraditadas por entradas mais recentes (devia ter sido apanhado na Fase 3)
- Sobre projectos/repos que já não existem em `~/.claude/projects/`

### Registar timestamp do dream

Após completar todas as 4 fases:
```bash
date +%s > ~/.claude/projects/C--Users-josep-es4uf2w/memory/.last-dream
rm -f ~/.claude/.dream-pending
```

---

## Safety

- **Nunca apagar memória sem substituição.** Se remover entrada, ou foi contraditada (substituída por mais recente) ou foi movida (para ficheiro de tópico ou arquivo). Nunca simplesmente apagar.
- **Backup antes da primeira execução:**
```bash
cp -r ~/.claude/projects/C--Users-josep-es4uf2w/memory/ ~/.claude/projects/C--Users-josep-es4uf2w/memory-backup-$(date +%Y%m%d)/
```

---

## Phase 6: SELF-IMPROVE (Nível 3 Agents)

**Objectivo:** Analisar agentes Nível 3 e propor melhorias específicas ao PROGRAM.md de cada um.

Correr após LINT. Apenas para agentes com PROGRAM.md + PERFORMANCE-LOG.md.

### Agentes Nível 3 (verificar por esta ordem)

```
~/.claude/skills/[outro-agente]/PROGRAM.md
~/.claude/skills/sombra/PROGRAM.md
~/.claude/skills/[o-teu-agente]/PROGRAM.md
~/.claude/skills/ressuscitador/PROGRAM.md
```

### Para cada agente

1. Ler PROGRAM.md — direcção actual e critérios de sucesso
2. Ler PERFORMANCE-LOG.md — execuções recentes
3. Verificar sessões dos últimos 7 dias que mencionem esse agente
4. Se há padrão de falha ou feedback negativo → formular 1 proposta específica
5. Escrever proposta em PERFORMANCE-LOG.md §Proposta de Melhoria (com data)
6. **NUNCA aplicar automaticamente — apenas propor**

### Output

Adicionar no resumo final:
```
SELF-IMPROVE YYYY-MM-DD:
- [outro agente]: [proposta ou "sem mudanças necessárias"]
- Sombra: [proposta ou "sem mudanças necessárias"]
- [nome do agente]: [proposta ou "sem mudanças necessárias"]
- Ressuscitador: [proposta ou "sem mudanças necessárias"]
```

---

## Phase 5: LINT (Memory OS Health Check)

**Objectivo:** Verificar saúde da wiki/ e detectar informação obsoleta ou contraditória.

Correr após PRUNE & INDEX. Ler `memory/MEMORY-OS.md §lint` para a checklist completa.

### Checklist mínima

1. Verificar se páginas `wiki/*.md` têm `last_updated` >60 dias — assinalar para revisão
2. Verificar contradições entre `feedback_*.md` recentes e páginas `wiki/`
3. Verificar SPAR scores em `wiki/agents.md` — reflectem sessões recentes?
4. Verificar as regras específicas dos teus sistemas antes de assumir comportamento
5. Links em `MEMORY.md` todos resolvem?

### Output do lint

Adicionar no resumo final:
```
LINT YYYY-MM-DD:
✅ [items OK]
⚠️  [items para atenção — não bloqueiam]
❌ [items críticos — resolver na próxima sessão]
```

---

## Verification

Após correr, verificar:
1. `wc -l` em MEMORY.md — deve ser abaixo de 200 linhas
2. Verificar que nenhum ficheiro de tópico tem entradas duplicadas
3. Confirmar que não restam datas relativas ("ontem", "semana passada", etc.)
4. Verificar que todos os ficheiros de tópico referenciados em MEMORY.md existem
5. Imprimir resumo: entradas adicionadas, actualizadas, arquivadas, contradições resolvidas, lint report
