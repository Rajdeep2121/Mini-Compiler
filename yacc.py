# Yacc example
import warnings
import ply.yacc as yacc
# Get the token map from the lexer. This is required.
from lex import tokens
from lex import reserved
from lex import symbol_tab

indentFlag=0

def p_assign(p):
    '''expression : ID EQUAL expression
                    | ID EQUAL EMP_LIST
                    | ID EQUAL EMP_TUPLE
                    | ID EQUAL EMP_SET
                    | ID EQUAL STR_CONST
                    | ID EQUAL ID
                    '''
    p[0] = p[2]
    # print("heere")
    # print(p[1])
    for value in symbol_tab.values():
        for key in value.keys():
            if key==p[1]:
                value[key].append(p[3])
    
        
    global indentFlag
    indentFlag = 0

def p_expression_plus(p):
    '''expression : ID PLUS EQUAL term
                    | expression PLUS term
                    | ID PLUS factor'''
    
   
    if type(p[1])==str:
        # print("its a string")
        for value in symbol_tab.values():
            for key in value.keys():
                if key==p[1]:
                    # print("jhjhk")
                    # print(value[key][3])
                    p[1]=value[key][3]
                    p[0]=p[1]+p[3]
    else:
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
    # if (len(p) == 4):
    #      p[0] = p[1] - p[3]
    # elif (len(p) == 3):
    #      p[0] = -p[2]
    if type(p[1])==str:
        # print("its a string")
        for value in symbol_tab.values():
            for key in value.keys():
                if key==p[1]:
                    # print("jhjhk")
                    # print(value[key][3])
                    p[1]=value[key][3]
                    p[0]=p[1]+p[3]
    else:
        p[0] = p[1] + p[3]

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
    '''expression : LEVEL2 ID EQUAL expression
                  | LEVEL2 ID EQUAL ID
                  | LEVEL2 ID EQUAL STR_CONST'''
    if indentFlag==2:
        p[0] = p[2]
        print("level2   ",p[2])
        for value in symbol_tab.values():
            for key in value.keys():
                if key==p[2]:
                    value[key].append(p[4])

    else:
        print("in else")
        print("Syntax error in input")
        
def p_indent_assign(p):
    '''expression : LEVEL1 ID EQUAL expression
                  | LEVEL1 ID EQUAL ID
                  | LEVEL1 ID EQUAL STR_CONST'''
    if indentFlag==1:
        p[0] = p[2]
        print("level1   ",p[2])
        for value in symbol_tab.values():
            for key in value.keys():
                if key==p[2]:
                    value[key].append(p[4])
        
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

f = open('input1.py')
data = f.read()

data=data.split('\n')

for i in data:
    if(i!=' '):
        print(i)
        yacc.parse(i)

print("###########################")
print("SYMBOL TABLE")
print(symbol_tab)
print("\nID \t\t| TYPE \t\t| LINE NO. \t| SCOPE\t\t| VALUE\n")

if 'level0' in symbol_tab:  
    values0 = list(symbol_tab['level0'].values())
    keys0 = list(symbol_tab['level0'].keys())
    for i in range(len(keys0)):
        values0[i].insert(0,keys0[i])

    for i in values0:
        for j in i:
            print(j,end=' \t\t| ')
        print("level 0")
        print()

if 'level1' in symbol_tab:
    values1 = list(symbol_tab['level1'].values())
    keys1 = list(symbol_tab['level1'].keys())
    for i in range(len(keys1)):
        values1[i].insert(0,keys1[i])

    for i in values1:
        for j in i:
            print(j,end=' \t\t| ')
        print("level 1")
        print()

if 'level2' in symbol_tab:
    values2 = list(symbol_tab['level2'].values())
    keys2 = list(symbol_tab['level2'].keys())
    for i in range(len(keys2)):
        values2[i].insert(0,keys2[i])

    for i in values2:
        for j in i:
            print(j,end=' \t\t| ')
        print("level 2")
        print()
# print(values0)
print("###########################")