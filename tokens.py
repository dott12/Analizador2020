import ply.lex as lex
import ply.yacc as yacc



# TODO: Buscar una manera de definir mas tokens (CREO?)
#'ESCRIBIR','LEER','MIENTRAS','PARA','FINSI','HACER','SI','SINO','CASE','BREAK','DEFAULT','SWITCH','PRINCIPAL'

reservadas = ['INICIO', 'FIN', 'ESCRIBIR', 'LEER']

tokens = reservadas + [
    'NAME','NUMBER',
    'PLUS','MINUS','TIMES','DIVIDE','EQUALS',
    'LPAREN','RPAREN', 'QUOTE'
]

# Tokens

t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_EQUALS  = r'='
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_QUOTE  = r'\''
#t_NAME    = r'[a-zA-Z_][a-zA-Z0-9_]*'


def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    # Aqui es donde se asignan las palabras reservadas
    if t.value.upper() in reservadas:
        t.value = t.value.upper()
        t.type = t.value
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignored characters
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print(f"Illegal character {t.value[0]!r}")
    t.lexer.skip(1)


parkin = lex.lex()

# Precedence rules for the arithmetic operators
precedence = (
    ('left', 'INICIO', 'FIN'),
    ('left','PLUS','MINUS'),
    ('left','TIMES','DIVIDE'),
    ('right','UMINUS'),
    )

# dictionary of names (for storing variables)
names = { }

def p_validprogram(p):
    'program : INICIO block FIN'

# <STAT> -> <EXP>

def p_statement_expr(p):
    'statement : expression'
    print(p[1])

def p_block(p):
    'block : statement'
    print(p[1])

def p_block2(p):
    'block : block expression'
    print(p[1])

# <STAT> -> <ID> EQUALS <NUMBER> | <ID> EQUALS <ID>
def p_statement_assign(p):
    'statement : NAME EQUALS expression'
    names[p[1]] = p[3]

# <OP> -> <NUMBER> PLUS <NUMBER> | <NUMBER> MINUS <NUMBER> | <NUMBER> TIMES <NUMBER> | <NUMBER> DIVIDE <NUMBER>
def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    if p[2] == '+'  : print("Valid SUM: " + str(p[1]) + " + " + str(p[3]))
    elif p[2] == '-': print("Valid MIN: " + str(p[1]) + " - " + str(p[3]))
    elif p[2] == '*': print("Valid MLT: " + str(p[1]) + " * " + str(p[3]))
    elif p[2] == '/': print("Valid DIV: " + str(p[1]) + " / " + str(p[3]))


def p_string(p):
    'string : QUOTE expression QUOTE'

def p_write(p):
    '''expression : ESCRIBIR expression
                |  ESCRIBIR string'''

def p_read(p):
    'expression : LEER expression'

def p_expression_uminus(p):
    'expression : MINUS expression %prec UMINUS'
    p[0] = -p[2]

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_expression_name(p):
    'expression : NAME'
    try:
        p[0] = names[p[1]]
    except LookupError:
        print(f"Undefined name {p[1]!r}")
        p[0] = 0


def p_error(p):
    print(f"Syntax error at {p.value!r}")


test = yacc.yacc(debug=True)

def analyze(input):
    return test.parse(input, debug=True)