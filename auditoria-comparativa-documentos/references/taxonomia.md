# Taxonomia de achados e regras de classificação

Leia antes da Etapa 5. Estas regras existem para que a mesma diferença receba o mesmo tipo em execuções diferentes; foram calibradas em testes com gabarito.

## Índice
1. Tipos de achado
2. Os três estados de "não encontrado"
3. Regras de desempate
4. Achado × observação × convergência (e exclusividade)
5. Unidade do achado

## 1. Tipos de achado

| Código | Tipo | Definição | Exemplo |
|---|---|---|---|
| **EQV-L** | Equivalente literal | Texto idêntico ou com diferenças apenas de forma (pontuação, formatação). | Mesma cláusula, mesma redação. |
| **EQV-S** | Equivalente semântico | Redação diferente, mesmo significado e mesmo efeito. | "em até 30 dias" × "no prazo máximo de trinta dias". |
| **CTR** | Contradição | Afirmações que **não podem ser verdadeiras ou cumpridas ao mesmo tempo**. | "prazo de 30 dias" × "prazo de 45 dias"; "deve" × "é vedado". |
| **DIV** | Divergência | Diferença material que **pode coexistir**, mas muda o efeito, a ênfase ou a condição. | A exige aprovação do gestor; B exige aprovação do gestor **e** do jurídico. |
| **PAR** | Cobertura parcial | Um documento trata o tema de forma mais ampla ou detalhada; o outro cobre só parte. | A lista 5 critérios de aceite; B lista 3 deles. |
| **EXC** | Exclusivo / não presente | O item existe em um ou mais documentos e o outro documento **foi lido e não trata do tema** (estado NÃO PRESENTE). | Cláusula de multa só em DOC-A. |
| **TER** | Inconsistência terminológica | Mesmo conceito com nomes diferentes, ou mesmo termo com significados diferentes. | "Cliente" em A = "Contratante" em B; "usuário" com definições diferentes. |
| **INT** | Contradição interna | Contradição dentro de um mesmo documento. | DOC-A §2 diz 30 dias; DOC-A §9 diz 60 dias. |
| **REF** | Referência quebrada | Referência a seção, anexo ou documento inexistente ou incompatível. | DOC-B cita "Anexo III", que não existe. |
| **NCL** | Não claro | Há conteúdo sobre o tema, mas não é possível classificá-lo com segurança (estado NÃO CLARO). | Redação admite duas leituras; cláusula parcial; dispositivos conflitantes. |
| **REV** | Requer revisão | Há conteúdo, mas a classificação depende de julgamento humano, ou a citação não pôde ser obtida/confirmada (estado REQUER REVISÃO). | Redação atípica; texto truncado; OCR ilegível; citação divergente na verificação. |


## 2. Os três estados de "não encontrado"
Quando não for possível produzir uma correspondência positiva entre documentos, **nunca deixe o item em branco nem use um "não encontrado" genérico**. Escolha um destes estados, porque cada um leva a uma ação diferente:

| Estado | Significado | Classificação | Ação típica |
|---|---|---|---|
| **NÃO PRESENTE** | O documento foi lido e o tema não está lá. | EXC | Decidir se o tema deve ser incluído. |
| **NÃO CLARO** | Há algo sobre o tema, mas é ambíguo, parcial ou conflitante. | NCL | Esclarecer a redação com o responsável. |
| **REQUER REVISÃO** | Algo foi encontrado, mas a decisão exige julgamento humano, ou a evidência não pôde ser extraída ou confirmada. | REV | Revisão humana do trecho indicado. |

"O documento não trata de multa" e "a cláusula de multa é ambígua" são informações diferentes. Juntá-las num mesmo rótulo esconde o que precisa ser feito.

Quando os documentos forem **versões**, acrescente o rótulo de mudança ao tipo: `INCLUÍDO`, `REMOVIDO` ou `ALTERADO` (ex.: `CTR / ALTERADO`).

Diferenças puramente de formatação, ortografia ou estilo **não** são achados, a menos que alterem o significado. Itens desse tipo podem ser agrupados como EQV-L.

## 3. Regras de desempate
Aplique estas regras sempre que mais de um tipo parecer possível. Elas existem para que a mesma diferença receba o mesmo tipo em execuções diferentes.

| Situação | Tipo | Por quê |
|---|---|---|
| A modalidade muda entre obrigação, faculdade e proibição ("deve" ↔ "pode" ↔ "não deve / é vedado"), mesmo com o resto da frase idêntico | **CTR** | O status normativo do mesmo item não pode ser ao mesmo tempo obrigatório e facultativo. Que o mesmo ato cumpra as duas versões não muda isso. |
| Muda um valor, prazo, unidade, base de cálculo ou responsável do **mesmo** item | **CTR** | Os dois valores não podem valer juntos para a mesma obrigação. |
| Um documento acrescenta uma condição, exceção, etapa ou requisito a um item que existe nos dois | **DIV** (`INCLUÍDO`, se forem versões) | A regra original continua lá, com o efeito alterado. Não é EXC, porque o tema existe nos dois. |
| Um documento cobre só parte de uma lista ou de um escopo que o outro cobre inteiro | **PAR** | Há sobreposição parcial do mesmo tema. |
| O **tema inteiro** existe em um documento e não aparece em nenhuma parte do outro | **EXC** | Só use EXC quando a busca descrita na regra de evidência de ausência não encontrar nada relacionado. |
| O documento troca um conteúdo objetivo por uma redação vaga sobre o mesmo tema (ex.: multa de 2% → "medidas cabíveis") | **NCL** | O tema existe, mas o novo conteúdo não pode ser classificado com segurança. |
| Mesmo conteúdo com número ou posição diferente | **EQV-L**, com nota de realocação | É equivalência, não diferença. Vai para Itens convergentes, não para Achados (ver `references/taxonomia.md`, seção 4). |

## 4. Achado × observação × convergência
Antes de registrar algo como achado, decida em qual seção ele entra:

| O que foi encontrado | Onde registrar |
|---|---|
| Diferença entre documentos (CTR, DIV, PAR, EXC, NCL, TER entre documentos) | **Achados detalhados** |
| Defeito que existe em um documento e não no outro (INT, REF, TER interno), inclusive um defeito novo numa versão | **Achados detalhados** |
| Conteúdo equivalente, inclusive realocado ou renumerado (EQV-L, EQV-S) | **Itens convergentes**, com nota de realocação quando houver. Nunca em Achados. |
| Ambiguidade, lacuna ou problema **igual nos dois documentos** (mesma redação, mesmo defeito) | **Observações não comparativas** (seção 6), sem ID de achado |
| Diferença de metadados do arquivo (datas, autor, título) | Achado **Informativo** só se afetar a cronologia ou a identificação das versões. Caso contrário, Observações. |
| Diferença na **identificação do documento**: número de versão, data de emissão, data e local de assinatura, título | **Inventário** (seção 1) e, se servir de base para a relação entre documentos, seção 2. Vira achado **somente** quando uma regra do próprio documento usa esse dado como marco (ex.: vigência contada "da data de sua assinatura"). Nesse caso, o achado trata do **efeito normativo** (o marco de vigência muda ou fica incerto), cita a regra e a data, e é classificado pelas regras de desempate. A data em si nunca é achado. |

Um problema comum aos dois documentos pode ser importante, mas não é resultado da comparação. Misturá-lo aos achados infla a contagem e confunde a leitura do que mudou.

**Exclusividade entre achado e convergência.** Cada par de itens comparados (ex.: DOC-A cl. 6.1 × DOC-B cl. 6.1) recebe **uma única** classificação: ou é achado, ou é convergente.
- Um item com achado **não aparece em Itens convergentes, nem em parte**. Não separe o "conteúdo que não mudou" (ex.: o gatilho de uma multa, o Anexo I dentro de uma cláusula que também cita um anexo inexistente, as obrigações de uma cláusula cuja parte obrigada mudou de nome) para listá-lo como convergente. O que não mudou é descrito na tabela **Ponto exato** do próprio achado, com o valor "igual".
- Um item **idêntico entre os documentos** continua convergente mesmo que participe de um achado **com outro item**. Exemplos: a cl. 4.3, idêntica nas duas versões, que contradiz o Anexo II da versão nova (INT entre 4.3 e Anexo II); a cl. 9.1, idêntica, à qual a versão nova acrescenta a cl. 9.2 (DIV). Nesse caso, liste-o como convergente com a nota "ver ACH-00X".

## 5. Unidade do achado
- **Um achado por item comparado.** Cada achado trata de um único item (ou de um único par de trechos, em INT e REF) e recebe um único tipo.
- **Separe achados só quando os pares de itens comparados forem diferentes.** Exemplo: o Anexo II mudou de 5 para 10 dias entre as versões (par: Anexo II de A × Anexo II de B → CTR) e, na versão nova, contradiz a cl. 4.3 (par: cl. 4.3 de B × Anexo II de B → INT). São dois pares, logo dois achados, ligados por referência cruzada ("ver ACH-00X").
- **Mudança entre versões e defeito no mesmo item = um único achado.** Quando a mudança e o defeito que ela cria estão no **mesmo** item, registre um achado só, com o tipo mais específico (REF, TER ou INT) e o rótulo de versão. Exemplos: a cl. 12.1 passou a citar um "Anexo IV" inexistente → um achado **REF / ALTERADO**, não um CTR + um REF; a Cláusula 6 passou a usar um termo não definido → um achado **TER / ALTERADO**, não um TER entre versões + um TER interno.
- **Não use tipos compostos** como "INT / ALTERADO" para juntar dois problemas. O rótulo de mudança de versão (INCLUÍDO, REMOVIDO, ALTERADO) só complementa o tipo do próprio achado.
- Na comparação de três ou mais documentos, o achado é por item, e o padrão (`A = B ≠ C`) mostra a posição de cada documento.
