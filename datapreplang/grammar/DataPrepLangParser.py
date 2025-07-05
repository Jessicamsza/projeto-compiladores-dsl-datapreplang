# Generated from datapreplang/grammar/DataPrepLang.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,24,99,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,4,0,
        28,8,0,11,0,12,0,29,1,0,1,0,1,1,1,1,1,1,1,1,3,1,38,8,1,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,49,8,2,1,3,1,3,1,3,1,3,1,3,1,4,1,4,
        1,4,1,4,4,4,60,8,4,11,4,12,4,61,1,4,1,4,1,5,1,5,1,6,1,6,1,6,1,6,
        1,6,1,7,1,7,1,7,1,7,4,7,77,8,7,11,7,12,7,78,1,7,1,7,1,8,1,8,3,8,
        85,8,8,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,12,1,12,
        1,12,0,0,13,0,2,4,6,8,10,12,14,16,18,20,22,24,0,2,1,0,22,23,2,0,
        21,21,23,23,93,0,27,1,0,0,0,2,37,1,0,0,0,4,39,1,0,0,0,6,50,1,0,0,
        0,8,55,1,0,0,0,10,65,1,0,0,0,12,67,1,0,0,0,14,72,1,0,0,0,16,84,1,
        0,0,0,18,86,1,0,0,0,20,89,1,0,0,0,22,94,1,0,0,0,24,96,1,0,0,0,26,
        28,3,2,1,0,27,26,1,0,0,0,28,29,1,0,0,0,29,27,1,0,0,0,29,30,1,0,0,
        0,30,31,1,0,0,0,31,32,5,0,0,1,32,1,1,0,0,0,33,38,3,4,2,0,34,38,3,
        6,3,0,35,38,3,8,4,0,36,38,3,14,7,0,37,33,1,0,0,0,37,34,1,0,0,0,37,
        35,1,0,0,0,37,36,1,0,0,0,38,3,1,0,0,0,39,40,5,1,0,0,40,41,5,2,0,
        0,41,42,5,3,0,0,42,43,5,23,0,0,43,44,5,4,0,0,44,48,5,21,0,0,45,46,
        5,5,0,0,46,47,5,6,0,0,47,49,5,23,0,0,48,45,1,0,0,0,48,49,1,0,0,0,
        49,5,1,0,0,0,50,51,5,7,0,0,51,52,5,21,0,0,52,53,5,8,0,0,53,54,5,
        23,0,0,54,7,1,0,0,0,55,56,5,8,0,0,56,57,5,21,0,0,57,59,5,20,0,0,
        58,60,3,10,5,0,59,58,1,0,0,0,60,61,1,0,0,0,61,59,1,0,0,0,61,62,1,
        0,0,0,62,63,1,0,0,0,63,64,5,9,0,0,64,9,1,0,0,0,65,66,3,12,6,0,66,
        11,1,0,0,0,67,68,5,10,0,0,68,69,3,24,12,0,69,70,5,16,0,0,70,71,3,
        22,11,0,71,13,1,0,0,0,72,73,5,13,0,0,73,74,5,21,0,0,74,76,5,20,0,
        0,75,77,3,16,8,0,76,75,1,0,0,0,77,78,1,0,0,0,78,76,1,0,0,0,78,79,
        1,0,0,0,79,80,1,0,0,0,80,81,5,9,0,0,81,15,1,0,0,0,82,85,3,18,9,0,
        83,85,3,20,10,0,84,82,1,0,0,0,84,83,1,0,0,0,85,17,1,0,0,0,86,87,
        5,14,0,0,87,88,3,24,12,0,88,19,1,0,0,0,89,90,5,15,0,0,90,91,5,11,
        0,0,91,92,5,10,0,0,92,93,3,24,12,0,93,21,1,0,0,0,94,95,7,0,0,0,95,
        23,1,0,0,0,96,97,7,1,0,0,97,25,1,0,0,0,6,29,37,48,61,78,84
    ]

class DataPrepLangParser ( Parser ):

    grammarFileName = "DataPrepLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'CARREGAR'", "'DADOS'", "'DE'", "'PARA'", 
                     "'USANDO'", "'DELIMITADOR'", "'SALVAR'", "'EM'", "'FIM'", 
                     "'COLUNA'", "'NA'", "'COMO'", "'ANALISAR'", "'DESCREVER'", 
                     "'CONTAGEM_VALORES'", "'PNULL'", "'('", "')'", "','", 
                     "':'" ]

    symbolicNames = [ "<INVALID>", "CARREGAR", "DADOS", "DE", "PARA", "USANDO", 
                      "DELIMITADOR", "SALVAR", "EM", "FIM", "COLUNA", "NA", 
                      "COMO", "ANALISAR", "DESCREVER", "CONTAGEM_VALORES", 
                      "PNULL", "LPAREN", "RPAREN", "COMMA", "COLON", "ID", 
                      "NUMBER", "STRING", "WHITESPACE" ]

    RULE_program = 0
    RULE_command = 1
    RULE_loadCommand = 2
    RULE_saveCommand = 3
    RULE_blockCommand = 4
    RULE_manipulationCommand = 5
    RULE_fillNullCommand = 6
    RULE_analyzeCommand = 7
    RULE_analysisCommand = 8
    RULE_describeCommand = 9
    RULE_countValuesCommand = 10
    RULE_value = 11
    RULE_columnIdentifier = 12

    ruleNames =  [ "program", "command", "loadCommand", "saveCommand", "blockCommand", 
                   "manipulationCommand", "fillNullCommand", "analyzeCommand", 
                   "analysisCommand", "describeCommand", "countValuesCommand", 
                   "value", "columnIdentifier" ]

    EOF = Token.EOF
    CARREGAR=1
    DADOS=2
    DE=3
    PARA=4
    USANDO=5
    DELIMITADOR=6
    SALVAR=7
    EM=8
    FIM=9
    COLUNA=10
    NA=11
    COMO=12
    ANALISAR=13
    DESCREVER=14
    CONTAGEM_VALORES=15
    PNULL=16
    LPAREN=17
    RPAREN=18
    COMMA=19
    COLON=20
    ID=21
    NUMBER=22
    STRING=23
    WHITESPACE=24

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(DataPrepLangParser.EOF, 0)

        def command(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DataPrepLangParser.CommandContext)
            else:
                return self.getTypedRuleContext(DataPrepLangParser.CommandContext,i)


        def getRuleIndex(self):
            return DataPrepLangParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = DataPrepLangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 26
                self.command()
                self.state = 29 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 8578) != 0)):
                    break

            self.state = 31
            self.match(DataPrepLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def loadCommand(self):
            return self.getTypedRuleContext(DataPrepLangParser.LoadCommandContext,0)


        def saveCommand(self):
            return self.getTypedRuleContext(DataPrepLangParser.SaveCommandContext,0)


        def blockCommand(self):
            return self.getTypedRuleContext(DataPrepLangParser.BlockCommandContext,0)


        def analyzeCommand(self):
            return self.getTypedRuleContext(DataPrepLangParser.AnalyzeCommandContext,0)


        def getRuleIndex(self):
            return DataPrepLangParser.RULE_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommand" ):
                listener.enterCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommand" ):
                listener.exitCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommand" ):
                return visitor.visitCommand(self)
            else:
                return visitor.visitChildren(self)




    def command(self):

        localctx = DataPrepLangParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_command)
        try:
            self.state = 37
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 33
                self.loadCommand()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 34
                self.saveCommand()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 3)
                self.state = 35
                self.blockCommand()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 4)
                self.state = 36
                self.analyzeCommand()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoadCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CARREGAR(self):
            return self.getToken(DataPrepLangParser.CARREGAR, 0)

        def DADOS(self):
            return self.getToken(DataPrepLangParser.DADOS, 0)

        def DE(self):
            return self.getToken(DataPrepLangParser.DE, 0)

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(DataPrepLangParser.STRING)
            else:
                return self.getToken(DataPrepLangParser.STRING, i)

        def PARA(self):
            return self.getToken(DataPrepLangParser.PARA, 0)

        def ID(self):
            return self.getToken(DataPrepLangParser.ID, 0)

        def USANDO(self):
            return self.getToken(DataPrepLangParser.USANDO, 0)

        def DELIMITADOR(self):
            return self.getToken(DataPrepLangParser.DELIMITADOR, 0)

        def getRuleIndex(self):
            return DataPrepLangParser.RULE_loadCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoadCommand" ):
                listener.enterLoadCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoadCommand" ):
                listener.exitLoadCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoadCommand" ):
                return visitor.visitLoadCommand(self)
            else:
                return visitor.visitChildren(self)




    def loadCommand(self):

        localctx = DataPrepLangParser.LoadCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_loadCommand)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(DataPrepLangParser.CARREGAR)
            self.state = 40
            self.match(DataPrepLangParser.DADOS)
            self.state = 41
            self.match(DataPrepLangParser.DE)
            self.state = 42
            self.match(DataPrepLangParser.STRING)
            self.state = 43
            self.match(DataPrepLangParser.PARA)
            self.state = 44
            self.match(DataPrepLangParser.ID)
            self.state = 48
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 45
                self.match(DataPrepLangParser.USANDO)
                self.state = 46
                self.match(DataPrepLangParser.DELIMITADOR)
                self.state = 47
                self.match(DataPrepLangParser.STRING)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SaveCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SALVAR(self):
            return self.getToken(DataPrepLangParser.SALVAR, 0)

        def ID(self):
            return self.getToken(DataPrepLangParser.ID, 0)

        def EM(self):
            return self.getToken(DataPrepLangParser.EM, 0)

        def STRING(self):
            return self.getToken(DataPrepLangParser.STRING, 0)

        def getRuleIndex(self):
            return DataPrepLangParser.RULE_saveCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSaveCommand" ):
                listener.enterSaveCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSaveCommand" ):
                listener.exitSaveCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSaveCommand" ):
                return visitor.visitSaveCommand(self)
            else:
                return visitor.visitChildren(self)




    def saveCommand(self):

        localctx = DataPrepLangParser.SaveCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_saveCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(DataPrepLangParser.SALVAR)
            self.state = 51
            self.match(DataPrepLangParser.ID)
            self.state = 52
            self.match(DataPrepLangParser.EM)
            self.state = 53
            self.match(DataPrepLangParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EM(self):
            return self.getToken(DataPrepLangParser.EM, 0)

        def ID(self):
            return self.getToken(DataPrepLangParser.ID, 0)

        def COLON(self):
            return self.getToken(DataPrepLangParser.COLON, 0)

        def FIM(self):
            return self.getToken(DataPrepLangParser.FIM, 0)

        def manipulationCommand(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DataPrepLangParser.ManipulationCommandContext)
            else:
                return self.getTypedRuleContext(DataPrepLangParser.ManipulationCommandContext,i)


        def getRuleIndex(self):
            return DataPrepLangParser.RULE_blockCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlockCommand" ):
                listener.enterBlockCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlockCommand" ):
                listener.exitBlockCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockCommand" ):
                return visitor.visitBlockCommand(self)
            else:
                return visitor.visitChildren(self)




    def blockCommand(self):

        localctx = DataPrepLangParser.BlockCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_blockCommand)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(DataPrepLangParser.EM)
            self.state = 56
            self.match(DataPrepLangParser.ID)
            self.state = 57
            self.match(DataPrepLangParser.COLON)
            self.state = 59 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 58
                self.manipulationCommand()
                self.state = 61 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==10):
                    break

            self.state = 63
            self.match(DataPrepLangParser.FIM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ManipulationCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fillNullCommand(self):
            return self.getTypedRuleContext(DataPrepLangParser.FillNullCommandContext,0)


        def getRuleIndex(self):
            return DataPrepLangParser.RULE_manipulationCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterManipulationCommand" ):
                listener.enterManipulationCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitManipulationCommand" ):
                listener.exitManipulationCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitManipulationCommand" ):
                return visitor.visitManipulationCommand(self)
            else:
                return visitor.visitChildren(self)




    def manipulationCommand(self):

        localctx = DataPrepLangParser.ManipulationCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_manipulationCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.fillNullCommand()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FillNullCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLUNA(self):
            return self.getToken(DataPrepLangParser.COLUNA, 0)

        def columnIdentifier(self):
            return self.getTypedRuleContext(DataPrepLangParser.ColumnIdentifierContext,0)


        def PNULL(self):
            return self.getToken(DataPrepLangParser.PNULL, 0)

        def value(self):
            return self.getTypedRuleContext(DataPrepLangParser.ValueContext,0)


        def getRuleIndex(self):
            return DataPrepLangParser.RULE_fillNullCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFillNullCommand" ):
                listener.enterFillNullCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFillNullCommand" ):
                listener.exitFillNullCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFillNullCommand" ):
                return visitor.visitFillNullCommand(self)
            else:
                return visitor.visitChildren(self)




    def fillNullCommand(self):

        localctx = DataPrepLangParser.FillNullCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_fillNullCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(DataPrepLangParser.COLUNA)
            self.state = 68
            self.columnIdentifier()
            self.state = 69
            self.match(DataPrepLangParser.PNULL)
            self.state = 70
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AnalyzeCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ANALISAR(self):
            return self.getToken(DataPrepLangParser.ANALISAR, 0)

        def ID(self):
            return self.getToken(DataPrepLangParser.ID, 0)

        def COLON(self):
            return self.getToken(DataPrepLangParser.COLON, 0)

        def FIM(self):
            return self.getToken(DataPrepLangParser.FIM, 0)

        def analysisCommand(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DataPrepLangParser.AnalysisCommandContext)
            else:
                return self.getTypedRuleContext(DataPrepLangParser.AnalysisCommandContext,i)


        def getRuleIndex(self):
            return DataPrepLangParser.RULE_analyzeCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnalyzeCommand" ):
                listener.enterAnalyzeCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnalyzeCommand" ):
                listener.exitAnalyzeCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnalyzeCommand" ):
                return visitor.visitAnalyzeCommand(self)
            else:
                return visitor.visitChildren(self)




    def analyzeCommand(self):

        localctx = DataPrepLangParser.AnalyzeCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_analyzeCommand)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(DataPrepLangParser.ANALISAR)
            self.state = 73
            self.match(DataPrepLangParser.ID)
            self.state = 74
            self.match(DataPrepLangParser.COLON)
            self.state = 76 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 75
                self.analysisCommand()
                self.state = 78 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==14 or _la==15):
                    break

            self.state = 80
            self.match(DataPrepLangParser.FIM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AnalysisCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def describeCommand(self):
            return self.getTypedRuleContext(DataPrepLangParser.DescribeCommandContext,0)


        def countValuesCommand(self):
            return self.getTypedRuleContext(DataPrepLangParser.CountValuesCommandContext,0)


        def getRuleIndex(self):
            return DataPrepLangParser.RULE_analysisCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnalysisCommand" ):
                listener.enterAnalysisCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnalysisCommand" ):
                listener.exitAnalysisCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnalysisCommand" ):
                return visitor.visitAnalysisCommand(self)
            else:
                return visitor.visitChildren(self)




    def analysisCommand(self):

        localctx = DataPrepLangParser.AnalysisCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_analysisCommand)
        try:
            self.state = 84
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 82
                self.describeCommand()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 83
                self.countValuesCommand()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DescribeCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DESCREVER(self):
            return self.getToken(DataPrepLangParser.DESCREVER, 0)

        def columnIdentifier(self):
            return self.getTypedRuleContext(DataPrepLangParser.ColumnIdentifierContext,0)


        def getRuleIndex(self):
            return DataPrepLangParser.RULE_describeCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDescribeCommand" ):
                listener.enterDescribeCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDescribeCommand" ):
                listener.exitDescribeCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDescribeCommand" ):
                return visitor.visitDescribeCommand(self)
            else:
                return visitor.visitChildren(self)




    def describeCommand(self):

        localctx = DataPrepLangParser.DescribeCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_describeCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(DataPrepLangParser.DESCREVER)
            self.state = 87
            self.columnIdentifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CountValuesCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTAGEM_VALORES(self):
            return self.getToken(DataPrepLangParser.CONTAGEM_VALORES, 0)

        def NA(self):
            return self.getToken(DataPrepLangParser.NA, 0)

        def COLUNA(self):
            return self.getToken(DataPrepLangParser.COLUNA, 0)

        def columnIdentifier(self):
            return self.getTypedRuleContext(DataPrepLangParser.ColumnIdentifierContext,0)


        def getRuleIndex(self):
            return DataPrepLangParser.RULE_countValuesCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCountValuesCommand" ):
                listener.enterCountValuesCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCountValuesCommand" ):
                listener.exitCountValuesCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCountValuesCommand" ):
                return visitor.visitCountValuesCommand(self)
            else:
                return visitor.visitChildren(self)




    def countValuesCommand(self):

        localctx = DataPrepLangParser.CountValuesCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_countValuesCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(DataPrepLangParser.CONTAGEM_VALORES)
            self.state = 90
            self.match(DataPrepLangParser.NA)
            self.state = 91
            self.match(DataPrepLangParser.COLUNA)
            self.state = 92
            self.columnIdentifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(DataPrepLangParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(DataPrepLangParser.STRING, 0)

        def getRuleIndex(self):
            return DataPrepLangParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = DataPrepLangParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            _la = self._input.LA(1)
            if not(_la==22 or _la==23):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ColumnIdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(DataPrepLangParser.ID, 0)

        def STRING(self):
            return self.getToken(DataPrepLangParser.STRING, 0)

        def getRuleIndex(self):
            return DataPrepLangParser.RULE_columnIdentifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumnIdentifier" ):
                listener.enterColumnIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumnIdentifier" ):
                listener.exitColumnIdentifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColumnIdentifier" ):
                return visitor.visitColumnIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def columnIdentifier(self):

        localctx = DataPrepLangParser.ColumnIdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_columnIdentifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            _la = self._input.LA(1)
            if not(_la==21 or _la==23):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





