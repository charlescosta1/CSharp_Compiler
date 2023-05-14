# GLC da Linguagem de Programação C# 
Terminais são representados pelos elementos cuja grafia está em maiúsculo, bem como pelos símbolos que estão entre aspas duplas (")
```
program → funcdecl | 
          funcdecl program |
          variable program |
          variable

funcdecl → signature body

signature → ID ID "(" sigparams ")"

sigparams → ID ID | 
            ID ID "," sigparams

body → "{" stms "}"

stms → stm  | 
       stm  stms

stm → exp ";"  | 
      WHILE "(" exp ")" body | return exp ";" |
      FOR "(" exp ";" exp ";" exp ")" body |  
      IF "(" exp ")" body ELSE body | 
      IF "(" exp ")" body
      
call → ID "(" params ")"

variable → type assign ";" 
           
type → INT |
       String |
       float |
       boolean
       
exp → exp "+" exp | 
      exp "-" exp | 
      exp "*" exp | 
      exp "/" exp | 
      exp "%" exp |
      exp "^" exp |
      exp "<" exp |
      exp ">" exp |
      exp "<=" exp |
      exp ">=" exp |
      exp "==" exp |
      exp "!=" exp |
      exp "&&" exp |
      exp "||" exp |
      exp "&" exp |
      exp "|" exp |
      exp "~" exp |
      exp "-=" exp |
      exp "+=" exp |
      exp "*=" exp |
      exp "/=" exp |
      exp "%=" exp |
      exp "&=" exp |
      exp "^=" exp |
      exp "|=" exp |
      exp "<<=" exp |
      exp ">>=" exp |
      exp ">>>=" exp | 
      exp "?" exp ":" exp |
      "!" exp |
      exp "++" |
      exp "--" |
      "++" exp |
      "--" exp |
      exp "<<" exp |
      exp ">>" exp |
      exp ">>>" exp |
      call |
      assign | 
      NUM | 
      ID

call → ID "("params")" | 
       ID "(" ")"

params → exp"," params | 
         exp



assign → ID "=" exp |
         ID "[" exp "]" "=" exp  |
         ID "[" "]" "=" "{" params "}"  exp  

```