# Yacc example
import ply.yacc as yacc
import re 
# Get the token map from the lexer. This is required.
from script import *
# from script import reserved

def p_assign(p):
    '''expression : ID EQUAL expression
                    | ID EQUAL STR_CONST'''
    p[0] = p[1]
   
def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]
    print(p[0])

def p_expression_plus_addon(p):
    'expression : ID PLUS EQUAL term'
    p[1] += p[2]
    print(symbol_tab)

def p_print_statement(p):
    'expression : PRINT expression'
    print(p[2])

def p_expression_minus(p):
    '''expression : expression MINUS term
                    | MINUS term'''
    if (len(p) == 4):
         p[0] = p[1] - p[3]
         print(p[0])
    elif (len(p) == 3):
         p[0] = -p[2]
         print(p[0])

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_times(p):
    'term : term MULTIPLY factor'
    p[0] = p[1] * p[3]

def p_term_div(p):
    'term : term DIVIDE factor'
    p[0] = p[1] / p[3]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_num(p):
    '''factor : INT
            | FLOAT'''
    p[0] = p[1]

def p_factor_expr(p):
    'factor : PARANOPEN expression PARANCLOSE'
    p[0] = p[2]

def p_while(p):
    '''expression : WHILE PARANOPEN ID EQUAL EQUAL factor PARANCLOSE COLON
                    | WHILE PARANOPEN ID EQUAL EQUAL STR_CONST PARANCLOSE COLON
                    | WHILE PARANOPEN ID EQUAL EQUAL ID PARANCLOSE COLON
                    | WHILE PARANOPEN ID GREATER factor PARANCLOSE COLON
                    | WHILE PARANOPEN ID GREATER STR_CONST PARANCLOSE COLON
                    | WHILE PARANOPEN ID GREATER ID PARANCLOSE COLON
                    | WHILE PARANOPEN ID GREATEREQ factor PARANCLOSE COLON
                    | WHILE PARANOPEN ID GREATEREQ STR_CONST PARANCLOSE COLON
                    | WHILE PARANOPEN ID GREATEREQ ID PARANCLOSE COLON
                    | WHILE PARANOPEN ID LESSER factor PARANCLOSE COLON
                    | WHILE PARANOPEN ID LESSER STR_CONST PARANCLOSE COLON
                    | WHILE PARANOPEN ID LESSER ID PARANCLOSE COLON
                    | WHILE PARANOPEN ID LESSEREQ factor PARANCLOSE COLON
                    | WHILE PARANOPEN ID LESSEREQ STR_CONST PARANCLOSE COLON
                    | WHILE PARANOPEN ID LESSEREQ ID PARANCLOSE COLON
                    | WHILE BOOL COLON
                    | WHILE STR_CONST COLON
                    | WHILE factor COLON
                    | WHILE ID COLON'''
    print("While loop starts")

def p_comments(p):
    'expression : HASH expression'
    print("comment")

def p_for(p):
    '''expression : FOR ID IN RANGE PARANOPEN expression PARANCLOSE COLON
                    | FOR ID IN STR_CONST COLON
                    | FOR ID IN ID COLON NEWLINE LEVEL1
                    | FOR ID IN PARANOPEN STR_CONST PARANCLOSE COLON'''
    print("For loop starts") 

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()
"""
while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    yacc.parse(s)
"""
f = open('inputFile.py')
data = f.read()

data=data.split('\n')
for i in data:
    try:
        if(i!=''):
            yacc.parse(i)
    except EOFError:
        break

