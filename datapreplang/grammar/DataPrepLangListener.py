# Generated from datapreplang/grammar/DataPrepLang.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .DataPrepLangParser import DataPrepLangParser
else:
    from DataPrepLangParser import DataPrepLangParser

# This class defines a complete listener for a parse tree produced by DataPrepLangParser.
class DataPrepLangListener(ParseTreeListener):

    # Enter a parse tree produced by DataPrepLangParser#program.
    def enterProgram(self, ctx:DataPrepLangParser.ProgramContext):
        pass

    # Exit a parse tree produced by DataPrepLangParser#program.
    def exitProgram(self, ctx:DataPrepLangParser.ProgramContext):
        pass


    # Enter a parse tree produced by DataPrepLangParser#command.
    def enterCommand(self, ctx:DataPrepLangParser.CommandContext):
        pass

    # Exit a parse tree produced by DataPrepLangParser#command.
    def exitCommand(self, ctx:DataPrepLangParser.CommandContext):
        pass


    # Enter a parse tree produced by DataPrepLangParser#loadCommand.
    def enterLoadCommand(self, ctx:DataPrepLangParser.LoadCommandContext):
        pass

    # Exit a parse tree produced by DataPrepLangParser#loadCommand.
    def exitLoadCommand(self, ctx:DataPrepLangParser.LoadCommandContext):
        pass


    # Enter a parse tree produced by DataPrepLangParser#saveCommand.
    def enterSaveCommand(self, ctx:DataPrepLangParser.SaveCommandContext):
        pass

    # Exit a parse tree produced by DataPrepLangParser#saveCommand.
    def exitSaveCommand(self, ctx:DataPrepLangParser.SaveCommandContext):
        pass


    # Enter a parse tree produced by DataPrepLangParser#blockCommand.
    def enterBlockCommand(self, ctx:DataPrepLangParser.BlockCommandContext):
        pass

    # Exit a parse tree produced by DataPrepLangParser#blockCommand.
    def exitBlockCommand(self, ctx:DataPrepLangParser.BlockCommandContext):
        pass


    # Enter a parse tree produced by DataPrepLangParser#manipulationCommand.
    def enterManipulationCommand(self, ctx:DataPrepLangParser.ManipulationCommandContext):
        pass

    # Exit a parse tree produced by DataPrepLangParser#manipulationCommand.
    def exitManipulationCommand(self, ctx:DataPrepLangParser.ManipulationCommandContext):
        pass


    # Enter a parse tree produced by DataPrepLangParser#fillNullCommand.
    def enterFillNullCommand(self, ctx:DataPrepLangParser.FillNullCommandContext):
        pass

    # Exit a parse tree produced by DataPrepLangParser#fillNullCommand.
    def exitFillNullCommand(self, ctx:DataPrepLangParser.FillNullCommandContext):
        pass


    # Enter a parse tree produced by DataPrepLangParser#analyzeCommand.
    def enterAnalyzeCommand(self, ctx:DataPrepLangParser.AnalyzeCommandContext):
        pass

    # Exit a parse tree produced by DataPrepLangParser#analyzeCommand.
    def exitAnalyzeCommand(self, ctx:DataPrepLangParser.AnalyzeCommandContext):
        pass


    # Enter a parse tree produced by DataPrepLangParser#analysisCommand.
    def enterAnalysisCommand(self, ctx:DataPrepLangParser.AnalysisCommandContext):
        pass

    # Exit a parse tree produced by DataPrepLangParser#analysisCommand.
    def exitAnalysisCommand(self, ctx:DataPrepLangParser.AnalysisCommandContext):
        pass


    # Enter a parse tree produced by DataPrepLangParser#describeCommand.
    def enterDescribeCommand(self, ctx:DataPrepLangParser.DescribeCommandContext):
        pass

    # Exit a parse tree produced by DataPrepLangParser#describeCommand.
    def exitDescribeCommand(self, ctx:DataPrepLangParser.DescribeCommandContext):
        pass


    # Enter a parse tree produced by DataPrepLangParser#countValuesCommand.
    def enterCountValuesCommand(self, ctx:DataPrepLangParser.CountValuesCommandContext):
        pass

    # Exit a parse tree produced by DataPrepLangParser#countValuesCommand.
    def exitCountValuesCommand(self, ctx:DataPrepLangParser.CountValuesCommandContext):
        pass


    # Enter a parse tree produced by DataPrepLangParser#value.
    def enterValue(self, ctx:DataPrepLangParser.ValueContext):
        pass

    # Exit a parse tree produced by DataPrepLangParser#value.
    def exitValue(self, ctx:DataPrepLangParser.ValueContext):
        pass


    # Enter a parse tree produced by DataPrepLangParser#columnIdentifier.
    def enterColumnIdentifier(self, ctx:DataPrepLangParser.ColumnIdentifierContext):
        pass

    # Exit a parse tree produced by DataPrepLangParser#columnIdentifier.
    def exitColumnIdentifier(self, ctx:DataPrepLangParser.ColumnIdentifierContext):
        pass



del DataPrepLangParser