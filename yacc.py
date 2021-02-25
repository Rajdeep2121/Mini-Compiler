# Yacc example
import ply.yacc as yacc
# Get the token map from the lexer. This is required.
from script import tokens
from script import reserved

def p_assign(p):
    '''expression : ID EQUAL expression
                    | ID EQUAL STR_CONST
                    '''
    if(len(p)==5):
        p[0] = p[2]
    else:
        p[0] = p[1]
def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]  
   
def p_print_statement(p):
    '''expression : PRINT expression
                    | PRINT PARANOPEN ID PARANCLOSE'''

def p_expression_minus(p):
    '''expression : expression MINUS term
                    | MINUS term'''
    if (len(p) == 4):
         p[0] = p[1] - p[3]
    elif (len(p) == 3):
         p[0] = -p[2]

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
    '''expression : WHILE PARANOPEN ID EQUAL factor PARANCLOSE COLON 
                    | WHILE PARANOPEN ID EQUAL STR_CONST PARANCLOSE COLON
                    | WHILE PARANOPEN ID EQUAL ID PARANCLOSE COLON
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

def p_for(p):
    '''expression : FOR ID IN RANGE PARANOPEN expression PARANCLOSE COLON 
                    | FOR ID IN STR_CONST COLON
                    | FOR ID IN ID COLON
                    | FOR ID IN PARANOPEN STR_CONST PARANCLOSE COLON'''
    print("For loop starts")

def p_blank(p):
    'expression : '

def p_comment(p):
    '''expression : HASH expression
                    | HASH ID
                    | HASH STR_CONST'''

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

f = open('input.txt')
data = f.read()

data=data.split('\n')

for i in data:
    # i=i.strip()
    yacc.parse(i)
   
# for i in data:
#     if len(i) > 0:
#         if i[0]=='#':
#             pass 
#         else:
#             i=i.strip()
#             print(i)
#             yacc.parse(i)
   
