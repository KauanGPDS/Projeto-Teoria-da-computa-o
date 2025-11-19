// Define que este arquivo contém a gramática combinada (léxica e sintática)
grammar MinhaLinguagem;

/*
 * ========================================
 * II. REGRAS SINTÁTICAS (O PARSER)
 * ========================================
 */

// A regra inicial: um programa é um conjunto de declarações ou comandos
program : (declaracao | comando)+;

// --- Declaração de Variáveis (Requisito: 3 tipos) ---
declaracao : tipo ID (',' ID)* ';';
tipo       : 'int' | 'float' | 'string'; // 3 tipos de variáveis

// --- Comandos Principais ---
comando
    : declaracao                     // Permitir declaração em qualquer lugar
    | atribuicao ';'                 // Atribuição (ex: a = 5;)
    | estruturaIf                    // if...else
    | estruturaWhile                 // loop 1
    | estruturaFor                   // loop 2
    | leitura ';'                    // scanf
    | escrita ';'                    // printf
    | expressao ';'                  // ex: 5 + 3; (embora inútil, é válido)
    | bloco                          // um bloco de comandos { ... }
    ;

bloco : '{' (comando)* '}';

// --- Atribuição (Requisito) ---
atribuicao : ID '=' expressao;

// --- Estruturas de Controle (Requisito) ---
estruturaIf : 'if' '(' expressao ')' comando ('else' comando)?; // if...else
estruturaWhile : 'while' '(' expressao ')' comando;           // while
estruturaFor : 'for' '(' atribuicao ';' expressao ';' atribuicao ')' comando; // for

// --- Leitura e Escrita (Requisito) ---
leitura : 'scanf' '(' ID ')' ;
escrita : 'printf' '(' (expressao | STRING_LITERAL) ')' ;

/*
 * --- Expressões com Precedência (Requisito) ---
 */

expressao
    : termo ( (ADD | SUB | GT | LT | EQ) termo )* // Adicionado GT, LT, EQ
    ;

termo
    : fator ( (MUL | DIV) fator )*
    ;

// Fator modificado para aceitar strings literais também
fator
    : '(' expressao ')'      // ( 1 + 2 )
    | ID                     // variavel
    | INT                    // 123
    | FLOAT                  // 123.45
    | STRING_LITERAL         // "ola"  <--- CORREÇÃO AQUI
    ;


/*
 * ========================================
 * I. REGRAS LÉXICAS (OS TOKENS)
 * ========================================
 */

// --- Operadores ---
ADD : '+';
SUB : '-';
MUL : '*';
DIV : '/';
GT  : '>'; // <--- CORREÇÃO AQUI
LT  : '<'; // <--- CORREÇÃO AQUI
EQ  : '==';

// --- Literais e IDs ---
ID : [a-zA-Z_] [a-zA-Z_0-9]*; // Nome da variável

// --- Números (Requisito: aceitar decimais) ---
INT   : [0-9]+;
FLOAT : [0-9]+ '.' [0-9]+;

// String literal simples
STRING_LITERAL : '"' ( ~["] | '""' )* '"' ;

// --- Espaços em branco (Requisito: ignorar) ---
WS : [ \t\r\n]+ -> skip; // 'skip' joga o token fora

// Comentários (Bônus, mas útil)
COMMENT_LINE : '//' .*? '\n' -> skip;