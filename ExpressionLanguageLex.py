# -------------------------
# ExpressionLanguageLex.py
#----------------------
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

  # -------------------------
  ### Palavras-chave contextuais
  # -------------------------
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
  'with': 'WIHT',
  'yield': 'YIELD',
  'null': 'NULL',
  'false': 'FALSE',
  'true': 'TRUE',
  'default': 'DEFAULT'
}

tokens = [
  'COMMA', 'SOMA', 'ID', 'NUMBER', 'VEZES', 'POT', 'LPAREN', 'RPAREN', 'IGUAL',
  'LCHAV', 'RCHAV', 'PV'
] + list(reservadas.values())

t_IGUAL = r'='
t_SOMA = r'\+'
t_VEZES = r'\*'
t_POT = r'\^'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','
t_LCHAV = r'{'
t_RCHAV = r'}'
t_PV = r';'


