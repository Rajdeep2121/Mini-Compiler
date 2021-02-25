# Yacc example
import warnings
import ply.yacc as yacc
# Get the token map from the lexer. This is required.
from lex import tokens
from lex import reserved

indentFlag=0

def p_assign(p):
    '''expression : ID EQUAL expression
                    | ID EQUAL STR_CONST
                    | ID EQUAL ID
                    '''
    p[0] = p[2]
    global indentFlag
    indentFlag = 0

def p_expression_plus(p):
    '''expression : ID PLUS EQUAL term
                    | expression PLUS term'''
    p[0] = p[1] + p[3]  
   
def p_print_statement(p):
    '''expression : PRINT PARANOPEN STR_CONST PARANCLOSE
                    | PRINT PARANOPEN ID PARANCLOSE
                    | PRINT PARANOPEN term PARANCLOSE'''
    global indentFlag 
    indentFlag=0

def p_expression_minus(p):
    '''expression : expression MINUS term
                    | ID MINUS EQUAL term
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

def p_loops(p):
    '''expression : whileloop
                    | forloop
                    | forloop2
                    | whileloop2'''
def p_while2(p):
    '''whileloop2 : LEVEL1 WHILE PARANOPEN ID EQUAL factor PARANCLOSE COLON 
                    | LEVEL1 WHILE PARANOPEN ID EQUAL STR_CONST PARANCLOSE COLON
                    | LEVEL1 WHILE PARANOPEN ID EQUAL ID PARANCLOSE COLON
                    | LEVEL1 WHILE PARANOPEN ID GREATER factor PARANCLOSE COLON
                    | LEVEL1 WHILE PARANOPEN ID GREATER STR_CONST PARANCLOSE COLON
                    | LEVEL1 WHILE PARANOPEN ID GREATER ID PARANCLOSE COLON
                    | LEVEL1 WHILE PARANOPEN ID GREATEREQ factor PARANCLOSE COLON
                    | LEVEL1 WHILE PARANOPEN ID GREATEREQ STR_CONST PARANCLOSE COLON
                    | LEVEL1 WHILE PARANOPEN ID GREATEREQ ID PARANCLOSE COLON
                    | LEVEL1 WHILE PARANOPEN ID LESSER factor PARANCLOSE COLON
                    | LEVEL1 WHILE PARANOPEN ID LESSER STR_CONST PARANCLOSE COLON
                    | LEVEL1 WHILE PARANOPEN ID LESSER ID PARANCLOSE COLON
                    | LEVEL1 WHILE PARANOPEN ID LESSEREQ factor PARANCLOSE COLON
                    | LEVEL1 WHILE PARANOPEN ID LESSEREQ STR_CONST PARANCLOSE COLON
                    | WHILE PARANOPEN ID LESSEREQ ID PARANCLOSE COLON
                    | LEVEL1 WHILE BOOL COLON
                    | LEVEL1 WHILE STR_CONST COLON
                    | LEVEL1 WHILE factor COLON
                    | LEVEL1 WHILE ID COLON'''
    print("While loop starts")
    global indentFlag
    indentFlag=2

def p_while(p):
    '''whileloop :  WHILE PARANOPEN ID EQUAL factor PARANCLOSE COLON 
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
    global indentFlag
    indentFlag=1

def p_for2(p):
    '''forloop2 : LEVEL1 FOR ID IN RANGE PARANOPEN term PARANCLOSE COLON 
                    | LEVEL1 FOR ID IN RANGE PARANOPEN LEN PARANOPEN ID PARANCLOSE PARANCLOSE COLON
                    | LEVEL1 FOR ID IN STR_CONST COLON
                    | LEVEL1 FOR ID IN ID COLON
                    | LEVEL1 FOR ID IN PARANOPEN STR_CONST PARANCLOSE COLON
                 '''
    global indentFlag
    indentFlag=2
    print("For2 loop starts")
    
def p_for(p):
    '''forloop : FOR ID IN RANGE PARANOPEN term PARANCLOSE COLON 
                    | FOR ID IN RANGE PARANOPEN LEN PARANOPEN ID PARANCLOSE PARANCLOSE COLON
                    | FOR ID IN STR_CONST COLON
                    | FOR ID IN ID COLON
                    | FOR ID IN PARANOPEN STR_CONST PARANCLOSE COLON
                 '''
    global indentFlag
    indentFlag=1
    print("For loop starts")

def p_indent_assign2(p):
    'expression : LEVEL2 ID EQUAL INT'
    if indentFlag==2:
        pass
    else:
        print("Syntax error in input")
        
def p_indent_assign(p):
    '''expression : LEVEL1 ID EQUAL INT
                | LEVEL1 ID EQUAL STR_CONST'''
    if indentFlag==1:
        pass
    else:
        print("Syntax error in input")
def p_indent2_print_statement(p):
    '''expression : LEVEL2 PRINT PARANOPEN STR_CONST PARANCLOSE
                    | LEVEL2 PRINT PARANOPEN ID PARANCLOSE
                    | LEVEL2 PRINT PARANOPEN term PARANCLOSE'''
    if indentFlag==2:
        pass 
    else:
        print("syntax error")
def p_indent_print_statement(p):
    '''expression : LEVEL1 PRINT PARANOPEN STR_CONST PARANCLOSE
                    | LEVEL1 PRINT PARANOPEN ID PARANCLOSE
                    | LEVEL1 PRINT PARANOPEN term PARANCLOSE'''
    if indentFlag==1:
        pass 
    else:
        print("Syntax error in input!")

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

f = open('inputFile.py')
data = f.read()

data=data.split('\n')

for i in data:
    if(i!=' '):
        print(i)
        yacc.parse(i)
   