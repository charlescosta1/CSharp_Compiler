# ------------------------- #
# ExpressionLanguageLex.py  #
#-------------------------- #

import ply.lex as lex

reservadas = {
  'bool': 'BOOL',
  'break': 'BREAK',
  'case': 'CASE',
  'catch': 'CATCH',
  'char': 'CHAR',
  'class': 'CLASS',
  'const': 'CONST',
  'decimal': 'DECIMAL',
  'do': 'DO',
  'double': 'DOUBLE',
  'else': 'ELSE',
  'enum': 'ENUM',
  'float': 'FLOAT',
  'for': 'FOR',
  'foreach': 'FOREACH',
  'goto': 'GOTO',
  'if': 'IF',
  'in': 'IN',
  'int': 'INT',
  'interface': 'INTERFACE',
  'is': 'IS',
  'long': 'LONG',
  'namespace': 'NAMESPACE',
  'new': 'NEW',
  'object': 'OBJECT',
  'out': 'OUT',
  'override': 'OVERRIDE',
  'params': 'PARAMS',
  'private': 'PRIVATE',
  'protected': 'PROTECTED',
  'public': 'PUBLIC',
  'readonly': 'READONLY',
  'ref': 'REF',
  'return': 'RETURN',
  'short': 'SHORTE',
  'sizeof': 'SIZEOF',
  'static': 'STATIC',
  'string': 'STRING',
  'struct': 'STRUCT',
  'switch': 'SWITCH',
  'this': 'THIS',
  'throw': 'THROW',
  'try': 'TRY',
  'typeof': 'TYPEOF',
  'uint': 'UINT',
  'ulong': 'ULONG',
  'usafe': 'USAFE',
  'ushort': 'USHORT',
  'void': 'VOID',
  'while': 'WHILE',
  # ---------------------------- #
  # Palavras-chave contextuais   #
  # ---------------------------- #
  'equals': 'EQUALS',
  'notnull': 'NOTNULL',
  'or': 'OR',
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
  'NUMBERFLOATALL',
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
  'LCOL',
  'LITERALSTRING',
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

t_LINHA = '[a-zA-Z][a-zA-Z \t]+'


def t_error(t):
  print("ERROR in INITIAL state")
  print(t.value)
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


def t_NUMBERFLOATALL(t):
  r'(\d+\.\d+)'
  return t


def t_ID(t):
  r'[a-zA-Z_][a-zA-Z_0-9]*'
  t.type = reservadas.get(t.value, 'ID')
  return t


def t_NUMBERINT(t):
  r'\d+'
  t.value = int(t.value)
  return t


def t_LITERALSTRING(t):
  r'\"([^\\]|(\\.))*?\"'
  return t


def t_COMMENT(t):
  r'(//.*)|(/\*(.|\n)*?\*/)'
  pass


def t_ATRIBUICAO(t):
  r'(\+\=)|(\-\=)|(\*\=)|(\/\=)|(\%\=)|(\&\=)|(\^\=)|(\|\=)|(\<<=)|(\>>=)|(\>>>=)'
  return t


def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)


t_ignore = ' \t'

# lexer = lex.lex()
# TESTAR OS OPEADORES:

# lexer.input(
#   " = + - * ( ) , . { } ; $ > < >= <= ^ & | ~ && || ?: ++ -- += -= *= /= %= &= ^= |= <<= >>= >>>= 1 1.90 1.75f 1.75F 1.75d #1.75D 1.85m 1.85M"
#   + ('"teste"') + "//COMMENT1\n" + "///COMMENT2\n" + "/*COMMENT3\nvárias linhas?\n?*/")
