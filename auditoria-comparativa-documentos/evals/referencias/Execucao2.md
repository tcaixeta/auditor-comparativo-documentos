## Análise comparativa: Contrato nº 041/2026, v1.0 (DOC-A) × v2.0 (DOC-B)

### 1. Identificação e escopo

| ID        | Título                                                       | Versão | Data       | Emissor                                                      | Páginas                        | Esquema de localização                                       | Integridade                                                  |
| --------- | ------------------------------------------------------------ | ------ | ---------- | ------------------------------------------------------------ | ------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **DOC-A** | Contrato de Prestação de Serviços de Suporte Técnico e Manutenção de Software, nº 041/2026 | 1.0    | 10/03/2026 | CONTRATANTE: Beta Logística S.A.; CONTRATADA: Alfa Sistemas Ltda. | 7 físicas (capa + 6 numeradas) | Cláusula + **página física** (p. N). O rodapé impresso (“Página 1 de 6”) começa na p. física 2, então página impressa = física − 1. Uso a física. | Texto nativo nas 7 páginas, extraído página a página. Sem OCR, nada ilegível. Anexo II é uma tabela na p. 7. |
| **DOC-B** | Mesmo título, nº 041/2026                                    | 2.0    | 02/09/2026 | Mesmas partes                                                | Não paginado (.docx)           | Cláusula + **par. N** (ordem do parágrafo no corpo do .docx, contando o título como par. 1). Tabela: “Tabela 1, linha L, col. C”. | 45 parágrafos e 1 tabela (4×3). **Sem alterações controladas e sem comentários.** Cabeçalho e rodapé vazios. |

### 2. Relação entre os documentos e premissas

**Relação identificada: versões (v1.0 → v2.0).** As bases são o mesmo número de contrato, as mesmas partes e o mesmo título, além de “Versão 1.0” (DOC-A, p. 1) e “Versão 2.0” (DOC-B, par. 3), com datas posteriores no DOC-B.

**Premissa:** o DOC-B é a versão mais recente e pretende substituir o DOC-A por inteiro. Por isso os achados levam os rótulos INCLUÍDO, REMOVIDO e ALTERADO. **Limite da premissa:** o DOC-B não tem nenhuma cláusula dizendo que substitui ou revoga a v1.0 (ver ACH-009).

**O que muda se a premissa estiver errada:**

- **Se o DOC-B for um aditivo:** as cláusulas da v1.0 que não aparecem no DOC-B, como o Seguro (ACH-005), poderiam continuar valendo. “REMOVIDO” passaria a ser “não alterado”.
- **Se forem minutas concorrentes:** nenhuma das duas prevalece. Os rótulos de versão caem e cada diferença vira uma divergência a decidir.

### 3. Resumo quantitativo

| Tipo               | Qtd. |      | Severidade           | Qtd.   |
| ------------------ | ---- | ---- | -------------------- | ------ |
| CTR                | 1    |      | Crítica              | 0      |
| INT                | 2    |      | Alta                 | 6      |
| DIV                | 3    |      | Média                | 4      |
| NCL                | 3    |      | Baixa                | 1      |
| EXC                | 1    |      | Informativa          | 2      |
| REF                | 1    |      | **Total de achados** | **13** |
| TER                | 1    |      | Itens convergentes   | 20     |
| EQV-L (realocação) | 1    |      |                      |        |

**Carga de revisão humana:** 3 itens em NÃO CLARO (ACH-004, 009, 010) e 0 em REQUER REVISÃO.

**Leitura geral (análise):** a v2.0 enfraquece o regime de nível de serviço a favor da CONTRATADA em quatro pontos ao mesmo tempo:

- prazo de correção crítica de 30 para 45 dias (ACH-001);
- prazo de severidade baixa de 5 para 10 dias úteis, só no Anexo (ACH-002);
- relatório mensal que deixa de ser obrigatório (ACH-003);
- multa objetiva substituída por “medidas cabíveis” (ACH-004).

Ela também remove o seguro (ACH-005) e cria problemas de redação: uma referência a anexo inexistente (ACH-006), um termo não definido (ACH-007) e uma contradição interna (ACH-002). Individualmente classifiquei cada achado como Alta. Juntos, eles merecem uma decisão consolidada.

### 4. Achados detalhados

#### ACH-001: Prazo de correção de falhas críticas ampliado de 30 para 45 dias

- **Tipo:** CTR / ALTERADO
- **Severidade:** Alta
- **Confiança:** Alta
- **Tópico:** Prazos de atendimento
- **Padrão:** A ≠ B

**Evidências**

- DOC-A, cl. 4.2 (p. 3): “4.2 A CONTRATADA deverá concluir a correção de falhas de severidade crítica em até 30 (trinta) dias corridos, contados da abertura do chamado.”
- DOC-B, cl. 4.2 (par. 16): “4.2 A CONTRATADA deverá concluir a correção de falhas de severidade crítica em até 45 (quarenta e cinco) dias corridos, contados da abertura do chamado.”
- **Citação verificada:** Sim (DOC-A e DOC-B)

**Ponto exato da diferença**

| Elemento      | DOC-A               | DOC-B                       |
| ------------- | ------------------- | --------------------------- |
| Prazo         | 30 dias             | 45 dias                     |
| Contagem      | corridos            | corridos (igual)            |
| Marco inicial | abertura do chamado | abertura do chamado (igual) |

**Análise.** Os dois valores não podem valer ao mesmo tempo para a mesma obrigação, por isso é CTR. O resto da frase é idêntico, então a mudança está isolada no número. É um aumento de 50% no prazo, a favor da CONTRATADA.

**Impacto / risco.** Na v1.0, a cl. 8.1 multava o descumprimento desse prazo. Na v2.0 o prazo aumenta e a multa deixa de existir (ACH-004). Uma falha crítica pode ficar sem correção por até 45 dias sem sanção definida.

**Recomendação.** A CONTRATANTE deve confirmar se a ampliação foi negociada. Se não foi, restabelecer os 30 dias.

**Verificado (revisor):** ☐

#### ACH-002: Prazo da severidade baixa: 5 dias úteis na cl. 4.3 × 10 dias úteis no Anexo II do DOC-B

- **Tipo:** INT (no DOC-B) / ALTERADO (no Anexo II)
- **Severidade:** Alta
- **Confiança:** Alta
- **Tópico:** Prazos de atendimento / Matriz de Severidade
- **Padrão:** A (cl. 4.3) = A (Anexo II) = B (cl. 4.3) ≠ B (Anexo II)

**Evidências**

- DOC-A, cl. 4.3 (p. 3): “4.3 Os chamados de severidade baixa serão atendidos em até 5 (cinco) dias úteis, conforme a Matriz de Severidade do Anexo II.”
- DOC-A, Anexo II, tabela, linha “Baixa”, col. “Prazo de atendimento” (p. 7): “Até 5 dias úteis”
- DOC-B, cl. 4.3 (par. 17): “4.3 Os chamados de severidade baixa serão atendidos em até 5 (cinco) dias úteis, conforme a Matriz de Severidade do Anexo II.”
- DOC-B, Anexo II, Tabela 1, linha 4 (“Baixa”), col. 3: “Até 10 dias úteis”
- **Citação verificada:** Sim (todas)

**Ponto exato da diferença**

| Elemento      | DOC-A cl. 4.3 | DOC-A Anexo II | DOC-B cl. 4.3 | DOC-B Anexo II    |
| ------------- | ------------- | -------------- | ------------- | ----------------- |
| Prazo (baixa) | 5 dias úteis  | 5 dias úteis   | 5 dias úteis  | **10 dias úteis** |

**Análise.** Na v2.0 só a linha da tabela foi alterada. A cláusula que remete a essa mesma tabela (“conforme a Matriz [...] do Anexo II”) continua com 5 dias. O DOC-B passa a se contradizer: a cláusula diz 5 e a fonte que ela cita diz 10. Não há regra de precedência entre cláusula e anexo nos documentos. Pode ter sido uma alteração incompleta ou intencional, e os documentos não permitem saber.

**Impacto / risco.** Disputa sobre qual prazo vale. A parte que se beneficia de cada leitura tende a invocá-la. O problema se agrava com o ACH-006, porque o Anexo II pode nem estar formalmente integrado à v2.0.

**Recomendação.** Decidir o prazo (5 ou 10) e alinhar a cl. 4.3 e o Anexo II. Incluir uma regra de precedência entre cláusulas e anexos.

**Verificado (revisor):** ☐

#### ACH-003: Relatório mensal de desempenho deixa de ser obrigatório (“deverá” → “poderá”)

- **Tipo:** DIV / ALTERADO
- **Severidade:** Alta
- **Confiança:** Alta
- **Tópico:** Obrigações da CONTRATADA
- **Padrão:** A ≠ B

**Evidências**

- DOC-A, cl. 5.2 (p. 3): “5.2 A CONTRATADA deverá emitir relatório mensal de desempenho até o 5º (quinto) dia útil de cada mês.”
- DOC-B, cl. 5.2 (par. 20): “5.2 A CONTRATADA poderá emitir relatório mensal de desempenho até o 5º (quinto) dia útil de cada mês.”
- **Citação verificada:** Sim (DOC-A e DOC-B)

**Ponto exato da diferença**

| Elemento                     | DOC-A                                        | DOC-B                  |
| ---------------------------- | -------------------------------------------- | ---------------------- |
| Modalidade                   | **deverá** (obrigação)                       | **poderá** (faculdade) |
| Prazo, periodicidade, objeto | 5º dia útil, mensal, relatório de desempenho | idênticos              |

**Análise.** É uma mudança de modalidade com o resto da frase idêntico. Classifiquei como DIV e não como CTR porque emitir o relatório cumpre as duas versões. Mas a v2.0 elimina a exigibilidade. O prazo de “até o 5º dia útil” continua no texto, mas fica sem efeito prático, já que não há obrigação a que ele se aplique.

**Impacto / risco.** A CONTRATANTE perde o instrumento contratual de acompanhamento dos prazos da Cl. 4, o que afeta a fiscalização pelo gestor (cl. 6.2).

**Recomendação.** Confirmar se a flexibilização foi intencional. Se não foi, voltar para “deverá”.

**Verificado (revisor):** ☐

#### ACH-004: Multa de 2% por descumprimento de prazo substituída por “medidas cabíveis”

- **Tipo:** NCL / ALTERADO
- **Severidade:** Alta
- **Confiança:** Alta
- **Tópico:** Penalidades
- **Padrão:** A ≠ B

**Evidências**

- DOC-A, cl. 8.1 (p. 4): “8.1 O descumprimento dos prazos previstos na Cláusula 4 sujeitará a CONTRATADA a multa de 2% (dois por cento) sobre o valor mensal, por ocorrência.”
- DOC-B, cl. 8.1 (par. 29): **NÃO CLARO.** “8.1 O descumprimento dos prazos previstos na Cláusula 4 poderá ensejar a aplicação das medidas cabíveis.” O texto trata da consequência do descumprimento, mas não define sanção, valor, base nem forma de cálculo.
- **Citação verificada:** Sim (DOC-A e DOC-B)

**Ponto exato da diferença**

| Elemento     | DOC-A                    | DOC-B                           |
| ------------ | ------------------------ | ------------------------------- |
| Consequência | multa                    | “medidas cabíveis” (indefinido) |
| Valor / base | 2% sobre o valor mensal  | não definido                    |
| Incidência   | por ocorrência           | não definida                    |
| Modalidade   | “sujeitará” (automático) | “poderá ensejar” (facultativo)  |
| Gatilho      | prazos da Cláusula 4     | prazos da Cláusula 4 (igual)    |

**Análise.** A mudança em si é certa: a multa objetiva foi retirada. O item ficou como NCL porque o que a v2.0 coloca no lugar não pode ser classificado com segurança. Não há outra cláusula no DOC-B que defina essas “medidas”. Busquei “multa”, “sanção” e “2%” sem resultado; “penalidade” aparece só no título da Cl. 8.

**Impacto / risco.** Os prazos da Cl. 4 deixam de ter consequência predefinida. Aplicar qualquer sanção dependeria de negociação ou disputa. Somado aos ACH-001 e ACH-003, o nível de serviço fica com pouca exigibilidade.

**Recomendação.** Definir as “medidas cabíveis” (tipo, valor, base e limite) ou restabelecer a multa. A eficácia jurídica de uma cláusula penal genérica deve ser avaliada pelo jurídico.

**Verificado (revisor):** ☐

#### ACH-005: Cláusula de seguro de responsabilidade civil removida

- **Tipo:** EXC / REMOVIDO
- **Severidade:** Alta
- **Confiança:** Alta
- **Tópico:** Seguro / garantias
- **Padrão:** A ≠ B (só em A)

**Evidências**

- DOC-A, Cláusula 10, título (p. 5): “Cláusula 10 – Do Seguro”
- DOC-A, cl. 10.1 (p. 5): “10.1 A CONTRATADA manterá, durante toda a vigência deste contrato, apólice de seguro de responsabilidade civil profissional com cobertura mínima de R$ 500.000,00 (quinhentos mil reais).”
- DOC-B: **NÃO PRESENTE.**
  - Seções verificadas: todas as Cláusulas 1 a 12, em especial a 5 (Obrigações da CONTRATADA), a 8 (Penalidades), a 10 e a 11, além dos Anexos I e II.
  - Termos buscados: “seguro”, “apólice”, “responsabilidade civil”, “cobertura”, “500.000”, “indeniza”.
  - Conteúdo relacionado: nenhum.
  - Observação: o número “Cláusula 10” foi reaproveitado para Proteção de Dados (ver ACH-011).
- **Citação verificada:** Sim (DOC-A)

**Ponto exato da diferença.** A obrigação inteira foi removida: a apólice de responsabilidade civil profissional, com cobertura mínima de R$ 500.000,00, durante a vigência.

**Análise.** Remoção completa e sem cláusula substituta. Pela premissa de versões, a obrigação deixa de existir. Se o DOC-B fosse um aditivo, ela poderia continuar valendo (ver seção 2).

**Impacto / risco.** A CONTRATANTE perde a garantia financeira contra danos causados pela CONTRATADA na execução, por exemplo falhas no sistema de gestão de frota.

**Recomendação.** Confirmar se a remoção foi intencional. Se não foi, reinserir. Avaliar com a área de riscos o valor de cobertura adequado.

**Verificado (revisor):** ☐

#### ACH-006: Cl. 12.1 do DOC-B integra o “Anexo IV”, que não existe

- **Tipo:** REF / ALTERADO
- **Severidade:** Alta
- **Confiança:** Alta
- **Tópico:** Disposições gerais / anexos
- **Padrão:** A ≠ B

**Evidências**

- DOC-A, cl. 12.1 (p. 6): “12.1 Integram este contrato o Anexo I (Descrição dos Serviços) e o Anexo II (Matriz de Severidade).”
- DOC-B, cl. 12.1 (par. 38): “12.1 Integram este contrato o Anexo I (Descrição dos Serviços) e o Anexo IV (Matriz de Severidade).”
- DOC-B, título do anexo existente (par. 45): “Anexo II – Matriz de Severidade”
- DOC-B, cl. 4.3 (par. 17): “[...] conforme a Matriz de Severidade do Anexo II.”
- **Citação verificada:** Sim (todas)

**Ponto exato da diferença**

| Elemento                       | DOC-A    | DOC-B        |
| ------------------------------ | -------- | ------------ |
| Anexo da Matriz citado na 12.1 | Anexo II | **Anexo IV** |
| Anexo da Matriz existente      | Anexo II | Anexo II     |

**Análise.** O DOC-B não tem Anexo III nem IV. Busquei “Anexo IV” e só a própria cl. 12.1 aparece. Dentro do DOC-B, a cl. 4.3 cita o Anexo II e a 12.1 cita o IV para o mesmo conteúdo. É provável que seja erro de digitação, mas isso é interpretação.

**Impacto / risco.** A 12.1 é a cláusula que incorpora os anexos ao contrato. Com a referência quebrada, pode-se questionar se a Matriz de Severidade (Anexo II) integra a v2.0. Ela é a única fonte do prazo de severidade média (2 dias úteis).

**Recomendação.** Corrigir a 12.1 para “Anexo II” ou, se existir um Anexo IV, anexá-lo.

**Verificado (revisor):** ☐

#### ACH-007: Termo “CLIENTE”, não definido, substitui “CONTRATANTE” na Cláusula 6

- **Tipo:** TER / ALTERADO
- **Severidade:** Média
- **Confiança:** Alta
- **Tópico:** Obrigações da CONTRATANTE / definições
- **Padrão:** A ≠ B

**Evidências**

- DOC-A, título da Cl. 6 (p. 4): “Cláusula 6 – Das Obrigações da CONTRATANTE”
- DOC-A, cl. 6.1 (p. 4): “6.1 A CONTRATANTE deverá fornecer à CONTRATADA acesso remoto ao ambiente do sistema, nos termos da política de segurança da informação da CONTRATANTE.”
- DOC-A, cl. 6.2 (p. 4): “6.2 A CONTRATANTE deverá designar um gestor do contrato, responsável por acompanhar a execução dos serviços.”
- DOC-B, título da Cl. 6 (par. 21): “Cláusula 6 – Das Obrigações do CLIENTE”
- DOC-B, cl. 6.1 (par. 22): “6.1 O CLIENTE deverá fornecer à CONTRATADA acesso remoto ao ambiente do sistema, nos termos da política de segurança da informação do CLIENTE.”
- DOC-B, cl. 6.2 (par. 23): “6.2 O CLIENTE deverá designar um gestor do contrato, responsável por acompanhar a execução dos serviços.”
- DOC-B, cl. 1.1 (par. 9): “[...] BETA LOGÍSTICA S.A., doravante denominada CONTRATANTE [...]”
- **Citação verificada:** Sim (todas)

**Ponto exato da diferença**

| Elemento                        | DOC-A                          | DOC-B                  |
| ------------------------------- | ------------------------------ | ---------------------- |
| Sujeito das obrigações da Cl. 6 | CONTRATANTE (definido na 1.1)  | CLIENTE (não definido) |
| Conteúdo das obrigações         | acesso remoto; designar gestor | idêntico               |

**Análise.** “CLIENTE” aparece só nos par. 21 a 23 do DOC-B e não é definido. A cl. 1.1 define apenas CONTRATANTE e CONTRATADA, e “CONTRATANTE” continua sendo usado nas cl. 7.1, 9.2 e 11.1. Tudo indica que se trata da mesma parte, mas o texto não diz isso.

**Impacto / risco.** As obrigações da Cl. 6 ficam atribuídas a uma parte não definida no contrato. É risco de disputa se a CONTRATANTE descumprir, por exemplo, o fornecimento de acesso remoto.

**Recomendação.** Voltar para “CONTRATANTE” ou definir “CLIENTE” na cl. 1.1.

**Verificado (revisor):** ☐

#### ACH-008: Rescisão pela CONTRATANTE passa a depender de aprovação da Diretoria Jurídica

- **Tipo:** DIV / INCLUÍDO
- **Severidade:** Média
- **Confiança:** Alta
- **Tópico:** Rescisão
- **Padrão:** A ≠ B

**Evidências**

- DOC-A, cl. 9.1 (p. 5): “9.1 Qualquer das partes poderá rescindir este contrato mediante notificação por escrito, com antecedência mínima de 30 (trinta) dias.”
- DOC-B, cl. 9.1 (par. 31): “9.1 Qualquer das partes poderá rescindir este contrato mediante notificação por escrito, com antecedência mínima de 30 (trinta) dias.”
- DOC-B, cl. 9.2 (par. 32): “9.2 A rescisão por iniciativa da CONTRATANTE dependerá de prévia aprovação de sua Diretoria Jurídica.”
- DOC-A, condição de aprovação: **NÃO PRESENTE.**
  - Seções verificadas: Cl. 9 inteira e as demais cláusulas.
  - Termos buscados: “Diretoria”, “Jurídic”, “aprovação”.
  - Conteúdo relacionado: só a cl. 9.1 (equivalente).
- **Citação verificada:** Sim (todas)

**Ponto exato da diferença**

| Elemento                                | DOC-A                         | DOC-B                                                        |
| --------------------------------------- | ----------------------------- | ------------------------------------------------------------ |
| Requisitos para a CONTRATANTE rescindir | notificação escrita + 30 dias | notificação escrita + 30 dias **+ aprovação prévia da Diretoria Jurídica** |
| Requisitos para a CONTRATADA            | notificação + 30 dias         | idêntico                                                     |

**Análise.** O texto da 9.1 é igual nos dois documentos. A diferença vem da 9.2 nova, que acrescenta uma condição só para uma das partes. Por isso é DIV e não EXC: o efeito da 9.1 muda. A condição é de governança interna da CONTRATANTE, mas foi escrita no contrato bilateral.

**Impacto / risco.** A CONTRATADA poderia contestar uma notificação de rescisão sem prova da aprovação. Na prática, a cláusula cria uma assimetria contra a própria CONTRATANTE. Os documentos não permitem concluir sobre o efeito jurídico disso, que precisa ser avaliado por um especialista.

**Recomendação.** Avaliar com o jurídico se a condição deve ficar no contrato ou só em política interna.

**Verificado (revisor):** ☐

#### ACH-009: Relação entre v1.0 e v2.0 e início da vigência não definidos

- **Tipo:** NCL
- **Severidade:** Média
- **Confiança:** Média (a classificação depende de leitura jurídica)
- **Tópico:** Vigência / relação entre versões
- **Padrão:** A = B (cl. 3.1 idêntica), com datas diferentes

**Evidências**

- DOC-A, cl. 3.1 (p. 2): “3.1 O presente contrato vigorará pelo prazo de 12 (doze) meses, contados da data de sua assinatura, podendo ser prorrogado mediante termo aditivo.”
- DOC-B, cl. 3.1 (par. 13): texto idêntico ao do DOC-A.
- DOC-A, capa (p. 1): “Data: 10 de março de 2026”; DOC-A, fecho (p. 6): “São Paulo, 10 de março de 2026.”
- DOC-B, capa (par. 4): “Data: 2 de setembro de 2026”; DOC-B, fecho (par. 40): “São Paulo, 2 de setembro de 2026.”
- DOC-B, cláusula que substitua ou revogue a v1.0: **NÃO PRESENTE.**
  - Termos buscados: “substitui”, “revoga”, “versão 1”, “aditivo”.
  - O único resultado é “termo aditivo”, na própria 3.1.
- **Citação verificada:** Sim (todas)

**Ponto exato da diferença.** O marco de vigência “data de sua assinatura” leva a 10/03/2026 em uma versão e a 02/09/2026 na outra. O DOC-B não diz se substitui o DOC-A.

**Análise: duas leituras incompatíveis**

- (a) A v2.0 consolida a v1.0. A vigência conta da assinatura original e termina por volta de março/2027.
- (b) A v2.0 é um instrumento novo. A vigência recomeça e termina por volta de setembro/2027. Nesse caso haveria dois instrumentos com o mesmo número.

A própria 3.1 prevê que a prorrogação se faça por “termo aditivo”, e a v2.0 não se apresenta como aditivo.

**Impacto / risco.** Incerteza sobre o fim do contrato, a data-base do reajuste anual pelo IPCA (cl. 7.3) e qual versão regeu os fatos ocorridos entre março e setembro de 2026.

**Recomendação.** Incluir na v2.0 uma cláusula que declare a substituição da v1.0, a data de efeito das alterações e o marco de vigência.

**Verificado (revisor):** ☐

#### ACH-010: Início do atendimento crítico em “4 horas corridas” × suporte só em dias úteis das 8h às 18h

- **Tipo:** NCL
- **Severidade:** Média
- **Confiança:** Média
- **Tópico:** Prazos de atendimento / escopo do serviço
- **Padrão:** A = B (a mesma ambiguidade existe nas duas versões)

**Evidências**

- DOC-A, cl. 4.1 (p. 3): “4.1 A CONTRATADA deverá iniciar o atendimento de chamados de severidade crítica em até 4 (quatro) horas corridas, contadas da abertura do chamado.”
- DOC-A, Anexo I (p. 7): “Suporte técnico remoto em dias úteis, das 8h às 18h; [...]”
- DOC-B, cl. 4.1 (par. 15) e Anexo I (par. 44): textos idênticos aos do DOC-A.
- **Citação verificada:** Sim (todas)

**Ponto exato da ambiguidade**

| Elemento         | Leitura 1                         | Leitura 2                                       |
| ---------------- | --------------------------------- | ----------------------------------------------- |
| Contagem das 4 h | corridas 24×7 (cl. 4.1 prevalece) | só dentro da janela de suporte (Anexo I limita) |

**Análise.** Não é diferença entre versões, e sim uma ambiguidade interna presente nas duas. Exemplo: um chamado crítico aberto numa sexta às 19h. Pela leitura 1 o atendimento começa até as 23h. Pela leitura 2, só na segunda às 8h.

**Impacto / risco.** Disputa sobre cumprimento de prazo. Na v1.0, isso afetava diretamente a multa da cl. 8.1.

**Recomendação.** Explicitar se a severidade crítica tem atendimento 24×7 ou se a contagem respeita a janela do Anexo I.

**Verificado (revisor):** ☐

#### ACH-011: Reestruturação e renumeração das Cláusulas 5, 10 e 11

- **Tipo:** EQV-L / ALTERADO (só a localização)
- **Severidade:** Baixa
- **Confiança:** Alta
- **Tópico:** Estrutura do contrato
- **Padrão:** conteúdo A = B, numeração A ≠ B

**Evidências**

- DOC-A, cl. 5.3 (p. 3): “5.3 A CONTRATADA deverá manter sigilo sobre todas as informações da CONTRATANTE a que tiver acesso em razão deste contrato, durante a vigência e por 5 (cinco) anos após o seu término.”
- DOC-B, título “Cláusula 11 – Da Confidencialidade” (par. 35) e cl. 11.1 (par. 36): “11.1 A CONTRATADA deverá manter sigilo sobre todas as informações da CONTRATANTE a que tiver acesso em razão deste contrato, durante a vigência e por 5 (cinco) anos após o seu término.”
- DOC-A, título “Cláusula 11 – Da Proteção de Dados Pessoais” (p. 5); DOC-B, título “Cláusula 10 – Da Proteção de Dados Pessoais” (par. 33)
- DOC-A, título “Cláusula 10 – Do Seguro” (p. 5)
- **Citação verificada:** Sim (todas)

**Ponto exato da diferença**

| Conteúdo          | DOC-A   | DOC-B                       |
| ----------------- | ------- | --------------------------- |
| Sigilo            | cl. 5.3 | cl. 11.1 (cláusula própria) |
| Proteção de dados | Cl. 11  | Cl. 10                      |
| Seguro            | Cl. 10  | removido (ACH-005)          |

**Análise.** O texto do sigilo e o da proteção de dados são idênticos. Mudou só a posição.

**Impacto / risco.** Documentos externos que citem “Cláusula 10” ou “Cláusula 11” pelo número da v1.0 passam a apontar para outro conteúdo.

**Recomendação.** Revisar referências externas, como pedidos, chamados e aditivos, que usem a numeração antiga.

**Verificado (revisor):** ☐

#### ACH-012: Versão e datas do instrumento

- **Tipo:** DIV / ALTERADO
- **Severidade:** Informativa
- **Confiança:** Alta
- **Tópico:** Identificação
- **Padrão:** A ≠ B

**Evidências**

- DOC-A (p. 1): “Versão 1.0” e “Data: 10 de março de 2026”
- DOC-B (par. 3 e par. 4): “Versão 2.0” e “Data: 2 de setembro de 2026”
- **Citação verificada:** Sim

**Análise.** É a mudança esperada entre versões. Cada documento é coerente consigo mesmo: a data da capa é igual à do fecho, e as citações dos fechos estão no ACH-009. Este achado sustenta a premissa da seção 2.

**Verificado (revisor):** ☐

#### ACH-013: Metadados dos arquivos não refletem as datas dos documentos

- **Tipo:** INT (metadados do arquivo, não é texto contratual)
- **Severidade:** Informativa
- **Confiança:** Alta
- **Tópico:** Metadados
- **Padrão:** n/a

**Evidências** (propriedades dos arquivos, não conteúdo do documento)

- DOC-A, propriedades do PDF: Title “Contrato 041/2026 v1.0 (fictício)”; CreationDate “Wed Oct 14 19:49:27 2026”.
- DOC-B, docProps/core.xml: title “Contrato 041/2026 v2.0 (fictício)”; created/modified “2013-12-23T23:15:00Z”; creator “python-docx”.

**Análise.** O DOC-B mostra datas de 2013, herdadas do modelo, e o DOC-A foi gerado depois da data que declara. Os metadados não servem para confirmar a cronologia. A ordem das versões se apoia só no texto (“Versão 1.0/2.0”).

**Recomendação.** Nenhuma ação contratual. Registro apenas para a trilha de auditoria.

**Verificado (revisor):** ☐

### 5. Itens convergentes

- **Título, número e partes** (EQV-L): DOC-A p. 1 e DOC-B par. 1, 2, 5 e 6, com “CONTRATO DE PRESTAÇÃO DE SERVIÇOS DE SUPORTE TÉCNICO E MANUTENÇÃO DE SOFTWARE”, “Contrato nº 041/2026”, “CONTRATANTE: Beta Logística S.A.” e “CONTRATADA: Alfa Sistemas Ltda.”
- **Nota de documento fictício** (EQV-L): DOC-A p. 1 · DOC-B par. 7, “Documento fictício, elaborado exclusivamente para testes.”
- **Partes / definições** (EQV-L): DOC-A cl. 1.1 (p. 2) · DOC-B cl. 1.1 (par. 9), “doravante denominada CONTRATANTE, e ALFA SISTEMAS LTDA., doravante denominada CONTRATADA”
- **Objeto** (EQV-L): DOC-A cl. 2.1 (p. 2) · DOC-B cl. 2.1 (par. 11), “manutenção corretiva e evolutiva do sistema de gestão de frota”
- **Vigência, texto** (EQV-L, mas ver ACH-009): DOC-A cl. 3.1 (p. 2) · DOC-B cl. 3.1 (par. 13), “vigorará pelo prazo de 12 (doze) meses”
- **Início do atendimento crítico** (EQV-L, mas ver ACH-010): DOC-A cl. 4.1 (p. 3) · DOC-B cl. 4.1 (par. 15), “em até 4 (quatro) horas corridas”
- **Prazo baixa, texto da cláusula** (EQV-L, mas ver ACH-002): DOC-A cl. 4.3 (p. 3) · DOC-B cl. 4.3 (par. 17), “em até 5 (cinco) dias úteis”
- **Equipe certificada** (EQV-L): DOC-A cl. 5.1 (p. 3) · DOC-B cl. 5.1 (par. 19), “manter equipe técnica com certificação”
- **Sigilo** (EQV-L, realocado, ver ACH-011): DOC-A cl. 5.3 (p. 3) · DOC-B cl. 11.1 (par. 36), “por 5 (cinco) anos após o seu término”
- **Obrigações de acesso remoto e gestor, conteúdo** (EQV-L, exceto o sujeito, ver ACH-007): DOC-A cl. 6.1 e 6.2 (p. 4) · DOC-B cl. 6.1 e 6.2 (par. 22 e 23), “designar um gestor do contrato”
- **Valor mensal** (EQV-L): DOC-A cl. 7.1 (p. 4) · DOC-B cl. 7.1 (par. 25), “R$ 18.500,00 (dezoito mil e quinhentos reais)”
- **Prazo de pagamento** (EQV-S): DOC-A cl. 7.2 (p. 4), “será efetuado em até 30 (trinta) dias após o recebimento da nota fiscal” · DOC-B cl. 7.2 (par. 26), “ocorrerá no prazo máximo de trinta dias, contado do recebimento da nota fiscal”. Mesmo prazo, mesmo marco e mesmo limite máximo.
- **Reajuste** (EQV-L): DOC-A cl. 7.3 (p. 4) · DOC-B cl. 7.3 (par. 27), “reajustado anualmente pela variação do IPCA”
- **Rescisão imotivada, regra geral** (EQV-L, mas ver ACH-008): DOC-A cl. 9.1 (p. 5) · DOC-B cl. 9.1 (par. 31), “com antecedência mínima de 30 (trinta) dias”
- **Proteção de dados** (EQV-L, renumerado): DOC-A cl. 11.1 (p. 5) · DOC-B cl. 10.1 (par. 34), “observada a Lei nº 13.709/2018”
- **Foro** (EQV-L): DOC-A cl. 12.2 (p. 6) · DOC-B cl. 12.2 (par. 39), “foro da Comarca de São Paulo/SP”
- **Assinaturas** (EQV-L): DOC-A p. 6 · DOC-B par. 41 e 42, “BETA LOGÍSTICA S.A. (CONTRATANTE)” e “ALFA SISTEMAS LTDA. (CONTRATADA)”
- **Anexo I, descrição dos serviços** (EQV-L): DOC-A p. 7 · DOC-B par. 44, “manutenção evolutiva limitada a 40 (quarenta) horas mensais”
- **Anexo II, linha Crítica** (EQV-L): DOC-A p. 7 · DOC-B Tabela 1, linha 2, “Início em até 4 horas corridas”
- **Anexo II, linha Média** (EQV-L): DOC-A p. 7 · DOC-B Tabela 1, linha 3, “Até 2 dias úteis”

### 6. Declaração de cobertura e limitações

**Cobertura**

- **DOC-A:** 7 de 7 páginas físicas analisadas, inclusive capa, assinaturas, anexos e tabela. Nenhuma página com OCR e nada ilegível.
- **DOC-B:** 45 de 45 parágrafos e a tabela inteira analisados. Não há alterações controladas, comentários nem conteúdo em cabeçalho ou rodapé. A miniatura embutida no .docx não é conteúdo e não foi analisada.
- **Reconciliação:** todo o conteúdo dos dois documentos está em um achado (ACH-001 a 013) ou nos itens convergentes. Nada ficou de fora.

**Verificação das citações**

- 80 citações conferidas, ou seja, **100%**, acima da cobertura mínima exigida.
- 0 corrigidas, 0 divergentes, 0 indisponíveis.
- A conferência foi automatizada: cada citação foi procurada no texto extraído da página ou parágrafo indicado. Normalizei só as quebras de linha do PDF; letras, números e pontuação não foram alterados.

**Limitações**

- A premissa de versões tem confiança Média (ver ACH-009).
- A validade jurídica das cl. 8.1 e 9.2 do DOC-B não foi avaliada e exige um especialista.

**Observações não comparativas** (comuns às duas versões; não são achados)

- **Severidade média fora da Cl. 4:** a Cl. 4 não trata dela. O prazo de 2 dias úteis existe só no Anexo II, e a multa da cl. 8.1 da v1.0 se refere apenas aos “prazos previstos na Cláusula 4”.
- **Prazo de correção só para crítica:** não há prazo de *conclusão* para severidade média ou baixa.
- **Pagamento sem tipo de contagem:** a cl. 7.2 não diz se os 30 dias são corridos ou úteis.

### 7. Questões em aberto

1. **Q1:** Qual é o prazo de correção de falhas críticas: 30 ou 45 dias corridos? A ampliação foi negociada? (ACH-001)
2. **Q2:** Qual é o prazo da severidade baixa: 5 ou 10 dias úteis? Nesse caso, prevalece a cláusula ou o anexo? (ACH-002)
3. **Q3:** O relatório mensal deixou de ser obrigatório de propósito? (ACH-003)
4. **Q4:** Quais são as “medidas cabíveis”? A multa de 2% por ocorrência deve voltar? (ACH-004)
5. **Q5:** A exclusão do seguro de R$ 500.000,00 foi intencional? (ACH-005)
6. **Q6:** “Anexo IV” é erro de digitação ou falta um anexo? (ACH-006)
7. **Q7:** “CLIENTE” é a CONTRATANTE? Corrigir ou definir o termo. (ACH-007)
8. **Q8:** A aprovação da Diretoria Jurídica deve ficar no contrato bilateral? (ACH-008)
9. **Q9:** A v2.0 substitui a v1.0? A partir de quando, e de quando conta a vigência? (ACH-009, ACH-012)
10. **Q10:** O início em 4 h corridas vale 24×7 ou só na janela de suporte? (ACH-010)
11. **Q11:** Há referências externas à numeração antiga das Cláusulas 5.3, 10 e 11? (ACH-011)

Os achados são indícios até um revisor conferi-los nos originais. O campo “Verificado” ficou em branco de propósito.

Se quiser, exporto a matriz de achados para planilha, no formato da seção 8, com a coluna “Verificado” em branco para o revisor.