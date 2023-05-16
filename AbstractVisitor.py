from abc import abstractmethod, ABCMeta

class AbstractVisitor(metaclass = ABCMeta):

  @abstractmethod
  def visitFuncDeclConcrete(self, funcDeclConcrete): pass
    
  @abstractmethod
  def visitModifierPublic(self, modifierPublic): pass

  @abstractmethod
  def visitModifierStatic(self, modifierStatic): pass

  @abstractmethod
  def visitModifierId(self, modifierId): pass

  @abstractmethod
  def visitModifierType(self, modifierType): pass

  @abstractmethod
  def visitSignatureId(self, signatureId): pass

  @abstractmethod
  def visitSignatureType(self, signatureType): pass

  @abstractmethod
  def visitSingleSigParams(self, singleSigParams): pass

  @abstractmethod
  def visitCompoundSigParams(self, compoundSigParams): pass

  @abstractmethod
  def visitBodyConcrete(self, bodyConcrete): pass

  @abstractmethod
  def visitSingleStm(self, singleStm): pass

  @abstractmethod
  def visitStmExp(self, stmExp): pass

  @abstractmethod
  def visitStmWhile(self, stmWhile): pass

  @abstractmethod
  def visitStmReturn(self, stmReturn): pass

  @abstractmethod
  def visitStmIfElse(self, stmIfElse): pass

  @abstractmethod
  def visitStmIf(self, stmIf): pass

  @abstractmethod
  def visitStmVariable(self, stmVariable): pass

  @abstractmethod
  def visitStmOptExp(self, stmOptExp): pass

  @abstractmethod
  def visitStmFor(self, stmFor): pass

  @abstractmethod
  def visitVariableConcrete(self, variableConcrete): pass

  @abstractmethod
  def visitTypeInt(self, typeInt): pass

  @abstractmethod
  def visitTypeString(self, typeString): pass

  @abstractmethod
  def visitTypeFloat(self, typeFloat): pass

  @abstractmethod
  def visitTypeBool(self, typeBool): pass

  @abstractmethod
  def visitTypeFloatDecimal(self, typeFloatDecimal): pass

  @abstractmethod
  def visitTypeFloatDouble(self, typeFloatDouble): pass

  @abstractmethod
  def visitTypeVoid(self, typeVoid): pass

  @abstractmethod
  def visitExpAtribuicao(self, expAtribuicao): pass

  @abstractmethod
  def visitExpLcor(self, expLcor): pass

  @abstractmethod
  def visitExpLcand(self, expLcand): pass

  @abstractmethod
  def visitExpOR(self, expOR): pass

  @abstractmethod
  def visitExpLand(self, expLand): pass

  @abstractmethod
  def visitExpIgual(self, expIgual): pass

  @abstractmethod
  def visitDiferente(self, expDiferente): pass

  @abstractmethod
  def visitMenor(self, expMenor): pass

  @abstractmethod
  def visitMenorIgual(self, expMenorIgual): pass

  @abstractmethod
  def visitMaior(self, expMaior): pass

  @abstractmethod
  def visitMaiorIgual(self, expMaiorIgual): pass

  @abstractmethod
  def visitSoma(self, expSoma): pass

  @abstractmethod
  def visitSubtracao(self, expSubtracao): pass

  @abstractmethod
  def visitVezes(self, expVezes): pass

  @abstractmethod
  def visitDivisao(self, expDivisao): pass

  @abstractmethod
  def visitIncremento(self, expIncremento): pass

  @abstractmethod
  def visitDecremento(self, expDecremento): pass

  @abstractmethod
  def visitExpBool(self, expBool): pass
    
  @abstractmethod
  def visitExpNumberInt(self, expNumberInt): pass
    
  @abstractmethod
  def visitExpNumberFloatall(self, expNumberFloatall): pass

  @abstractmethod
  def visitExpNumberFloat(self, expNumberFloat): pass
    
  @abstractmethod
  def visitCallParams(self, CallParams): pass 

  @abstractmethod
  def visitParamsConcrete(self, ParamsConcrete): pass

  @abstractmethod
  def visitParamsExp(self, ParamsExp): pass

  @abstractmethod
  def visitAssignArrayExp(self, AssignArrayExp): pass

  @abstractmethod
  def visitArray(self, AssignArray): pass

  @abstractmethod
  def visitAssignId(self, AssignId): pass