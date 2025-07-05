# Generated from datapreplang/grammar/DataPrepLang.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .DataPrepLangParser import DataPrepLangParser
else:
    from DataPrepLangParser import DataPrepLangParser

# This class defines a complete generic visitor for a parse tree produced by DataPrepLangParser.

class DataPrepLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by DataPrepLangParser#program.
    def visitProgram(self, ctx:DataPrepLangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataPrepLangParser#command.
    def visitCommand(self, ctx:DataPrepLangParser.CommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataPrepLangParser#loadCommand.
    def visitLoadCommand(self, ctx:DataPrepLangParser.LoadCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataPrepLangParser#saveCommand.
    def visitSaveCommand(self, ctx:DataPrepLangParser.SaveCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataPrepLangParser#blockCommand.
    def visitBlockCommand(self, ctx:DataPrepLangParser.BlockCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataPrepLangParser#manipulationCommand.
    def visitManipulationCommand(self, ctx:DataPrepLangParser.ManipulationCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataPrepLangParser#fillNullCommand.
    def visitFillNullCommand(self, ctx:DataPrepLangParser.FillNullCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataPrepLangParser#analyzeCommand.
    def visitAnalyzeCommand(self, ctx:DataPrepLangParser.AnalyzeCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataPrepLangParser#analysisCommand.
    def visitAnalysisCommand(self, ctx:DataPrepLangParser.AnalysisCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataPrepLangParser#describeCommand.
    def visitDescribeCommand(self, ctx:DataPrepLangParser.DescribeCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataPrepLangParser#countValuesCommand.
    def visitCountValuesCommand(self, ctx:DataPrepLangParser.CountValuesCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataPrepLangParser#value.
    def visitValue(self, ctx:DataPrepLangParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataPrepLangParser#columnIdentifier.
    def visitColumnIdentifier(self, ctx:DataPrepLangParser.ColumnIdentifierContext):
        return self.visitChildren(ctx)



del DataPrepLangParser