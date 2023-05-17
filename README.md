# Linguagem C#

Este projeto consiste no desenvolvimento de um compilador para a linguagem C#. O compilador é responsável por traduzir o código-fonte escrito em C# em um formato que a máquina possa entender e executar.

# Funcionalidades
- Análise léxica: O compilador realiza a análise léxica, também conhecida como tokenização, onde o código-fonte é dividido em tokens como palavras-chave, identificadores, literais, operadores e pontuação.

- Análise sintática: Após a análise léxica, o compilador passa pela análise sintática, verificando se a sequência de tokens segue a gramática definida pela linguagem C#. Nesta etapa, é criada uma árvore de análise sintática (AST) que representa a estrutura hierárquica do código-fonte.

- Análise semântica: A análise semântica ocorre após a análise sintática e verifica se as regras semânticas da linguagem estão sendo seguidas corretamente. Isso inclui verificar a validade dos tipos, a existência de variáveis e funções, a coerência das expressões, entre outros aspectos.

- Geração de código: Após a análise semântica, o compilador realiza a geração de código, traduzindo a AST em código de máquina ou em um código intermediário como o CIL (Common Intermediate Language).

# Contribuição
- Carlos Henrique (github: @carloshldj)
- Charles Dayan (github: @charlescosta1)
- Jorge Matheus (github: @JorgeMatheuss)
