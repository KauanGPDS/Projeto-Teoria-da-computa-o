# Generated from MinhaLinguagem.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MinhaLinguagemParser import MinhaLinguagemParser
else:
    from MinhaLinguagemParser import MinhaLinguagemParser

# This class defines a complete generic visitor for a parse tree produced by MinhaLinguagemParser.

class MinhaLinguagemVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MinhaLinguagemParser#program.
    def visitProgram(self, ctx:MinhaLinguagemParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinhaLinguagemParser#declaracao.
    def visitDeclaracao(self, ctx:MinhaLinguagemParser.DeclaracaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinhaLinguagemParser#tipo.
    def visitTipo(self, ctx:MinhaLinguagemParser.TipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinhaLinguagemParser#comando.
    def visitComando(self, ctx:MinhaLinguagemParser.ComandoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinhaLinguagemParser#bloco.
    def visitBloco(self, ctx:MinhaLinguagemParser.BlocoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinhaLinguagemParser#atribuicao.
    def visitAtribuicao(self, ctx:MinhaLinguagemParser.AtribuicaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinhaLinguagemParser#estruturaIf.
    def visitEstruturaIf(self, ctx:MinhaLinguagemParser.EstruturaIfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinhaLinguagemParser#estruturaWhile.
    def visitEstruturaWhile(self, ctx:MinhaLinguagemParser.EstruturaWhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinhaLinguagemParser#estruturaFor.
    def visitEstruturaFor(self, ctx:MinhaLinguagemParser.EstruturaForContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinhaLinguagemParser#leitura.
    def visitLeitura(self, ctx:MinhaLinguagemParser.LeituraContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinhaLinguagemParser#escrita.
    def visitEscrita(self, ctx:MinhaLinguagemParser.EscritaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinhaLinguagemParser#expressao.
    def visitExpressao(self, ctx:MinhaLinguagemParser.ExpressaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinhaLinguagemParser#termo.
    def visitTermo(self, ctx:MinhaLinguagemParser.TermoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinhaLinguagemParser#fator.
    def visitFator(self, ctx:MinhaLinguagemParser.FatorContext):
        return self.visitChildren(ctx)



del MinhaLinguagemParser