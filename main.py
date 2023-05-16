import ply.yacc as yacc
from ExpressionLanguageLex import *
from ExpressionLanguageParser import *
import Visitor as Vis

lexer = lex.lex()



data1 = '''
public void main(){
  int a = 1;
  float b = 1.4;
}

public main(){
  int a = 1;
  float b = 1.4;
}

static float num(){
 float a = 2.23;
 return a;
}

'''


data2 = '''
string teste = "teste1";
int a = 12;
float b = 1.2f;
double c = 1.2d;
decimal d = 1.4m;
float e = 1.5;
int x = 2;

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

static float num(){
 float a = 2.23;
 return a;
}

static void test(){
  for(j=0; j<10; j++){
    return j;
  }
  
  for(; k<10; k++){
    return k;
  }
}


'''

lexer.input(data2)
parser = yacc.yacc()
result = parser.parse(debug=True)