import sys
from antlr4 import *
# Importa os arquivos gerados pelo ANTLR
from MinhaLinguagemLexer import MinhaLinguagemLexer
from MinhaLinguagemParser import MinhaLinguagemParser
# Importa o SEU visitor
from MeuVisitor import MeuVisitor 

def main(argv):
    # 1. Pega o arquivo de código-fonte para compilar
    # (ex: python compilador.py ./testes/teste1.minhalang)
    try:
        arquivo_fonte = argv[1]
        input_stream = FileStream(arquivo_fonte, encoding='utf-8')
    except IndexError:
        print("Erro: Você deve fornecer um arquivo para compilar.")
        print("Uso: python compilador.py <caminho_do_arquivo>")
        return
    except FileNotFoundError:
        print(f"Erro: Arquivo '{argv[1]}' não encontrado.")
        return

    # 2. Conecta o Léxico (Fase 1)
    lexer = MinhaLinguagemLexer(input_stream)
    stream = CommonTokenStream(lexer)

    # 3. Conecta o Parser (Fase 2)
    parser = MinhaLinguagemParser(stream)
    
    # 4. Gera a Árvore Sintática (Inicia a análise sintática)
    print(f"Iniciando compilação de: {arquivo_fonte}\n")
    tree = parser.program() # 'program' é a regra inicial da sua gramática

    # 5. Se o parser não detectou erros, inicia a Análise Semântica (Fase 3)
    if parser.getNumberOfSyntaxErrors() == 0:
        print("--- Análise Sintática OK ---")
        
        # 6. Inicia o seu Visitor (o "cérebro")
        meu_visitor = MeuVisitor()
        meu_visitor.visit(tree) # Inicia a "caminhada" na árvore

        # 7. Verifica se seu visitor encontrou erros semânticos
        if not meu_visitor.temErros():
            print("\n--- Análise Semântica OK ---")
            print("====================================")
            print(" ✅ COMPILAÇÃO BEM-SUCEDIDA! ✅")
            print(" O código está correto.")
            print("====================================")
        else:
            print("\n--- Erros de Análise Semântica ---")
            print("====================================")
            print(" ❌ ERRO DE COMPILAÇÃO! ❌")
            print(" O código possui erros semânticos:")
            for erro in meu_visitor.getErros():
                print(f"-> {erro}")
            print("====================================")

    else:
        print("\n--- Erros de Análise Sintática ---")
        print("====================================")
        print(" ❌ ERRO DE COMPILAÇÃO! ❌")
        print(" O código possui erros de sintaxe.")
        print(" (O ANTLR já deve ter impresso os erros acima)")
        print("====================================")


if __name__ == '__main__':
    main(sys.argv)