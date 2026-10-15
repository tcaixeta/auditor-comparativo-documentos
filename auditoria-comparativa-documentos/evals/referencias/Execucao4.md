## Análise comparativa: Contrato nº 041/2026, DOC-A (v1.0) × DOC-B (v2.0)

> Os achados abaixo são **indícios até serem conferidos** por um revisor humano no documento original. O campo **Verificado** fica sempre em branco para o revisor.

### 1. Identificação e escopo

| ID        | Arquivo                | Versão | Data       | Partes / emissor                                             | Extensão                                                     | Esquema de localização                                       | Integridade                                                  |
| --------- | ---------------------- | ------ | ---------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **DOC-A** | DOC-A_contrato_v1.pdf  | 1.0    | 10/03/2026 | Beta Logística S.A. (CONTRATANTE) e Alfa Sistemas Ltda. (CONTRATADA). Metadado *Author*: Kit de teste | 7 páginas físicas: capa sem número e 6 páginas com rodapé no padrão Página N de 6 | Cláusula + **página física** (`p. N`). A p. 1 é a capa, então a página física é a impressa + 1. Tabela: `p. 7 · Tabela 1, linha L, col. C`, com a linha 1 sendo o cabeçalho | Texto nativo nas 7 páginas, **sem OCR**. A tabela da p. 7 foi extraída separadamente. Nada ilegível. |
| **DOC-B** | DOC-B_contrato_v2.docx | 2.0    | 02/09/2026 | Mesmas partes. Metadado *creator*: python-docx               | 45 parágrafos e 1 tabela, sem paginação fixa                 | Cláusula + **número do parágrafo** (`par. N`). Contei todos os parágrafos do corpo em ordem, a partir de 1, incluindo o título, as linhas da capa e os títulos de cláusula. Não há parágrafos vazios. Tabela: `Tabela 1, linha L, col. C` | Sem alterações controladas, comentários, cabeçalho ou rodapé. Nada ilegível. |

**Título dos dois:** Contrato de prestação de serviços de suporte técnico e manutenção de software.

**Estrutura:** os dois têm 12 cláusulas, o Anexo I (Descrição dos Serviços) e o Anexo II (Matriz de Severidade). Em DOC-B, as cláusulas 10 e 11 foram reorganizadas:

- **DOC-A:** a cláusula 10 trata de Seguro e a 11 de Proteção de Dados.
- **DOC-B:** a cláusula 10 trata de Proteção de Dados e a 11 de Confidencialidade. O texto da 11 estava antes em DOC-A 5.3.

### 2. Relação entre os documentos e premissas

**Relação identificada: são versões do mesmo contrato (DOC-A v1.0 → DOC-B v2.0).**
 Os dois têm o mesmo número, título e partes. DOC-A p. 1 traz “Versão 1.0” e “Data: 10 de março de 2026”. DOC-B traz “Versão 2.0” no par. 3 e “Data: 2 de setembro de 2026” no par. 4. Os títulos nos metadados dos arquivos indicam v1.0 e v2.0.

**Como isso afeta a classificação:** DOC-A é a linha de base. Cada diferença recebe o rótulo INCLUÍDO, REMOVIDO ou ALTERADO e é avaliada pelo impacto da mudança. Nenhuma versão é tratada como a correta.

| Premissa                                                     | Base                                                         | O que muda se estiver errada                                 |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **P1:** DOC-B é a versão posterior e pretende substituir DOC-A. | Numeração de versão e datas. **Nenhum dos dois documentos declara isso.** A cl. 3.1 prevê prorrogação “mediante termo aditivo”, e DOC-B não se apresenta como aditivo. | Se DOC-B for só minuta ou proposta, os achados viram pontos de negociação. Se as duas versões estiverem assinadas, elas coexistem sem regra de precedência (ver Q1). |
| **P2:** não se sabe se os documentos foram assinados.        | Os blocos de assinatura estão em branco nos dois (DOC-A p. 6; DOC-B par. 41–42). | A classificação não muda, mas muda qual texto obriga as partes hoje. |
| **P3:** o localizador do PDF usa a página física.            | O rodapé impresso não conta a capa.                          | Para obter a página impressa, subtraia 1.                    |

### 3. Resumo quantitativo

| Tipo | Qtde |      | Severidade           | Qtde  |
| ---- | ---- | ---- | -------------------- | ----- |
| CTR  | 3    |      | Crítica              | 1     |
| NCL  | 1    |      | Alta                 | 5     |
| EXC  | 1    |      | Média                | 3     |
| DIV  | 1    |      | Baixa / Informativa  | 0     |
| INT  | 1    |      | **Total de achados** | **9** |
| REF  | 1    |      |                      |       |
| TER  | 1    |      |                      |       |
| REV  | 0    |      |                      |       |

**Carga de revisão humana:**

- 1 item em NÃO CLARO (ACH-001).
- Nenhum item em REQUER REVISÃO.
- 1 achado com confiança Média (ACH-009).

**Itens convergentes:** 21, sendo 20 EQV-L e 1 EQV-S.

**Leitura geral (análise):** a maior parte do corpo do contrato foi mantida. As mudanças da v2.0 se concentram no nível de serviço e nos mecanismos que garantem seu cumprimento:

- o prazo de correção de falhas críticas ficou mais longo;
- o prazo da severidade baixa dobrou no anexo;
- a multa foi trocada por uma redação vaga;
- o relatório mensal virou facultativo;
- o seguro foi removido.

Todas essas mudanças reduzem obrigações ou garantias do lado da CONTRATADA. A v2.0 também traz três defeitos que não existiam na v1.0: uma contradição interna, uma referência quebrada e um termo não definido.

### 4. Achados detalhados

#### ACH-001: Multa por descumprimento de prazos substituída por “medidas cabíveis”

- **Tipo:** NCL. Mudança entre versões: ALTERADO
- **Severidade:** Crítica
- **Confiança:** Alta
- **Tópico:** Penalidades
- **Padrão entre documentos:** A ≠ B

**Evidências**

- DOC-A, cl. 8.1 (p. 4): “O descumprimento dos prazos previstos na Cláusula 4 sujeitará a CONTRATADA a multa de 2% (dois por cento) sobre o valor mensal, por ocorrência.”
- DOC-B, cl. 8.1 (par. 29): **NÃO CLARO.** “O descumprimento dos prazos previstos na Cláusula 4 poderá ensejar a aplicação das medidas cabíveis.” A cláusula trata das consequências do descumprimento, mas não define sanção, valor, base de cálculo nem incidência.
- **Citação verificada:** Sim (DOC-A e DOC-B)

**Ponto exato da diferença**

| Elemento        | DOC-A                                        | DOC-B                                   |
| --------------- | -------------------------------------------- | --------------------------------------- |
| Consequência    | multa                                        | “medidas cabíveis”, sem definição       |
| Valor           | 2%                                           | não definido                            |
| Base de cálculo | valor mensal                                 | não definida                            |
| Incidência      | por ocorrência                               | não definida                            |
| Modalidade      | “sujeitará a CONTRATADA”: consequência certa | “poderá ensejar”: consequência eventual |

**Análise**

- **Por que NCL:** a regra de desempate manda classificar como NCL, e não como CTR ou EXC, a troca de um conteúdo objetivo (multa de 2%) por uma redação vaga sobre o mesmo tema. O tema continua no documento, mas o novo texto não permite saber qual sanção se aplica.
- **Modalidade:** a mudança de consequência certa para eventual faz parte deste mesmo item.
- **Efeito na v2.0:** a Cláusula 4 fica sem sanção objetiva. Isso agrava ACH-002 e ACH-003, porque os prazos ficaram mais longos e o atraso deixou de ter consequência definida.

**Impacto e risco:** a CONTRATANTE perde uma penalidade prefixada. Qualquer sanção passaria a depender de negociação ou de litígio sobre o que são “medidas cabíveis”. Se essa redação é exigível, cabe a um especialista jurídico avaliar.

**Recomendação:**

1. Confirmar com os responsáveis se a remoção da multa foi intencional.
2. Se não foi, restabelecer uma penalidade objetiva, com percentual, base, incidência e eventual teto.
3. Se foi, registrar a decisão.
4. Em qualquer caso, encaminhar para revisão jurídica.

**Verificado (revisor):** ☐

------

#### ACH-002: Prazo de conclusão da correção de falhas críticas passou de 30 para 45 dias corridos

- **Tipo:** CTR. Mudança entre versões: ALTERADO
- **Severidade:** Alta
- **Confiança:** Alta
- **Tópico:** Prazos de atendimento
- **Padrão entre documentos:** A ≠ B

**Evidências**

- DOC-A, cl. 4.2 (p. 3): “A CONTRATADA deverá concluir a correção de falhas de severidade crítica em até 30 (trinta) dias corridos, contados da abertura do chamado.”
- DOC-B, cl. 4.2 (par. 16): “A CONTRATADA deverá concluir a correção de falhas de severidade crítica em até 45 (quarenta e cinco) dias corridos, contados da abertura do chamado.”
- **Citação verificada:** Sim (DOC-A e DOC-B)

**Ponto exato da diferença**

| Elemento         | DOC-A               | DOC-B            |
| ---------------- | ------------------- | ---------------- |
| Prazo            | 30 dias             | **45 dias**      |
| Tipo de contagem | corridos            | corridos (igual) |
| Marco inicial    | abertura do chamado | igual            |
| Modalidade       | deverá              | igual            |

**Análise:** é a mesma obrigação com dois valores que não podem valer ao mesmo tempo, por isso CTR. O prazo aumenta 50%. A severidade crítica é descrita como “Sistema indisponível” nos dois documentos (DOC-A p. 7 · Tabela 1, linha 2, col. 2; DOC-B Tabela 1, linha 2, col. 2). Pela v2.0, o sistema pode ficar indisponível até 45 dias sem que haja descumprimento, e sem multa objetiva (ACH-001).

**Impacto e risco:** a CONTRATANTE fica mais exposta em caso de indisponibilidade do sistema de gestão de frota.

**Recomendação:** confirmar se a mudança foi negociada e registrar a justificativa. Avaliar este prazo junto com a penalidade (ACH-001).

**Verificado (revisor):** ☐

------

#### ACH-003: Prazo da severidade baixa na Matriz (Anexo II) passou de 5 para 10 dias úteis

- **Tipo:** CTR. Mudança entre versões: ALTERADO
- **Severidade:** Alta
- **Confiança:** Alta
- **Tópico:** Prazos de atendimento / Anexo II
- **Padrão entre documentos:** A ≠ B

**Evidências**

- DOC-A, Anexo II (p. 7 · Tabela 1, linha 4, col. 3), na linha “Baixa”: “Até 5 dias úteis”
- DOC-B, Anexo II (Tabela 1, linha 4, col. 3), na linha “Baixa”: “Até 10 dias úteis”
- **Citação verificada:** Sim (DOC-A e DOC-B)

**Ponto exato da diferença**

| Elemento                                 | DOC-A        | DOC-B             |
| ---------------------------------------- | ------------ | ----------------- |
| Prazo de atendimento da severidade baixa | 5 dias úteis | **10 dias úteis** |
| Descrição da severidade (col. 2)         | igual        | igual             |

**Análise:**

- É o mesmo item com valores incompatíveis, por isso CTR.
- Só o anexo mudou. A cl. 4.3 continua idêntica nas duas versões (ver Itens convergentes), e por isso esta mudança cria a contradição interna de ACH-004.
- Além disso, a cl. 12.1 de DOC-B não lista mais o Anexo II entre os anexos que integram o contrato (ACH-007). Isso deixa incerto o status desta tabela na v2.0.

**Impacto e risco:** se prevalecer o anexo, o prazo para chamados de baixa severidade dobra.

**Recomendação:** decidir entre 5 e 10 dias úteis e alinhar a cl. 4.3 e o Anexo II.

**Verificado (revisor):** ☐

------

#### ACH-004: Contradição interna em DOC-B entre a cl. 4.3 (5 dias úteis) e o Anexo II (10 dias úteis)

- **Tipo:** INT
- **Severidade:** Alta
- **Confiança:** Alta
- **Tópico:** Prazos de atendimento
- **Padrão entre documentos:** interno a DOC-B. Em DOC-A, a cl. 4.3 e o Anexo II são coerentes entre si.

**Evidências**

- DOC-B, cl. 4.3 (par. 17): “Os chamados de severidade baixa serão atendidos em até 5 (cinco) dias úteis, conforme a Matriz de Severidade do Anexo II.”
- DOC-B, Anexo II (Tabela 1, linha 4, col. 3): “Até 10 dias úteis”
- Referência sem o defeito:
  - DOC-A, cl. 4.3 (p. 3): “Os chamados de severidade baixa serão atendidos em até 5 (cinco) dias úteis, conforme a Matriz de Severidade do Anexo II.”
  - DOC-A, Anexo II (p. 7 · Tabela 1, linha 4, col. 3): “Até 5 dias úteis”
- **Citação verificada:** Sim

**Ponto exato da diferença**

| Elemento                  | DOC-B, cl. 4.3 | DOC-B, Anexo II, linha 4 |
| ------------------------- | -------------- | ------------------------ |
| Prazo da severidade baixa | 5 dias úteis   | 10 dias úteis            |

**Análise:** a cláusula fixa 5 dias úteis e diz que segue a Matriz, mas a Matriz fixa 10. Os dois prazos não podem valer para os mesmos chamados. DOC-B não tem regra de precedência entre corpo e anexos (Observação O1), então o próprio texto não resolve o conflito. A origem está em ACH-003, e o efeito é agravado por ACH-007.

**Impacto e risco:** abre disputa sobre o prazo aplicável e sobre quando há descumprimento da Cláusula 4.

**Recomendação:** corrigir para um único valor e incluir uma cláusula de precedência entre corpo e anexos.

**Verificado (revisor):** ☐

------

#### ACH-005: Relatório mensal de desempenho deixou de ser obrigatório e virou facultativo

- **Tipo:** CTR. Mudança entre versões: ALTERADO
- **Severidade:** Alta
- **Confiança:** Alta
- **Tópico:** Obrigações da CONTRATADA
- **Padrão entre documentos:** A ≠ B

**Evidências**

- DOC-A, cl. 5.2 (p. 3): “A CONTRATADA deverá emitir relatório mensal de desempenho até o 5º (quinto) dia útil de cada mês.”
- DOC-B, cl. 5.2 (par. 20): “A CONTRATADA poderá emitir relatório mensal de desempenho até o 5º (quinto) dia útil de cada mês.”
- **Citação verificada:** Sim (DOC-A e DOC-B)

**Ponto exato da diferença**

| Elemento                        | DOC-A              | DOC-B                  |
| ------------------------------- | ------------------ | ---------------------- |
| Modalidade                      | deverá (obrigação) | **poderá** (faculdade) |
| Periodicidade, prazo e conteúdo | iguais             | iguais                 |

**Análise:**

- **Por que CTR:** pela regra de desempate, mudança de modalidade é CTR mesmo com o resto da frase idêntico.
- **Não há substituto:** nenhuma outra cláusula, em nenhum dos dois documentos, prevê relatório ou medição do cumprimento dos prazos da Cláusula 4. Procurei pelos termos “relatório” e “medição”.
- **Efeito na v2.0:** a CONTRATANTE perde o direito de exigir a principal prova documental de desempenho. Isso acontece justamente quando os prazos (ACH-002, ACH-003) e a penalidade (ACH-001) também foram flexibilizados.

**Impacto e risco:** fica mais difícil comprovar descumprimento do nível de serviço.

**Recomendação:** confirmar a intenção. Se o acompanhamento for necessário, voltar a usar “deverá”.

**Verificado (revisor):** ☐

------

#### ACH-006: Cláusula de seguro de responsabilidade civil profissional foi removida

- **Tipo:** EXC. Mudança entre versões: REMOVIDO
- **Severidade:** Alta
- **Confiança:** Alta
- **Tópico:** Seguro / garantias
- **Padrão entre documentos:** A ≠ B (presente só em DOC-A)

**Evidências**

- DOC-A, cl. 10.1 (p. 5): “A CONTRATADA manterá, durante toda a vigência deste contrato, apólice de seguro de responsabilidade civil profissional com cobertura mínima de R$ 500.000,00 (quinhentos mil reais).”
- DOC-B: **NÃO PRESENTE.**
  - Procurei no documento inteiro (par. 1–45 e Tabela 1), com atenção a estas partes:
    - Cláusula 5, Obrigações da CONTRATADA (par. 18–20)
    - Cláusula 8, Penalidades (par. 28–29)
    - Cláusula 10, Proteção de Dados (par. 33–34)
    - Cláusula 11, Confidencialidade (par. 35–36)
    - Cláusula 12, Disposições Gerais (par. 37–39)
    - Anexo I (par. 43–44)
  - Termos buscados: “seguro”, “apólice”, “responsabilidade civil”, “cobertura”, “garantia”, “indeniz”, “500.000”.
  - Conteúdo relacionado encontrado: nenhum.
- **Citação verificada:** Sim (DOC-A)

**Ponto exato da diferença**

| Elemento                                      | DOC-A                        | DOC-B   |
| --------------------------------------------- | ---------------------------- | ------- |
| Obrigação de manter seguro de RC profissional | sim, durante toda a vigência | ausente |
| Cobertura mínima                              | R$ 500.000,00                | —       |

**Análise:** o tema inteiro deixou de existir e a busca não encontrou nada relacionado, por isso EXC. O número da cláusula foi reaproveitado: em DOC-B, a Cláusula 10 passou a tratar de Proteção de Dados.

**Impacto e risco:** a CONTRATANTE perde a garantia contratual de cobertura para danos causados pela CONTRATADA durante os serviços.

**Recomendação:** confirmar se a remoção foi intencional. Se não foi, reinserir a cláusula.

**Verificado (revisor):** ☐

------

#### ACH-007: A cl. 12.1 de DOC-B cita um “Anexo IV (Matriz de Severidade)” que não existe

- **Tipo:** REF. Mudança entre versões: ALTERADO (cl. 12.1)
- **Severidade:** Média
- **Confiança:** Alta
- **Tópico:** Disposições gerais / anexos
- **Padrão entre documentos:** defeito presente só em DOC-B

**Evidências**

- DOC-B, cl. 12.1 (par. 38): “Integram este contrato o Anexo I (Descrição dos Serviços) e o Anexo IV (Matriz de Severidade).”
- DOC-B, título do anexo (par. 45): “Anexo II – Matriz de Severidade”
- DOC-B, cl. 4.3 (par. 17): “[...] conforme a Matriz de Severidade do Anexo II.”
- DOC-A, cl. 12.1 (p. 6): “Integram este contrato o Anexo I (Descrição dos Serviços) e o Anexo II (Matriz de Severidade).”
- Busca em DOC-B: os únicos anexos que existem são o Anexo I (par. 43) e o Anexo II (par. 45). Não há “Anexo III” nem outro “Anexo IV”.
- **Citação verificada:** Sim

**Ponto exato da diferença**

| Elemento                                 | DOC-A, cl. 12.1 | DOC-B, cl. 12.1 |
| ---------------------------------------- | --------------- | --------------- |
| Anexo indicado como Matriz de Severidade | Anexo II        | **Anexo IV**    |
| Esse anexo existe no documento?          | Sim             | Não             |

**Análise:** é provável que seja erro de numeração, mas isso é inferência. Pela letra do texto, a cl. 12.1 de DOC-B não inclui o Anexo II entre os anexos que integram o contrato, enquanto a cl. 4.3 continua remetendo a ele. Isso enfraquece o status contratual da Matriz e se soma à contradição de ACH-004. Se um anexo não listado vincula as partes, cabe a um especialista jurídico avaliar.

**Impacto e risco:** a correção é simples, mas, sem ela, o defeito alimenta a disputa sobre qual prazo vale.

**Recomendação:** corrigir a cl. 12.1 para “Anexo II” ou renumerar o anexo de forma consistente em todo o documento.

**Verificado (revisor):** ☐

------

#### ACH-008: Rescisão pela CONTRATANTE passou a depender de aprovação da Diretoria Jurídica

- **Tipo:** DIV. Mudança entre versões: INCLUÍDO
- **Severidade:** Média
- **Confiança:** Alta
- **Tópico:** Rescisão
- **Padrão entre documentos:** A ≠ B

**Evidências**

- DOC-A, cl. 9.1 (p. 5): “Qualquer das partes poderá rescindir este contrato mediante notificação por escrito, com antecedência mínima de 30 (trinta) dias.”
- DOC-B, cl. 9.1 (par. 31): “Qualquer das partes poderá rescindir este contrato mediante notificação por escrito, com antecedência mínima de 30 (trinta) dias.”
- DOC-B, cl. 9.2 (par. 32): “A rescisão por iniciativa da CONTRATANTE dependerá de prévia aprovação de sua Diretoria Jurídica.”
- DOC-A: a Cláusula 9 (p. 5) tem só a 9.1. Busquei “aprovação”, “Diretoria” e “Jurídic” no documento inteiro e não houve nenhuma ocorrência.
- **Citação verificada:** Sim

**Ponto exato da diferença**

| Elemento                               | DOC-A                                         | DOC-B                                                        |
| -------------------------------------- | --------------------------------------------- | ------------------------------------------------------------ |
| Condições para a CONTRATANTE rescindir | notificação escrita e 30 dias de antecedência | notificação escrita, 30 dias e **prévia aprovação da Diretoria Jurídica** |
| Condições para a CONTRATADA rescindir  | notificação escrita e 30 dias de antecedência | igual                                                        |

**Análise:**

- **Por que DIV:** o tema existe nos dois documentos. A v2.0 acrescenta uma condição a um direito que já existia, por isso DIV e não EXC.
- **Assimetria:** a mudança trata as partes de forma diferente e coloca uma aprovação interna da CONTRATANTE num contrato bilateral.
- **Lacuna:** o texto não diz o que acontece se a notificação for enviada sem essa aprovação. Não fica claro se a rescisão perde a validade perante a CONTRATADA ou se ela pode exigir comprovação. Isso pede avaliação de especialista jurídico.

**Impacto e risco:** a CONTRATADA pode contestar uma rescisão alegando falta de comprovação da aprovação interna.

**Recomendação:** confirmar a intenção. Avaliar se a regra deveria ficar numa política interna, e não no contrato. Se ficar no contrato, definir como a aprovação é comprovada e qual o efeito se ela faltar.

**Verificado (revisor):** ☐

------

#### ACH-009: DOC-B usa “CLIENTE”, termo não definido, para a parte obrigada na Cláusula 6

- **Tipo:** TER
- **Severidade:** Média
- **Confiança:** Média
- **Tópico:** Obrigações da CONTRATANTE / terminologia
- **Padrão entre documentos:** defeito presente só em DOC-B

**Evidências em DOC-A**

- Cl. 1.1 (p. 2): “BETA LOGÍSTICA S.A., doravante denominada CONTRATANTE”
- Título da Cláusula 6 (p. 4): “Cláusula 6 – Das Obrigações da CONTRATANTE”
- Cl. 6.1 (p. 4): “A CONTRATANTE deverá fornecer à CONTRATADA acesso remoto ao ambiente do sistema, nos termos da política de segurança da informação da CONTRATANTE.”
- Cl. 6.2 (p. 4): “A CONTRATANTE deverá designar um gestor do contrato, responsável por acompanhar a execução dos serviços.”

**Evidências em DOC-B**

- Cl. 1.1 (par. 9): “BETA LOGÍSTICA S.A., doravante denominada CONTRATANTE”
- Título da Cláusula 6 (par. 21): “Cláusula 6 – Das Obrigações do CLIENTE”
- Cl. 6.1 (par. 22): “O CLIENTE deverá fornecer à CONTRATADA acesso remoto ao ambiente do sistema, nos termos da política de segurança da informação do CLIENTE.”
- Cl. 6.2 (par. 23): “O CLIENTE deverá designar um gestor do contrato, responsável por acompanhar a execução dos serviços.”
- Cl. 7.1 (par. 25), que volta a usar CONTRATANTE logo em seguida: “a CONTRATANTE pagará à CONTRATADA”

**Busca:** “CLIENTE” aparece em DOC-B só nos par. 21–23 e não é definido em nenhum lugar. Em DOC-A, o termo não aparece.

**Citação verificada:** Sim

**Ponto exato da diferença**

| Elemento                      | DOC-A                            | DOC-B                     |
| ----------------------------- | -------------------------------- | ------------------------- |
| Parte obrigada na Cláusula 6  | CONTRATANTE, definida na cl. 1.1 | **CLIENTE**, não definido |
| Demais elementos de 6.1 e 6.2 | —                                | iguais aos de DOC-A       |

**Análise:** é razoável entender CLIENTE como CONTRATANTE, já que só uma parte ocupa esse papel. Mas isso é inferência. Por isso a confiança é Média e as cláusulas 6.1 e 6.2 não entraram como equivalentes (EQV-S). As obrigações da Cláusula 6, de dar acesso remoto e designar um gestor do contrato, são pré-requisitos para a CONTRATADA cumprir os prazos da Cláusula 4.

**Impacto e risco:** dá argumento para discutir quem responde pelas obrigações da Cláusula 6 e, em consequência, pelo descumprimento de prazos.

**Recomendação:** substituir “CLIENTE” por “CONTRATANTE” nos par. 21–23 ou definir o termo na cl. 1.1.

**Verificado (revisor):** ☐

### 5. Itens convergentes

**Capa e identificação**

- **Título** (EQV-L). DOC-A p. 1 · DOC-B par. 1: “CONTRATO DE PRESTAÇÃO DE SERVIÇOS DE SUPORTE TÉCNICO E MANUTENÇÃO DE SOFTWARE”
- **Número do contrato** (EQV-L). DOC-A p. 1 · DOC-B par. 2: “Contrato nº 041/2026”
- **Partes na capa** (EQV-L). DOC-A p. 1 · DOC-B par. 5–6: “CONTRATANTE: Beta Logística S.A.” / “CONTRATADA: Alfa Sistemas Ltda.”
- **Nota de documento fictício** (EQV-L). DOC-A p. 1 · DOC-B par. 7: “Documento fictício, elaborado exclusivamente para testes.”

**Corpo**

- **Partes, cl. 1.1** (EQV-L). DOC-A p. 2 · DOC-B par. 9: “BETA LOGÍSTICA S.A., doravante denominada CONTRATANTE, e ALFA SISTEMAS LTDA., doravante denominada CONTRATADA”
- **Objeto, cl. 2.1** (EQV-L). DOC-A p. 2 · DOC-B par. 11: “serviços de suporte técnico e manutenção corretiva e evolutiva do sistema de gestão de frota”
- **Vigência, cl. 3.1** (EQV-L). DOC-A p. 2 · DOC-B par. 13: “vigorará pelo prazo de 12 (doze) meses, contados da data de sua assinatura”
- **Início do atendimento de severidade crítica, cl. 4.1** (EQV-L). DOC-A p. 3 · DOC-B par. 15: “iniciar o atendimento de chamados de severidade crítica em até 4 (quatro) horas corridas”
- **Atendimento de severidade baixa, cl. 4.3** (EQV-L, texto idêntico; ver ACH-004). DOC-A p. 3 · DOC-B par. 17: “Os chamados de severidade baixa serão atendidos em até 5 (cinco) dias úteis”
- **Equipe certificada, cl. 5.1** (EQV-L). DOC-A p. 3 · DOC-B par. 19: “manter equipe técnica com certificação no sistema objeto deste contrato”
- **Sigilo** (EQV-L, **realocado**). Saiu de DOC-A cl. 5.3, dentro de Obrigações da CONTRATADA, e foi para DOC-B cl. 11.1, na nova “Cláusula 11 – Da Confidencialidade”. DOC-A cl. 5.3 (p. 3) · DOC-B cl. 11.1 (par. 36): “manter sigilo sobre todas as informações da CONTRATANTE a que tiver acesso em razão deste contrato, durante a vigência e por 5 (cinco) anos após o seu término”
- **Preço, cl. 7.1** (EQV-L). DOC-A p. 4 · DOC-B par. 25: “o valor mensal de R$ 18.500,00 (dezoito mil e quinhentos reais)”
- **Prazo de pagamento, cl. 7.2** (EQV-S). Mesmo prazo e mesmo marco inicial; os dois também não dizem se os dias são corridos ou úteis.
  - DOC-A p. 4: “O pagamento será efetuado em até 30 (trinta) dias após o recebimento da nota fiscal.”
  - DOC-B par. 26: “O pagamento ocorrerá no prazo máximo de trinta dias, contado do recebimento da nota fiscal.”
- **Reajuste, cl. 7.3** (EQV-L). DOC-A p. 4 · DOC-B par. 27: “O valor mensal será reajustado anualmente pela variação do IPCA.”
- **Rescisão por notificação, cl. 9.1** (EQV-L; a condição nova está em ACH-008). DOC-A p. 5 · DOC-B par. 31: “Qualquer das partes poderá rescindir este contrato mediante notificação por escrito”
- **Proteção de dados** (EQV-L, **renumerado** de DOC-A cl. 11.1 para DOC-B cl. 10.1). DOC-A p. 5 · DOC-B par. 34: “tratará os dados pessoais a que tiver acesso exclusivamente para a execução do objeto deste contrato, observada a Lei nº 13.709/2018”
- **Foro, cl. 12.2** (EQV-L). DOC-A p. 6 · DOC-B par. 39: “Fica eleito o foro da Comarca de São Paulo/SP”
- **Blocos de assinatura** (EQV-L). DOC-A p. 6 · DOC-B par. 41–42: “BETA LOGÍSTICA S.A. (CONTRATANTE)” / “ALFA SISTEMAS LTDA. (CONTRATADA)”

**Anexos**

- **Anexo I** (EQV-L). DOC-A p. 7 · DOC-B par. 44: “manutenção evolutiva limitada a 40 (quarenta) horas mensais”
- **Anexo II, severidade crítica** (EQV-L). DOC-A p. 7 · Tabela 1, linha 2 · DOC-B Tabela 1, linha 2: “Sistema indisponível” / “Início em até 4 horas corridas”
- **Anexo II, severidade média** (EQV-L). DOC-A p. 7 · Tabela 1, linha 3 · DOC-B Tabela 1, linha 3: “Funcionalidade degradada” / “Até 2 dias úteis”

**Fora da contagem:**

- São idênticos os títulos das Cláusulas 1 a 5, 7 a 9 e 12, os títulos dos Anexos I e II e o cabeçalho da Matriz.
- Os títulos das Cláusulas 10 e 11 mudaram por causa da reorganização (ver ACH-006 e os itens de sigilo e proteção de dados acima).
- O título da Cláusula 6 está em ACH-009.

### 6. Declaração de cobertura e limitações

**O que foi analisado**

- **DOC-A:** as páginas físicas 1 a 7 inteiras, com texto nativo e sem OCR, incluindo a tabela da p. 7 e os rodapés.
- **DOC-B:** os par. 1 a 45 e a Tabela 1 inteiros. Também procurei alterações controladas, comentários, cabeçalhos e rodapés, e não há nenhum.
- **Metadados** dos dois arquivos (ver O7).

**O que não foi analisado:** nenhum conteúdo ficou de fora. Não avaliei a validade jurídica das cláusulas, porque isso está fora do escopo da evidência documental. Os achados indicam onde essa avaliação é necessária.

**Diferenças de identificação que não viraram achado:** a versão e a data na capa e o local e a data de assinatura mudam entre os documentos.

- DOC-A: “Versão 1.0” e “Data: 10 de março de 2026” na p. 1; “São Paulo, 10 de março de 2026.” na p. 6.
- DOC-B: “Versão 2.0” no par. 3; “Data: 2 de setembro de 2026” no par. 4; “São Paulo, 2 de setembro de 2026.” no par. 40.

Essas informações são coerentes dentro de cada documento e servem para identificar as versões. O rodapé de DOC-A (“Contrato nº 041/2026 – Versão 1.0 · Página 1 de 6” e seguintes) não existe em DOC-B, mas é só diferença de formatação.

**Reconciliação:** todos os dispositivos dos dois documentos foram classificados como achado ou como item convergente.

**Verificação das citações:** fiz uma conferência mecânica por script contra o texto extraído e depois conferi cada localizador.

- **Total:** 91 trechos entre aspas atribuídos aos documentos, todos conferidos. Isso é 100%, acima da amostra exigida. Os termos de busca entre aspas não são citações e ficaram fora da contagem.
- **Evidências e itens convergentes:** 100% confirmados no localizador indicado. Nenhuma citação corrigida, divergente ou indisponível.
- **Trechos entre aspas fora das Evidências** (Ponto exato, Análise, Recomendação, Observações, Questões e inventário): 100% conferidos. **Corrigi 3** que eram expressões minhas entre aspas e viraram paráfrase sem aspas. Nenhum divergente.
- **Quebras de linha do PDF:** foram tratadas como um espaço simples. Nenhuma citação atravessa hifenização.

**Limitações**

- A relação de versões com substituição é uma premissa (P1). Nenhum documento a declara.
- Não se sabe se os documentos foram assinados (P2).
- ACH-009 depende de entender CLIENTE como CONTRATANTE.

**Observações não comparativas** (problemas iguais nos dois documentos; ficam fora da contagem de achados)

- **O1. Não há regra de precedência entre corpo e anexos.** Busquei “prevalec”, “precedên” e “conflit” nos dois, sem resultado. Em DOC-A isso não tem efeito hoje, porque corpo e anexos são coerentes. Em DOC-B, impede resolver ACH-004.
- **O2. O prazo de pagamento não diz o tipo de contagem.** A cl. 7.2 de DOC-A (p. 4) e de DOC-B (par. 26) não dizem se os 30 dias são corridos ou úteis. A Cláusula 4, ao contrário, especifica.
- **O3. O reajuste não tem data-base.** A cl. 7.3 dos dois diz “reajustado anualmente pela variação do IPCA”, sem marco inicial nem período de apuração.
- **O4. O prazo de atendimento é ambíguo para as severidades média e baixa.**
  - Para a crítica, os dois documentos separam o início do atendimento (cl. 4.1 e “Início em até 4 horas corridas” no Anexo II) da conclusão (cl. 4.2).
  - Para a média e a baixa, a Matriz diz só, por exemplo, “Até 2 dias úteis”, e a cl. 4.3 diz “serão atendidos”. Não fica claro se o prazo é de início ou de solução.
  - Não há prazo de correção para essas severidades, e a severidade média só aparece no Anexo II.
- **O5. Nenhum documento trata da substituição entre versões.** DOC-B não menciona a versão 1.0 nem diz que a substitui; busquei “substitu”, sem resultado. A cl. 3.1 dos dois prevê prorrogação “mediante termo aditivo”. Ver Q1.
- **O6. Os blocos de assinatura estão em branco** nos dois (DOC-A p. 6; DOC-B par. 41–42).
- **O7. As datas dos arquivos não refletem a cronologia.**
  - O PDF de DOC-A foi criado em 14/10/2026, depois da data do conteúdo (10/03/2026).
  - O DOCX de DOC-B tem criação e modificação em 23/12/2013 e *creator* python-docx, datas anteriores ao próprio contrato.
  - Os títulos nos metadados (v1.0 e v2.0) e o conteúdo identificam as versões de forma coerente, então a identificação não é afetada. A cronologia deve vir do conteúdo.
- **O8. Contexto externo, não evidência.** A cláusula de proteção de dados é igual e mínima nos dois: trata da finalidade e cita a Lei nº 13.709/2018. Contratos com operador de dados costumam tratar também de segurança, incidentes e eliminação dos dados ao término. Vale avaliar com o encarregado de dados ou o jurídico.

### 7. Questões em aberto

- **Q1.** DOC-B (v2.0) substitui DOC-A (v1.0)? Foi assinado? Se as duas versões estiverem assinadas, qual prevalece? *Ref.: P1, P2, O5, O6. Afeta todos os achados.*
- **Q2.** A troca da multa de 2% por “medidas cabíveis” foi intencional? Qual sanção se pretende aplicar? *Ref.: ACH-001.*
- **Q3.** O prazo de 45 dias corridos para corrigir falhas críticas foi negociado e aceito pela CONTRATANTE? *Ref.: ACH-002.*
- **Q4.** O prazo da severidade baixa é de 5 ou de 10 dias úteis? *Ref.: ACH-003, ACH-004.*
- **Q5.** Tornar o relatório mensal facultativo foi intencional? Como o desempenho será medido? *Ref.: ACH-005.*
- **Q6.** A remoção do seguro de RC profissional foi intencional? *Ref.: ACH-006.*
- **Q7.** “Anexo IV” na cl. 12.1 é erro de digitação para Anexo II? *Ref.: ACH-007.*
- **Q8.** Que efeito tem, perante a CONTRATADA, uma rescisão feita sem a aprovação da Diretoria Jurídica? Essa regra deve ficar no contrato? *Ref.: ACH-008.*
- **Q9.** “CLIENTE” na Cláusula 6 se refere à CONTRATANTE? *Ref.: ACH-009.*
- **Q10.** Deve ser incluída uma regra de precedência entre corpo e anexos? *Ref.: O1, ACH-004.*