#!/usr/bin/env python3
"""Confere mecanicamente todo trecho entre aspas de uma análise contra o texto extraído.

Uso:
    python verificar_citacoes.py analise.md --doc DOC-A=extraido_DOC-A.md --doc DOC-B=extraido_DOC-B.md

Os arquivos --doc são as saídas de extrair_documento.py. Para cada trecho entre aspas
(“...” ou "..."), o script:
  1. identifica o documento (último DOC-X antes do trecho) e o localizador
     (p. N / página N, par. N ou par. N–M, Tabela T, linha L) — antes do trecho ou logo depois;
  2. confere se o texto existe, caractere por caractere (espaços normalizados), no localizador;
  3. classifica: OK, OK_SEM_LOCALIZADOR, LOCALIZADOR_DIVERGENTE, DOC_DIVERGENTE, NAO_ENCONTRADA.
Cortes com [...], [...] ou ... são aceitos: cada parte precisa existir no mesmo localizador.
Ênfase markdown dentro da citação (**negrito**) é ignorada.
Texto em `código` e blocos ``` são ignorados (termos de busca e rótulos não são citações).

Saída: relatório no terminal. Código de saída 1 se houver NAO_ENCONTRADA, DOC_DIVERGENTE
(o texto existe, mas em outro documento) ou LOCALIZADOR_DIVERGENTE.
Cada problema precisa ser tratado conforme a seção de verificação da skill: corrigir o localizador,
substituir pela citação literal, transformar em paráfrase sem aspas, ou rebaixar o achado para REV.
"""
import argparse
import re
import sys
from collections import Counter

norm = lambda s: re.sub(r"\s+", " ", s).strip()
QUOTE = re.compile(r"“([^”]+)”|\"([^\"\n]+)\"")
DOCRE = re.compile(r"DOC-([A-Z0-9]+)")
LOCS = [
    ("pag", re.compile(r"\bp(?:ág(?:ina)?|\.)\s?(?:física\s)?(\d+)", re.I)),
    ("par", re.compile(r"\bpar\.\s?(\d+)(?:\s?[–-]\s?(\d+))?")),
    ("tab", re.compile(r"Tabela\s(\d+),?\s+linha\s(\d+)")),
]


def carregar(path):
    """Lê a saída de extrair_documento.py e indexa por página, parágrafo e célula."""
    pag, par, tab, cur = {}, {}, {}, None
    linhas = open(path, encoding="utf-8").read().splitlines()
    buf = []
    for ln in linhas:
        m = re.match(r"=== .* · Página (\d+) ===", ln)
        if m:
            if cur is not None:
                pag[cur] = norm(" ".join(buf))
            cur, buf = int(m.group(1)), []
            continue
        if cur is not None:
            buf.append(ln)
        m = re.match(r"\[par\. (\d+)\] (.*)", ln)
        if m:
            par[int(m.group(1))] = norm(m.group(2))
        m = re.match(r"\s*\[Tabela (\d+), linha (\d+), col\. (\d+)\] (.*)", ln)
        if m:
            tab.setdefault((int(m.group(1)), int(m.group(2))), []).append(norm(m.group(4)))
    if cur is not None:
        pag[cur] = norm(" ".join(buf))
    tudo = norm(" ".join(linhas))
    return {"pag": pag, "par": par, "tab": {k: " ".join(v) for k, v in tab.items()}, "tudo": tudo}


def onde(doc, partes):
    """Lista de localizadores onde todas as partes ocorrem."""
    achados = []
    for p, t in doc["pag"].items():
        if all(x in t for x in partes):
            achados.append(f"p. {p}")
    for p, t in doc["par"].items():
        if all(x in t for x in partes):
            achados.append(f"par. {p}")
    for (t, l), txt in doc["tab"].items():
        if all(x in txt for x in partes):
            achados.append(f"Tabela {t}, linha {l}")
    return achados


def localizadores(trecho, do_fim=True):
    """Localizadores presentes no trecho, do mais próximo da citação para o mais distante."""
    achados = [(tipo, m.groups(), m.start()) for tipo, rx in LOCS for m in rx.finditer(trecho)]
    return sorted(achados, key=lambda x: x[2], reverse=do_fim)


def confere(doc, loc, partes):
    tipo, g, _ = loc
    if tipo == "pag":
        txt = doc["pag"].get(int(g[0]), "")
    elif tipo == "par":
        a = int(g[0]); b = int(g[1]) if g[1] else a
        txt = " ".join(doc["par"].get(i, "") for i in range(a, b + 1))
    else:
        txt = doc["tab"].get((int(g[0]), int(g[1])), "")
    return bool(txt) and all(x in txt for x in partes), bool(txt)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("analise")
    ap.add_argument("--doc", action="append", required=True, help="DOC-X=arquivo_extraido.md")
    ap.add_argument("--todos", action="store_true", help="lista também as citações OK")
    a = ap.parse_args()
    docs = {}
    for d in a.doc:
        k, v = d.split("=", 1)
        docs[k.replace("DOC-", "")] = carregar(v)

    res, cont = [], Counter()
    em_bloco = False
    for n, linha in enumerate(open(a.analise, encoding="utf-8"), 1):
        if linha.strip().startswith("```"):
            em_bloco = not em_bloco
            continue
        if em_bloco:
            continue
        limpa = re.sub(r"`[^`]*`", lambda m: " " * len(m.group(0)), linha)
        ms = list(QUOTE.finditer(limpa))
        for i, m in enumerate(ms):
            q = m.group(1) or m.group(2)
            q_limpa = re.sub(r"\*\*|__|(?<!\w)\*|\*(?!\w)", "", q)  # ênfase markdown não altera o texto
            partes = [norm(x) for x in re.split(r"\[\s?(?:\.\.\.|…)\s?\]|…|\.\.\.", q_limpa) if norm(x)]
            if not partes:
                continue
            prefixo = limpa[:m.start()]
            depois = limpa[m.end():(ms[i + 1].start() if i + 1 < len(ms) else len(limpa))][:45]
            dm = list(DOCRE.finditer(prefixo))
            doc_id = dm[-1].group(1) if dm else None
            # contexto: do último DOC-X citado até a citação (ou a linha inteira, se não houver DOC-X)
            ctx = prefixo[dm[-1].end():] if dm else prefixo
            candidatos = localizadores(depois, do_fim=False) + localizadores(ctx)
            alvo = [doc_id] if doc_id in docs else list(docs)
            presentes = {k: onde(docs[k], partes) for k in alvo}
            if not any(all(x in docs[k]["tudo"] for x in partes) for k in docs):
                st, det = "NAO_ENCONTRADA", ""
            elif doc_id in docs and not all(x in docs[doc_id]["tudo"] for x in partes):
                outros = [f"DOC-{k}" for k in docs if all(x in docs[k]["tudo"] for x in partes)]
                st, det = "DOC_DIVERGENTE", f"não está em DOC-{doc_id}; está em {', '.join(outros)}"
            elif candidatos:
                # aceita se algum localizador candidato confirma o trecho no documento indicado
                # (ou em qualquer documento, quando a linha cita mais de um)
                ordem = ([doc_id] if doc_id in docs else []) + [k for k in docs if k != doc_id]
                if any(confere(docs[k], c, partes)[0] for c in candidatos for k in ordem):
                    st, det = "OK", ""
                else:
                    st = "LOCALIZADOR_DIVERGENTE"
                    det = f"está em: {', '.join(presentes.get(doc_id) or ['(só no texto corrido)']) if doc_id in docs else presentes}"
            else:
                st, det = "OK_SEM_LOCALIZADOR", f"encontrada em DOC-{'/'.join(k for k in alvo if presentes[k] or all(x in docs[k]['tudo'] for x in partes))}"
            cont[st] += 1
            res.append((n, st, f"DOC-{doc_id}" if doc_id else "?", q, det))

    print(f"Trechos entre aspas conferidos: {sum(cont.values())}")
    for k in ("OK", "OK_SEM_LOCALIZADOR", "LOCALIZADOR_DIVERGENTE", "DOC_DIVERGENTE", "NAO_ENCONTRADA"):
        print(f"  {k}: {cont[k]}")
    problemas = [r for r in res if r[1] in ("NAO_ENCONTRADA", "LOCALIZADOR_DIVERGENTE", "DOC_DIVERGENTE")]
    if problemas:
        print("\nPROBLEMAS (tratar antes de entregar):")
        for n, st, d, q, det in problemas:
            print(f"  L{n} [{st}] {d}: “{q[:90]}” {det}")
    if a.todos:
        print("\nTODOS:")
        for n, st, d, q, det in res:
            print(f"  L{n} [{st}] {d}: “{q[:70]}” {det}")
    print("\nOK_SEM_LOCALIZADOR: o texto existe, mas o localizador não foi identificado automaticamente; "
          "confira manualmente os que sustentam achados.")
    sys.exit(1 if problemas else 0)


if __name__ == "__main__":
    main()
