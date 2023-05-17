from AbstractVisitor import AbstractVisitor
from ExpressionLanguageParser import *

# global tab
tab = 0


def blank():
  p = ''
  for x in range(tab):
    p = p + ' '
  return p


class Visitor(AbstractVisitor):

  def visitFuncDeclConcrete(self, funcDeclConcrete):
    funcDeclConcrete.signature.accept(self)
    funcDeclConcrete.body.accept(self)

  def visitModifierPublic(self, modifierPublic):
    modifierPublic.modifier.accept(self)

  def visitModifierStatic(self, modifierStatic):
    modifierStatic.modifier.accept(self)

  def visitModifierId(self, modifierId):
    modifierId.modifier.accept(self)

  def visitModifierType(self, modifierType):
    modifierType.modifier.accept(self)

  def visitSignatureId(self, signatureId):
    print(blank(), signatureId.modifier, ' ', end='', sep='')
    print(signatureId.id, '(', end='', sep='')
    signatureId.sigParams.accept(self)
    print(' ) ', end='')

  def visitSignatureType(self, signatureType):
    print(blank(), signatureType.modifier, ' ', end='', sep='')
    print(signatureType.type, ' ', end='', sep='')
    print(signatureType.id, end='', sep='')
    print('(', end='', sep='')
    signatureType.sigParams.accept(self)
    print(' ) ', end='')

  def visitSingleSigParams(self, singleSigParams):
    print(singleSigParams.type, ' ', end='', sep='')
    print(singleSigParams.id, ' ', end='', sep='')

  def visitCompoundSigParams(self, compoundSigParams):
    print(compoundSigParams.type, ' ', end='', sep='')
    print(compoundSigParams.id, ', ', end='', sep='')
    compoundSigParams.sigParams.accept(self)

  def visitBodyConcrete(self, bodyConcrete):
    global tab
    print('{ ')
    tab = tab + 3
    if (bodyConcrete.stms != None):
      bodyConcrete.stms.accept(self)
    tab = tab - 3
    print(blank(), ' } ', sep='')

  def visitSingleStm(self, singleStm):
    singleStm.stm.accept(self)

  def visitCompoundStm(self, compoundStm):
    compoundStm.stm.accept(self)
    compoundStm.stms.accept(self)

  def visitStmExp(self, stmExp):
    print(blank(), sep='', end='')
    stmExp.exp1.accept(self)
    print('')

  def visitStmWhile(self, stmWhile):
    print(blank(), 'while (', end='', sep='')
    stmWhile.exp1.accept(self)
    print(')', end='', sep='')
    stmWhile.body.accept(self)

  def visitStmReturn(self, stmReturn):
    print(blank(), 'return ', end='', sep='')
    stmReturn.exp1.accept(self)
    print(';')

  def visitStmIfElse(self, stmIfElse):
    print('if (', end='', sep='')
    stmIfElse.exp1.accept(self)
    print(')', end='', sep='')
    stmIfElse.body1.accept(self)
    print('else ', end='', sep='')
    stmIfElse.body2.accept(self)

  def visitStmIf(self, stmIf):
    print('if (', end='', sep='')
    stmIf.exp1.accept(self)
    print(')', end='', sep='')
    stmIf.body.accept(self)

  def visitStmVariable(self, stmVariable):
    stmVariable.variable.accept(self)

  def visitStmOptExp(self, stmOptExp):
    stmOptExp.optexp.accept(self)

  def visitStmFor(self, stmFor):
    print('for (', end='', sep='')
    stmFor.optexp1.accept(self)
    print('; ')
    stmFor.optexp2.accept(self)
    print('; ')
    stmFor.optexp3.accept(self)
    print(')', end='', sep='')
    stmFor.body.accept(self)

  def visitVariableConcrete(self, variableConcrete):
    variableConcrete.type.accept(self)
    variableConcrete.assign.accept(self)

  def visitTypeInt(self, typeInt):
    typeInt.typeint.accept(self)

  def visitTypeString(self, typeString):
    typeString.typestring.accept(self)

  def visitTypeFloat(self, typeFloat):
    typeFloat.typefloat.accept(self)

  def visitTypeBool(self, typeBool):
    typeBool.typebool.accept(self)

  def visitTypeFloatDecimal(self, typeFloatDecimal):
    typeFloatDecimal.typefloatdecimal.accept(self)

  def visitTypeFloatDouble(self, typeFloatDouble):
    typeFloatDouble.typefloat.accept(self)

  def visitTypeVoid(self, typeVoid):
    typeVoid.typevoid.accept(self)

  def visitExpAtribuicao(self, expAtribuicao):
    expAtribuicao.exp1.accept(self)
    print(' = ', end='')
    expAtribuicao.exp2.accept(self)

  def visitExpLcor(self, expLcor):
    expLcor.exp1.accept(self)
    print(' || ', end='')
    expLcor.exp2.accept(self)

  def visitExpLcand(self, expLcand):
    expLcand.exp1.accept(self)
    print(' && ', end='')
    expLcand.exp2.accept(self)

  def visitExpOR(self, expOR):
    expOR.exp1.accept(self)
    print(' | ', end='')
    expOR.exp2.aceept(self)

  def visitExpLand(self, expLand):
    expLand.exp1.accept(self)
    print(' & ', end='')
    expLand.exp2.accept(self)

  def visitExpIgual(self, expIgual):
    expIgual.exp1.accept(self)
    print(' = ', end='')
    expIgual.exp2.accept(self)

  def visitDiferente(self, expDiferente):
    expDiferente.exp1.accept(self)
    print(' != ', end='')
    expDiferente.exp2.accept(self)

  def visitMenor(self, expMenor):
    expMenor.exp1.accept(self)
    print(' < ', end='')
    expMenor.exp2.accept(self)

  def visitMenorIgual(self, expMenorIgual):
    expMenorIgual.exp1.accept(self)
    print(' <= ', end='')
    expMenorIgual.exp2.accept(self)

  def visitMaior(self, expMaior):
    expMaior.exp1.accept(self)
    print(' > ', end='')
    expMaior.exp2.accept(self)

  def visitMaiorIgual(self, expMaiorIgual):
    expMaiorIgual.exp1.accept(self)
    print(' >= ', end='')
    expMaiorIgual.exp2.accept(self)

  def visitSoma(self, expSoma):
    expSoma.exp1.accept(self)
    print(' + ', end='')
    expSoma.exp2.accept(self)

  def visitSubtracao(self, expSubtracao):
    expSubtracao.exp1.accept(self)
    print(' - ', end='')
    expSubtracao.exp2.accept(self)

  def visitVezes(self, expVezes):
    expVezes.exp1.accept(self)
    print(' * ', end='')
    expVezes.exp2.accept(self)

  def visitDivisao(self, expDivisao):
    expDivisao.exp1.accept(self)
    print(' / ', end='')
    expDivisao.exp2.accept(self)

  def visitIncremento(self, expIncremento):
    expIncremento.exp1.accept(self)
    print(' ++ ', end='')
    expIncremento.exp2.accept(self)

  def visitDecremento(self, expDecremento):
    expDecremento.exp1.accept(self)
    print(' -- ', end='')
    expDecremento.exp2.accept(self)

  def visitExpBool(self, expBool):
    print(expBool.exp1, end='')

  def visitExpLiteralString(self, expLiteralString):
    print(expLiteralString.exp1, end='')

  def visitExpId(self, expId):
    print(expId.exp1, end='')

  def visitExpCall(self, expCall):
    expCall.exp1.accept(self)

  def visitExpNumberInt(self, expNumberInt):
    print(expNumberInt.exp1, end='')

  def visitExpNumberFloatall(self, expNumberFloatall):
    print(expNumberFloatall.exp1, end='')

  def visitExpNumberFloat(self, expNumberFloat):
    print(expNumberFloat.exp1, end='')

  def visitExpNumberDecimal(self, expNumberDecimal):
    print(expNumberDecimal.exp1, end='')

  def visitExpNumberDouble(self, expNumberDouble):
    print(expNumberDouble.exp1, end='')

  def visitExpPar(self, expPar):
    print(' ( ', end='')
    ExpPar.exp1.accept(self)
    print(' ) ', end='')

  def visitCallParams(self, CallParams):
    CallParams.id.accept(self)
    print(' ( ', end='')
    CallParams.params.accept(self)
    print(' ) ', end='')

  def visitParamsConcrete(self, ParamsConcrete):
    ParamsConcrete.exp.accept(self)
    print(' , ', end='')
    ParamsConcrete.params.accept(self)

  def visitParamsExp(self, ParamsExp):
    ParamsExp.exp.accept(self)

  def visitAssignIgual(self, AssignIgual):
    AssignIgual.id.accept(self)
    print(' = ', end='')
    AssignIgual.exp.accept(self)

  def visitAssignArrayExp(self, AssignArrayExp):
    AssignArrayExp.id.accept(self)
    print(' [ ', end='')
    AssignArrayExp.exp1.accept(self)
    print(' ] ', end='')
    print(' = ', end='')
    AssignArrayExp.exp2.accept(self)

  def visitArray(self, AssignArray):
    AssignArray.id.accept(self)
    print(' [ ', end='')
    print(' ] ', end='')
    print(' = ', end='')
    print(' { ', end='')
    AssignArray.params.accept(self)
    print(' } ', end='')
    AssignArray.exp.accept(self)

  def visitAssignId(self, AssignId):
    AssignId.id.accept(self)