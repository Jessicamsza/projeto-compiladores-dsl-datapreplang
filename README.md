# DataPrepLang: DSL para Pré-processamento de Dados

## Equipe
* *Jéssica Maria Silva de Souza*

---

## 1. Motivação da Linguagem

### O Problema
No ciclo de vida de qualquer projeto de Análise de Dados ou Inteligência Artificial, uma das etapas mais demoradas e repetitivas é a de **pré-processamento e limpeza de dados**. Tarefas como carregar diferentes formatos de arquivos, tratar valores ausentes, remover dados irrelevantes e realizar análises exploratórias iniciais geralmente exigem a escrita de scripts verbosos em bibliotecas como Pandas, tornando o fluxo de trabalho lento e suscetível a erros.

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

Execute o interpretador a partir do terminal do Codespaces
Digite o comandoexecutar um dos exemplos:

    ```bash
    #  Exemplo com o dataset de Vendas
    python datapreplang/main.py examples/teste_vendas.dpl

    # Exemplo com o dataset de Churn
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
