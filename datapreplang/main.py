import sys
from antlr4 import *
from grammar.DataPrepLangLexer import DataPrepLangLexer
from grammar.DataPrepLangParser import DataPrepLangParser
from interpreter import Interpreter # IMPORTANTE: Importa nossa nova classe

def main():
    try:
        input_file = sys.argv[1]
        with open(input_file, 'r', encoding='utf-8-sig') as file:
            data = file.read()
        input_stream = InputStream(data)
    except (IndexError, FileNotFoundError):
        print(f"Arquivo não encontrado ou não especificado: '{sys.argv[1]}'")
        return

    lexer = DataPrepLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = DataPrepLangParser(stream)
    tree = parser.program()

    if parser.getNumberOfSyntaxErrors() > 0:
        print("Execução falhou devido a erros de sintaxe.")
    else:
        print("Análise sintática concluída. Iniciando interpretação...")
        print("-" * 50)
        
        # --- EXECUÇÃO DO INTERPRETADOR ---
        # 1. Cria uma instância do nosso interpretador.
        interpreter = Interpreter()
        
        # 2. Inicia a "caminhada" pela árvore a partir do topo (nó 'program').
        interpreter.visit(tree)
        
        print("-" * 50)
        print("Interpretação concluída.")

if __name__ == '__main__':
    main()