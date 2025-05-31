
# Aula 07 - Execução Condicional

{% set aula = "07" %}
{% set link = "MTGywDavSrI" %}
{% set objetivos = 
[
  "Explorar atributos e métodos de objetos usando as funções dir() e help()",
  "Utilizar os operadores // e % para divisão inteira e resto de divisão",
  "Construir expressões booleanas com operadores relacionais e lógicos",
  "Aplicar estruturas condicionais com if, else, elif e aninhamentos",
  "Escrever programas que tomam decisões com base em múltiplas condições"
]

%}
{% include "templates/cabecalho.md" %}


## A função dir do Python!

Existem duas funções fundamentais para qualquer objeto em python.

A função `dir(object)` sem argumentos devolve a lista de nomes no escopo local atual. 

Com um argumento, tentará devolver uma lista de atributos válidos para esse objeto.

O mecanismo padrão `dir()` se comporta de maneira diferente com diferentes tipos de objetos, pois tenta produzir as informações mais relevantes e não completas.

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

Usamos a função `dir()` para descobrir o nome de um método das strings.
Podemos utilizar a função `help` para detalhamento desse método:

```python
>>> help(quarto_verso.capitalize)
capitalize() method of builtins.str instance
    Return a capitalized version of the string.
    More specifically, make the first character have upper case and the rest lower
```

De fato, o primeiro caractere se torna maiúsculo.

```python
>>> quarto_verso.capitalize()
'Temos todo tempo do mundo'
```

### Outro exemplo

```python
>>> help(quarto_verso.isnumeric)
isnumeric() method of builtins.str instance
    Return True if the string is a numeric string, False otherwise.
    A string is numeric if all characters in the string are numeric and there is at 
    least one character in the string. 
```


**Utilize as funções embutidas `dir(object)` e `help(request)` sempre que houver dúvidas ou quiser explorar mais o Python essas são funções que irão ajudar.**



## Novos operadores - Divisão por piso e módulo

O operador de **divisão pelo piso**, `//`, divide dois números e arredonda o resultado para um número inteiro para baixo.


Por exemplo, suponha que o tempo de execução de um filme seja de 105 minutos.

Podemos querer saber a quanto isso corresponde em horas.

Usando a divisão convencional, temos um ponto flutuante como resposta.


```python
>>> minutos_total_filme = 105
>>> minutos_total_filme / 60
1.75
```

 

Não é comum escrever horas com números decimais. 

A divisão pelo piso devolve o número inteiro de horas, ignorando a parte fracionária.

```python
>>> minutos_total_filme = 105
>>> horas_filme = minutos_filme // 60
>>> horas_filme
1
```




Se ainda queremos obter o restante, podemos subtrair a hora inteira recém descoberta da quantidade inicial de minutos:

```python
>>> minutos_restante_filme = minutos_total_filme - horas_filme * 60
>>> minutos_restante_filme
45
```




Uma alternativa para descobrir os minutos restante, seria usar o **operador módulo**, %, que divide dois números e devolve o resto.

```python
>>> minutos_restante_filme = minutos_total_filme % 60
>>> minutos_restante_filme
45
```

Perceba que apenas utilizando os novos operadores conseguiríamos responder a pergunta inicial, em duas instruções.

```python
>>> minutos_total_filme = 105
>>> minutos_total_filme // 60
1
>>> minutos_total_filme % 60
45
```



## Novos operadores - Módulo

O operador por módulo é mais útil do que parece.

É possível, por meio de seu uso verificar se um número é divisível por outro.

Se `x % y` for zero, então x é divisível por y.

Também é possível extrair o dígito ou dígitos mais à direita de um número.

Por exemplo, `x % 10` produz o dígito mais à direita de x (na base 10).
Da mesma forma que `x % 100` produz os dois últimos dígitos.



---
## Expressões booleanas 

Uma expressão booleana é uma expressão que pode ser verdadeira ou falsa.

Os exemplos seguintes usam o operador `==`, que **compara** dois operando e produz `True` se forem iguais e `False` se não forem

```python
>>> 5 == 5
True
>> 5 == 6
False
```

---


`True` e `False` são valores especiais que pertencem ao tipo booleano.

Não são strings.

```python
>>> type(True)
<class 'bool'>
>> type(False)
<class 'bool'>
```

---

### Operadores relacionais

Dentre os **operadores relacionais**, temos:

O operador `==`, que compara se dois valores são iguais.

O operador `!=`, que compara se dois valores são diferentes.

O operador `>`, que compara se um valor é maior a outro.

O operador `<`, que compara se um valor é menor a outro.

O operador `>=`, que compara se um valor é maior ou igual a outro.

O operador `<=`, que compara se um valor é menor ou igual a outro.

---


Alguns símbolos do Python são diferentes dos símbolos matemáticos.

Um erro comum é usar apenas um sinal de igual (=) em vez de um sinal duplo (==).

`=` é um sinal de atribuição e `==` é um operador relacional.

---

### Operadores lógicos

Há três **operadores lógicos**: `and`, `or` e `not`. 

Sua semântica é referente ao significado em inglês.

Por exemplo, 

`x > 0 and x < 10` só é verdade (`True`) se x for maior que 0 `e` menor que 10.

`n % 2 == 0 or n % 3 == 0` é verdadeiro (`True`) se *uma ou as duas* condição(ões) for(em) verdadeira(s), isto é, se o número for divisível por 2 `ou` 3.

`not (x > y)` é verdade (`True`) se x > y for falso, isto é, se x for `menor que ou igual a` y. 
O operador `not` nega uma expressão booleana.

---


O Python não é muito estrito com os operandos dos operadores lógicos.

E aceita qualquer número que não seja zero como `True`.

Essa característica possui sua utilidade, mas há sutilezas que podem ser confusas. 

Portanto use com moderação.


---

## Execução condicional

Para escrever programas, quase sempre precisamos da capacidade de **verificar condições** e mudar o comportamento do programa de acordo com essas condições.

É por meio das **instruções condicionais** que essa capacidade é possível.

A forma mais simples de uma instrução desse tipo é a instrução `if` ("Se", em português).

---

## Execução condicional

```python
>>> if x > 0:
...     print('x é positivo')
...
```

Perceba que há um expressão booleana (`x > 0`) após o `if`. Ela é chamada de **condição**. 

Perceba também que a instrução após a condição é endentada e delimitada por `:`.

Isso significa que assim como a função, aqui também temos um escopo de existência.

Ou melhor, todas as instruções endentadas após a condição, só serão executadas se a condição for verdadeira (possuir valor `True`)

---

### Execução alternativa

A execução alternativa (else ou "senão ou caso contrário") é utilizada quando há duas possibilidades e a condição determina qual será executada.

```python
>>> if num % 2 == 0:
...     print('É par')
... else:
...     print('É impar')
...
```

Se o resto quando num for dividido por 2 for 0, então sabemos que x é par e o programa exibe a uma mensagem para par.

Se a condição for falso, o segundo conjunto de instruções é executado. Logo x é impar e uma mensagem de acordo é exibida.

Como há apenas duas possibilidade para uma condição, ou verdadeira ou falsa, exatamente uma das alternativas será executada. Essas duas alternativas são ramos no fluxo de execução.

---

Meio limitante apenas duas opções, não?

---

## Condicionais encadeadas

As vezes, há mais de duas possibilidades e precisamos de mais de dois ramos no fluxo de execução.

Podemos utilizar condicionais encadeadas (no sentindo de interligadas).

```python
>>> if x < y:
...     print('x é menor que y <=> y é maior que x')
... elif x > y
...     print('x é maior que y <=> y é menor que x')
... else:
...     print('x é igual à y <=> y é igual à x')
...
```

`elif` é uma abreviatura de "else if" (caso contrário, se)

---

### elif

É importante notar, que cada condição é verificada em ordem.

Se uma delas for verdadeira, o ramo correspondente é executado e a instrução é encerrada.

Mesmo, se por acaso, mais de uma condição for verdade, só o primeiro ramo verdadeiro é executado.


---
## Condicionais aninhadas

Condicionais podem ser aninhados (dentro) de outros condicionais.

Por exemplo,


```python
>>> if x == y:
...     print('x é igual à y <=> y é igual a x')
... else:
...     if x < y:
...         print('x é menor que y <=> y é maior que x')
...     else:
...         print('x é maior que y <=> y é menor que x')
...
```

O condicional mais externo, possui dois ramos.
O primeiro ramo contém uma instrução simples **(if)**.
O segundo ramo contém mais duas instruções internas, onde inclusive uma delas, possui uma outra instrução condicional.

---



 Embora seja possível, **condicionais aninhadas** são difíceis de ler rapidamente.

 É uma boa ideia evitá-las quando for possível.

Os operadores lógicos muitas vezes oferecem uma resolução mais simples para instruções aninhadas.

---




Usando condicionais aninhadas

```python
>>> if x > 0:
...     if x < y:
...         print('x é um número positivo de um único dígito')
...
```

Usando operadores lógicos

```python
>>> if x > 0 and x < 10:
...     print('x é um número positivo de um único dígito')
...
```

---


