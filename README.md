# DataPrepLang: DSL para Pré-processamento de Dados

## Equipe
* *Jéssica Maria Silva de Souza*

---

## 1. Motivação e Descrição da Linguagem (Critérios 'c' e 'd')

### O Problema
No ciclo de vida de qualquer projeto de Análise de Dados ou Inteligência Artificial, uma das etapas mais demoradas e repetitivas é a de **pré-processamento e limpeza de dados**. Tarefas como carregar diferentes formatos de arquivos, tratar valores ausentes, remover dados irrelevantes e realizar análises exploratórias iniciais geralmente exigem a escrita de scripts verbosos em bibliotecas como Pandas, tornando o fluxo de trabalho lento e suscetível a erros.

### A Solução: DataPrepLang
**DataPrepLang** é uma Linguagem de Domínio Específico (DSL) declarativa e de alto nível, projetada para simplificar e automatizar esse pipeline de limpeza de dados. Com uma sintaxe intuitiva e próxima da linguagem natural, ela permite que analistas e cientistas de dados definam fluxos de trabalho de pré-processamento de forma rápida, legível e reproduzível, focando no "o quê" em vez do "como".

A linguagem é **interpretada** e utiliza a biblioteca Pandas como seu back-end de execução, traduzindo comandos simples em operações de DataFrames complexas.

---

## 2. Sintaxe da Linguagem

A linguagem é composta por uma sequência de comandos que operam sobre tabelas de dados carregadas na memória.

| Comando                             | Descrição                                                                                                                              |
| ----------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `CARREGAR DADOS DE "..." PARA ...`  | Carrega uma tabela de um arquivo CSV para uma variável na memória. Suporta a cláusula opcional `USANDO DELIMITADOR "..."`.                 |
| `EM ... : ... FIM`                  | Define um bloco de contexto onde todos os comandos de manipulação internos operarão sobre a tabela especificada.                         |
| `COLUNA "..." PNULL ...`            | **(Dentro de um bloco EM)** Preenche os valores nulos (`NaN`) de uma coluna com um valor numérico ou de texto especificado.              |
| `ANALISAR ... : ... FIM`            | Define um bloco de contexto para realizar comandos de análise exploratória na tabela especificada.                                       |
| `DESCREVER "..."`                   | **(Dentro de um bloco ANALISAR)** Exibe estatísticas descritivas (média, desvio padrão, etc.) para uma coluna numérica.                   |
| `CONTAGEM_VALORES NA COLUNA "..."`  | **(Dentro de um bloco ANALISAR)** Exibe a contagem de ocorrências para cada valor único em uma coluna categórica.                         |
| `SALVAR ... EM "..."`               | Salva a tabela especificada (com todas as modificações aplicadas) em um novo arquivo CSV.                                                |

---

## 3. Guia de Execução 
### Executando no GitHub Codespaces 

Este projeto foi configurado para rodar perfeitamente no GitHub Codespaces com o mínimo de esforço.

1.  Clique no botão verde **"< > Code"** no topo desta página do repositório.
2.  Vá para a aba **"Codespaces"** e clique em **"Create codespace on main"**.
3.  Aguarde um instante. O Codespaces irá criar um ambiente virtual e instalará **automaticamente** todas as dependências listadas no `requirements.txt`.
4.  Quando o ambiente carregar, um terminal aparecerá na parte inferior. Para executar um dos exemplos, simplesmente digite o comando:

    ```bash
    # Para executar o exemplo de limpeza de dados de vendas
    python datapreplang/main.py examples/teste_vendas.dpl

    # Para executar o exemplo de limpeza de dados de churn
    python datapreplang/main.py examples/teste_chrun.dpl
    ```
    A saída da execução do interpretador será exibida no terminal.

### Executando Localmente

1.  Clone o repositório: `git clone <url_do_seu_repositorio>`
2.  Navegue até a pasta: `cd DataPrepLang`
3.  Crie e ative um ambiente virtual:
    ```bash
    python -m venv venv
    # No Windows:
    .\venv\Scripts\activate
    # No macOS/Linux:
    source venv/bin/activate
    ```
4.  Instale as dependências: `pip install -r requirements.txt`
5.  Execute o interpretador com um arquivo de exemplo:
    ```bash
    python datapreplang/main.py examples/teste_vendas.dpl
    ```