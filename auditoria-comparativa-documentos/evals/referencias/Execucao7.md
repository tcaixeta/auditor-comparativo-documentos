# Análise comparativa — Contrato nº 041/2026: DOC-A (v1.0, PDF) × DOC-B (v2.0, .docx)

> Os achados são **indícios** para revisão. Só devem embasar decisões depois que o revisor conferir cada evidência no documento original e marcar o campo **Verificado**.

## 1. Identificação e escopo

| Campo | DOC-A | DOC-B |
|---|---|---|
| Arquivo | DOC-A_contrato_v1.pdf | DOC-B_contrato_v2.docx |
| Título | Contrato de prestação de serviços de suporte técnico e manutenção de software | idem |
| Nº do contrato | 041/2026 | 041/2026 |
| Versão | 1.0 (p. 1) | 2.0 (par. 3) |
| Data do documento | 10 de março de 2026 (p. 1 e p. 6) | 2 de setembro de 2026 (par. 4 e par. 40) |
| Partes | Beta Logística S.A. (CONTRATANTE); Alfa Sistemas Ltda. (CONTRATADA) | idem |
| Emissor/autor | Não identificado no texto. Metadado do PDF: autor `Kit de teste`. | Não identificado no texto. Metadado: criador `python-docx`. |
| Tamanho | 7 páginas físicas | 45 parágrafos + 1 tabela (sem paginação fixa) |
| Estrutura | Capa; Cláusulas 1–12; bloco de assinaturas; Anexo I; Anexo II (tabela) | Capa; Cláusulas 1–12; bloco de assinaturas; Anexo I; Anexo II (tabela) |
| Esquema de localização | Cláusula + **página física** (`p. N`). A numeração impressa no rodapé (Página 1 de 6 … 6 de 6) começa na página física 2; a capa (p. 1) não tem número. Usada a **página física**. Tabela: `p. 7 · Tabela 1`. | Cláusula + **número do parágrafo** (`par. N`). Regra de contagem: parágrafos do corpo numerados de 1 a 45 em sequência, começando pelo título (par. 1); não há parágrafos vazios; a tabela fica fora da contagem e é localizada como `Tabela 1, linha L, col. C`. |
| Integridade | Camada de texto nativa em todas as páginas; nenhuma página com OCR; nada ilegível. | Sem alterações controladas, sem comentários, sem cabeçalho/rodapé. `customXml` contém só bibliografia vazia; `thumbnail.jpeg` é miniatura do modelo e não foi analisada como conteúdo. |

## 2. Relação entre os documentos e premissas

**Relação identificada: Versões** (DOC-A = v1.0, anterior; DOC-B = v2.0, posterior).

Base: mesmo número de contrato, mesmo título, mesmas partes, mesma estrutura de 12 cláusulas e 2 anexos, e identificação expressa de versão (DOC-A, p. 1: "Versão 1.0"; DOC-B, par. 3: "Versão 2.0") com datas em ordem cronológica.

**Como isso afeta a classificação:** as diferenças são lidas como mudança de DOC-A para DOC-B e recebem os rótulos `INCLUÍDO`, `REMOVIDO` ou `ALTERADO`. Nenhuma versão prevalece por regra declarada; a análise descreve o que mudou e o efeito.

**Premissas adotadas**

| # | Premissa | Impacto se estiver errada |
|---|---|---|
| P1 | DOC-B é a versão posterior e pretende substituir DOC-A. Nenhum dos documentos declara isso: foram buscados `substitu`, `revog`, `versão anterior`, `anterior`, `prevalec`, `precedência`, sem resultado. | Se DOC-B for uma contraproposta em negociação (pares independentes), os rótulos de versão deixam de valer e os achados viram divergências a decidir; os tipos (CTR, NCL etc.) não mudam. |
| P2 | DOC-B é um instrumento completo, assinado na data do seu bloco de assinatura, e não um termo aditivo. | Afeta diretamente o ACH-001: se DOC-B for só uma versão consolidada sem nova assinatura, o marco da vigência pode continuar sendo o de DOC-A. |

## 3. Resumo quantitativo

| Tipo | Qtde | | Severidade | Qtde |
|---|---|---|---|---|
| CTR | 4 | | Crítica | 1 |
| NCL | 1 | | Alta | 7 |
| EXC | 1 | | Média | 2 |
| REF | 1 | | Baixa | 0 |
| INT | 1 | | Informativa | 0 |
| TER | 1 | | **Total** | **10** |
| DIV | 1 | | | |
| REV | 0 | | | |

**Carga de revisão humana:** 1 item em NÃO CLARO (ACH-006) e 0 em REQUER REVISÃO. Os 10 achados aguardam o campo **Verificado**. Itens convergentes: 20.

**Leitura geral (efeito combinado, não usado para elevar severidades):** a v2.0 desloca o equilíbrio do contrato a favor da CONTRATADA. Prazos de correção e atendimento ficam mais longos (ACH-002, ACH-003), o relatório mensal deixa de ser obrigatório (ACH-005), a multa objetiva é substituída por redação vaga (ACH-006) e o seguro de responsabilidade civil sai do contrato (ACH-007). Em conjunto, os prazos aumentam ao mesmo tempo em que a fiscalização e a sanção por descumpri-los enfraquecem. A v2.0 também introduz defeitos que não existiam na v1.0 (ACH-004, ACH-008, ACH-009) e uma condição interna da CONTRATANTE para rescindir (ACH-010).

## 4. Achados detalhados

### ACH-001 — O marco inicial da vigência muda com a nova data de assinatura

- **Tipo:** CTR / ALTERADO
- **Severidade:** Crítica. Âncora: muda um elemento essencial do documento (vigência).
- **Confiança:** Média. Depende da premissa P2; as linhas de assinatura estão em branco nos dois documentos, e a data de assinatura só aparece na linha de local e data.
- **Tópico:** Vigência
- **Padrão entre documentos:** A ≠ B

**Evidências**
- DOC-A, cl. 3.1 (p. 2): "3.1 O presente contrato vigorará pelo prazo de 12 (doze) meses, contados da data de sua assinatura, podendo ser prorrogado mediante termo aditivo."
- DOC-A, bloco de assinatura (p. 6): "São Paulo, 10 de março de 2026."
- DOC-B, cl. 3.1 (par. 13): "3.1 O presente contrato vigorará pelo prazo de 12 (doze) meses, contados da data de sua assinatura, podendo ser prorrogado mediante termo aditivo."
- DOC-B, bloco de assinatura (par. 40): "São Paulo, 2 de setembro de 2026."
- **Citação verificada:** Sim (DOC-A e DOC-B)

**Ponto exato da diferença**
| Elemento | DOC-A | DOC-B |
|---|---|---|
| Regra de vigência (cl. 3.1) | 12 meses contados da assinatura | igual |
| Prorrogação | mediante termo aditivo | igual |
| Data do local e assinatura | 10/03/2026 | 02/09/2026 |
| Término resultante (cálculo do analista; a regra de contagem não está nos documentos) | março de 2027 | setembro de 2027 |

**Análise**
O texto da cl. 3.1 é idêntico, mas o marco a que ele remete (a data de assinatura) mudou. Se DOC-B for assinado como novo instrumento, a vigência passa a contar de 02/09/2026 e termina cerca de seis meses depois do término previsto em DOC-A. Pela regra de desempate, a mudança do valor de um prazo do mesmo item é CTR: o contrato não pode ter dois termos finais. A própria cl. 3.1 prevê prorrogação por termo aditivo, e DOC-B não se identifica como aditivo nem diz se reinicia ou mantém a vigência original. Outras regras dependem do término: o reajuste anual (cl. 7.3) e o sigilo por 5 anos após o término (DOC-A cl. 5.3; DOC-B cl. 11.1) também se deslocam.

**Impacto / risco**
Incerteza sobre a data de término do contrato e sobre a data-base de reajuste e de sigilo. Possível prorrogação de fato sem o instrumento previsto na cl. 3.1.

**Recomendação**
Declarar em DOC-B se ele substitui DOC-A, e a partir de quando, e fixar expressamente as datas de início e término. A escolha da forma (termo aditivo × novo instrumento) deve ser validada pelo jurídico.

**Verificado (revisor):** ☐

---

### ACH-002 — O prazo de correção de falha crítica sobe de 30 para 45 dias corridos

- **Tipo:** CTR / ALTERADO
- **Severidade:** Alta. Âncora: altera prazo de forma material (correção de 30 para 45 dias).
- **Confiança:** Alta
- **Tópico:** Prazos de atendimento
- **Padrão entre documentos:** A ≠ B

**Evidências**
- DOC-A, cl. 4.2 (p. 3): "4.2 A CONTRATADA deverá concluir a correção de falhas de severidade crítica em até 30 (trinta) dias corridos, contados da abertura do chamado."
- DOC-B, cl. 4.2 (par. 16): "4.2 A CONTRATADA deverá concluir a correção de falhas de severidade crítica em até 45 (quarenta e cinco) dias corridos, contados da abertura do chamado."
- **Citação verificada:** Sim (DOC-A e DOC-B)

**Ponto exato da diferença**
| Elemento | DOC-A | DOC-B |
|---|---|---|
| Prazo | 30 dias | 45 dias |
| Tipo de contagem | corridos | igual |
| Marco inicial | abertura do chamado | igual |
| Modalidade / responsável | deverá / CONTRATADA | igual |

**Análise**
O valor do prazo muda para o mesmo item. Pela regra de desempate, é CTR. As duas versões não podem valer juntas para a mesma obrigação.

**Impacto / risco**
Uma falha crítica (sistema indisponível, segundo o Anexo II) pode durar 15 dias a mais sem que haja descumprimento.

**Recomendação**
Confirmar se a mudança é intencional e registrar a justificativa. Avaliar o prazo junto com a cláusula de penalidade (ver ACH-006).

**Verificado (revisor):** ☐

---

### ACH-003 — Anexo II: o prazo da severidade baixa sobe de 5 para 10 dias úteis

- **Tipo:** CTR / ALTERADO
- **Severidade:** Alta. Âncora: altera prazo de forma material.
- **Confiança:** Alta
- **Tópico:** Prazos de atendimento (Matriz de Severidade)
- **Padrão entre documentos:** A ≠ B

**Evidências**
- DOC-A, Anexo II (p. 7 · Tabela 1, linha Baixa, col. Prazo de atendimento): "Até 5 dias úteis"
- DOC-B, Anexo II (Tabela 1, linha 4, col. 3): "Até 10 dias úteis"
- Descrição da linha, igual nos dois: DOC-A (p. 7 · Tabela 1, linha Baixa, col. Descrição): "Dúvida ou falha sem impacto operacional" · DOC-B (Tabela 1, linha 4, col. 2): "Dúvida ou falha sem impacto operacional"
- **Citação verificada:** Sim (DOC-A e DOC-B)

**Ponto exato da diferença**
| Elemento | DOC-A | DOC-B |
|---|---|---|
| Prazo de atendimento (baixa) | 5 dias | 10 dias |
| Tipo de contagem | úteis | igual |
| Descrição da severidade | dúvida ou falha sem impacto operacional | igual |

**Análise**
Mudança de valor do mesmo item, logo CTR. Em DOC-A, o Anexo II e a cl. 4.3 dão o mesmo prazo. Em DOC-B, a mudança ficou só no anexo e criou uma contradição interna (ver ACH-004).

**Impacto / risco**
O prazo para chamados de baixa severidade dobra. Somado ao ACH-004, não se sabe qual prazo vale.

**Recomendação**
Decidir o prazo pretendido e alinhar o Anexo II e a cl. 4.3.

**Verificado (revisor):** ☐

---

### ACH-004 — DOC-B: a cl. 4.3 e o Anexo II dão prazos diferentes para a severidade baixa

- **Tipo:** INT
- **Severidade:** Alta. Âncora: contradição cláusula × anexo com prazos diferentes, que deixa incerto qual regra material vale.
- **Confiança:** Alta
- **Tópico:** Prazos de atendimento
- **Padrão entre documentos:** defeito só em DOC-B; em DOC-A, a cl. 4.3 (p. 3) e o Anexo II (p. 7) são consistentes.

**Evidências**
- DOC-B, cl. 4.3 (par. 17): "4.3 Os chamados de severidade baixa serão atendidos em até 5 (cinco) dias úteis, conforme a Matriz de Severidade do Anexo II."
- DOC-B, Anexo II (Tabela 1, linha 4, col. 3): "Até 10 dias úteis"
- **Citação verificada:** Sim

**Ponto exato da diferença**
| Elemento | DOC-B cl. 4.3 | DOC-B Anexo II |
|---|---|---|
| Prazo (severidade baixa) | 5 dias úteis | 10 dias úteis |
| Remissão | remete à Matriz do Anexo II | — |

**Análise**
A cláusula fixa 5 dias úteis e diz seguir o Anexo II, mas o Anexo II diz 10. A remissão é circular: a cláusula diz seguir um anexo que a contradiz. DOC-B não tem regra de precedência entre cláusulas e anexos (buscados `prevalec`, `precedência`, `conflit`, `divergên`, sem resultado). Para piorar, a cl. 12.1 de DOC-B indica outro anexo como Matriz de Severidade (ver ACH-008).

**Impacto / risco**
Disputa sobre o cumprimento do prazo de chamados de baixa severidade e sobre a aplicação de penalidades vinculadas à Cláusula 4.

**Recomendação**
Unificar o prazo e, se quiser, incluir uma regra de precedência entre corpo e anexos.

**Verificado (revisor):** ☐

---

### ACH-005 — O relatório mensal de desempenho deixa de ser obrigatório

- **Tipo:** CTR / ALTERADO
- **Severidade:** Alta. Âncora: enfraquece mecanismo de fiscalização (relatório obrigatório que vira facultativo).
- **Confiança:** Alta
- **Tópico:** Obrigações da CONTRATADA
- **Padrão entre documentos:** A ≠ B

**Evidências**
- DOC-A, cl. 5.2 (p. 3): "5.2 A CONTRATADA deverá emitir relatório mensal de desempenho até o 5º (quinto) dia útil de cada mês."
- DOC-B, cl. 5.2 (par. 20): "5.2 A CONTRATADA poderá emitir relatório mensal de desempenho até o 5º (quinto) dia útil de cada mês."
- **Citação verificada:** Sim (DOC-A e DOC-B)

**Ponto exato da diferença**
| Elemento | DOC-A | DOC-B |
|---|---|---|
| Modalidade | deverá (obrigação) | poderá (faculdade) |
| Objeto, periodicidade, prazo | relatório mensal, até o 5º dia útil | igual |

**Análise**
Só muda o verbo modal. Pela regra de desempate, a mudança de obrigação para faculdade é CTR: o status normativo do item não pode ser os dois ao mesmo tempo. O relatório é o instrumento que permite ao gestor do contrato (cl. 6.2) medir o cumprimento dos prazos da Cláusula 4.

**Impacto / risco**
A CONTRATANTE perde o meio formal de acompanhar os níveis de serviço e de demonstrar descumprimento.

**Recomendação**
Confirmar a intenção. Se o relatório for necessário para fiscalizar, restabelecer a redação obrigatória.

**Verificado (revisor):** ☐

---

### ACH-006 — A multa de 2% é substituída por medidas cabíveis não definidas

- **Tipo:** NCL / ALTERADO
- **Severidade:** Alta. Âncora: remove ou enfraquece sanção (multa trocada por redação vaga).
- **Confiança:** Alta
- **Tópico:** Penalidades
- **Padrão entre documentos:** A ≠ B

**Evidências**
- DOC-A, cl. 8.1 (p. 4): "8.1 O descumprimento dos prazos previstos na Cláusula 4 sujeitará a CONTRATADA a multa de 2% (dois por cento) sobre o valor mensal, por ocorrência."
- DOC-B, cl. 8.1 (par. 29): **NÃO CLARO.** "8.1 O descumprimento dos prazos previstos na Cláusula 4 poderá ensejar a aplicação das medidas cabíveis." O item trata da consequência do descumprimento, mas não define a sanção, o valor nem a base de cálculo.
- **Citação verificada:** Sim (DOC-A e DOC-B)

**Ponto exato da diferença**
| Elemento | DOC-A | DOC-B |
|---|---|---|
| Gatilho | descumprimento dos prazos da Cláusula 4 | igual |
| Consequência | multa | medidas cabíveis (não definidas) |
| Valor / base de cálculo | 2% sobre o valor mensal | não há |
| Incidência | por ocorrência | não há |
| Sujeito passivo | CONTRATADA, expressa | não nomeado |
| Modalidade | sujeitará (consequência certa) | poderá ensejar (consequência eventual) |

**Análise**
O tema continua existindo, mas o conteúdo objetivo foi trocado por uma expressão sem definição. Pela regra de desempate, isso é NCL. A expressão de DOC-B, par. 29, "medidas cabíveis", não é definida em nenhum ponto do documento: ocorre uma única vez, e `multa` e `sanç` não aparecem; `penalidade` aparece só no título da Cláusula 8 (par. 28). A validade e a aplicabilidade de uma sanção sem conteúdo definido é questão jurídica e precisa de avaliação de especialista.

**Impacto / risco**
Sem sanção objetiva, os prazos da Cláusula 4 (já alongados, ver ACH-002 e ACH-003) ficam sem consequência certa.

**Recomendação**
Esclarecer com o responsável quais são as medidas pretendidas. Definir sanção, valor, base de cálculo e incidência, ou restabelecer a multa.

**Verificado (revisor):** ☐

---

### ACH-007 — A cláusula de seguro de responsabilidade civil profissional foi removida

- **Tipo:** EXC / REMOVIDO
- **Severidade:** Alta. Âncora: remove seguro.
- **Confiança:** Alta
- **Tópico:** Seguro
- **Padrão entre documentos:** presente em A; ausente em B

**Evidências**
- DOC-A, cl. 10.1 (p. 5): "10.1 A CONTRATADA manterá, durante toda a vigência deste contrato, apólice de seguro de responsabilidade civil profissional com cobertura mínima de R$ 500.000,00 (quinhentos mil reais)."
- DOC-A, título (p. 5): "Cláusula 10 – Do Seguro"
- DOC-B: **NÃO PRESENTE.** Lido o documento inteiro (par. 1–45 e Tabela 1), em especial Cl. 5 – Obrigações da CONTRATADA (par. 18–20), Cl. 10 (par. 33–34, que em DOC-B trata de proteção de dados), Cl. 11 (par. 35–36), Cl. 12 (par. 37–39) e Anexos I e II (par. 43–45, Tabela 1). Termos buscados: `seguro`, `apólice`, `responsabilidade civil`, `cobertura`, `500.000`, `indeniz`, `garantia`, sem resultado. O radical `segur` só aparece em par. 22 (política de segurança da informação), que não tem relação com seguro. Conteúdo relacionado: nenhum.
- **Citação verificada:** Sim (DOC-A)

**Ponto exato da diferença**
| Elemento | DOC-A | DOC-B |
|---|---|---|
| Obrigação de manter seguro | sim, durante toda a vigência | não há |
| Tipo de apólice | responsabilidade civil profissional | não há |
| Cobertura mínima | R$ 500.000,00 | não há |

**Análise**
O tema inteiro some, então é EXC / REMOVIDO. A remoção também renumerou o contrato: em DOC-A a Cláusula 10 trata de seguro e a 11 de proteção de dados; em DOC-B a Cláusula 10 trata de proteção de dados e a 11 de confidencialidade. Referências externas à numeração antiga passariam a apontar para outro conteúdo. Se o seguro for exigido por lei, regulação ou política interna, é questão que este documento não permite avaliar (contexto externo; especialista).

**Impacto / risco**
A CONTRATANTE perde a garantia financeira para danos causados pela CONTRATADA na prestação dos serviços.

**Recomendação**
Confirmar se a remoção é intencional. Se não for, reincluir a cláusula. Verificar se há documentos externos que citam cláusulas pelo número.

**Verificado (revisor):** ☐

---

### ACH-008 — A cl. 12.1 passa a citar um Anexo IV que não existe

- **Tipo:** REF / ALTERADO
- **Severidade:** Alta. Âncora: referência quebrada na cláusula de integração, que deixa de listar o anexo com os prazos (SLAs).
- **Confiança:** Alta
- **Tópico:** Disposições gerais / anexos
- **Padrão entre documentos:** A ≠ B (referência válida em A, quebrada em B)

**Evidências**
- DOC-A, cl. 12.1 (p. 6): "12.1 Integram este contrato o Anexo I (Descrição dos Serviços) e o Anexo II (Matriz de Severidade)."
- DOC-B, cl. 12.1 (par. 38): "12.1 Integram este contrato o Anexo I (Descrição dos Serviços) e o Anexo IV (Matriz de Severidade)."
- DOC-B, título do anexo existente (par. 45): "Anexo II – Matriz de Severidade"
- DOC-B, cl. 4.3 (par. 17): "conforme a Matriz de Severidade do Anexo II"
- **Citação verificada:** Sim (DOC-A e DOC-B)

**Ponto exato da diferença**
| Elemento | DOC-A | DOC-B |
|---|---|---|
| Anexo I (Descrição dos Serviços) | integra | igual |
| Anexo que contém a Matriz de Severidade | Anexo II (existe, p. 7) | Anexo IV (não existe) |
| Anexos efetivamente presentes | I e II | I e II (par. 43 e 45) |

**Análise**
A mudança e o defeito estão no mesmo item, então há um único achado. Em DOC-B, `Anexo IV` aparece só no par. 38; `Anexo III` não aparece; os anexos presentes são I e II. A mesma Matriz é chamada de Anexo II na cl. 4.3 e de Anexo IV na cl. 12.1. Provavelmente é erro de digitação, mas não dá para concluir isso pelo documento. Do jeito que está, a cláusula de integração não lista o anexo que contém os prazos.

**Impacto / risco**
Abre margem para questionar se a Matriz de Severidade (Anexo II) integra o contrato. Os prazos de média e baixa severidade só estão nela.

**Recomendação**
Corrigir a remissão (Anexo II) ou anexar o Anexo IV, se ele existir em outro documento.

**Verificado (revisor):** ☐

---

### ACH-009 — A Cláusula 6 usa CLIENTE, termo não definido, no lugar de CONTRATANTE

- **Tipo:** TER / ALTERADO
- **Severidade:** Média. Âncora: termo não definido usado no lugar do definido, com sentido inferível pelo contexto.
- **Confiança:** Alta
- **Tópico:** Obrigações da CONTRATANTE
- **Padrão entre documentos:** A ≠ B

**Evidências**
- DOC-A, título (p. 4): "Cláusula 6 – Das Obrigações da CONTRATANTE"
- DOC-A, cl. 6.1 (p. 4): "6.1 A CONTRATANTE deverá fornecer à CONTRATADA acesso remoto ao ambiente do sistema, nos termos da política de segurança da informação da CONTRATANTE."
- DOC-A, cl. 6.2 (p. 4): "6.2 A CONTRATANTE deverá designar um gestor do contrato, responsável por acompanhar a execução dos serviços."
- DOC-B, título (par. 21): "Cláusula 6 – Das Obrigações do CLIENTE"
- DOC-B, cl. 6.1 (par. 22): "6.1 O CLIENTE deverá fornecer à CONTRATADA acesso remoto ao ambiente do sistema, nos termos da política de segurança da informação do CLIENTE."
- DOC-B, cl. 6.2 (par. 23): "6.2 O CLIENTE deverá designar um gestor do contrato, responsável por acompanhar a execução dos serviços."
- Definição das partes, igual nos dois: DOC-A, cl. 1.1 (p. 2): "1.1 BETA LOGÍSTICA S.A., doravante denominada CONTRATANTE, e ALFA SISTEMAS LTDA., doravante denominada CONTRATADA [...]" · DOC-B, cl. 1.1 (par. 9): "1.1 BETA LOGÍSTICA S.A., doravante denominada CONTRATANTE, e ALFA SISTEMAS LTDA., doravante denominada CONTRATADA [...]"
- **Citação verificada:** Sim (DOC-A e DOC-B)

**Ponto exato da diferença**
| Elemento | DOC-A | DOC-B |
|---|---|---|
| Parte obrigada (título, 6.1, 6.2) | CONTRATANTE (definida na cl. 1.1) | CLIENTE (não definido) |
| Titular da política de segurança (6.1) | CONTRATANTE | CLIENTE |
| Obrigações: acesso remoto; designar gestor | presentes | igual |

**Análise**
Em DOC-B, `CLIENTE` aparece 4 vezes, todas na Cláusula 6 (par. 21–23). `doravante` só ocorre no par. 9, que define CONTRATANTE e CONTRATADA. Em todas as outras cláusulas, DOC-B continua usando CONTRATANTE (por exemplo, a cl. 7.1, par. 25). Pelo contexto, dá para inferir que CLIENTE = CONTRATANTE, mas essa equivalência não está escrita. A mudança e o defeito estão no mesmo item, então há um único achado.

**Impacto / risco**
Abre margem para alegar que as obrigações da Cláusula 6 (dar acesso remoto, designar gestor) não têm parte obrigada definida.

**Recomendação**
Padronizar para CONTRATANTE, ou definir CLIENTE na cl. 1.1.

**Verificado (revisor):** ☐

---

### ACH-010 — Nova condição: a rescisão pela CONTRATANTE depende de aprovação da Diretoria Jurídica

- **Tipo:** DIV / INCLUÍDO
- **Severidade:** Média. Âncora: acrescenta etapa procedimental (aprovação interna antes de rescindir) a uma regra que continua existindo.
- **Confiança:** Alta
- **Tópico:** Rescisão
- **Padrão entre documentos:** A ≠ B

**Evidências**
- DOC-A, cl. 9.1 (p. 5): "9.1 Qualquer das partes poderá rescindir este contrato mediante notificação por escrito, com antecedência mínima de 30 (trinta) dias." A Cláusula 9 de DOC-A tem só o item 9.1; logo depois vem a Cláusula 10 (p. 5).
- DOC-B, cl. 9.1 (par. 31): "9.1 Qualquer das partes poderá rescindir este contrato mediante notificação por escrito, com antecedência mínima de 30 (trinta) dias."
- DOC-B, cl. 9.2 (par. 32): "9.2 A rescisão por iniciativa da CONTRATANTE dependerá de prévia aprovação de sua Diretoria Jurídica."
- **Citação verificada:** Sim (DOC-A e DOC-B)

**Ponto exato da diferença**
| Elemento | DOC-A | DOC-B |
|---|---|---|
| Direito de rescindir; forma; aviso prévio | qualquer parte; por escrito; 30 dias | igual |
| Condição adicional para a CONTRATANTE | nenhuma | prévia aprovação da sua Diretoria Jurídica |
| Condição adicional para a CONTRATADA | nenhuma | nenhuma |

**Análise**
O tema existe nos dois documentos e DOC-B acrescenta uma condição, então é DIV (e não EXC). A condição só se aplica à CONTRATANTE, o que torna a rescisão assimétrica. É um requisito de governança interna dela, que a CONTRATADA não tem como verificar. `Diretoria` aparece uma única vez (par. 32), e DOC-B não diz como a aprovação é comprovada nem o que acontece com uma notificação enviada sem ela. A eficácia dessa condição perante a CONTRATADA é questão jurídica (especialista).

**Impacto / risco**
A CONTRATADA pode contestar uma rescisão alegando falta de aprovação prévia, o que atrasa ou invalida a saída da CONTRATANTE.

**Recomendação**
Confirmar se a condição deve mesmo constar do contrato ou só de norma interna. Se ficar, definir como a aprovação será comprovada.

**Verificado (revisor):** ☐

## 5. Itens convergentes

**Identificação e partes**
- **Título** (EQV-L) — DOC-A p. 1: "CONTRATO DE PRESTAÇÃO DE SERVIÇOS DE SUPORTE TÉCNICO E MANUTENÇÃO DE SOFTWARE" · DOC-B par. 1: "CONTRATO DE PRESTAÇÃO DE SERVIÇOS DE SUPORTE TÉCNICO E MANUTENÇÃO DE SOFTWARE"
- **Número do contrato** (EQV-L) — DOC-A p. 1: "Contrato nº 041/2026" · DOC-B par. 2: "Contrato nº 041/2026"
- **Partes na capa** (EQV-L) — DOC-A p. 1: "CONTRATANTE: Beta Logística S.A." / "CONTRATADA: Alfa Sistemas Ltda." · DOC-B par. 5–6: "CONTRATANTE: Beta Logística S.A." / "CONTRATADA: Alfa Sistemas Ltda."
- **Aviso de documento fictício** (EQV-L) — DOC-A p. 1: "Documento fictício, elaborado exclusivamente para testes." · DOC-B par. 7: "Documento fictício, elaborado exclusivamente para testes."
- **Cl. 1.1 – Partes** (EQV-L) — DOC-A p. 2: "celebram o presente contrato, que se regerá pelas cláusulas a seguir" · DOC-B par. 9: "celebram o presente contrato, que se regerá pelas cláusulas a seguir"

**Objeto**
- **Cl. 2.1 – Objeto** (EQV-L) — DOC-A p. 2: "serviços de suporte técnico e manutenção corretiva e evolutiva do sistema de gestão de frota" · DOC-B par. 11: "serviços de suporte técnico e manutenção corretiva e evolutiva do sistema de gestão de frota"
- **Anexo I – Descrição dos Serviços** (EQV-L) — DOC-A p. 7: "manutenção evolutiva limitada a 40 (quarenta) horas mensais" · DOC-B par. 44: "manutenção evolutiva limitada a 40 (quarenta) horas mensais" (texto integral idêntico)

**Prazos de atendimento**
- **Cl. 4.1 – Início do atendimento crítico** (EQV-L) — DOC-A p. 3: "em até 4 (quatro) horas corridas, contadas da abertura do chamado" · DOC-B par. 15: "em até 4 (quatro) horas corridas, contadas da abertura do chamado"
- **Cl. 4.3 – Severidade baixa** (EQV-L; ver ACH-004) — DOC-A p. 3: "serão atendidos em até 5 (cinco) dias úteis" · DOC-B par. 17: "serão atendidos em até 5 (cinco) dias úteis"
- **Anexo II – linha Crítica** (EQV-L) — DOC-A p. 7 · Tabela 1: "Início em até 4 horas corridas" · DOC-B Tabela 1, linha 2, col. 3: "Início em até 4 horas corridas"
- **Anexo II – linha Média** (EQV-L) — DOC-A p. 7 · Tabela 1: "Até 2 dias úteis" · DOC-B Tabela 1, linha 3, col. 3: "Até 2 dias úteis"

**Obrigações da CONTRATADA**
- **Cl. 5.1 – Equipe certificada** (EQV-L) — DOC-A p. 3: "manter equipe técnica com certificação no sistema objeto deste contrato" · DOC-B par. 19: "manter equipe técnica com certificação no sistema objeto deste contrato"
- **Sigilo** (EQV-L, realocado: DOC-A cl. 5.3 → DOC-B cl. 11.1, agora em cláusula própria, DOC-B par. 35: "Cláusula 11 – Da Confidencialidade") — DOC-A p. 3: "durante a vigência e por 5 (cinco) anos após o seu término" · DOC-B par. 36: "durante a vigência e por 5 (cinco) anos após o seu término"
- **Proteção de dados pessoais** (EQV-L, renumerado: DOC-A cl. 11.1 → DOC-B cl. 10.1) — DOC-A p. 5: "exclusivamente para a execução do objeto deste contrato, observada a Lei nº 13.709/2018" · DOC-B par. 34: "exclusivamente para a execução do objeto deste contrato, observada a Lei nº 13.709/2018"

**Preço e pagamento**
- **Cl. 7.1 – Valor mensal** (EQV-L) — DOC-A p. 4: "o valor mensal de R$ 18.500,00 (dezoito mil e quinhentos reais)" · DOC-B par. 25: "o valor mensal de R$ 18.500,00 (dezoito mil e quinhentos reais)"
- **Cl. 7.2 – Prazo de pagamento** (EQV-S) — DOC-A p. 4: "em até 30 (trinta) dias após o recebimento da nota fiscal" · DOC-B par. 26: "no prazo máximo de trinta dias, contado do recebimento da nota fiscal". Mesmo prazo, mesmo marco e mesma (falta de) indicação de contagem; só a redação muda.
- **Cl. 7.3 – Reajuste** (EQV-L) — DOC-A p. 4: "reajustado anualmente pela variação do IPCA" · DOC-B par. 27: "reajustado anualmente pela variação do IPCA"

**Rescisão, foro e assinaturas**
- **Cl. 9.1 – Rescisão com aviso prévio** (EQV-L; ver ACH-010) — DOC-A p. 5: "com antecedência mínima de 30 (trinta) dias" · DOC-B par. 31: "com antecedência mínima de 30 (trinta) dias"
- **Cl. 12.2 – Foro** (EQV-L) — DOC-A p. 6: "Fica eleito o foro da Comarca de São Paulo/SP" · DOC-B par. 39: "Fica eleito o foro da Comarca de São Paulo/SP"
- **Linhas de assinatura** (EQV-L) — DOC-A p. 6: "BETA LOGÍSTICA S.A. (CONTRATANTE)" / "ALFA SISTEMAS LTDA. (CONTRATADA)" · DOC-B par. 41–42: "BETA LOGÍSTICA S.A. (CONTRATANTE)" / "ALFA SISTEMAS LTDA. (CONTRATADA)"

Títulos de cláusula: idênticos, exceto o da Cláusula 6 (ACH-009) e as Cláusulas 10 e 11, renumeradas (ACH-007 e itens de sigilo e proteção de dados acima).

## 6. Declaração de cobertura e limitações

**Analisado**
- DOC-A: páginas físicas 1 a 7, todas, incluindo capa, rodapés e a tabela do Anexo II (p. 7). Sem OCR.
- DOC-B: parágrafos 1 a 45 e Tabela 1 (4 linhas × 3 colunas), todos. Não há cabeçalho, rodapé, comentários nem alterações controladas.

**Não analisado:** `docProps/thumbnail.jpeg` de DOC-B (miniatura do modelo, não é conteúdo contratual). Metadados dos arquivos aparecem só em Observações.

**Reconciliação:** todos os itens normativos dos dois documentos foram classificados em um achado (ACH-001 a ACH-010) ou nos itens convergentes. Versão e data de emissão estão no inventário. A data de assinatura só virou achado porque a cl. 3.1 a usa como marco (ACH-001).

**Verificação das citações:** a conferência foi automatizada e cobriu 100% das citações (acima do mínimo exigido). Cada trecho foi comparado caractere por caractere com o texto extraído, no localizador indicado: a página física em DOC-A e o parágrafo ou célula em DOC-B. As quebras de linha do PDF foram normalizadas como espaço.
- Citações das Evidências: 33 conferidas, 33 confirmadas, 0 corrigidas, 0 divergentes, 0 indisponíveis.
- Trechos entre aspas nas demais seções (Itens convergentes, Análise, Observações, Seção 2): 55 conferidos, 55 confirmados, 0 divergentes do original. Antes disso, a primeira passada corrigiu 9 trechos: em 5, as aspas foram removidas e o texto virou paráfrase ou rótulo (títulos de ACH-006, ACH-008 e ACH-009, Análise de ACH-004, Seção 2); 4 receberam localizador explícito (Análise de ACH-006, item de sigilo, Observação 3).

**Limitações**
- ACH-001 depende da premissa P2. Os dois documentos têm as linhas de assinatura em branco, e a data de assinatura efetiva não está comprovada.
- A validade jurídica de ACH-006 (sanção indefinida), ACH-007 (eventual exigência legal de seguro) e ACH-010 (condição interna para rescindir) não foi avaliada e precisa de especialista.

**Observações não comparativas** (questões iguais nos dois documentos ou de metadados; fora da contagem de achados)
1. **Prazo de pagamento sem tipo de contagem.** Nos dois documentos, a cl. 7.2 não diz se os dias são corridos ou úteis. DOC-A p. 4: "em até 30 (trinta) dias após o recebimento da nota fiscal" · DOC-B par. 26: "no prazo máximo de trinta dias, contado do recebimento da nota fiscal".
2. **Severidades média e baixa sem prazo de conclusão.** Para a severidade crítica há prazo de início (cl. 4.1) e de conclusão (cl. 4.2). Para média e baixa, só há prazo de atendimento, sem dizer se é de início ou de solução. DOC-A p. 3 e DOC-B par. 17 (cl. 4.3): "serão atendidos em até 5 (cinco) dias úteis". A severidade média só aparece no Anexo II, nos dois documentos.
3. **Horário de suporte × prazo crítico em horas corridas.** Nos dois documentos, o Anexo I limita o suporte a dias úteis em horário comercial (DOC-A p. 7: "Suporte técnico remoto em dias úteis, das 8h às 18h" · DOC-B par. 44: "Suporte técnico remoto em dias úteis, das 8h às 18h"), enquanto a cl. 4.1 exige início em horas corridas (DOC-A p. 3: "em até 4 (quatro) horas corridas" · DOC-B par. 15: "em até 4 (quatro) horas corridas"). Não está claro se um chamado crítico aberto fora do horário de suporte precisa ser atendido fora desse horário.
4. **Reajuste sem data-base.** A cl. 7.3 dos dois documentos não define a data-base nem o período de apuração do IPCA (DOC-A p. 4; DOC-B par. 27).
5. **Metadados de arquivo.** O PDF de DOC-A foi gerado em 14/10/2026, depois da data do documento. O .docx de DOC-B tem criação e modificação em 23/12/2013 (padrão do gerador `python-docx`), o que não bate com a data do documento (02/09/2026). Isso não afeta a cronologia, que é dada pela versão e pela data escritas no texto.

## 7. Questões em aberto

- **Q1** — DOC-B substitui DOC-A como novo instrumento, com vigência a partir de 02/09/2026, ou consolida alterações mantendo a vigência iniciada em 10/03/2026? A forma escolhida é compatível com a cl. 3.1, que prevê prorrogação por termo aditivo? Ref.: ACH-001.
- **Q2** — Qual prazo de correção de falha crítica vale: 30 ou 45 dias corridos? Ref.: ACH-002.
- **Q3** — Qual prazo vale para a severidade baixa (5 ou 10 dias úteis)? Em DOC-B, qual prevalece: a cl. 4.3 ou o Anexo II? Ref.: ACH-003, ACH-004.
- **Q4** — O relatório mensal de desempenho passou a ser facultativo de propósito? Ref.: ACH-005.
- **Q5** — Quais são as medidas pretendidas na cl. 8.1 de DOC-B? A multa de 2% sobre o valor mensal, por ocorrência, deve ser mantida? Ref.: ACH-006.
- **Q6** — A remoção do seguro de responsabilidade civil profissional (R$ 500.000,00) foi intencional? Ref.: ACH-007.
- **Q7** — O Anexo IV citado na cl. 12.1 de DOC-B é erro de digitação (Anexo II) ou um anexo que não foi juntado? Ref.: ACH-008, ACH-004.
- **Q8** — CLIENTE, na Cláusula 6 de DOC-B, é a CONTRATANTE? O termo deve ser padronizado ou definido? Ref.: ACH-009.
- **Q9** — A aprovação prévia da Diretoria Jurídica para rescindir deve constar do contrato? Se sim, como será comprovada à CONTRATADA? Ref.: ACH-010.
