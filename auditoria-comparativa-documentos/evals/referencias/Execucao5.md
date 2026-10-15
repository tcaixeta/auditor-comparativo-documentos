# Análise comparativa — Contrato nº 041/2026 · DOC-A (v1.0) × DOC-B (v2.0)

> Todos os achados abaixo são **indícios até verificação humana**. Só devem embasar decisões depois que o revisor conferir cada evidência no documento original e marcar o campo **Verificado**.

## 1. Identificação e escopo

|                                    | DOC-A                                                        | DOC-B                                                        |
| ---------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Arquivo                            | DOC-A_contrato_v1.pdf                                        | DOC-B_contrato_v2.docx                                       |
| Título                             | CONTRATO DE PRESTAÇÃO DE SERVIÇOS DE SUPORTE TÉCNICO E MANUTENÇÃO DE SOFTWARE | idêntico                                                     |
| Nº / versão                        | Contrato nº 041/2026 · "Versão 1.0" (p. 1)                   | Contrato nº 041/2026 · "Versão 2.0" (par. 3)                 |
| Data de emissão                    | "Data: 10 de março de 2026" (p. 1)                           | "Data: 2 de setembro de 2026" (par. 4)                       |
| Local e data (bloco de assinatura) | "São Paulo, 10 de março de 2026." (p. 6)                     | "São Paulo, 2 de setembro de 2026." (par. 40)                |
| Partes                             | Beta Logística S.A. (CONTRATANTE) · Alfa Sistemas Ltda. (CONTRATADA) | idênticas                                                    |
| Emissor                            | Não declarado no texto (metadado `Author` do PDF: `Kit de teste`) | Não declarado (metadado `creator`: `python-docx`)            |
| Extensão                           | 7 páginas físicas; 12 cláusulas + Anexos I e II              | 45 parágrafos de corpo + 1 tabela; 12 cláusulas + Anexos I e II |
| Esquema de localização             | Cláusula + **página física** (p. 1 = capa). A numeração impressa no rodapé começa na p. física 2 ("Página 1 de 6"), ou seja, impressa = física − 1; a capa não tem número. **Localizador adotado: página física.** | Cláusula + **par. N**: todos os parágrafos do corpo numerados em sequência a partir de 1, incluindo títulos (o documento não tem parágrafos vazios). Tabela: `Tabela 1, linha L, col. C` (linha 1 = cabeçalho). |
| Integridade                        | Texto extraível em todas as páginas; **nenhuma página com OCR**. Tabela da p. 7 extraída separadamente (Tabela 1) e conferida com o texto corrido. Quebras de linha dentro de um parágrafo foram unidas com um espaço. | Sem alterações controladas (nenhuma marca de inserção/exclusão no XML), sem comentários, cabeçalho e rodapé vazios. |

## 2. Relação entre os documentos e premissas

**Relação identificada: Versões (v1.0 → v2.0).** Base: mesmo número de contrato, mesmo título, mesmas partes, mesma estrutura de 12 cláusulas e 2 anexos, identificação explícita como versão 1.0 e 2.0, e datas em ordem cronológica (10/03/2026 → 02/09/2026).

**Como isso afeta a classificação:** nenhum documento é tratado como referência que prevalece; as diferenças são registradas como mudanças de DOC-A para DOC-B (`INCLUÍDO`, `REMOVIDO`, `ALTERADO`). Defeitos que só existem em DOC-B (INT, REF, TER interno) são registrados como achados próprios, sem rótulo de mudança.

**Premissas e impacto se estiverem erradas:**

| #    | Premissa                                                     | Se estiver errada                                            |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| P1   | DOC-B é a versão posterior, destinada a substituir DOC-A.    | Se DOC-B fosse um **aditivo** a DOC-A, os itens ausentes em DOC-B (ex.: seguro, ACH-007) poderiam continuar vigentes por DOC-A, e os EXC/REMOVIDO seriam apenas pontos sobre os quais o aditivo é omisso. Se fossem **minutas independentes**, os rótulos de versão perderiam sentido e os achados seriam divergências a decidir. Nenhum dos documentos declara regra de precedência nem diz que substitui o outro. |
| P2   | A data do bloco de local e data (`São Paulo, <data>`) de cada documento é a sua data de assinatura. | Afeta só o ACH-001 (marco da vigência). Por isso o ACH-001 tem confiança Média. |

**Decisões de método:** seguindo a regra de unidade do achado, a diferença entre versões e o defeito interno que ela cria em DOC-B são achados separados e ligados por referência cruzada (ACH-003 × ACH-004; ACH-008 × ACH-009; ACH-010 × ACH-011).

## 3. Resumo quantitativo

**12 achados · 20 itens convergentes**

| Tipo                      | Qtde | Achados                     |
| ------------------------- | ---- | --------------------------- |
| CTR — Contradição         | 5    | ACH-001, 002, 003, 005, 008 |
| NCL — Não claro           | 1    | ACH-006                     |
| EXC — Não presente        | 1    | ACH-007                     |
| INT — Contradição interna | 1    | ACH-004                     |
| REF — Referência quebrada | 1    | ACH-009                     |
| TER — Terminologia        | 2    | ACH-010, 011                |
| DIV — Divergência         | 1    | ACH-012                     |

| Severidade          | Qtde | Achados           |
| ------------------- | ---- | ----------------- |
| Crítica             | 1    | ACH-001           |
| Alta                | 8    | ACH-002 a ACH-009 |
| Média               | 3    | ACH-010 a ACH-012 |
| Baixa / Informativa | 0    | —                 |

Rótulos de versão: ALTERADO 7 (ACH-001, 002, 003, 005, 006, 008, 010) · REMOVIDO 1 (ACH-007) · INCLUÍDO 1 (ACH-012) · defeitos novos de DOC-B 3 (ACH-004, 009, 011).

**Carga de revisão humana:** 1 item NÃO CLARO (ACH-006) · 0 itens REQUER REVISÃO. Prioridade de conferência: **ACH-001** (Crítico com confiança Média).

**Leitura geral (análise):** a v2.0 mantém objeto, preço, pagamento, foro e anexo de serviços, mas o conjunto das mudanças reduz as obrigações da CONTRATADA e os mecanismos de controle da CONTRATANTE: o prazo de correção crítica fica mais longo (ACH-002), o prazo para severidade baixa dobra no Anexo II (ACH-003), o relatório mensal fica facultativo (ACH-005), a multa dá lugar a uma consequência indefinida (ACH-006) e o seguro sai do contrato (ACH-007). Em sentido oposto, a rescisão pela CONTRATANTE ganha uma condição interna (ACH-012). A v2.0 também introduz três defeitos de redação inexistentes na v1.0 (ACH-004, 009, 011) e, como a vigência é contada da assinatura, recoloca em dúvida o próprio período contratual (ACH-001). Esse efeito combinado não altera a severidade individual de cada achado.

## 4. Achados detalhados

### ACH-001 — O marco inicial da vigência muda com a nova data de assinatura

- **Tipo:** CTR / ALTERADO
- **Severidade:** Crítica
- **Confiança:** Média
- **Tópico:** Vigência
- **Padrão entre documentos:** A ≠ B

**Evidências**

- DOC-A, cl. 3.1 (p. 2): "O presente contrato vigorará pelo prazo de 12 (doze) meses, contados da data de sua assinatura, podendo ser prorrogado mediante termo aditivo."
- DOC-A, local e data (p. 6): "São Paulo, 10 de março de 2026."
- DOC-B, cl. 3.1 (par. 13): "O presente contrato vigorará pelo prazo de 12 (doze) meses, contados da data de sua assinatura, podendo ser prorrogado mediante termo aditivo."
- DOC-B, local e data (par. 40): "São Paulo, 2 de setembro de 2026."
- **Citação verificada:** Sim (DOC-A e DOC-B)

**Ponto exato da diferença**

| Elemento                   | DOC-A               | DOC-B                 |
| -------------------------- | ------------------- | --------------------- |
| Texto da cl. 3.1           | igual               | igual                 |
| Prazo                      | 12 meses            | 12 meses              |
| Marco (data de assinatura) | 10 de março de 2026 | 2 de setembro de 2026 |

**Análise** A cláusula 3.1 é idêntica, mas usa a data de assinatura como marco, e cada versão traz uma data diferente. Lida literalmente, a v1.0 corre de 10/03/2026 a cerca de 10/03/2027, e a v2.0 recomeça a contagem em 02/09/2026, terminando por volta de 02/09/2027. Os dois períodos não podem valer ao mesmo tempo para o mesmo contrato, o que caracteriza CTR (valor diferente do mesmo item). A confiança é Média porque depende da premissa P2 (nenhum dos documentos diz expressamente que a data do bloco de assinatura é a data de assinatura) e porque DOC-B não informa se substitui DOC-A com nova vigência ou se apenas consolida o texto mantendo o marco original. A datação em si está no inventário; o achado trata apenas do efeito sobre a vigência. Severidade pela âncora Crítica: muda um elemento essencial (vigência).

**Impacto / risco** Incerteza sobre a data de término e de prorrogação, e sobre qual versão rege o período de 10/03/2026 a 02/09/2026. Possível disputa sobre extensão do contrato em cerca de seis meses sem termo aditivo, que é o instrumento previsto na própria cl. 3.1 para prorrogação.

**Recomendação** Incluir em DOC-B uma cláusula que diga expressamente se ele substitui DOC-A, a partir de quando, e qual é o marco da vigência (data original ou nova). Avaliar com o jurídico se a mudança deveria ser formalizada como termo aditivo.

**Verificado (revisor):** ☐

------

### ACH-002 — Prazo de correção de falhas críticas passa de 30 para 45 dias corridos

- **Tipo:** CTR / ALTERADO
- **Severidade:** Alta
- **Confiança:** Alta
- **Tópico:** Prazos de atendimento
- **Padrão entre documentos:** A ≠ B

**Evidências**

- DOC-A, cl. 4.2 (p. 3): "A CONTRATADA deverá concluir a correção de falhas de severidade crítica em até 30 (trinta) dias corridos, contados da abertura do chamado."
- DOC-B, cl. 4.2 (par. 16): "A CONTRATADA deverá concluir a correção de falhas de severidade crítica em até 45 (quarenta e cinco) dias corridos, contados da abertura do chamado."
- **Citação verificada:** Sim (DOC-A e DOC-B)

**Ponto exato da diferença**

| Elemento                 | DOC-A               | DOC-B                       |
| ------------------------ | ------------------- | --------------------------- |
| Prazo                    | 30 (trinta)         | 45 (quarenta e cinco)       |
| Tipo de contagem         | dias corridos       | dias corridos (igual)       |
| Marco inicial            | abertura do chamado | abertura do chamado (igual) |
| Responsável / modalidade | CONTRATADA · deverá | CONTRATADA · deverá (igual) |

**Análise** A mesma obrigação recebe dois prazos distintos; não podem valer juntos → CTR. Só o número muda. Severidade pela âncora Alta (exemplo literal: prazo de correção de 30 para 45 dias).

**Impacto / risco** Falhas críticas (sistema indisponível, conforme Anexo II) podem ficar sem correção por até 15 dias a mais sem caracterizar descumprimento. Interage com ACH-006, que retira a multa por atraso nesses prazos.

**Recomendação** Confirmar com os responsáveis se a ampliação foi intencional e registrar a decisão.

**Verificado (revisor):** ☐

------

### ACH-003 — Anexo II: prazo de atendimento da severidade baixa passa de 5 para 10 dias úteis

- **Tipo:** CTR / ALTERADO
- **Severidade:** Alta
- **Confiança:** Alta
- **Tópico:** Prazos de atendimento (Matriz de Severidade)
- **Padrão entre documentos:** A ≠ B

**Evidências**

- DOC-A, Anexo II (p. 7, Tabela 1, linha Baixa, col. Prazo de atendimento): "Até 5 dias úteis"
- DOC-B, Anexo II (Tabela 1, linha 4, col. 3): "Até 10 dias úteis"
- **Citação verificada:** Sim (DOC-A e DOC-B)

**Ponto exato da diferença**

| Elemento                      | DOC-A      | DOC-B              |
| ----------------------------- | ---------- | ------------------ |
| Prazo                         | 5          | 10                 |
| Unidade                       | dias úteis | dias úteis (igual) |
| Descrição da severidade baixa | igual      | igual              |

**Análise** Mesmo item da matriz com dois valores → CTR. Na v1.0 o valor era coerente com a cl. 4.3; na v2.0 deixou de ser (ver ACH-004).

**Impacto / risco** Dobra o prazo de atendimento de chamados de severidade baixa, caso o Anexo II prevaleça sobre a cl. 4.3.

**Recomendação** Decidir o prazo pretendido e harmonizar a matriz e a cl. 4.3 (ver ACH-004).

**Verificado (revisor):** ☐

------

### ACH-004 — DOC-B: cláusula 4.3 e Anexo II fixam prazos diferentes para a severidade baixa

- **Tipo:** INT
- **Severidade:** Alta
- **Confiança:** Alta
- **Tópico:** Prazos de atendimento
- **Padrão entre documentos:** defeito só em DOC-B (em DOC-A, cl. 4.3 e Anexo II indicam o mesmo prazo, cinco dias úteis)

**Evidências**

- DOC-B, cl. 4.3 (par. 17): "Os chamados de severidade baixa serão atendidos em até 5 (cinco) dias úteis, conforme a Matriz de Severidade do Anexo II."
- DOC-B, Anexo II (Tabela 1, linha 4, col. 3): "Até 10 dias úteis"
- **Citação verificada:** Sim (DOC-B)

**Ponto exato da diferença**

| Elemento                    | DOC-B cl. 4.3 (par. 17) | DOC-B Anexo II (Tabela 1, linha 4) |
| --------------------------- | ----------------------- | ---------------------------------- |
| Prazo para severidade baixa | 5 (cinco) dias úteis    | 10 dias úteis                      |
| Unidade                     | dias úteis              | dias úteis                         |

**Análise** A cláusula fixa um número e, na mesma frase, remete à matriz, que fixa outro. Não se sabe qual é o prazo contratual para medir o cumprimento. A incerteza aumenta porque, em DOC-B, o Anexo II não consta da lista de anexos que integram o contrato (ver ACH-008 e ACH-009). Achado separado do ACH-003 conforme a regra de unidade. Severidade pela âncora Alta (cláusula × anexo com prazos diferentes).

**Impacto / risco** Disputa sobre atraso em chamados de severidade baixa; base incerta para qualquer consequência prevista na Cláusula 8.

**Recomendação** Unificar o prazo na cl. 4.3 e no Anexo II, ou declarar qual prevalece.

**Verificado (revisor):** ☐

------

### ACH-005 — O relatório mensal de desempenho deixa de ser obrigatório

- **Tipo:** CTR / ALTERADO
- **Severidade:** Alta
- **Confiança:** Alta
- **Tópico:** Obrigações da CONTRATADA
- **Padrão entre documentos:** A ≠ B

**Evidências**

- DOC-A, cl. 5.2 (p. 3): "A CONTRATADA deverá emitir relatório mensal de desempenho até o 5º (quinto) dia útil de cada mês."
- DOC-B, cl. 5.2 (par. 20): "A CONTRATADA poderá emitir relatório mensal de desempenho até o 5º (quinto) dia útil de cada mês."
- **Citação verificada:** Sim (DOC-A e DOC-B)

**Ponto exato da diferença**

| Elemento                          | DOC-A              | DOC-B              |
| --------------------------------- | ------------------ | ------------------ |
| Modalidade                        | deverá (obrigação) | poderá (faculdade) |
| Prazo, periodicidade, responsável | igual              | igual              |

**Análise** Só muda o verbo modal; pela regra de desempate, mudança de obrigação para faculdade é CTR. Severidade pela âncora Alta (relatório obrigatório que vira facultativo).

**Impacto / risco** A CONTRATANTE perde o instrumento regular de acompanhamento do desempenho, do qual depende o gestor do contrato previsto na cl. 6.2. Sem relatório, fica mais difícil comprovar descumprimento dos prazos da Cláusula 4.

**Recomendação** Confirmar se a mudança foi intencional; se o relatório deve ser mantido, voltar a usar a modalidade obrigatória.

**Verificado (revisor):** ☐

------

### ACH-006 — A multa de 2% é substituída por "medidas cabíveis" não definidas

- **Tipo:** NCL / ALTERADO
- **Severidade:** Alta
- **Confiança:** Alta
- **Tópico:** Penalidades
- **Padrão entre documentos:** A ≠ B

**Evidências**

- DOC-A, cl. 8.1 (p. 4): "O descumprimento dos prazos previstos na Cláusula 4 sujeitará a CONTRATADA a multa de 2% (dois por cento) sobre o valor mensal, por ocorrência."
- DOC-B, cl. 8.1 (par. 29): **NÃO CLARO.** "O descumprimento dos prazos previstos na Cláusula 4 poderá ensejar a aplicação das medidas cabíveis." Trata das consequências do atraso, mas não define sanção, valor nem base de cálculo. Busca em todo o DOC-B por `multa`, `penalidade` e `sanç`: só aparece o título da Cláusula 8 (par. 28); nenhuma outra cláusula define as medidas.
- **Citação verificada:** Sim (DOC-A e DOC-B)

**Ponto exato da diferença**

| Elemento        | DOC-A                                   | DOC-B                                    |
| --------------- | --------------------------------------- | ---------------------------------------- |
| Gatilho         | descumprimento dos prazos da Cláusula 4 | igual                                    |
| Consequência    | multa de 2% (dois por cento)            | "medidas cabíveis" (não definidas)       |
| Base de cálculo | valor mensal                            | não especificada                         |
| Incidência      | por ocorrência                          | não especificada                         |
| Modalidade      | "sujeitará" (consequência certa)        | "poderá ensejar" (consequência eventual) |

**Análise** Pela regra de desempate, a troca de um conteúdo objetivo por uma redação vaga sobre o mesmo tema é NCL. A mudança de modalidade faz parte do mesmo item e não gera achado separado. Severidade pela âncora Alta (multa trocada por "medidas cabíveis").

**Impacto / risco** Sem sanção definida, os prazos da Cláusula 4 (inclusive os alterados em ACH-002 e ACH-003) deixam de ter consequência objetiva, e qualquer medida aplicada fica sujeita a disputa.

**Recomendação** Esclarecer com os responsáveis quais são as medidas pretendidas e definir sanção, valor e base de cálculo, ou restabelecer a multa.

**Verificado (revisor):** ☐

------

### ACH-007 — A cláusula de seguro de responsabilidade civil foi removida

- **Tipo:** EXC / REMOVIDO
- **Severidade:** Alta
- **Confiança:** Alta
- **Tópico:** Seguro / garantias
- **Padrão entre documentos:** A ≠ B

**Evidências**

- DOC-A, cl. 10 (p. 5): "Cláusula 10 – Do Seguro"
- DOC-A, cl. 10.1 (p. 5): "A CONTRATADA manterá, durante toda a vigência deste contrato, apólice de seguro de responsabilidade civil profissional com cobertura mínima de R$ 500.000,00 (quinhentos mil reais)."
- DOC-B: **NÃO PRESENTE.** Seções verificadas: todo o corpo (par. 8–45) e a Tabela 1, com atenção à Cláusula 5 – Obrigações da CONTRATADA (par. 18–20), Cláusula 8 – Penalidades (par. 28–29), Cláusula 10 (par. 33–34, que agora trata de proteção de dados), Cláusula 11 (par. 35–36), Cláusula 12 (par. 37–39) e Anexo I (par. 43–44). Termos buscados: `seguro`, `apólice`, `responsabilidade civil`, `cobertura`, `indeniz`, `garantia`, `500.000`. Conteúdo relacionado: nenhum.
- **Citação verificada:** Sim (DOC-A)

**Ponto exato da diferença**

| Elemento                   | DOC-A          | DOC-B                              |
| -------------------------- | -------------- | ---------------------------------- |
| Obrigação de manter seguro | sim (cl. 10.1) | não presente                       |
| Cobertura mínima           | R$ 500.000,00  | —                                  |
| Número da Cláusula 10      | Do Seguro      | reutilizado para Proteção de Dados |

**Análise** O tema inteiro desapareceu, então é EXC. A renumeração (a antiga Cláusula 11 virou Cláusula 10) pode esconder a remoção em uma comparação feita pela numeração. Severidade pela âncora Alta (remove garantia/seguro).

**Impacto / risco** A CONTRATANTE perde a cobertura de danos causados pela CONTRATADA na prestação dos serviços.

**Recomendação** Confirmar se a remoção foi intencional; se não foi, restabelecer a cláusula.

**Verificado (revisor):** ☐

------

### ACH-008 — A cláusula 12.1 deixa de listar o Anexo II e passa a listar um "Anexo IV"

- **Tipo:** CTR / ALTERADO
- **Severidade:** Alta
- **Confiança:** Alta
- **Tópico:** Disposições gerais — anexos integrantes
- **Padrão entre documentos:** A ≠ B

**Evidências**

- DOC-A, cl. 12.1 (p. 6): "Integram este contrato o Anexo I (Descrição dos Serviços) e o Anexo II (Matriz de Severidade)."
- DOC-B, cl. 12.1 (par. 38): "Integram este contrato o Anexo I (Descrição dos Serviços) e o Anexo IV (Matriz de Severidade)."
- **Citação verificada:** Sim (DOC-A e DOC-B)

**Ponto exato da diferença**

| Elemento            | DOC-A                            | DOC-B    |
| ------------------- | -------------------------------- | -------- |
| 1º anexo integrante | Anexo I (Descrição dos Serviços) | igual    |
| Número do 2º anexo  | Anexo II                         | Anexo IV |
| Título do 2º anexo  | Matriz de Severidade             | igual    |

**Análise** O mesmo item (lista de anexos integrantes) passa a ter conteúdo diferente → CTR. Consequência entre versões: em DOC-B, o anexo que contém a Matriz de Severidade (Anexo II) não é mais declarado integrante do contrato. Pode ser um erro de digitação, mas isso é hipótese e só os responsáveis podem confirmar. O defeito de referência interno a DOC-B está no ACH-009. Severidade pela âncora Alta (cláusula de integração que deixa de listar o anexo com os SLAs).

**Impacto / risco** Discussão sobre a força vinculante da Matriz de Severidade, da qual dependem as cl. 4.3 e 8.1.

**Recomendação** Corrigir a cl. 12.1 de DOC-B para listar o anexo correto.

**Verificado (revisor):** ☐

------

### ACH-009 — DOC-B remete a um "Anexo IV" que não existe no documento

- **Tipo:** REF
- **Severidade:** Alta
- **Confiança:** Alta
- **Tópico:** Disposições gerais — anexos integrantes
- **Padrão entre documentos:** defeito só em DOC-B

**Evidências**

- DOC-B, cl. 12.1 (par. 38): "Integram este contrato o Anexo I (Descrição dos Serviços) e o Anexo IV (Matriz de Severidade)."
- DOC-B, Anexo II (par. 45): "Anexo II – Matriz de Severidade"
- DOC-B, cl. 4.3 (par. 17): "[...] conforme a Matriz de Severidade do Anexo II."
- DOC-B, Anexo IV: **NÃO PRESENTE.** Anexos existentes: Anexo I (par. 43) e Anexo II (par. 45). Termos buscados: `Anexo IV`, `Anexo III` — única ocorrência é a própria cl. 12.1 (par. 38).
- **Citação verificada:** Sim (DOC-B)

**Ponto exato da diferença**

| Elemento                                | DOC-B cl. 12.1 | DOC-B corpo e anexos                             |
| --------------------------------------- | -------------- | ------------------------------------------------ |
| Número do anexo da Matriz de Severidade | Anexo IV       | Anexo II (título do anexo e remissão da cl. 4.3) |
| Existência do anexo citado              | —              | Anexo IV inexistente                             |

**Análise** Referência a um anexo inexistente e, dentro de DOC-B, dois números diferentes para a mesma Matriz. Achado separado do ACH-008 pela regra de unidade (aqui é o defeito interno; lá, a mudança entre versões). Severidade pela âncora Alta (referência quebrada que deixa incerto qual regra material vale).

**Impacto / risco** Uma das partes pode alegar que a Matriz de Severidade não integra o contrato, o que afeta prazos de atendimento e penalidades.

**Recomendação** Corrigir a remissão da cl. 12.1 (ou, se existir de fato um Anexo IV, anexá-lo).

**Verificado (revisor):** ☐

------

### ACH-010 — Na Cláusula 6, a parte obrigada passa a ser chamada de CLIENTE em vez de CONTRATANTE

- **Tipo:** TER / ALTERADO
- **Severidade:** Média
- **Confiança:** Alta
- **Tópico:** Obrigações da CONTRATANTE
- **Padrão entre documentos:** A ≠ B

**Evidências**

- DOC-A, cl. 6 (p. 4): "Cláusula 6 – Das Obrigações da CONTRATANTE"
- DOC-A, cl. 6.1 (p. 4): "A CONTRATANTE deverá fornecer à CONTRATADA acesso remoto ao ambiente do sistema, nos termos da política de segurança da informação da CONTRATANTE."
- DOC-A, cl. 6.2 (p. 4): "A CONTRATANTE deverá designar um gestor do contrato, responsável por acompanhar a execução dos serviços."
- DOC-B, cl. 6 (par. 21): "Cláusula 6 – Das Obrigações do CLIENTE"
- DOC-B, cl. 6.1 (par. 22): "O CLIENTE deverá fornecer à CONTRATADA acesso remoto ao ambiente do sistema, nos termos da política de segurança da informação do CLIENTE."
- DOC-B, cl. 6.2 (par. 23): "O CLIENTE deverá designar um gestor do contrato, responsável por acompanhar a execução dos serviços."
- **Citação verificada:** Sim (DOC-A e DOC-B)

**Ponto exato da diferença**

| Elemento                                                     | DOC-A       | DOC-B   |
| ------------------------------------------------------------ | ----------- | ------- |
| Designação no título, no sujeito de 6.1 e 6.2 e no titular da política de segurança | CONTRATANTE | CLIENTE |
| Obrigações (acesso remoto; designação de gestor), modalidade | igual       | igual   |

**Análise** O conteúdo das obrigações não muda; só muda o nome da parte obrigada. Como há uma única parte contratante, o sentido ainda é inferível pelo contexto. Severidade pela âncora Média (termo não definido usado no lugar do definido). O defeito interno de DOC-B está no ACH-011.

**Impacto / risco** Abre espaço para questionar a quem cabem as obrigações de acesso remoto e de designação do gestor, das quais depende a execução dos serviços.

**Recomendação** Usar o termo definido (CONTRATANTE) em toda a Cláusula 6.

**Verificado (revisor):** ☐

------

### ACH-011 — DOC-B usa um termo não definido (CLIENTE) ao lado do termo definido (CONTRATANTE)

- **Tipo:** TER
- **Severidade:** Média
- **Confiança:** Alta
- **Tópico:** Definições das partes
- **Padrão entre documentos:** defeito só em DOC-B

**Evidências**

- DOC-B, cl. 1.1 (par. 9): "BETA LOGÍSTICA S.A., doravante denominada CONTRATANTE, e ALFA SISTEMAS LTDA., doravante denominada CONTRATADA [...]"
- DOC-B, cl. 6.1 (par. 22): "O CLIENTE deverá fornecer à CONTRATADA acesso remoto ao ambiente do sistema [...]"
- DOC-B, cl. 9.2 (par. 32): "A rescisão por iniciativa da CONTRATANTE dependerá de prévia aprovação de sua Diretoria Jurídica."
- Busca por `CLIENTE` em DOC-B: só nos par. 21, 22 e 23 (Cláusula 6); nenhuma definição. `CONTRATANTE` aparece nos par. 5, 9, 11, 25, 32, 36 e 41.
- **Citação verificada:** Sim (DOC-B)

**Ponto exato da diferença**

| Elemento                          | DOC-B cl. 1.1 e demais cláusulas | DOC-B Cláusula 6       |
| --------------------------------- | -------------------------------- | ---------------------- |
| Nome da parte Beta Logística S.A. | CONTRATANTE (definido)           | CLIENTE (não definido) |

**Análise** O mesmo conceito tem dois nomes no mesmo documento, e um deles não tem definição. Achado separado do ACH-010 pela regra de unidade. Severidade pela âncora Média.

**Impacto / risco** Mesmo do ACH-010; também prejudica a consistência de futuras remissões ao termo.

**Recomendação** Eliminar o termo CLIENTE ou, se for intencional, defini-lo na cl. 1.1.

**Verificado (revisor):** ☐

------

### ACH-012 — A rescisão por iniciativa da CONTRATANTE passa a depender de aprovação da Diretoria Jurídica

- **Tipo:** DIV / INCLUÍDO
- **Severidade:** Média
- **Confiança:** Alta
- **Tópico:** Rescisão
- **Padrão entre documentos:** A ≠ B

**Evidências**

- DOC-B, cl. 9.2 (par. 32): "A rescisão por iniciativa da CONTRATANTE dependerá de prévia aprovação de sua Diretoria Jurídica."
- DOC-A: sem correspondente para a condição. Seções verificadas: Cláusula 9 (p. 5) e todo o documento (p. 1–7). Termos buscados: `aprovação`, `Diretoria`, `Jurídica`. Conteúdo relacionado: a regra geral de rescisão, idêntica nas duas versões — DOC-A, cl. 9.1 (p. 5): "Qualquer das partes poderá rescindir este contrato mediante notificação por escrito, com antecedência mínima de 30 (trinta) dias." · DOC-B, cl. 9.1 (par. 31): "Qualquer das partes poderá rescindir este contrato mediante notificação por escrito, com antecedência mínima de 30 (trinta) dias."
- **Citação verificada:** Sim (DOC-A e DOC-B)

**Ponto exato da diferença**

| Elemento                                  | DOC-A               | DOC-B                                      |
| ----------------------------------------- | ------------------- | ------------------------------------------ |
| Direito de rescindir com 30 dias de aviso | qualquer das partes | igual                                      |
| Condição adicional para a CONTRATANTE     | nenhuma             | prévia aprovação de sua Diretoria Jurídica |
| Condição adicional para a CONTRATADA      | nenhuma             | nenhuma                                    |

**Análise** A regra de rescisão existe nos dois documentos; DOC-B acrescenta uma condição para uma das partes → DIV / INCLUÍDO (não é EXC, porque o tema existe nos dois). A condição é uma etapa interna da CONTRATANTE inserida no contrato e cria assimetria em relação à regra de que qualquer das partes pode rescindir. Se uma notificação sem essa aprovação é válida perante a CONTRATADA é uma questão jurídica, fora do escopo desta análise; recomenda-se avaliação por especialista. Severidade pela âncora Média (aprovação interna antes de rescindir).

**Impacto / risco** A CONTRATADA pode contestar uma rescisão alegando falta da aprovação, que ela não tem como verificar.

**Recomendação** Confirmar se a condição deve constar do contrato ou só de normas internas da CONTRATANTE; se for mantida, definir como a aprovação é comprovada.

**Verificado (revisor):** ☐

## 5. Itens convergentes

Fragmentos literais contíguos. A nota **ver ACH** indica item idêntico entre as versões que participa de um achado com **outro** item.

**Partes e objeto**

- **Qualificação das partes** (EQV-L) — DOC-A cl. 1.1 (p. 2): "doravante denominada CONTRATANTE, e ALFA SISTEMAS LTDA., doravante denominada CONTRATADA" · DOC-B cl. 1.1 (par. 9): "doravante denominada CONTRATANTE, e ALFA SISTEMAS LTDA., doravante denominada CONTRATADA" — ver ACH-011
- **Objeto** (EQV-L) — DOC-A cl. 2.1 (p. 2): "manutenção corretiva e evolutiva do sistema de gestão de frota" · DOC-B cl. 2.1 (par. 11): "manutenção corretiva e evolutiva do sistema de gestão de frota"

**Vigência**

- **Prazo e marco da vigência (texto)** (EQV-L) — DOC-A cl. 3.1 (p. 2): "vigorará pelo prazo de 12 (doze) meses, contados da data de sua assinatura" · DOC-B cl. 3.1 (par. 13): "vigorará pelo prazo de 12 (doze) meses, contados da data de sua assinatura" — ver ACH-001

**Prazos de atendimento**

- **Início do atendimento, severidade crítica** (EQV-L) — DOC-A cl. 4.1 (p. 3): "em até 4 (quatro) horas corridas, contadas da abertura do chamado" · DOC-B cl. 4.1 (par. 15): "em até 4 (quatro) horas corridas, contadas da abertura do chamado"
- **Atendimento, severidade baixa (cláusula)** (EQV-L) — DOC-A cl. 4.3 (p. 3): "serão atendidos em até 5 (cinco) dias úteis" · DOC-B cl. 4.3 (par. 17): "serão atendidos em até 5 (cinco) dias úteis" — ver ACH-004

**Obrigações da CONTRATADA**

- **Equipe certificada** (EQV-L) — DOC-A cl. 5.1 (p. 3): "manter equipe técnica com certificação no sistema objeto deste contrato" · DOC-B cl. 5.1 (par. 19): "manter equipe técnica com certificação no sistema objeto deste contrato"
- **Sigilo por 5 anos** (EQV-L, **realocado**: DOC-A cl. 5.3, dentro da Cláusula 5 → DOC-B cl. 11.1, na nova Cláusula 11 – Da Confidencialidade) — DOC-A cl. 5.3 (p. 3): "manter sigilo sobre todas as informações da CONTRATANTE" · DOC-B cl. 11.1 (par. 36): "manter sigilo sobre todas as informações da CONTRATANTE"

**Preço e pagamento**

- **Valor mensal** (EQV-L) — DOC-A cl. 7.1 (p. 4): "o valor mensal de R$ 18.500,00 (dezoito mil e quinhentos reais)" · DOC-B cl. 7.1 (par. 25): "o valor mensal de R$ 18.500,00 (dezoito mil e quinhentos reais)"
- **Prazo de pagamento** (EQV-S) — DOC-A cl. 7.2 (p. 4): "em até 30 (trinta) dias após o recebimento da nota fiscal" · DOC-B cl. 7.2 (par. 26): "no prazo máximo de trinta dias, contado do recebimento da nota fiscal"
- **Reajuste** (EQV-L) — DOC-A cl. 7.3 (p. 4): "reajustado anualmente pela variação do IPCA" · DOC-B cl. 7.3 (par. 27): "reajustado anualmente pela variação do IPCA"

**Rescisão**

- **Rescisão por notificação com 30 dias** (EQV-L) — DOC-A cl. 9.1 (p. 5): "com antecedência mínima de 30 (trinta) dias" · DOC-B cl. 9.1 (par. 31): "com antecedência mínima de 30 (trinta) dias" — ver ACH-012

**Proteção de dados**

- **Tratamento de dados pessoais** (EQV-L, **renumerado**: DOC-A cl. 11.1 → DOC-B cl. 10.1; nenhuma remissão interna aponta para os números antigos) — DOC-A cl. 11.1 (p. 5): "exclusivamente para a execução do objeto deste contrato, observada a Lei nº 13.709/2018" · DOC-B cl. 10.1 (par. 34): "exclusivamente para a execução do objeto deste contrato, observada a Lei nº 13.709/2018"

**Disposições gerais e assinaturas**

- **Foro** (EQV-L) — DOC-A cl. 12.2 (p. 6): "Fica eleito o foro da Comarca de São Paulo/SP" · DOC-B cl. 12.2 (par. 39): "Fica eleito o foro da Comarca de São Paulo/SP"
- **Signatários** (EQV-L) — DOC-A (p. 6): "BETA LOGÍSTICA S.A. (CONTRATANTE)" e "ALFA SISTEMAS LTDA. (CONTRATADA)" · DOC-B (par. 41): "BETA LOGÍSTICA S.A. (CONTRATANTE)" e (par. 42): "ALFA SISTEMAS LTDA. (CONTRATADA)"

**Anexo I – Descrição dos Serviços**

- **Horário do suporte** (EQV-L) — DOC-A Anexo I (p. 7): "Suporte técnico remoto em dias úteis, das 8h às 18h" · DOC-B Anexo I (par. 44): "Suporte técnico remoto em dias úteis, das 8h às 18h"
- **Manutenção corretiva** (EQV-L) — DOC-A Anexo I (p. 7): "manutenção corretiva de falhas" · DOC-B Anexo I (par. 44): "manutenção corretiva de falhas"
- **Limite da manutenção evolutiva** (EQV-L) — DOC-A Anexo I (p. 7): "manutenção evolutiva limitada a 40 (quarenta) horas mensais" · DOC-B Anexo I (par. 44): "manutenção evolutiva limitada a 40 (quarenta) horas mensais"

**Anexo II – Matriz de Severidade**

- **Título do anexo** (EQV-L) — DOC-A Anexo II (p. 7): "Anexo II – Matriz de Severidade" · DOC-B Anexo II (par. 45): "Anexo II – Matriz de Severidade" — ver ACH-009
- **Severidade crítica** (EQV-L) — DOC-A Anexo II (p. 7, Tabela 1, linha Crítica): "Sistema indisponível" / "Início em até 4 horas corridas" · DOC-B Anexo II (Tabela 1, linha 2, col. 3): "Início em até 4 horas corridas"
- **Severidade média** (EQV-L) — DOC-A Anexo II (p. 7, Tabela 1, linha Média): "Funcionalidade degradada" / "Até 2 dias úteis" · DOC-B Anexo II (Tabela 1, linha 3, col. 3): "Até 2 dias úteis"

## 6. Declaração de cobertura e limitações

**Cobertura**

- DOC-A: páginas físicas 1 a 7 analisadas integralmente (capa, Cláusulas 1–12, bloco de assinatura, Anexos I e II, rodapés). Nenhuma página com OCR. Tabela da p. 7 extraída separadamente e conferida com o texto corrido.
- DOC-B: par. 1 a 45 e Tabela 1 (4 linhas × 3 colunas) analisados integralmente; cabeçalho e rodapé vazios; sem alterações controladas e sem comentários.
- Reconciliação: todo o conteúdo de DOC-A e DOC-B foi classificado em um dos 12 achados ou nos 20 itens convergentes. Os dados de identificação (capa, número de versão, datas de emissão, rodapé paginado de DOC-A, que não existe em DOC-B) estão no inventário e só geraram achado quando usados como marco (ACH-001).
- Conteúdo não analisado: nenhum.

**Resultado da verificação das citações** (verificação mecânica de 100% das citações, não apenas da amostra exigida: cada trecho foi buscado no texto extraído e, nas Evidências e nos Itens convergentes, também conferido no localizador indicado)

- Evidências e Itens convergentes: 77 citações conferidas · 77 confirmadas no localizador · 0 corrigidas · 0 divergentes · 0 indisponíveis.
- Trechos entre aspas nas demais seções (inventário, Ponto exato, títulos, Análise, Observações, Questões): 20 conferidos · 17 confirmados · 3 corrigidos (rótulos que tinham ficado entre aspas e foram convertidos em paráfrase ou formato de código; não sustentavam nenhum achado).

**Limitações**

- ACH-001 depende da premissa P2 (data do bloco de assinatura = data de assinatura).
- Validade jurídica não foi avaliada (ex.: oponibilidade da condição da cl. 9.2; efeitos da troca da multa por medidas indefinidas; necessidade de termo aditivo). Esses pontos exigem um especialista.
- Os metadados dos arquivos não são confiáveis para cronologia: o PDF foi gerado em 14/10/2026 e o .docx traz datas de criação/modificação de 23/12/2013 (`python-docx`). A cronologia usada vem das datas internas dos documentos.

**Observações não comparativas** (problemas iguais nos dois documentos; sem ID e fora da contagem de achados)

- **O1 — Prazo de atendimento ambíguo na Matriz (Anexo II).** Na linha da severidade crítica o prazo diz expressamente que se trata do início ("Início em até 4 horas corridas"); nas linhas média e baixa (ex.: "Até 2 dias úteis") não se diz se o prazo é de início ou de conclusão. DOC-A p. 7, Tabela 1; DOC-B Tabela 1, linhas 3 e 4.
- **O2 — Sem prazo de correção para severidades média e baixa.** A cl. 4.2 só fixa prazo de conclusão para a severidade crítica (DOC-A p. 3; DOC-B par. 16).
- **O3 — Severidade média sem cláusula correspondente.** A Cláusula 4 trata das severidades crítica (4.1, 4.2) e baixa (4.3); a média só aparece no Anexo II.
- **O4 — Reajuste sem data-base.** A cl. 7.3 prevê reajuste anual pelo IPCA sem dizer a partir de quando (DOC-A p. 4; DOC-B par. 27).
- **O5 — Partes sem qualificação.** A cl. 1.1 não traz CNPJ, endereço nem representantes legais (DOC-A p. 2; DOC-B par. 9).
- **O6 — Forma da nova versão.** A cl. 3.1 prevê prorrogação "mediante termo aditivo", mas nenhum dos documentos regula como uma nova versão substitui a anterior (relaciona-se à Q1).

## 7. Questões em aberto

1. **Q1** — DOC-B substitui DOC-A? A partir de quando? A vigência de 12 meses passa a contar de 2/9/2026 ou mantém o marco de 10/3/2026? A mudança deveria ser formalizada por termo aditivo? *Ref.: ACH-001*
2. **Q2** — O prazo de correção de falhas críticas é de 30 ou de 45 dias corridos? *Ref.: ACH-002*
3. **Q3** — O prazo para severidade baixa é de 5 ou de 10 dias úteis? Em DOC-B, qual prevalece entre a cl. 4.3 e o Anexo II? *Ref.: ACH-003, ACH-004*
4. **Q4** — Tornar o relatório mensal facultativo foi intencional? Como o gestor do contrato (cl. 6.2) vai acompanhar o desempenho sem ele? *Ref.: ACH-005*
5. **Q5** — Quais são as medidas aplicáveis ao descumprimento dos prazos? A multa de 2% deve ser mantida? *Ref.: ACH-006*
6. **Q6** — A remoção da obrigação de seguro de responsabilidade civil foi intencional? *Ref.: ACH-007*
7. **Q7** — O Anexo IV da cl. 12.1 é erro de digitação por Anexo II, ou falta um anexo em DOC-B? *Ref.: ACH-008, ACH-009*
8. **Q8** — CLIENTE e CONTRATANTE designam a mesma parte? O termo pode ser unificado? *Ref.: ACH-010, ACH-011*
9. **Q9** — A condição de aprovação pela Diretoria Jurídica deve constar do contrato? Quais os efeitos de uma notificação de rescisão feita sem ela? (requer avaliação jurídica) *Ref.: ACH-012*