# Checklist antes da entrega

Etapa 11. Confirme cada item; se algum falhar, corrija antes de responder.

1. Os documentos foram extraídos com localizadores (PDF página a página, DOCX por parágrafo), e as páginas com OCR estão registradas?
2. Todo achado tem evidência com localizador e citação literal de **cada** documento envolvido?
3. A verificação das citações (`scripts/verificar_citacoes.py`, ou manual) foi executada na cobertura exigida, e as citações divergentes ou indisponíveis foram rebaixadas para REV?
4. Todo localizador existe no documento e aponta para o trecho citado?
5. Todo item sem correspondência positiva está em um dos três estados (NÃO PRESENTE, NÃO CLARO, REQUER REVISÃO), e todo NÃO PRESENTE informa onde e como se procurou?
6. Todo achado não equivalente identifica o elemento exato da diferença?
7. Evidência, análise e recomendação estão separadas?
8. A classificação seguiu as **regras de desempate** (especialmente modalidade = CTR, condição acrescentada = DIV, EXC só para tema inteiro ausente) e é coerente com a taxonomia (CTR × DIV, EQV-S × DIV, NCL × REV)?
9. Cada achado trata de **um único item**, sem tipos compostos? Achados foram separados só quando os pares de itens são diferentes, e mudança + defeito no mesmo item viraram um achado só?
10. Equivalências (inclusive realocadas ou renumeradas) estão só em Itens convergentes, e problemas comuns aos dois documentos estão só em Observações não comparativas? Nenhum item com achado (nem parte dele) aparece nos convergentes?
11. Todo trecho entre aspas **fora** das Evidências (Análise, Ponto exato, Impacto, Recomendação, Observações, Questões) é literal? Termos de busca e rótulos estão em formato de código, e não entre aspas?
12. Versão, datas e demais dados de identificação estão no inventário, e só viraram achado quando uma regra do documento os usa como marco?
13. A relação entre os documentos e as premissas foram declaradas?
14. Todo conteúdo relevante foi classificado em algum achado ou nos itens convergentes, ou aparece na declaração de cobertura?
15. Não há achados duplicados descrevendo o mesmo item?
16. A severidade de cada achado foi escolhida pelas **âncoras de severidade**, avaliando o achado isoladamente (efeito combinado só na Leitura geral), e a confiança está justificada?
17. As verificações transversais (contradição interna, terminologia, referências, metadados) foram executadas?
18. O campo e a coluna **Verificado** estão em branco, reservados ao revisor?

## O que não fazer

- reduzir a análise a uma lista de "diferenças" sem localização e evidência;
- omitir itens iguais;
- comparar apenas pela estrutura ou numeração dos documentos;
- tratar diferença de redação como diferença de conteúdo, nem o contrário, sem justificar;
- escolher um vencedor entre documentos sem base na relação definida ou em regra de precedência declarada;
- misturar paráfrase com citação literal;
- colocar entre aspas, em qualquer seção, um texto que não seja cópia literal do documento;
- juntar dois problemas distintos num mesmo achado ou usar tipos compostos;
- registrar como achado uma equivalência (mesmo realocada) ou um problema igual nos dois documentos;
- entregar um achado com classificação firme sustentado por citação reconstruída ou não verificada;
- deixar um item sem correspondência em branco ou com um "não encontrado" genérico;
- extrair PDFs sem marcar as páginas ou DOCX sem numerar os parágrafos;
- preencher o campo ou a coluna **Verificado**;
- apresentar análise parcial como completa;
- usar conhecimento externo como se fosse evidência documental.
