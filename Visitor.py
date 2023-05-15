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
    print(blank(),sep='',end='')
    stmExp.exp1.accept(self)
    print('')

  def visitStmWhile(self, stmWhile):
    print (blank(), 'while (', end='', sep='')
    stmWhile.exp1.accept(self)
    print (')', end='', sep='')
    stmWhile.body.accept(self)
    
  def visitStmReturn(self, stmReturn):
    print (blank(), 'return ', end='', sep='')
    stmReturn.exp1.accept(self)
    print (';')

  def visitStmIfElse(self, stmIfElse):
    print ('if (', end='', sep='')
    stmIfElse.exp1.accept(self)
    print (')', end='', sep='')
    stmIfElse.body1.accept(self)
    print ('else ', end='', sep='')
    stmIfElse.body2.accept(self)

  def visitStmIf(self, stmIf):
    print ('if (', end='', sep='')
    stmIf.exp1.accept(self)
    print (')', end='', sep='')
    stmIf.body.accept(self)

  def visitStmVariable(self, stmVariable):
    stmVariable.variable.accept(self)

  def visitStmOptExp(self, stmOptExp):
    stmOptExp.optexp.accept(self)

  def visitStmFor(self, stmFor):
    print ('for (', end='', sep='')
    stmFor.optexp1.accept(self)
    print ('; ')
    stmFor.optexp2.accept(self)
    print ('; ')
    stmFor.optexp3.accept(self)
    print (')', end='', sep='')
    stmFor.body.accept(self)

  def visitVariableConcrete(self, variableConcrete):
    variableConcrete.type.accept(self)
    variableConcrete.assign.accept(self)

  def visitTypeInt(self, typeInt):
    typeInt.typeint.accept(self)