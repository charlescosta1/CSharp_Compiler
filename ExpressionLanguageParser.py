import ply.yacc as yacc
from ExpressionLanguageLex import *
import AnaliseAbstrata as sa


def p_program(p):
  '''program : funcdecl 
  | funcdecl program 
  | variable program 
  | variable '''
  if len(p) == 2:
    p[0] = sa.ProgramConcrete1(p[1])
  else:
    p[0] = sa.ProgramConcrete2(p[1], p[2])


def p_funcdecl(p):
  '''funcdecl : signature body '''
  p[0] = sa.FuncDeclConcrete(p[1], p[2])


def p_signature(p):
  '''signature : ID ID LPAREN sigparams RPAREN 
  | ID ID LPAREN RPAREN
  | type ID LPAREN RPAREN
  | type ID LPAREN sigparams RPAREN'''
  if len(p) == 6:
    p[0] = sa.SignatureConcrete(p[1], p[2], p[4])
  else:
    p[0] = sa.SignatureConcrete(p[1], p[2], None)


def p_sigparams(p):
  '''sigparams : ID ID 
  | ID ID COMMA sigparams '''
  if (len(p) == 3):
    p[0] = sa.SingleSigParams(p[1], p[2])
  else:
    p[0] = sa.CompoundSigParams(p[1], p[2], p[4])


def p_body(p):
  ''' body : LCHAV stms RCHAV 
  | LCHAV RCHAV '''
  if (len(p) == 4):
    p[0] = sa.BodyConcrete(p[2])
  else:
    p[0] = sa.BodyConcrete(None)


def p_stms(p):
  ''' stms : stm 
  | stm stms '''
  if (len(p) == 2):
    p[0] = sa.SingleStm(p[1])
  else:
    p[0] = sa.CompoundStm(p[1], p[2])


def p_stm(p):
  '''stm : exp1 PV '''
  p[0] = sa.StmExp(p[1])


def p_stm_while(p):
  '''stm : WHILE LPAREN exp1 RPAREN body '''
  p[0] = sa.StmWhile(p[1], p[3], p[5])


def p_stm_return(p):
  '''stm : RETURN exp1 PV '''
  p[0] = sa.StmReturn(p[1], p[2])


def p_stm_ifelse(p):
  '''stm : IF LPAREN exp1 RPAREN body ELSE body '''
  p[0] = sa.StmIfElse(p[1], p[3], p[5], p[6], p[7])


def p_stm_if(p):
  '''stm : IF LPAREN exp1 RPAREN body '''
  p[0] = sa.StmIfElse(p[1], p[3], p[5], None, None)


def p_stm_variable(p):
  '''stm : variable '''
  p[0] = sa.StmVariable(p[1])


def p_optexp(p):
  '''optexp : exp1
  |
  '''
  p[0] = sa.StmOptExp(p[1])


def p_stm_for(p):
  '''stm : FOR LPAREN optexp PV optexp PV optexp RPAREN body '''
  p[0] = sa.StmFor(p[3], p[5], p[7], p[9])


def p_variable(p):
  ''' variable : type assign PV '''
  pass


def p_type(p):
  '''type : INT '''
  pass


def p_type_string(p):
  '''type : STRING '''
  pass


def p_type_float(p):
  '''type : FLOAT '''
  pass


def p_type_bool(p):
  '''type : BOOL '''
  pass


def p_type_void(p):
  '''type : VOID '''
  pass


def p_exp1(p):
  '''exp1 : exp1 ATRIBUICAO exp2
  | exp2'''
  pass


def p_exp2(p):
  '''exp2 : exp2 LCOR exp3
  | exp3'''
  pass


def p_exp3(p):
  '''exp3 : exp3 LCAND exp4
   | exp4'''
  pass


def p_exp4(p):
  '''exp4 : exp4 OR exp5
   | exp5'''
  pass


def p_exp5(p):
  '''exp5 : exp5 EXOR exp6
  | exp6'''
  pass


def p_exp6(p):
  '''exp6 : exp6 LAND exp7
  | exp7'''
  pass


def p_exp7(p):
  '''exp7 : exp7 IGUAL exp8
  | exp7 DIFERENTE exp8
  | exp8'''
  pass


def p_exp8(p):
  '''exp8 : exp8 MENOR exp9
  | exp8 MENOR_IGUAL exp9
  | exp8 MAIOR exp9
  | exp8 MAIOR_IGUAL exp9
  | exp9'''
  pass


def p_exp9_soma(p):
  '''exp9 : exp9 SOMA exp10
         | exp10'''
  # if len(p) == 2:
  #   p[0] = p[1]
  # else:
  #   p[0] = sa.SomaExp(p[1], p[3])
  pass


def p_exp10_subtracao2(p):
  '''exp10 : exp10 SUBTRACAO exp12 '''
  #  p[0] = sa.SubtracaoExp(p[1], p[3])
  pass


def p_exp10_subtracao1(p):
  '''exp10 : exp12 '''
  #  p[0] = p[1]
  pass


def p_exp12_vezes(p):
  '''exp12 : exp12 VEZES exp13
    | exp13'''
  #if len(p) == 2:
  #p[0] = p[1]
  #else:
  #p[0] = sa.VezesExp(p[1], p[3])
  pass


def p_exp13_divisao(p):
  '''exp13 : exp13 DIVISAO exp14
    | exp14'''
  #if len(p) == 2:
  #p[0] = p[1]
  #else:
  #p[0] = sa.DivisaoExp(p[1], p[3])

  pass


def p_exp14(p):
  '''exp14 : exp14 INCREMENTO
  | exp15 DECREMENTO
  | exp15'''
  pass


def p_exp15(p):
  '''exp15 : TRUE 
  | FALSE
  | LITERALSTRING
  | ID
  | call
  | NUMBERINT
  | LPAREN exp1 RPAREN'''
  pass


def p_call(p):
  ''' call : ID LPAREN params RPAREN 
  | ID LPAREN RPAREN '''
  #if len(p) == 5:
  #  p[0] = sa.ParamsCall(p[1], p[3])
  #else:
  #  p[0] = sa.NoParamsCall(p[1])
  pass


def p_params(p):
  ''' params : exp1 COMMA params 
  | exp1 '''
  #if len(p) == 2:
  #  p[0] = sa.SingleParam(p[1])
  #elif len(p) == 4:
  #  p[0] = sa.CompoundParams(p[1], p[3])
  pass


def p_assign(p):
  ''' assign : ID IGUAL exp1 
      | ID LCOL exp1 RCOL IGUAL exp1 
      | ID LCOL RCOL IGUAL LCHAV params RCHAV exp1
      | ID
  '''
  pass


def p_error(p):
  print("Syntax error in input!")
