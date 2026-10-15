# Formato de saída

Leia antes de escrever a resposta. Use este formato, a menos que o usuário peça outro.

Abra o relatório com o aviso de que os achados são indícios e só devem embasar decisões depois de conferidos por um revisor humano no documento original (campo **Verificado**).

## 1. Identificação e escopo
Tabela de inventário: ID, título, versão, data, emissor, número de páginas, esquema de localização (incluindo página física × numeração impressa, se diferirem) e observações de integridade (páginas com OCR, trechos ilegíveis).

## 2. Relação entre os documentos e premissas
Relação identificada, como ela afeta a classificação, premissas adotadas e o impacto de cada premissa.

## 3. Resumo quantitativo
Contagem de achados por tipo e por severidade. Destaque a **carga de revisão humana**: quantos itens estão em NÃO CLARO (NCL) e REQUER REVISÃO (REV). No máximo um parágrafo de leitura geral.

## 4. Achados detalhados
Ordenados por severidade (Crítica → Informativa) e, dentro da mesma severidade, por tópico. Use este modelo para cada achado:

```markdown
### ACH-001 — [Título curto e descritivo]

- **Tipo:** CTR
- **Severidade:** Alta
- **Confiança:** Alta
- **Tópico:** Prazos de entrega
- **Padrão entre documentos:** A ≠ B  (para 3+ documentos: ex. A = B ≠ C)

**Evidências**
- DOC-A, cláusula 4.2 (p. 7): "O fornecedor deverá entregar os equipamentos em até 30 (trinta) dias corridos [...]"
- DOC-B, cl. 5.1 (par. 24): "A entrega ocorrerá no prazo de 45 dias úteis contados da assinatura."
- **Citação verificada:** Sim (DOC-A e DOC-B)

**Ponto exato da diferença**
| Elemento | DOC-A | DOC-B |
|---|---|---|
| Prazo | 30 dias | 45 dias |
| Tipo de contagem | corridos | úteis |
| Marco inicial | não especificado | assinatura |

**Análise**
[Interpretação: por que é uma contradição e não uma divergência; efeito prático.]

**Impacto / risco**
[O que pode acontecer se não for tratado.]

**Recomendação**
[Ação sugerida: harmonizar, decidir qual prevalece, esclarecer com o responsável, corrigir referência etc.]

**Verificado (revisor):** ☐  ← preenchido por quem revisa, nunca pela IA
```

Para achados do tipo **EXC**, substitua as evidências do documento que não contém o item por:

```markdown
- DOC-B: **NÃO PRESENTE.** Seções verificadas: 3 (Obrigações), 7 (Penalidades), Anexo II. Termos buscados: `multa`, `penalidade`, `sanção`. Conteúdo relacionado: nenhum.
```

Para achados **NCL** e **REV**, indique o estado e o motivo:

```markdown
- DOC-B, §7.3 (p. 15): **NÃO CLARO.** "O atraso poderá ensejar as medidas cabíveis." Trata de consequências do atraso, mas não define multa nem valor.
- DOC-C, p. 9: **REQUER REVISÃO.** citação indisponível: página escaneada com OCR ilegível na região da cláusula 6.
```

## 5. Itens convergentes
Lista compacta dos itens EQV-L e EQV-S, agrupados por tópico, com localizador de cada documento e um trecho literal curto, suficiente para verificação. Nesta seção, o trecho é um **fragmento contíguo** da frase original e dispensa a marcação `[...]`; mesmo assim, precisa ser cópia literal. **Não inclua itens que tenham achado, nem partes deles** (ver `references/taxonomia.md`, seção 4, exclusividade). Exemplo:

```markdown
- **Vigência do contrato** (EQV-S) — DOC-A cl. 2.1: "vigorará por 12 meses" · DOC-B cl. 3: "prazo de vigência de um ano"
```

## 6. Declaração de cobertura e limitações
- Seções e páginas analisadas por documento; páginas com OCR.
- Conteúdo não analisado e motivo (ilegível, fora do escopo, limite de tamanho).
- Resultado da verificação das citações: conferidas, corrigidas, divergentes e indisponíveis, informando separadamente as citações das Evidências e os trechos entre aspas das demais seções.
- Limitações que afetam a confiança da análise.
- **Observações não comparativas**: ambiguidades, lacunas e problemas iguais nos dois documentos, com localizador e, se houver citação, citação literal. Sem ID de achado e fora da contagem de achados.

## 7. Questões em aberto
Perguntas numeradas que exigem decisão ou esclarecimento dos responsáveis pelos documentos, cada uma vinculada aos achados correspondentes (ex.: "Q1 — Qual prazo prevalece? Ref.: ACH-001, ACH-004").

## 8. Exportação para planilha (quando solicitada)
Uma linha por achado (e, opcionalmente, uma por item convergente). Quando a skill `xlsx` estiver disponível, use-a para gerar o arquivo.

| Coluna | Conteúdo |
|---|---|
| ID | ACH-001 |
| Tópico | Prazos de entrega |
| Tipo | CTR, DIV, PAR, EXC, NCL, REV… |
| Estado | Encontrado / NÃO PRESENTE / NÃO CLARO / REQUER REVISÃO (por documento, quando diferir) |
| Severidade | Crítica → Informativa |
| Confiança | Alta / Média / Baixa |
| Padrão | A ≠ B; A = B ≠ C |
| Elemento divergente | Prazo: 30 dias corridos × 45 dias úteis |
| Localizador DOC-X | Uma coluna por documento (cláusula, página) |
| Citação DOC-X | Uma coluna por documento, com o texto literal |
| Citação verificada | Sim / Corrigida / Divergente / Indisponível |
| Análise | Interpretação resumida |
| Recomendação | Ação sugerida |
| **Verificado** | **Em branco.** Preenchido pelo revisor humano após conferir a evidência no documento original. |
| Observações do revisor | Em branco |

Regras da planilha:
- A coluna **Verificado** nunca é preenchida pela IA. Ela separa o que a IA apontou do que uma pessoa confirmou.
- Os valores das citações são idênticos aos do relatório; a planilha não pode resumir ou parafrasear evidências.
- Se as citações deixarem a planilha difícil de ler, mova-as para uma aba ou arquivo complementar de evidências, ligado pelo ID do achado, sem perder nenhuma.
