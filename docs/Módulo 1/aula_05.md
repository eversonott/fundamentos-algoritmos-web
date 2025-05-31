# Aula 05 -  Introdução à funções

{% set aula = "05" %}
{% set link = "6qb3ZnMwcSA" %}
{% set objetivos = 
[
  "Compreender o conceito de função como sequência nomeada de instruções",
  "Utilizar funções integradas do Python e interpretar argumentos e retornos",
  "Importar e usar funções do módulo math com notação de ponto",
  "Definir funções próprias com parâmetros e aplicar o conceito de escopo",
  "Compor e encadear funções para resolver problemas matemáticos e lógicos"
]
%}
{% include "templates/cabecalho.md" %}

## Funções

Função é uma sequência nomeada de instruções.

Ou seja, ao definir uma função, você específica o nome e a sequência de instruções.

Depois de declarada, podemos "chamar" a função pelo nome.


### Chamada de função

Já vimos algumas "funções".

```python
>>> type(42)
<class 'int'>
>>> type('Oi')
<class 'str'>
>>> type(4.6)
<class 'float'>
```

```python
>>> print("Essa é uma mensagem.")
Essa é uma mensagem.
>>> mensagem = 'Olá'
>>> print(mensagem)
Olá
```

Já vimos que os parêntese das funções sempre precisam estar em dupla.

Em uma função a expressão entre os parênteses é chamada de **argumento**.

No caso da função de nome `type`.

```python
>>> type(42)
<class 'int'>
```

O argumento é o número `42`.

O **resultado da função** é `<class 'int'>`. Que nesse caso é o tipo do argumento.

É comum dizer que uma função **"recebe"** um argumento e **"retorna"** um resultado. Por isso, as vezes, chamamos o resultado de retorno.


### Funções que convertem valores

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



`int` pode converter valores de ponto flutuante em números inteiros, mas não realiza arredondamentos, apenas ignora a parte decimal.

```python
>>> int(3.9999)
3
```


Portanto também temos a função `float`, que converte números inteiros e strings em números de ponto flutuante:

```python
>>> float(23)
23.0
```

```python
>>> float('3.14')
3.14
```

Logo, também teremos a `str` que converte o argumento em uma string.

```python
>>> str(32)
'32'
```

```python
>>> str(3.14)
'3.14'
```



### Funções matemáticas

O Python possui um módulo matemático que oferece a maioria das funções matemáticas comuns.

> Um **módulo** é um arquivo que contém uma coleção de funções relacionadas.

Para usar funções em um módulo, precisamos importá-lo com um **instrução de importação**.

Veremos posteriormente sobre importação de módulos.

Por exemplo:

```python
>>> import math
```

Essa instrução cria um objeto de módulo chamado **math** (matemática).


O objeto de módulo contém as funções e variáveis definidas no módulo.

Para acessar uma das funções, é preciso especificar o nome do módulo e o nome da função, separador por um ponto. Esse formato é chamado de **notação de ponto**.

```python
>>> import math
>>> relacao_sinal_ruido = potencia_sinal / potencia_ruido
>>> decibeis = 10 * math.log10(relacao_sinal_ruido)
```

O exemplo acima, usa `math.log10` para calcular a proporção de sinal e de ruído em decibéis (assumindo que *potencia_sinal* e *potencia_ruido* tenham sido declarados).

O módulo matemático também oferece as funções `log`, `log2` que calcula logaritmos de base **e** (logaritmo natural) e logaritmos com base **2**.



#### Algumas funções trigonométricas

```python
>>> import math
>>> graus_radianos = 0.7
>>> altura = math.sin(radians)
```

Nesse exemplo encontramos o seno de *graus_radianos*. 

O nome da variável indica que funções trigonométricas aceitam seu parâmetro, apenas em radianos.


Para converter graus em radianos, divida por 180 e multiplique por π.

```python
>>> import math
>>> angulo_em_graus = 45
>>> angulo_em_radianos = angulo_em_graus / 180.0 * math.pi
>>> math.sin(angulo_em_radianos)
0.7071067811865475
```

A expressão `math.pi` recebe a variável pi do módulo matemático, seu valor é uma aproximação de ponto flutuante de π, com precisão aproximada de 15 dígitos.

#### Todas as funções de math


<table>
    <tr>
        <td colspan="2"><center><strong>Funções teóricas dos números</strong><center></td>
    </tr>
    <tr>
        <td>comb(n,k)</td>
        <td>Número de maneiras de escolher k itens de n itens sem repetição e sem ordem </td>
    </tr>
    <tr>
        <td>factorial(n)</td>
        <td>n fatorial </td>
    </tr>
    <tr>
        <td>gcd(*integers)</td>
        <td>Maior divisor comum dos argumentos inteiros </td>
    </tr>
    <tr>
        <td>isqrt(n)</td>
        <td>Raiz quadrada inteira de um inteiro não negativo n </td>
    </tr>
    <tr>
        <td>lcm(*integers)</td>
        <td>Mínimo múltiplo comum dos argumentos inteiros </td>
    </tr>
    <tr>
        <td>perm(n,k)</td>
        <td>Número de maneiras de escolher k itens de n itens sem repetição e com ordem </td>
    </tr>
    <tr>
        <td colspan="2"><center><strong>Aritmética de ponto flutuante </strong><center></td>
    </tr>
    <tr>
        <td>ceil(x)</td>
        <td>Teto de x , o menor número inteiro maior ou igual a x </td>
    </tr>
    <tr>
        <td>fabs(x)</td>
        <td>Valor absoluto de x </td>
    </tr>
    <tr>
        <td>floor(x)</td>
        <td>Piso de x , o maior número inteiro menor ou igual a x </td>
    </tr>
    <tr>
        <td>fma(x,y,z)</td>
        <td>Operação de adição múltipla fundida: (x * y) + z</td>
    </tr>
    <tr>
        <td>fmod(x,y)</td>
        <td>Restante da divisão x / y</td>
    </tr>
    <tr>
        <td>modf(x)</td>
        <td>Partes fracionárias e inteiras de x </td>
    </tr>
    <tr>
        <td>remainder(x,y)</td>
        <td>Resto de x em relação a y </td>
    </tr>
    <tr>
        <td>trunc(x)</td>
        <td>Parte inteira de x </td>
    </tr>
    <tr>
        <td colspan="2"><center><strong>Funções de manipulação de ponto flutuante </strong><center></td>
    </tr>
    <tr>
        <td>copysign(x,y)</td>
        <td>Magnitude (valor absoluto) de x com o sinal de y </td>
    </tr>
    <tr>
        <td>frexp(x)</td>
        <td>Mantissa e expoente de x </td>
    </tr>
    <tr>
        <td>isclose(a,b,rel_tol,abs_tol)</td>
        <td>Verifique se os valores aeb estão próximos um outro do </td>
    </tr>
    <tr>
        <td>isfinite(x)</td>
        <td>Verifique se x não é infinito nem NaN </td>
    </tr>
    <tr>
        <td>isinf(x)</td>
        <td>Verifique se x é um infinito positivo ou negativo </td>
    </tr>
    <tr>
        <td>isnan(x)</td>
        <td>Verifique se x é um NaN (não um número) </td>
    </tr>
    <tr>
        <td>ldexp(x,i)</td>
        <td>x * (2**i), inverso da função frexp()</td>
    </tr>
    <tr>
        <td>nextafter(x,y,steps)</td>
        <td>O valor de ponto flutuante avança após x em direção a y </td>
    </tr>
    <tr>
        <td>ulp(x)</td>
        <td>Valor do bit menos significativo de x </td>
    </tr>
    <tr>
        <td colspan="2"><center><strong>Funções de potência, exponenciais e logarítmicas </strong><center></td>
    </tr>
    <tr>
        <td>cbrt(x)</td>
        <td>Raiz cúbica de x </td>
    </tr>
    <tr>
        <td>exp(x)</td>
        <td>e elevado à potência x </td>
    </tr>
    <tr>
        <td>exp2(x)</td>
        <td>2 elevado à potência x </td>
    </tr>
    <tr>
        <td>expm1(x)</td>
        <td>e elevado à potência x , menos 1 </td>
    </tr>
    <tr>
        <td>log(x,base)</td>
        <td>Logaritmo de x para a base fornecida ( e por padrão) </td>
    </tr>
    <tr>
        <td>log1p(x)</td>
        <td>Logaritmo natural de 1+x (base e ) </td>
    </tr>
    <tr>
        <td>log2(x)</td>
        <td>Logaritmo de base 2 de x </td>
    </tr>
    <tr>
        <td>log10(x)</td>
        <td>Logaritmo de base 10 de x </td>
    </tr>
    <tr>
        <td>pow(x,y)</td>
        <td>x elevado à potência y </td>
    </tr>
    <tr>
        <td>sqrt(x)</td>
        <td>Raiz quadrada de x </td>
    </tr>
    <tr>
        <td colspan="2"><center><strong>Funções de soma e produto </strong><center></td>
    </tr>
    <tr>
        <td>dist(p,q)</td>
        <td>Distância euclidiana entre dois pontos p e q dada como um iterável de coordenadas </td>
    </tr>
    <tr>
        <td>fsum(iterable)</td>
        <td>Soma dos valores no iterável de entrada </td>
    </tr>
    <tr>
        <td>hypot(*coordinates)</td>
        <td>Norma euclidiana de um iterável de coordenadas </td>
    </tr>
    <tr>
        <td>prod(iterable,start)</td>
        <td>Produto de elementos na entrada iterável com um inicial valor </td>
    </tr>
    <tr>
        <td>sumprod(p,q)</td>
        <td>Soma dos produtos de dois iteráveis ​​p e q </td>
    </tr>
    <tr>
        <td colspan="2"><center><strong>Conversão angular </strong></center></td>
    </tr>
    <tr>
        <td>degrees(x)</td>
        <td>Converta o ângulo x de radianos para graus </td>
    </tr>
    <tr>
        <td>radians(x)</td>
        <td>Converta o ângulo x de graus para radianos </td>
    </tr>
    <tr>
        <td colspan="2"><center><strong>Funções trigonométricas <strong><center></td>
    </tr>
    <tr>
        <td>acos(x)</td>
        <td>Arco cosseno de x </td>
    </tr>
    <tr>
        <td>asin(x)</td>
        <td>Arco seno de x </td>
    </tr>
    <tr>
        <td>atan(x)</td>
        <td>Arco tangente de x </td>
    </tr>
    <tr>
        <td>atan2(y,x)</td>
        <td>atan(y / x)</td>
    </tr>
    <tr>
        <td>cos(x)</td>
        <td>Cosseno de x </td>
    </tr>
    <tr>
        <td>sin(x)</td>
        <td>Seno de x </td>
    </tr>
    <tr>
        <td>tan(x)</td>
        <td>Tangente de x </td>
    </tr>
    <tr>
        <td colspan="2"><center><strong>Funções hiperbólicas </strong></center></td>
    </tr>
    <tr>
        <td>acosh(x)</td>
        <td>Cosseno hiperbólico inverso de x </td>
    </tr>
    <tr>
        <td>asinh(x)</td>
        <td>Seno hiperbólico inverso de x </td>
    </tr>
    <tr>
        <td>atanh(x)</td>
        <td>Tangente hiperbólica inversa de x </td>
    </tr>
    <tr>
        <td>cosh(x)</td>
        <td>Cosseno hiperbólico de x </td>
    </tr>
    <tr>
        <td>sinh(x)</td>
        <td>Seno hiperbólico de x </td>
    </tr>
    <tr>
        <td>tanh(x)</td>
        <td>Tangente hiperbólica de x </td>
    </tr>
    <tr>
        <td colspan="2"><center><strong>Funções especiais </strong><center></td>
    </tr>
    <tr>
        <td>erf(x)</td>
        <td>Função de erro  em x </td>
    </tr>
    <tr>
        <td>erfc(x)</td>
        <td>Função de erro complementar  em x </td>
    </tr>
    <tr>
        <td>gamma(x)</td>
        <td>Função gama  em x </td>
    </tr>
    <tr>
        <td>lgamma(x)</td>
        <td>Logaritmo natural do valor absoluto da função Gamma  em x </td>
    </tr>
    <tr>
        <td colspan="2"><center><strong>Constantes </strong></center></td>
    </tr>
    <tr>
        <td>pi</td>
        <td>π = 3,141592… </td>
    </tr>
    <tr>
        <td>e</td>
        <td>e = 2.718281… </td>
    </tr>
    <tr>
        <td>tau</td>
        <td>τ = 2 π = 6,283185… </td>
    </tr>
    <tr>
        <td>inf</td>
        <td>Infinito positivo </td>
    </tr>
    <tr>
        <td>nan</td>
        <td>“Não é um número” (NaN) </td>
    </tr>
</table>

	


### A composição das funções

Já falamos sobre variáveis, expressões e instruções, agora vamos começar a combinar esses elementos.

O argumento de uma função pode ser qualquer tipo de expressão, inclusive expressões com operadores aritméticos.

```python
>>> import math
>>>  x = math.sin(angulo_em_graus / 360.0 * 2 * math.pi)
```



Também é possível passar como argumento chamadas de outras funções:

```python
>>> import math
>>>  x = math.exp(math.log(x + 1))
```

`math.exp(x)` retorna *e* elevado à potência *x*.



### Novas funções

Por enquanto só utilizamos funções que vêm com o Python.

#### Mas como criar novas funções?

Uma definição de função especifica o nome de uma nova função e a sequência de instruções que serão executadas quando ela for **chamada**




```python
>>> def imprime_letra_musica():
...     print('Todos os dias quando acordo')
...     print('Não tenho mais o tempo que passou')
...
```

- **def** é uma palavra-chave que indica uma definição de função.

- O nome da função é *imprime_letra_musica*.

- Os parênteses vazios depois do nome indicam que esta função não usa argumentos.

- Os ":" indicam o inicio do escopo da função e a tabulação indica esse próprio escopo.



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

Ou seja, o nome da função e seus argumentos ou não dentro de parenteses.

```python
>>> imprime_letra_musica()
Todos os dias quando acordo
Não tenho mais o tempo que passou
```

Uma vez que a função tenha sido definida, é possível usá-la dentro de outra função.


A definição de funções tem que ser executada antes que a função seja chamada. Ou seja, não faz sentido chamar uma função que ainda não foi criada.

```python
>>> imprime_letra_musica()
NameError: name 'imprime_letra_musica' is not defined
```


A grosso modo, as instruções de um programa são sempre executadas uma após a outra, de cima para baixo. Isso é chamado de **fluxo de execução**.

As definições de função não alteram o fluxo da execução do programa, mas é necessário lembrar que as instruções dentro da função não são executadas até a função ser chamada.

Uma chamada de função é como um desvio no fluxo de execução. 

O fluxo salta para o corpo da função, executa as instruções lá, e então volta para continuar de onde parou.



#### Parâmetros e argumentos

Algumas funções exigem argumentos.

Por exemplo, `math.pow` exige dois argumentos, a base e o expoente.


```python title='Documentação do math.pow'
math.pow(x, y, /)
    Retorna x**y (x elavado à potência de y).
```

```python
>>> import math
>>> math.pow(2,3)
8.0
```

Se chamarmos `pow` sem passar os argumentos:

```python
    math.pow()
    ~~~~~~~~^^
TypeError: pow expected 2 arguments, got 0
# Erro de tipo: pow esperava 2 argumentos, obteve 0
```

Mas, dentro da função os argumentos são atribuídos a variáveis chamadas **parâmetros**.

Os parâmetros só existem dentro do escopo da função, por isso podemos atribuir o valor passado por argumento a outro nome.

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

Perceba que a nossa função atribui o valor do argumento a um parâmetro chamado **nome**.

Mas perceba que essa função funciona com qualquer valor que possa ser exibido, desde que seja passado por argumento. Até mesmo com expressões podem ser passadas.

```python
>>> imprime_nome('João')
João
```
```python
>>> imprime_nome('José' * 4)
JoséJoséJoséJosé
```
Não importa o argumento, dentro da função `imprime_nome` qualquer argumento corresponde ao parâmetro `nome`.



## Prática!



