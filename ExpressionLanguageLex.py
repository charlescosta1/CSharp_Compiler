# ------------------------- #
# ExpressionLanguageLex.py  #
#-------------------------- #

import ply.lex as lex

reservadas = {
  'abstract': 'ABSTRACT',
  'as': 'AS',
  'base': 'BASE',
  'bool': 'BOOL',
  'break': 'BREAK',
  'byte': 'BYTE',
  'case': 'CASE',
  'catch': 'CATCH',
  'char': 'CHAR',
  'checked': 'CHECKED',
  'unchecked': 'UNCHECKED',
  'class': 'CLASS',
  'const': 'CONST',
  'continue': 'CONTINUE',
  'decimal': 'DECIMAL',
  'delegate': 'DELEGATE',
  'do': 'DO',
  'double': 'DOUBLE',
  'else': 'ELSE',
  'enum': 'ENUM',
  'event': 'EVENT',
  'explicit': 'EXPLICIT',
  'implicit': 'IMPLICIT',
  'finally': 'FINALLY',
  'fixed': 'FIXED',
  'float': 'FLOAT',
  'for': 'FOR',
  'foreach': 'FOREACH',
  'goto': 'GOTO',
  'if': 'IF',
  'in': 'IN',
  'int': 'INT',
  'interface': 'INTERFACE',
  'internal': 'INTERNAL',
  'is': 'IS',
  'lock': 'LOCK',
  'long': 'LONG',
  'namespace': 'NAMESPACE',
  'new': 'NEW',
  'object': 'OBJECT',
  'operator': 'OPERATOR',
  'out': 'OUT',
  'override': 'OVERRIDE',
  'params': 'PARAMS',
  'private': 'PRIVATE',
  'protected': 'PROTECTED',
  'public': 'PUBLIC',
  'readonly': 'READONLY',
  'ref': 'REF',
  'return': 'RETURN',
  'sbyte': 'SBYTE',
  'sealed': 'SEALED',
  'short': 'SHORTE',
  'sizeof': 'SIZEOF',
  'stackalloc': 'STACKALLOC',
  'static': 'STATIC',
  'string': 'STRING',
  'struct': 'STRUCT',
  'switch': 'SWITCH',
  'this': 'THIS',
  'throw': 'THROW',
  'try': 'TRY',
  'typeof': 'TYPEOF',
  'uint': 'UNINT',
  'ulong': 'ULONG',
  'usafe': 'USAFE',
  'ushort': 'USHORT',
  'using': 'USING',
  'virtual': 'VIRTUAL',
  'void': 'VOID',
  'volatile': 'VOLATILE',
  'while': 'WHILE',

  # ---------------------------- #
  # Palavras-chave contextuais   #
  # ---------------------------- #
  
  'add': 'ADD',
  'and': 'AND',
  'alias': 'ALIAS',
  'ascending': 'ASCENDING',
  'args': 'ARGS',
  'async': 'ASYNC',
  'await': 'AWAIT',
  'by': 'BY',
  'descending': 'DESCENDING',
  'dynamic': 'DYNAMIC',
  'equals': 'EQUALS',
  'from': 'FROM',
  'get': 'GET',
  'global': 'GLOBAL',
  'group': 'GROUP',
  'init': 'INIT',
  'into': 'INTO',
  'join': 'JOIN',
  'let': 'LET',
  'managed': 'MANAGED',
  'unmanaged': 'UNMANAGED',
  'nameof': 'NAMEOF',
  'nint': 'NINT',
  'not': 'NOT',
  'notnull': 'NOTNULL',
  'nuint': 'NUINT',
  'on': 'ON',
  'or': 'OR',
  'orderby': 'ORDERBY',
  'partial': 'PARTIAL',
  'record': 'RECORD',
  'remove': 'REMOVE',
  'select': 'SELECT',
  'set': 'SET',
  'value': 'VALUE',
  'var': 'VAR',
  'when': 'WHEN',
  'where': 'WHERE',
  'with': 'WITH',
  'yield': 'YIELD',

  # ------------------------ #
  #   Literais Reservadas    #
  # ------------------------ #
  
  'null': 'NULL',
  'false': 'FALSE',
  'true': 'TRUE',
  'default': 'DEFAULT'
}

tokens = [
  'COMMA',
  'SOMA',
  'SUBTRACAO',
  'DIVISAO',
  'ID',
  'NUMBERINT',
  'NUMBERFLOAT',
  'NUMBERDOUBLE',
  'NUMBERDECIMAL',
  'VEZES',
  'LPAREN',
  'RPAREN',
  'IGUAL',
  'PONTO',
  'LCHAV',
  'RCHAV',
  'PV',
  'RESTO',
  'COMMENT',
  'MAIOR',
  'MENOR',
  'MAIOR_IGUAL',
  'MENOR_IGUAL',
  'IGUALDADE',
  'DIFERENTE',
  'MENOS_IGUAL',
  'MAIS_IGUAL',
  'VEZES_IGUAL',
  'DIVISAO_IGUAL',
  'SOBRA_IGUAL',
  'LAND_IGUAL',
  'EXOR',
  'LAND',
  'INOR',
  'COMPLEMENTO',
  'LCAND',
  'LCOR',
  'TERNARIO',
  'ATRIBUICAO',
  'INCREMENTO',
  'DECREMENTO',
  'LINHA', 
  'IDENT',
  'DEDENT',
  'LSHIFT',
  'RSHIFT',
  'NEGACAO',
  'RCOL',
  'LCOL'
] + list(reservadas.values())

t_IGUAL = r'='
t_SOMA = r'\+'
t_SUBTRACAO = r'\-'
t_VEZES = r'\*'
t_DIVISAO = r'\/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','
t_PONTO = r'\.'
t_LCHAV = r'{'
t_RCHAV = r'}'
t_LCOL = r'\['
t_RCOL = r'\]'
t_PV = r';'
t_NEGACAO = r'\!'
t_RESTO = r'\%'
t_MAIOR = r'>'
t_MENOR = r'<'
t_MAIOR_IGUAL = r'>='
t_MENOR_IGUAL = r'<='
t_IGUALDADE = r'=='
t_DIFERENTE = r'!='
t_MENOS_IGUAL = r'-='
t_MAIS_IGUAL = r'\+='
t_VEZES_IGUAL = r'\*='
t_DIVISAO_IGUAL = r'/='
t_SOBRA_IGUAL = r'%='
t_LAND_IGUAL = r'&='
t_EXOR = r'\^'
t_LAND = r'\&'
t_INOR = r'\|'
t_COMPLEMENTO = r'\~'
t_LCAND = r'\&&'
t_LCOR = r'\|\|'
t_TERNARIO = r'\?:'
t_INCREMENTO = r'\+\+'
t_DECREMENTO = r'-\-'
t_LSHIFT = r'\<<'
t_RSHIFT = r'\>>'


stack = [0]
states = (
  ('idstate', 'exclusive'),
  ('dedstate', 'exclusive'),
)
t_LINHA = '[a-zA-Z][a-zA-Z \t]+'

def space_counter(token):
  spaces = 0
  for c in token.value:
    if c == ' ':
      spaces += 1
    elif c == '\t':
      spaces += 8 - (spaces % 8)
  return spaces

def t_breakline(t):
  r'\n+'  #recognizes one or more break lines
  t.lexer.lineno += len(t.value)
  t.lexer.begin('idstate')


def t_idstate_blankline(t):
  r'([ \t]+)\n'  #recognizes a blank line
  # print('t_idstate_blankline')
  pass

def t_idstate_linewithcode(t):
  '([ \t]+) | ([a-zA-Z])'  #recognizes white spaces and tabs or a letter
  # print('t_idstate_linewithcode')
  n_spaces = space_counter(t)
  t.lexer.begin('INITIAL')
  if n_spaces < stack[-1]:
    t.lexer.skip(-len(t.value))
    stack.pop()
    t.type = 'DEDENT'
    t.lexer.begin('dedstate')
    return t
  elif n_spaces > stack[-1]:
    stack.append(n_spaces)
    t.type = 'IDENT'
    return t
  elif n_spaces == 0:
    t.lexer.skip(-1)


def t_dedstate_linewithdedent(t):
  '([ \t]+) | ([a-zA-Z])'  #recognizes white spaces and tabs or a letter
  n_spaces = space_counter(t)
  if n_spaces < stack[-1]:
    t.lexer.skip(-len(t.value))
    stack.pop()
    t.type = 'DEDENT'
    return t
  elif n_spaces >= stack[-1]:
    t.lexer.begin('INITIAL')
    if n_spaces > stack[-1]:
      print('Erro de dedentação --->', n_spaces)
    elif n_spaces == 0:  # If the element starts with a letter
      t.lexer.skip(-1)


def t_error(t):
  print("ERROR in INITIAL state")
  print(t.value)
  t.lexer.skip(1)


def t_idstate_error(t):
  print("ERROR in idstate state")
  t.lexer.skip(1)


def t_dedstate_error(t):
  print("ERROR in dedstate state")
  t.lexer.skip(1)

def t_NUMBERFLOAT(t):
  r'(\d+\.\d+[fF])'
  return t

def t_NUMBERDOUBLE(t):
  r'(\d+\.\d+[dD])'
  return t

def t_NUMBERDECIMAL(t):
  r'(\d+\.\d+[mM])'
  return t
  
def t_FLOAT(t):
  r'\d+\.\d+'
  return t
  
def t_ID(t):
  r'[a-zA-Z_][a-zA-Z_0-9]*'
  t.type = reservadas.get(t.value, 'ID')
  return t

def t_NUMBERINT(t):
  r'\d+'
  t.value = int(t.value)
  return t

def t_STRING(t):
  r'\"([^\\]|(\\.))*?\"'
  return t

def t_COMMENT(t):
  r'(//.*)|(/\*(.|\n)*?\*/)'
  return t

def t_ATRIBUICAO(t):
  r'(\+\=)|(\-\=)|(\*\=)|(\/\=)|(\%\=)|(\&\=)|(\^\=)|(\|\=)|(\<<=)|(\>>=)|(\>>>=)'
  return t

def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)

t_ignore = ' \t'

#def t_error(t):
#  print("Illegal character '%s'" % t.value[0])
#  t.lexer.skip(1)

#lexer = lex.lex()
# TESTAR OS OPEADORES:

#lexer.input(
#  " = + - * ( ) , . { } ; $ > < >= <= ^ & | ~ && || ?: ++ -- += -= *= /= %= &= ^= |= <<= >>= >>>= 1 1.90 1.75f 1.75F 1.75d #1.75D 1.85m 1.85M"
#  + ('"teste"') + "//COMMENT1\n" + "///COMMENT2\n" + "/*COMMENT3\nvárias linhas?\n?*/")
#
#for tok in lexer:
#  print(tok.type, tok.lineno, tok.value, tok.lexpos)  ##


# TESTAR A IDENTAÇÃO:

#lex.lex()
#programa = """cleardef perm
#    if len lsurf   
#                
#       return lalala land
#r sapore torf
#    for i in range len l  
#             s  lili lost
#             p perm
#             for x in pix
#                append tipo tor
#    return r
#"""
#lex.input(programa)
#
#for token in lex.lexer:
#  print('[', token.type, ',', token.value, ']->', stack)