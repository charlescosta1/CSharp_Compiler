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


def p_modifier_public(p):
  '''modifier : PUBLIC'''
  p[0] = sa.ModifierPublic(p[1])


def p_modifier_static(p):
  '''modifier : STATIC'''
  p[0] = sa.ModifierStatic(p[1])


def p_signature_id(p):
  '''signature : modifier ID LPAREN sigparams RPAREN'''
  p[0] = sa.SignatureId(p[1], p[2], p[4])


def p_signature_id_noparam(p):
  '''signature : modifier ID LPAREN RPAREN'''
  p[0] = sa.SignatureId(p[1], p[2], None)


def p_signature_modifier_type(p):
  '''signature : modifier type ID LPAREN sigparams RPAREN'''
  p[0] = sa.SignatureType(p[1], p[2], p[3], p[5])


def p_signature_modifier_type_noparam(p):
  '''signature : modifier type ID LPAREN RPAREN'''
  p[0] = sa.SignatureType(p[1], p[2], p[3], None)


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
  p[0] = sa.StmWhile(p[3], p[5])


def p_stm_return(p):
  '''stm : RETURN exp1 PV '''
  p[0] = sa.StmReturn(p[2])


def p_stm_ifelse(p):
  '''stm : IF LPAREN exp1 RPAREN body ELSE body '''
  p[0] = sa.StmIfElse(p[3], p[5], p[7])


def p_stm_if(p):
  '''stm : IF LPAREN exp1 RPAREN body '''
  p[0] = sa.StmIfElse(p[3], p[5])


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
  p[0] = sa.VariableConcrete(p[1], p[2])


def p_type(p):
  '''type : INT '''
  p[0] = sa.TypeInt(p[1])


def p_type_string(p):
  '''type : STRING '''
  p[0] = sa.TypeString(p[1])


def p_type_bool(p):
  '''type : BOOL '''
  p[0] = sa.TypeBool(p[1])


def p_type_float(p):
  '''type : FLOAT '''
  p[0] = sa.TypeFloat(p[1])


def p_type_float_decimal(p):
  '''type : DECIMAL '''
  p[0] = sa.TypeFloatDecimal(p[1])


def p_type_float_double(p):
  '''type : DOUBLE '''
  p[0] = sa.TypeFloatDouble(p[1])


def p_type_void(p):
  '''type : VOID '''
  p[0] = sa.TypeVoid(p[1])


def p_exp1_atribuicao1(p):
  '''exp1 : exp1 ATRIBUICAO exp2 '''
  p[0] = sa.ExpAtribuicao(p[1], p[3])


def p_exp1_atribuicao2(p):
  '''exp1 : exp2 '''
  p[0] = p[1]


def p_exp2_lcor1(p):
  '''exp2 : exp2 LCOR exp3'''
  p[0] = sa.ExpLcor(p[1], p[3])


def p_exp2_lcor2(p):
  '''exp2 : exp3'''
  p[0] = p[1]


def p_exp3_lcand1(p):
  '''exp3 : exp3 LCAND exp4'''
  p[0] = sa.ExpLcand(p[1], p[3])


def p_exp3_lcand2(p):
  '''exp3 : exp4'''
  p[0] = p[1]


def p_exp4_or1(p):
  '''exp4 : exp4 OR exp5 '''
  p[0] = sa.ExpOr(p[1], p[3])


def p_exp4_or2(p):
  '''exp4 : exp5'''
  p[0] = p[1]


def p_exp5_exor1(p):
  '''exp5 : exp5 EXOR exp6 '''
  p[0] = sa.ExpExor(p[1], p[3])


def p_exp4_exor2(p):
  '''exp5 : exp6'''
  p[0] = p[1]


def p_exp6_land1(p):
  '''exp6 : exp6 LAND exp7 '''
  p[0] = sa.ExpLand(p[1], p[3])


def p_exp6_land2(p):
  '''exp6 : exp7'''
  p[0] = p[1]


def p_exp7_igual(p):
  '''exp7 : exp7 IGUAL exp8'''
  p[0] = sa.ExpIgual(p[1], p[3])


def p_exp7_diferente(p):
  '''exp7 : exp7 DIFERENTE exp8'''
  p[0] = sa.ExpDiferente(p[1], p[3])


def p_exp7(p):
  '''exp7 : exp8'''
  p[0] = p[1]


def p_exp8_menor(p):
  '''exp8 : exp8 MENOR exp9 '''
  p[0] = sa.ExpMenor(p[1], p[3])


def p_exp8_menorigual(p):
  '''exp8 : exp8 MENOR_IGUAL exp9 '''
  p[0] = sa.ExpMenorIgual(p[1], p[3])


def p_exp8_maior(p):
  '''exp8 : exp8 MAIOR exp9 '''
  p[0] = sa.ExpMaior(p[1], p[3])


def p_exp8_maiorigual(p):
  '''exp8 : exp8 MAIOR_IGUAL exp9 '''
  p[0] = sa.ExpMaiorIgual(p[1], p[3])


def p_exp8(p):
  '''exp8 : exp9'''
  p[0] = p[1]


def p_exp9_soma1(p):
  '''exp9 : exp9 SOMA exp10'''
  p[0] = sa.ExpSoma(p[1], p[3])


def p_exp9_soma2(p):
  '''exp9 : exp10'''
  p[0] = p[1]


def p_exp10_subtracao1(p):
  '''exp10 : exp10 SUBTRACAO exp12 '''
  p[0] = sa.ExpSubtracao(p[1], p[3])


def p_exp10_subtracao2(p):
  '''exp10 : exp12 '''
  p[0] = p[1]


def p_exp12_vezes1(p):
  '''exp12 : exp12 VEZES exp13 '''
  p[0] = sa.ExpVezes(p[1], p[3])


def p_exp12_vezes2(p):
  '''exp12 : exp13'''
  p[0] = p[1]


def p_exp13_divisao1(p):
  '''exp13 : exp13 DIVISAO exp14 '''
  p[0] = sa.ExpDivisao(p[1], p[3])


def p_exp13_divisao2(p):
  '''exp13 : exp14 '''
  p[0] = p[1]


def p_exp14_incremento(p):
  '''exp14 : exp14 INCREMENTO '''
  p[0] = sa.ExpIncremento(p[1])


def p_exp14_decremento(p):
  '''exp14 : exp14 DECREMENTO '''
  p[0] = sa.ExpDecremento(p[1])


def p_exp14(p):
  '''exp14 : exp15'''
  p[0] = p[1]


def p_exp15_bool(p):
  '''exp15 : TRUE 
            | FALSE '''
  if (p[1] == 'true' or p[1] == 'false'):
    p[0] = sa.ExpBool(p[1])


def p_exp15_literalstring(p):
  '''exp15 : LITERALSTRING'''
  p[0] = sa.ExpLiteralString(p[1])


def p_exp15_id(p):
  '''exp15 : ID'''
  p[0] = sa.ExpId(p[1])


def p_exp15_call(p):
  '''exp15 : call'''
  p[0] = sa.ExpCall(p[1])


def p_exp15_numberint(p):
  '''exp15 : NUMBERINT'''
  p[0] = sa.ExpNumberInt(p[1])


def p_exp15_numberfloatall(p):
  '''exp15 : NUMBERFLOATALL'''
  p[0] = sa.ExpNumberFloatall(p[1])


def p_exp15_numberfloat(p):
  '''exp15 : NUMBERFLOAT'''
  p[0] = sa.ExpNumberFloat(p[1])


def p_exp15_numberdecimal(p):
  '''exp15 : NUMBERDECIMAL'''
  p[0] = sa.ExpNumberDecimal(p[1])


def p_exp15_numberdouble(p):
  '''exp15 : NUMBERDOUBLE'''
  p[0] = sa.ExpNumberDouble(p[1])


def p_exp15_par(p):
  '''exp15 : LPAREN exp1 RPAREN'''
  p[0] = sa.ExpPar(p[1])


def p_call(p):
  ''' call : ID LPAREN params RPAREN '''
  p[0] = sa.CallParams(p[1], p[3])


def p_call_noparams(p):
  ''' call : ID LPAREN RPAREN '''
  p[0] = sa.CallParams(p[1], None)


def p_params(p):
  ''' params : exp1 COMMA params '''
  p[0] = sa.ParamsConcrete(p[1], p[3])


def p_params_exp(p):
  ''' params : exp1 '''
  p[0] = sa.ParamsExp(p[1])


def p_assign(p):
  ''' assign : ID IGUAL exp1 '''
  p[0] = sa.AssignIgual(p[1], p[3])


def p_assign_array_exp(p):
  ''' assign : ID LCOL exp1 RCOL IGUAL exp1 '''
  p[0] = sa.AssignArrayExp(p[1], p[3], p[6])


def p_assign_array(p):
  ''' assign : ID LCOL RCOL IGUAL LCHAV params RCHAV exp1 '''
  p[0] - sa.AssignArray(p[1], p[6], p[8])


def p_assign_id(p):
  ''' assign : ID '''
  p[0] = sa.AssignId(p[1])


def p_error(p):
  print("Syntax error in input!")
