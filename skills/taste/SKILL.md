---
name: taste
description: Calibra o julgamento estético do Claude para design de alta qualidade — tipografia, cor, espaçamento, motion, layout. Corre antes de qualquer geração HTML/CSS. Usa quando: design parece genérico, queres elevar a qualidade visual, antes de activar o Design Pro, ou quando o output parece "AI slop". Resultado: Claude passa a fazer escolhas com opinião, como um designer sénior.
argument-hint: "[contexto opcional: marca, tipo de output, audiência]"
---

# Taste — Calibração de Design para Claude

**Missão:** Transformar o Claude de "funcionalmente correcto" em "visualmente memorável".
**Regra de ouro:** Um designer sénior nunca escolhe o default. Taste é a recusa activa do previsível.

## Argumento recebido: $ARGUMENTS

---

## ACTIVAÇÃO

Ao activar, confirmar:
> "🎨 Taste carregado — calibração activa. Nenhuma escolha de design será default a partir daqui."

---

## OS 5 EIXOS DE TASTE

### 1 — TIPOGRAFIA

**Regra master:** Nunca um font pair banal. Display deve contrastar com body — não variar suavemente.

| ✅ Com Taste | ❌ Sem Taste |
|-------------|-------------|
| Clash Display + DM Sans | Inter + Inter |
| Playfair Display + IBM Plex | Roboto + Open Sans |
| Space Grotesk + Literata | Helvetica + Arial |

**Hierarquia obrigatória:** 3 tamanhos max — display / body / caption. Nunca 5 tamanhos na mesma página.

**Letter-spacing:**
- Display grande (>48px): tight (`-0.02em`)
- Small caps / labels: wide (`+0.08em`)
- Body: nunca alterar (`0`)

**Line-height:**
- Display: 1.0–1.15 (tenso, impacto)
- Body: 1.5–1.7 (legível, respirável)
- Captions: 1.3–1.4

---

### 2 — COR

**Regra master:** Uma cor dominante + um acento afiado. Nunca 5 cores iguais em importância.

| Princípio | Aplicação |
|-----------|-----------|
| Cor dominante = 60–70% da área | Fundo, superfícies, containers |
| Cor de acento = 10–15% | CTAs, destaques, iconografia |
| Neutros = 20–30% | Texto, separadores, bordas |

**Proibido:**
- Gradientes roxos (#7c3aed, #8b5cf6) — assinatura de AI
- "Safe blue" (#3b82f6) sem razão contextual
- Mais de 2 hues num único componente
- Sombras `rgba(0,0,0,0.1)` genéricas — usar sombras com cor (ex: `rgba(var(--primary), 0.15)`)

**Contraste obrigatório:** WCAG AA — 4.5:1 texto normal, 3:1 texto grande.

---

### 3 — ESPAÇAMENTO

**Regra master:** Espaçamento é hierarquia. Proximidade = relação. Distância = separação.

**Sistema de escala (base 4px):**
```
4px  — detalhe interno (gap entre ícone e texto)
8px  — espaçamento pequeno (padding input)
16px — espaçamento base (padding card)
24px — separação de grupos próximos
32px — separação de secções
48px — secções independentes
64px — acima do fold / hero
```

**Regras de ouro:**
- Padding de cards: nunca igual em X e Y — geralmente mais em Y (respira melhor verticalmente)
- Whitespace generoso = premium. Denso = information-rich. Nunca "default Bootstrap"
- Nunca padding `p-4` Tailwind como primeira escolha — questionar sempre

---

### 4 — MOTION

**Regra master:** Motion tem propósito. Guia atenção, não decora.

| ✅ Com Taste | ❌ Sem Taste |
|-------------|-------------|
| fadeUp + stagger 80ms | bounce / elastic |
| ease-out (rápido no início) | ease-in-out linear |
| duration 200–600ms | >800ms qualquer coisa |
| Só anima o que importa | Tudo anima ao mesmo tempo |

**Valores obrigatórios:**
- Fast: 150ms (hover states)
- Base: 300ms (entradas de elementos)
- Slow: 600ms (page transitions, reveals de secções)
- Easing: `cubic-bezier(0.16, 1, 0.3, 1)` (ease-out rápido)

**Proibido:**
- `bounce` easing — amateur signal
- `infinite` animations em hero sections
- Parallax sem propósito
- Animações em mais de 3 elementos simultâneos sem choreografia

---

### 5 — LAYOUT

**Regra master:** Grid é estrutura. O que sai do grid é drama.

**Decisões de layout com taste:**

| Situação | Escolha com taste |
|----------|------------------|
| Hero | 1 acção clara above the fold — headline + sub + CTA único |
| Cards | Nunca 3 colunas iguais em móvel — 1 coluna é mais forte |
| Imagem + texto | Alinhamento diagonal ou bleeding edge — não box quadrado |
| Tabelas | Alternância subtil de linhas (opacity 3-5%) — nunca bordas |
| Formulários | Campo único por linha — nunca 2 inputs na mesma linha em móvel |

**Proporções clássicas:**
- Golden ratio (1:1.618) para secções hero vs content
- Rule of thirds para posicionamento de CTAs
- Container max-width: 1280px (nunca full-width em desktop)

---

## CHECKLIST PRÉ-GERAÇÃO (obrigatório antes de escrever código)

Antes de gerar qualquer HTML/CSS, responder internamente:

```
□ Font pair: display contrasta com body? (NÃO são da mesma família)
□ Cor dominante definida? Acento afiado definido?
□ Gradiente roxo proibido? Purple/violet fora da paleta da tua marca?
□ Hierarquia tipográfica: max 3 tamanhos?
□ Espaçamento intencional ou default Tailwind?
□ Motion: propósito definido ou decorativo?
□ Layout: hierarquia visual clara above the fold?
□ "O que torna este output INESQUECÍVEL?" — responder em 1 frase
```

Se qualquer resposta for "não sei" → parar e decidir antes de gerar.

---

## INTEGRAÇÃO COM DESIGN PRO

Quando o Design Pro está activo, o Taste corre **antes** do Aesthetic Direction Protocol (§1):

```
[Taste carregado → Checklist pré-geração]
         ↓
[Design Pro §1 — Aesthetic Direction Protocol]
         ↓
[Geração com escolhas intencionais]
```

---

## ANTI-AI-SLOP (24 Tells a Evitar)

| # | Tell | Alternativa |
|---|------|-------------|
| 1 | Gradiente roxo genérico | Cor de marca específica |
| 2 | `shadow-lg` Tailwind default | Sombra com cor contextual |
| 3 | Inter como única fonte | Font pair com contraste |
| 4 | 5+ cores na mesma paleta | 1 dominante + 1 acento |
| 5 | Bounce/elastic easing | ease-out cubic-bezier |
| 6 | Cards todos iguais em tamanho | Hierarquia de tamanho intencional |
| 7 | Padding simétrico em X e Y | Mais padding vertical |
| 8 | Emoji em bullet lists | Lucide icons ou SVG custom |
| 9 | >3 níveis de hierarquia de fonte | 3 max (display/body/caption) |
| 10 | CTA "Saiba mais" / "Click here" | CTA específico com verbo de acção |
| 11 | Imagem placeholder (placehold.co) | Nunca usar em output final |
| 12 | 3 colunas iguais em móvel | Single column mobile-first |
| 13 | Texto sobre imagem sem overlay | Semi-transparent overlay ou blur |
| 14 | Todos os elementos animam juntos | Stagger 80ms entre elementos |
| 15 | `#ffffff` fundo puro em dark mode | Off-white (#f8f8f8) ou tint da marca |
| 16 | Bordas `border-gray-200` genéricas | Bordas com opacidade (opacity: 10%) |
| 17 | Line-height 1.0 em body | 1.5–1.7 em body |
| 18 | Letter-spacing 0 em display grande | `-0.02em` em display >48px |
| 19 | Container full-width em desktop | max-width 1280px centrado |
| 20 | 3 níveis de heading na mesma secção | 1 heading por secção |
| 21 | Cor do texto `#000000` puro | `#111827` ou tint da marca |
| 22 | Formulário com 2 inputs na mesma linha | 1 input por linha |
| 23 | Hover state só muda cor | Hover muda cor + transform sutil |
| 24 | Sem feedback visual em loading | Skeleton ou spinner da marca |

---

*Taste v1.0 | Calibração de Design Premium | Brasfone 2026*
*Baseado em: Design Pro v3.0, Anti-AI-Slop principles, The Power of Moments (Heath)*
