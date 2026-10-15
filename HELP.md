# HELP — Auditoria comparativa de documentos

Guia de uso da **persona**, da **skill no Claude** e da **skill em outros LLMs** (ChatGPT, Gemini, Copilot, API).

---

## Sumário

1. [O que é e o que faz](#1-o-que-é-e-o-que-faz)
2. [Arquivos do pacote](#2-arquivos-do-pacote)
3. [Qual forma de uso escolher](#3-qual-forma-de-uso-escolher)
4. [Uso como persona (prompt)](#4-uso-como-persona-prompt)
5. [Uso como skill no Claude](#5-uso-como-skill-no-claude)
6. [Uso em outros LLMs](#6-uso-em-outros-llms)
7. [Scripts: extração e verificação de citações](#7-scripts-extração-e-verificação-de-citações)
8. [Como ler o resultado](#8-como-ler-o-resultado)
9. [Testar e manter (kit e gabarito)](#9-testar-e-manter-kit-e-gabarito)
10. [Solução de problemas](#10-solução-de-problemas)
11. [Histórico de versões](#11-histórico-de-versões)

---

## 1. O que é e o que faz

Compara **dois ou mais documentos** com rigor de auditoria: contratos e aditivos, versões v1 × v2, especificações, PRDs, requisitos × proposta, edital × proposta, norma × procedimento, políticas, propostas de fornecedores.

Para cada diferença, aponta:
- **qual item** e **em qual documento**;
- **onde exatamente**: cláusula + página física (PDF) ou parágrafo (DOCX);
- **o texto literal** de cada lado, conferido contra o original;
- **o elemento exato** que muda (valor, prazo, responsável, "deve" × "pode", condição…);
- tipo, severidade, confiança, impacto e recomendação.

Também lista o que é **igual** nos documentos, os problemas comuns aos dois (em "Observações") e as **questões em aberto** para os responsáveis.

Os achados são **indícios** que aceleram a revisão humana. A confirmação final é sempre de uma pessoa, no campo **Verificado**, que a IA nunca preenche.

---

## 2. Arquivos do pacote

| Arquivo | Para quê |
|---|---|
| [`persona-auditor-comparativo-documentos.md`](persona-auditor-comparativo-documentos.md) | **Persona v1.0** completa, em um único arquivo (~43 mil caracteres). Para colar como prompt. |
| [`auditoria-comparativa-documentos.skill`](auditoria-comparativa-documentos.skill) | **Skill empacotada** para instalar no Claude (7 arquivos). |
| [`auditoria-comparativa-documentos/`](auditoria-comparativa-documentos/SKILL.md) | Pasta-fonte da skill: `SKILL.md`, `references/`, `scripts/` e `evals/` (testes, fora do pacote). |
| [`auditoria-comparativa-documentos/scripts/extrair_documento.py`](auditoria-comparativa-documentos/scripts/extrair_documento.py) | Extrai PDF/DOCX/TXT com localizadores (página física, parágrafo, tabela). |
| [`auditoria-comparativa-documentos/scripts/verificar_citacoes.py`](auditoria-comparativa-documentos/scripts/verificar_citacoes.py) | Confere cada trecho entre aspas da análise contra o texto extraído. |
| [`kit-teste-persona/`](kit-teste-persona/LEIA-ME.md) | Kit de teste: contrato fictício v1 (PDF) e v2 (DOCX), gabarito v3 e scorecard. |
| `kit-teste-persona/gabarito-e-scorecard-rodada-*.xlsx` | Avaliações das rodadas 1 a 4. |
| [`auditoria-comparativa-documentos-workspace/`](auditoria-comparativa-documentos-workspace/iteration-1/benchmark.md) | Testes da skill (com e sem skill) e a página de revisão. |

> ⚠️ Estes arquivos estão numa pasta criada para esta sessão do Claude. Se a sessão for apagada, a pasta também é. Guarde uma cópia do que for usar: no mínimo, a persona, o `.skill`, a pasta da skill e o kit.

---

## 3. Qual forma de uso escolher

| Situação | Use |
|---|---|
| Uso no Claude (app, claude.ai, Claude Code), de forma recorrente | **Skill** (seção 5) — é a forma mais completa: aciona sozinha e já roda os scripts |
| Uso pontual no Claude, ou num Projeto do Claude.ai | **Persona** nas instruções do Projeto (seção 4) |
| ChatGPT, Gemini, Copilot ou outro assistente | **Outros LLMs** (seção 6) |
| Integração por API (qualquer provedor) | Persona como prompt de sistema (seção 6.3) |
| Qualquer caso em que a evidência precisa ser auditável | Some os **scripts** (seção 7), em qualquer opção |

Nos testes, **sem** a skill o modelo encontrou as diferenças, mas errou localizadores (citou páginas impressas como se fossem físicas), alterou citações e oscilou em tipos e severidades. **Com** a skill, 100% das verificações passaram. O ganho está na **auditabilidade**, não na detecção.

---

## 4. Uso como persona (prompt)

### 4.1 Onde colocar

| Ferramenta | Como |
|---|---|
| **Projeto do Claude.ai** | Cole o conteúdo da persona nas **instruções do Projeto**. Toda conversa do Projeto já começa com ela. |
| **Conversa avulsa** (qualquer IA) | Cole a persona como **primeira mensagem** e, na mensagem seguinte, envie a tarefa e os documentos. |
| **Claude Code** | Coloque a persona num `CLAUDE.md` da pasta de trabalho, ou cole no início da conversa. |
| **API** | Use a persona como **prompt de sistema**. |

### 4.2 Prompt padrão da tarefa

Mantenha a persona separada da tarefa. A cada uso, envie:

```markdown
## Tarefa
Compare os documentos anexos seguindo integralmente a sua metodologia.

## Documentos
- DOC-A: [nome do arquivo] — [descrição curta]
- DOC-B: [nome do arquivo] — [descrição curta]
- DOC-C: [se houver]

## Relação
[Versões | Referência × avaliado (diga qual é a referência) | Pares independentes | Hierárquicos | Não informada]

## Foco
[Ex.: priorize prazos, penalidades e responsabilidades | Análise completa]

## Saída
Use o formato de saída padrão (achados detalhados).
[Opcional: Ao final, gere também a planilha de achados conforme a seção 8 do formato.]
```

### 4.3 Boas práticas

- **Informe a relação** entre os documentos quando souber. Ela muda a interpretação: numa relação de versões, uma ausência é "removido"; numa relação referência × avaliado, é "não conformidade".
- **Informe o foco**, se houver. A análise fica mais curta e a cobertura declara o que ficou de fora.
- **Use os scripts** (seção 7) se a IA não executar código: envie o texto extraído no lugar do arquivo original e confira a resposta com o verificador.
- **Documentos longos** (80+ páginas): peça por blocos de seções. A persona avisa quando não consegue analisar tudo com o mesmo rigor, e nunca deve apresentar uma análise parcial como completa.

---

## 5. Uso como skill no Claude

### 5.1 Instalar

| Onde | Como |
|---|---|
| **App do Claude / claude.ai** | No cartão do arquivo `auditoria-comparativa-documentos.skill`, clique em **Save skill**. Outra forma: nas configurações do Claude, área de **Skills** (dentro de Capacidades; o nome do menu pode variar), envie o arquivo `.skill`. |
| **Claude Code** (global) | O `.skill` é um arquivo ZIP. Descompacte em `~/.claude/skills/`, de modo que exista `~/.claude/skills/auditoria-comparativa-documentos/SKILL.md`. |
| **Claude Code** (um projeto) | Descompacte em `.claude/skills/` dentro do projeto. |

Comando para o Claude Code (global):

```bash
unzip auditoria-comparativa-documentos.skill -d ~/.claude/skills/
```

### 5.2 Dependências

Os scripts usam `pypdf` e `python-docx` (e `openpyxl`, se você pedir planilha):

```bash
pip install pypdf python-docx openpyxl
```

Sem essas bibliotecas, a skill usa as skills `pdf` e `docx` do Claude, com as mesmas regras de localizador.

### 5.3 Como acionar

Não é preciso colar a persona. A skill é acionada quando você pede para **comparar, confrontar, cruzar, auditar** documentos ou **ver o que mudou** entre versões. Exemplos testados:

- Pedido estruturado: o prompt da seção 4.2.
- Pedido informal:
  > tenho aqui as duas versões do contrato de suporte com a Alfa Sistemas (DOC-A_contrato_v1.pdf é a antiga e DOC-B_contrato_v2.docx a que mandaram agora). preciso levar pro jurídico amanhã exatamente o que mudou, com cláusula e trecho de cada lado. me manda também uma planilha com os pontos pra eu ir marcando o que já conferi
- Pedido com foco:
  > Compare a versão vigente com a proposta de nova versão. Só me interessam os pontos que afetam prazos de atendimento e penalidades.

Se a skill não for acionada, peça explicitamente: *"use a skill auditoria-comparativa-documentos"*.

### 5.4 O que a skill faz por você

1. Extrai cada documento com `extrair_documento.py`: página física no PDF; parágrafo, tabela e alterações controladas no DOCX.
2. Segue as 11 etapas da metodologia, lendo as referências na hora certa (taxonomia, severidade, formato).
3. Roda `verificar_citacoes.py` no rascunho e corrige o que for apontado.
4. Executa o checklist final e entrega o relatório (e a planilha, se você pedir).

### 5.5 Custo esperado

Nos testes, uma análise de dois documentos de 7 páginas levou de 4 a 6 minutos, e cerca de 10 minutos com planilha. Isso dá cerca de 1,7× mais tokens que um pedido sem a skill, por causa da extração, da verificação e do relatório completo.

---

## 6. Uso em outros LLMs

O arquivo `.skill` é específico do Claude. Em outras ferramentas, use o **conteúdo** da skill (texto em Markdown) e os **scripts** (Python).

### 6.1 Assistente personalizado (GPT personalizado no ChatGPT, Gem no Gemini, agente no Copilot)

| Campo da ferramenta | O que colocar |
|---|---|
| **Instruções** | Conteúdo do `SKILL.md`, **sem** o cabeçalho entre `---` (~14 mil caracteres). |
| **Arquivos de conhecimento** | `references/taxonomia.md`, `references/severidade.md`, `references/formato-saida.md`, `references/checklist.md`. |
| **Execução de código** (se houver) | Envie também os 2 scripts e ative a execução de código. |

Ajustes no texto das instruções:
- Troque `<diretório-da-skill>/scripts/...` por *"os scripts anexados"* (com execução de código) ou por *"o texto extraído que o usuário enviar"* (sem execução).
- Troque as menções às skills `pdf`, `docx` e `xlsx` pelos recursos da ferramenta para ler PDF/DOCX e gerar planilha.

Essas ferramentas limitam o tamanho do campo de instruções. Se não couber, mantenha nas instruções o papel, a leitura da entrada, a metodologia e as regras de evidência, e mova a verificação das citações, o comportamento e a seção de incerteza para um arquivo de conhecimento.

### 6.2 Qualquer IA, com os scripts na sua máquina

Use este fluxo quando a ferramenta não executa código ou quando você quer controle total da evidência:

1. **Extraia** os documentos (seção 7.1).
2. Abra a conversa com a persona (ou as instruções da 6.1) e envie os arquivos `extraido_DOC-*.md` **no lugar dos originais**, com o prompt da seção 4.2.
3. Salve a resposta como `analise.md`.
4. **Verifique** as citações (seção 7.2).
5. Se houver `NAO_ENCONTRADA`, `DOC_DIVERGENTE` ou `LOCALIZADOR_DIVERGENTE`, devolva a lista à IA e peça a correção. Repita até zerar.

### 6.3 Via API (qualquer provedor)

- **Prompt de sistema:** a persona completa, ou o `SKILL.md` com as 4 referências concatenadas ao final.
- **Mensagem do usuário:** o prompt da seção 4.2, com o texto extraído pelos scripts.
- **Pós-processamento:** rode `verificar_citacoes.py` na resposta. Em caso de problema, faça uma segunda chamada pedindo a correção.
- Na API do Claude, a skill também pode ser usada como skill; consulte a documentação de *Agent Skills*.

### 6.4 Antes de confiar: calibre no novo modelo

Toda a calibração foi feita com o Claude: tipos, regras de desempate, âncoras de severidade, unidade do achado e regra de aspas. Outro modelo pode se comportar diferente. Antes de usar em documentos reais:

1. Rode o caso C0 do [kit](kit-teste-persona/LEIA-ME.md) **duas vezes**, em conversas novas.
2. Preencha o [gabarito v3](kit-teste-persona/gabarito-e-scorecard.xlsx) (seção 9).
3. Só use em documentos reais se o resultado for **Aprovado**. Se não for, ajuste as instruções na seção que o scorecard indicar.

---

## 7. Scripts: extração e verificação de citações

Requisitos: Python 3.9+, `pip install pypdf python-docx`.

### 7.1 `extrair_documento.py`

```bash
python extrair_documento.py <arquivo> --id DOC-A [--saida extraido_DOC-A.md]
```

| Formato | O que gera |
|---|---|
| **PDF** | Uma seção por **página física**: `=== DOC-A · Página N ===`. Avisa quando uma página não tem texto (provável escaneada → OCR). Inclui os metadados do arquivo. |
| **DOCX** | `[par. N]` para cada parágrafo do corpo, em ordem, a partir de 1; `[Tabela T, linha L, col. C]` para células; seções para **alterações controladas** (inserções e exclusões, com autor e data), comentários, cabeçalhos e rodapés. |
| **TXT / MD** | `[par. N]` para cada bloco separado por linha em branco. |

O arquivo gerado é a **fonte de todas as citações e localizadores**. Guarde-o junto com a análise.

### 7.2 `verificar_citacoes.py`

```bash
python verificar_citacoes.py analise.md --doc DOC-A=extraido_DOC-A.md --doc DOC-B=extraido_DOC-B.md
```

Confere cada trecho entre aspas (“...” ou "...") da análise. Ignora o que está em `código`, aceita cortes com `[...]`, `…` ou `...` e ignora **negrito** dentro da citação.

| Resultado | Significado | O que fazer |
|---|---|---|
| `OK` | Texto encontrado no localizador indicado | Nada |
| `OK_SEM_LOCALIZADOR` | Texto existe, mas o localizador não foi reconhecido automaticamente | Conferir à mão os que sustentam achados Crítica/Alta, CTR e EXC |
| `LOCALIZADOR_DIVERGENTE` | Texto existe, mas em outro lugar | Corrigir o localizador |
| `DOC_DIVERGENTE` | Texto atribuído ao documento errado | Corrigir a atribuição |
| `NAO_ENCONTRADA` | Texto não existe em nenhum documento | Substituir pela citação literal, remover as aspas (paráfrase) ou passar para `código` (termos e rótulos); em evidência de achado, rebaixar para **REV** |

O código de saída é 1 quando há problemas, o que permite usar o verificador em automações.

---

## 8. Como ler o resultado

### 8.1 Estrutura do relatório

1. **Identificação e escopo:** inventário dos documentos e esquema de localização.
2. **Relação e premissas:** relação entre os documentos e o que muda se uma premissa estiver errada.
3. **Resumo quantitativo:** achados por tipo e severidade; carga de revisão humana.
4. **Achados detalhados:** evidências, ponto exato, análise, impacto, recomendação e o campo **Verificado (revisor): ☐**.
5. **Itens convergentes:** o que é igual, com localizador e fragmento literal.
6. **Cobertura e limitações:** o que foi analisado, resultado da verificação das citações e **Observações não comparativas** (problemas iguais nos dois documentos).
7. **Questões em aberto:** perguntas para os responsáveis, ligadas aos achados.
8. **Planilha** (se pedida): uma linha por achado, com a coluna **Verificado** em branco.

### 8.2 Tipos de achado

| Código | Significado |
|---|---|
| **CTR** | Contradição: não podem valer ao mesmo tempo (ex.: 30 × 45 dias; "deve" × "pode") |
| **DIV** | Divergência: podem coexistir, mas o efeito muda (ex.: condição acrescentada) |
| **PAR** | Cobertura parcial |
| **EXC** | Tema inteiro presente em um documento e ausente no outro (NÃO PRESENTE) |
| **NCL** | Não claro: conteúdo vago ou ambíguo sobre o tema |
| **REV** | Requer revisão humana ou citação indisponível |
| **TER** | Inconsistência de terminologia |
| **INT** | Contradição interna, dentro de um mesmo documento |
| **REF** | Referência quebrada (ex.: anexo inexistente) |
| **EQV-L / EQV-S** | Equivalente literal / de sentido. Aparecem só nos convergentes. |

Quando a relação é de versões, o tipo recebe também o rótulo `INCLUÍDO`, `REMOVIDO` ou `ALTERADO`.

### 8.3 Severidade (resumo das âncoras)

| Nível | Situações típicas |
|---|---|
| **Crítica** | Elemento essencial: partes, objeto, preço total, vigência, validade; algo exigido por lei removido |
| **Alta** | Obrigação, prazo, valor ou responsável alterado; sanção, garantia, seguro ou fiscalização removidos ou enfraquecidos; referência quebrada que afeta regra material |
| **Média** | Condição procedimental acrescentada; termo não definido com sentido inferível |
| **Baixa** | Detalhamento ou organização sem efeito prático |
| **Informativa** | Versão, data e metadados (em geral, ficam no inventário) |

### 8.4 Revisão humana

1. Comece pelos achados **Crítica/Alta** e pelos de confiança **Média/Baixa**.
2. Para cada achado, abra o documento no localizador citado e confira o trecho.
3. Marque **Verificado** no relatório ou na planilha.
4. Leve as **Questões em aberto** aos responsáveis.

---

## 9. Testar e manter (kit e gabarito)

### 9.1 Quando testar

- Ao usar em um **novo modelo ou ferramenta** (seção 6.4).
- Depois de **alterar** a persona ou a skill (teste de regressão).

### 9.2 Como testar

1. Use os documentos de [`kit-teste-persona/documentos/`](kit-teste-persona/LEIA-ME.md): contrato fictício v1 (PDF) e v2 (DOCX), com **9 diferenças plantadas** e **3 armadilhas**.
2. Rode o prompt do caso C0 do LEIA-ME **duas vezes**, em conversas novas. **Nunca** envie a planilha de gabarito para a IA.
3. Preencha as abas *Execução 1* e *Execução 2* do [gabarito v3](kit-teste-persona/gabarito-e-scorecard.xlsx). Confira as citações com o `verificar_citacoes.py`, que é mais rápido que o Ctrl+F.
4. Leia o **Scorecard**. Os 3 primeiros critérios são eliminatórios: citação errada, citação errada marcada como verificada e diferença Crítica/Alta não detectada.

### 9.3 Testes automatizados da skill (Claude Code)

A pasta [`auditoria-comparativa-documentos/evals/`](auditoria-comparativa-documentos/evals/README.md) traz:
- `evals.json`: 3 casos de teste (formal, informal com planilha, foco), com as expectativas;
- `referencias/`: as 8 execuções do desenvolvimento, sendo a 7 e a 8 o padrão de referência da v1.0;
- o teste de regressão do verificador (descrito no README da pasta).

Esses testes são usados com a skill **skill-creator** do Claude. Peça: *"use a skill-creator para testar de novo a skill auditoria-comparativa-documentos com os evals da pasta"*.

---

## 10. Solução de problemas

| Problema | Solução |
|---|---|
| `pypdf` ou `python-docx` não instalado | `pip install pypdf python-docx` |
| Página do PDF sem texto (escaneada) | Aplique OCR antes (no Claude, a skill `pdf` faz isso). Achados baseados nessa página ficam com confiança no máximo **Média**. |
| A IA cita a página impressa em vez da física | Envie o texto extraído pelo script, que já marca a página física, e lembre a regra no pedido. |
| O verificador acusa termos de busca ou rótulos | Esses termos devem estar em `código`, não entre aspas. Peça a correção ou ignore se não forem citações. |
| O verificador acusa sugestões de redação entre aspas | Não são citações; peça que a IA as escreva sem aspas ou em bloco separado. |
| A skill não é acionada | Peça explicitamente: *"use a skill auditoria-comparativa-documentos"*. |
| Documento muito longo | Peça a análise por blocos de seções e confira a declaração de cobertura. |
| Três ou mais documentos | Funciona: os achados mostram o padrão (ex.: `A = B ≠ C`). Informe a relação (ex.: política × norma × procedimento). |
| DOCX com alterações controladas | O extrator lista inserções e exclusões, que são evidência direta do que mudou. |
| `generate_review.py` da skill-creator falha com Python 3.9 | Requer Python 3.10+. Atualize o Python ou rode com `from __future__ import annotations`. |

---

## 11. Histórico de versões

| Versão | Mudança | Resultado nos testes |
|---|---|---|
| Persona inicial | Evidência com localizador e citação literal; taxonomia; três estados de "não encontrado"; verificação das citações | Rodada 1: 9/9 diferenças, mas 4 citações não literais na Análise e tipos variando |
| + ajustes 1–4 e 6 | Aspas literais em toda seção; regras de desempate; unidade do achado; achado × observação; parágrafo no DOCX | Rodada 2: 100%; severidade instável |
| + calibração | Âncoras de severidade; regra de versão/data; exclusividade achado × convergência; termos em `código` | Rodada 3: 100%, severidade 9/9; duplicação de REF/TER em uma execução |
| **v1.0** | Regra de unidade refinada | Rodada 4: 100%; mesmos 10 achados nas duas execuções |
| **Skill 1.0** | Persona v1.0 em formato de skill + scripts de extração e verificação | Iteração 1: 100% com a skill × 40% sem (3 casos) |
