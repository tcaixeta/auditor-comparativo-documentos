## Análise comparativa: Contrato nº 041/2026, v1.0 (DOC-A) × v2.0 (DOC-B)

> Os achados abaixo são indícios. Só devem embasar decisões depois que um revisor humano conferir cada evidência no documento original (campo **Verificado**).

### 1. Identificação e escopo

| ID        | Título                                                       | Versão | Data       | Emissor / partes                                             | Páginas                    | Esquema de localização                                       | Integridade                                                  |
| --------- | ------------------------------------------------------------ | ------ | ---------- | ------------------------------------------------------------ | -------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **DOC-A** | Contrato de Prestação de Serviços de Suporte Técnico e Manutenção de Software, Contrato nº 041/2026 | 1.0    | 10/03/2026 | Emissor não identificado. Partes: Beta Logística S.A. (CONTRATANTE) e Alfa Sistemas Ltda. (CONTRATADA) | 7 físicas (A4)             | Cláusula + **página física** (p. 1 = capa). O rodapé impresso “Página N de 6” começa na p. física 2, então página impressa = física − 1. Uso a física. | Texto extraível nas 7 páginas, sem OCR. 1 tabela (Anexo II, p. 7). |
| **DOC-B** | Mesmo título                                                 | 2.0    | 02/09/2026 | Mesmo do DOC-A                                               | Sem paginação fixa (.docx) | Numeração de cláusula. Anexos: título + linha/coluna da tabela. | Sem alterações controladas e sem comentários (verificado no XML). Metadados com datas incoerentes (ver ACH-011). |

### 2. Relação entre os documentos e premissas

**Relação identificada: versões (v1.0 → v2.0).** Os dois documentos têm o mesmo número (041/2026), o mesmo título, as mesmas partes e a mesma estrutura de cláusulas. As capas dizem “Versão 1.0” e “Versão 2.0”, e a data de DOC-B é posterior.

**Premissa:** DOC-B é a versão posterior e substitui DOC-A por inteiro. Por isso as diferenças são classificadas como INCLUÍDO, REMOVIDO ou ALTERADO, no sentido A → B. Nenhum documento está “certo” por mérito.

**O que muda se a premissa estiver errada:**

- **Se DOC-B for uma minuta em negociação, ainda não assinada:** os achados passam a ser propostas de alteração a aceitar ou recusar, e DOC-A continua valendo.
- **Se DOC-B for um aditivo ou complemento:** as remoções (seguro, multa) não revogariam automaticamente as cláusulas de DOC-A. Mas DOC-B não se declara aditivo, e nenhum dos dois tem cláusula de precedência ou de substituição (ver ACH-010).

### 3. Resumo quantitativo

**Itens:** 11 achados e 21 itens convergentes (20 EQV-L e 1 EQV-S).

| Tipo                      | Crítica | Alta  | Média | Informativa | Total  |
| ------------------------- | ------- | ----- | ----- | ----------- | ------ |
| CTR (contradição)         | –       | 3     | –     | –           | 3      |
| NCL (não claro)           | 1       | –     | –     | –           | 1      |
| EXC (exclusivo)           | –       | 1     | 1     | –           | 2      |
| INT (contradição interna) | –       | 1     | –     | 1           | 2      |
| REF (referência quebrada) | –       | 1     | –     | –           | 1      |
| TER (terminologia)        | –       | –     | 1     | –           | 1      |
| DIV (divergência)         | –       | –     | 1     | –           | 1      |
| **Total**                 | **1**   | **6** | **3** | **1**       | **11** |

**Carga de revisão humana:** 1 item NÃO CLARO (ACH-001) e 0 em REQUER REVISÃO.

**Leitura geral (análise):** todas as mudanças de conteúdo da v2.0 reduzem obrigações ou sanções da CONTRATADA:

- o prazo de correção de falha crítica aumenta 50%;
- o relatório mensal passa a ser opcional;
- a multa é retirada;
- a cláusula de seguro é retirada;
- o prazo de severidade baixa dobra no Anexo II.

A única inclusão (9.2) restringe a CONTRATANTE. A v2.0 também trouxe três defeitos de redação que não existiam na v1.0: o “Anexo IV” inexistente, o termo “CLIENTE” sem definição e a contradição entre a cl. 4.3 e o Anexo II.

### 4. Achados detalhados

#### ACH-001 — Multa por descumprimento de prazos substituída por “medidas cabíveis” sem definição

- **Tipo:** NCL / ALTERADO
- **Severidade:** Crítica
- **Confiança:** Alta (quanto à remoção da multa)
- **Tópico:** Penalidades
- **Padrão entre documentos:** A ≠ B

**Evidências**

- DOC-A, cl. 8.1 (p. 4): “O descumprimento dos prazos previstos na Cláusula 4 sujeitará a CONTRATADA a multa de 2% (dois por cento) sobre o valor mensal, por ocorrência.”
- DOC-B, cl. 8.1: **NÃO CLARO.** “O descumprimento dos prazos previstos na Cláusula 4 poderá ensejar a aplicação das medidas cabíveis.” A cláusula trata das consequências do descumprimento, mas não define a sanção, o valor, a base de cálculo, a incidência nem quem sofre a sanção.
- Busca em todo o DOC-B: “multa” e “sanção” não aparecem; “penalidade” aparece só no título da Cláusula 8.
- **Citação verificada:** Sim (DOC-A e DOC-B)

**Ponto exato da diferença**

| Elemento            | DOC-A                            | DOC-B                                    |
| ------------------- | -------------------------------- | ---------------------------------------- |
| Modalidade          | “sujeitará” (consequência certa) | “poderá ensejar” (consequência eventual) |
| Sanção              | multa                            | “medidas cabíveis” (sem definição)       |
| Valor / base        | 2% sobre o valor mensal          | não definido                             |
| Incidência          | por ocorrência                   | não definida                             |
| Quem sofre a sanção | CONTRATADA (expresso)            | não nomeado                              |

**Análise**
 Não é uma CTR, porque em tese “medidas cabíveis” pode incluir uma multa. Mas o texto de DOC-B não traz nenhuma sanção objetiva que se possa cobrar. Somado a ACH-002, ACH-003 e ACH-006, os SLAs da Cláusula 4 ficam sem o seu instrumento de cobrança. Saber se uma “medida cabível” genérica sustenta a cobrança de multa é questão jurídica e exige um especialista.

**Impacto / risco**
 A CONTRATANTE perde o mecanismo financeiro objetivo para cobrar atrasos, e passa a haver risco de disputa sobre quais medidas são cabíveis.

**Recomendação**
 Confirmar se a retirada da multa foi intencional. Se não foi, restaurar a redação de DOC-A. Se foi, definir as medidas de forma concreta. Submeter ao jurídico.

**Verificado (revisor):** ☐

------

#### ACH-002 — Prazo para concluir a correção de falha crítica passou de 30 para 45 dias corridos

- **Tipo:** CTR / ALTERADO
- **Severidade:** Alta
- **Confiança:** Alta
- **Tópico:** Prazos de atendimento
- **Padrão:** A ≠ B

**Evidências**

- DOC-A, cl. 4.2 (p. 3): “A CONTRATADA deverá concluir a correção de falhas de severidade crítica em até 30 (trinta) dias corridos, contados da abertura do chamado.”
- DOC-B, cl. 4.2: “A CONTRATADA deverá concluir a correção de falhas de severidade crítica em até 45 (quarenta e cinco) dias corridos, contados da abertura do chamado.”
- **Citação verificada:** Sim

**Ponto exato da diferença**

| Elemento      | DOC-A               | DOC-B                       |
| ------------- | ------------------- | --------------------------- |
| Prazo         | 30 dias             | 45 dias                     |
| Contagem      | corridos            | corridos (igual)            |
| Marco inicial | abertura do chamado | abertura do chamado (igual) |
| Modalidade    | deverá              | deverá (igual)              |

**Análise**
 São dois prazos para a mesma obrigação e eles se excluem. Uma correção concluída entre o 31º e o 45º dia é descumprimento pela v1.0 e cumprimento pela v2.0. Isso equivale a um aumento de 50% no prazo.

**Impacto / risco**
 O sistema de gestão de frota pode ficar indisponível por mais tempo sem que haja descumprimento contratual.

**Recomendação**
 Confirmar se a mudança foi intencional e registrar a justificativa.

**Verificado (revisor):** ☐

------

#### ACH-003 — Relatório mensal de desempenho deixou de ser obrigatório

- **Tipo:** CTR / ALTERADO
- **Severidade:** Alta
- **Confiança:** Alta
- **Tópico:** Obrigações da CONTRATADA
- **Padrão:** A ≠ B

**Evidências**

- DOC-A, cl. 5.2 (p. 3): “A CONTRATADA deverá emitir relatório mensal de desempenho até o 5º (quinto) dia útil de cada mês.”
- DOC-B, cl. 5.2: “A CONTRATADA poderá emitir relatório mensal de desempenho até o 5º (quinto) dia útil de cada mês.”
- **Citação verificada:** Sim

**Ponto exato da diferença**

| Elemento          | DOC-A                  | DOC-B                  |
| ----------------- | ---------------------- | ---------------------- |
| Modalidade        | **deverá** (obrigação) | **poderá** (faculdade) |
| Restante da frase | idêntico               | idêntico               |

**Análise**
 A única mudança é o verbo, mas as duas versões não podem valer ao mesmo tempo: na v1.0 a obrigação existe e na v2.0 não existe. Em ambas, o relatório é o único instrumento contratual de prestação de contas sobre o desempenho. Sem ele, a CONTRATANTE pode perder a base para medir os SLAs da Cláusula 4. Além disso, a v2.0 ficou com uma redação estranha: um prazo (“até o 5º dia útil”) para algo que é apenas facultativo.

**Impacto / risco**
 Perda de visibilidade sobre o desempenho e maior dificuldade de provar um descumprimento.

**Recomendação**
 Confirmar se a mudança foi intencional. Se a intenção era manter a obrigação, restaurar “deverá”.

**Verificado (revisor):** ☐

------

#### ACH-004 — Cláusula de seguro de responsabilidade civil profissional removida

- **Tipo:** EXC / REMOVIDO
- **Severidade:** Alta
- **Confiança:** Alta
- **Tópico:** Seguro / garantias
- **Padrão:** A ≠ B

**Evidências**

- DOC-A, cl. 10.1 (p. 5): “A CONTRATADA manterá, durante toda a vigência deste contrato, apólice de seguro de responsabilidade civil profissional com cobertura mínima de R$ 500.000,00 (quinhentos mil reais).”
- DOC-B: **NÃO PRESENTE.**
  - Seções verificadas: o documento inteiro (capa, Cláusulas 1 a 12, fecho, Anexos I e II), com atenção à Cl. 5 (Obrigações da CONTRATADA), à Cl. 8 (Penalidades) e à posição da antiga Cl. 10, que agora é “Da Proteção de Dados Pessoais”.
  - Termos buscados: “seguro”, “apólice”, “responsabilidade civil”, “cobertura”, “garantia”.
  - Conteúdo relacionado: nenhum.
- **Citação verificada:** Sim (DOC-A)

**Ponto exato da diferença**

| Elemento                    | DOC-A                        | DOC-B   |
| --------------------------- | ---------------------------- | ------- |
| Obrigação de manter apólice | sim, durante toda a vigência | ausente |
| Cobertura mínima            | R$ 500.000,00                | ausente |

**Análise**
 A remoção veio junto com uma renumeração: a antiga Cl. 11 virou Cl. 10 e foi criada uma nova Cl. 11 (Confidencialidade). Quem comparar as versões pelo número da cláusula pode não perceber a remoção.

**Impacto / risco**
 A CONTRATANTE perde a garantia financeira contra danos causados pela CONTRATADA na prestação do serviço.

**Recomendação**
 Confirmar se a remoção foi intencional. Se a garantia continua necessária, reinserir a cláusula.

**Verificado (revisor):** ☐

------

#### ACH-005 — DOC-B: o prazo de severidade baixa diverge entre a cl. 4.3 (5 dias úteis) e o Anexo II (10 dias úteis)

- **Tipo:** INT
- **Severidade:** Alta
- **Confiança:** Alta
- **Tópico:** Prazos de atendimento
- **Padrão:** contradição interna de B (em A, cláusula e anexo são coerentes)

**Evidências**

- DOC-B, cl. 4.3: “Os chamados de severidade baixa serão atendidos em até 5 (cinco) dias úteis, conforme a Matriz de Severidade do Anexo II.”
- DOC-B, Anexo II, tabela, linha “Baixa”, coluna “Prazo de atendimento”: “Até 10 dias úteis”
- **Citação verificada:** Sim

**Ponto exato da diferença**

| Elemento                    | DOC-B cl. 4.3 | DOC-B Anexo II |
| --------------------------- | ------------- | -------------- |
| Prazo para severidade baixa | 5 dias úteis  | 10 dias úteis  |

**Análise**
 A cl. 4.3 remete à própria matriz (“conforme a Matriz [...] do Anexo II”), e a matriz traz outro valor. DOC-B não tem regra de precedência entre o corpo do contrato e os anexos (a cl. 12.1 apenas lista os anexos). Por isso não é possível saber, só pelo texto, qual prazo vale.

**Impacto / risco**
 Disputa sobre o SLA e sobre quando há descumprimento.

**Recomendação**
 Harmonizar os dois valores, decidindo entre 5 e 10 dias (ver ACH-006).

**Verificado (revisor):** ☐

------

#### ACH-006 — Anexo II: prazo de severidade baixa passou de 5 para 10 dias úteis

- **Tipo:** CTR / ALTERADO
- **Severidade:** Alta
- **Confiança:** Alta
- **Tópico:** Matriz de Severidade
- **Padrão:** A ≠ B

**Evidências**

- DOC-A, Anexo II (p. 7 · Tabela 1), linha “Baixa”, coluna “Prazo de atendimento”: “Até 5 dias úteis”
- DOC-B, Anexo II, tabela, linha “Baixa”, coluna “Prazo de atendimento”: “Até 10 dias úteis”
- **Citação verificada:** Sim

**Ponto exato da diferença**

| Elemento                | DOC-A                                     | DOC-B         |
| ----------------------- | ----------------------------------------- | ------------- |
| Prazo                   | 5 dias úteis                              | 10 dias úteis |
| Descrição da severidade | “Dúvida ou falha sem impacto operacional” | igual         |

**Análise**
 O prazo foi alterado no anexo, mas não na cl. 4.3, e é daí que nasce o ACH-005. O padrão sugere uma atualização parcial, mas isso é uma inferência (confiança média).

**Impacto / risco**
 O prazo para chamados de baixa severidade dobra.

**Recomendação**
 Decidir o valor pretendido e aplicá-lo de forma coerente na cl. 4.3 e no Anexo II.

**Verificado (revisor):** ☐

------

#### ACH-007 — DOC-B cl. 12.1 incorpora ao contrato um “Anexo IV” que não existe

- **Tipo:** REF / ALTERADO
- **Severidade:** Alta
- **Confiança:** Alta
- **Tópico:** Disposições gerais / anexos
- **Padrão:** A ≠ B

**Evidências**

- DOC-A, cl. 12.1 (p. 6): “Integram este contrato o Anexo I (Descrição dos Serviços) e o Anexo II (Matriz de Severidade).”
- DOC-B, cl. 12.1: “Integram este contrato o Anexo I (Descrição dos Serviços) e o Anexo IV (Matriz de Severidade).”
- DOC-B, título do anexo: “Anexo II – Matriz de Severidade”
- Busca em DOC-B: “Anexo IV” aparece só na cl. 12.1; “Anexo III” não aparece. Os anexos existentes são o I e o II. Já a cl. 4.3 de DOC-B cita “Anexo II”.
- **Citação verificada:** Sim

**Ponto exato da diferença**

| Elemento                              | DOC-A | DOC-B            |
| ------------------------------------- | ----- | ---------------- |
| Número do anexo da Matriz na cl. 12.1 | II    | IV (inexistente) |

**Análise**
 Provavelmente é um erro de digitação (inferência). O risco é que se argumente que o Anexo II não foi formalmente incorporado ao contrato. Isso pesa porque o SLA de severidade **média** (“Até 2 dias úteis”) existe apenas no Anexo II, nos dois documentos: a Cláusula 4 não trata da severidade média.

**Impacto / risco**
 A Matriz de Severidade pode perder a base contratual, levando junto o SLA de severidade média.

**Recomendação**
 Corrigir a cl. 12.1 para “Anexo II”.

**Verificado (revisor):** ☐

------

#### ACH-008 — Termo “CLIENTE” usado na Cláusula 6 de DOC-B sem definição

- **Tipo:** TER / ALTERADO
- **Severidade:** Média
- **Confiança:** Alta para o fato; Média para a equivalência CLIENTE = CONTRATANTE, que é inferência
- **Tópico:** Obrigações da CONTRATANTE
- **Padrão:** A ≠ B

**Evidências**

- DOC-A, título da Cl. 6 (p. 4): “Cláusula 6 – Das Obrigações da CONTRATANTE”
- DOC-A, cl. 6.1 (p. 4): “A CONTRATANTE deverá fornecer à CONTRATADA acesso remoto ao ambiente do sistema, nos termos da política de segurança da informação da CONTRATANTE.”
- DOC-A, cl. 6.2 (p. 4): “A CONTRATANTE deverá designar um gestor do contrato, responsável por acompanhar a execução dos serviços.”
- DOC-B, título da Cl. 6: “Cláusula 6 – Das Obrigações do CLIENTE”
- DOC-B, cl. 6.1: “O CLIENTE deverá fornecer à CONTRATADA acesso remoto ao ambiente do sistema, nos termos da política de segurança da informação do CLIENTE.”
- DOC-B, cl. 6.2: “O CLIENTE deverá designar um gestor do contrato, responsável por acompanhar a execução dos serviços.”
- DOC-B, cl. 1.1, onde os termos são definidos: “BETA LOGÍSTICA S.A., doravante denominada CONTRATANTE, e ALFA SISTEMAS LTDA., doravante denominada CONTRATADA”
- Busca em DOC-B: “CLIENTE” aparece só na Cl. 6 (título, 6.1 e 6.2). O restante do documento continua usando CONTRATANTE (1.1, 2.1, 7.1, 9.2, 11.1 e assinaturas).
- **Citação verificada:** Sim

**Ponto exato da diferença**

| Elemento                          | DOC-A                         | DOC-B                   |
| --------------------------------- | ----------------------------- | ----------------------- |
| Quem tem as obrigações da Cl. 6   | CONTRATANTE (definido na 1.1) | CLIENTE (sem definição) |
| Dono da política de segurança     | CONTRATANTE                   | CLIENTE                 |
| Restante do conteúdo de 6.1 e 6.2 | idêntico                      | idêntico                |

**Análise**
 É razoável entender que CLIENTE é a Beta Logística, mas o termo não está definido. E ele aparece justamente nas obrigações que tornam o serviço possível: dar acesso remoto e designar o gestor do contrato.

**Impacto / risco**
 Discussão sobre a quem cabem essas obrigações.

**Recomendação**
 Substituir “CLIENTE” por “CONTRATANTE”.

**Verificado (revisor):** ☐

------

#### ACH-009 — Incluída a exigência de aprovação prévia da Diretoria Jurídica para rescisão pela CONTRATANTE

- **Tipo:** EXC / INCLUÍDO
- **Severidade:** Média
- **Confiança:** Alta
- **Tópico:** Rescisão
- **Padrão:** A ≠ B

**Evidências**

- DOC-B, cl. 9.2: “A rescisão por iniciativa da CONTRATANTE dependerá de prévia aprovação de sua Diretoria Jurídica.”
- DOC-A: **NÃO PRESENTE.**
  - Seções verificadas: Cl. 9 (Rescisão), Cl. 6 (Obrigações da CONTRATANTE), Cl. 12 (Disposições Gerais).
  - Termos buscados: “aprovação”, “Diretoria”, “Jurídica”, “rescisão”.
  - Conteúdo relacionado, mas não equivalente: DOC-A, cl. 9.1 (p. 5): “Qualquer das partes poderá rescindir este contrato mediante notificação por escrito, com antecedência mínima de 30 (trinta) dias.” Essa redação se repete idêntica em DOC-B 9.1.
- **Citação verificada:** Sim

**Ponto exato da diferença**

| Elemento                              | DOC-A                          | DOC-B                                                        |
| ------------------------------------- | ------------------------------ | ------------------------------------------------------------ |
| Condição para a CONTRATANTE rescindir | apenas notificação com 30 dias | notificação com 30 dias **+** aprovação prévia da Diretoria Jurídica |
| Condição para a CONTRATADA rescindir  | apenas notificação             | apenas notificação (inalterada)                              |

**Análise**
 Não há contradição interna com a 9.1: a 9.2 acrescenta uma condição e as duas convivem. Mas a cláusula coloca uma regra de governança interna da CONTRATANTE dentro de um contrato bilateral e só restringe um dos lados. Fica em aberto se uma notificação feita sem essa aprovação vale perante a CONTRATADA, e como a CONTRATADA confirmaria a aprovação. O efeito jurídico precisa ser avaliado por um especialista.

**Impacto / risco**
 Possível contestação de uma rescisão feita pela CONTRATANTE.

**Recomendação**
 Confirmar se a inclusão foi intencional. Se a regra for só de política interna, avaliar mantê-la fora do contrato. Se ficar no contrato, definir o efeito da falta de aprovação.

**Verificado (revisor):** ☐

------

#### ACH-010 — Nova data de emissão e assinatura sem esclarecer o início da vigência nem o instrumento da alteração

- **Tipo:** DIV / ALTERADO
- **Severidade:** Média
- **Confiança:** Média
- **Tópico:** Identificação / Vigência
- **Padrão:** A ≠ B

**Evidências**

- DOC-A, capa (p. 1): “Versão 1.0” e “Data: 10 de março de 2026”. Fecho (p. 6): “São Paulo, 10 de março de 2026.”
- DOC-B, capa: “Versão 2.0” e “Data: 2 de setembro de 2026”. Fecho: “São Paulo, 2 de setembro de 2026.”
- Cl. 3.1, idêntica nos dois (DOC-A p. 2 e DOC-B): “O presente contrato vigorará pelo prazo de 12 (doze) meses, contados da data de sua assinatura, podendo ser prorrogado mediante termo aditivo.”
- **Citação verificada:** Sim

**Ponto exato da diferença**

| Elemento                              | DOC-A                    | DOC-B                                                  |
| ------------------------------------- | ------------------------ | ------------------------------------------------------ |
| Versão                                | 1.0                      | 2.0                                                    |
| Data do documento e do fecho          | 10/03/2026               | 02/09/2026                                             |
| Marco de início da vigência (cl. 3.1) | “data de sua assinatura” | “data de sua assinatura” (texto igual, data diferente) |

**Análise**
 Se a v2.0 for assinada em 02/09/2026, a vigência “contada da data de sua assinatura” pode ser lida como reiniciada, terminando por volta de setembro de 2027 em vez de março de 2027. Além disso, DOC-B se apresenta como “Versão 2.0”, e não como termo aditivo, e não declara que substitui a v1.0 nem lista o que mudou. Não há como saber pelo texto se a v2.0 foi assinada. A forma jurídica correta deve ser avaliada por um especialista.

**Impacto / risco**
 Incerteza sobre a data de término, sobre o reajuste anual pelo IPCA (cl. 7.3) e sobre qual versão está valendo.

**Recomendação**
 Declarar em DOC-B se ela substitui a v1.0, de quando conta a vigência e qual o instrumento formal da alteração.

**Verificado (revisor):** ☐

------

#### ACH-011 — Metadados do DOC-B incompatíveis com a data do documento

- **Tipo:** INT
- **Severidade:** Informativa
- **Confiança:** Alta
- **Tópico:** Metadados

**Evidências**

- DOC-B, docProps/core.xml: `dcterms:created` = “2013-12-23T23:15:00Z”, `dcterms:modified` = “2013-12-23T23:15:00Z”, `dc:creator` = “python-docx”
- DOC-B, capa: “Data: 2 de setembro de 2026”
- Para comparação, os metadados do PDF de DOC-A (CreationDate 14/10/2026) são posteriores à data do documento. Isso é compatível com uma exportação feita depois e não gera achado.
- **Citação verificada:** Sim

**Análise**
 Os metadados de DOC-B provavelmente vieram do modelo usado para gerar o arquivo. Não têm efeito normativo, mas impedem usar os metadados como prova de quando a v2.0 foi produzida.

**Recomendação**
 Nenhuma ação contratual. Apenas não usar os metadados como evidência de cronologia.

**Verificado (revisor):** ☐

### 5. Itens convergentes

**Capa e partes (EQV-L)**

- **Título** — DOC-A p. 1 · DOC-B capa: “CONTRATO DE PRESTAÇÃO DE SERVIÇOS DE SUPORTE TÉCNICO E MANUTENÇÃO DE SOFTWARE”
- **Número do contrato** — DOC-A p. 1 · DOC-B capa: “Contrato nº 041/2026”
- **Partes na capa** — DOC-A p. 1 · DOC-B capa: “CONTRATANTE: Beta Logística S.A.” e “CONTRATADA: Alfa Sistemas Ltda.”
- **Nota de documento fictício** — DOC-A p. 1 · DOC-B capa: “Documento fictício, elaborado exclusivamente para testes.”
- **Cl. 1.1 Partes** — DOC-A p. 2 · DOC-B 1.1: “BETA LOGÍSTICA S.A., doravante denominada CONTRATANTE [...]”
- **Blocos de assinatura** — DOC-A p. 6 · DOC-B fecho: “BETA LOGÍSTICA S.A. (CONTRATANTE)” e “ALFA SISTEMAS LTDA. (CONTRATADA)”

**Objeto e vigência (EQV-L)**

- **Cl. 2.1 Objeto** — DOC-A p. 2 · DOC-B 2.1: “serviços de suporte técnico e manutenção corretiva e evolutiva do sistema de gestão de frota”
- **Cl. 3.1 Vigência** (texto idêntico; o efeito está tratado em ACH-010) — DOC-A p. 2 · DOC-B 3.1: “vigorará pelo prazo de 12 (doze) meses”

**Prazos (EQV-L)**

- **Cl. 4.1 Início do atendimento de chamado crítico** — DOC-A p. 3 · DOC-B 4.1: “em até 4 (quatro) horas corridas”
- **Cl. 4.3 Severidade baixa** (texto idêntico entre os documentos; ver ACH-005 e ACH-006) — DOC-A p. 3 · DOC-B 4.3: “em até 5 (cinco) dias úteis”
- **Anexo II, severidade crítica** — DOC-A p. 7 · DOC-B Anexo II: “Início em até 4 horas corridas”
- **Anexo II, severidade média** — DOC-A p. 7 · DOC-B Anexo II: “Até 2 dias úteis”

**Obrigações (EQV-L)**

- **Cl. 5.1 Equipe certificada** — DOC-A p. 3 · DOC-B 5.1: “manter equipe técnica com certificação”
- **Sigilo** (realocado: DOC-A cl. 5.3 → DOC-B cl. 11.1) — DOC-A p. 3 · DOC-B 11.1: “por 5 (cinco) anos após o seu término”
- **Proteção de dados** (renumerado: DOC-A cl. 11.1 → DOC-B cl. 10.1) — DOC-A p. 5 · DOC-B 10.1: “observada a Lei nº 13.709/2018”

**Preço e pagamento**

- **Cl. 7.1 Valor mensal** (EQV-L) — DOC-A p. 4 · DOC-B 7.1: “R$ 18.500,00 (dezoito mil e quinhentos reais)”
- **Cl. 7.2 Prazo de pagamento** (**EQV-S**; o mesmo prazo e o mesmo marco, nenhum dos dois diz se os dias são corridos ou úteis) — DOC-A p. 4: “em até 30 (trinta) dias após o recebimento da nota fiscal” · DOC-B 7.2: “no prazo máximo de trinta dias, contado do recebimento da nota fiscal”
- **Cl. 7.3 Reajuste** (EQV-L) — DOC-A p. 4 · DOC-B 7.3: “reajustado anualmente pela variação do IPCA”

**Rescisão, foro e escopo (EQV-L)**

- **Cl. 9.1 Rescisão** — DOC-A p. 5 · DOC-B 9.1: “com antecedência mínima de 30 (trinta) dias”
- **Cl. 12.2 Foro** — DOC-A p. 6 · DOC-B 12.2: “foro da Comarca de São Paulo/SP”
- **Anexo I Descrição dos serviços** — DOC-A p. 7 · DOC-B Anexo I: “manutenção evolutiva limitada a 40 (quarenta) horas mensais”

### 6. Declaração de cobertura e limitações

**O que foi analisado**

- **DOC-A:** as 7 páginas físicas por inteiro (capa, Cl. 1 a 12, fecho, Anexos I e II), extraídas página a página. A tabela do Anexo II (p. 7) também foi lida. Nenhuma página precisou de OCR. Os rodapés (“Contrato nº 041/2026 – Versão 1.0 · Página N de 6”) não foram tratados como conteúdo normativo.
- **DOC-B:** os 57 parágrafos do documento (capa, Cl. 1 a 12, fecho, Anexos I e II com tabela de 4 linhas × 3 colunas) e os metadados (core.xml e app.xml). Não há alterações controladas nem comentários.
- **Conteúdo não analisado:** nenhum. A validade jurídica das cláusulas ficou fora do escopo; os pontos que dependem dela estão sinalizados para um especialista.

**Verificação das citações**

- 60 citações de texto conferidas mecanicamente (100%) contra o texto extraído, no localizador indicado. Nos trechos de DOC-A, a busca foi restrita à página citada.
- 0 corrigidas, 0 divergentes, 0 indisponíveis.
- Os 3 valores de metadados (ACH-011) foram conferidos diretamente no XML.
- Na comparação, as diferenças de espaço e quebra de linha foram ignoradas, porque o PDF quebra as linhas no meio das frases.

**Limitações**

- DOC-B não tem paginação, então os localizadores são cláusulas e células de tabela.
- A relação “versões, com substituição integral” é uma premissa inferida (ver §2).

**Observações críticas** (temas que nenhum dos dois documentos trata bem; não são achados comparativos)

1. Nenhum dos dois define prazo de **conclusão** para as severidades média e baixa. Também não fica claro se “atendidos” (cl. 4.3) e “Prazo de atendimento” (Anexo II) significam início ou conclusão do atendimento.
2. A Cláusula 4 não trata da severidade média, que só aparece no Anexo II (ver ACH-007).
3. Nenhum dos dois tem regra de precedência entre o corpo do contrato e os anexos, nem cláusula de substituição de versões.

### 7. Questões em aberto

- **Q1 —** A retirada da multa de 2% por ocorrência foi intencional? Se foi, quais são as “medidas cabíveis”? Ref.: ACH-001
- **Q2 —** O novo prazo de 45 dias corridos para correção de falha crítica foi acordado? Ref.: ACH-002
- **Q3 —** O relatório mensal deve continuar obrigatório? Ref.: ACH-003
- **Q4 —** A exigência de seguro de R$ 500.000,00 foi dispensada de propósito? Ref.: ACH-004
- **Q5 —** O prazo para severidade baixa é de 5 ou de 10 dias úteis? Ref.: ACH-005, ACH-006
- **Q6 —** Confirmar que o “Anexo IV” da cl. 12.1 é o Anexo II. Ref.: ACH-007
- **Q7 —** Confirmar que “CLIENTE” é a CONTRATANTE e padronizar o termo. Ref.: ACH-008
- **Q8 —** O que acontece se a CONTRATANTE notificar a rescisão sem a aprovação da Diretoria Jurídica? A regra deve ficar no contrato? Ref.: ACH-009
- **Q9 —** A v2.0 foi assinada? Ela substitui a v1.0? De quando conta a vigência? Por que não foi feita por termo aditivo? Ref.: ACH-010, §2
- **Q10 —** Deve ser incluída uma regra de precedência entre o corpo do contrato e os anexos? Ref.: ACH-005, ACH-007

Se quiser, exporto os achados para uma planilha no formato da seção 8, com a coluna **Verificado** em branco para o revisor.