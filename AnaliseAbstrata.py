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


class Signature(metaclass=ABCMeta):

  @abstractmethod
  def accept(self, visitor):
    pass


class SignatureConcrete(Signature):

  def __init__(self, type, id, sigParams):
    self.type = type
    self.id = id
    self.sigParams = sigParams

  def accept(self, visitor):
    return visitor.visitSignatureConcrete(self)


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

  def __init__(self, stm):
    self.stm = stm

  def accept(self, visitor):
    return visitor.visitStmExp(self)


class StmWhile(Stm):

  def __init__(self, type, exp1, body):
    self.type = type
    self.exp1 = exp1
    self.body = body

  def accept(self, visitor):
    return visitor.visitStmWhile(self)


class StmReturn(Stm):

  def __init__(self, stm, exp1):
    self.stm = stm
    self.exp1 = exp1

  def accept(self, visitor):
    return visitor.visitStmReturn(self)


class StmIfElse(Stm):

  def __init__(self, stm1, exp1, body1, stm2, body2):
    self.stm1 = stm1
    self.exp1 = exp1
    self.body1 = body1
    self.stm2 = stm2
    self.body2 = body2

  def accept(self, visitor):
    return visitor.visitStmIfElse(self)


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
