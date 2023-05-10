import ply.yacc as yacc
from ExpressionLanguageLex import *
from ExpressionLanguageParser import *

lexer = lex.lex()

data = '''
string teste = "teste1";
float x = 1.2;

public void Main()
{
bool test = true;
int i = 1;
  
while (i > 5){
  if (x > 0){
    return x;
  }
  else{
    return test;
  }
    return i;
  }
  ReadKey();
}
'''

lexer.input(data)
parser = yacc.yacc()
result = parser.parse(debug=True)