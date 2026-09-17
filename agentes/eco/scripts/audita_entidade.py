#!/usr/bin/env python3
"""O Eco - vigia da entidade no Wikidata.

Porque existe: um modelo generativo que nao sabe distinguir a tua marca de uma homonima (uma
cidade, um instrumento, outra empresa com o mesmo nome) tende a responder sobre a coisa errada.
Isto explica confusoes que parecem aleatorias: quando um modelo procura "quem somos", encontra
o que o grafo de conhecimento tiver, certo ou nao.

Porque nao usamos um MCP de Wikidata generico: esses fazem search e SPARQL avulsos. O que este
script precisa e outra coisa: vigiar a MESMA pergunta ao longo do tempo, para a tua marca e para
os concorrentes que escolheres, e assinalar quando algo mudar. Isso e serie temporal, nao consulta.

Stdlib apenas. Nao escreve no Wikidata: escrever la e acto publico e irreversivel, decide-se por
fora deste script.

Configuracao: cria `entidades.json` ao lado deste script (ver `entidades.example.json`), com:
  {"nossos": ["A tua marca", "A tua empresa-mae, se aplicavel"],
   "concorrentes": ["Concorrente 1", "Concorrente 2"],
   "ancora": {"nome": "Uma entidade da tua industria que ja exista no Wikidata", "qid": "Q..."}}
A ancora e opcional: e uma entidade grande e ja notoria do teu sector, a que a tua possa ligar-se
por sameAs quando existir (reduz o trabalho de te desambiguares sozinho).

Uso:  python3 audita_entidade.py [--config entidades.json] [--json baseline/entidade-DATA.json]
"""
import json
import sys
import urllib.parse
import urllib.request
from datetime import date
from pathlib import Path

API = "https://www.wikidata.org/w/api.php"
UA = "EcoGEO/1.0 (auditoria de entidade)"

# Sinais de que um resultado NAO e o teu. Se todos os resultados baterem aqui, o nome esta ocupado
# por outra coisa (uma cidade, um objecto, uma pagina de desambiguacao...). Ajusta a lista ao teu
# caso: estes sao genericos, os teus falsos positivos podem ser outros.
SINAIS_ALHEIOS = ("desambigua", "human settlement", "wikimedia", "instrumento musical",
                  "município", "municipio", "aldeia", "vila", "rio", "montanha")


def carrega_config(caminho):
    p = Path(caminho)
    if not p.exists():
        print(f"AVISO: '{caminho}' não existe. Copia 'entidades.example.json' para '{caminho}' e"
              f" preenche com a tua marca, os teus concorrentes e (opcional) uma âncora do sector.")
        return {"nossos": [], "concorrentes": [], "ancora": None}
    with p.open(encoding="utf-8") as f:
        d = json.load(f)
    d.setdefault("nossos", [])
    d.setdefault("concorrentes", [])
    d.setdefault("ancora", None)
    return d


def consulta(termo, lingua="pt", limite=8):
    q = urllib.parse.urlencode({
        "action": "wbsearchentities", "search": termo, "language": lingua,
        "uselang": lingua, "format": "json", "limit": limite,
    })
    req = urllib.request.Request(f"{API}?{q}", headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.load(r).get("search", []), None
    except Exception as e:
        return None, str(e)


def classifica(resultados):
    """Quatro estados. A consulta falhada nao e 'nao existe', e a descricao vazia nao e 'e teu'.

    Ausencia de informacao nunca conta como prova a favor: um resultado sem descricao nao entra
    na conta nem a favor, nem contra.
    """
    if resultados is None:
        return "NAO VERIFICADO"
    if not resultados:
        return "AUSENTE"
    candidatas = 0
    for r in resultados:
        desc = (r.get("description") or "").strip()
        if not desc:
            continue
        texto = f"{r.get('label','')} {desc}".lower()
        if not any(s in texto for s in SINAIS_ALHEIOS):
            candidatas += 1
    if candidatas:
        return "TALVEZ TEU"   # candidata a confirmar a olho, nunca automatico
    return "NOME OCUPADO"


def main():
    argv = sys.argv[1:]
    saida, config = None, "entidades.json"
    i = 0
    while i < len(argv):
        if argv[i] == "--json" and i + 1 < len(argv):
            saida = argv[i + 1]; i += 2
        elif argv[i] == "--config" and i + 1 < len(argv):
            config = argv[i + 1]; i += 2
        else:
            i += 1

    cfg = carrega_config(config)
    if not cfg["nossos"]:
        return 2

    r = {"data": date.today().isoformat(), "nossos": {}, "concorrentes": {}, "ancora": {}}
    print(f"\n{'='*70}\n  ENTIDADE NO WIKIDATA   {r['data']}\n{'='*70}")

    print("\n  A TUA MARCA")
    for t in cfg["nossos"]:
        res, err = consulta(t)
        est = classifica(res)
        r["nossos"][t] = {"estado": est, "erro": err,
                          "resultados": [{"id": x["id"], "label": x.get("label"),
                                          "desc": x.get("description")} for x in (res or [])]}
        print(f"    {t:<22} {est}")
        for x in (res or [])[:4]:
            print(f"        {x['id']:<11} {x.get('label','')} | {(x.get('description') or '(sem descricao)')[:52]}")

    if cfg["concorrentes"]:
        print("\n  CONCORRENTES")
        for t in cfg["concorrentes"]:
            res, err = consulta(t)
            est = classifica(res)
            r["concorrentes"][t] = {"estado": est, "erro": err, "n": len(res or [])}
            print(f"    {t:<22} {est}")

    if cfg.get("ancora"):
        nome, qid = cfg["ancora"]["nome"], cfg["ancora"]["qid"]
        res, err = consulta(nome)
        tem = any(x["id"] == qid for x in (res or []))
        r["ancora"] = {"nome": nome, "qid": qid, "existe": tem, "erro": err}
        print(f"\n  ÂNCORA\n    {nome} ({qid}): {'existe' if tem else 'NAO ENCONTRADA'}")

    ocupados = [t for t, v in r["nossos"].items() if v["estado"] == "NOME OCUPADO"]
    ausentes = [t for t, v in r["nossos"].items() if v["estado"] == "AUSENTE"]
    conc_com = [t for t, v in r["concorrentes"].items() if v["estado"] == "TALVEZ TEU"]
    print(f"\n{'-'*70}\n  VEREDICTO")
    if ocupados:
        print(f"    NOME OCUPADO por entidades alheias: {', '.join(ocupados)}")
        print("    Um modelo que procure quem és encontra outra coisa. Isto nao se resolve com")
        print("    conteudo no teu site: resolve-se com entidade propria e sameAs.")
    if ausentes:
        print(f"    SEM ENTIDADE NENHUMA: {', '.join(ausentes)}")
    if conc_com:
        print(f"    ATENCAO: concorrentes que podem ja ter entidade: {', '.join(conc_com)}")
    elif cfg["concorrentes"]:
        print("    Nenhum concorrente tem entidade. O terreno esta vazio para todos.")
    if r.get("ancora", {}).get("existe"):
        nome, qid = r["ancora"]["nome"], r["ancora"]["qid"]
        print(f"    Âncora disponível: ligar a tua entidade a {qid} ({nome}) dá-te apoio")
        print("    num item que já é notório, em vez de nasceres isolado.")
    print(f"{'-'*70}")

    if saida:
        Path(saida).parent.mkdir(parents=True, exist_ok=True)
        with open(saida, "w", encoding="utf-8") as f:
            json.dump(r, f, ensure_ascii=False, indent=1)
        print(f"  JSON: {saida}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
