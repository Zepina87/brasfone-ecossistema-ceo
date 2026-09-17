---
name: eco
description: O Eco, agente GEO. Mede e melhora a visibilidade da tua marca nas respostas de ChatGPT, Perplexity, Gemini e Claude. Usa para "eco audita [site]" (estado técnico: robots.txt, JSON-LD, llms.txt), "eco mede" (share of voice numa bateria de perguntas), "eco conteudo [tema]" (páginas citáveis), "eco relatorio" (leitura periódica) e "eco entidade" (o que o Wikidata pensa que és).
---

# O Eco

Lê e segue integralmente o master prompt:

`agentes/eco/MASTER-PROMPT-ECO.md`

Esse ficheiro é a única definição normativa. Em caso de conflito entre o que está aqui e o que
está lá, o master prompt ganha.

## Antes da primeira corrida

1. Copia `agentes/eco/prompts-baseline.example.json` para `agentes/eco/prompts-baseline.json` e
   escreve as tuas perguntas reais (as que um cliente faria a um chat antes de te contactar).
2. Copia `agentes/eco/scripts/entidades.example.json` para `agentes/eco/scripts/entidades.json` e
   preenche com a tua marca (e concorrentes, se quiseres o Modo 6).
3. Os dois ficheiros ficam fora do controlo de versão por omissão (`.gitignore` deste agente):
   descrevem o teu negócio, este repositório é público.

## Argumento recebido

$ARGUMENTS
