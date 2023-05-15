from abc import abstractmethod
from abc import ABCMeta


class Program(metaclass=ABCMeta):

  @abstractmethod
  def accept(self, visitor):
    pass


class ProgramConcrete1(Program):

  def __init__(self, funcdecl):
    self.funcdecl = funcdecl

  def accept(self, visitor):
    return visitor.visitProgramConcrete1(self)


class ProgramConcrete2(Program):

  def __init__(self, program, funcdecl):
    self.program = program
    self.funcdecl = funcdecl

  def accept(self, visitor):
    return visitor.visitProgramConcrete2(self)


class FuncDecl(metaclass=ABCMeta):

  @abstractmethod
  def accept(self, visitor):
    pass


class FuncDeclConcrete(FuncDecl):

  def __init__(self, signature, body):
    self.signature = signature
    self.body = body

  def accept(self, visitor):
    return visitor.visitFuncDeclConcrete(self)


class modifier(metaclass=ABCMeta):

  @abstractmethod
  def accept(self, visitor):
    pass


class ModifierPublic(modifier):

  def __init__(self, modifier):
    self.modifier = modifier

  def accept(self, visitor):
    return visitor.visitModifierPublic(self)


class ModifierStatic(modifier):

  def __init__(self, modifier):
    self.modifier = modifier

  def accept(self, visitor):
    return visitor.visitModifierStatic(self)


class ModifierId(modifier):

  def __init__(self, modifier):
    self.modifier = modifier

  def accept(self, visitor):
    return visitor.visitModifierId(self)


class ModifierType(modifier):

  def __init__(self, modifier):
    self.modifier = modifier

  def accept(self, visitor):
    return visitor.visitModifierType(self)


class Signature(metaclass=ABCMeta):

  @abstractmethod
  def accept(self, visitor):
    pass


class SignatureId(Signature):

  def __init__(self, modifier, id, sigParams):
    self.modifier = modifier
    self.id = id
    self.sigParams = sigParams

  def accept(self, visitor):
    return visitor.visitSignatureId(self)


class SignatureType(Signature):

  def __init__(self, modifier, type, id, sigParams):
    self.modifier = modifier
    self.type = type
    self.id = id
    self.sigParams = sigParams

  def accept(self, visitor):
    return visitor.visitSignatureType(self)


class SigParams(metaclass=ABCMeta):

  @abstractmethod
  def accept(self, visitor):
    pass


class SingleSigParams(SigParams):

  def __init__(self, type, id):
    self.type = type
    self.id = id

  def accept(self, visitor):
    return visitor.visitSingleSigParams(self)


class CompoundSigParams(SigParams):

  def __init__(self, type, id, sigParams):
    self.type = type
    self.id = id
    self.sigParams = sigParams

  def accept(self, visitor):
    return visitor.visitCompoundSigParams(self)


class Body(metaclass=ABCMeta):

  @abstractmethod
  def accept(self, visitor):
    pass


class BodyConcrete(Body):

  def __init__(self, stms):
    self.stms = stms

  def accept(self, visitor):
    return visitor.visitBodyConcrete(self)


class Stms(metaclass=ABCMeta):

  @abstractmethod
  def accept(self, visitor):
    pass


class SingleStm(Stms):

  def __init__(self, stm):
    self.stm = stm

  def accept(self, visitor):
    return visitor.visitSingleStm(self)


class CompoundStm(Stms):

  def __init__(self, stm, stms):
    self.stm = stm
    self.stms = stms

  def accept(self, visitor):
    return visitor.visitCompoundStm(self)


class Stm(metaclass=ABCMeta):

  @abstractmethod
  def accept(self, visitor):
    pass


class StmExp(Stm):

  def __init__(self, exp1):
    self.exp1 = exp1

  def accept(self, visitor):
    return visitor.visitStmExp(self)


class StmWhile(Stm):

  def __init__(self, exp1, body):
    self.exp1 = exp1
    self.body = body

  def accept(self, visitor):
    return visitor.visitStmWhile(self)


class StmReturn(Stm):

  def __init__(self, exp1):
    self.exp1 = exp1

  def accept(self, visitor):
    return visitor.visitStmReturn(self)


class StmIfElse(Stm):

  def __init__(self, exp1, body1, body2):
    self.exp1 = exp1
    self.body1 = body1
    self.body2 = body2

  def accept(self, visitor):
    return visitor.visitStmIfElse(self)


class StmIf(Stm):

  def __init__(self, exp1, body):
    self.exp1 = exp1
    self.body = body

  def accept(self, visitor):
    return visitor.visitStmIf(self)


class StmVariable(Stm):

  def __init__(self, variable):
    self.variable = variable

  def accept(self, visitor):
    return visitor.visitStmVariable(self)


class StmOptExp(Stm):

  def __init__(self, optexp):
    self.optexp = optexp

  def accept(self, visitor):
    return visitor.visitStmOptExp(self)


class StmFor(Stm):

  def __init__(self, optexp1, optexp2, optexp3, body):
    self.optexp1 = optexp1
    self.optexp2 = optexp2
    self.optexp3 = optexp3
    self.body = body

  def accept(self, visitor):
    return visitor.visitStmFor(self)


class variable(metaclass=ABCMeta):

  @abstractmethod
  def accept(self, visitor):
    pass


class VariableConcrete(variable):

  def __init__(self, type, assign):
    self.type = type
    self.assign = assign

  def accept(self, visitor):
    return visitor.visitVariableConcrete(self)


class type(metaclass=ABCMeta):

  @abstractmethod
  def accept(self, visitor):
    pass


class TypeInt(type):

  def __init__(self, typeint):
    self.typeint = typeint

  def accept(self, visitor):
    return visitor.visitTypeInt(self)


class TypeString(type):

  def __init__(self, typestring):
    self.typestring = typestring

  def accept(self, visitor):
    return visitor.visitTypeString(self)


class TypeFloat(type):

  def __init__(self, typefloat):
    self.typefloat = typefloat

  def accept(self, visitor):
    return visitor.visitTypeFloat(self)


class TypeBool(type):

  def __init__(self, typebool):
    self.typebool = typebool

  def accept(self, visitor):
    return visitor.visitTypeBool(self)


class TypeFloatDecimal(type):

  def __init__(self, typefloatdecimal):
    self.typefloatdecimal = typefloatdecimal

  def accept(self, visitor):
    return visitor.visitTypeFloatDecimal(self)


class TypeFloatDouble(type):

  def __init__(self, typefloatdouble):
    self.typefloatdouble = typefloatdouble

  def accept(self, visitor):
    return visitor.visitTypeFloatDouble(self)


class TypeVoid(type):

  def __init__(self, typevoid):
    self.typevoid = typevoid

  def accept(self, visitor):
    return visitor.visitTypeVoid(self)


class exp(metaclass=ABCMeta):

  @abstractmethod
  def accept(self, visitor):
    pass


class ExpAtribuicao(exp):

  def __init__(self, exp1, exp2):
    self.exp1 = exp1
    self.exp2 = exp2

  def accept(self, visitor):
    return visitor.visitExpAtribuicao(self)


class ExpLcor(exp):

  def __init__(self, exp1, exp2):
    self.exp1 = exp1
    self.exp2 = exp2

  def accept(self, visitor):
    return visitor.visitExpLcor(self)


class ExpLcand(exp):

  def __init__(self, exp1, exp2):
    self.exp1 = exp1
    self.exp2 = exp2

  def accept(self, visitor):
    return visitor.visitExpLand(self)


class ExpOR(exp):

  def __init__(self, exp1, exp2):
    self.exp1 = exp1
    self.exp2 = exp2

  def accept(self, visitor):
    return visitor.visitExpOR(self)


class ExpExor(exp):

  def __init__(self, exp1, exp2):
    self.exp1 = exp1
    self.exp2 = exp2

  def accept(self, visitor):
    return visitor.visitExor(self)


class ExpLand(exp):

  def __init__(self, exp1, exp2):
    self.exp1 = exp1
    self.exp2 = exp2

  def accept(self, visitor):
    return visitor.visitLand(self)


class ExpIgual(exp):

  def __init__(self, exp1, exp2):
    self.exp1 = exp1
    self.exp2 = exp2

  def accept(self, visitor):
    return visitor.visitIgual(self)


class ExpDiferente(exp):

  def __init__(self, exp1, exp2):
    self.exp1 = exp1
    self.exp2 = exp2

  def accept(self, visitor):
    return visitor.visitDiferente(self)


class ExpMenor(exp):

  def __init__(self, exp1, exp2):
    self.exp1 = exp1
    self.exp2 = exp2

  def accept(self, visitor):
    return visitor.visitMenor(self)


class ExpMenoIgual(exp):

  def __init__(self, exp1, exp2):
    self.exp1 = exp1
    self.exp2 = exp2

  def accept(self, visitor):
    return visitor.visitMenorIgual(self)


class ExpMaior(exp):

  def __init__(self, exp1, exp2):
    self.exp1 = exp1
    self.exp2 = exp2

  def accept(self, visitor):
    return visitor.visitMaior(self)


class ExpMaiorIgual(exp):

  def __init__(self, exp1, exp2):
    self.exp1 = exp1
    self.exp2 = exp2

  def accept(self, visitor):
    return visitor.visitMaiorIgual(self)


class ExpSoma(exp):

  def __init__(self, exp1, exp2):
    self.exp1 = exp1
    self.exp2 = exp2

  def accept(self, visitor):
    return visitor.visitSoma(self)


class ExpSubtracao(exp):

  def __init__(self, exp1, exp2):
    self.exp1 = exp1
    self.exp2 = exp2

  def accept(self, visitor):
    return visitor.visitSubtracao(self)


class ExpVezes(exp):

  def __init__(self, exp1, exp2):
    self.exp1 = exp1
    self.exp2 = exp2

  def accept(self, visitor):
    return visitor.visitVezes(self)


class ExpDivisao(exp):

  def __init__(self, exp1, exp2):
    self.exp1 = exp1
    self.exp2 = exp2

  def accept(self, visitor):
    return visitor.visitDivisao(self)


class ExpIncremento(exp):

  def __init__(self, exp1):
    self.exp1 = exp1

  def accept(self, visitor):
    return visitor.visitIncremento(self)


class ExpDecremento(exp):

  def __init__(self, exp1):
    self.exp1 = exp1

  def accept(self, visitor):
    return visitor.visitDecremento(self)


class ExpBool(exp):

  def __init__(self, exp1):
    self.exp1 = exp1

  def accept(self, visitor):
    return visitor.visitBool(self)


class ExpLiteralString(exp):

  def __init__(self, exp1):
    self.exp1 = exp1

  def accept(self, visitor):
    return visitor.visitLiteralString(self)


class ExpId(exp):

  def __init__(self, exp1):
    self.exp1 = exp1

  def accept(self, visitor):
    return visitor.visitId(self)


class ExpCall(exp):

  def __init__(self, exp1):
    self.exp1 = exp1

  def accept(self, visitor):
    return visitor.visitCall(self)


class ExpNumberInt(exp):

  def __init__(self, exp1):
    self.exp1 = exp1

  def accept(self, visitor):
    return visitor.visitNumberInt(self)


class ExpNumberFloatall(exp):

  def __init__(self, exp1):
    self.exp1 = exp1

  def accept(self, visitor):
    return visitor.visitNumberFloatall(self)


class ExpNumberFloat(exp):

  def __init__(self, exp1):
    self.exp1 = exp1

  def accept(self, visitor):
    return visitor.visitNumberFloat(self)


class ExpNumberDecimal(exp):

  def __init__(self, exp1):
    self.exp1 = exp1

  def accept(self, visitor):
    return visitor.visitNumberDecimal(self)


class ExpNumberDouble(exp):

  def __init__(self, exp1):
    self.exp1 = exp1

  def accept(self, visitor):
    return visitor.visitNumberDouble(self)


class ExpPar(exp):

  def __init__(self, exp1):
    self.exp1 = exp1

  def accept(self, visitor):
    return visitor.visitPar(self)


class call(metaclass=ABCMeta):

  @abstractmethod
  def accept(self, visitor):
    pass


class CallParams(call):

  def __init__(self, id, params):
    self.id = id
    self.params = params

  def accept(self, visitor):
    return visitor.visitCallParams(self)


class params(metaclass=ABCMeta):

  @abstractmethod
  def accept(self, visitor):
    pass


class ParamsConcrete(params):

  def __init__(self, exp, params):
    self.exp = exp
    self.params = params

  def accept(self, visitor):
    return visitor.visitParamsConcrete(self)


class ParamsExp(params):

  def __init__(self, exp):
    self.exp = exp

  def accept(self, visitor):
    return visitor.visitParamsExp(self)


class assign(metaclass=ABCMeta):

  @abstractmethod
  def accept(self, visitor):
    pass


class AssignIgual(assign):

  def __init__(self, id, exp):
    self.id = id
    self.exp = exp

  def accept(self, visitor):
    return visitor.visitAssignIgual(self)


class AssignArrayExp(assign):

  def __init__(self, id, exp1, exp2):
    self.id = id
    self.exp1 = exp1
    self.exp2 = exp2

  def accept(self, visitor):
    return visitor.visitAssignArrayExp(self)


class AssignArray(assign):

  def __init__(self, id, params, exp):
    self.id = id
    self.params = params
    self.exp = exp

  def accept(self, visitor):
    return visitor.visitAssignArray(self)


class AssignId(assign):

  def __init__(self, id):
    self.id = id

  def accept(self, visitor):
    return visitor.visitAssignId(self)
