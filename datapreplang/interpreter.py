import pandas as pd
from grammar.DataPrepLangVisitor import DataPrepLangVisitor
from grammar.DataPrepLangParser import DataPrepLangParser

class Interpreter(DataPrepLangVisitor):
    def __init__(self):
        self.variables = {}

    def visitLoadCommand(self, ctx:DataPrepLangParser.LoadCommandContext):
            # Pega o nome do arquivo do token STRING. O .getText() pega o texto do token.
            # [1:-1] para remover as aspas do início e do fim.
            file_path = ctx.STRING(0).getText()[1:-1]
            var_name = ctx.ID().getText()
            # Verifica se a cláusula opcional de delimitador foi usada.
            delimiter = ',' # Padrão é vírgula
            if ctx.DELIMITADOR():
                delimiter = ctx.STRING(1).getText()[1:-1]

            print(f"-> Executando: Carregando dados de '{file_path}' com delimitador '{delimiter}' para a variável '{var_name}'...")

            try:
                df = pd.read_csv(file_path, delimiter=delimiter)
                self.variables[var_name] = df
                print(f"   SUCESSO: Tabela '{var_name}' carregada com {len(df)} linhas e {len(df.columns)} colunas.")

            except FileNotFoundError:
                print(f"   ERRO: Arquivo não encontrado em '{file_path}'. Verifique o caminho.")
            except Exception as e:
                print(f"   ERRO: Ocorreu um problema ao ler o arquivo: {e}")
            
            return None
    
    # bloco 'EM ... FIM'e define o contexto
    def visitBlockCommand(self, ctx:DataPrepLangParser.BlockCommandContext):
        # o nome da variável é o 'contexto' de trabalho.
        var_name = ctx.ID().getText()
        print(f"-> Entrando no bloco de manipulação para a tabela '{var_name}'...")
        self.current_df_name = var_name
        self.visitChildren(ctx)
        # Limpa a variável de contexto ao sair do bloco.
        self.current_df_name = None
        print(f"-> Saindo do bloco de manipulação.")
        return None
    
    # bloco 'ANALISAR ... FIM' e define o contexto
    def visitAnalyzeCommand(self, ctx:DataPrepLangParser.AnalyzeCommandContext):
        var_name = ctx.ID().getText()
        print(f"-> Entrando no bloco de análise para a tabela '{var_name}'...")
        self.current_df_name = var_name
        self.visitChildren(ctx)
        self.current_df_name = None
        print(f"-> Saindo do bloco de análise.")
        return None
    
    # Implementa a lógica para: COLUNA "nome" PNULL valor
    def visitFillNullCommand(self, ctx:DataPrepLangParser.FillNullCommandContext):
        if not self.current_df_name:
            print("   ERRO: O comando PNULL deve ser usado dentro de um bloco 'EM'.")
            return

        col_name = ctx.columnIdentifier().getText().replace('"', '')
        value_ctx = ctx.value()
        if value_ctx.NUMBER():
            fill_value = float(value_ctx.NUMBER().getText())
        else:
            fill_value = value_ctx.STRING().getText().replace('"', '')

        print(f"   -> Executando: Na coluna '{col_name}', preenchendo valores nulos com '{fill_value}'...")
        try:
            df = self.variables[self.current_df_name]
            if col_name not in df.columns:
                print(f"ERRO: A coluna '{col_name}' não existe na tabela '{self.current_df_name}'.")
                return

            df[col_name] = df[col_name].fillna(value=fill_value)
            print(f"SUCESSO: Valores nulos em '{col_name}' preenchidos.")

        except KeyError:
            print(f"   ERRO: A tabela '{self.current_df_name}' não foi encontrada.")
        except Exception as e:
            print(f"   ERRO: Ocorreu um problema inesperado: {e}")

        return None
    
    # Implementa a lógica para: DESCREVER "nome_coluna"
    def visitDescribeCommand(self, ctx:DataPrepLangParser.DescribeCommandContext):
        if not self.current_df_name:
            print("   ERRO: O comando DESCREVER deve ser usado dentro de um bloco 'ANALISAR'.")
            return
        col_name = ctx.columnIdentifier().getText().replace('"', '')
        print(f"   -> Executando: Análise descritiva da coluna '{col_name}'...")
        try:
            df = self.variables[self.current_df_name]
            if col_name not in df.columns:
                print(f"      ERRO: A coluna '{col_name}' não existe.")
                return
            description = df[col_name].describe()
            print("      " + str(description).replace('\n', '\n      '))
        except KeyError:
            print(f"   ERRO: A tabela '{self.current_df_name}' não foi encontrada.")
        except Exception as e:
            print(f"   ERRO: Ocorreu um problema inesperado: {e}")
        return None

    # Implementa a lógica para: CONTAGEM_VALORES NA COLUNA "nome"
    def visitCountValuesCommand(self, ctx:DataPrepLangParser.CountValuesCommandContext):
        if not self.current_df_name:
            print("   ERRO: O comando CONTAGEM_VALORES deve ser usado dentro de um bloco 'ANALISAR'.")
            return
        col_name = ctx.columnIdentifier().getText().replace('"', '')
        print(f"   -> Executando: Contagem de valores para a coluna '{col_name}'...")
        try:
            df = self.variables[self.current_df_name]
            if col_name not in df.columns:
                print(f"      ERRO: A coluna '{col_name}' não existe.")
                return
            counts = df[col_name].value_counts()
            print("      " + str(counts).replace('\n', '\n      '))
        except KeyError:
            print(f"   ERRO: A tabela '{self.current_df_name}' não foi encontrada.")
        except Exception as e:
            print(f"   ERRO: Ocorreu um problema inesperado: {e}")
        return None
    
        if not self.current_df_name:
            print("   ERRO: O comando CRIARCOL deve ser usado dentro de um bloco 'EM'.")
            return

        new_col_name = ctx.STRING().getText().replace('"', '')
        print(f"   -> Executando: Criando nova coluna '{new_col_name}'...")
        
        try:
            new_column_data = self.visit(ctx.expression())
            df = self.variables[self.current_df_name]
            df[new_col_name] = new_column_data
            print(f"      SUCESSO: Coluna '{new_col_name}' criada.")

        except Exception as e:
            print(f"   ERRO: Não foi possível criar a coluna. Detalhes: {e}")
        
        return None

    # Implementa a lógica para: SALVAR tabela EM "caminho/do/arquivo.csv"
    def visitSaveCommand(self, ctx:DataPrepLangParser.SaveCommandContext):
        var_name = ctx.ID().getText()
        file_path = ctx.STRING().getText().replace('"', '')
        print(f"-> Executando: Salvando tabela '{var_name}' em '{file_path}'...")
        if var_name not in self.variables:
            print(f"   ERRO: Tabela '{var_name}' não existe na memória.")
            return
        try:
            df = self.variables[var_name]
            df.to_csv(file_path, index=False)
            print(f"   SUCESSO: Tabela salva em '{file_path}'.")
        except Exception as e:
            print(f"   ERRO: Não foi possível salvar o arquivo. Detalhes: {e}")
        return None

        if ctx.NUMBER():
            return float(ctx.NUMBER().getText())
        
        if ctx.columnIdentifier():
            df = self.variables[self.current_df_name]
            col_name = ctx.columnIdentifier().getText().replace('"', '')
            return df[col_name]
