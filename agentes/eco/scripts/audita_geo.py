#!/usr/bin/env python3
"""O Eco - auditoria GEO deterministica de um dominio.

Porque existe: escrever "robots OK (IA permitida)" sem nomear um unico crawler e afirmacao sem
medicao. Este script mede, e separa TREINO de CITABILIDADE, que nao sao a mesma coisa: bloquear
GPTBot nao tira citabilidade no ChatGPT Search (isso e o OAI-SearchBot), e Google-Extended nunca
governa elegibilidade para AI Overviews (isso e o Googlebot).

Taxonomia extraida de AgriciDaniel/claude-seo (MIT), com as fontes primarias dos proprios
fabricantes. Sem dependencias externas: stdlib apenas, de proposito, para nao arrastar playwright.

Uso:  python3 audita_geo.py <dominio|url> [mais dominios...] [--json saida.json]
Sai 0 sempre que conseguiu medir; 1 se nenhum alvo respondeu.
"""
import json
import re
import sys
import urllib.error
import urllib.request
from datetime import date

UA = "Mozilla/5.0 (compatible; EcoGEO/1.0)"

# Lista canonica de bots de IA, copia LOCAL de ai-robots-txt/ai.robots.txt (MIT, dezenas de
# contribuidores). Local de proposito: o auditor nao vai a rede em cada execucao, senao a medicao
# deixa de ser reproduzivel e passa a depender de um repo alheio estar de pe. Actualizar copiando
# de novo o robots.json desse repo quando quiseres a lista mais recente.
_CANON = {}
try:
    import os as _os
    _p = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "kb", "ai-robots.json")
    with open(_p, encoding="utf-8") as _f:
        _CANON = {k: v for k, v in json.load(_f).items() if not k.startswith("_")}
except Exception:
    pass  # sem lista local o auditor continua a funcionar, so perde o cruzamento


def obedece(bot):
    """Devolve True/False/None (None = por esclarecer ou desconhecido) segundo a lista canonica."""
    v = _CANON.get(bot)
    if not v:
        return None
    r = str(v.get("respect", "")).strip().lower()
    if r.startswith("[yes") or r == "yes":
        return True
    if r.startswith("[no") or r == "no":
        return False
    return None
TIMEOUT = 25

# (bot, capacidade que governa, o que NAO prova)
BOTS = [
    ("OAI-SearchBot",      "citabilidade", "ChatGPT Search",                 "nao prova nada sobre treino da OpenAI"),
    ("Claude-SearchBot",   "citabilidade", "pesquisa do Claude",             "nao prova nada sobre treino da Anthropic"),
    ("PerplexityBot",      "citabilidade", "Perplexity",                     ""),
    ("Googlebot",          "citabilidade", "Google Search, AI Overviews e AI Mode", "nao confundir com Google-Extended"),
    ("Bingbot",            "citabilidade", "Bing e Copilot",                 ""),
    ("Applebot",           "citabilidade", "Siri, Spotlight e Safari",       "nao confundir com Applebot-Extended"),
    ("MistralAI-Index",    "citabilidade", "pesquisa da Mistral",            ""),
    ("Amazonbot",          "citabilidade", "respostas da Alexa",             ""),
    ("GPTBot",             "treino",       "treino de modelos OpenAI",       "NAO governa citabilidade no ChatGPT Search"),
    ("ClaudeBot",          "treino",       "treino de modelos Anthropic",    "NAO governa citabilidade na pesquisa do Claude"),
    ("Google-Extended",    "treino",       "treino e grounding do Gemini e Vertex", "NAO governa AI Overviews nem Google Search"),
    ("Applebot-Extended",  "treino",       "opt-out de treino da Apple Intelligence", "NAO governa Siri, Spotlight nem Safari"),
    ("CCBot",              "treino",       "Common Crawl",                   ""),
    ("Bytespider",         "treino",       "ByteDance",                      "NAO obedece ao robots.txt: permitir/bloquear aqui nao o trava"),
    ("cohere-ai",          "treino",       "Cohere",                         "obediencia ao robots.txt POR ESCLARECER, nao assumir"),
]

# Operadores cujos bots decidem se somos citados. Um bot novo de um destes e noticia;
# um bot novo de um scraper qualquer nao e.
OPERADORES_QUE_IMPORTAM = ("OpenAI", "Anthropic", "Google", "Perplexity", "Microsoft",
                           "Apple", "Meta", "Mistral", "Amazon", "DuckDuckGo", "You.com")

# Ignoram robots.txt por desenho: so se controlam no servidor.
USER_TRIGGERED = ["ChatGPT-User", "Claude-User", "Perplexity-User", "Google-Agent",
                  "Google-NotebookLM", "Google Messages"]


def fetch(url, timeout=TIMEOUT):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            raw = r.read()
            enc = r.headers.get_content_charset() or "utf-8"
            return r.status, raw.decode(enc, errors="replace"), dict(r.headers)
    except urllib.error.HTTPError as e:
        return e.code, "", {}
    except Exception as e:
        return None, f"ERRO: {e}", {}


def parse_robots(txt):
    """Devolve {user_agent_minusculas: [(tipo, caminho), ...]} respeitando grupos consecutivos."""
    grupos, agentes_actuais, a_ler_agentes = {}, [], False
    for linha in txt.splitlines():
        linha = linha.split("#", 1)[0].strip()
        if not linha or ":" not in linha:
            continue
        campo, _, valor = linha.partition(":")
        campo, valor = campo.strip().lower(), valor.strip()
        if campo == "user-agent":
            if not a_ler_agentes:
                agentes_actuais, a_ler_agentes = [], True
            agentes_actuais.append(valor.lower())
            grupos.setdefault(valor.lower(), [])
        elif campo in ("allow", "disallow"):
            a_ler_agentes = False
            for ag in agentes_actuais:
                grupos.setdefault(ag, []).append((campo, valor))
    return grupos


def regras_para(grupos, bot):
    """robots.txt: o grupo mais especifico que casa com o bot ganha; senao, o grupo *."""
    b = bot.lower()
    if b in grupos:
        return grupos[b], bot
    candidatos = [ag for ag in grupos if ag != "*" and ag and (ag in b or b in ag)]
    if candidatos:
        melhor = max(candidatos, key=len)
        return grupos[melhor], melhor
    return grupos.get("*", []), "*" if "*" in grupos else "(nenhum grupo)"


def permitido(regras, caminho="/"):
    """Longest-match wins; empate resolve a favor de Allow (norma do Google)."""
    melhor_len, melhor_tipo = -1, None
    for tipo, valor in regras:
        if valor == "":
            if tipo == "disallow":
                continue
            continue
        padrao = valor.replace("*", ".*").replace("?", r"\?")
        rx = "^" + padrao
        try:
            if re.match(rx, caminho):
                if len(valor) > melhor_len or (len(valor) == melhor_len and tipo == "allow"):
                    melhor_len, melhor_tipo = len(valor), tipo
        except re.error:
            continue
    if melhor_tipo is None:
        return True
    return melhor_tipo == "allow"


def analisa_home(html):
    tipos, blocos = [], re.findall(
        r'<script[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script\s*>',
        html, re.DOTALL | re.IGNORECASE)
    for b in blocos:
        try:
            d = json.loads(b.strip())
        except Exception:
            achados = re.findall(r'"@type"\s*:\s*"([^"]+)"', b)
            tipos.extend(achados)
            continue
        for item in (d if isinstance(d, list) else [d]):
            if isinstance(item, dict):
                t = item.get("@type")
                if isinstance(t, list):
                    tipos.extend(t)
                elif t:
                    tipos.append(t)
                for sub in item.get("@graph", []) or []:
                    if isinstance(sub, dict) and sub.get("@type"):
                        st = sub["@type"]
                        tipos.extend(st if isinstance(st, list) else [st])
    md = re.search(r'<meta[^>]+name=["\']description["\'][^>]+content=["\']([^"\']*)["\']', html, re.I)
    titulo = re.search(r"<title[^>]*>(.*?)</title>", html, re.DOTALL | re.I)
    texto = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", html, flags=re.DOTALL | re.I)
    texto = re.sub(r"<[^>]+>", " ", texto)
    palavras = len(re.sub(r"\s+", " ", texto).split())
    return {
        "jsonld_tipos": sorted(set(tipos)),
        "meta_description": (md.group(1).strip() if md else ""),
        "title": (re.sub(r"\s+", " ", titulo.group(1)).strip() if titulo else ""),
        "h1": len(re.findall(r"<h1\b", html, re.I)),
        "h2": len(re.findall(r"<h2\b", html, re.I)),
        "palavras_visiveis": palavras,
        "bytes_html": len(html),
        "racio_texto_html": round(palavras * 5.5 / max(len(html), 1), 4),
        "suspeita_csr": palavras < 200 and len(html) > 5000,
    }


def audita(alvo):
    dom = alvo.replace("https://", "").replace("http://", "").strip("/")
    base = "https://" + dom
    r = {"dominio": dom, "data": date.today().isoformat()}

    st, robots, _ = fetch(base + "/robots.txt")
    r["robots_status"] = st
    # Tri-valor de proposito. Um robots.txt que nao respondeu NAO e "tudo permitido": e
    # ausencia de medicao. Nunca ler ausencia de dado como facto.
    if st == 200:
        grupos = parse_robots(robots)
        r["medicao"] = "medida"
    elif st == 404:
        grupos = {}
        r["medicao"] = "ausente"
        r["robots_nota"] = "sem robots.txt (HTTP 404): pela norma tudo permitido, mas e inferencia, nao leitura"
    else:
        grupos = {}
        r["medicao"] = "nao_verificada"
        r["robots_nota"] = f"robots.txt inacessivel (HTTP {st}): estado dos bots DESCONHECIDO"
    r["robots_grupos"] = sorted(grupos.keys())

    r["bots"] = []
    for bot, capacidade, governa, aviso in BOTS:
        if r["medicao"] == "nao_verificada":
            estado, grupo = "NAO VERIFICADO", "(sem leitura)"
        else:
            regras, grupo = regras_para(grupos, bot)
            estado = "PERMITIDO" if permitido(regras) else "BLOQUEADO"
            if r["medicao"] == "ausente":
                estado = "PERMITIDO (inferido)"
        r["bots"].append({
            "bot": bot, "capacidade": capacidade, "governa": governa,
            "estado": estado, "grupo_aplicado": grupo, "aviso": aviso,
            "obedece": obedece(bot),
        })
    # Bots novos: so os de operadores que decidem se somos citados. A lista canonica tem
    # centenas de entradas e a maioria e scraper obscuro: despejar tudo seria ruido.
    conhecidos = {b[0] for b in BOTS} | set(USER_TRIGGERED)
    r["bots_novos"] = sorted(
        k for k, v in _CANON.items()
        if k not in conhecidos
        and any(o in str(v.get("operator", "")) for o in OPERADORES_QUE_IMPORTAM)
    )
    r["canon_total"] = len(_CANON)
    r["user_triggered"] = USER_TRIGGERED

    for f in ("llms.txt", "llms-full.txt"):
        st2, corpo, _ = fetch(base + "/" + f, timeout=15)
        r[f.replace(".", "_").replace("-", "_")] = {
            "status": st2,
            "bytes": len(corpo) if st2 == 200 else 0,
            "primeira_linha": corpo.splitlines()[0][:120] if st2 == 200 and corpo.strip() else "",
        }

    st3, html, hdrs = fetch(base + "/")
    r["home_status"] = st3
    if st3 == 200:
        r["home"] = analisa_home(html)
    else:
        r["home"] = {"erro": html[:200]}
    return r


def imprime(r):
    print(f"\n{'='*72}\n  {r['dominio']}   (robots HTTP {r['robots_status']}, home HTTP {r['home_status']}, medicao: {r['medicao']})\n{'='*72}")
    if r["medicao"] != "medida":
        print(f"  AVISO: {r.get('robots_nota', '')}")
    print("\n  CITABILIDADE (decide se somos citados nas respostas)")
    for b in r["bots"]:
        if b["capacidade"] == "citabilidade":
            print(f"    {b['estado']:<21} {b['bot']:<20} governa: {b['governa']}")
    print("\n  TREINO (nao afecta citabilidade; bloquear e decisao de licenciamento)")
    for b in r["bots"]:
        if b["capacidade"] == "treino":
            print(f"    {b['estado']:<21} {b['bot']:<20} governa: {b['governa']}")
    print(f"\n  IGNORAM ROBOTS.TXT POR DESENHO (so se controlam no servidor):\n    {', '.join(r['user_triggered'])}")
    maus = [b["bot"] for b in r["bots"] if b.get("obedece") is False]
    if maus:
        print(f"    MAIS: {', '.join(maus)} declaram NAO obedecer. O que o robots.txt diz sobre")
        print("          eles e irrelevante; so se travam no servidor.")
    duvida = [b["bot"] for b in r["bots"] if b.get("obedece") is None and b["bot"] in _CANON]
    if duvida:
        print(f"    POR ESCLARECER (a lista canonica nao confirma obediencia): {', '.join(duvida)}")
    if r.get("bots_novos"):
        print(f"\n  BOTS DE OPERADORES QUE IMPORTAM e que a tua tabela ainda NAO cobre ({len(r['bots_novos'])}):")
        for b in r["bots_novos"]:
            op = str(_CANON[b].get("operator", "?")).split("]")[0].lstrip("[")
            fn = str(_CANON[b].get("function", "?"))[:58]
            print(f"    {b:<28} {op:<12} {fn}")
    lt, lf = r["llms_txt"], r["llms_full_txt"]
    print(f"\n  llms.txt: HTTP {lt['status']} ({lt['bytes']} bytes)   llms-full.txt: HTTP {lf['status']}")
    print("    peso ZERO para Google Search (guia oficial da Google). Reportar, nunca prometer.")
    h = r["home"]
    if "erro" not in h:
        print(f"\n  HOMEPAGE\n    title: {h['title'][:80] or '(vazio)'}")
        print(f"    meta description: {(h['meta_description'][:80] + '...') if h['meta_description'] else 'VAZIA'}")
        print(f"    JSON-LD: {', '.join(h['jsonld_tipos']) if h['jsonld_tipos'] else 'NENHUM'}")
        print(f"    h1: {h['h1']}  h2: {h['h2']}  palavras visiveis: {h['palavras_visiveis']}  html: {h['bytes_html']} bytes")
        if h["suspeita_csr"]:
            print("    AVISO: pouco texto para muito HTML. Suspeita de render no cliente.")
            print("           Crawlers de IA nao executam JavaScript.")


def main():
    argv, args, saida, salta = sys.argv[1:], [], None, False
    for i, a in enumerate(argv):
        if salta:
            salta = False
            continue
        if a == "--json":
            saida = argv[i + 1] if i + 1 < len(argv) else None
            salta = True
        elif not a.startswith("--"):
            args.append(a)
    if not args:
        print(__doc__)
        return 2
    res = []
    for alvo in args:
        try:
            r = audita(alvo)
            res.append(r)
            imprime(r)
        except Exception as e:
            print(f"  {alvo}: FALHOU ({e})")
    if saida and res:
        with open(saida, "w", encoding="utf-8") as f:
            json.dump(res, f, ensure_ascii=False, indent=2)
        print(f"\n  JSON: {saida}")
    return 0 if res else 1


if __name__ == "__main__":
    sys.exit(main())
