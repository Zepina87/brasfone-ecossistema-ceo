---
name: learn
description: Extrai padrões reutilizáveis da sessão actual e guarda em memory/learnings/ ou memory/patterns/. Usa quando resolves um problema não trivial, descobres um workaround ou identificas um padrão que vai poupar tempo no futuro.
disable-model-invocation: false
argument-hint: [tema opcional] ou sem argumento para análise automática
---

# /learn, extractor de padrões

## O que fazes quando este skill é activado

Analisa a conversa actual e extrai padrões reutilizáveis para a tua memória persistente.

## Processo obrigatório (4 passos)

### PASSO 1 — Scaneares a sessão
Olha para trás na conversa. Identifica momentos onde:
- Um problema foi resolvido de forma não óbvia
- Tu corrigiste uma abordagem (a correcção passa a regra)
- Um workaround foi descoberto (ex: MCP não funciona → usar API REST)
- Um padrão surgiu e pode ser reutilizado noutros agentes
- Uma integração foi validada (ex: API Manychat confirmada)

### PASSO 2 — Classificares o tipo
- **learning** → solução específica, problema encontrado e resolvido
- **pattern** → padrão arquitectural reutilizável em múltiplos agentes
- **feedback** → correcção do José que deve guiar comportamento futuro

### PASSO 3 — Propores antes de guardar
Apresentar ao José:
```
Encontrei [N] padrão(ões) para guardar:

1. [TÍTULO] — tipo: [learning|pattern|feedback]
   Resumo: [1 linha]
   Guardar em: memory/[learnings|patterns|]/[nome-ficheiro].md

Confirmas?
```

### PASSO 4 — Guardares nos ficheiros correctos

**Para learnings** → `memory/learnings/[agente-ou-tema]-[YYYY-MM-DD].md`
Formato:
```markdown
## Sessão [data]
- Agente/Tema: [nome]
- Problema: [descrição]
- Solução: [descrição]
- Reutilizável em: [onde aplica]
```

**Para patterns** → `memory/patterns/[categoria].md`
Formato:
```markdown
# Padrão: [Nome]
## O que é
## Quando usar
## Estrutura
## Instâncias activas
## Lição aprendida
```

**Para feedback** → criar ou actualizar `memory/feedback_[tema].md`
Formato frontmatter standard:
```markdown
---
name: feedback-[tema]
type: feedback
---
Regra: [regra clara]
**Why:** [razão]
**How to apply:** [quando activar]
```

### Depois de guardar
Actualizar o índice `MEMORY.md` com o link para o novo ficheiro se não existir ainda.

## Categorias de padrões a detectar

1. **Error resolution** — o que falhou, causa raiz, fix aplicado
2. **MCP limitations** — quando um MCP não funciona e qual o workaround
3. **Agent design** — decisões de arquitectura de agentes que funcionaram
4. **Integration patterns** — como duas ferramentas foram ligadas com sucesso
5. **Prompt patterns** — estruturas de prompt que produziram outputs superiores
6. **Deploy patterns** — como publicar/distribuir um output

## O que NÃO extrair
- Fixes triviais (typo, formatação)
- Problemas únicos sem recorrência (serviço fora do ar)
- Informação já em MEMORY.md

## Argumento recebido: $ARGUMENTS
- Com argumento → focar extracção nesse tema específico
- Sem argumento → análise completa da sessão actual
