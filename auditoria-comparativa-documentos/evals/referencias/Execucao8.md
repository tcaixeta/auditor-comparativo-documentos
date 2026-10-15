# Análise comparativa — Contrato nº 041/2026 · v1.0 (DOC-A) × v2.0 (DOC-B)

> **Aviso ao leitor:** os achados abaixo são indícios organizados para revisão. Só devem embasar decisões depois de conferidos por um revisor humano no documento original (campo **Verificado**, sempre em branco neste relatório).

---

## 1. Identificação e escopo

| ID | Arquivo | Título | Versão | Data | Emissor / partes | Tamanho | Esquema de localização | Integridade |
|---|---|---|---|---|---|---|---|---|
| **DOC-A** | DOC-A_contrato_v1.pdf | CONTRATO DE PRESTAÇÃO DE SERVIÇOS DE SUPORTE TÉCNICO E MANUTENÇÃO DE SOFTWARE — Contrato nº 041/2026 | 1.0 | 10 de março de 2026 | CONTRATANTE: Beta Logística S.A. · CONTRATADA: Alfa Sistemas Ltda. | 7 páginas físicas | Numeração própria (cláusula/item) + **página física** (`p. N`, 1ª página do PDF = 1). A numeração impressa no rodapé é diferente: a capa (p. 1) não é numerada e a p. 2 traz `Página 1 de 6` (impressa = física − 1). **Localizador adotado: página física.** Tabela do Anexo II: `p. 7, Tabela 1, linha L, col. C`. | Texto extraível nas 7 páginas; **nenhuma página com OCR**; nenhuma página faltante. Quebras de linha do PDF foram normalizadas para espaço simples nas citações. |
| **DOC-B** | DOC-B_contrato_v2.docx | CONTRATO DE PRESTAÇÃO DE SERVIÇOS DE SUPORTE TÉCNICO E MANUTENÇÃO DE SOFTWARE — Contrato nº 041/2026 | 2.0 | 2 de setembro de 2026 | CONTRATANTE: Beta Logística S.A. · CONTRATADA: Alfa Sistemas Ltda. | 45 parágrafos + 1 tabela (sem paginação fixa) | Numeração própria + **número do parágrafo** (`par. N`). Regra de contagem: parágrafos do corpo numerados em sequência a partir de 1, incluindo título e títulos de cláusula; não há parágrafos em branco; a tabela fica fora da contagem e recebe localizador próprio (`Tabela 1, linha L, col. C`, após o par. 45). | **Sem alterações controladas** (nenhum `w:ins`/`w:del`), **sem comentários**; cabeçalho e rodapé vazios. Nenhum conteúdo inextraível. |

Estrutura comum aos dois documentos: capa/identificação → Cláusulas 1 a 12 → local, data e assinaturas → Anexo I (Descrição dos Serviços) → Anexo II (Matriz de Severidade).
Diferença estrutural: DOC-A tem a Cláusula 10 – Do Seguro e a Cláusula 11 – Da Proteção de Dados Pessoais; DOC-B tem a Cláusula 10 – Da Proteção de Dados Pessoais e a Cláusula 11 – Da Confidencialidade (o sigilo, que em DOC-A era o item 5.3, foi realocado). A partir da Cláusula 10, **o mesmo número de cláusula trata de temas diferentes** nas duas versões.

---

## 2. Relação entre os documentos e premissas

**Relação identificada: Versões (v1.0 → v2.0 do mesmo instrumento).**
Base: mesmo título, mesmo número (`Contrato nº 041/2026`), mesmas partes; DOC-A traz `Versão 1.0` (p. 1) e data de 10/03/2026; DOC-B traz `Versão 2.0` (par. 3) e data de 02/09/2026.

**Como isso afeta a classificação:** nenhuma versão é tratada como correta. Cada diferença recebe o rótulo de mudança `INCLUÍDO`, `REMOVIDO` ou `ALTERADO`, e o achado descreve o impacto da mudança de DOC-A para DOC-B.

| Premissa | Impacto se estiver errada |
|---|---|
| P1 — DOC-B é a versão posterior de DOC-A e pretende substituí-la integralmente. | Se DOC-B fosse um aditivo ou uma minuta não assinada, os achados continuariam válidos como diferenças de texto, mas o ACH-001 (marco de vigência) perderia efeito, e a remoção do ACH-007 passaria a ser uma proposta de remoção. |
| P2 — A data do local de assinatura de cada versão é a data em que aquela versão foi (ou será) assinada. | As linhas de assinatura estão em branco nos dois documentos; se DOC-B nunca for assinado, o ACH-001 deixa de existir como mudança efetiva de vigência. |
| P3 — Nenhum dos documentos declara regra de precedência entre cláusulas e anexos (busca por `prevalec`, `precedência`, `conflit`, `substitu`, `revoga`: zero ocorrências nos dois). | Se houvesse regra de precedência fora dos documentos (ex.: em um contrato-quadro), o ACH-004 poderia ser resolvido por ela. |

---

## 3. Resumo quantitativo

**Achados: 10**

| Tipo | Qtde | | Severidade | Qtde |
|---|---|---|---|---|
| CTR (contradição) | 4 | | Crítica | 1 |
| NCL (não claro) | 1 | | Alta | 7 |
| EXC (não presente) | 1 | | Média | 2 |
| INT (contradição interna) | 1 | | Baixa | 0 |
| REF (referência quebrada) | 1 | | Informativa | 0 |
| TER (terminologia) | 1 | | | |
| DIV (divergência) | 1 | | | |
| REV (requer revisão) | 0 | | | |

Rótulos de versão: 7 `ALTERADO`, 1 `REMOVIDO`, 1 `INCLUÍDO`; 1 defeito interno novo em DOC-B (INT).
**Carga de revisão humana:** 1 item em NÃO CLARO (ACH-006) e 0 em REQUER REVISÃO. 1 achado com confiança Média (ACH-001); demais com confiança Alta.
**Itens convergentes:** 26 (25 EQV-L, dos quais 2 realocados — sigilo e proteção de dados —, e 1 EQV-S).

**Leitura geral (efeito combinado — não altera a severidade individual):** a v2.0 mantém objeto, preço, reajuste, foro e escopo de serviços, mas desloca o equilíbrio em favor da CONTRATADA em quatro frentes ao mesmo tempo: prazos mais longos (correção crítica de 30 para 45 dias; severidade baixa de 5 para 10 dias úteis no anexo), sanção objetiva substituída por redação vaga, relatório de desempenho que deixa de ser obrigatório e seguro de responsabilidade civil removido. Somadas, essas mudanças reduzem tanto a exigência quanto a capacidade de medir e cobrar o desempenho. A v2.0 também introduz três defeitos de redação que não existiam na v1.0 (anexo inexistente, cláusula × anexo contraditórios e termo não definido) e uma restrição interna nova à rescisão pela CONTRATANTE.

---

## 4. Achados detalhados

### ACH-001 — Marco inicial da vigência muda com a nova data de assinatura

- **Tipo:** CTR / ALTERADO
- **Severidade:** Crítica
- **Confiança:** Média
- **Tópico:** Vigência
- **Padrão entre documentos:** A ≠ B

**Evidências**
- DOC-A, cl. 3.1 (p. 2): "3.1 O presente contrato vigorará pelo prazo de 12 (doze) meses, contados da data de sua assinatura, podendo ser prorrogado mediante termo aditivo."
- DOC-A, local e data (p. 6): "São Paulo, 10 de março de 2026."
- DOC-B, cl. 3.1 (par. 13): "3.1 O presente contrato vigorará pelo prazo de 12 (doze) meses, contados da data de sua assinatura, podendo ser prorrogado mediante termo aditivo."
- DOC-B, local e data (par. 40): "São Paulo, 2 de setembro de 2026."
- **Citação verificada:** Sim (DOC-A e DOC-B)

**Ponto exato da diferença**
| Elemento | DOC-A | DOC-B |
|---|---|---|
| Regra de vigência (cl. 3.1) | 12 meses da assinatura | igual |
| Marco inicial (data de assinatura) | 10/03/2026 | 02/09/2026 |
| Termo final resultante *(cálculo, não texto)* | 10/03/2027 | 02/09/2027 |
| Deslocamento do marco | — | +176 dias |

**Análise**
A data, isoladamente, é dado de identificação; vira achado porque a cl. 3.1 a usa como marco de vigência. O texto da regra é idêntico, mas o marco ao qual ela se aplica muda, e o mesmo contrato nº 041/2026 não pode ter dois inícios de vigência. Nenhuma das versões diz se a v2.0 substitui a v1.0 (zero ocorrências de `substitu`, `revoga`), e a própria cl. 3.1 prevê prorrogação mediante termo aditivo, enquanto DOC-B não se identifica como aditivo. Confiança **Média** porque o efeito depende das premissas P1 e P2 (as linhas de assinatura estão em branco nos dois documentos).
Severidade pela âncora **Crítica** (muda um elemento essencial: vigência).

**Impacto / risco**
Incerteza sobre o termo final do contrato e, por consequência, sobre o período de obrigações atreladas à vigência (ex.: equipe certificada durante toda a vigência, cl. 5.1; sigilo por 5 anos após o término). Uma assinatura da v2.0 sem cláusula de transição pode ser lida como reinício do prazo de 12 meses, estendendo-o em cerca de seis meses sem termo aditivo.

**Recomendação**
Decidir se a v2.0 substitui a v1.0 ou se é uma alteração do contrato em curso. No primeiro caso, incluir cláusula de transição/substituição com data de início expressa; no segundo, formalizar como termo aditivo mantendo o marco de 10/03/2026. Validar com o jurídico.

**Verificado (revisor):** ☐

---

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
| Elemento | DOC-A | DOC-B |
|---|---|---|
| Prazo | 30 dias | 45 dias |
| Tipo de contagem | corridos | igual |
| Marco inicial | abertura do chamado | igual |
| Modalidade | deverá | igual |

**Análise**
Mesmo item, mesmo responsável, mesma contagem e mesmo marco; só o valor do prazo muda. Os dois prazos não podem valer juntos para a mesma obrigação → CTR. A mudança amplia em 50% o tempo para corrigir falhas que, pelo Anexo II, correspondem a sistema indisponível. Severidade pela âncora **Alta** (prazo de correção de 30 para 45 dias).

**Impacto / risco**
O sistema de gestão de frota pode ficar indisponível por até 45 dias sem descumprimento contratual. O efeito se soma ao ACH-006 (sanção por atraso deixou de ser objetiva).

**Recomendação**
Confirmar se a ampliação foi negociada e aceita pela CONTRATANTE; se não, restabelecer 30 dias ou justificar o novo prazo.

**Verificado (revisor):** ☐

---

### ACH-003 — Anexo II: prazo de severidade baixa passa de 5 para 10 dias úteis

- **Tipo:** CTR / ALTERADO
- **Severidade:** Alta
- **Confiança:** Alta
- **Tópico:** Prazos de atendimento (Matriz de Severidade)
- **Padrão entre documentos:** A ≠ B

**Evidências**
- DOC-A, Anexo II (p. 7, Tabela 1, linha 4): "Baixa" | "Dúvida ou falha sem impacto operacional" | "Até 5 dias úteis"
- DOC-B, Anexo II (Tabela 1, linha 4): "Baixa" | "Dúvida ou falha sem impacto operacional" | "Até 10 dias úteis"
- **Citação verificada:** Sim (DOC-A e DOC-B)

**Ponto exato da diferença**
| Elemento | DOC-A | DOC-B |
|---|---|---|
| Severidade / descrição | Baixa — falha sem impacto operacional | igual |
| Prazo de atendimento | 5 | 10 |
| Unidade | dias úteis | igual |

**Análise**
Mesmo item da matriz, valor diferente → CTR. Em DOC-A o anexo é coerente com a cl. 4.3; em DOC-B não é (ver ACH-004). Severidade pela âncora **Alta** (alteração material de prazo).

**Impacto / risco**
Dobra o prazo de atendimento de chamados de severidade baixa, se o anexo prevalecer.

**Recomendação**
Definir o prazo desejado e alinhar anexo e cláusula 4.3 na mesma redação.

**Verificado (revisor):** ☐

---

### ACH-004 — DOC-B: cláusula 4.3 e Anexo II fixam prazos diferentes para severidade baixa

- **Tipo:** INT (defeito novo em DOC-B; inexistente em DOC-A)
- **Severidade:** Alta
- **Confiança:** Alta
- **Tópico:** Prazos de atendimento
- **Padrão entre documentos:** DOC-A coerente; DOC-B contraditório internamente

**Evidências**
- DOC-B, cl. 4.3 (par. 17): "4.3 Os chamados de severidade baixa serão atendidos em até 5 (cinco) dias úteis, conforme a Matriz de Severidade do Anexo II."
- DOC-B, Anexo II (Tabela 1, linha 4, col. 3): "Até 10 dias úteis"
- Contraste — DOC-A, cl. 4.3 (p. 3): "4.3 Os chamados de severidade baixa serão atendidos em até 5 (cinco) dias úteis, conforme a Matriz de Severidade do Anexo II."
- Contraste — DOC-A, Anexo II (p. 7, Tabela 1, linha 4, col. 3): "Até 5 dias úteis"
- **Citação verificada:** Sim (DOC-A e DOC-B)

**Ponto exato da diferença**
| Elemento | DOC-B cl. 4.3 | DOC-B Anexo II |
|---|---|---|
| Prazo para severidade baixa | 5 dias úteis | 10 dias úteis |
| Remissão | remete à Matriz do Anexo II | — |

**Análise**
A cláusula afirma um prazo "conforme" uma matriz que diz outro. As duas regras não podem ser cumpridas como escritas ao mesmo tempo, e DOC-B não tem regra de precedência entre cláusula e anexo (premissa P3). A situação é agravada pelo ACH-008: a cl. 12.1 de DOC-B não lista o Anexo II entre os anexos integrantes, o que torna incerto se a matriz sequer faz parte do contrato. Par diferente do ACH-003 (aqui: cl. 4.3 × Anexo II dentro de DOC-B), por isso achado separado. A cl. 4.3 é idêntica nas duas versões e consta dos convergentes com remissão a este achado. Severidade pela âncora **Alta** (cláusula × anexo com prazos diferentes).

**Impacto / risco**
Disputa sobre qual prazo vale; o atraso entre o 6º e o 10º dia útil pode ser cobrado por um lado e negado pelo outro.

**Recomendação**
Corrigir uma das duas redações e, idealmente, incluir regra de precedência entre corpo do contrato e anexos.

**Verificado (revisor):** ☐

---

### ACH-005 — Relatório mensal de desempenho deixa de ser obrigatório

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
| Elemento | DOC-A | DOC-B |
|---|---|---|
| Modalidade | deverá (obrigação) | poderá (faculdade) |
| Objeto, periodicidade e prazo | relatório mensal até o 5º dia útil | igual |

**Análise**
Única palavra alterada, mas é a modalidade normativa: pela regra de desempate, mudança de obrigação para faculdade é CTR, ainda que emitir o relatório cumpra as duas versões. Severidade pela âncora **Alta** (relatório obrigatório que vira facultativo = enfraquece mecanismo de fiscalização).

**Impacto / risco**
A CONTRATANTE perde o instrumento contratual de acompanhamento dos prazos da Cláusula 4; sem relatório, a apuração de descumprimentos depende de controles próprios.

**Recomendação**
Restabelecer a obrigação ou, se mantida a faculdade, prever outro mecanismo obrigatório de medição de SLA.

**Verificado (revisor):** ☐

---

### ACH-006 — Multa de 2% por descumprimento de prazo substituída por "medidas cabíveis"

- **Tipo:** NCL / ALTERADO
- **Severidade:** Alta
- **Confiança:** Alta
- **Tópico:** Penalidades
- **Padrão entre documentos:** A ≠ B

**Evidências**
- DOC-A, cl. 8.1 (p. 4): "8.1 O descumprimento dos prazos previstos na Cláusula 4 sujeitará a CONTRATADA a multa de 2% (dois por cento) sobre o valor mensal, por ocorrência."
- DOC-B, cl. 8.1 (par. 29): **NÃO CLARO.** "8.1 O descumprimento dos prazos previstos na Cláusula 4 poderá ensejar a aplicação das medidas cabíveis." Trata das consequências do descumprimento dos prazos, mas não define quais medidas, valor, base de cálculo nem frequência. Busca no restante de DOC-B por `multa`, `medidas`, `sanção`, `advertência`, `penalidade`: a única outra ocorrência é o título da Cláusula 8 (par. 28); nenhuma definição das medidas.
- **Citação verificada:** Sim (DOC-A e DOC-B)

**Ponto exato da diferença**
| Elemento | DOC-A | DOC-B |
|---|---|---|
| Gatilho | descumprimento dos prazos da Cláusula 4 | igual |
| Consequência | multa de 2% | medidas cabíveis (não definidas) |
| Base de cálculo | valor mensal | não definida |
| Frequência | por ocorrência | não definida |
| Modalidade | sujeitará (consequência certa) | poderá ensejar (consequência eventual) |

**Análise**
O tema continua presente, mas o conteúdo objetivo foi trocado por redação vaga; pela regra de desempate, é NCL (e não CTR, embora a modalidade também tenha mudado). Severidade pela âncora **Alta** (multa trocada por medidas cabíveis = sanção enfraquecida).

**Impacto / risco**
Os prazos da Cláusula 4 deixam de ter consequência quantificável; a aplicação de qualquer sanção passa a depender de interpretação e pode ser contestada.

**Recomendação**
Esclarecer com o responsável pela v2.0 quais são as medidas pretendidas e reescrever com consequência objetiva (percentual, base, limite), ou restabelecer a multa.

**Verificado (revisor):** ☐

---

### ACH-007 — Cláusula de seguro de responsabilidade civil profissional removida

- **Tipo:** EXC / REMOVIDO
- **Severidade:** Alta
- **Confiança:** Alta
- **Tópico:** Seguro / garantias
- **Padrão entre documentos:** A ≠ B (presente só em DOC-A)

**Evidências**
- DOC-A, cl. 10.1 (p. 5): "10.1 A CONTRATADA manterá, durante toda a vigência deste contrato, apólice de seguro de responsabilidade civil profissional com cobertura mínima de R$ 500.000,00 (quinhentos mil reais)."
- DOC-B: **NÃO PRESENTE.** Seções verificadas: documento inteiro (par. 1–45 e Tabela 1), com atenção a Cláusula 5 – Obrigações da CONTRATADA (par. 18–20), Cláusula 8 – Penalidades (par. 28–29), Cláusula 10 – Proteção de Dados Pessoais (par. 33–34, número que em DOC-A era do Seguro), Cláusula 11 – Confidencialidade (par. 35–36), Cláusula 12 – Disposições Gerais (par. 37–39) e Anexos I e II (par. 43–45, Tabela 1). Termos buscados: `seguro`, `apólice`, `responsabilidade civil`, `cobertura`, `500.000`, `indeniz`, `garantia`. Conteúdo relacionado: nenhum.
- **Citação verificada:** Sim (DOC-A)

**Ponto exato da diferença**
| Elemento | DOC-A | DOC-B |
|---|---|---|
| Obrigação de manter seguro | sim, durante toda a vigência | ausente |
| Tipo de apólice | responsabilidade civil profissional | — |
| Cobertura mínima | R$ 500.000,00 | — |

**Análise**
O tema inteiro desaparece; a renumeração faz a Cláusula 10 de DOC-B tratar de proteção de dados, o que pode mascarar a remoção numa leitura por número. Severidade pela âncora **Alta** (remove garantia/seguro).

**Impacto / risco**
A CONTRATANTE fica sem garantia contratual de cobertura para danos causados pela CONTRATADA na execução dos serviços.

**Recomendação**
Confirmar se a remoção foi intencional e aprovada; se não, restabelecer a cláusula.

**Verificado (revisor):** ☐

---

### ACH-008 — Cláusula 12.1 passa a citar um "Anexo IV" que não existe

- **Tipo:** REF / ALTERADO
- **Severidade:** Alta
- **Confiança:** Alta
- **Tópico:** Disposições gerais / anexos integrantes
- **Padrão entre documentos:** A ≠ B

**Evidências**
- DOC-A, cl. 12.1 (p. 6): "12.1 Integram este contrato o Anexo I (Descrição dos Serviços) e o Anexo II (Matriz de Severidade)."
- DOC-B, cl. 12.1 (par. 38): "12.1 Integram este contrato o Anexo I (Descrição dos Serviços) e o Anexo IV (Matriz de Severidade)."
- DOC-B, título do anexo existente (par. 45): "Anexo II – Matriz de Severidade"
- Busca em DOC-B: `Anexo IV` ocorre apenas no par. 38; `Anexo III`: nenhuma ocorrência. Não há anexo numerado IV.
- **Citação verificada:** Sim (DOC-A e DOC-B)

**Ponto exato da diferença**
| Elemento | DOC-A | DOC-B |
|---|---|---|
| Anexo da Matriz de Severidade citado | Anexo II | Anexo IV |
| Anexo citado existe no documento? | sim (p. 7) | não (o existente é o Anexo II, par. 45) |
| Anexo I (Descrição dos Serviços) | citado | igual |

**Análise**
Mudança e defeito estão no mesmo item → um único achado REF / ALTERADO. Provável erro de numeração, mas o efeito é que a Matriz de Severidade de DOC-B não está formalmente listada como integrante do contrato, enquanto a cl. 4.3 remete a ela (ver ACH-004). Severidade pela âncora **Alta** (cláusula de integração que deixa de listar o anexo com os SLAs).

**Impacto / risco**
Incerteza sobre a força contratual da matriz (prazos de severidade média e baixa); a severidade média só está definida no anexo.

**Recomendação**
Corrigir a referência para Anexo II (ou criar o Anexo IV, se for essa a intenção) e conferir as demais remissões.

**Verificado (revisor):** ☐

---

### ACH-009 — Cláusula 6 passa a usar o termo não definido "CLIENTE"

- **Tipo:** TER / ALTERADO
- **Severidade:** Média
- **Confiança:** Alta
- **Tópico:** Obrigações da CONTRATANTE / terminologia
- **Padrão entre documentos:** A ≠ B

**Evidências**
- DOC-A, título da Cláusula 6 (p. 4): "Cláusula 6 – Das Obrigações da CONTRATANTE"
- DOC-A, cl. 6.1 (p. 4): "6.1 A CONTRATANTE deverá fornecer à CONTRATADA acesso remoto ao ambiente do sistema, nos termos da política de segurança da informação da CONTRATANTE."
- DOC-A, cl. 6.2 (p. 4): "6.2 A CONTRATANTE deverá designar um gestor do contrato, responsável por acompanhar a execução dos serviços."
- DOC-B, título da Cláusula 6 (par. 21): "Cláusula 6 – Das Obrigações do CLIENTE"
- DOC-B, cl. 6.1 (par. 22): "6.1 O CLIENTE deverá fornecer à CONTRATADA acesso remoto ao ambiente do sistema, nos termos da política de segurança da informação do CLIENTE."
- DOC-B, cl. 6.2 (par. 23): "6.2 O CLIENTE deverá designar um gestor do contrato, responsável por acompanhar a execução dos serviços."
- DOC-B, definição das partes, cl. 1.1 (par. 9): "1.1 BETA LOGÍSTICA S.A., doravante denominada CONTRATANTE, e ALFA SISTEMAS LTDA., doravante denominada CONTRATADA, celebram o presente contrato, que se regerá pelas cláusulas a seguir."
- Busca em DOC-B: `CLIENTE` ocorre apenas nos par. 21–23; nenhuma definição. As demais cláusulas de DOC-B continuam usando `CONTRATANTE` (par. 25, 32, 36).
- **Citação verificada:** Sim (DOC-A e DOC-B)

**Ponto exato da diferença**
| Elemento | DOC-A | DOC-B |
|---|---|---|
| Parte obrigada na Cláusula 6 | CONTRATANTE (definida na cl. 1.1) | CLIENTE (não definido) |
| Titular da política de segurança | CONTRATANTE | CLIENTE |
| Obrigações (acesso remoto; designar gestor) | — | igual |

**Análise**
Mudança e defeito no mesmo item (Cláusula 6) → um único achado TER / ALTERADO. Pelo contexto, CLIENTE quase certamente designa a Beta Logística S.A., mas o termo não está definido e convive, no mesmo documento, com CONTRATANTE. Severidade pela âncora **Média** (termo não definido usado no lugar do definido, sentido inferível pelo contexto).

**Impacto / risco**
Margem para alegar que as obrigações de fornecer acesso e designar gestor não recaem formalmente sobre a parte definida.

**Recomendação**
Substituir CLIENTE por CONTRATANTE na Cláusula 6 (título, 6.1 e 6.2).

**Verificado (revisor):** ☐

---

### ACH-010 — Rescisão pela CONTRATANTE passa a depender de aprovação da Diretoria Jurídica

- **Tipo:** DIV / INCLUÍDO
- **Severidade:** Média
- **Confiança:** Alta
- **Tópico:** Rescisão
- **Padrão entre documentos:** A ≠ B

**Evidências**
- DOC-A, cl. 9.1 (p. 5): "9.1 Qualquer das partes poderá rescindir este contrato mediante notificação por escrito, com antecedência mínima de 30 (trinta) dias."
- DOC-A: não há item 9.2; a Cláusula 9 termina no item 9.1 (p. 5). Busca por `aprovação`, `Diretoria`, `jurídic`: nenhuma ocorrência em DOC-A.
- DOC-B, cl. 9.1 (par. 31): "9.1 Qualquer das partes poderá rescindir este contrato mediante notificação por escrito, com antecedência mínima de 30 (trinta) dias."
- DOC-B, cl. 9.2 (par. 32): "9.2 A rescisão por iniciativa da CONTRATANTE dependerá de prévia aprovação de sua Diretoria Jurídica."
- **Citação verificada:** Sim (DOC-A e DOC-B)

**Ponto exato da diferença**
| Elemento | DOC-A | DOC-B |
|---|---|---|
| Direito de rescisão por qualquer parte | sim | igual |
| Forma e aviso prévio | notificação escrita, 30 dias | igual |
| Condição adicional para a CONTRATANTE | nenhuma | prévia aprovação da Diretoria Jurídica |
| Condição adicional para a CONTRATADA | nenhuma | igual |

**Análise**
A regra de rescisão existe nas duas versões; DOC-B acrescenta uma condição a ela → DIV / INCLUÍDO (não EXC). A condição é assimétrica (só para a CONTRATANTE) e depende de ato interno de uma das partes, sem prazo, forma de comprovação ou efeito previsto caso a notificação seja enviada sem a aprovação. Se essa condição é oponível à CONTRATADA é questão jurídica que os documentos não resolvem — requer avaliação de especialista. Severidade pela âncora **Média** (condição procedimental acrescentada a regra que continua existindo).

**Impacto / risco**
A CONTRATADA pode contestar uma rescisão alegando ausência de aprovação prévia, atrasando a saída da CONTRATANTE.

**Recomendação**
Confirmar a intenção; se for controle interno da CONTRATANTE, retirá-lo do contrato ou deixar expresso que não afeta a validade da notificação perante a CONTRATADA.

**Verificado (revisor):** ☐

---

## 5. Itens convergentes

**Identificação**
- **Título** (EQV-L) — DOC-A p. 1: "CONTRATO DE PRESTAÇÃO DE SERVIÇOS DE SUPORTE TÉCNICO E MANUTENÇÃO DE SOFTWARE" · DOC-B par. 1: "CONTRATO DE PRESTAÇÃO DE SERVIÇOS DE SUPORTE TÉCNICO E MANUTENÇÃO DE SOFTWARE"
- **Número do contrato** (EQV-L) — DOC-A p. 1: "Contrato nº 041/2026" · DOC-B par. 2: "Contrato nº 041/2026"
- **Partes na capa** (EQV-L) — DOC-A p. 1: "CONTRATANTE: Beta Logística S.A." / "CONTRATADA: Alfa Sistemas Ltda." · DOC-B par. 5–6: "CONTRATANTE: Beta Logística S.A." / "CONTRATADA: Alfa Sistemas Ltda."
- **Nota de documento fictício** (EQV-L) — DOC-A p. 1 · DOC-B par. 7: "Documento fictício, elaborado exclusivamente para testes."

**Partes, objeto e vigência**
- **Qualificação das partes** (EQV-L) — DOC-A cl. 1.1 (p. 2) · DOC-B cl. 1.1 (par. 9): "doravante denominada CONTRATANTE"
- **Objeto** (EQV-L) — DOC-A cl. 2.1 (p. 2) · DOC-B cl. 2.1 (par. 11): "manutenção corretiva e evolutiva do sistema de gestão de frota"
- **Regra de vigência** (EQV-L, ver ACH-001) — DOC-A cl. 3.1 (p. 2) · DOC-B cl. 3.1 (par. 13): "vigorará pelo prazo de 12 (doze) meses"

**Prazos de atendimento**
- **Início do atendimento crítico** (EQV-L) — DOC-A cl. 4.1 (p. 3) · DOC-B cl. 4.1 (par. 15): "em até 4 (quatro) horas corridas, contadas da abertura do chamado"
- **Prazo de severidade baixa na cláusula** (EQV-L, ver ACH-004) — DOC-A cl. 4.3 (p. 3) · DOC-B cl. 4.3 (par. 17): "serão atendidos em até 5 (cinco) dias úteis"

**Obrigações da CONTRATADA**
- **Equipe certificada** (EQV-L) — DOC-A cl. 5.1 (p. 3) · DOC-B cl. 5.1 (par. 19): "manter equipe técnica com certificação no sistema objeto deste contrato"
- **Sigilo** (EQV-L, **realocado**: DOC-A item 5.3 → DOC-B cl. 11.1, em cláusula própria "Da Confidencialidade") — DOC-A cl. 5.3 (p. 3) · DOC-B cl. 11.1 (par. 36): "durante a vigência e por 5 (cinco) anos após o seu término"

**Preço e pagamento**
- **Valor mensal** (EQV-L) — DOC-A cl. 7.1 (p. 4) · DOC-B cl. 7.1 (par. 25): "R$ 18.500,00 (dezoito mil e quinhentos reais)"
- **Prazo de pagamento** (EQV-S) — DOC-A cl. 7.2 (p. 4): "em até 30 (trinta) dias após o recebimento da nota fiscal" · DOC-B cl. 7.2 (par. 26): "no prazo máximo de trinta dias, contado do recebimento da nota fiscal" — mesmo prazo, mesmo marco, mesma natureza de prazo máximo.
- **Reajuste** (EQV-L) — DOC-A cl. 7.3 (p. 4) · DOC-B cl. 7.3 (par. 27): "reajustado anualmente pela variação do IPCA"

**Rescisão**
- **Rescisão por qualquer das partes** (EQV-L, ver ACH-010) — DOC-A cl. 9.1 (p. 5) · DOC-B cl. 9.1 (par. 31): "com antecedência mínima de 30 (trinta) dias"

**Proteção de dados**
- **Tratamento de dados pessoais** (EQV-L, **realocado**: DOC-A cl. 11.1 → DOC-B cl. 10.1) — DOC-A cl. 11.1 (p. 5) · DOC-B cl. 10.1 (par. 34): "exclusivamente para a execução do objeto deste contrato, observada a Lei nº 13.709/2018"

**Disposições gerais e assinaturas**
- **Foro** (EQV-L) — DOC-A cl. 12.2 (p. 6) · DOC-B cl. 12.2 (par. 39): "Fica eleito o foro da Comarca de São Paulo/SP"
- **Bloco de assinatura da CONTRATANTE** (EQV-L) — DOC-A p. 6 · DOC-B par. 41: "BETA LOGÍSTICA S.A. (CONTRATANTE)"
- **Bloco de assinatura da CONTRATADA** (EQV-L) — DOC-A p. 6 · DOC-B par. 42: "ALFA SISTEMAS LTDA. (CONTRATADA)"

**Anexo I – Descrição dos Serviços**
- **Horário do suporte remoto** (EQV-L) — DOC-A p. 7 · DOC-B par. 44: "Suporte técnico remoto em dias úteis, das 8h às 18h"
- **Manutenção corretiva** (EQV-L) — DOC-A p. 7 · DOC-B par. 44: "manutenção corretiva de falhas"
- **Limite de manutenção evolutiva** (EQV-L) — DOC-A p. 7 · DOC-B par. 44: "limitada a 40 (quarenta) horas mensais"

**Anexo II – Matriz de Severidade** (linhas sem achado)
- **Título do anexo** (EQV-L) — DOC-A p. 7 · DOC-B par. 45: "Anexo II – Matriz de Severidade"
- **Cabeçalho da tabela** (EQV-L) — DOC-A p. 7, Tabela 1, linha 1 · DOC-B Tabela 1, linha 1: "Prazo de atendimento"
- **Linha Crítica** (EQV-L) — DOC-A p. 7, Tabela 1, linha 2 · DOC-B Tabela 1, linha 2: "Sistema indisponível" | "Início em até 4 horas corridas"
- **Linha Média** (EQV-L) — DOC-A p. 7, Tabela 1, linha 3 · DOC-B Tabela 1, linha 3: "Funcionalidade degradada" | "Até 2 dias úteis"

*Itens com achado (cl. 4.2, 5.2, 6, 8.1, 9.2, 10.1 de DOC-A, 12.1, local e data, linha Baixa do Anexo II) não constam desta lista.*

---

## 6. Declaração de cobertura e limitações

**Cobertura**
- DOC-A: páginas físicas 1 a 7 analisadas integralmente (capa, Cláusulas 1–12, local/data/assinaturas, Anexo I, Anexo II com Tabela 1). Nenhuma página com OCR; nenhuma ilegível. Rodapés impressos (`Contrato nº 041/2026 – Versão 1.0 · Página N de 6`) tratados como elemento de identificação, sem conteúdo normativo.
- DOC-B: parágrafos 1 a 45 e Tabela 1 analisados integralmente. Sem alterações controladas, comentários, cabeçalho ou rodapé.
- Reconciliação: todo item de DOC-A e de DOC-B foi classificado em um achado ou nos itens convergentes. Elementos apenas de identificação (número de versão, data na capa, rodapé de DOC-A) estão no inventário (seção 1); a data de assinatura entrou no ACH-001 por ser marco da cl. 3.1.
- Verificações transversais executadas: contradição interna (1 em DOC-B — ACH-004; nenhuma em DOC-A), terminologia (ACH-009), referências cruzadas (todas as remissões conferidas: Anexo I, Anexo II, Cláusula 4; 1 quebrada — ACH-008), dependências ocultas (registradas em ACH-004/ACH-008), ambiguidades (seção abaixo), metadados (abaixo).

**Verificação das citações**
- Execução mecânica: cada trecho entre aspas atribuído a um documento foi comparado, por script, com o texto extraído no localizador indicado (página física em DOC-A; parágrafo ou célula em DOC-B), após normalizar apenas as quebras de linha do PDF.
- Evidências (campo **Evidências** dos 10 achados, 100%, incluindo todos os CTR e o EXC): **34 trechos conferidos, 34 confirmados, 0 corrigidos, 0 divergentes, 0 indisponíveis.**
- Trechos entre aspas fora das Evidências (Ponto exato, Análise, Recomendação, Itens convergentes, Observações, Questões): **47 trechos conferidos (100%), 47 confirmados na versão final; 3 corrigidos; 0 divergentes; 0 indisponíveis** (as 3 correções: expressões da seção 2 que estavam entre aspas sem serem citações foram convertidas em texto corrido) (expressões não literais foram escritas sem aspas ou em formato de código).
- Nenhum achado precisou ser rebaixado para REV.

**Limitações**
- Os documentos não contêm assinaturas efetivas (linhas em branco); o ACH-001 depende das premissas P1 e P2.
- Questões de validade/oponibilidade jurídica (ACH-001, ACH-010) não são concluídas aqui; recomendam-se avaliação jurídica.
- Os termos finais de vigência no ACH-001 são cálculo do analista, não texto dos documentos.

**Observações não comparativas** (iguais nos dois documentos; sem ID e fora da contagem de achados)
1. **Severidade média sem regra no corpo do contrato.** A Cláusula 4 trata apenas de severidade crítica (4.1, 4.2) e baixa (4.3); a severidade média só aparece no Anexo II (DOC-A p. 7, Tabela 1, linha 3; DOC-B Tabela 1, linha 3: "Até 2 dias úteis"). Em DOC-B, isso pesa mais por causa do ACH-008.
2. **Sem prazo de conclusão para severidades média e baixa.** Só a severidade crítica tem prazo de correção (cl. 4.2); para as demais, o texto fala em atendimento sem dizer se é início ou conclusão (cl. 4.3: "serão atendidos em até 5 (cinco) dias úteis"; Anexo II, coluna "Prazo de atendimento"), enquanto a linha Crítica especifica "Início em até 4 horas corridas".
3. **Prazo de pagamento sem tipo de contagem.** A cl. 7.2 não diz se os trinta dias são corridos ou úteis (DOC-A p. 4; DOC-B par. 26).
4. **Reajuste sem data-base.** A cl. 7.3 ("reajustado anualmente pela variação do IPCA") não define a partir de quando se conta o ano nem o período de apuração — ponto sensível diante do ACH-001.
5. **Certificação não especificada.** A cl. 5.1 exige equipe "com certificação no sistema objeto deste contrato" sem indicar qual certificação nem quantos profissionais.
6. **Ausência de cláusula de substituição de versões.** Nenhum dos documentos diz que substitui instrumentos anteriores (busca por `substitu`, `revoga`: zero ocorrências) — origem da incerteza do ACH-001.
7. **Metadados de arquivo.** DOC-A (PDF) registra criação em 14/10/2026, autor `Kit de teste`. DOC-B (.docx) registra criação/modificação em 23/12/2013 e criador `python-docx` (valores padrão do gerador), incompatíveis com a data do próprio documento. Não afetam a identificação das versões, que é dada pelo texto (versão e data na capa).

---

## 7. Questões em aberto

- **Q1** — A v2.0 substitui a v1.0 ou altera o contrato em curso? A vigência conta a partir de 10/03/2026 ou de 02/09/2026? *Ref.: ACH-001*
- **Q2** — A ampliação do prazo de correção de falhas críticas para 45 dias corridos foi negociada e aceita pela CONTRATANTE? *Ref.: ACH-002*
- **Q3** — Qual é o prazo para severidade baixa: 5 ou 10 dias úteis? E qual prevalece em caso de conflito entre cláusula e anexo? *Ref.: ACH-003, ACH-004*
- **Q4** — A emissão do relatório mensal deve mesmo ser facultativa? Se sim, como a CONTRATANTE medirá o cumprimento da Cláusula 4? *Ref.: ACH-005*
- **Q5** — Quais são as "medidas cabíveis" da nova cl. 8.1? A multa de 2% foi removida intencionalmente? *Ref.: ACH-006*
- **Q6** — A remoção do seguro de responsabilidade civil profissional (cobertura mínima de R$ 500.000,00) foi aprovada? *Ref.: ACH-007*
- **Q7** — O "Anexo IV" da cl. 12.1 é erro de numeração (Anexo II) ou falta um anexo? *Ref.: ACH-008, ACH-004*
- **Q8** — CLIENTE, na Cláusula 6, deve ser lido como CONTRATANTE? *Ref.: ACH-009*
- **Q9** — A aprovação da Diretoria Jurídica é controle interno da CONTRATANTE ou condição de validade da rescisão perante a CONTRATADA? Há prazo e forma de comprovação? *Ref.: ACH-010*

---

*Relatório gerado em 15/10/2026. Exportação para planilha não solicitada; disponível sob demanda no formato da seção 8 da metodologia.*
