# Auditoria Comparativa de Documentos

> **Sistema Especialista em Análise Comparativa e Auditoria Documental com Rastreabilidade Forense, Evidência Literal e Verificação Mecânica de Citações.**

[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](VERSION)
[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Format Support](https://img.shields.io/badge/formats-PDF%20%7C%20DOCX%20%7C%20TXT%20%7C%20MD-orange.svg)](#)
[![Validation](https://img.shields.io/badge/citation--verification-100%25%20pass-brightgreen.svg)](#)
[![Anthropic Claude Skill](https://img.shields.io/badge/Claude%20Skill-1.0-purple.svg)](#)

---

## Sumário

- [Visão Geral](#visão-geral)
- [Principais Funcionalidades](#principais-funcionalidades)
- [Estrutura do Repositório](#estrutura-do-repositório)
- [Pilha Tecnológica (Tech Stack)](#pilha-tecnológica-tech-stack)
- [Pré-requisitos](#pré-requisitos)
- [Guia de Início Rápido (Getting Started)](#guia-de-início-rápido-getting-started)
  - [1. Clonar e Configurar o Ambiente](#1-clonar-e-configurar-o-ambiente)
  - [2. Instalação das Dependências](#2-instalação-das-dependências)
  - [3. Extração com Localizadores](#3-extração-com-localizadores)
  - [4. Execução da Auditoria](#4-execução-da-auditoria)
  - [5. Verificação Mecânica das Citações](#5-verificação-mecânica-das-citações)
- [Metodologia e Arquitetura do Sistema](#metodologia-e-arquitetura-do-sistema)
  - [Fluxo de Dados e Ciclo de Vida da Auditoria](#fluxo-de-dados-e-ciclo-de-vida-da-auditoria)
  - [As 11 Etapas da Metodologia de Auditoria](#as-11-etapas-da-metodologia-de-auditoria)
  - [Regras Fundamentais de Evidência](#regras-fundamentais-de-evidência)
  - [Taxonomia de Achados (Classificação)](#taxonomia-de-achados-classificação)
  - [Os Três Estados de "Não Encontrado"](#os-três-estados-de-não-encontrado)
  - [Regras de Desempate e Unidade do Achado](#regras-de-desempate-e-unidade-do-achado)
  - [Matriz e Âncoras de Severidade](#matriz-e-âncoras-de-severidade)
- [Formas de Implantação e Uso](#formas-de-implantação-e-uso)
  - [Opção 1: Skill Nativa no Claude Code / Claude Desktop](#opção-1-skill-nativa-no-claude-code--claude-desktop)
  - [Opção 2: Persona Prompt em Projetos Claude.ai / Web](#opção-2-persona-prompt-em-projetos-claudeai--web)
  - [Opção 3: Outros LLMs (ChatGPT, Gemini, Copilot)](#opção-3-outros-llms-chatgpt-gemini-copilot)
  - [Opção 4: Automação via API e Pipelines CI/CD](#opção-4-automação-via-api-e-pipelines-cicd)
- [Referência dos Scripts e Parâmetros de Linha de Comando](#referência-dos-scripts-e-parâmetros-de-linha-de-comando)
  - [`extrair_documento.py`](#extrair_documentopy)
  - [`verificar_citacoes.py`](#verificar_citacoespy)
- [Formato do Relatório de Saída](#formato-do-relatório-de-saída)
  - [Estrutura Padrão em Markdown](#estrutura-padrão-em-markdown)
  - [Exportação para Planilha de Acompanhamento (.xlsx)](#exportação-para-planilha-de-acompanhamento-xlsx)
- [Testes, Avaliação e Benchmark (Evals)](#testes-avaliação-e-benchmark-evals)
  - [Bateria de Regressão e Validação](#bateria-de-regressão-e-validação)
  - [Casos de Teste Padronizados (`evals.json`)](#casos-de-teste-padronizados-evalsjson)
- [Solução de Problemas (Troubleshooting)](#solução-de-problemas-troubleshooting)
- [Contribuição](#contribuição)
- [Licença](#licença)

---

## Visão Geral

O projeto **Auditoria Comparativa de Documentos** foi concebido para transformar a forma como analistas jurídicos, engenheiros de requisitos, gestores de contratos e auditores comparam documentos críticos (contratos, aditivos contratuais, especificações técnicas, PRDs, editais, propostas comerciais, políticas e normas corporativas).

Ao contrário de ferramentas tradicionais de *diff* baseadas exclusivamente em correspondência sintática ou de texto corrido, este sistema atua como um **Auditor Sênior Especializado**:
1. **Compara significado e força normativa**, identificando sutilezas semânticas onde redações diferentes expressam a mesma obrigação, ou onde alterações de uma única palavra ("deve" $\leftrightarrow$ "pode") invertem o risco operacional.
2. **Garante rastreabilidade forense absoluta**: todo achado possui localização física exata (página do PDF, parágrafo do DOCX, célula de tabela) e citação literal contígua verificada caractere a caractere.
3. **Elimina alucinações e distorções**: através de verificação mecânica via script Python, nenhuma citação fabricada ou aproximada passa para o relatório final.
4. **Reserva a validação final para o humano**: os achados são indícios organizados que aceleram em até 80% o tempo de análise técnica, com o campo **Verificado (revisor)** estritamente reservado para conferência humana.

---

## Principais Funcionalidades

- **Extração Rastreável Multi-formato**:
  - **PDF**: Segmentação por página física (`=== DOC-A · Página N ===`), detecção de páginas escaneadas (necessidade de OCR) e extração de metadados.
  - **DOCX**: Numeração linear contínua de parágrafos (`[par. N]`), extração isolada de células de tabelas (`[Tabela T, linha L, col. C]`), metadados e detecção forense de **alterações controladas** (*track changes* — inserções e exclusões com autor e data) e comentários.
  - **TXT / Markdown**: Indexação sequencial de blocos textuais (`[par. N]`).
- **Taxonomia Padronizada e Calibrada**:
  - 10 códigos unificados de classificação: Contradição (`CTR`), Divergência (`DIV`), Cobertura Parcial (`PAR`), Exclusivo/Não Presente (`EXC`), Não Claro (`NCL`), Requer Revisão (`REV`), Inconsistência Terminológica (`TER`), Contradição Interna (`INT`), Referência Quebrada (`REF`) e Equivalência (`EQV-L` / `EQV-S`).
- **Diferenciação Estrita de Ausências**:
  - Distingue com precisão cirúrgica entre **NÃO PRESENTE** (documento foi lido integralmente e não aborda o tema), **NÃO CLARO** (texto ambíguo ou vago) e **REQUER REVISÃO** (julgamento humano obrigatório ou texto ilegível).
- **Verificação Mecânica Contínua (`verificar_citacoes.py`)**:
  - Script determinístico que varre o rascunho da análise, extrai todos os fragmentos entre aspas e valida se o texto reside exatamente no localizador e no documento informados.
- **Exportação Dual**:
  - Relatório detalhado em Markdown com inventário, tabela comparativa lado a lado por elemento divergente, impacto, recomendações e questões abertas.
  - Planilha estruturada (.xlsx) com uma linha por achado e coluna `Verificado` vazia pronta para triagem humana.

---

## Estrutura do Repositório

```
auditoria-comparativa-documentos/
├── README.md                                    # Esta documentação completa do projeto
├── HELP.md                                      # Guia operacional de uso rápido e histórico de versões
├── persona-auditor-comparativo-documentos.md   # Persona completa v1.0 (prompt monobloco para LLMs)
├── auditoria-comparativa-documentos.skill      # Pacote ZIP instalável no Claude Code e claude.ai
│
└── auditoria-comparativa-documentos/            # Código-fonte da Agent Skill
    ├── SKILL.md                                 # Definição e instruções mestras da skill
    ├── references/                              # Conhecimento normativo e regras da metodologia
    │   ├── checklist.md                         # Checklist de autovalidação de 18 itens pré-entrega
    │   ├── formato-saida.md                     # Template do relatório executivo e esquema da planilha
    │   ├── severidade.md                        # Âncoras e matriz de impacto (Crítica a Informativa)
    │   └── taxonomia.md                         # Catálogo de tipos, desempate, estados e unidade
    ├── scripts/                                 # Scripts utilitários Python
    │   ├── extrair_documento.py                 # Extrator de PDFs, DOCX e TXT com localizadores
    │   └── verificar_citacoes.py                # Verificador mecânico de citações literais
    └── evals/                                   # Conjunto de testes, benchmarks e validação
        ├── README.md                            # Guia de execução dos testes de regressão
        ├── evals.json                           # Casos de avaliação da metodologia
        ├── files/                               # Documentos de teste (PDF v1 e DOCX v2)
        ├── gabarito/                            # Planilha de gabarito v3 e scorecard
        └── referencias/                         # Histórico de execuções de calibração (Execucao1 a 8)
```

---

## Pilha Tecnológica (Tech Stack)

| Componente | Tecnologia | Versão Mínima | Descrição |
|---|---|---|---|
| **Linguagem Principal** | Python | 3.9+ (Recomendado 3.10+) | Execução dos scripts de extração, verificação e automação |
| **Manipulação de PDF** | `pypdf` | 4.0+ | Extração página a página, metadados e detecção de scans |
| **Manipulação de DOCX** | `python-docx` | 1.1+ | Extração de parágrafos, tabelas, comentários e track changes |
| **Geração de Planilhas** | `openpyxl` | 3.1+ | Geração da matriz de auditoria em formato Microsoft Excel |
| **IA / LLM Host** | Claude / GPT-4o / Gemini 1.5+ | - | Motores cognitivos compatíveis com a persona e metodologia |
| **Padrão de Skill** | Anthropic Agent Skills | v1.0 | Formato padronizado de habilidades para Claude Desktop e Code |

---

## Pré-requisitos

1. **Interpretador Python**:
   - Python 3.9 ou superior instalado e configurado no PATH do sistema.
   ```bash
   python --version
   ```

2. **Gerenciador de Pacotes `pip`**:
   - Atualizado para instalação segura das bibliotecas de parsing.

3. **Ambiente LLM (opções suportadas)**:
   - **Claude Code CLI** ou **Claude Desktop** (com suporte a Skills ativado);
   - Ou acesso à web interface de **Claude.ai**, **ChatGPT**, **Google Gemini** ou **Microsoft Copilot**;
   - Ou credenciais de API (Anthropic, OpenAI, Google) para execuções automatizadas em lote.

---

## Guia de Início Rápido (Getting Started)

Siga este passo a passo para auditar um par de documentos em menos de 5 minutos.

### 1. Clonar e Configurar o Ambiente

```bash
# Clonar o repositório
git clone https://github.com/seu-usuario/auditoria-comparativa-documentos.git
cd auditoria-comparativa-documentos

# (Opcional, porém recomendado) Criar e ativar um ambiente virtual
python -m venv .venv

# No Linux/macOS:
source .venv/bin/activate
# No Windows (PowerShell):
.venv\Scripts\Activate.ps1
# No Windows (CMD):
.venv\Scripts\activate.bat
```

### 2. Instalação das Dependências

Instale as bibliotecas necessárias para extração documental e geração de planilhas:

```bash
pip install pypdf python-docx openpyxl
```

### 3. Extração com Localizadores

Sempre converta os arquivos de entrada antes de submetê-los à análise. Isso assegura que as referências de página e parágrafo sejam determinísticas:

```bash
# Extração do documento base (DOC-A em PDF)
python auditoria-comparativa-documentos/scripts/extrair_documento.py caminho/para/contrato_v1.pdf --id DOC-A --saida extraido_DOC-A.md

# Extração do documento avaliado (DOC-B em DOCX)
python auditoria-comparativa-documentos/scripts/extrair_documento.py caminho/para/contrato_v2.docx --id DOC-B --saida extraido_DOC-B.md
```

### 4. Execução da Auditoria

Se você estiver utilizando a **Skill no Claude**, basta anexar os arquivos e solicitar a comparação no chat.

Se estiver utilizando a **Persona (Prompt)** em qualquer IA, copie o conteúdo de `persona-auditor-comparativo-documentos.md` como prompt de sistema e envie a mensagem de tarefa estruturada:

```markdown
## Tarefa
Compare os documentos anexos seguindo integralmente a sua metodologia de auditoria comparativa.

## Documentos
- DOC-A: extraido_DOC-A.md — Contrato Original v1.0
- DOC-B: extraido_DOC-B.md — Proposta de Renovação com Aditivos v2.0

## Relação
Versões (DOC-A é a versão vigente e DOC-B é a nova proposta).

## Foco
Análise completa de cláusulas operacionais, prazos, penalidades e garantias.

## Saída
Use o formato de saída padrão (achados detalhados) e gere o arquivo Markdown.
```

Salve o resultado retornado pelo modelo como `analise_rascunho.md`.

### 5. Verificação Mecânica das Citações

Rode o script validador contra o relatório gerado:

```bash
python auditoria-comparativa-documentos/scripts/verificar_citacoes.py analise_rascunho.md --doc DOC-A=extraido_DOC-A.md --doc DOC-B=extraido_DOC-B.md
```

**Exemplo de saída de sucesso:**
```text
Trechos entre aspas conferidos: 24
  OK: 24
  OK_SEM_LOCALIZADOR: 0
  LOCALIZADOR_DIVERGENTE: 0
  DOC_DIVERGENTE: 0
  NAO_ENCONTRADA: 0
```

Se houver apontamentos de `NAO_ENCONTRADA` ou `LOCALIZADOR_DIVERGENTE`, repasse o log para a IA corrigir os trechos ou proceda com o rebaixamento para o estado `REV`.

---

## Metodologia e Arquitetura do Sistema

### Fluxo de Dados e Ciclo de Vida da Auditoria

```
┌────────────────────────────────┐         ┌────────────────────────────────┐
│   Documento Original (PDF)     │         │   Documento Avaliado (DOCX)    │
└───────────────┬────────────────┘         └───────────────┬────────────────┘
                │                                          │
                ▼                                          ▼
     [ extrair_documento.py ]                   [ extrair_documento.py ]
    • Páginas Físicas (p. N)                   • Parágrafos ([par. N])
    • Alertas de OCR                           • Tabelas ([Tabela, L, C])
    • Metadados brutos                         • Track Changes & Comentários
                │                                          │
                └────────────────────┬─────────────────────┘
                                     │
                                     ▼
                ┌──────────────────────────────────────────┐
                │        Arquivos Extraídos (.md)          │
                │        extraido_DOC-A / extraido_DOC-B   │
                └────────────────────┬─────────────────────┘
                                     │
                                     ▼
                ┌──────────────────────────────────────────┐
                │          Motor Cognitivo (LLM)           │
                │   • Skill Claude ou Persona Prompt       │
                │   • Leitura de Taxonomia e Severidade    │
                │   • Decomposição Atômica e Alinhamento   │
                │   • Detecção de Falhas Transversais      │
                └────────────────────┬─────────────────────┘
                                     │
                                     ▼
                ┌──────────────────────────────────────────┐
                │        Rascunho da Análise (.md)         │
                └────────────────────┬─────────────────────┘
                                     │
                                     ▼
                ┌──────────────────────────────────────────┐
                │         [ verificar_citacoes.py ]        │
                │   • Validação caractere a caractere      │
                │   • Classificação de consistência        │
                └────────────────────┬─────────────────────┘
                                     │
                   ┌─────────────────┴─────────────────┐
                   │                                   │
              (Problemas > 0)                    (100% Validado)
                   │                                   │
                   ▼                                   ▼
        [ Correção Iterativa ]            [ Checklist Pré-entrega ]
        (Ajuste de localizadores               (references/checklist.md)
         ou rebaixamento REV)                          │
                                                       ▼
                                          ┌─────────────────────────────┐
                                          │     Relatório Final         │
                                          │  • Markdown Executivo       │
                                          │  • Planilha de Auditoria    │
                                          │  • "Verificado: [ ]" Vazio  │
                                          └─────────────────────────────┘
```

---

### As 11 Etapas da Metodologia de Auditoria

A análise segue rigorosamente um processo estadiado em 11 passos ordenados:

1. **Inventário**: Mapeamento dos metadados, títulos, datas, versões, número de páginas e esquema de indexação física de cada documento.
2. **Determinação da Relação e Premissas**: Caracterização da relação lógica entre os documentos:
   - *Versões* ($v1 \times v2$): alterações, inclusões e exclusões.
   - *Referência $\times$ Avaliado*: a referência prevalece; ausências no avaliado são não-conformidades.
   - *Pares Independentes*: comparação simétrica entre propostas concorrentes.
   - *Hierárquicos*: ordenação normativa (Lei $\rightarrow$ Política $\rightarrow$ Procedimento).
3. **Eixo de Comparação**: Criação de tópicos pela união de todos os temas existentes, assegurando que conteúdos presentes em apenas um documento nunca sejam omitidos.
4. **Decomposição e Alinhamento Atômico**: Fracionamento em obrigações ou regras unitárias, alinhadas pelo significado, e não pela numeração de cláusulas.
5. **Classificação Conforme Taxonomia**: Aplicação de tipo único por achado baseando-se em `references/taxonomia.md`.
6. **Isolamento do Ponto Exato**: Identificação do elemento divergente (valor, prazo, modalidade, condição, responsável).
7. **Verificações Transversais**: Varredura ativa em busca de contradições internas no mesmo documento, referências quebradas para anexos inexistentes e mudanças de terminologia.
8. **Avaliação de Severidade, Impacto e Confiança**: Enquadramento nas âncoras objetivas de `references/severidade.md`.
9. **Reconciliação de Cobertura**: Declaração explícita de tudo o que foi analisado e do que ficou de fora.
10. **Verificação Mecânica de Citações**: Execução de `verificar_citacoes.py` contra o texto original.
11. **Autovalidação (Checklist)**: Validação dos 18 quesitos de integridade documental de `references/checklist.md`.

---

### Regras Fundamentais de Evidência

As regras de evidência são mandatórias e eliminatórias:

1. **Formato Padrão de Citação**:
   $$\text{DOC-X, [localizador]: "citação literal"}$$
2. **Localizador Obrigatório**: Número formal da cláusula ou artigo acompanhado da **página física** do PDF (1ª página do arquivo = 1) ou do **número do parágrafo** no DOCX (`[par. N]`). É expressamente proibido estimar ou inventar localizadores.
3. **Fidelidade Literal Absoluta**: O texto entre aspas deve ser cópia fiel caractere a caractere. Supressões com `[...]` são permitidas apenas nas extremidades da citação. Parafraseamento nunca deve receber aspas.
4. **Reserva Exclusiva de Aspas**: Aspas duplas (`"..."`) ou tipográficas (`“...”`) são estritamente reservadas para citações de documentos. Termos de busca, radicais ou rótulos de campos utilizam blocos de código (ex: `multa`, `indenização`, `Verificado`).
5. **Simetria de Evidências**: Todo achado comparativo deve apresentar evidências literais de **todos** os documentos confrontados.
6. **Comprovação de Ausência**: Para classificar um item como `NÃO PRESENTE`, é obrigatório declarar as seções vasculhadas e os termos de busca consultados.

---

### Taxonomia de Achados (Classificação)

| Código | Nome | Definição | Exemplo Prático |
|---|---|---|---|
| **EQV-L** | Equivalente Literal | Texto idêntico ou com divergências meramente ortográficas ou tipográficas. | Mesma cláusula copiada entre instrumentos. |
| **EQV-S** | Equivalente Semântico | Redações distintas, mas com exatamente o mesmo efeito jurídico e prático. | "em até 30 dias" $\times$ "no prazo máximo de trinta dias". |
| **CTR** | Contradição | Disposições inconciliáveis que não podem ser cumpridas simultaneamente. | Prazo de 30 dias $\times$ 45 dias; Obrigação ("deve") $\times$ Faculdade ("pode"). |
| **DIV** | Divergência | Disposições materiais que podem coexistir, mas impõem condições ou efeitos adicionais. | Exigência de aprovação pelo Gestor $\times$ Aprovação pelo Gestor **e** pelo Jurídico. |
| **PAR** | Cobertura Parcial | Um documento trata o tema de maneira exaustiva, enquanto o outro cobre fração limitada. | Lista de 5 entregáveis obrigatórios $\times$ Lista contendo apenas 3. |
| **EXC** | Exclusivo / Não Presente | Tema presente em um instrumento e comprovadamente ausente no outro. | Cláusula de SLA presente no DOC-A e ausente no DOC-B. |
| **NCL** | Não Claro | O tema é mencionado, porém de forma vaga, ambígua ou incompleta. | Substituição de penalidade tarifada de 2% por "medidas legais cabíveis". |
| **REV** | Requer Revisão | Exige julgamento de mérito humano ou evidência com citação ilegível/divergente. | Trecho em página escaneada com OCR corrompido. |
| **TER** | Inconsistência Terminológica | Sinônimos conflitantes ou polissemia semântica entre instrumentos. | "Contratante" em DOC-A $\times$ "Cliente" em DOC-B sem definição uniforme. |
| **INT** | Contradição Interna | Conflito normativo interno entre dispositivos do **mesmo** documento. | Cláusula 4.3 prevê 5 dias, mas Anexo II do mesmo contrato prevê 10 dias. |
| **REF** | Referência Quebrada | Citação a anexo, cláusula ou documento que não existe ou está incorreto. | Dispositivo remete a obrigações dispostas no "Anexo IV" inexistente. |

---

### Os Três Estados de "Não Encontrado"

Quando um item procurado não puder ser correspondido positivamente, adote um destes três estados categóricos:

```
                                  [ BUSCA DO ITEM ]
                                          │
                     ┌────────────────────┼────────────────────┐
                     ▼                    ▼                    ▼
             [ NÃO PRESENTE ]       [ NÃO CLARO ]      [ REQUER REVISÃO ]
             ────────────────       ─────────────      ──────────────────
             O tema inexiste no     O tema existe,     Existe texto, mas a
             documento após busca   mas a redação é    definição depende de
             completa declarada.    vaga ou ambígua.   julgamento humano ou
                                                       OCR ilegível.
             Classificação: EXC     Classificação: NCL Classificação: REV
```

---

### Regras de Desempate e Unidade do Achado

- **Modalidade Normativa Prevalece**: A alteração entre imposição ("deve"), faculdade ("pode") e vedação ("é vedado") é **sempre Contradição (`CTR`)**, independentemente de o restante do texto ser idêntico.
- **Valores e Prazos Objetivos**: Qualquer divergência em números, índices, moedas, prazos (dias corridos $\times$ úteis) e marcos iniciais é classificada como **`CTR`**.
- **Adição de Condições Procedimentais**: Condição extra adicionada a uma obrigação já existente classifica-se como **Divergência (`DIV`)** (com o qualificador `INCLUÍDO`, se forem versões).
- **Tema Exclusivo Real**: Só utilize **`EXC`** se o tema como um todo não possuir nenhum correlato após varredura exaustiva.
- **Unidade Estrita do Achado**:
  - Cada achado avalia **um único item comparado** (ou par de trechos em `INT` e `REF`).
  - Mudança de versão somada a defeito no mesmo item gera **apenas um achado consolidado** (ex.: cláusula 12.1 alterada para citar Anexo IV inexistente gera um único achado `REF / ALTERADO`).
  - **Exclusividade**: um item classificado como achado **nunca** pode figurar na lista de Itens Convergentes.

---

### Matriz e Âncoras de Severidade

A severidade reflete o impacto prático do achado e é estritamente independente da confiança:

| Severidade | Âncoras de Enquadramento | Exemplo Típico |
|---|---|---|
| **Crítica** | Afeta elemento essencial (partes, objeto principal, preço total, vigência e validade). Remove obrigação legal imperativa. Impossibilita o cumprimento conjunto. | DOC-A estipula preço global de R$ 100.000,00 e DOC-B estipula R$ 150.000,00 para o mesmo escopo. |
| **Alta** | Altera obrigações materiais, prazos de atendimento, penalidades, limites de responsabilidade. Remove ou enfraquece garantias, seguros ou prerrogativas de auditoria. | Prazo de atendimento alterado de 24h para 72h; exclusão da exigência de apólice de seguro de responsabilidade civil. |
| **Média** | Acrescenta etapas burocráticas ou condicionantes procedimentais. Gera inconsistência terminológica inferível pelo contexto. | Exigência de aviso prévio por carta registrada com AR em vez de simples e-mail. |
| **Baixa** | Ajustes de redação, clarificações sem alteração de escopo, reordenação de cláusulas com remissões preservadas. | Inclusão de exemplos ilustrativos para um critério técnico já consolidado. |
| **Informativa** | Registro de datas, versões de sistema e metadados que não produzem efeito normativo direto. | Atualização do número de versão no cabeçalho do documento. |

---

## Formas de Implantação e Uso

### Opção 1: Skill Nativa no Claude Code / Claude Desktop

A forma mais recomendada para usuários do ecossistema Anthropic Claude.

#### Instalação no Claude Code (Global):
Descompacte o arquivo `.skill` diretamente no diretório de skills do usuário:

```bash
# Linux / macOS
unzip auditoria-comparativa-documentos.skill -d ~/.claude/skills/

# Windows (PowerShell)
Expand-Archive -Path "auditoria-comparativa-documentos.skill" -DestinationPath "$HOME\.claude\skills\"
```

#### Instalação no Claude Desktop / claude.ai:
1. Abra as **Configurações** do Claude Desktop.
2. Navegue até a seção de **Skills / Capacidades**.
3. Faça o upload do arquivo `auditoria-comparativa-documentos.skill`.

---

### Opção 2: Persona Prompt em Projetos Claude.ai / Web

Ideal para uso corporativo em projetos compartilhados no `claude.ai`:
1. Crie um novo **Projeto** no Claude.ai.
2. Nas **Instruções do Projeto (System Prompt)**, copie e cole a íntegra do arquivo [`persona-auditor-comparativo-documentos.md`](persona-auditor-comparativo-documentos.md).
3. Faça upload dos arquivos de conhecimento (`taxonomia.md`, `severidade.md`, `formato-saida.md`, `checklist.md`) na seção de arquivos do projeto.
4. Inicie qualquer conversa fornecendo os documentos extraídos e a tarefa estruturada.

---

### Opção 3: Outros LLMs (ChatGPT, Gemini, Copilot)

Para utilizar no **OpenAI ChatGPT (Custom GPT)**, **Google Gemini (Gems)** ou **Microsoft Copilot Studio**:

1. **Campo de Instruções**: Cole o conteúdo de `SKILL.md` (ou de `persona-auditor-comparativo-documentos.md`).
2. **Base de Conhecimento**: Faça upload dos arquivos presentes em `auditoria-comparativa-documentos/references/`.
3. **Execução de Código**: Se a plataforma dispuser de interpretador de código integrado (ex: Advanced Data Analysis no ChatGPT), faça upload também dos scripts `extrair_documento.py` e `verificar_citacoes.py`.

---

### Opção 4: Automação via API e Pipelines CI/CD

Você pode integrar a auditoria comparativa diretamente em esteiras corporativas (GitLab CI, GitHub Actions, AWS Lambda):

```python
import subprocess
from pathlib import Path
from anthropic import Anthropic

client = Anthropic()

# 1. Extração determinística
subprocess.run(["python", "auditoria-comparativa-documentos/scripts/extrair_documento.py", "docs/v1.pdf", "--id", "DOC-A", "--saida", "tmp_A.md"], check=True)
subprocess.run(["python", "auditoria-comparativa-documentos/scripts/extrair_documento.py", "docs/v2.docx", "--id", "DOC-B", "--saida", "tmp_B.md"], check=True)

texto_A = Path("tmp_A.md").read_text(encoding="utf-8")
texto_B = Path("tmp_B.md").read_text(encoding="utf-8")
system_prompt = Path("persona-auditor-comparativo-documentos.md").read_text(encoding="utf-8")

# 2. Chamada à API
user_message = f"""
## Tarefa: Realizar auditoria comparativa entre DOC-A e DOC-B.
## Relação: Versões (DOC-A vigente x DOC-B proposta).

### DOC-A:
{texto_A}

### DOC-B:
{texto_B}
"""

response = client.messages.create(
    model="claude-3-7-sonnet-20250219",
    max_tokens=4000,
    system=system_prompt,
    messages=[{"role": "user", "content": user_message}]
)

Path("rascunho.md").write_text(response.content[0].text, encoding="utf-8")

# 3. Verificação mecânica
resultado = subprocess.run([
    "python", "auditoria-comparativa-documentos/scripts/verificar_citacoes.py",
    "rascunho.md", "--doc", "DOC-A=tmp_A.md", "--doc", "DOC-B=tmp_B.md"
])

if resultado.returncode != 0:
    print("Aviso: Falhas de citação detectadas no rascunho. Executar repasse corretivo.")
```

---

## Referência dos Scripts e Parâmetros de Linha de Comando

### `extrair_documento.py`

Extrai textos de documentos preservando marcações físicas e estruturais necessárias para a auditoria.

```bash
python extrair_documento.py <arquivo> --id <DOC-ID> [--saida <caminho_saida>]
```

#### Argumentos:
| Parâmetro | Obrigatório | Tipo | Descrição |
|---|---|---|---|
| `arquivo` | Sim | Posicional | Caminho para o arquivo `.pdf`, `.docx`, `.txt` ou `.md`. |
| `--id` | Sim | String | Identificador a ser associado ao documento (ex: `DOC-A`, `DOC-B`). |
| `--saida` | Não | Caminho | Nome do arquivo de saída. Padrão: `extraido_<ID>.md` no mesmo diretório. |

#### Comportamento por Formato:
- **PDF**: Emite delimitadores `=== DOC-X · Página N ===`. Identifica páginas com menos de 20 caracteres como prováveis páginas escaneadas e insere advertência para aplicação de OCR.
- **DOCX**: Numera parágrafos contínuos do corpo como `[par. N]`. Converte tabelas para `[Tabela T, linha L, col. C]`. Captura alterações controladas (*track changes*) informando tipo (`INSERIDO`/`EXCLUÍDO`), autor e data.
- **TXT/MD**: Mapeia blocos separados por linhas em branco como `[par. N]`.

---

### `verificar_citacoes.py`

Analisa mecanicamente o relatório Markdown e verifica cada trecho entre aspas contra os arquivos extraídos.

```bash
python verificar_citacoes.py <analise.md> --doc <DOC-ID=arquivo_extraido.md> [--todos]
```

#### Argumentos:
| Parâmetro | Obrigatório | Tipo | Descrição |
|---|---|---|---|
| `analise` | Sim | Posicional | Caminho do relatório de auditoria gerado pelo LLM. |
| `--doc` | Sim | Múltiplo | Mapeamento no formato `DOC-ID=caminho_extraido.md`. Pode ser repetido quantas vezes forem necessárias. |
| `--todos` | Não | Flag | Exibe na saída do terminal inclusive as citações classificadas com status `OK`. |

#### Códigos de Retorno do Script:
- `0`: Sucesso total. Todas as citações existem nos localizadores indicados.
- `1`: Erro detectado. Existem citações com status `NAO_ENCONTRADA`, `DOC_DIVERGENTE` ou `LOCALIZADOR_DIVERGENTE`.

#### Classificação de Citações:
- `OK`: Texto literal idêntico localizado no exato localizador indicado.
- `OK_SEM_LOCALIZADOR`: O texto existe no documento, mas o localizador não pôde ser verificado via regex (necessita checagem humana visual).
- `LOCALIZADOR_DIVERGENTE`: O texto existe no documento, porém em página ou parágrafo distinto daquele indicado no relatório.
- `DOC_DIVERGENTE`: O trecho citado existe, mas pertence a outro documento da análise.
- `NAO_ENCONTRADA`: O texto entre aspas não existe literalmente em nenhum arquivo extraído (alucinação ou paráfrase indevida).

---

## Formato do Relatório de Saída

### Estrutura Padrão em Markdown

O relatório padrão é composto por 7 blocos principais:

1. **Aviso de Responsabilidade e Metodologia**: Alerta inicial indicando que os achados constituem indícios e que o campo `Verificado` é de preenchimento exclusivo do revisor humano.
2. **Identificação e Escopo**: Tabela de inventário com IDs, formatos, versões, datas, quantidades de páginas e conformidade de integridade.
3. **Relação entre Documentos e Premissas**: Justificativa da relação adotada e impacto de desvios de premissa.
4. **Resumo Quantitativo**: Tabela consolidada de achados por tipo versus severidade, destacando a carga de revisão (`NCL` + `REV`).
5. **Achados Detalhados**: Cartões individuais ordenados por severidade decrescente com a seguinte anatomia:

```markdown
### ACH-001 — Prazo de Notificação Prévia de Rescisão

- **Tipo:** CTR / ALTERADO
- **Severidade:** Alta
- **Confiança:** Alta
- **Tópico:** Rescisão Contratual
- **Padrão entre documentos:** A ≠ B

**Evidências**
- DOC-A, cláusula 14.1 (p. 6): "Qualquer das partes poderá rescindir o presente instrumento mediante aviso prévio de 30 (trinta) dias [...]"
- DOC-B, cl. 15.1 (par. 42): "A rescisão imotivada exigirá notificação expressa com antecedência mínima de 60 (sessenta) dias."
- **Citação verificada:** Sim (DOC-A e DOC-B)

**Ponto exato da diferença**
| Elemento | DOC-A | DOC-B |
|---|---|---|
| Prazo de aviso prévio | 30 dias | 60 dias |
| Natureza da rescisão | Qualquer rescisão | Rescisão imotivada |

**Análise**
Divergência inconciliável de prazo entre as duas versões (CTR). Na vigência de DOC-B, o prazo para desligamento sem justa causa dobra, impactando o planejamento de transição de fornecedor.

**Impacto / risco**
Risco de prorrogação forçada de custos contratuais por mais 30 dias caso a empresa decida descontinuar o serviço.

**Recomendação**
Avaliar junto à área demandante se a ampliação para 60 dias atende ao cronograma operacional ou se deve ser mantido o padrão de 30 dias da versão vigente.

**Verificado (revisor):** ☐
```

6. **Itens Convergentes**: Relação compacta de dispositivos idênticos (`EQV-L`) ou semanticamente equivalentes (`EQV-S`), incluindo anotações de realocação física de cláusulas.
7. **Declaração de Cobertura, Limitações e Questões em Aberto**: Transparência sobre páginas analisadas, ocorrências de OCR e lista numerada de dúvidas para decisão dos gestores de negócio.

---

### Exportação para Planilha de Acompanhamento (.xlsx)

Quando solicitado, a skill ou a persona gera uma planilha contendo as seguintes colunas padronizadas:

| Coluna | Descrição |
|---|---|
| `ID` | Identificador único do achado (ex: `ACH-001`). |
| `Tópico` | Agrupador temático (ex: Prazos, Penalidades, SLA). |
| `Tipo` | Código taxonômico (`CTR`, `DIV`, `EXC`, etc.). |
| `Severidade` | Classificação de risco (`Crítica`, `Alta`, `Média`, `Baixa`, `Informativa`). |
| `Confiança` | Nível de certeza da evidência (`Alta`, `Média`, `Baixa`). |
| `Padrão` | Comportamento multi-documental (`A ≠ B`, `A = B ≠ C`). |
| `Elemento Divergente` | Resumo objetivo do elemento discrepante. |
| `Localizador DOC-A` | Cláusula e página física do primeiro documento. |
| `Citação DOC-A` | Texto literal correspondente extraído de DOC-A. |
| `Localizador DOC-B` | Cláusula e parágrafo/página do segundo documento. |
| `Citação DOC-B` | Texto literal correspondente extraído de DOC-B. |
| `Citação Verificada` | Status mecânico (`Sim`, `Corrigida`, `Divergente`). |
| `Análise` | Síntese do efeito normativo da diferença. |
| `Recomendação` | Ação prática recomendada para o revisor. |
| **Verificado** | **Coluna estritamente vazia**, destinada ao carimbo ou "X" do revisor humano. |

---

## Testes, Avaliação e Benchmark (Evals)

O repositório conta com uma suíte de avaliação empírica calibrada durante o desenvolvimento da metodologia (diretório `auditoria-comparativa-documentos/evals/`).

### Bateria de Regressão e Validação

Para validar o funcionamento do verificador mecânico e comparar a precisão das análises, utilize os documentos de teste fornecidos:

```bash
# 1. Extração dos contratos fictícios do kit de avaliação
python auditoria-comparativa-documentos/scripts/extrair_documento.py auditoria-comparativa-documentos/evals/files/DOC-A_contrato_v1.pdf --id DOC-A --saida /tmp/DOC-A.md
python auditoria-comparativa-documentos/scripts/extrair_documento.py auditoria-comparativa-documentos/evals/files/DOC-B_contrato_v2.docx --id DOC-B --saida /tmp/DOC-B.md

# 2. Execução do teste de regressão nas referências históricas
# Execução 1 (rodada preliminar com falhas) deve acusar citações não encontradas
python auditoria-comparativa-documentos/scripts/verificar_citacoes.py auditoria-comparativa-documentos/evals/referencias/Execucao1.md --doc DOC-A=/tmp/DOC-A.md --doc DOC-B=/tmp/DOC-B.md

# Execução 7 (padrão de referência v1.0 calibrado) deve retornar 0 falhas (código de saída 0)
python auditoria-comparativa-documentos/scripts/verificar_citacoes.py auditoria-comparativa-documentos/evals/referencias/Execucao7.md --doc DOC-A=/tmp/DOC-A.md --doc DOC-B=/tmp/DOC-B.md
```

### Casos de Teste Padronizados (`evals.json`)

O arquivo [`evals.json`](auditoria-comparativa-documentos/evals/evals.json) define 3 cenários formais de benchmark:

1. **`versoes-relacao-nao-informada`**:
   - Prompt cego solicitando análise comparativa integral.
   - Avalia a capacidade de identificar os 9 achados plantados (alteração de prazos, mudança de "deverá" para "poderá", remoção de seguro, exigência de aprovação jurídica, conversão de multa para "medidas cabíveis", inconsistência de terminologia, referência a anexo inexistente, contradição interna e alteração de SLA) e desviar das 3 armadilhas de falsos positivos (cláusulas apenas renumeradas ou equivalências semânticas).
2. **`pedido-informal-com-planilha`**:
   - Prompt informal com linguagem cotidiana e demanda expressa de planilha Excel.
   - Avalia a manutenção do rigor de citação mesmo sob comandos informais.
3. **`foco-prazos-penalidades`**:
   - Solicitação restrita a prazos e penalidades.
   - Avalia a profundidade nos tópicos solicitados e a declaração explícita de limitação de escopo na cobertura.

---

## Solução de Problemas (Troubleshooting)

| Sintoma / Erro | Causa Raiz Provável | Solução Recomendada |
|---|---|---|
| `ImportError: No module named 'pypdf'` ou `'docx'` | Dependências ausentes no ambiente Python ativo. | Execute: `pip install pypdf python-docx openpyxl` no mesmo ambiente Python. |
| `[SEM TEXTO EXTRAÍVEL]` no arquivo `.md` do PDF | A página do PDF é uma imagem escaneada (sem camada OCR). | Aplique ferramenta de OCR no PDF antes da extração. Registre a ocorrência no inventário e limite a confiança dos achados derivados a `Média` ou `Baixa`. |
| IA cita número de página impressa no rodapé em vez da física | O PDF possui capa ou pré-textuais sem numeração, defasando a contagem. | Lembre a regra no prompt inicial ou use os arquivos gerados por `extrair_documento.py`, que forçam o cabeçalho físico `=== DOC-X · Página N ===`. |
| Script `verificar_citacoes.py` acusa `NAO_ENCONTRADA` para termos isolados | Termos de busca ou nomes de campos foram colocados indevidamente entre aspas no relatório. | Mude termos de busca para formato de código inline (ex: `` `multa` ``, `` `indenização` ``). Aspas são de uso exclusivo para citações literais de texto. |
| Script acusa `DOC_DIVERGENTE` | A IA atribuiu a citação do DOC-B como se pertencesse ao DOC-A. | Corrija a indicação do identificador do documento que precede a citação no relatório. |
| Script acusa `LOCALIZADOR_DIVERGENTE` | O texto citado é legítimo, mas está em outro parágrafo ou página. | Atualize o localizador com a indicação fornecida pelo script na mensagem de erro `está em: p. X / par. Y`. |
| A Skill não é ativada espontaneamente pelo Claude | O prompt do usuário não utilizou gatilhos comparativos explícitos. | Solicite explicitamente: *"Use a skill auditoria-comparativa-documentos para confrontar estes documentos"*. |
| Documento extenso (mais de 100 páginas) excede o limite de contexto | Tamanho do texto integral ultrapassa a capacidade de resposta coerente do modelo. | Fatie a extração por blocos de capítulos ou seções funcionais e processe em rodadas separadas. |

---

## Contribuição

Contribuições para aperfeiçoamento da metodologia, expansão da taxonomia ou melhorias nos scripts utilitários são muito bem-vindas!

1. Faça um Fork do projeto.
2. Crie uma branch para sua funcionalidade ou correção:
   ```bash
   git checkout -b feature/nova-ancora-severidade
   ```
3. Realize suas modificações, assegurando que o arquivo `evals/evals.json` e os testes de regressão continuem passando com 100% de sucesso:
   ```bash
   python auditoria-comparativa-documentos/scripts/verificar_citacoes.py auditoria-comparativa-documentos/evals/referencias/Execucao7.md --doc DOC-A=/tmp/DOC-A.md --doc DOC-B=/tmp/DOC-B.md
   ```
4. Submeta um Pull Request detalhado com a justificativa técnica das alterações.

---

## Licença

Este projeto é distribuído sob os termos da Licença **MIT**. Consulte o arquivo `LICENSE` para obter informações adicionais sobre termos de uso, reprodução e modificação.
