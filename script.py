import ply.lex as lex
import re
#import ply.yacc as yacc

tokens = ['NAME','STR_CONST','ID','INT','FLOAT','PLUS','MINUS','MULTIPLY','MOD','DIVIDE','COMMA','COLON','PARANOPEN','PARANCLOSE','EMP_LIST','EMP_TUPLE','EMP_SET','FLOWEROPEN','FLOWERCLOSE','EQUAL','GREATER','LESSER','GREATEREQ','LESSEREQ','EQEQ','NOTEQ','BIT_AND','BIT_OR','NEWLINE','LEVEL3','LEVEL2','LEVEL1','NEWLINE', 'HASH']

reserved = {'if':'IF','in':'IN','for':'FOR','range':'RANGE','print':'PRINT','True':'BOOL','False':'BOOL','and':'AND','or':'OR','while':'WHILE','def':'DEF'}

symbol_table=[]
level=0




tokens = tokens + list(reserved.values())

# t_ignore=' '
t_ignore_COMMENT=r'[#].* | \'\'\'.*\'\'\''
t_PLUS=r'\+'
t_MINUS=r'\-'
t_MOD=r'%'
t_MULTIPLY=r'\*'
t_DIVIDE=r'/'
t_EQUAL=r'='
t_COMMA=r','
t_COLON=r':'
t_PARANOPEN=r'\('
t_PARANCLOSE=r'\)'
t_FLOWEROPEN=r'{'
t_FLOWERCLOSE=r'}'
t_GREATER=r'>'
t_LESSER=r'<'
t_GREATEREQ=r'>='
t_LESSEREQ=r'<='
t_EQEQ=r'=='
t_NOTEQ=r'!='
t_BIT_AND=r'&'
t_BIT_OR=r'\|'
t_EMP_LIST=r'\[\]'
t_EMP_TUPLE=r'\(\)'
t_EMP_SET=r'\{\}'
t_NEWLINE=r'\n'
t_HASH=r'\#'


def t_error(t):
    #print "ERROR"
    t.lexer.skip(1)

def t_newline(t):
    r'\n+'
    # print("nlvalue",len(t.value))
    t.type='NEWLINE'
    t.value='newline'
    t.lexer.lineno = t.lexer.lineno + len(t.value)
    # print("lineno",t.lexer.lineno)
    return t
def t_level3(t):
    r'\s{12}'
    print("tab3")
    t.type='LEVEL3'
    t.value='level3'
    return t
    # global level
    # level=3


def t_level2(t):
    r'\s{8}'
    print("tab2")
    t.type='LEVEL2'
    t.value='level2'
    return t
    # global level
    # print(level)
    # level=2
def t_level1(t):
    r'\s{4} | [\t]'
    print("tab1")
    t.type='LEVEL1'
    t.value='level1'
    return t
    # global level
    # level=1
    # print(level)
    



def t_NUMBER(t):
    r'[\d.]+(?:E-?.\d+)?'
    if '.' in t.value:
        t.value=float(t.value)
        t.type='FLOAT'
    else:
        t.value = int(t.value)
        t.type='INT'
    return t
# def t_FLOAT(t):
#     r'^[-+]?[0-9]+\.[0-9]+[eE][-+]?[0-9]+$'
#     # print("string",t.value)
#     t.value=float(t.value)
#     print(t.value)
#     return t

def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if len(t.value)>31:
        print("identifier is exceeding 31 characters")
        t.value=t.value[:31]
        print(len(t.value))
        print("new",t.value)
    if t.value in reserved:
        t.type=reserved[t.value]
    else:
        t.type="ID"
    return t       

def t_COMMENT(t):
    r'[#].*'
    t.lexer.skip(1)

def t_MCOMMENT(t):
    r'[\"|\']{3}(.*\n*.*)[\"|\']{3}'
    print("multiline")

def t_STR_CONST(t):
    r'(\'.*\')|(\".*\")'
    return t

def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

lexer = lex.lex()

f = open('inputFile.py')
data = f.read()
# print(data)
lexer.input(data)
tokens_=[]
symbol_tab=dict()
while True:
    tok = lexer.token()
    
    if not tok:
        break
    print(tok)
    tokens_.append(tok)
    # column_no=find_column(data,tok)
    # if tok.value in {'[','{','(',')','}',']'}:
    #     tok.value=ord(tok.value)
    # token=[tok.type,tok.value,tok.lineno,column_no]
    # symbol_table.append(token)
    # print(token)
level_flag="level0"
symbol_tab['level0']=dict()
for i in range(len(tokens_)):
    if tokens_[i].type=='LEVEL1':
        print("encountered colon")
        print(level_flag)
        level_flag='level1'
    elif tokens_[i].type=='LEVEL2':
        level_flag='level2'
    elif tokens_[i].type=='LEVEL3':
        level_flag='level3'
    if not level_flag in symbol_tab.keys():
            print('create')
            symbol_tab[level_flag]=dict()
            print(symbol_tab)
    if tokens_[i].type=='NEWLINE':
        level_flag="level0"

    if tokens_[i].type=='ID' and tokens_[i+1].value=='=':
        symbol_tab[level_flag][tokens_[i].value]=[tokens_[i+2].type, tokens_[i+2].value]
    # print(tokens_[i].type)




print(symbol_tab)





