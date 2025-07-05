
grammar DataPrepLang;

// regras do parser

program: command+ EOF;

command:
      loadCommand
    | saveCommand
    | blockCommand
    | analyzeCommand
    ;

loadCommand: 'CARREGAR' 'DADOS' 'DE' STRING 'PARA' ID ('USANDO' 'DELIMITADOR' STRING)?;

saveCommand: 'SALVAR' ID 'EM' STRING;

blockCommand: 'EM' ID ':' (manipulationCommand)+ 'FIM';

manipulationCommand: fillNullCommand;

fillNullCommand: 'COLUNA' columnIdentifier 'PNULL' value;

analyzeCommand: 'ANALISAR' ID ':' (analysisCommand)+ 'FIM';

analysisCommand:
      describeCommand
    | countValuesCommand
    ;

describeCommand: 'DESCREVER' columnIdentifier;

countValuesCommand: 'CONTAGEM_VALORES' 'NA' 'COLUNA' columnIdentifier;

value: NUMBER | STRING;

columnIdentifier: ID | STRING;

// regras do lexer
// Tokens

CARREGAR: 'CARREGAR';
DADOS: 'DADOS';
DE: 'DE';
PARA: 'PARA';
USANDO: 'USANDO';
DELIMITADOR: 'DELIMITADOR';
SALVAR: 'SALVAR';
EM: 'EM';
FIM: 'FIM';
COLUNA: 'COLUNA';
NA: 'NA';
COMO: 'COMO';
ANALISAR: 'ANALISAR';
DESCREVER: 'DESCREVER';
CONTAGEM_VALORES: 'CONTAGEM_VALORES';
PNULL:    'PNULL';   // preencher valores nulos

LPAREN: '(';
RPAREN: ')';
COMMA: ',';
COLON: ':';

ID:     [a-zA-Z_][a-zA-Z_0-9]*;
NUMBER: [0-9]+ ('.' [0-9]+)?;
STRING: '"' ( ~["] | '""' )* '"';

WHITESPACE:   [ \t\r\n]+ -> skip;