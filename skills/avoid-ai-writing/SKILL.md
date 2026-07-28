---
name: avoid-ai-writing
description: Audit and rewrite content to remove AI-generated writing patterns ("AI-isms"). Two modes — rewrite (default, fixes and produces clean text) and detect (flags without changing). Detects 34+ categories including Tier 1/2/3 vocabulary, template phrases, em-dash abuse, bold overuse, uniform rhythm, hedging, hollow intensifiers. Use before publishing any public-facing writing. Complements `/ghost-check` (Brasfone PT-PT variant).
license: MIT · Conor Bronsdon
source: github.com/conorbronsdon/avoid-ai-writing (v3.3.1)
---

# avoid-ai-writing (EN)

Skill original de Conor Bronsdon, versão 3.3.1. Para Brasfone, usar preferencialmente a versão PT-PT adaptada: **`/ghost-check`**.

## Two modes

### Rewrite (default)
1. Detect all AI-isms in the input
2. Return a rewritten version with patterns removed
3. Show summary of changes
4. Run a second-pass audit to catch residuals

### Detect
Flag only, no rewrite. Useful when the text should not be altered but you want a quality assessment.

## Target: AI-isms — single source of truth

> **All patterns live in the canonical `red-list.md` at `~/.claude/skills/ghost-check/red-list.md`.**
> Load it before auditing. Do **not** copy the lists here — they change only there.
> The red-list is bilingual (EN + PT); for EN output use the EN entries.

10 blocks: Tier 1/2/3 vocabulary · template phrases · assistant/chatbot phrases · formatting · hedging & hollow intensifiers · adverb-tics · structural rhythm · PT-specific slop.

Beyond the red-list, also flag these EN-only structural tells:
- Missing connectives (abrupt transitions that break flow)
- Copula avoidance ("X stands as", "X serves as" instead of "X is")
- Synonym cycling (avoiding repeating a natural keyword)
- Cold open rushing to thesis

## Severity tiers

- **P0 credibility killers** — patterns that destroy trust on sight
- **P1 obvious AI smell** — recognisable AI tells
- **P2 polish** — stylistic issues

## Context profiles (adjust strictness)

| Profile | Rigor |
|---|---|
| LinkedIn post | 🔴 Maximum |
| Blog | 🟠 High |
| Technical blog | 🟡 Medium-high |
| Investor email | 🔴 Maximum |
| Documentation | 🟢 Low (jargon tolerance) |
| Casual | 🟡 Medium |

## Output format

### Rewrite mode
```
ISSUES FOUND: [N]
- [Tier 1] word × count
- [Template] phrase
- [Formatting] em-dashes × count

REWRITTEN TEXT:
[...clean text...]

CHANGES SUMMARY:
- Removed [X] Tier 1 words
- Rewrote [N] template phrases
- Reduced em-dashes from [A] to [B]

SECOND-PASS AUDIT:
- [residuals or "clean"]
```

### Detect mode
```
FLAGS BY SEVERITY:

P0:
- [line/quote] — [issue] — [suggested action]

P1:
- [...]

P2:
- [...]

ASSESSMENT: [Publishable / Revise / Rewrite required]
```

## Principle

Writing that sounds like a **person** wrote it — direct, specific. Writing should **demonstrate** confidence, not **assert** it. Human irregularities are voice, not errors.

## Brasfone note

Use `/ghost-check` for PT-PT texts. This skill is kept in English as reference and for any EN output (e.g. international clients, LinkedIn EN content).

Full original: https://github.com/conorbronsdon/avoid-ai-writing
