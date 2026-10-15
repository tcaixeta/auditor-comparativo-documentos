# Análise comparativa — Contrato nº 041/2026, v1.0 (DOC-A) × v2.0 (DOC-B)

> Os achados abaixo são indícios organizados para revisão. Só devem embasar decisões depois de conferidos por um revisor no documento original (campo **Verificado**).

## 1. Identificação e escopo

| ID | Arquivo | Título | Versão | Data | Emissor / partes | Páginas | Esquema de localização | Integridade |
|---|---|---|---|---|---|---|---|---|
| DOC-A | DOC-A_contrato_v1.pdf | Contrato de Prestação de Serviços de Suporte Técnico e Manutenção de Software, nº 041/2026 | 1.0 | 10/03/2026 | CONTRATANTE: Beta Logística S.A.; CONTRATADA: Alfa Sistemas Ltda. | 7 físicas (capa sem número; rodapé impresso "Página 1 de 6" começa na página física 2) | Cláusula + **página física** (`cl. 4.2 (p. 3)`). Página física = numeração impressa + 1. Tabela: `p. 7, Tabela 1, linha L, col. C` | Texto nativo nas 7 páginas, extraído página a página; sem OCR; 1 tabela (p. 7) extraída separadamente. Nada ilegível. |
| DOC-B | DOC-B_contrato_v2.docx | Idem, nº 041/2026 | 2.0 | 02/09/2026 | Mesmas partes | n/a (.docx) | Cláusula + **parágrafo** (`cl. 4.2 (par. 16)`). Contagem: parágrafos do corpo em sequência, a partir de 1, incluindo títulos; não há parágrafos vazios; total 45. Tabela após o par. 45: `Tabela 1, linha L, col. C` | Sem alterações controladas, sem comentários, cabeçalho e rodapé vazios. Metadados do arquivo incompatíveis com o conteúdo (ver Observações). |

## 2. Relação entre os documentos e premissas

**Relação identificada: versões** (v1.0 → v2.0 do mesmo contrato). Base: mesmo número de contrato, mesmo título, mesmas partes, campo "Versão" (DOC-A p. 1: "Versão 1.0"; DOC-B par. 3: "Versão 2.0") e datas sequenciais (março → setembro de 2026).

- **Efeito na classificação:** as diferenças recebem os rótulos INCLUÍDO, REMOVIDO ou ALTERADO, no sentido DOC-A → DOC-B. Nenhum documento é tratado como o correto; a análise mostra o que mudou e o efeito da mudança.
- **Premissa P1:** DOC-B pretende substituir integralmente DOC-A. Nenhum dos dois documentos declara isso nem traz regra de precedência. *Se P1 estiver errada* (DOC-B como aditivo ou instrumento complementar), seria preciso uma regra de precedência que hoje não existe, e cada achado viraria um conflito sem critério de solução no próprio texto.
- **Premissa P2:** DOC-B é um instrumento assinado em 02/09/2026 (conforme seu bloco de assinatura). *Se DOC-B for apenas minuta ou consolidação*, o ACH-010 (data) perde relevância prática.

## 3. Resumo quantitativo

| Tipo | Qtd. | | Severidade | Qtd. |
|---|---|---|---|---|
| CTR | 4 | | Crítica | 0 |
| NCL | 1 | | Alta | 6 |
| EXC | 1 | | Média | 4 |
| INT | 1 | | Baixa | 0 |
| REF | 1 | | Informativa | 0 |
| TER | 1 | | **Total de achados** | **10** |
| DIV | 1 | | Itens convergentes | 27 |

**Carga de revisão humana:** 1 item em NÃO CLARO (ACH-005), 0 em REQUER REVISÃO; os 10 achados aguardam o campo Verificado.

**Leitura geral:** a v2.0 mantém a estrutura e a maior parte do texto, mas as mudanças se concentram no regime de nível de serviço e em sua exigibilidade: o prazo de correção de falhas críticas aumentou, o prazo da severidade baixa dobrou no Anexo II (e passou a contradizer a cl. 4.3 da própria v2.0), o relatório mensal deixou de ser obrigatório, a multa objetiva foi trocada por uma redação vaga e a exigência de seguro foi suprimida. Todas as mudanças afrouxam obrigações da CONTRATADA ou garantias da CONTRATANTE. A v2.0 também introduz defeitos que a v1.0 não tinha (referência a anexo inexistente e termo "CLIENTE" sem definição).

## 4. Achados detalhados

### ACH-001 — Prazo de correção de falhas críticas ampliado de 30 para 45 dias

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
| Prazo de conclusão | 30 dias | 45 dias |
| Tipo de contagem | corridos | corridos (igual) |
| Marco inicial | abertura do chamado | abertura do chamado (igual) |

**Análise**
Mesmo item, mesma obrigação, valor diferente: os dois prazos não podem valer ao mesmo tempo (regra de desempate: valor alterado = CTR). O restante da frase é idêntico, o que isola a mudança no número. É um aumento de 50% no prazo máximo para uma falha classificada no Anexo II como sistema indisponível.

**Impacto / risco**
Para a CONTRATANTE, a janela tolerada de indisponibilidade sem descumprimento cresce 15 dias. Somado ao ACH-005, o descumprimento também deixa de ter sanção objetiva.

**Recomendação**
Confirmar com os responsáveis se a ampliação foi negociada e, se sim, registrar a justificativa; caso contrário, restabelecer 30 dias.

**Verificado (revisor):** ☐

---

### ACH-002 — Prazo da severidade baixa no Anexo II alterado de 5 para 10 dias úteis

- **Tipo:** CTR / ALTERADO
- **Severidade:** Alta
- **Confiança:** Alta
- **Tópico:** Prazos de atendimento (Anexo II – Matriz de Severidade)
- **Padrão entre documentos:** A ≠ B

**Evidências**
- DOC-A, Anexo II (p. 7, Tabela 1, linha 4, col. 3): "Até 5 dias úteis"
- DOC-B, Anexo II (Tabela 1, linha 4, col. 3): "Até 10 dias úteis"
- Linha correspondente nos dois (col. 1 e col. 2): "Baixa" / "Dúvida ou falha sem impacto operacional"
- **Citação verificada:** Sim (DOC-A e DOC-B)

**Ponto exato da diferença**
| Elemento | DOC-A | DOC-B |
|---|---|---|
| Prazo de atendimento, severidade baixa | 5 dias úteis | 10 dias úteis |

**Análise**
Mesmo item da matriz (mesma severidade, mesma descrição), valor dobrado → CTR. As linhas "Crítica" e "Média" ficaram inalteradas (ver Itens convergentes). A mudança no anexo não foi acompanhada na cl. 4.3 da v2.0, o que gera a contradição interna registrada separadamente no ACH-003.

**Impacto / risco**
Dobra o prazo tolerado para chamados de baixa severidade e cria dúvida sobre qual prazo vale na v2.0.

**Recomendação**
Decidir o prazo pretendido e alinhar anexo e cláusula 4.3 no mesmo sentido.

**Verificado (revisor):** ☐

---

### ACH-003 — DOC-B: cláusula 4.3 e Anexo II fixam prazos diferentes para a severidade baixa

- **Tipo:** INT
- **Severidade:** Alta
- **Confiança:** Alta
- **Tópico:** Prazos de atendimento
- **Padrão entre documentos:** defeito só em DOC-B (em DOC-A, cl. 4.3 e Anexo II coincidem em 5 dias úteis)

**Evidências**
- DOC-B, cl. 4.3 (par. 17): "4.3 Os chamados de severidade baixa serão atendidos em até 5 (cinco) dias úteis, conforme a Matriz de Severidade do Anexo II."
- DOC-B, Anexo II (Tabela 1, linha 4, col. 3): "Até 10 dias úteis"
- **Citação verificada:** Sim

**Ponto exato da diferença**
| Elemento | DOC-B cl. 4.3 | DOC-B Anexo II |
|---|---|---|
| Prazo, severidade baixa | 5 dias úteis | 10 dias úteis |

**Análise**
A cláusula declara que seu prazo segue a matriz do Anexo II, mas a matriz diz outra coisa. As duas regras não podem valer para o mesmo chamado. O texto não traz regra de prevalência entre corpo e anexos. É um defeito novo da v2.0, consequência provável de a alteração do ACH-002 ter sido feita só no anexo (inferência, não declarada nos documentos). Ver também ACH-007: a cláusula de integração da v2.0 nem sequer cita o Anexo II.

**Impacto / risco**
Disputa sobre o prazo aplicável e sobre se houve descumprimento.

**Recomendação**
Corrigir uma das duas fontes para o prazo decidido no ACH-002.

**Verificado (revisor):** ☐

---

### ACH-004 — Relatório mensal de desempenho passou de obrigatório a facultativo

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
| Prazo | 5º dia útil | 5º dia útil (igual) |

**Análise**
Única palavra alterada, mas muda o status normativo do item (regra de desempate: modalidade = CTR). Na v2.0 o prazo continua escrito, o que fica sem efeito prático: um prazo não obriga quando a própria emissão é facultativa. O relatório é a fonte natural para a CONTRATANTE aferir os prazos da Cláusula 4.

**Impacto / risco**
A CONTRATANTE perde o instrumento contratual de acompanhamento do nível de serviço, o que dificulta provar descumprimentos (ACH-001 a ACH-003).

**Recomendação**
Confirmar se a mudança foi intencional; se não, restabelecer "deverá".

**Verificado (revisor):** ☐

---

### ACH-005 — Multa objetiva de 2% substituída por "medidas cabíveis"

- **Tipo:** NCL / ALTERADO
- **Severidade:** Alta
- **Confiança:** Alta (quanto à classificação)
- **Tópico:** Penalidades
- **Padrão entre documentos:** A ≠ B

**Evidências**
- DOC-A, cl. 8.1 (p. 4): "8.1 O descumprimento dos prazos previstos na Cláusula 4 sujeitará a CONTRATADA a multa de 2% (dois por cento) sobre o valor mensal, por ocorrência."
- DOC-B, cl. 8.1 (par. 29): **NÃO CLARO.** "8.1 O descumprimento dos prazos previstos na Cláusula 4 poderá ensejar a aplicação das medidas cabíveis." Trata das consequências do descumprimento, mas não define multa, percentual, base de cálculo nem forma de aplicação.
- Busca em DOC-B pelos termos multa, %, por cento, sanção: nenhuma ocorrência; penalidade só aparece no título da Cláusula 8 (par. 28): "Cláusula 8 – Das Penalidades"
- **Citação verificada:** Sim (DOC-A e DOC-B)

**Ponto exato da diferença**
| Elemento | DOC-A | DOC-B |
|---|---|---|
| Consequência | multa | medidas cabíveis (não definidas) |
| Valor | 2% | não definido |
| Base de cálculo | valor mensal | não definida |
| Incidência | por ocorrência | não definida |
| Modalidade | sujeitará (automática) | poderá ensejar (eventual) |
| Gatilho | descumprimento dos prazos da Cláusula 4 | igual |

**Análise**
O tema continua presente, mas o conteúdo objetivo foi trocado por redação vaga (regra de desempate → NCL, não EXC). Não é possível dizer, só pelo texto, quais medidas a v2.0 admite. A exigibilidade efetiva de uma medida cabível sem previsão contratual é questão jurídica fora do alcance desta análise e exige avaliação de especialista.

**Impacto / risco**
O nível de serviço da Cláusula 4 fica sem sanção quantificada. Com o ACH-001 e o ACH-004, forma um conjunto de mudanças que reduz bastante a proteção da CONTRATANTE.

**Recomendação**
Esclarecer com os responsáveis quais medidas se pretendia prever; se a multa foi retirada de propósito, registrar a decisão; caso contrário, restabelecer o percentual, a base e a incidência. Submeter a redação final ao jurídico.

**Verificado (revisor):** ☐

---

### ACH-006 — Cláusula de seguro de responsabilidade civil profissional suprimida

- **Tipo:** EXC / REMOVIDO
- **Severidade:** Alta
- **Confiança:** Alta
- **Tópico:** Seguro / garantias
- **Padrão entre documentos:** A ≠ B (presente só em DOC-A)

**Evidências**
- DOC-A, cl. 10 (p. 5): "Cláusula 10 – Do Seguro"
- DOC-A, cl. 10.1 (p. 5): "10.1 A CONTRATADA manterá, durante toda a vigência deste contrato, apólice de seguro de responsabilidade civil profissional com cobertura mínima de R$ 500.000,00 (quinhentos mil reais)."
- DOC-B: **NÃO PRESENTE.** Seções verificadas: documento inteiro, com atenção às Cláusulas 5 (Obrigações da CONTRATADA, par. 18–20), 8 (Penalidades, par. 28–29), 10 e 11 (par. 33–36, onde o tema estava na numeração da v1.0), 12 (par. 37–39) e Anexos I e II. Termos buscados: seguro, apólice, responsabilidade civil, cobertura, 500.000, indeniza (radical). Conteúdo relacionado: nenhum. A numeração da v2.0 avança direto da Cláusula 9 para a Cláusula 10 (Proteção de Dados Pessoais).
- **Citação verificada:** Sim (DOC-A); ausência confirmada por busca textual em DOC-B

**Ponto exato da diferença**
| Elemento | DOC-A | DOC-B |
|---|---|---|
| Obrigação de manter seguro | sim | ausente |
| Tipo de apólice | responsabilidade civil profissional | — |
| Cobertura mínima | R$ 500.000,00 | — |
| Período | toda a vigência | — |

**Análise**
O tema inteiro desapareceu, sem nada equivalente ou parcial em outra cláusula → EXC / REMOVIDO. As cláusulas seguintes foram renumeradas (ver Itens convergentes).

**Impacto / risco**
A CONTRATANTE perde a garantia financeira para danos causados pela CONTRATADA na execução dos serviços.

**Recomendação**
Confirmar se a supressão foi intencional; se não, reincluir a cláusula.

**Verificado (revisor):** ☐

---

### ACH-007 — DOC-B: cláusula de integração cita "Anexo IV", que não existe

- **Tipo:** REF / ALTERADO
- **Severidade:** Média
- **Confiança:** Alta
- **Tópico:** Disposições gerais / anexos
- **Padrão entre documentos:** A ≠ B (defeito só em DOC-B)

**Evidências**
- DOC-A, cl. 12.1 (p. 6): "12.1 Integram este contrato o Anexo I (Descrição dos Serviços) e o Anexo II (Matriz de Severidade)."
- DOC-B, cl. 12.1 (par. 38): "12.1 Integram este contrato o Anexo I (Descrição dos Serviços) e o Anexo IV (Matriz de Severidade)."
- DOC-B, título do anexo (par. 45): "Anexo II – Matriz de Severidade"
- DOC-B, cl. 4.3 (par. 17), que cita o mesmo anexo pelo número correto: "conforme a Matriz de Severidade do Anexo II."
- Busca em DOC-B: os únicos títulos de anexo são o par. 43 (Anexo I) e o par. 45 (Anexo II); não há Anexo III nem Anexo IV.
- **Citação verificada:** Sim

**Ponto exato da diferença**
| Elemento | DOC-A | DOC-B |
|---|---|---|
| Anexo integrado com a Matriz de Severidade | Anexo II (existe) | Anexo IV (não existe) |

**Análise**
O título entre parênteses identifica o conteúdo, então o mais provável é erro de numeração (inferência). Ainda assim, pelo texto, o Anexo II da v2.0 não está formalmente listado entre os documentos integrantes, e a própria v2.0 o cita com dois números diferentes.

**Impacto / risco**
Abre espaço para discutir se a Matriz de Severidade integra o contrato, o que afeta diretamente o ACH-002 e o ACH-003.

**Recomendação**
Corrigir a referência para "Anexo II" (ou juntar o Anexo IV, se ele de fato existir).

**Verificado (revisor):** ☐

---

### ACH-008 — Cláusula 6 de DOC-B troca "CONTRATANTE" por "CLIENTE", termo não definido

- **Tipo:** TER / ALTERADO
- **Severidade:** Média
- **Confiança:** Alta
- **Tópico:** Obrigações da CONTRATANTE / definições das partes
- **Padrão entre documentos:** A ≠ B

**Evidências**
- DOC-A, cl. 6 (p. 4): "Cláusula 6 – Das Obrigações da CONTRATANTE"
- DOC-A, cl. 6.1 (p. 4): "6.1 A CONTRATANTE deverá fornecer à CONTRATADA acesso remoto ao ambiente do sistema, nos termos da política de segurança da informação da CONTRATANTE."
- DOC-B, cl. 6 (par. 21): "Cláusula 6 – Das Obrigações do CLIENTE"
- DOC-B, cl. 6.1 (par. 22): "6.1 O CLIENTE deverá fornecer à CONTRATADA acesso remoto ao ambiente do sistema, nos termos da política de segurança da informação do CLIENTE."
- DOC-B, cl. 6.2 (par. 23): "6.2 O CLIENTE deverá designar um gestor do contrato, responsável por acompanhar a execução dos serviços."
- DOC-B, cl. 1.1 (par. 9), definição das partes: "1.1 BETA LOGÍSTICA S.A., doravante denominada CONTRATANTE, e ALFA SISTEMAS LTDA., doravante denominada CONTRATADA [...]"
- Busca: o termo CLIENTE ocorre 4 vezes em DOC-B, todas na Cláusula 6 (par. 21–23), e nenhuma em DOC-A. O restante de DOC-B continua usando "CONTRATANTE" (ex.: cl. 7.1, 9.2, 11.1).
- **Citação verificada:** Sim (DOC-A e DOC-B)

**Ponto exato da diferença**
| Elemento | DOC-A | DOC-B |
|---|---|---|
| Designação do obrigado na Cláusula 6 | CONTRATANTE (definido na cl. 1.1) | CLIENTE (não definido) |

**Análise**
Pelo contexto, CLIENTE designa a Beta Logística S.A. (inferência razoável), mas a v2.0 não define o termo e o usa só nessa cláusula. É uma inconsistência terminológica entre as versões e, ao mesmo tempo, interna à v2.0 (mesmo conceito com dois nomes). O conteúdo das obrigações 6.1 e 6.2 não mudou (ver Itens convergentes).

**Impacto / risco**
Margem para discutir quem responde pelas obrigações de fornecer acesso e de designar o gestor.

**Recomendação**
Substituir "CLIENTE" por "CONTRATANTE" na Cláusula 6.

**Verificado (revisor):** ☐

---

### ACH-009 — Rescisão pela CONTRATANTE passa a depender de aprovação da Diretoria Jurídica

- **Tipo:** DIV / INCLUÍDO
- **Severidade:** Média
- **Confiança:** Alta
- **Tópico:** Rescisão
- **Padrão entre documentos:** A ≠ B

**Evidências**
- DOC-A, cl. 9.1 (p. 5): "9.1 Qualquer das partes poderá rescindir este contrato mediante notificação por escrito, com antecedência mínima de 30 (trinta) dias."
- DOC-B, cl. 9.1 (par. 31): texto idêntico ao de DOC-A, cl. 9.1.
- DOC-B, cl. 9.2 (par. 32): "9.2 A rescisão por iniciativa da CONTRATANTE dependerá de prévia aprovação de sua Diretoria Jurídica."
- Busca em DOC-A pelos termos aprovação, Diretoria, Jurídica: nenhuma ocorrência.
- **Citação verificada:** Sim (DOC-A e DOC-B)

**Ponto exato da diferença**
| Elemento | DOC-A | DOC-B |
|---|---|---|
| Condição para rescisão pela CONTRATANTE | notificação escrita + 30 dias | notificação escrita + 30 dias **+ prévia aprovação da Diretoria Jurídica** |
| Condição para rescisão pela CONTRATADA | notificação escrita + 30 dias | igual |

**Análise**
O tema existe nos dois e a regra original permanece; a v2.0 acrescenta uma condição só para uma das partes → DIV / INCLUÍDO. A condição é de governança interna da CONTRATANTE posta no contrato. O texto não diz como a aprovação é comprovada à CONTRATADA nem o efeito de uma notificação feita sem ela (ambiguidade). A validade e os efeitos dessa condição perante terceiros são questão jurídica para especialista.

**Impacto / risco**
Uma notificação de rescisão da CONTRATANTE pode ser contestada pela falta de aprovação prévia.

**Recomendação**
Confirmar a intenção; se mantida, definir a forma de comprovação e a consequência da falta de aprovação, ou retirar a condição do contrato e tratá-la como norma interna.

**Verificado (revisor):** ☐

---

### ACH-010 — Data do instrumento alterada (marco da vigência)

- **Tipo:** CTR / ALTERADO
- **Severidade:** Média
- **Confiança:** Média
- **Tópico:** Identificação / vigência
- **Padrão entre documentos:** A ≠ B

**Evidências**
- DOC-A, capa (p. 1): "Data: 10 de março de 2026"
- DOC-A, local e data de assinatura (p. 6): "São Paulo, 10 de março de 2026."
- DOC-B, capa (par. 4): "Data: 2 de setembro de 2026"
- DOC-B, local e data de assinatura (par. 40): "São Paulo, 2 de setembro de 2026."
- Cláusula de vigência, idêntica nos dois (DOC-A cl. 3.1, p. 2; DOC-B cl. 3.1, par. 13): "3.1 O presente contrato vigorará pelo prazo de 12 (doze) meses, contados da data de sua assinatura, podendo ser prorrogado mediante termo aditivo."
- **Citação verificada:** Sim (DOC-A e DOC-B)

**Ponto exato da diferença**
| Elemento | DOC-A | DOC-B |
|---|---|---|
| Data do instrumento / assinatura | 10/03/2026 | 02/09/2026 |
| Fim da vigência derivado da cl. 3.1 (cálculo) | março de 2027 | setembro de 2027 |

**Análise**
A data mudar entre versões é esperado; o problema é que a cl. 3.1 conta a vigência "da data de sua assinatura". Sob a premissa P1/P2, a v2.0 reinicia a contagem e estende o fim da vigência em cerca de seis meses, sem termo aditivo, que é o instrumento previsto na própria cl. 3.1 para prorrogação. A confiança é Média porque depende de a v2.0 ser um instrumento efetivamente assinado que substitui a v1.0 (premissas declaradas na seção 2).

**Impacto / risco**
Incerteza sobre a data de término e sobre se houve prorrogação.

**Recomendação**
Esclarecer a natureza da v2.0 (novo contrato, substituição ou consolidação) e declarar expressamente a data de início da vigência.

**Verificado (revisor):** ☐

## 5. Itens convergentes

**Identificação**
- **Título** (EQV-L): DOC-A p. 1 · DOC-B par. 1: "CONTRATO DE PRESTAÇÃO DE SERVIÇOS DE SUPORTE TÉCNICO E" (texto idêntico; no PDF o título quebra em duas linhas)
- **Número do contrato** (EQV-L): DOC-A p. 1 · DOC-B par. 2: "Contrato nº 041/2026"
- **Partes na capa** (EQV-L): DOC-A p. 1 · DOC-B par. 5–6: "CONTRATANTE: Beta Logística S.A." / "CONTRATADA: Alfa Sistemas Ltda."
- **Nota de documento fictício** (EQV-L): DOC-A p. 1 · DOC-B par. 7: "Documento fictício, elaborado exclusivamente para testes."

**Cláusulas 1 a 3**
- **1.1 Partes e denominações** (EQV-L): DOC-A p. 2 · DOC-B par. 9: "celebram o presente contrato, que se regerá pelas cláusulas a seguir."
- **2.1 Objeto** (EQV-L): DOC-A p. 2 · DOC-B par. 11: "serviços de suporte técnico e manutenção corretiva e evolutiva do sistema de gestão de frota"
- **3.1 Vigência** (EQV-L): DOC-A p. 2 · DOC-B par. 13: "vigorará pelo prazo de 12 (doze) meses" (ver ACH-010 quanto ao marco inicial)

**Prazos de atendimento**
- **4.1 Início de atendimento, severidade crítica** (EQV-L): DOC-A p. 3 · DOC-B par. 15: "em até 4 (quatro) horas corridas, contadas da abertura do chamado."
- **4.3 Severidade baixa — texto da cláusula** (EQV-L): DOC-A p. 3 · DOC-B par. 17: "serão atendidos em até 5 (cinco) dias úteis" (texto inalterado; ver ACH-003)

**Obrigações da CONTRATADA**
- **5.1 Equipe certificada** (EQV-L): DOC-A p. 3 · DOC-B par. 19: "manter equipe técnica com certificação no sistema objeto deste contrato durante toda a vigência."
- **Confidencialidade** (EQV-L, **realocado**: DOC-A cl. 5.3 → DOC-B cl. 11.1, agora em cláusula própria "Cláusula 11 – Da Confidencialidade", par. 35): DOC-A p. 3 · DOC-B par. 36: "durante a vigência e por 5 (cinco) anos após o seu término."

**Obrigações da CONTRATANTE** (conteúdo das obrigações; designação da parte tratada no ACH-008)
- **6.1 Acesso remoto** (EQV-S): DOC-A p. 4 · DOC-B par. 22: "deverá fornecer à CONTRATADA acesso remoto ao ambiente do sistema"
- **6.2 Gestor do contrato** (EQV-S): DOC-A p. 4 · DOC-B par. 23: "deverá designar um gestor do contrato, responsável por acompanhar a execução dos serviços."

**Preço e pagamento**
- **7.1 Valor mensal** (EQV-L): DOC-A p. 4 · DOC-B par. 25: "R$ 18.500,00 (dezoito mil e quinhentos reais)."
- **7.2 Prazo de pagamento** (EQV-S): DOC-A p. 4: "em até 30 (trinta) dias após o recebimento da nota fiscal." · DOC-B par. 26: "no prazo máximo de trinta dias, contado do recebimento da nota fiscal."
- **7.3 Reajuste** (EQV-L): DOC-A p. 4 · DOC-B par. 27: "será reajustado anualmente pela variação do IPCA."

**Penalidades**
- **8.1 Gatilho da penalidade** (EQV-L): DOC-A p. 4 · DOC-B par. 29: "O descumprimento dos prazos previstos na Cláusula 4" (consequência tratada no ACH-005)

**Rescisão**
- **9.1 Rescisão por notificação** (EQV-L): DOC-A p. 5 · DOC-B par. 31: "com antecedência mínima de 30 (trinta) dias."

**Proteção de dados**
- **LGPD** (EQV-L, **realocado**: DOC-A cl. 11.1 → DOC-B cl. 10.1, título "Cláusula 10 – Da Proteção de Dados Pessoais", par. 33): DOC-A p. 5 · DOC-B par. 34: "exclusivamente para a execução do objeto deste contrato, observada a Lei nº 13.709/2018."

**Disposições gerais e assinaturas**
- **12.1 Anexo I integrado** (EQV-L): DOC-A p. 6 · DOC-B par. 38: "Integram este contrato o Anexo I (Descrição dos Serviços)" (referência ao segundo anexo tratada no ACH-007)
- **12.2 Foro** (EQV-L): DOC-A p. 6 · DOC-B par. 39: "Fica eleito o foro da Comarca de São Paulo/SP"
- **Linhas de assinatura** (EQV-L): DOC-A p. 6 · DOC-B par. 41–42: "BETA LOGÍSTICA S.A. (CONTRATANTE)" / "ALFA SISTEMAS LTDA. (CONTRATADA)"

**Anexos**
- **Anexo I — Descrição dos serviços** (EQV-L): DOC-A p. 7 · DOC-B par. 44: "manutenção evolutiva limitada a 40 (quarenta) horas mensais."
- **Anexo II — título** (EQV-L): DOC-A p. 7 · DOC-B par. 45: "Anexo II – Matriz de Severidade"
- **Anexo II — cabeçalho da tabela** (EQV-L): DOC-A p. 7, Tabela 1, linha 1 · DOC-B Tabela 1, linha 1: "Prazo de atendimento"
- **Anexo II — severidade crítica** (EQV-L): DOC-A p. 7, Tabela 1, linha 2 · DOC-B Tabela 1, linha 2: "Início em até 4 horas corridas"
- **Anexo II — severidade média** (EQV-L): DOC-A p. 7, Tabela 1, linha 3 · DOC-B Tabela 1, linha 3: "Até 2 dias úteis"

Títulos das Cláusulas 1, 2, 3, 4, 5, 7, 8, 9 e 12 são idênticos nos dois documentos (o título da Cláusula 6 está no ACH-008; os das Cláusulas 10 e 11 foram reordenados, conforme acima).

## 6. Declaração de cobertura e limitações

**Cobertura**
- DOC-A: páginas físicas 1 a 7 analisadas integralmente, inclusive a Tabela 1 (p. 7). Sem OCR.
- DOC-B: parágrafos 1 a 45 e Tabela 1 analisados integralmente; cabeçalho e rodapé verificados (vazios); sem alterações controladas e sem comentários.
- Conteúdo não analisado: nenhum. Todo o conteúdo dos dois documentos foi classificado em achado, item convergente ou observação (os campos "Versão" de cada documento foram usados para determinar a relação).

**Verificação das citações** (comparação automática com o texto extraído, normalizando só as quebras de linha do PDF, seguida de conferência do localizador)
- Evidências dos achados: 100% conferidas (todos os achados são Alta/Média e incluem CTR e EXC). Confirmadas no localizador indicado: todas. Corrigidas: 0. Divergentes: 0. Indisponíveis: 0.
- Itens convergentes: 100% conferidos, nos dois documentos. Divergentes: 0.
- Trechos entre aspas fora das Evidências (Análise, Observações, Questões): 100% conferidos. Corrigidos: 3 (expressões minhas que estavam entre aspas sem serem cópia literal viraram paráfrase sem aspas). Divergentes remanescentes: 0. Termos de busca aparecem sem aspas, para não serem confundidos com citações.
- Buscas de ausência (seguro, apólice, responsabilidade civil, cobertura, 500.000, indeniza, multa, Anexo III, Anexo IV, CLIENTE, Diretoria, aprovação) feitas por busca textual sobre o texto integral extraído.

**Limitações**
- A relação de versões e as premissas P1/P2 são inferidas: nenhum documento declara substituir o outro.
- Questões sobre validade jurídica (ACH-005, ACH-009) foram sinalizadas para especialista, sem conclusão.
- A data de fim de vigência no ACH-010 é cálculo derivado da cl. 3.1, não texto dos documentos.

**Observações não comparativas** (iguais nos dois documentos ou fora do escopo comparativo; sem ID de achado)
1. **Janela de suporte × prazo crítico em horas corridas.** O Anexo I (DOC-A p. 7; DOC-B par. 44) prevê "Suporte técnico remoto em dias úteis, das 8h às 18h", enquanto a cl. 4.1 (DOC-A p. 3; DOC-B par. 15) fixa início "em até 4 (quatro) horas corridas, contadas da abertura do chamado." Nenhum dos dois diz como fica um chamado crítico aberto à noite ou em fim de semana.
2. **Prazo de pagamento sem tipo de contagem.** A cl. 7.2, nos dois documentos, não informa se os 30 dias são corridos ou úteis.
3. **Severidade média só no anexo, sem prazo de correção.** O prazo da severidade média ("Até 2 dias úteis") aparece só no Anexo II; a Cláusula 4 não o menciona. Como a cl. 8.1 se refere aos "prazos previstos na Cláusula 4", fica em dúvida se o descumprimento desse prazo entra na penalidade. Os dois documentos também só preveem prazo de correção para a severidade crítica (cl. 4.2).
4. **Ausência de regra de alteração e precedência.** Nenhum dos dois documentos diz como versões posteriores se relacionam com as anteriores; a cl. 3.1 só prevê termo aditivo para prorrogação.
5. **Metadados de DOC-B incompatíveis com o conteúdo** (só DOC-B; não afeta a identificação da versão, que está clara no texto): propriedades do arquivo com criação e modificação em 23/12/2013 e autor "python-docx", enquanto o texto é datado de 2 de setembro de 2026. Os metadados do PDF (DOC-A) estão coerentes com o conteúdo (título "Contrato 041/2026 v1.0 (fictício)", criado em 14/10/2026).
6. **Paginação do PDF.** A numeração impressa no rodapé de DOC-A ("Página 1 de 6") começa na página física 2 e ignora a capa. Este relatório usa a página física.

## 7. Questões em aberto

- **Q1** — A ampliação do prazo de correção de falhas críticas de 30 para 45 dias foi negociada? Ref.: ACH-001
- **Q2** — Qual é o prazo para a severidade baixa na v2.0: 5 dias úteis (cl. 4.3) ou 10 dias úteis (Anexo II)? Ref.: ACH-002, ACH-003
- **Q3** — A emissão do relatório mensal deixou de ser obrigatória de propósito? Ref.: ACH-004
- **Q4** — Quais são as "medidas cabíveis" da cl. 8.1 da v2.0, e a multa de 2% foi suprimida intencionalmente? Ref.: ACH-005
- **Q5** — A exigência de seguro de responsabilidade civil profissional foi retirada de propósito? Ref.: ACH-006
- **Q6** — "Anexo IV" é erro de numeração do Anexo II ou existe um anexo a ser juntado? Ref.: ACH-007
- **Q7** — "CLIENTE" deve ser lido como CONTRATANTE? Corrigir para o termo definido. Ref.: ACH-008
- **Q8** — Como a aprovação da Diretoria Jurídica será comprovada à CONTRATADA, e qual o efeito de uma notificação sem ela? Ref.: ACH-009
- **Q9** — A v2.0 é novo instrumento, substituição ou consolidação? A vigência passa a contar de 02/09/2026? Ref.: ACH-010, premissas P1/P2
- **Q10** — Como tratar chamados críticos abertos fora da janela de suporte do Anexo I? Ref.: Observação 1
