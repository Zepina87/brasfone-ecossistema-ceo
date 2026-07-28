---
name: adhd
description: Ideação divergente paralela para problemas abertos. Lança N branches de raciocínio ISOLADOS sob molduras cognitivas distintas (sem contexto partilhado), depois um crítico separado pontua, agrupa, poda armadilhas e aprofunda as melhores. Corrige a "convergência prematura" (o modelo ancora na primeira ideia e todas as ramificações herdam a âncora). Usar SÓ quando o pedido tem a forma "dá-me umas quantas formas de…" — decisões de design, naming, estratégia, ângulos de conteúdo/copy, debugging difuso, arquitectura de solução. NUNCA para tarefas de execução determinística. Trigger: /adhd [problema].
disable-model-invocation: true
---

# ADHD — Ideação Divergente Paralela (versão Brasfone PT-PT)

> Autorado de raiz a partir do protocolo público de UditAkhourii/adhd (MIT). Não contém código do repo original — é a nossa reimplementação Brasfone. O padrão corre nativo no Claude Code via o tool `Agent/Task`; **não requer o pacote npm `adhd-agent`, rede, shell ou env vars.**

## Missão

Vencer a convergência prematura. Chain-of-Thought linear ancora na primeira coisa que diz; Tree-of-Thought alarga mas continua a andar sobre um contexto partilhado, logo a âncora persiste. Esta skill trata isso como problema **arquitectural, não de prompting**: gera ramos de raciocínio isolados, com zero contexto partilhado durante a divergência, e só depois avalia.

## PRÉ-FLIGHT GATE — quando NÃO correr

Saltar a skill (e responder normal) se:
- O pedido é "rápido", "standard", "canónico", "textbook", ou tem **uma** solução óbvia única.
- É **execução determinística**: criar ou deduplicar registos, normalizar dados, escrever num sistema de produção, aplicar etiquetas, sincronizar, pontuar segundo critérios fixos, planear tarefas. Estes agentes precisam de UMA resposta auditável (`🧭 ROUTE`), não de 30 ideias.
- O custo (5-10× uma resposta, ~30-90s) não se justifica para a decisão em causa.

Invocação explícita `/adhd` salta o gate (o José pediu de propósito).

## FASE 1 — DIVERGE (modo gerador)

1. Escolher **5 molduras cognitivas** da tabela abaixo (variar de run para run; escolher as mais produtivas para o problema).
2. Lançar **5 `Agent/Task` calls PARALELOS e ISOLADOS** — invariante crítico: **não serializar, não partilhar contexto entre branches** (é isso que impede a ancoragem). Cada branch recebe apenas: o problema + contexto mínimo + a sua moldura + a instrução:
   > "Estás em modo DIVERGENTE sob a moldura [X]. Gera 6 ideias curtas e distintas. NÃO avalies, NÃO escolhas a melhor, empurra para além das respostas óbvias. Devolve APENAS um array JSON de 6 strings."
3. Proibido avaliar nesta fase. Recolher os 30 candidatos (5×6).

## FASE 2 — FOCUS (modo crítico, separado do gerador)

1. **Pontuar** cada ideia: novidade (0-10), viabilidade (0-10), fit ao objectivo (0-10). Marcar **armadilhas** (ideias com risco escondido) com razão de 1 linha.
2. **Agrupar** por ângulo subjacente (dá o mapa de onde estão as ideias e onde há vazios).
3. **Aprofundar as 3 melhores** por score ponderado: `novidade×0.35 + viabilidade×0.40 + fit×0.25`. Para cada uma: esboço de 4-8 frases, riscos que a sustentam, primeiro passo concreto, sub-ideias.
4. Destacar 1 **pick não-óbvio** (a ideia lateral que o baseline single-shot nunca consideraria).

## MOLDURAS COGNITIVAS

Genéricas: engenheiro de hardware · regulador · criança de 10 anos · concorrente directo · biólogo/natureza · logística · game designer · lógica de mercados · inversão (fazer o oposto) · orçamento €0 / 1 hora · orçamento infinito · remover 1 pressuposto · speedrunner · colónia de formigas · on-call às 3h da manhã.

Comercial (usar quando o problema é de vendas ou de relação com clientes): vendedor cansado ao quadragésimo telefonema · cliente que já tem software e não quer mudar · CFO que corta budget · parceiro certificado de um fornecedor de software · consultor que cobra por hora · o lead que nunca atende.

## INTEGRAÇÃO BRASFONE — regras que não se negoceiam

- **A montante dos gates, nunca a contornar.** O output do ADHD é matéria-prima especulativa. Antes de QUALQUER acção externa, passa obrigatoriamente por RARV + ghost-check + prova social (`kb/prova-social/casos.md`). ADHD gera ângulos; os gates decidem o que sai.
- **Não fura zero-hallucination.** As ideias distorcidas são para ideação interna. Nada de alegações inventadas em copy final (métricas, parcerias) — a prova social continua a valer só a confirmada na KB.
- **Custo:** avisar sempre que uma run custa 5-10× e ~30-90s. Não usar em loops nem em pipelines determinísticos (viola o Cost Control do Cérebro: tiering/batching).
- **PT-PT** no conteúdo; sem travessão em output destinado a cliente.

## AGENTES QUE DEVEM CHAMAR /adhd (divergência genuína)

Conteúdo (ângulos para uma publicação) · Copy (assuntos de email, ganchos) · Design (direcções visuais) · Arquitectura (formas de resolver um problema técnico).

**NÃO chamar** em agentes de execução determinística: os que criam registos, pontuam segundo critérios fixos, sincronizam sistemas ou planeiam tarefas. São convergentes por desenho, e divergir estraga-lhes a auditabilidade.
