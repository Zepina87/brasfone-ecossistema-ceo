#!/usr/bin/env python3
"""O Eco - gera o JSON-LD que falta as tuas superficies.

Porque existe: uma auditoria tipica encontra zero JSON-LD e meta description vazia numa marca de
campanha, e so LocalBusiness/WebSite na marca principal. Faltam Organization, Service e FAQPage,
e escreve-los a mao repete sempre a mesma estrutura.

A entidade canonica (nome, descricao, tier de parceria, relacao entre marcas) e um FACTO do
negocio, nunca se inventa aqui: fixa-se uma vez em `entidades.json` (ver `entidades.example.json`)
e so se altera por decisao de quem manda nisso.

Uso:  python3 gera_jsonld.py organization <chave>
      python3 gera_jsonld.py faq perguntas.json
      python3 gera_jsonld.py service --nome "..." --descricao "..." [--entidade <chave>]
Saida: JSON-LD pronto a colar, ja dentro de <script type="application/ld+json">.
"""
import argparse
import json
import sys
from pathlib import Path


def carrega_entidades(caminho="entidades.json"):
    p = Path(caminho)
    if not p.exists():
        sys.exit(f"Falta '{caminho}'. Copia 'entidades.example.json' para '{caminho}' e preenche "
                  f"com a tua marca (nome, url, descricao, area servida, sameAs).")
    with p.open(encoding="utf-8") as f:
        return json.load(f)


def organization(entidades, chave, wikidata=None, wikidata_mae=None):
    """`wikidata` e `wikidata_mae` sao QIDs (ex. Q123). So existem no dia em que a entidade
    existir no Wikidata; ate la o comportamento e o de sempre. Um sameAs para o Wikidata e o
    sinal de desambiguacao mais forte que um JSON-LD pode dar: diz ao motor QUAL "tua marca"
    tu es, quando o nome no grafo aponta para outra coisa qualquer (uma cidade, um objecto,
    outra empresa homonima)."""
    if chave not in entidades:
        sys.exit(f"Entidade '{chave}' não está em entidades.json. Chaves disponíveis: {sorted(entidades)}")
    e = entidades[chave]
    d = {
        "@context": "https://schema.org",
        "@type": "Organization",
        "name": e["name"],
        "url": e["url"],
        "description": e["description"],
        "areaServed": e.get("areaServed", []),
        "sameAs": e.get("sameAs", []),
    }
    if e.get("slogan"):
        d["slogan"] = e["slogan"]
    if e.get("knowsAbout"):
        d["knowsAbout"] = e["knowsAbout"]
    if e.get("logo"):
        d["logo"] = e["logo"]
    if wikidata:
        d["sameAs"] = [*d["sameAs"], f"https://www.wikidata.org/wiki/{wikidata}"]
    if e.get("parentOrganization"):
        mae = dict(e["parentOrganization"])
        if wikidata_mae:
            mae["sameAs"] = [*mae.get("sameAs", []), f"https://www.wikidata.org/wiki/{wikidata_mae}"]
        d["parentOrganization"] = {"@type": "Organization", **mae}
    return d


def service(entidades, nome, descricao, entidade):
    if entidade not in entidades:
        sys.exit(f"Entidade '{entidade}' não está em entidades.json.")
    e = entidades[entidade]
    return {
        "@context": "https://schema.org",
        "@type": "Service",
        "name": nome,
        "description": descricao,
        "provider": {"@type": "Organization", "name": e["name"], "url": e["url"]},
        "areaServed": e.get("areaServed", []),
        "serviceType": nome,
    }


def faq(pares):
    """pares: lista de {"pergunta": ..., "resposta": ...}.

    A resposta cabe idealmente em 134 a 167 palavras e responde nas primeiras 40 a 60 (é a forma
    que mais se cita, por estudo de terceiro sobre extraccao de respostas por IA). O script avisa
    quando sai fora, porque e esse o ponto de escrever FAQ para ser citada.
    """
    itens, avisos = [], []
    for i, p in enumerate(pares, 1):
        n = len(p["resposta"].split())
        if n < 40:
            avisos.append(f"  pergunta {i}: resposta com {n} palavras, curta demais para ser citada (alvo 134 a 167)")
        elif n > 200:
            avisos.append(f"  pergunta {i}: resposta com {n} palavras, longa demais para extraccao limpa (alvo 134 a 167)")
        itens.append({
            "@type": "Question",
            "name": p["pergunta"],
            "acceptedAnswer": {"@type": "Answer", "text": p["resposta"]},
        })
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": itens}, avisos


def imprime(d, avisos=None):
    print('<script type="application/ld+json">')
    print(json.dumps(d, ensure_ascii=False, indent=2))
    print("</script>")
    if avisos:
        print("\nAVISOS de citabilidade:", file=sys.stderr)
        for a in avisos:
            print(a, file=sys.stderr)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--entidades-json", default="entidades.json", help="ficheiro de configuração das tuas marcas")
    sub = ap.add_subparsers(dest="cmd", required=True)

    o = sub.add_parser("organization", help="Organization para uma das tuas marcas")
    o.add_argument("entidade", help="chave em entidades.json")
    o.add_argument("--wikidata", metavar="QID", help="QID da entidade no Wikidata, quando existir (ex. Q123456)")
    o.add_argument("--wikidata-mae", metavar="QID", help="QID da empresa-mãe no Wikidata, para o parentOrganization")

    s = sub.add_parser("service", help="Service prestado por uma das tuas marcas")
    s.add_argument("--nome", required=True)
    s.add_argument("--descricao", required=True)
    s.add_argument("--entidade", required=True, help="chave em entidades.json")

    f = sub.add_parser("faq", help="FAQPage a partir de um JSON com pergunta e resposta")
    f.add_argument("ficheiro", help='JSON: [{"pergunta": "...", "resposta": "..."}]')

    a = ap.parse_args()
    if a.cmd == "faq":
        with open(a.ficheiro, encoding="utf-8") as fh:
            pares = json.load(fh)
        d, avisos = faq(pares)
        imprime(d, avisos)
        return 0

    entidades = carrega_entidades(a.entidades_json)
    if a.cmd == "organization":
        imprime(organization(entidades, a.entidade, a.wikidata, a.wikidata_mae))
    else:
        imprime(service(entidades, a.nome, a.descricao, a.entidade))
    return 0


if __name__ == "__main__":
    sys.exit(main())
