# Changelog

Todas as alterações notáveis neste projeto serão documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/),
e este projeto adere ao [Semantic Versioning](https://semver.org/lang/pt-BR/).

## [Unreleased]

## [1.0.0] - 2026-10-15

### Adicionado
- **Persona Monobloco (`persona-auditor-comparativo-documentos.md`)**: Prompt mestre v1.0 para auditoria comparativa entre dois ou mais documentos em qualquer LLM.
- **Skill Anthropic Claude (`auditoria-comparativa-documentos/` e `.skill`)**: Pacote completo de Agent Skill com instruções estruturadas em `SKILL.md`.
- **Scripts Forenses em Python**:
  - `extrair_documento.py`: Extrator para PDF (páginas físicas e detecção de OCR), DOCX (parágrafos lineares, tabelas, comentários e alterações controladas) e TXT/MD.
  - `verificar_citacoes.py`: Verificador mecânico de citações literais caractere a caractere contra os documentos extraídos.
- **Referências Normativas (`references/`)**:
  - `taxonomia.md`: Catálogo dos 10 tipos de achados, regras de desempate, os três estados de ausência e unidade do achado.
  - `severidade.md`: Matriz e âncoras de severidade (Crítica, Alta, Média, Baixa, Informativa) e níveis de confiança.
  - `formato-saida.md`: Especificação do relatório comparativo executivo e formato da planilha de auditoria (.xlsx).
  - `checklist.md`: 18 quesitos eliminatórios de autovalidação pré-entrega.
- **Suíte de Testes e Benchmark (`evals/`)**:
  - Arquivos de teste reais em PDF e DOCX com 9 alterações plantadas e 3 armadilhas de falso positivo.
  - Gabarito v3 e scorecard automatizado.
  - Histórico de 8 execuções de calibração empírica.
- **Documentação Abrangente**:
  - `README.md`: Documentação técnica completa do sistema.
  - `HELP.md`: Guia operacional de uso rápido e histórico de versões.
