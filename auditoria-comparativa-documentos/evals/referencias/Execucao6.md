# Análise comparativa — Contrato nº 041/2026 · v1.0 (DOC-A) × v2.0 (DOC-B)

> Os achados abaixo são indícios organizados para revisão. Só devem embasar decisões depois que um revisor humano conferir cada evidência no documento original (campo **Verificado**).

## 1. Identificação e escopo

| ID        | Título                                                       | Versão | Data                  | Emissor                                                      | Páginas / extensão                                    | Esquema de localização                                       | Integridade                                                  |
| --------- | ------------------------------------------------------------ | ------ | --------------------- | ------------------------------------------------------------ | ----------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **DOC-A** | Contrato de Prestação de Serviços de Suporte Técnico e Manutenção de Software — Contrato nº 041/2026 (arquivo `DOC-A_contrato_v1.pdf`) | 1.0    | 10 de março de 2026   | Não declarado. Partes: Beta Logística S.A. (CONTRATANTE) e Alfa Sistemas Ltda. (CONTRATADA). Metadado `Author`: Kit de teste | 7 páginas físicas (PDF/A4)                            | Cláusula + **página física** (`cl. 4.2 (p. 3)`). A numeração impressa no rodapé começa na p. física 2 (Página 1 de 6): **página física = impressa + 1**; a capa (p. 1) não tem número. Tabela do Anexo II: `Tabela 1, linha L, col. C` (linha 1 = cabeçalho) | Texto extraível nas 7 páginas, sem OCR. A tabela do Anexo II é texto posicionado (sem estrutura de tabela no PDF); linhas e colunas reconstruídas pelo alinhamento. Quebras de linha do PDF normalizadas para um espaço nas citações (não há hifenização) |
| **DOC-B** | Mesmo título — Contrato nº 041/2026 (arquivo `DOC-B_contrato_v2.docx`) | 2.0    | 2 de setembro de 2026 | Não declarado. Mesmas partes. Metadado `creator`: python-docx | 45 parágrafos de corpo + 1 tabela; sem paginação fixa | Cláusula + **número do parágrafo** (`cl. 4.2 (par. 16)`). Regra: cada parágrafo do corpo, em ordem, a partir de 1, incluindo títulos (não há parágrafos vazios). Tabela fora da contagem: `Tabela 1, linha L, col. C`, situada após o par. 45 | Sem alterações controladas, comentários, texto oculto, campos, cabeçalho ou rodapé. Metadados do arquivo com data de 2013 (ver Observações) |

Estrutura (igual nos dois): capa; Cláusulas 1 a 12; fecho com local e data; linhas de assinatura; Anexo I (Descrição dos Serviços); Anexo II (Matriz de Severidade). Diferenças de estrutura em DOC-B: a Cláusula 10 (Do Seguro) não existe; a antiga Cláusula 11 (Proteção de Dados) passa a ser a 10; surge a Cláusula 11 (Da Confidencialidade), que recebe o conteúdo do item 5.3 de DOC-A.

## 2. Relação entre os documentos e premissas

**Relação identificada: versões (v1.0 → v2.0) do mesmo contrato.** Base: mesmo número (041/2026), mesmo título, mesmas partes, mesma estrutura, versões 1.0 e 2.0 com datas em sequência (10/03/2026 e 02/09/2026). A relação não foi informada; é inferida.

**Efeito na classificação:** as diferenças recebem os rótulos `INCLUÍDO`, `REMOVIDO` ou `ALTERADO`, medidos de DOC-A para DOC-B. A análise descreve a mudança e o seu impacto; não decide qual versão está correta.

| Premissa                                                     | Fundamento                                                   | O que muda se estiver errada                                 |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **P1** — DOC-B é a versão posterior e pretende substituir DOC-A | Numeração de versão e datas                                  | Se DOC-B for uma proposta alternativa ou minuta não adotada, a relação passa a ser de pares independentes: os tipos (CTR, DIV etc.) se mantêm, mas os rótulos de versão perdem sentido e nenhuma diferença é, em si, uma mudança |
| **P2** — DOC-B não é um termo aditivo                        | DOC-B não se declara aditivo nem menciona DOC-A; reproduz o contrato inteiro | Se fosse aditivo, a relação seria hierárquica e seria preciso uma regra de precedência, que nenhum dos dois declara |
| **P3** — a data do fecho é a data de assinatura              | Fecho com local e data imediatamente antes das linhas de assinatura, nos dois documentos | As linhas de assinatura estão em branco nos dois; se a data do fecho não for a de assinatura, o ACH-001 passa a NCL (marco incerto) |

## 3. Resumo quantitativo

**Achados: 10** · Itens convergentes: 22

| Tipo                               | Qtd. | Achados                            |
| ---------------------------------- | ---- | ---------------------------------- |
| CTR — Contradição                  | 4    | ACH-001, ACH-002, ACH-003, ACH-005 |
| INT — Contradição interna          | 1    | ACH-004                            |
| NCL — Não claro                    | 1    | ACH-006                            |
| EXC — Exclusivo / não presente     | 1    | ACH-007                            |
| REF — Referência quebrada          | 1    | ACH-008                            |
| TER — Inconsistência terminológica | 1    | ACH-009                            |
| DIV — Divergência                  | 1    | ACH-010                            |
| REV — Requer revisão               | 0    | —                                  |

| Severidade          | Qtd. |
| ------------------- | ---- |
| Crítica             | 1    |
| Alta                | 7    |
| Média               | 2    |
| Baixa / Informativa | 0    |

**Carga de revisão humana:** 1 item em NÃO CLARO (ACH-006) e 0 em REQUER REVISÃO. Os 10 achados aguardam o campo **Verificado**.

**Leitura geral (análise):** a v2.0 muda o marco da vigência (ACH-001) e, no conjunto, afrouxa obrigações e mecanismos de controle sobre a CONTRATADA: prazo de correção maior, prazo maior para chamados de baixa severidade no anexo, relatório facultativo, multa substituída por redação vaga e seguro removido (ACH-002, 003, 005, 006, 007). Ao mesmo tempo, acrescenta uma condição à rescisão pela CONTRATANTE (ACH-010). A v2.0 também traz três defeitos que a v1.0 não tinha: cláusula × anexo com prazos diferentes, referência a um anexo inexistente e uso de um termo não definido (ACH-004, 008, 009). Os achados 004 e 008 se somam: em DOC-B, não se sabe qual prazo vale para severidade baixa nem se o Anexo II integra o contrato. Esse efeito combinado não altera a severidade individual de cada achado.

## 4. Achados detalhados

### ACH-001 — Marco inicial da vigência muda com a nova data de assinatura

- **Tipo:** CTR / ALTERADO
- **Severidade:** Crítica
- **Confiança:** Média
- **Tópico:** Vigência
- **Padrão entre documentos:** A ≠ B

**Evidências**

- DOC-A, cl. 3.1 (p. 2): "3.1 O presente contrato vigorará pelo prazo de 12 (doze) meses, contados da data de sua assinatura, podendo ser prorrogado mediante termo aditivo."
- DOC-A, fecho (p. 6): "São Paulo, 10 de março de 2026."
- DOC-A, capa (p. 1): "Data: 10 de março de 2026"
- DOC-B, cl. 3.1 (par. 13): "3.1 O presente contrato vigorará pelo prazo de 12 (doze) meses, contados da data de sua assinatura, podendo ser prorrogado mediante termo aditivo."
- DOC-B, fecho (par. 40): "São Paulo, 2 de setembro de 2026."
- DOC-B, capa (par. 4): "Data: 2 de setembro de 2026"
- **Citação verificada:** Sim (DOC-A e DOC-B)

**Ponto exato da diferença**

| Elemento                                                     | DOC-A               | DOC-B                 |
| ------------------------------------------------------------ | ------------------- | --------------------- |
| Regra de vigência (cl. 3.1)                                  | igual               | igual                 |
| Data do fecho (marco da cl. 3.1, pela P3)                    | 10 de março de 2026 | 2 de setembro de 2026 |
| Termo final resultante (cálculo da análise, não escrito nos documentos) | 10/03/2027          | 02/09/2027            |
| Declaração de que substitui a versão anterior                | —                   | não há                |

**Análise** A regra da cl. 3.1 é idêntica, mas o marco que ela usa (a data de assinatura) muda. Lido nos próprios termos, cada documento dá ao mesmo contrato nº 041/2026 um início de vigência diferente, com quase seis meses de distância; os dois inícios não podem valer ao mesmo tempo. Daí a classificação CTR pela regra de desempate (mesmo item, valor diferente). A data em si não é o achado; o achado é o efeito sobre a vigência. Confiança Média porque: (a) as linhas de assinatura estão em branco nos dois documentos e a leitura depende da P3; (b) DOC-B não diz se reinicia a vigência ou apenas consolida o contrato original; (c) a cl. 3.1 só admite prorrogação mediante termo aditivo, e DOC-B não se identifica como aditivo. Se DOC-B for uma consolidação que mantém o marco original, o achado passa a NCL.

**Impacto / risco** Incerteza sobre a data de término (março × setembro de 2027), sobre a data-base do reajuste anual (cl. 7.3) e sobre qual conjunto de cláusulas regeu o período entre março e setembro de 2026 (por exemplo, multa e seguro, que existem só na v1.0).

**Recomendação** Os responsáveis devem declarar em DOC-B se ele substitui DOC-A, a partir de quando suas cláusulas se aplicam e de quando se conta a vigência. A necessidade de formalizar a mudança por termo aditivo deve ser avaliada por especialista jurídico.

**Verificado (revisor):** ☐

------

### ACH-002 — Prazo de correção de falhas críticas passa de 30 para 45 dias corridos

- **Tipo:** CTR / ALTERADO
- **Severidade:** Alta
- **Confiança:** Alta
- **Tópico:** Prazos de atendimento
- **Padrão entre documentos:** A ≠ B

**Evidências**

- DOC-A, cl. 4.2 (p. 3): "4.2 A CONTRATADA deverá concluir a correção de falhas de severidade crítica em até 30 (trinta) dias corridos, contados da abertura do chamado."
- DOC-B, cl. 4.2 (par. 16): "4.2 A CONTRATADA deverá concluir a correção de falhas de severidade crítica em até 45 (quarenta e cinco) dias corridos, contados da abertura do chamado."
- **Citação verificada:** Sim (DOC-A e DOC-B)

**Ponto exato da diferença**

| Elemento                 | DOC-A               | DOC-B                       |
| ------------------------ | ------------------- | --------------------------- |
| Prazo                    | 30 dias             | 45 dias                     |
| Tipo de contagem         | corridos            | corridos (igual)            |
| Marco inicial            | abertura do chamado | abertura do chamado (igual) |
| Modalidade / responsável | deverá / CONTRATADA | igual                       |

**Análise** Mesma obrigação, dois prazos: não podem valer juntos (CTR pela regra de desempate). O prazo aumenta 50%. Severidade Alta pela âncora de prazo de correção alterado (o exemplo da âncora é justamente 30 → 45 dias). Em DOC-A, o descumprimento desse prazo gera multa (cl. 8.1); em DOC-B, a consequência ficou indefinida (ver ACH-006).

**Impacto / risco** Falhas que deixam o sistema indisponível podem ficar até 15 dias a mais sem correção sem caracterizar descumprimento.

**Recomendação** Confirmar qual prazo é o pretendido e registrar a justificativa da mudança.

**Verificado (revisor):** ☐

------

### ACH-003 — Anexo II: prazo para severidade baixa passa de 5 para 10 dias úteis

- **Tipo:** CTR / ALTERADO
- **Severidade:** Alta
- **Confiança:** Alta
- **Tópico:** Prazos de atendimento (Matriz de Severidade)
- **Padrão entre documentos:** A ≠ B

**Evidências**

- DOC-A, Anexo II, Tabela 1, linha 4, col. 1 (p. 7): "Baixa"
- DOC-A, Anexo II, Tabela 1, linha 4, col. 3 (p. 7): "Até 5 dias úteis"
- DOC-B, Anexo II, Tabela 1, linha 4, col. 1 (após par. 45): "Baixa"
- DOC-B, Anexo II, Tabela 1, linha 4, col. 3 (após par. 45): "Até 10 dias úteis"
- **Citação verificada:** Sim (DOC-A e DOC-B)

**Ponto exato da diferença**

| Elemento                                | DOC-A  | DOC-B         |
| --------------------------------------- | ------ | ------------- |
| Prazo de atendimento — severidade baixa | 5 dias | 10 dias       |
| Tipo de contagem                        | úteis  | úteis (igual) |
| Descrição da severidade (col. 2)        | igual  | igual         |

**Análise** O mesmo item da matriz tem dois prazos (CTR). O prazo dobra. Em DOC-B, esse novo valor também contradiz a cl. 4.3 do próprio DOC-B, o que é tratado em achado separado (ver ACH-004).

**Impacto / risco** Prazo mais longo para dúvidas e falhas sem impacto operacional; somado ao ACH-004, o prazo aplicável fica indeterminado.

**Recomendação** Confirmar se a alteração para 10 dias úteis é intencional e, se for, alinhar a cl. 4.3 (ACH-004).

**Verificado (revisor):** ☐

------

### ACH-004 — DOC-B: a cl. 4.3 (5 dias úteis) contradiz o Anexo II (10 dias úteis)

- **Tipo:** INT
- **Severidade:** Alta
- **Confiança:** Alta
- **Tópico:** Prazos de atendimento
- **Padrão entre documentos:** interno a DOC-B (em DOC-A, a cl. 4.3 e o Anexo II coincidem em 5 dias úteis)

**Evidências**

- DOC-B, cl. 4.3 (par. 17): "4.3 Os chamados de severidade baixa serão atendidos em até 5 (cinco) dias úteis, conforme a Matriz de Severidade do Anexo II."
- DOC-B, Anexo II, Tabela 1, linha 4, col. 3 (após par. 45): "Até 10 dias úteis"
- **Citação verificada:** Sim (DOC-B)

**Ponto exato da diferença**

| Elemento                 | DOC-B cl. 4.3               | DOC-B Anexo II |
| ------------------------ | --------------------------- | -------------- |
| Prazo — severidade baixa | 5 dias úteis                | 10 dias úteis  |
| Remissão                 | remete à Matriz do Anexo II | —              |

**Análise** A cl. 4.3 afirma que o prazo é o da Matriz de Severidade, mas a matriz diz outra coisa. Os dois valores não podem valer juntos e DOC-B não tem regra de precedência entre cláusulas e anexos. O problema se agrava com o ACH-008: a cl. 12.1 de DOC-B não lista o Anexo II entre os documentos que integram o contrato. Severidade Alta pela âncora de contradição entre cláusula e anexo com prazos diferentes.

**Impacto / risco** Disputa sobre o prazo aplicável aos chamados de severidade baixa; cada parte pode invocar o valor que a favorece.

**Recomendação** Alinhar a cl. 4.3 e o Anexo II e incluir uma regra de precedência entre o corpo do contrato e os anexos.

**Verificado (revisor):** ☐

------

### ACH-005 — Relatório mensal de desempenho passa de obrigatório a facultativo

- **Tipo:** CTR / ALTERADO
- **Severidade:** Alta
- **Confiança:** Alta
- **Tópico:** Obrigações da CONTRATADA
- **Padrão entre documentos:** A ≠ B

**Evidências**

- DOC-A, cl. 5.2 (p. 3): "5.2 A CONTRATADA deverá emitir relatório mensal de desempenho até o 5º (quinto) dia útil de cada mês."
- DOC-B, cl. 5.2 (par. 20): "5.2 A CONTRATADA poderá emitir relatório mensal de desempenho até o 5º (quinto) dia útil de cada mês."
- **Citação verificada:** Sim (DOC-A e DOC-B)

**Ponto exato da diferença**

| Elemento                                  | DOC-A                                               | DOC-B              |
| ----------------------------------------- | --------------------------------------------------- | ------------------ |
| Modalidade                                | deverá (obrigação)                                  | poderá (faculdade) |
| Objeto, periodicidade, prazo, responsável | relatório mensal, até o quinto dia útil, CONTRATADA | igual              |

**Análise** Única diferença é o verbo modal, mas a regra de desempate trata a passagem de obrigação para faculdade como CTR: o mesmo item não pode ser obrigatório e facultativo. Em DOC-B, nenhuma outra cláusula obriga a CONTRATADA a reportar desempenho, e o prazo de um ato facultativo perde efeito prático. Severidade Alta pela âncora de mecanismo de fiscalização enfraquecido (relatório obrigatório que vira facultativo).

**Impacto / risco** O gestor do contrato (cl. 6.2) perde a fonte periódica de informação para acompanhar prazos e níveis de serviço.

**Recomendação** Confirmar se a mudança é intencional; se o relatório continuar necessário, restabelecer a obrigação.

**Verificado (revisor):** ☐

------

### ACH-006 — Multa de 2% substituída por medidas cabíveis não definidas

- **Tipo:** NCL / ALTERADO
- **Severidade:** Alta
- **Confiança:** Alta
- **Tópico:** Penalidades
- **Padrão entre documentos:** A ≠ B

**Evidências**

- DOC-A, cl. 8.1 (p. 4): "8.1 O descumprimento dos prazos previstos na Cláusula 4 sujeitará a CONTRATADA a multa de 2% (dois por cento) sobre o valor mensal, por ocorrência."
- DOC-B, cl. 8.1 (par. 29): **NÃO CLARO.** "8.1 O descumprimento dos prazos previstos na Cláusula 4 poderá ensejar a aplicação das medidas cabíveis." Trata da consequência do descumprimento, mas não define a medida, o valor, a base de cálculo nem quem a aplica. O termo não é definido em outra parte de DOC-B (termos buscados em todo o documento: `medidas`, `multa`, `penalidade`, `sanção`; `medidas` só ocorre no par. 29; `penalidade` só no título da Cláusula 8, par. 28; `multa` e `sanção` não ocorrem).
- **Citação verificada:** Sim (DOC-A e DOC-B)

**Ponto exato da diferença**

| Elemento                | DOC-A                                   | DOC-B                                  |
| ----------------------- | --------------------------------------- | -------------------------------------- |
| Título da cláusula      | Das Penalidades                         | igual                                  |
| Gatilho                 | descumprimento dos prazos da Cláusula 4 | igual                                  |
| Consequência            | multa                                   | medidas cabíveis (não definidas)       |
| Valor / base de cálculo | 2% sobre o valor mensal                 | não definido                           |
| Incidência              | por ocorrência                          | não definida                           |
| Modalidade              | sujeitará (consequência certa)          | poderá ensejar (consequência eventual) |
| Parte sujeita           | CONTRATADA (expressa)                   | não expressa                           |

**Análise** O tema continua existindo, mas o conteúdo objetivo foi trocado por uma redação vaga: pela regra de desempate, NCL e não EXC. A mudança de modalidade faz parte do mesmo item e não gera achado separado. Severidade Alta pela âncora de sanção removida ou enfraquecida (multa trocada por redação vaga).

**Impacto / risco** Sem valor nem critério definidos, o descumprimento de prazos deixa de ter consequência automática e passa a depender de negociação ou litígio.

**Recomendação** Esclarecer com os responsáveis quais são as medidas pretendidas e defini-las (tipo, valor, base, incidência), ou restabelecer a multa.

**Verificado (revisor):** ☐

------

### ACH-007 — Cláusula de seguro de responsabilidade civil removida

- **Tipo:** EXC / REMOVIDO
- **Severidade:** Alta
- **Confiança:** Alta
- **Tópico:** Seguro / garantias
- **Padrão entre documentos:** A ≠ B

**Evidências**

- DOC-A, cl. 10.1 (p. 5): "10.1 A CONTRATADA manterá, durante toda a vigência deste contrato, apólice de seguro de responsabilidade civil profissional com cobertura mínima de R$ 500.000,00 (quinhentos mil reais)."
- DOC-B: **NÃO PRESENTE.** Seções verificadas: todo o documento (par. 1–45 e Tabela 1), em especial cl. 5 (Obrigações da CONTRATADA, par. 18–20), cl. 8 (Penalidades, par. 28–29), cl. 10 (par. 33–34, que nesta versão trata de proteção de dados), cl. 11 (Confidencialidade, par. 35–36), cl. 12 (Disposições Gerais, par. 37–39) e Anexo I (par. 43–44). Termos buscados: `seguro`, `segur`, `apólice`, `apolice`, `responsabilidade civil`, `responsabilidade`, `cobertura`, `indeniz`, `garantia`, `sinistro`, `500.000`. Conteúdo relacionado: nenhum (o radical `segur` só aparece em segurança da informação, cl. 6.1, par. 22, que não trata de seguro).
- **Citação verificada:** Sim (DOC-A)

**Ponto exato da diferença**

| Elemento                                      | DOC-A           | DOC-B        |
| --------------------------------------------- | --------------- | ------------ |
| Obrigação de manter seguro de RC profissional | sim             | não presente |
| Cobertura mínima                              | R$ 500.000,00   | —            |
| Período                                       | toda a vigência | —            |

**Análise** O tema inteiro deixa de existir: EXC. A renumeração esconde a remoção, porque em DOC-B a Cláusula 10 continua existindo, mas trata de proteção de dados. Severidade Alta pela âncora de remoção de garantia ou seguro.

**Impacto / risco** A CONTRATANTE perde a garantia de cobertura para danos causados pela prestação dos serviços.

**Recomendação** Confirmar se a remoção foi intencional. Se foi, registrar a decisão; se não foi, restabelecer a cláusula.

**Verificado (revisor):** ☐

------

### ACH-008 — Cl. 12.1 de DOC-B integra ao contrato um Anexo IV inexistente

- **Tipo:** REF
- **Severidade:** Alta
- **Confiança:** Alta
- **Tópico:** Disposições gerais / anexos
- **Padrão entre documentos:** A ≠ B (defeito presente só em DOC-B)

**Evidências**

- DOC-A, cl. 12.1 (p. 6): "12.1 Integram este contrato o Anexo I (Descrição dos Serviços) e o Anexo II (Matriz de Severidade)."
- DOC-B, cl. 12.1 (par. 38): "12.1 Integram este contrato o Anexo I (Descrição dos Serviços) e o Anexo IV (Matriz de Severidade)."
- DOC-B, título do anexo (par. 45): "Anexo II – Matriz de Severidade"
- DOC-B, cl. 4.3 (par. 17): "[...] conforme a Matriz de Severidade do Anexo II."
- DOC-B: nenhum anexo com o número IV. Anexos existentes: Anexo I (par. 43) e Anexo II (par. 45). Termos buscados: `Anexo III`, `Anexo IV`; `Anexo IV` só ocorre no par. 38.
- **Citação verificada:** Sim (DOC-A e DOC-B)

**Ponto exato da diferença**

| Elemento                              | DOC-A                            | DOC-B    |
| ------------------------------------- | -------------------------------- | -------- |
| Primeiro anexo integrado              | Anexo I (Descrição dos Serviços) | igual    |
| Segundo anexo integrado — número      | Anexo II                         | Anexo IV |
| Segundo anexo integrado — nome        | Matriz de Severidade             | igual    |
| O anexo referido existe no documento? | sim                              | não      |

**Análise** O nome coincide com o do Anexo II, o que sugere erro de numeração, mas isso é uma inferência que os documentos não confirmam. Do jeito que está escrito, a cláusula de integração de DOC-B não inclui o anexo que traz a matriz de prazos, e a cl. 4.3 continua remetendo ao Anexo II. Severidade Alta pela âncora de cláusula de integração que deixa de listar o anexo com os SLAs.

**Impacto / risco** Questionamento sobre a força contratual da Matriz de Severidade, a única fonte do prazo para severidade média e do prazo de 10 dias para severidade baixa (ver ACH-004).

**Recomendação** Corrigir a remissão na cl. 12.1 ou, se houver de fato um Anexo IV, incluí-lo.

**Verificado (revisor):** ☐

------

### ACH-009 — Cláusula 6 passa a chamar a contratante de CLIENTE, termo não definido

- **Tipo:** TER / ALTERADO
- **Severidade:** Média
- **Confiança:** Alta
- **Tópico:** Partes / Obrigações da contratante
- **Padrão entre documentos:** A ≠ B

**Evidências**

- DOC-A, título da cl. 6 (p. 4): "Cláusula 6 – Das Obrigações da CONTRATANTE"
- DOC-A, cl. 6.1 (p. 4): "6.1 A CONTRATANTE deverá fornecer à CONTRATADA acesso remoto ao ambiente do sistema, nos termos da política de segurança da informação da CONTRATANTE."
- DOC-A, cl. 6.2 (p. 4): "6.2 A CONTRATANTE deverá designar um gestor do contrato, responsável por acompanhar a execução dos serviços."
- DOC-B, título da cl. 6 (par. 21): "Cláusula 6 – Das Obrigações do CLIENTE"
- DOC-B, cl. 6.1 (par. 22): "6.1 O CLIENTE deverá fornecer à CONTRATADA acesso remoto ao ambiente do sistema, nos termos da política de segurança da informação do CLIENTE."
- DOC-B, cl. 6.2 (par. 23): "6.2 O CLIENTE deverá designar um gestor do contrato, responsável por acompanhar a execução dos serviços."
- DOC-B, cl. 1.1 (par. 9): "1.1 BETA LOGÍSTICA S.A., doravante denominada CONTRATANTE [...]"
- DOC-B: o termo `CLIENTE` só ocorre nos par. 21–23 e não é definido; nas demais cláusulas, DOC-B continua usando CONTRATANTE (par. 5, 9, 11, 25, 32, 36, 41).
- **Citação verificada:** Sim (DOC-A e DOC-B)

**Ponto exato da diferença**

| Elemento                                       | DOC-A       | DOC-B   |
| ---------------------------------------------- | ----------- | ------- |
| Designação da parte na cl. 6                   | CONTRATANTE | CLIENTE |
| Termo definido na cl. 1.1?                     | sim         | não     |
| Dona da política de segurança (6.1)            | CONTRATANTE | CLIENTE |
| Obrigações (acesso remoto; gestor do contrato) | igual       | igual   |

**Análise** Pelo contexto, dá para inferir que CLIENTE corresponde à Beta Logística S.A., mas o termo não está definido e convive com o termo definido no mesmo documento. É um único problema (a troca de termo na cl. 6), por isso um único achado. Severidade Média pela âncora de termo não definido usado no lugar do definido, com sentido inferível pelo contexto.

**Impacto / risco** Margem para discutir quem está obrigado a dar acesso remoto e a designar o gestor, e de qual política de segurança se trata.

**Recomendação** Substituir CLIENTE por CONTRATANTE na cl. 6 ou definir o termo na cl. 1.1.

**Verificado (revisor):** ☐

------

### ACH-010 — Rescisão pela CONTRATANTE passa a depender de aprovação da Diretoria Jurídica

- **Tipo:** DIV / INCLUÍDO
- **Severidade:** Média
- **Confiança:** Alta
- **Tópico:** Rescisão
- **Padrão entre documentos:** A ≠ B

**Evidências**

- DOC-A, cl. 9.1 (p. 5): "9.1 Qualquer das partes poderá rescindir este contrato mediante notificação por escrito, com antecedência mínima de 30 (trinta) dias."
- DOC-A: a Cláusula 9 (p. 5) só tem o item 9.1. Termos buscados em todo o documento: `aprovação`, `Diretoria`, `jurídic`. Nenhum encontrado.
- DOC-B, cl. 9.2 (par. 32): "9.2 A rescisão por iniciativa da CONTRATANTE dependerá de prévia aprovação de sua Diretoria Jurídica."
- **Citação verificada:** Sim (DOC-A e DOC-B)

**Ponto exato da diferença**

| Elemento                                          | DOC-A   | DOC-B                                      |
| ------------------------------------------------- | ------- | ------------------------------------------ |
| Regra geral de rescisão (9.1)                     | igual   | igual                                      |
| Condição adicional para rescisão pela CONTRATANTE | nenhuma | prévia aprovação da sua Diretoria Jurídica |
| Condição para rescisão pela CONTRATADA            | nenhuma | nenhuma (igual)                            |

**Análise** DOC-B acrescenta uma condição a uma regra que continua existindo nos dois: DIV pela regra de desempate, e não EXC. A condição cria assimetria entre as partes e não diz o que acontece com uma notificação enviada sem essa aprovação (se é inválida ou se é só descumprimento de um procedimento interno). Severidade Média pela âncora de condição procedimental acrescentada (aprovação interna antes de rescindir).

**Impacto / risco** Possível contestação de rescisões feitas pela CONTRATANTE e atraso no exercício desse direito.

**Recomendação** Esclarecer se a aprovação é condição de validade da rescisão ou apenas um procedimento interno; neste caso, avaliar se ela deve ficar no contrato.

**Verificado (revisor):** ☐

## 5. Itens convergentes

**Identificação e partes**

- **Título** (EQV-L) — DOC-A p. 1: "CONTRATO DE PRESTAÇÃO DE SERVIÇOS DE SUPORTE TÉCNICO E MANUTENÇÃO DE SOFTWARE" · DOC-B par. 1: "CONTRATO DE PRESTAÇÃO DE SERVIÇOS DE SUPORTE TÉCNICO E MANUTENÇÃO DE SOFTWARE"
- **Número do contrato** (EQV-L) — DOC-A p. 1: "Contrato nº 041/2026" · DOC-B par. 2: "Contrato nº 041/2026"
- **Partes na capa** (EQV-L) — DOC-A p. 1: "CONTRATANTE: Beta Logística S.A." · DOC-B par. 5: "CONTRATANTE: Beta Logística S.A."; DOC-A p. 1: "CONTRATADA: Alfa Sistemas Ltda." · DOC-B par. 6: "CONTRATADA: Alfa Sistemas Ltda."
- **Aviso de documento fictício** (EQV-L) — DOC-A p. 1: "Documento fictício, elaborado exclusivamente para testes." · DOC-B par. 7: "Documento fictício, elaborado exclusivamente para testes."
- **Qualificação das partes** (EQV-L) — DOC-A cl. 1.1 (p. 2): "celebram o presente contrato, que se regerá pelas cláusulas a seguir" · DOC-B cl. 1.1 (par. 9): "celebram o presente contrato, que se regerá pelas cláusulas a seguir"
- **Linhas de assinatura** (EQV-L) — DOC-A p. 6: "BETA LOGÍSTICA S.A. (CONTRATANTE)" e "ALFA SISTEMAS LTDA. (CONTRATADA)" · DOC-B par. 41: "BETA LOGÍSTICA S.A. (CONTRATANTE)"; par. 42: "ALFA SISTEMAS LTDA. (CONTRATADA)"

**Objeto e vigência**

- **Objeto** (EQV-L) — DOC-A cl. 2.1 (p. 2): "manutenção corretiva e evolutiva do sistema de gestão de frota" · DOC-B cl. 2.1 (par. 11): "manutenção corretiva e evolutiva do sistema de gestão de frota"
- **Regra de vigência** (EQV-L; ver ACH-001) — DOC-A cl. 3.1 (p. 2): "vigorará pelo prazo de 12 (doze) meses, contados da data de sua assinatura" · DOC-B cl. 3.1 (par. 13): "vigorará pelo prazo de 12 (doze) meses, contados da data de sua assinatura"

**Prazos de atendimento**

- **Início do atendimento crítico** (EQV-L) — DOC-A cl. 4.1 (p. 3): "iniciar o atendimento de chamados de severidade crítica em até 4 (quatro) horas corridas" · DOC-B cl. 4.1 (par. 15): "iniciar o atendimento de chamados de severidade crítica em até 4 (quatro) horas corridas"
- **Prazo para severidade baixa na cláusula** (EQV-L; ver ACH-004) — DOC-A cl. 4.3 (p. 3): "serão atendidos em até 5 (cinco) dias úteis" · DOC-B cl. 4.3 (par. 17): "serão atendidos em até 5 (cinco) dias úteis"

**Obrigações da CONTRATADA**

- **Equipe certificada** (EQV-L) — DOC-A cl. 5.1 (p. 3): "manter equipe técnica com certificação no sistema objeto deste contrato" · DOC-B cl. 5.1 (par. 19): "manter equipe técnica com certificação no sistema objeto deste contrato"
- **Sigilo** (EQV-L, realocado: cl. 5.3 de DOC-A → cl. 11.1 de DOC-B, sob o novo título Cláusula 11 – Da Confidencialidade) — DOC-A cl. 5.3 (p. 3): "durante a vigência e por 5 (cinco) anos após o seu término" · DOC-B cl. 11.1 (par. 36): "durante a vigência e por 5 (cinco) anos após o seu término"

**Preço e pagamento**

- **Valor mensal** (EQV-L) — DOC-A cl. 7.1 (p. 4): "R$ 18.500,00 (dezoito mil e quinhentos reais)" · DOC-B cl. 7.1 (par. 25): "R$ 18.500,00 (dezoito mil e quinhentos reais)"
- **Prazo de pagamento** (EQV-S) — DOC-A cl. 7.2 (p. 4): "em até 30 (trinta) dias após o recebimento da nota fiscal" · DOC-B cl. 7.2 (par. 26): "no prazo máximo de trinta dias, contado do recebimento da nota fiscal"
- **Reajuste** (EQV-L) — DOC-A cl. 7.3 (p. 4): "reajustado anualmente pela variação do IPCA" · DOC-B cl. 7.3 (par. 27): "reajustado anualmente pela variação do IPCA"

**Penalidades e rescisão**

- **Rescisão imotivada** (EQV-L; ver ACH-010) — DOC-A cl. 9.1 (p. 5): "com antecedência mínima de 30 (trinta) dias" · DOC-B cl. 9.1 (par. 31): "com antecedência mínima de 30 (trinta) dias"

**Proteção de dados**

- **LGPD** (EQV-L, realocado: cl. 11.1 de DOC-A → cl. 10.1 de DOC-B, mesmo título) — DOC-A cl. 11.1 (p. 5): "exclusivamente para a execução do objeto deste contrato, observada a Lei nº 13.709/2018" · DOC-B cl. 10.1 (par. 34): "exclusivamente para a execução do objeto deste contrato, observada a Lei nº 13.709/2018"

**Disposições gerais**

- **Foro** (EQV-L) — DOC-A cl. 12.2 (p. 6): "Fica eleito o foro da Comarca de São Paulo/SP" · DOC-B cl. 12.2 (par. 39): "Fica eleito o foro da Comarca de São Paulo/SP"

**Anexos**

- **Anexo I** (EQV-L) — DOC-A p. 7: "manutenção evolutiva limitada a 40 (quarenta) horas mensais" · DOC-B par. 44: "manutenção evolutiva limitada a 40 (quarenta) horas mensais"
- **Anexo II — cabeçalho da tabela** (EQV-L) — DOC-A Tabela 1, linha 1, col. 3 (p. 7): "Prazo de atendimento" · DOC-B Tabela 1, linha 1, col. 3: "Prazo de atendimento"
- **Anexo II — severidade crítica** (EQV-L) — DOC-A Tabela 1, linha 2, col. 3 (p. 7): "Início em até 4 horas corridas" · DOC-B Tabela 1, linha 2, col. 3: "Início em até 4 horas corridas"
- **Anexo II — severidade média** (EQV-L) — DOC-A Tabela 1, linha 3, col. 3 (p. 7): "Até 2 dias úteis" · DOC-B Tabela 1, linha 3, col. 3: "Até 2 dias úteis"

Itens com achado e que, por isso, não aparecem aqui nem em parte: datas da capa e do fecho (ACH-001), cl. 4.2, linha 4 (Baixa) inteira do Anexo II, cl. 5.2, Cláusula 6 inteira, Cláusula 8 inteira (título e 8.1), cl. 9.2, Cláusula 10 de DOC-A e cl. 12.1. Os títulos das demais cláusulas são idênticos nas duas versões, exceto pela renumeração descrita no inventário (Cláusulas 10 e 11).

## 6. Declaração de cobertura e limitações

**Analisado**

- DOC-A: páginas físicas 1 a 7 (capa, Cláusulas 1–12, fecho, assinaturas, Anexos I e II). Nenhuma página com OCR; nenhum trecho ilegível.
- DOC-B: parágrafos 1 a 45 e Tabela 1, inteiros. Sem alterações controladas, comentários, cabeçalho, rodapé ou texto oculto a extrair.
- Reconciliação: todos os itens de cada documento foram classificados em um achado ou nos itens convergentes. Número de versão e datas ficaram no inventário; as datas viraram achado só pelo efeito na cl. 3.1 (ACH-001).

**Não analisado / limites**

- Formatação visual, fontes e leiaute (sem efeito normativo).
- Validade jurídica das cláusulas (ex.: eficácia da cl. 9.2, necessidade de termo aditivo): requer especialista.
- O documento de política de segurança da informação citado na cl. 6.1 não foi fornecido.

**Verificações transversais executadas:** contradição interna (em DOC-A, nenhuma; em DOC-B, ACH-004), terminologia (ACH-009), referências cruzadas (ACH-008; a única remissão a número de cláusula, Cláusula 4 na cl. 8.1, continua correta após a renumeração em DOC-B), dependências ocultas e ambiguidades (Observações) e metadados (Observações).

**Resultado da verificação das citações** (conferência mecânica de cada trecho entre aspas contra o texto extraído, no localizador indicado, cobertura de 100%)

- Evidências dos achados: 32 conferidas, 0 corrigidas, 0 divergentes, 0 indisponíveis. Todos os localizadores conferem com o ponto em que o trecho foi encontrado.
- Itens convergentes: 48 conferidas, 0 corrigidas, 0 divergentes, 0 indisponíveis.
- Trechos entre aspas fora das Evidências (Análise, Ponto exato, Impacto, Recomendação, Observações, Questões): 4 conferidos e literais (3 nas Observações, 1 nas Questões). Durante a revisão, 2 expressões entre aspas que não eram citações (na seção 2) e 8 referências às âncoras de severidade tiveram as aspas removidas.

**Limitações que afetam a confiança:** ausência de assinaturas nos dois documentos (P3); DOC-B sem declaração de substituição ou de vigência própria (P1/P2); tabela do PDF reconstruída por alinhamento (os valores das células conferem com o texto extraído).

**Observações não comparativas** (problemas iguais nos dois documentos; sem ID e fora da contagem)

1. **Atendimento crítico × horário de suporte.** A cl. 4.1 fixa início em até 4 horas corridas (DOC-A p. 3; DOC-B par. 15), mas o Anexo I diz "Suporte técnico remoto em dias úteis, das 8h às 18h" (DOC-A p. 7; DOC-B par. 44). Não fica claro se as 4 horas correm fora do horário de suporte.
2. **Atendido = iniciado ou concluído?** A cl. 4.3 usa "serão atendidos em até 5 (cinco) dias úteis" (DOC-A p. 3; DOC-B par. 17). A matriz explicita início só para severidade crítica. Para média e baixa, não se sabe se o prazo é de início ou de conclusão, e não há prazo de correção para essas severidades.
3. **Alcance da cl. 8.1.** Nas duas versões, a consequência se refere aos "prazos previstos na Cláusula 4" (DOC-A p. 4; DOC-B par. 29). O prazo da severidade média só existe no Anexo II, que fica fora desse alcance.
4. **Dias do pagamento.** A cl. 7.2 não diz se os 30 dias são corridos ou úteis (DOC-A p. 4; DOC-B par. 26).
5. **Data-base do reajuste.** A cl. 7.3 não define a data-base nem o período de apuração do IPCA (DOC-A p. 4; DOC-B par. 27).
6. **Documento externo não integrado.** A cl. 6.1 remete à política de segurança da informação de uma das partes, que não está entre os anexos da cl. 12.1 (DOC-A p. 4; DOC-B par. 22).
7. **Precedência.** Nenhum dos documentos tem regra de precedência entre o corpo do contrato e os anexos.
8. **Assinaturas.** As linhas de assinatura estão em branco nos dois documentos (DOC-A p. 6; DOC-B par. 41–42).
9. **Metadados de arquivo (não afetam a cronologia).** O DOCX tem `created`/`modified` = 2013-12-23T23:15:00Z e `creator` = python-docx, valores padrão da biblioteca geradora e incompatíveis com a data de 02/09/2026. O PDF tem `CreationDate` de 14/10/2026, posterior à data do documento (10/03/2026). A cronologia das versões foi estabelecida pelo conteúdo (número de versão e datas), não pelos metadados.

## 7. Questões em aberto

- **Q1** — DOC-B substitui DOC-A? A partir de quando valem as cláusulas da v2.0, e a vigência de 12 meses é contada de 10/03/2026 ou de 02/09/2026? A mudança precisa ser formalizada por termo aditivo (cl. 3.1)? Ref.: ACH-001.
- **Q2** — Qual é o prazo de correção de falhas críticas: 30 ou 45 dias corridos? Ref.: ACH-002.
- **Q3** — Para severidade baixa, o prazo é de 5 ou de 10 dias úteis, e em DOC-B qual prevalece, a cl. 4.3 ou o Anexo II? Ref.: ACH-003, ACH-004.
- **Q4** — O relatório mensal de desempenho deve continuar obrigatório? Ref.: ACH-005.
- **Q5** — Quais são as "medidas cabíveis" da cl. 8.1 de DOC-B? A multa de 2% foi abandonada de propósito? Ref.: ACH-006.
- **Q6** — A remoção do seguro de responsabilidade civil foi intencional? Ref.: ACH-007.
- **Q7** — O Anexo IV citado na cl. 12.1 de DOC-B é o Anexo II (Matriz de Severidade) ou um anexo que ficou faltando? Ref.: ACH-008.
- **Q8** — CLIENTE, na Cláusula 6 de DOC-B, é a CONTRATANTE? Ref.: ACH-009.
- **Q9** — A aprovação da Diretoria Jurídica (cl. 9.2) é condição de validade da rescisão ou procedimento interno da CONTRATANTE? Ref.: ACH-010.
- **Q10** — As lacunas comuns às duas versões (Observações 1 a 7) serão tratadas na próxima revisão?