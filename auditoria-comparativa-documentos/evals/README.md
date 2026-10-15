# Testes da skill auditoria-comparativa-documentos

Esta pasta não entra no pacote instalado (o empacotador exclui `evals/`).

## Conteúdo

| Caminho | O quê |
|---|---|
| `files/DOC-A_contrato_v1.pdf` | Contrato fictício v1.0 — 7 páginas, capa sem número (página física = impressa + 1) |
| `files/DOC-B_contrato_v2.docx` | Mesmo contrato v2.0, com 9 diferenças plantadas e 3 armadilhas |
| `gabarito/gabarito-v3.xlsx` | Gabarito (aba Gabarito), avaliação por execução e scorecard automático. **Nunca enviar para a IA avaliada.** |
| `referencias/Execucao1.md` … `Execucao8.md` | As 8 execuções do desenvolvimento da persona, que deu origem à skill |
| `evals.json` | Casos de teste da skill-creator, com as expectativas |

## Histórico das execuções de referência

| Execuções | Versão da persona | O que mostraram |
|---|---|---|
| 1 e 2 | Inicial (verificação de citações, três estados) | 9/9 diferenças, mas 4 trechos não literais entre aspas na Análise, tipos variando entre execuções, contradição interna fundida com a mudança entre versões, equivalências e problemas comuns como achados |
| 3 e 4 | + aspas literais em toda seção, regras de desempate, unidade do achado, achado × observação, parágrafo no DOCX | 100%; restaram severidade instável, data do instrumento tratada de forma diferente, itens com achado listados como convergentes |
| 5 e 6 | + âncoras de severidade, regra para versão/data, exclusividade achado × convergência, termos em código | 100%, severidade 9/9 nas duas; a Execução 5 duplicou REF e TER |
| 7 e 8 | **v1.0** = conteúdo desta skill (regra de unidade refinada) | 100%; mesmos 10 achados, na mesma ordem, com a mesma classificação nas duas — **padrão de referência** |

## Teste de regressão do verificador de citações

O verificador precisa continuar acusando os problemas das primeiras rodadas e não acusar a v1.0:

```bash
python scripts/extrair_documento.py evals/files/DOC-A_contrato_v1.pdf --id DOC-A --saida /tmp/A.md
python scripts/extrair_documento.py evals/files/DOC-B_contrato_v2.docx --id DOC-B --saida /tmp/B.md
for n in 1 2 7; do python scripts/verificar_citacoes.py evals/referencias/Execucao$n.md --doc DOC-A=/tmp/A.md --doc DOC-B=/tmp/B.md | head -6; done
```

Esperado: Execuções 1 e 2 com várias `NAO_ENCONTRADA` (por exemplo, “até o 5º dia útil” e “medida cabível”); Execução 7 com zero problemas.
