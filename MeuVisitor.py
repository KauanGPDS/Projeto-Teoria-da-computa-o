# Importa o Visitor gerado pelo ANTLR
from MinhaLinguagemVisitor import MinhaLinguagemVisitor
# Importa o Parser (para termos acesso aos tipos de contexto)
from MinhaLinguagemParser import MinhaLinguagemParser

# Classe para guardar informações das variáveis na Tabela de Símbolos
class Variavel:
    def __init__(self, tipo, linha, coluna):
        self.tipo = tipo
        self.linha = linha
        self.coluna = coluna
        # Você pode adicionar 'escopo' aqui futuramente

class MeuVisitor(MinhaLinguagemVisitor):
    def __init__(self):
        # Tabela de Símbolos: Um dicionário para guardar as variáveis
        self.tabela_de_simbolos = {} 
        # Lista de erros semânticos
        self._erros = []

    # --- Funções de ajuda para erros ---
    def temErros(self):
        return len(self._erros) > 0

    def getErros(self):
        return self._erros

    # --- IMPLEMENTAÇÃO DOS DIFERENCIAIS ---

    """
    DIFERENCIAL 1: "A cada utilização de uma variável, é necessário 
                   verificar se ela já foi declarada."
    
    Isso é feito em todos os métodos que usam um ID, como:
    - visitAtribuicao (Lado Esquerdo)
    - visitFator (Quando o fator é um ID)
    - visitLeitura
    """

    """
    DIFERENCIAL 2: "A cada atribuição, verificar se é possível realizar 
                   as operações, devido aos tipos das variáveis..."
    
    Isso é feito em 'visitAtribuicao' e 'inferirTipoExpressao'.
    """

    # O ANTLR chama este método quando "visita" uma declaração
    # Ex: int a;
    def visitDeclaracao(self, ctx: MinhaLinguagemParser.DeclaracaoContext):
        # Pega o tipo (ex: 'int')
        tipo = ctx.tipo().getText()
        
        # Itera por todos os IDs declarados (ex: int a, b, c;)
        for id_node in ctx.ID():
            nome_var = id_node.getText()
            linha = id_node.getSymbol().line
            coluna = id_node.getSymbol().column
            
            # REQUISITO: Verificar se a variável já foi declarada
            if nome_var in self.tabela_de_simbolos:
                self._erros.append(
                    f"[Erro Linha {linha}:{coluna}] Variável '{nome_var}' já foi declarada."
                )
            else:
                # Adiciona na Tabela de Símbolos
                self.tabela_de_simbolos[nome_var] = Variavel(tipo=tipo, linha=linha, coluna=coluna)
                print(f"[LOG] Variável '{nome_var}' (tipo {tipo}) adicionada à tabela.")

        return self.visitChildren(ctx)

    # O ANTLR chama este método quando visita uma atribuição
    # Ex: a = 10 + b;
    def visitAtribuicao(self, ctx: MinhaLinguagemParser.AtribuicaoContext):
        nome_var = ctx.ID().getText()
        linha = ctx.ID().getSymbol().line
        coluna = ctx.ID().getSymbol().column

        # DIFERENCIAL 1: Checa se a variável da esquerda foi declarada
        if nome_var not in self.tabela_de_simbolos:
            self._erros.append(
                f"[Erro Linha {linha}:{coluna}] Variável '{nome_var}' não foi declarada (em atribuição)."
            )
            return # Não podemos checar tipos se a var nem existe

        # Pega o tipo esperado (da variável na tabela)
        tipo_esperado = self.tabela_de_simbolos[nome_var].tipo

        # Pega o tipo da expressão do lado direito
        tipo_da_expressao = self.inferirTipoExpressao(ctx.expressao())

        # DIFERENCIAL 2: Verificação de Tipos na Atribuição
        if tipo_da_expressao and tipo_esperado != tipo_da_expressao:
            # Regra especial: permitir int -> float
            if tipo_esperado == 'float' and tipo_da_expressao == 'int':
                pass # Isso é permitido
            else:
                self._erros.append(
                    f"[Erro Linha {linha}:{coluna}] Tipo incompatível em '{nome_var}'. "
                    f"Esperava '{tipo_esperado}' mas recebeu '{tipo_da_expressao}'."
                )

        return self.visitChildren(ctx)

    # Função auxiliar para descobrir o tipo de uma expressão
    def inferirTipoExpressao(self, ctx: MinhaLinguagemParser.ExpressaoContext):
        # Esta é uma implementação simplificada.
        # Regra: int + float = float. string + string = string. int + int = int.
        # int + string = ERRO.
        
        tipos_na_expressao = set()
        
        # Vamos "visitar" todos os fatores da expressão para ver seus tipos
        # Este é um "mini-visitor" manual
        for termo in ctx.termo():
            for fator in termo.fator():
                tipo = self.inferirTipoFator(fator)
                if tipo:
                    tipos_na_expressao.add(tipo)
        
        # Lógica de inferência (simplificada):
        if 'string' in tipos_na_expressao and len(tipos_na_expressao) > 1:
            self._erros.append(f"[Erro Linha {ctx.start.line}] Operação inválida: não se pode misturar 'string' com números.")
            return 'string' # Retorna string, mas já marcou o erro
        if 'string' in tipos_na_expressao:
            return 'string'
        if 'float' in tipos_na_expressao:
            return 'float' # Se tiver float e int, vira float
        if 'int' in tipos_na_expressao:
            return 'int'
        
        return None # Expressão vazia ou com erro

    # Descobre o tipo de um único "fator" (número, ID, etc.)
    def inferirTipoFator(self, ctx: MinhaLinguagemParser.FatorContext):
        if ctx.ID():
            nome_var = ctx.ID().getText()
            linha = ctx.ID().getSymbol().line
            coluna = ctx.ID().getSymbol().column
            
            # DIFERENCIAL 1: Checa se a variável (em uso) foi declarada
            if nome_var not in self.tabela_de_simbolos:
                self._erros.append(
                    f"[Erro Linha {linha}:{coluna}] Variável '{nome_var}' não foi declarada (em expressão)."
                )
                return None
            return self.tabela_de_simbolos[nome_var].tipo

        if ctx.INT():
            return 'int'
        if ctx.FLOAT():
            return 'float'
        if ctx.STRING_LITERAL():
            return 'string'
        if ctx.expressao(): # Trata parênteses (ex: (1+2))
            return self.inferirTipoExpressao(ctx.expressao())
        
        return None

    # Verifica declaração no 'scanf'
    def visitLeitura(self, ctx:MinhaLinguagemParser.LeituraContext):
        nome_var = ctx.ID().getText()
        linha = ctx.ID().getSymbol().line
        coluna = ctx.ID().getSymbol().column

        # DIFERENCIAL 1: Checa se a variável foi declarada
        if nome_var not in self.tabela_de_simbolos:
            self._erros.append(
                f"[Erro Linha {linha}:{coluna}] Variável '{nome_var}' não foi declarada (em scanf)."
            )
        
        return self.visitChildren(ctx)

    # Verifica tipos no 'printf'
    def visitEscrita(self, ctx: MinhaLinguagemParser.EscritaContext):
        # Apenas precisamos visitar a expressão para checar se as
        # variáveis dentro dela foram declaradas.
        # A gramática já permite STRING_LITERAL ou expressao.
        if ctx.expressao():
            self.inferirTipoExpressao(ctx.expressao()) # Isso vai rodar as checagens
            
        return self.visitChildren(ctx)