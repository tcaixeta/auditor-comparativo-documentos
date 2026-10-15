#!/usr/bin/env python3
"""Extrai o texto de um documento com localizadores rastreáveis.

Uso:
    python extrair_documento.py <arquivo> --id DOC-A [--saida extraido_DOC-A.md]

Formatos:
    .pdf   uma seção por página física:  === DOC-A · Página N ===
    .docx  parágrafos numerados [par. N], tabelas na ordem em que aparecem
           ([Tabela T, linha L, col. C]), alterações controladas visíveis,
           comentários, cabeçalhos e rodapés em seções próprias
    .txt / .md   blocos separados por linha em branco viram [par. N]

Dependências: pypdf (PDF) e python-docx (DOCX).
    pip install pypdf python-docx

O texto extraído é a base de todas as citações e localizadores da análise.
Guarde o arquivo de saída: ele também é usado por verificar_citacoes.py.
"""
import argparse
import re
import sys
import zipfile
from pathlib import Path

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def norm(s):
    return re.sub(r"[ \t]+", " ", s).strip()


# ---------------------------------------------------------------- PDF
def extrair_pdf(path, doc_id):
    try:
        from pypdf import PdfReader
    except ImportError:
        sys.exit("pypdf não instalado: pip install pypdf (ou use a skill pdf e siga o mesmo formato de marcadores)")
    reader = PdfReader(str(path))
    out, avisos = [], []
    for i, page in enumerate(reader.pages, 1):
        texto = page.extract_text() or ""
        out.append(f"=== {doc_id} · Página {i} ===")
        if len(texto.strip()) < 20:
            avisos.append(i)
            out.append("[SEM TEXTO EXTRAÍVEL — provável página escaneada: aplicar OCR ou marcar como REQUER REVISÃO]")
        out.append(texto.strip())
        out.append("")
    cab = [f"# {doc_id} — {path.name}", f"Formato: PDF · {len(reader.pages)} páginas físicas (1ª página do arquivo = 1).",
           "Localizador: página FÍSICA. Se o rodapé impresso numerar diferente (ex.: capa sem número), registre as duas no inventário."]
    if avisos:
        cab.append(f"ATENÇÃO: páginas sem texto extraível: {avisos}")
    meta = reader.metadata or {}
    if meta:
        cab.append("Metadados do arquivo (não são conteúdo): " + "; ".join(f"{k.strip('/')}={v}" for k, v in meta.items() if v))
    return "\n".join(cab + ["", *out])


# ---------------------------------------------------------------- DOCX
def texto_paragrafo(p):
    """Texto aceito (inserções incluídas, exclusões fora) + lista de mudanças controladas."""
    partes, mudancas = [], []
    for el in p.iter():
        tag = el.tag
        if tag == W + "t":
            partes.append(el.text or "")
        elif tag == W + "tab":
            partes.append("\t")
        elif tag in (W + "br", W + "cr"):
            partes.append("\n")
    for ins in p.iter(W + "ins"):
        t = "".join(x.text or "" for x in ins.iter(W + "t"))
        if t:
            mudancas.append(("INSERIDO", t, ins.get(W + "author"), ins.get(W + "date")))
    for de in p.iter(W + "del"):
        t = "".join(x.text or "" for x in de.iter(W + "delText"))
        if t:
            mudancas.append(("EXCLUÍDO", t, de.get(W + "author"), de.get(W + "date")))
    return norm("".join(partes)), mudancas


def extrair_docx(path, doc_id):
    try:
        import docx  # noqa: F401
        from docx import Document
    except ImportError:
        sys.exit("python-docx não instalado: pip install python-docx (ou use a skill docx e siga o mesmo formato)")
    d = Document(str(path))
    body = d.element.body
    out, mudancas, n_par, n_tab, ultimo_par = [], [], 0, 0, 0
    for el in body.iterchildren():
        if el.tag == W + "p":
            n_par += 1
            ultimo_par = n_par
            t, m = texto_paragrafo(el)
            out.append(f"[par. {n_par}] {t}")
            mudancas += [(n_par, *x) for x in m]
        elif el.tag == W + "tbl":
            n_tab += 1
            out.append(f"[Tabela {n_tab} — após par. {ultimo_par}]")
            for li, tr in enumerate(el.iter(W + "tr"), 1):
                for ci, tc in enumerate(tr.iter(W + "tc"), 1):
                    t = norm(" ".join(texto_paragrafo(p)[0] for p in tc.iter(W + "p")))
                    out.append(f"  [Tabela {n_tab}, linha {li}, col. {ci}] {t}")
    cab = [f"# {doc_id} — {path.name}",
           f"Formato: DOCX · {n_par} parágrafos de corpo · {n_tab} tabela(s). Sem paginação fixa.",
           "Localizador: numeração própria + [par. N]. Regra de contagem: todo parágrafo do corpo, em ordem, a partir de 1, "
           "incluindo títulos e parágrafos vazios; tabelas fora da contagem, com localizador próprio."]
    extra = []
    if mudancas:
        extra += ["", "## Alterações controladas (track changes) — evidência direta do que mudou"]
        extra += [f"- par. {p}: {tipo} \"{t}\" (autor: {a or '?'}; data: {dt or '?'})" for p, tipo, t, a, dt in mudancas]
        cab.append(f"ATENÇÃO: {len(mudancas)} alteração(ões) controlada(s). O texto acima é a versão com inserções aceitas e exclusões removidas.")
    else:
        cab.append("Alterações controladas: nenhuma.")
    # comentários
    with zipfile.ZipFile(str(path)) as z:
        if "word/comments.xml" in z.namelist():
            from lxml import etree
            root = etree.fromstring(z.read("word/comments.xml"))
            coms = root.findall(W + "comment")
            if coms:
                extra += ["", "## Comentários do documento (contexto, não conteúdo normativo)"]
                for c in coms:
                    t = norm(" ".join(x.text or "" for x in c.iter(W + "t")))
                    extra.append(f"- Comentário {c.get(W + 'id')} ({c.get(W + 'author')}): {t}")
    # cabeçalhos e rodapés
    hf = []
    for si, s in enumerate(d.sections, 1):
        for nome, parte in (("cabeçalho", s.header), ("rodapé", s.footer)):
            t = norm(" ".join(p.text for p in parte.paragraphs))
            if t:
                hf.append(f"- Seção {si}, {nome}: {t}")
    if hf:
        extra += ["", "## Cabeçalhos e rodapés"] + hf
    cp = d.core_properties
    cab.append(f"Metadados do arquivo (não são conteúdo): title={cp.title!r}; author={cp.author!r}; created={cp.created}; modified={cp.modified}")
    return "\n".join(cab + ["", *out, *extra])


# ---------------------------------------------------------------- TXT/MD
def extrair_texto(path, doc_id):
    blocos = [norm(b) for b in re.split(r"\n\s*\n", path.read_text(encoding="utf-8", errors="replace")) if b.strip()]
    cab = [f"# {doc_id} — {path.name}", f"Formato: texto · {len(blocos)} blocos.",
           "Localizador: numeração própria do texto + [par. N] (blocos separados por linha em branco). Sem paginação."]
    return "\n".join(cab + [""] + [f"[par. {i}] {b}" for i, b in enumerate(blocos, 1)])


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("arquivo")
    ap.add_argument("--id", required=True, help="identificador do documento, ex.: DOC-A")
    ap.add_argument("--saida", help="arquivo de saída (padrão: extraido_<ID>.md ao lado do original)")
    a = ap.parse_args()
    path = Path(a.arquivo)
    ext = path.suffix.lower()
    if ext == ".pdf":
        txt = extrair_pdf(path, a.id)
    elif ext == ".docx":
        txt = extrair_docx(path, a.id)
    elif ext in (".txt", ".md"):
        txt = extrair_texto(path, a.id)
    else:
        sys.exit(f"Formato não suportado: {ext}. Converta para PDF, DOCX ou TXT.")
    saida = Path(a.saida) if a.saida else path.with_name(f"extraido_{a.id}.md")
    saida.write_text(txt, encoding="utf-8")
    print(f"OK: {saida}")


if __name__ == "__main__":
    main()
