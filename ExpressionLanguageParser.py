import ply.yacc as yacc
from ExpressionLanguageLex import *
#from ExpressionLanguageParser import *

precedence = (
  ('left', 'ATRIBUICAO'),
  ('right', 'TERNARIO'),
  ('left', 'LCOR'),
  ('left', 'LCAND'),
  ('left', 'INOR'),
  ('left', 'EXOR'),
  ('left', 'LAND'),
  ('left', 'IGUALDADE', 'DIFERENTE'),
  ('left', 'MENOR', 'MAIOR', 'MAIOR_IGUAL', 'MENOR_IGUAL'),
  ('left', 'LSHIFT', 'RSHIFT'),
  ('left', 'SOMA', 'SUBTRACAO'),
  ('left', 'VEZES', 'DIVISAO', 'RESTO'),
  ('right', 'INCREMENTO', 'DECREMENTO', 'PRE_FIX', 'NEGACAO', 'COMPLEMENTO'),
  ('left', 'POS_FIX'),
)
 
def p_program(p):
  '''program : funcdecl 
  | funcdecl program 
  | variable program 
  | variable '''
  pass

def p_funcdecl(p):
  '''funcdecl : signature body '''
  pass


def p_signature(p):
  '''signature : ID ID LPAREN sigparams RPAREN '''
  pass


def p_sigparams(p):
  '''sigparams : ID ID 
  | COMMA sigparams '''
  pass


def p_body(p):
  ''' body : LCHAV stms RCHAV 
  | LCHAV RCHAV '''
  pass


def p_stms(p):
  ''' stms : stm 
  | stm stms '''
  pass


def p_stm(p):
  '''stm : exp PV
    | WHILE LPAREN exp RPAREN body 
                  | RETURN exp PV 
                  | FOR LPAREN exp PV exp PV exp RPAREN body 
                  | IF LPAREN exp RPAREN body ELSE body 
                  | IF LPAREN exp RPAREN body
  '''
  pass
  

def p_variable(p):
  ''' variable : type assign PV 
  | stm '''
  pass

def p_type(p):
  '''type : INT
  | STRING
  | FLOAT
  | BOOL 
  '''
  pass

def p_exp(p):
  ''' exp : exp SOMA exp 
  | exp SUBTRACAO exp
  | exp VEZES exp 
  | exp DIVISAO exp 
  | exp MENOR exp 
  | exp MAIOR exp
  | exp RESTO exp 
  | exp EXOR exp 
  | exp MENOR_IGUAL exp 
  | exp MAIOR_IGUAL exp 
  | exp IGUALDADE exp 
  | exp DIFERENTE exp 
  | exp LCAND exp 
  | exp LCOR exp 
  | exp LAND exp 
  | exp INOR exp 
  | exp COMPLEMENTO exp 
  | exp MAIS_IGUAL exp 
  | exp VEZES_IGUAL exp 
  | exp DIVISAO_IGUAL exp  
  | exp SOBRA_IGUAL exp 
  | exp LAND_IGUAL exp 
  | exp ATRIBUICAO exp
  | exp TERNARIO exp 
  | NEGACAO exp 
  | exp INCREMENTO %prec POS_FIX
  | exp DECREMENTO
  | INCREMENTO exp %prec PRE_FIX
  | DECREMENTO exp 
  | exp LSHIFT exp 
  | exp RSHIFT exp
  | exp IGUAL exp
  | call 
  | assign 
  | ID
  | ID PONTO call
  | NUMBERINT
  | NUMBERFLOAT
  | NUMBERDECIMAL
  | NUMBERDOUBLE
  | NUMBERFLOATALL
  | TRUE
  | FALSE
  | STRING
  '''
  pass
  

def p_call(p):
  ''' call : ID LPAREN params RPAREN 
  | ID LPAREN RPAREN '''
  pass


def p_params(p):
  ''' params : exp COMMA params 
  | exp '''
  pass


def p_assign(p):
  ''' assign : ID IGUAL exp 
      | ID LCOL exp RCOL IGUAL exp 
      | ID LCOL RCOL IGUAL LCHAV params RCHAV exp
      | ID
  '''
  pass

def p_error(p):
    print("Syntax error in input!")