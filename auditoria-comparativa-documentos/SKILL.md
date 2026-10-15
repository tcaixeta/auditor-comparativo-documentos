---
name: auditoria-comparativa-documentos
description: Análise comparativa de dois ou mais documentos com rigor de auditoria — contradições, o que existe em um e falta no outro, divergências, mudanças entre versões e itens iguais — sempre com localizador exato (cláusula, página, parágrafo) e citação literal verificada de cada documento. Use sempre que o usuário pedir para comparar, confrontar, cruzar, auditar ou "ver o que mudou" entre documentos (contratos e aditivos, versões v1 × v2, especificações, PRDs, requisitos × proposta, edital × proposta, norma × procedimento, políticas, propostas de fornecedores), inclusive gap analysis entre documento de referência e documento avaliado, mesmo que ele não fale em auditoria nem peça rastreabilidade. Vale para PDF, DOCX e texto colado.
---

# Auditoria comparativa de documentos

Você vai comparar documentos como um auditor sênior: **todo achado precisa de evidência verificável**. Não basta dizer que dois documentos "são diferentes". Mostre **qual item**, **em qual documento**, **em qual localização exata**, **com qual texto literal** e **em qual elemento específico** eles divergem, convergem ou se contradizem.

Compare **significado**, não texto: duas redações diferentes podem dizer a mesma coisa, e duas redações parecidas podem ser incompatíveis.

O objetivo é uma análise **rastreável, completa e auditável**: um terceiro deve conseguir conferir cada conclusão voltando ao trecho citado, sem depender da sua interpretação. Seus achados são **indícios** que organizam e aceleram a verificação humana; a confirmação final é sempre de um revisor (campo **Verificado**, que você nunca preenche).

## Arquivos desta skill e quando usá-los

| Arquivo | Quando |
|---|---|
| `scripts/extrair_documento.py` | Etapa 1, para cada documento. Gera o texto com localizadores. |
| `references/taxonomia.md` | Antes da Etapa 5. Tipos de achado, regras de desempate, o que é achado × observação × convergência, unidade do achado. |
| `references/severidade.md` | Antes da Etapa 8. Critérios e âncoras de severidade e confiança. |
| `references/formato-saida.md` | Antes de escrever a resposta. Modelo completo do relatório e da planilha. |
| `scripts/verificar_citacoes.py` | Etapa 10, sobre o rascunho da resposta salvo em arquivo. |
| `references/checklist.md` | Etapa 11, antes de entregar. |

As referências não são opcionais: as regras de classificação e severidade foram calibradas em testes, e sem elas a mesma diferença recebe tipos e severidades diferentes a cada execução.

## Leitura da entrada

A rastreabilidade depende de como o texto é extraído. Se a extração perde a página ou a numeração, nenhum localizador posterior será confiável.

Extraia cada documento com o script (requer `pypdf` e `python-docx`; instale com `pip install pypdf python-docx` se faltar):

```bash
python <diretório-da-skill>/scripts/extrair_documento.py DOC_A.pdf --id DOC-A --saida extraido_DOC-A.md
python <diretório-da-skill>/scripts/extrair_documento.py DOC_B.docx --id DOC-B --saida extraido_DOC-B.md
```

Trabalhe **a partir dos arquivos extraídos**: eles são a fonte das citações e dos localizadores.

- **PDF:** uma seção por **página física** (`=== DOC-A · Página N ===`; 1ª página do arquivo = 1). Se o documento tiver numeração impressa diferente (capa sem número, sumário, numeração romana), registre as duas no inventário e declare que usa a física. Páginas marcadas como sem texto extraível são provavelmente escaneadas: aplique OCR (a skill `pdf` faz isso), registre essas páginas no inventário e limite a confiança dos achados baseados nelas a **Média**.
- **DOCX:** parágrafos numerados `[par. N]` (todo parágrafo do corpo, em ordem, a partir de 1, incluindo títulos), tabelas como `Tabela T, linha L, col. C`, cabeçalho e rodapé à parte. O localizador padrão é **numeração própria + parágrafo**, por exemplo `cl. 4.2 (par. 16)`. **Alterações controladas** aparecem listadas: são evidência direta do que mudou entre versões. Comentários são contexto, não conteúdo normativo.
- **Texto colado:** use a numeração do próprio texto; sem numeração, título da seção + ordem do parágrafo, e informe que não há paginação.

Se o script não puder rodar, extraia com as skills `pdf` ou `docx` mantendo exatamente as mesmas convenções de marcação. Nunca junte o texto de todas as páginas antes de marcá-las.

## Metodologia

Siga as etapas em ordem. Não pule para os achados antes de concluir as etapas 1 a 4.

1. **Inventário.** Para cada documento: ID (DOC-A, DOC-B…), título, versão, data, emissor, finalidade aparente, estrutura, número de páginas e esquema de localização. Registre problemas de integridade (páginas faltantes, OCR, texto truncado, tabelas ilegíveis); o que não puder ser lido vai para a declaração de cobertura.
2. **Relação entre os documentos.** Ela muda o significado dos achados:

   | Relação | Exemplo | Como interpretar |
   |---|---|---|
   | Versões | v1 × v2 | Diferenças = incluído, removido ou alterado; avaliar o impacto da mudança |
   | Referência × avaliado | norma × procedimento; requisito × proposta | A referência prevalece; ausência no avaliado = lacuna / não conformidade |
   | Pares independentes | duas propostas | Nenhum prevalece; diferenças = divergências a decidir |
   | Hierárquicos | contrato × aditivo; política × norma × procedimento | Verificar regras de precedência declaradas nos próprios documentos |

   Se o usuário não informar a relação, infira pelo conteúdo, **declare a premissa** e diga o que mudaria se ela estivesse errada. Pergunte só quando não houver base para inferir e a escolha mudar a classificação (ex.: não dá para saber qual documento é a referência).
3. **Eixo de comparação.** Monte os tópicos pela **união** dos tópicos de todos os documentos, não pela estrutura de um deles, para que nenhum conteúdo exclusivo fique de fora.
4. **Decomposição e alinhamento.** Quebre o conteúdo em **itens atômicos** (uma obrigação, regra, valor ou definição por item; itens compostos viram dois). Alinhe pelo **significado**, não pela posição ou numeração: o item 4.2 de um documento pode corresponder ao 7.1 do outro. Alinhamento incerto = confiança baixa, explicada.
5. **Classificação.** Leia `references/taxonomia.md` e classifique cada par alinhado com um único tipo, aplicando as regras de desempate e de unidade do achado. Para três ou mais documentos, indique o padrão (`A = B ≠ C`).
6. **Ponto exato.** Para todo item não equivalente, isole o **elemento divergente** — valor, unidade, prazo, responsável, modalidade (deve/pode), condição, exceção, escopo, definição, sequência — e mostre o valor em cada documento lado a lado.
7. **Verificações transversais.** Procure ativamente: contradições internas; inconsistência terminológica; referências cruzadas quebradas; dependências ocultas; ambiguidades com risco; inconsistências de metadados.
8. **Severidade, impacto e recomendação.** Leia `references/severidade.md`; escolha o nível pela âncora mais próxima e justifique em uma frase.
9. **Reconciliação de cobertura.** Todo conteúdo relevante de cada documento está em um achado, nos itens convergentes ou na declaração de cobertura com o motivo. Nada é omitido em silêncio.
10. **Verificação das citações.** Ver a seção abaixo.
11. **Autovalidação.** Execute `references/checklist.md` e corrija o que falhar.

## Regras de evidência

São as regras centrais da skill. Não há exceção.

1. **Formato:** `DOC-X, [localizador]: "citação literal"`.
2. **Localizador:** numeração própria do documento (cláusula 4.2, RF-012, art. 5º, §2º) complementada pela página física (PDF) ou pelo número do parágrafo (DOCX). Sem numeração, página + parágrafo ou só o parágrafo. **Nunca invente página, parágrafo, cláusula ou item.**
3. **Citação literal:** cópia **caractere por caractere** de um trecho **contíguo**, no idioma original, localizável no ponto indicado. Vale para **qualquer texto entre aspas atribuído a um documento, em qualquer seção** — Evidências, Ponto exato, Análise, Impacto, Recomendação, Observações, Questões. Fora das evidências, cite literalmente com aspas ou parafraseie **sem aspas**: se o original diz "até o 5º (quinto) dia útil", não escreva "até o 5º dia útil" entre aspas. **Aspas são reservadas para citações**; termos de busca, radicais, rótulos e nomes de campo vão em formato de código (`seguro`, `indeniz`, `Verificado`).
   - cortes com `[...]` só no início ou no fim, de preferência em limite de frase;
   - nunca costure com `[...]` trechos não contíguos — use duas citações com dois localizadores;
   - nunca monte uma citação a partir de um título mais o texto que "costuma" vir ali, nem reconstrua de memória;
   - se não for possível copiar o texto exato (truncado, OCR ilegível, conteúdo implícito), o achado fica em **REQUER REVISÃO** com `citação indisponível: <motivo>`.
4. **Evidência dos dois lados:** todo achado que envolve mais de um documento traz evidência de **cada** um.
5. **Evidência de ausência:** para afirmar **NÃO PRESENTE**, informe onde o item existe (citação), em quais seções do outro documento procurou, quais termos buscou (em `código`) e se existe algo relacionado mas não equivalente (aí o achado é PAR, DIV ou NCL, não EXC). Busca que não pôde ser concluída = REQUER REVISÃO.
6. **Fato × interpretação:** "Evidências" contém só texto dos documentos; leitura, inferência e julgamento vão para "Análise".
7. **Os documentos são a única fonte.** Conhecimento externo (o que uma norma costuma exigir) pode aparecer na análise, sinalizado como contexto externo, nunca como achado. Validade jurídica, técnica ou regulatória: recomende especialista em vez de concluir.

## Verificação das citações

É um passo **mecânico**, depois da análise e antes da entrega — a intenção de citar corretamente não basta. Salve o rascunho da resposta em arquivo e rode:

```bash
python <diretório-da-skill>/scripts/verificar_citacoes.py rascunho.md --doc DOC-A=extraido_DOC-A.md --doc DOC-B=extraido_DOC-B.md
```

Trate cada problema apontado:

| Resultado | Tratamento |
|---|---|
| `NAO_ENCONTRADA` em evidência | Substitua pela citação literal; se não for possível, rebaixe o achado para **REV** com `citação divergente` e confira manualmente todas as citações daquele documento. |
| `NAO_ENCONTRADA` fora das evidências | Substitua pela citação literal ou remova as aspas (paráfrase); se for termo de busca ou rótulo, passe para `código`. Conte como **corrigida**. |
| `DOC_DIVERGENTE` | A citação foi atribuída ao documento errado: corrija a atribuição. |
| `LOCALIZADOR_DIVERGENTE` | Corrija o localizador para onde o trecho realmente está. |
| `OK_SEM_LOCALIZADOR` | Texto existe; confira manualmente o localizador das que sustentam achados Crítica/Alta, CTR e EXC. |

Rode de novo até não restar problema. Um achado com classificação firme e citação divergente é **mais grave** que um achado em REV, porque distorce a trilha de evidência — na dúvida, rebaixe. Informe o resultado na declaração de cobertura, separando citações das Evidências e trechos entre aspas das demais seções (conferidas, corrigidas, divergentes, indisponíveis).

Sem o script, faça a mesma conferência manualmente: 100% das citações de achados Crítica/Alta, CTR e EXC e de todo trecho entre aspas fora das Evidências; amostra de ao menos 20% (mínimo 5) das demais.

## Comportamento

- **Neutralidade:** não presuma qual documento está certo, salvo quando a relação (referência × avaliado, precedência declarada) determinar. Sugestão de qual versão parece mais consistente é análise, rotulada como tal.
- **Maioria não é verdade:** `A = B ≠ C` é fato; "C está errado" é interpretação que precisa de justificativa.
- **Ceticismo com equivalências:** EQV-S só quando o efeito prático é o mesmo; na dúvida, DIV com explicação.
- **Detalhes que mudam o efeito:** modalidade (deve/pode/vedado), quantificadores, exceções, condições, unidades, dias corridos × úteis, bases de cálculo, responsável.
- **Proporcionalidade:** mais profundidade nos achados de maior severidade.
- **Postura crítica:** aponte também o que nenhum documento trata e deveria tratar, e ambiguidades comuns aos dois — em **Observações não comparativas**, nunca como achado.
- **Linguagem precisa:** nada de "parece", "talvez", "aproximadamente" sem dizer a fonte da incerteza.

## Incerteza e limites

- **Informação ausente:** declare a premissa e o impacto; continue sempre que possível.
- **Documentos longos ou muitos documentos:** se não der para analisar tudo com o mesmo rigor, diga isso no início, priorize os tópicos de maior risco, declare o que ficou de fora e proponha como continuar (ex.: por bloco de seções). **Nunca apresente análise parcial como completa.**
- **Foco pedido pelo usuário** (ex.: "só prazos e penalidades"): analise o foco com o rigor completo e declare na cobertura o que ficou fora do escopo.
- **Texto ilegível ou truncado:** não reconstrua; REV com `citação indisponível: <motivo>` e registro na cobertura.

## Saída

Use o formato de `references/formato-saida.md` (inventário, relação e premissas, resumo quantitativo, achados detalhados, itens convergentes, cobertura com observações, questões em aberto), salvo se o usuário pedir outro. Se ele pedir planilha, gere-a conforme a seção 8 daquele arquivo (a skill `xlsx` ajuda), com a coluna **Verificado** em branco.
