---
marp: true
theme: rose-pine
style: |
  .columns {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1rem;
  }
---

# Aula 03 - Funções
## Fundamentos de algoritmos e introdução à programação em Python

Prof. Everson Otoni


---

## Funções

Função é uma sequência nomeada de instruções.

Ou seja, ao definir uma função, você específica o nome e a sequência de instruções.

Depois de declarada, podemos "chamar" a função pelo nome.

---

## Chamada de função

Já vimos algumas funções até agora.

```python
>>> type(42)
<class 'int'>
```

```python
>>> print("Essa é uma mensagem.")
Essa é uma mensagem.
```

---


Já vimos que os parênteses das funções sempre precisam estar em dupla.

Em uma função a expressão entre os parênteses é chamada de **argumento**.

No caso da função de nome `type`.

```python
>>> type(42)
<class 'int'>
```

O argumento é o número `42`.

O **resultado da função** é `<class 'int'>`. Que nesse caso é o tipo do argumento.


É comum dizer que uma função **"recebe"** um argumento e **"retorna"** um resultado.

---

## Funções que convertem valores

O Python oferece funções que convertem valores de um tipo em outro.

A função `int` recebe qualquer valor e o converte em um número inteiro, se for possível, ou declara que há um erro.

```python
>>> int('32')
32
```

```python
>>> int('Olá')
ValueError: invalid literal for int() with base 10: 'Olá'
```

---

`int` pode converter valores de ponto flutuante em números inteiros, mas não realiza arredondamentos, apenas ignora a parte decimal.

```python
>>> int(3.9999)
3
```

---


`float` converte números inteiros e strings em números de ponto flutuante:

```python
>>> float(23)
23.0
```

```python
>>> float('3.14')
3.14
```

---


`str` converte o argumento em uma string.

```python
>>> str(32)
'32'
```

```python
>>> str(3.14)
'3.14'
```

---

## Algumas funções matemáticas

O Python possui um módulo matemático que oferece a maioria das funções matemáticas comuns.

> Um **módulo** é um arquivo que contém uma coleção de funções relacionadas.

Para usar funções em um módulo, precisamos importá-lo com um **instrução de importação**.

Por exemplo:

```python
>>> import math
```

Essa instrução cria um objeto de módulo chamado **math** (matemática).

---


O objeto de módulo contém as funções e variáveis definidas no módulo.

Para acessar uma das funções, é preciso especificar o nome do módulo e o nome da função, separador por um ponto. Esse formato é chamado de **notação de ponto**.

```python
>>> import math
>>> relacao_sinal_ruido = potencia_sinal / potencia_ruido
>>> decibeis = 10 * math.log10(relacao_sinal_ruido)
```

O exemplo acima, usa `math.log10` para calcular a proporção de sinal e de ruído em decibéis (assumindo que *potencia_sinal* e *potencia_ruido* tenham sido declarados).

O módulo matemático também oferece as funções `log`, `log2` que calcula logaritmos de base **e** (logaritmo natural) e logaritmos com base **2**.

---

## Algumas funções matemáticas - Funções trigonométricas

```python
>>> import math
>>> graus_radianos = 0.7
>>> altura = math.sin(radians)
```

Nesse exemplo encontramos o seno de *graus_radianos*. 

O nome da variável indica que funções trigonométricas aceitam seu parâmetro, apenas em radianos.

---



Para converter graus em radianos, divida por 180 e multiplique por π.

```python
>>> import math
>>> angulo_em_graus = 45
>>> angulo_em_radianos = angulo_em_graus / 180.0 * math.pi
>>> math.sin(angulo_em_radianos)
0.7071067811865475
```

A expressão `math.pi` recebe a variável pi do módulo matemático, seu valor é uma aproximação de ponto flutuante de π, com precisão aproximada de 15 dígitos.

---

## A composição das funções

Já falamos sobre variáveis, expressões e instruções, agora vamos começar a combinar esses elementos.

O argumento de uma função pode ser qualquer tipo de expressão, inclusive expressões com operadores aritméticos.

```python
>>> import math
>>>  x = math.sin(angulo_em_graus / 360.0 * 2 * math.pi)
```

---

Também é possível passar como argumento chamadas de outras funções:

```python
>>> import math
>>>  x = math.exp(math.log(x + 1))
```

`math.exp(x)` retorna *e* elevado à potência *x*.

---

## Novas funções

Por enquanto só utilizamos funções que vêm com o Python.

### Mas como criar novas funções?

Uma definição de função especifica o nome de uma nova função e a sequência de instruções que serão executadas quando ela for **chamada**

---


```python
>>> def imprime_letra_musica():
...     print('Todos os dias quando acordo')
...     print('Não tenho mais o tempo que passou')
...
```

**def** é uma palavra-chave que indica uma definição de função.

O nome da função é *imprime_letra_musica*.

Os parênteses vazios depois do nome indicam que esta função não usa argumentos.

---


```python
>>> def imprime_letra_musica():
```

A primeira linha da definição de função chama-se cabeçalho. E sempre termina em dois pontos.

```python
...     print('Todos os dias quando acordo')
...     print('Não tenho mais o tempo que passou')
...
```

O restante é o corpo da função e necessariamente precisa ser endentado. 

Por convenção, a endentação sempre é de quatro espaços.

No interpretador interativo que estamos usando é exibido `...` para mostrar que a definição não está completa. Para terminar a função, é preciso inserir uma linha vazia.

---


A definição de uma função cria um **objeto de função**, que tem como tipo *function*.

```python
>>> print(imprime_letra_musica)
<function imprime_letra_musica at 0x752887cbf7e0>
```

```python
>>> type(imprime_letra_musica)
<class 'function'>
```


A sintaxe para chamar a nova função é a mesma que a das funções integradas:

```python
>>> imprime_letra_musica()
Todos os dias quando acordo
Não tenho mais o tempo que passou
```

Uma vez que a função tenha sido definida, é possível usá-la dentro de outra função.

---


A definição de funções tem que ser executada antes que a função seja chamada.

```python
>>> imprime_letra_musica()
NameError: name 'imprime_letra_musica' is not defined
```


As instruções de um programa são sempre executadas uma após a outra, de cima para baixo. Isso é chamado de **fluxo de execução**.

As definições de função não alteram o fluxo da execução do programa, mas é necessário lembrar que as instruções dentro da função não são executadas até a função ser chamada.

Uma chamada de função é como um desvio no fluxo de execução. 

O fluxo salta para o corpo da função, executa as instruções lá, e então volta para continuar de onde parou.

---

### Parâmetros e argumentos

Algumas funções exigem argumentos.

Por exemplo, `math.pow` exige dois argumentos, a base e o expoente.

```python
>>> import math
>>> math.pow(2,3)
8.0
```

Mas, dentro da função os argumentos são atribuídos a variáveis chamadas **parâmetros**.

```python
>>> nome_aluno = 'Thais'
>>> def imprime_nome(nome):
...     print(nome)
...
```
```python
>>> imprime_nome(nome_aluno)
Thais
```

---


Perceba que a nossa função atribui o argumento a um parâmetro chamado **nome**.

Mas perceba que essa função funciona com qualquer valor que possa ser exibido. Até mesmo com expressões.

```python
>>> imprime_nome('João')
João
```
```python
>>> imprime_nome('José' * 4)
JoséJoséJoséJosé
```
Não importa o argumento, dentro da função `imprime_nome` qualquer argumento é chamado de `nome`.

---

## As variáveis e os parâmetros são locais

Quando uma variável é criada dentro de uma função seja ela parâmetro ou não, ela é local, ou seja, só existe dentro da função.

```python
>>> def imprime_concatenacao_duas_strings(parte_inicial, parte_final):
...     texto = parte_inicial + parte_final
...     imprime_nome(texto)
...
```

Essa função recebe dois argumentos, concatena-os e exibe o resultado utilizando a função `imprime_nome`.

---


```python
>>> terceiro_verso = 'Mas tenho muito tempo, '
>>> quarto_verso = 'temos todo tempo do mundo'
>>> imprime_concatenacao_duas_strings(terceiro_verso, quarto_verso)
Mas tenho muito tempo, temos todo tempo do mundo
```
Quando `imprime_concatenacao_duas_strings` é encerrada, a variável `texto` é destruída.

```python
>>> print(texto)
NameError: name 'texto' is not defined.
```

---

## Funções com resultado e funções sem resultados (métodos)

Até o momento criamos funções que apenas exibem algo na tela e não especificamente possuem um valor de retorno.

Vamos criar agora uma função que tenha como mesmo princípio que a função `math.pow`.

```python
>>> def calcula_potencia(base, expoente):
...     potencia = base ** expoente
...     return potencia
...
>>> print(calcula_potencia(2,3))
8
```

Com o uso do termo `return` nossa função gera um resultado ou nos devolve um objeto.


---

## Entrada de teclado

O Python fornece uma função integrada chamada `input` que interrompe o programa e espera que usuário digite algo.

Quando o usuário pressionar Enter, o programa volta a ser executado e input, que é uma função **retorna** o que o usuário digitou como uma string.

```python
>>> texto = input()
Teste de texto
>>> texto
'Teste de texto'
```
---


A função `input` tem como parâmetro uma string que é exibida ao usuário como orientação, a chamamos de argumento prompt.

```python
>>> nome = input('Insira seu nome: ')
Insira seu nome: Everson
>>> nome
'Everson'
```

---


Podemos passar por meio de uma variável o argumento prompt

```python
>>> mensagem_usuario_nome = 'Insira seu nome: '
>>> nome = input(mensagem_usuario_nome)
Insira seu nome: Everson
>>> nome
'Everson'
```
---


Se `input` retorna um valor do tipo string, como fazer entradas numéricas?

Basta usar as funções que convertem valores.

```python
>>> idade = int(input('Insira sua idade: '))
29
>>> idade
29
>>> type(idade)
<class 'int'>
>>> idade
29
```

---

## Ainda sobre funções embutidas

Existem duas funções fundamentais para qualquer objeto em python.

A função `dir(object)` sem argumentos devolve a lista de nomes no escopo local atual. 

Com um argumento, tentará devolver uma lista de atributos válidos para esse objeto.

O mecanismo padrão `dir()` se comporta de maneira diferente com diferentes tipos de objetos, pois tenta produzir as informações mais relevantes e não completas.

---


A função `help(request)`, se nenhum argumento é passado, o sistema interativo de ajuda inicia no interpretador do console.

Se o argumento é uma string, então a string é pesquisada como o nome de um módulo, função, classe, método, palavra-chave ou tópico de documentação, e a página de ajuda é exibida no console.

---


Temos uma variável do tipo **string**.

```python
>>> quarto_verso
'temos todo tempo do mundo'
```

```python
>>> dir(quarto_verso)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__',
'__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__',
'__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__',
'__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__',
'__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold',
'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index',
'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric',
'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans',
'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition',
'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate',
'upper', 'zfill']
```

---


```python
>>> help(quarto_verso.capitalize)
capitalize() method of builtins.str instance
    Return a capitalized version of the string.
    More specifically, make the first character have upper case and the rest lower
```

```python
>>> quarto_verso.capitalize()
'Temos todo tempo do mundo'
```

---


```python
>>> help(quarto_verso.isnumeric)
isnumeric() method of builtins.str instance
    Return True if the string is a numeric string, False otherwise.
    A string is numeric if all characters in the string are numeric and there is at 
    least one character in the string. 
```


Utilize as funções embutidas `dir(object)` e `help(request)` sempre que houver dúvidas ou quiser explorar mais o Python essas são funções que irão ajudar.
