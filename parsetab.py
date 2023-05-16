
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ATRIBUICAO BOOL BREAK CASE CATCH CHAR CLASS COMMA COMMENT COMPLEMENTO CONST DECIMAL DECREMENTO DEDENT DEFAULT DIFERENTE DIVISAO DIVISAO_IGUAL DO DOUBLE ELSE ENUM EQUALS EXOR FALSE FLOAT FOR FOREACH GOTO ID IDENT IF IGUAL IGUALDADE IN INCREMENTO INT INTERFACE IS LAND LAND_IGUAL LCAND LCHAV LCOL LCOR LINHA LITERALSTRING LONG LPAREN LSHIFT MAIOR MAIOR_IGUAL MAIS_IGUAL MENOR MENOR_IGUAL MENOS_IGUAL NAMESPACE NEGACAO NEW NOTNULL NULL NUMBERDECIMAL NUMBERDOUBLE NUMBERFLOAT NUMBERFLOATALL NUMBERINT OBJECT OR OUT OVERRIDE PARAMS PONTO PRIVATE PROTECTED PUBLIC PV RCHAV RCOL READONLY REF RESTO RETURN RPAREN RSHIFT SHORTE SIZEOF SOBRA_IGUAL SOMA STATIC STRING STRUCT SUBTRACAO SWITCH TERNARIO THIS THROW TRUE TRY TYPEOF UINT ULONG USAFE USHORT VEZES VEZES_IGUAL VOID WHILEprogram : funcdecl \n  | funcdecl program \n  | variable program \n  | variable funcdecl : signature body modifier : PUBLICmodifier : STATICsignature : modifier ID LPAREN sigparams RPARENsignature : modifier ID LPAREN RPARENsignature : modifier type ID LPAREN sigparams RPARENsignature : modifier type ID LPAREN RPARENsigparams : ID ID \n  | ID ID COMMA sigparams  body : LCHAV stms RCHAV \n  | LCHAV RCHAV  stms : stm \n  | stm stms stm : exp1 PV stm : WHILE LPAREN exp1 RPAREN body stm : RETURN exp1 PV stm : IF LPAREN exp1 RPAREN body ELSE body stm : IF LPAREN exp1 RPAREN body stm : variable optexp : exp1 optexp : stm : FOR LPAREN optexp PV optexp PV optexp RPAREN body  variable : type assign PV type : INT type : STRING type : BOOL type : FLOAT type : DECIMAL type : DOUBLE type : VOID exp1 : exp1 ATRIBUICAO exp2 exp1 : exp2 exp2 : exp2 LCOR exp3exp2 : exp3exp3 : exp3 LCAND exp4exp3 : exp4exp4 : exp4 OR exp5 exp4 : exp5exp5 : exp5 EXOR exp6 exp5 : exp6exp6 : exp6 LAND exp7 exp6 : exp7exp7 : exp7 IGUAL exp8exp7 : exp7 DIFERENTE exp8exp7 : exp8exp8 : exp8 MENOR exp9 exp8 : exp8 MENOR_IGUAL exp9 exp8 : exp8 MAIOR exp9 exp8 : exp8 MAIOR_IGUAL exp9 exp8 : exp9exp9 : exp9 SOMA exp10exp9 : exp10exp10 : exp10 SUBTRACAO exp12 exp10 : exp12 exp12 : exp12 VEZES exp13 exp12 : exp13exp13 : exp13 DIVISAO exp14 exp13 : exp14 exp14 : exp14 INCREMENTO exp14 : exp14 DECREMENTO exp14 : exp15exp15 : TRUE \n            | FALSE exp15 : LITERALSTRINGexp15 : IDexp15 : callexp15 : NUMBERINTexp15 : NUMBERFLOATALLexp15 : NUMBERFLOATexp15 : NUMBERDECIMALexp15 : NUMBERDOUBLEexp15 : LPAREN exp1 RPAREN call : ID LPAREN params RPAREN  call : ID LPAREN RPAREN  params : exp1 COMMA params  params : exp1  assign : ID IGUAL exp1  assign : ID LCOL exp1 RCOL IGUAL exp1  assign : ID LCOL RCOL IGUAL LCHAV params RCHAV exp1  assign : ID '
    
_lr_action_items = {'INT':([0,2,3,6,14,15,18,19,25,26,32,57,62,64,99,136,137,146,150,],[7,7,7,7,-6,-7,-5,7,-15,7,-23,-27,-14,-18,-20,-19,-22,-21,-26,]),'STRING':([0,2,3,6,14,15,18,19,25,26,32,57,62,64,99,136,137,146,150,],[8,8,8,8,-6,-7,-5,8,-15,8,-23,-27,-14,-18,-20,-19,-22,-21,-26,]),'BOOL':([0,2,3,6,14,15,18,19,25,26,32,57,62,64,99,136,137,146,150,],[9,9,9,9,-6,-7,-5,9,-15,9,-23,-27,-14,-18,-20,-19,-22,-21,-26,]),'FLOAT':([0,2,3,6,14,15,18,19,25,26,32,57,62,64,99,136,137,146,150,],[10,10,10,10,-6,-7,-5,10,-15,10,-23,-27,-14,-18,-20,-19,-22,-21,-26,]),'DECIMAL':([0,2,3,6,14,15,18,19,25,26,32,57,62,64,99,136,137,146,150,],[11,11,11,11,-6,-7,-5,11,-15,11,-23,-27,-14,-18,-20,-19,-22,-21,-26,]),'DOUBLE':([0,2,3,6,14,15,18,19,25,26,32,57,62,64,99,136,137,146,150,],[12,12,12,12,-6,-7,-5,12,-15,12,-23,-27,-14,-18,-20,-19,-22,-21,-26,]),'VOID':([0,2,3,6,14,15,18,19,25,26,32,57,62,64,99,136,137,146,150,],[13,13,13,13,-6,-7,-5,13,-15,13,-23,-27,-14,-18,-20,-19,-22,-21,-26,]),'PUBLIC':([0,2,3,18,25,57,62,],[14,14,14,-5,-15,-27,-14,]),'STATIC':([0,2,3,18,25,57,62,],[15,15,15,-5,-15,-27,-14,]),'$end':([1,2,3,16,17,18,25,57,62,],[0,-1,-4,-2,-3,-5,-15,-27,-14,]),'LCHAV':([4,94,122,124,126,127,128,135,143,149,],[19,-9,133,-8,-11,19,19,-10,19,19,]),'ID':([5,6,7,8,9,10,11,12,13,14,15,19,23,25,26,29,30,32,57,58,59,60,62,64,65,66,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,88,92,95,99,129,131,132,133,134,136,137,144,145,146,150,],[21,22,-28,-29,-30,-31,-32,-33,-34,-6,-7,50,61,-15,50,50,50,-23,-27,50,50,92,-14,-18,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,123,92,-20,50,50,50,50,92,-19,-22,50,50,-21,-26,]),'RCHAV':([19,24,25,26,32,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,62,63,64,86,87,96,98,99,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,119,120,130,136,137,139,141,146,150,],[25,62,-15,-16,-23,-36,-38,-40,-42,-44,-46,-49,-54,-56,-58,-60,-62,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-27,-14,-17,-18,-63,-64,-35,-76,-20,-37,-39,-41,-43,-45,-47,-48,-50,-51,-52,-53,-55,-57,-59,-61,-78,-80,-77,-19,-22,-79,145,-21,-26,]),'WHILE':([19,25,26,32,57,62,64,99,136,137,146,150,],[28,-15,28,-23,-27,-14,-18,-20,-19,-22,-21,-26,]),'RETURN':([19,25,26,32,57,62,64,99,136,137,146,150,],[30,-15,30,-23,-27,-14,-18,-20,-19,-22,-21,-26,]),'IF':([19,25,26,32,57,62,64,99,136,137,146,150,],[31,-15,31,-23,-27,-14,-18,-20,-19,-22,-21,-26,]),'FOR':([19,25,26,32,57,62,64,99,136,137,146,150,],[33,-15,33,-23,-27,-14,-18,-20,-19,-22,-21,-26,]),'TRUE':([19,25,26,29,30,32,57,58,59,62,64,65,66,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,88,99,129,131,132,133,136,137,144,145,146,150,],[47,-15,47,47,47,-23,-27,47,47,-14,-18,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,-20,47,47,47,47,-19,-22,47,47,-21,-26,]),'FALSE':([19,25,26,29,30,32,57,58,59,62,64,65,66,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,88,99,129,131,132,133,136,137,144,145,146,150,],[48,-15,48,48,48,-23,-27,48,48,-14,-18,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,-20,48,48,48,48,-19,-22,48,48,-21,-26,]),'LITERALSTRING':([19,25,26,29,30,32,57,58,59,62,64,65,66,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,88,99,129,131,132,133,136,137,144,145,146,150,],[49,-15,49,49,49,-23,-27,49,49,-14,-18,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,-20,49,49,49,49,-19,-22,49,49,-21,-26,]),'NUMBERINT':([19,25,26,29,30,32,57,58,59,62,64,65,66,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,88,99,129,131,132,133,136,137,144,145,146,150,],[52,-15,52,52,52,-23,-27,52,52,-14,-18,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,-20,52,52,52,52,-19,-22,52,52,-21,-26,]),'NUMBERFLOATALL':([19,25,26,29,30,32,57,58,59,62,64,65,66,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,88,99,129,131,132,133,136,137,144,145,146,150,],[53,-15,53,53,53,-23,-27,53,53,-14,-18,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,-20,53,53,53,53,-19,-22,53,53,-21,-26,]),'NUMBERFLOAT':([19,25,26,29,30,32,57,58,59,62,64,65,66,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,88,99,129,131,132,133,136,137,144,145,146,150,],[54,-15,54,54,54,-23,-27,54,54,-14,-18,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,-20,54,54,54,54,-19,-22,54,54,-21,-26,]),'NUMBERDECIMAL':([19,25,26,29,30,32,57,58,59,62,64,65,66,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,88,99,129,131,132,133,136,137,144,145,146,150,],[55,-15,55,55,55,-23,-27,55,55,-14,-18,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,-20,55,55,55,55,-19,-22,55,55,-21,-26,]),'NUMBERDOUBLE':([19,25,26,29,30,32,57,58,59,62,64,65,66,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,88,99,129,131,132,133,136,137,144,145,146,150,],[56,-15,56,56,56,-23,-27,56,56,-14,-18,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,-20,56,56,56,56,-19,-22,56,56,-21,-26,]),'LPAREN':([19,22,25,26,28,29,30,31,32,33,50,57,58,59,61,62,64,65,66,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,88,99,129,131,132,133,136,137,144,145,146,150,],[29,60,-15,29,66,29,29,69,-23,70,88,-27,29,29,95,-14,-18,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,-20,29,29,29,29,-19,-22,29,29,-21,-26,]),'PV':([20,21,27,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,68,70,86,87,89,96,98,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,119,129,130,138,140,148,],[57,-84,64,-36,-38,-40,-42,-44,-46,-49,-54,-56,-58,-60,-62,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,99,-25,-63,-64,-81,-35,-76,129,-24,-37,-39,-41,-43,-45,-47,-48,-50,-51,-52,-53,-55,-57,-59,-61,-78,-25,-77,144,-82,-83,]),'IGUAL':([21,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,86,87,91,98,107,108,109,110,111,112,113,114,115,116,117,119,121,130,],[58,76,-49,-54,-56,-58,-60,-62,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-63,-64,122,-76,76,-47,-48,-50,-51,-52,-53,-55,-57,-59,-61,-78,132,-77,]),'LCOL':([21,],[59,]),'ELSE':([25,62,137,],[-15,-14,143,]),'ATRIBUICAO':([27,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,67,68,86,87,89,90,96,97,98,100,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,119,120,130,140,148,],[65,-36,-38,-40,-42,-44,-46,-49,-54,-56,-58,-60,-62,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,65,65,-63,-64,65,65,-35,65,-76,65,65,-37,-39,-41,-43,-45,-47,-48,-50,-51,-52,-53,-55,-57,-59,-61,-78,65,-77,65,65,]),'RPAREN':([34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,60,67,86,87,88,93,95,96,97,98,100,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,123,125,130,139,142,144,147,],[-36,-38,-40,-42,-44,-46,-49,-54,-56,-58,-60,-62,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,94,98,-63,-64,119,124,126,-35,127,-76,128,-24,-37,-39,-41,-43,-45,-47,-48,-50,-51,-52,-53,-55,-57,-59,-61,130,-78,-80,-12,135,-77,-79,-13,-25,149,]),'RCOL':([34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,59,86,87,90,96,98,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,119,130,],[-36,-38,-40,-42,-44,-46,-49,-54,-56,-58,-60,-62,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,91,-63,-64,121,-35,-76,-37,-39,-41,-43,-45,-47,-48,-50,-51,-52,-53,-55,-57,-59,-61,-78,-77,]),'COMMA':([34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,86,87,96,98,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,119,120,123,130,],[-36,-38,-40,-42,-44,-46,-49,-54,-56,-58,-60,-62,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-63,-64,-35,-76,-37,-39,-41,-43,-45,-47,-48,-50,-51,-52,-53,-55,-57,-59,-61,-78,131,134,-77,]),'LCOR':([34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,86,87,96,98,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,119,130,],[71,-38,-40,-42,-44,-46,-49,-54,-56,-58,-60,-62,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-63,-64,71,-76,-37,-39,-41,-43,-45,-47,-48,-50,-51,-52,-53,-55,-57,-59,-61,-78,-77,]),'LCAND':([35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,86,87,98,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,119,130,],[72,-40,-42,-44,-46,-49,-54,-56,-58,-60,-62,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-63,-64,-76,72,-39,-41,-43,-45,-47,-48,-50,-51,-52,-53,-55,-57,-59,-61,-78,-77,]),'OR':([36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,86,87,98,104,105,106,107,108,109,110,111,112,113,114,115,116,117,119,130,],[73,-42,-44,-46,-49,-54,-56,-58,-60,-62,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-63,-64,-76,73,-41,-43,-45,-47,-48,-50,-51,-52,-53,-55,-57,-59,-61,-78,-77,]),'EXOR':([37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,86,87,98,105,106,107,108,109,110,111,112,113,114,115,116,117,119,130,],[74,-44,-46,-49,-54,-56,-58,-60,-62,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-63,-64,-76,74,-43,-45,-47,-48,-50,-51,-52,-53,-55,-57,-59,-61,-78,-77,]),'LAND':([38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,86,87,98,106,107,108,109,110,111,112,113,114,115,116,117,119,130,],[75,-46,-49,-54,-56,-58,-60,-62,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-63,-64,-76,75,-45,-47,-48,-50,-51,-52,-53,-55,-57,-59,-61,-78,-77,]),'DIFERENTE':([39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,86,87,98,107,108,109,110,111,112,113,114,115,116,117,119,130,],[77,-49,-54,-56,-58,-60,-62,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-63,-64,-76,77,-47,-48,-50,-51,-52,-53,-55,-57,-59,-61,-78,-77,]),'MENOR':([40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,86,87,98,108,109,110,111,112,113,114,115,116,117,119,130,],[78,-54,-56,-58,-60,-62,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-63,-64,-76,78,78,-50,-51,-52,-53,-55,-57,-59,-61,-78,-77,]),'MENOR_IGUAL':([40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,86,87,98,108,109,110,111,112,113,114,115,116,117,119,130,],[79,-54,-56,-58,-60,-62,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-63,-64,-76,79,79,-50,-51,-52,-53,-55,-57,-59,-61,-78,-77,]),'MAIOR':([40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,86,87,98,108,109,110,111,112,113,114,115,116,117,119,130,],[80,-54,-56,-58,-60,-62,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-63,-64,-76,80,80,-50,-51,-52,-53,-55,-57,-59,-61,-78,-77,]),'MAIOR_IGUAL':([40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,86,87,98,108,109,110,111,112,113,114,115,116,117,119,130,],[81,-54,-56,-58,-60,-62,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-63,-64,-76,81,81,-50,-51,-52,-53,-55,-57,-59,-61,-78,-77,]),'SOMA':([41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,86,87,98,110,111,112,113,114,115,116,117,119,130,],[82,-56,-58,-60,-62,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-63,-64,-76,82,82,82,82,-55,-57,-59,-61,-78,-77,]),'SUBTRACAO':([42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,86,87,98,114,115,116,117,119,130,],[83,-58,-60,-62,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-63,-64,-76,83,-57,-59,-61,-78,-77,]),'VEZES':([43,44,45,46,47,48,49,50,51,52,53,54,55,56,86,87,98,115,116,117,119,130,],[84,-60,-62,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-63,-64,-76,84,-59,-61,-78,-77,]),'DIVISAO':([44,45,46,47,48,49,50,51,52,53,54,55,56,86,87,98,116,117,119,130,],[85,-62,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-63,-64,-76,85,-61,-78,-77,]),'INCREMENTO':([45,46,47,48,49,50,51,52,53,54,55,56,86,87,98,117,119,130,],[86,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-63,-64,-76,86,-78,-77,]),'DECREMENTO':([45,46,47,48,49,50,51,52,53,54,55,56,86,87,98,117,119,130,],[87,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-63,-64,-76,87,-78,-77,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,2,3,],[1,16,17,]),'funcdecl':([0,2,3,],[2,2,2,]),'variable':([0,2,3,19,26,],[3,3,3,32,32,]),'signature':([0,2,3,],[4,4,4,]),'type':([0,2,3,6,19,26,],[5,5,5,23,5,5,]),'modifier':([0,2,3,],[6,6,6,]),'body':([4,127,128,143,149,],[18,136,137,146,150,]),'assign':([5,],[20,]),'stms':([19,26,],[24,63,]),'stm':([19,26,],[26,26,]),'exp1':([19,26,29,30,58,59,66,69,70,88,129,131,132,133,144,145,],[27,27,67,68,89,90,97,100,102,120,102,120,140,120,102,148,]),'exp2':([19,26,29,30,58,59,65,66,69,70,88,129,131,132,133,144,145,],[34,34,34,34,34,34,96,34,34,34,34,34,34,34,34,34,34,]),'exp3':([19,26,29,30,58,59,65,66,69,70,71,88,129,131,132,133,144,145,],[35,35,35,35,35,35,35,35,35,35,103,35,35,35,35,35,35,35,]),'exp4':([19,26,29,30,58,59,65,66,69,70,71,72,88,129,131,132,133,144,145,],[36,36,36,36,36,36,36,36,36,36,36,104,36,36,36,36,36,36,36,]),'exp5':([19,26,29,30,58,59,65,66,69,70,71,72,73,88,129,131,132,133,144,145,],[37,37,37,37,37,37,37,37,37,37,37,37,105,37,37,37,37,37,37,37,]),'exp6':([19,26,29,30,58,59,65,66,69,70,71,72,73,74,88,129,131,132,133,144,145,],[38,38,38,38,38,38,38,38,38,38,38,38,38,106,38,38,38,38,38,38,38,]),'exp7':([19,26,29,30,58,59,65,66,69,70,71,72,73,74,75,88,129,131,132,133,144,145,],[39,39,39,39,39,39,39,39,39,39,39,39,39,39,107,39,39,39,39,39,39,39,]),'exp8':([19,26,29,30,58,59,65,66,69,70,71,72,73,74,75,76,77,88,129,131,132,133,144,145,],[40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,108,109,40,40,40,40,40,40,40,]),'exp9':([19,26,29,30,58,59,65,66,69,70,71,72,73,74,75,76,77,78,79,80,81,88,129,131,132,133,144,145,],[41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,110,111,112,113,41,41,41,41,41,41,41,]),'exp10':([19,26,29,30,58,59,65,66,69,70,71,72,73,74,75,76,77,78,79,80,81,82,88,129,131,132,133,144,145,],[42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,114,42,42,42,42,42,42,42,]),'exp12':([19,26,29,30,58,59,65,66,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,88,129,131,132,133,144,145,],[43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,115,43,43,43,43,43,43,43,]),'exp13':([19,26,29,30,58,59,65,66,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,88,129,131,132,133,144,145,],[44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,116,44,44,44,44,44,44,44,]),'exp14':([19,26,29,30,58,59,65,66,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,88,129,131,132,133,144,145,],[45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,117,45,45,45,45,45,45,45,]),'exp15':([19,26,29,30,58,59,65,66,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,88,129,131,132,133,144,145,],[46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,]),'call':([19,26,29,30,58,59,65,66,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,88,129,131,132,133,144,145,],[51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,]),'sigparams':([60,95,134,],[93,125,142,]),'optexp':([70,129,144,],[101,138,147,]),'params':([88,131,133,],[118,139,141,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> funcdecl','program',1,'p_program','ExpressionLanguageParser.py',7),
  ('program -> funcdecl program','program',2,'p_program','ExpressionLanguageParser.py',8),
  ('program -> variable program','program',2,'p_program','ExpressionLanguageParser.py',9),
  ('program -> variable','program',1,'p_program','ExpressionLanguageParser.py',10),
  ('funcdecl -> signature body','funcdecl',2,'p_funcdecl','ExpressionLanguageParser.py',18),
  ('modifier -> PUBLIC','modifier',1,'p_modifier_public','ExpressionLanguageParser.py',23),
  ('modifier -> STATIC','modifier',1,'p_modifier_static','ExpressionLanguageParser.py',28),
  ('signature -> modifier ID LPAREN sigparams RPAREN','signature',5,'p_signature_id','ExpressionLanguageParser.py',33),
  ('signature -> modifier ID LPAREN RPAREN','signature',4,'p_signature_id_noparam','ExpressionLanguageParser.py',38),
  ('signature -> modifier type ID LPAREN sigparams RPAREN','signature',6,'p_signature_modifier_type','ExpressionLanguageParser.py',43),
  ('signature -> modifier type ID LPAREN RPAREN','signature',5,'p_signature_modifier_type_noparam','ExpressionLanguageParser.py',48),
  ('sigparams -> ID ID','sigparams',2,'p_sigparams','ExpressionLanguageParser.py',53),
  ('sigparams -> ID ID COMMA sigparams','sigparams',4,'p_sigparams','ExpressionLanguageParser.py',54),
  ('body -> LCHAV stms RCHAV','body',3,'p_body','ExpressionLanguageParser.py',62),
  ('body -> LCHAV RCHAV','body',2,'p_body','ExpressionLanguageParser.py',63),
  ('stms -> stm','stms',1,'p_stms','ExpressionLanguageParser.py',71),
  ('stms -> stm stms','stms',2,'p_stms','ExpressionLanguageParser.py',72),
  ('stm -> exp1 PV','stm',2,'p_stm','ExpressionLanguageParser.py',80),
  ('stm -> WHILE LPAREN exp1 RPAREN body','stm',5,'p_stm_while','ExpressionLanguageParser.py',85),
  ('stm -> RETURN exp1 PV','stm',3,'p_stm_return','ExpressionLanguageParser.py',90),
  ('stm -> IF LPAREN exp1 RPAREN body ELSE body','stm',7,'p_stm_ifelse','ExpressionLanguageParser.py',95),
  ('stm -> IF LPAREN exp1 RPAREN body','stm',5,'p_stm_if','ExpressionLanguageParser.py',100),
  ('stm -> variable','stm',1,'p_stm_variable','ExpressionLanguageParser.py',105),
  ('optexp -> exp1','optexp',1,'p_optexp','ExpressionLanguageParser.py',110),
  ('optexp -> <empty>','optexp',0,'p_optexp_none','ExpressionLanguageParser.py',114),
  ('stm -> FOR LPAREN optexp PV optexp PV optexp RPAREN body','stm',9,'p_stm_for','ExpressionLanguageParser.py',118),
  ('variable -> type assign PV','variable',3,'p_variable','ExpressionLanguageParser.py',123),
  ('type -> INT','type',1,'p_type','ExpressionLanguageParser.py',128),
  ('type -> STRING','type',1,'p_type_string','ExpressionLanguageParser.py',133),
  ('type -> BOOL','type',1,'p_type_bool','ExpressionLanguageParser.py',138),
  ('type -> FLOAT','type',1,'p_type_float','ExpressionLanguageParser.py',143),
  ('type -> DECIMAL','type',1,'p_type_float_decimal','ExpressionLanguageParser.py',148),
  ('type -> DOUBLE','type',1,'p_type_float_double','ExpressionLanguageParser.py',153),
  ('type -> VOID','type',1,'p_type_void','ExpressionLanguageParser.py',158),
  ('exp1 -> exp1 ATRIBUICAO exp2','exp1',3,'p_exp1_atribuicao1','ExpressionLanguageParser.py',163),
  ('exp1 -> exp2','exp1',1,'p_exp1_atribuicao2','ExpressionLanguageParser.py',168),
  ('exp2 -> exp2 LCOR exp3','exp2',3,'p_exp2_lcor1','ExpressionLanguageParser.py',173),
  ('exp2 -> exp3','exp2',1,'p_exp2_lcor2','ExpressionLanguageParser.py',178),
  ('exp3 -> exp3 LCAND exp4','exp3',3,'p_exp3_lcand1','ExpressionLanguageParser.py',183),
  ('exp3 -> exp4','exp3',1,'p_exp3_lcand2','ExpressionLanguageParser.py',188),
  ('exp4 -> exp4 OR exp5','exp4',3,'p_exp4_or1','ExpressionLanguageParser.py',193),
  ('exp4 -> exp5','exp4',1,'p_exp4_or2','ExpressionLanguageParser.py',198),
  ('exp5 -> exp5 EXOR exp6','exp5',3,'p_exp5_exor1','ExpressionLanguageParser.py',203),
  ('exp5 -> exp6','exp5',1,'p_exp4_exor2','ExpressionLanguageParser.py',208),
  ('exp6 -> exp6 LAND exp7','exp6',3,'p_exp6_land1','ExpressionLanguageParser.py',213),
  ('exp6 -> exp7','exp6',1,'p_exp6_land2','ExpressionLanguageParser.py',218),
  ('exp7 -> exp7 IGUAL exp8','exp7',3,'p_exp7_igual','ExpressionLanguageParser.py',223),
  ('exp7 -> exp7 DIFERENTE exp8','exp7',3,'p_exp7_diferente','ExpressionLanguageParser.py',228),
  ('exp7 -> exp8','exp7',1,'p_exp7','ExpressionLanguageParser.py',233),
  ('exp8 -> exp8 MENOR exp9','exp8',3,'p_exp8_menor','ExpressionLanguageParser.py',238),
  ('exp8 -> exp8 MENOR_IGUAL exp9','exp8',3,'p_exp8_menorigual','ExpressionLanguageParser.py',243),
  ('exp8 -> exp8 MAIOR exp9','exp8',3,'p_exp8_maior','ExpressionLanguageParser.py',248),
  ('exp8 -> exp8 MAIOR_IGUAL exp9','exp8',3,'p_exp8_maiorigual','ExpressionLanguageParser.py',253),
  ('exp8 -> exp9','exp8',1,'p_exp8','ExpressionLanguageParser.py',258),
  ('exp9 -> exp9 SOMA exp10','exp9',3,'p_exp9_soma1','ExpressionLanguageParser.py',263),
  ('exp9 -> exp10','exp9',1,'p_exp9_soma2','ExpressionLanguageParser.py',268),
  ('exp10 -> exp10 SUBTRACAO exp12','exp10',3,'p_exp10_subtracao1','ExpressionLanguageParser.py',273),
  ('exp10 -> exp12','exp10',1,'p_exp10_subtracao2','ExpressionLanguageParser.py',278),
  ('exp12 -> exp12 VEZES exp13','exp12',3,'p_exp12_vezes1','ExpressionLanguageParser.py',283),
  ('exp12 -> exp13','exp12',1,'p_exp12_vezes2','ExpressionLanguageParser.py',288),
  ('exp13 -> exp13 DIVISAO exp14','exp13',3,'p_exp13_divisao1','ExpressionLanguageParser.py',293),
  ('exp13 -> exp14','exp13',1,'p_exp13_divisao2','ExpressionLanguageParser.py',298),
  ('exp14 -> exp14 INCREMENTO','exp14',2,'p_exp14_incremento','ExpressionLanguageParser.py',303),
  ('exp14 -> exp14 DECREMENTO','exp14',2,'p_exp14_decremento','ExpressionLanguageParser.py',308),
  ('exp14 -> exp15','exp14',1,'p_exp14','ExpressionLanguageParser.py',313),
  ('exp15 -> TRUE','exp15',1,'p_exp15_bool','ExpressionLanguageParser.py',318),
  ('exp15 -> FALSE','exp15',1,'p_exp15_bool','ExpressionLanguageParser.py',319),
  ('exp15 -> LITERALSTRING','exp15',1,'p_exp15_literalstring','ExpressionLanguageParser.py',325),
  ('exp15 -> ID','exp15',1,'p_exp15_id','ExpressionLanguageParser.py',330),
  ('exp15 -> call','exp15',1,'p_exp15_call','ExpressionLanguageParser.py',335),
  ('exp15 -> NUMBERINT','exp15',1,'p_exp15_numberint','ExpressionLanguageParser.py',340),
  ('exp15 -> NUMBERFLOATALL','exp15',1,'p_exp15_numberfloatall','ExpressionLanguageParser.py',345),
  ('exp15 -> NUMBERFLOAT','exp15',1,'p_exp15_numberfloat','ExpressionLanguageParser.py',350),
  ('exp15 -> NUMBERDECIMAL','exp15',1,'p_exp15_numberdecimal','ExpressionLanguageParser.py',355),
  ('exp15 -> NUMBERDOUBLE','exp15',1,'p_exp15_numberdouble','ExpressionLanguageParser.py',360),
  ('exp15 -> LPAREN exp1 RPAREN','exp15',3,'p_exp15_par','ExpressionLanguageParser.py',365),
  ('call -> ID LPAREN params RPAREN','call',4,'p_call','ExpressionLanguageParser.py',370),
  ('call -> ID LPAREN RPAREN','call',3,'p_call_noparams','ExpressionLanguageParser.py',375),
  ('params -> exp1 COMMA params','params',3,'p_params','ExpressionLanguageParser.py',380),
  ('params -> exp1','params',1,'p_params_exp','ExpressionLanguageParser.py',385),
  ('assign -> ID IGUAL exp1','assign',3,'p_assign','ExpressionLanguageParser.py',390),
  ('assign -> ID LCOL exp1 RCOL IGUAL exp1','assign',6,'p_assign_array_exp','ExpressionLanguageParser.py',395),
  ('assign -> ID LCOL RCOL IGUAL LCHAV params RCHAV exp1','assign',8,'p_assign_array','ExpressionLanguageParser.py',400),
  ('assign -> ID','assign',1,'p_assign_id','ExpressionLanguageParser.py',405),
]
