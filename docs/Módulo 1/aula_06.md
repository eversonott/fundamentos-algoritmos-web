# Aula 06 - Expressões booleanas, Operadores Relacionais, Operadores Lógicos e Execução Condicional


{% set aula = "06" %}
{% set link = "" %}
{% set objetivos = 
[
]
%}
{% include "templates/cabecalho_sem_video.md" %}

## Funções (continuação)

### Novas funções (continuação)

#### As variáveis e os parâmetros são locais

Quando uma variável é criada dentro de uma função seja ela parâmetro ou não, ela é local, ou seja, só existe dentro da função. Só existe dentro do escopo da função.

```python
>>> def imprime_concatenacao_duas_strings(parte_inicial, parte_final):
...     texto = parte_inicial + parte_final
...     imprime_nome(texto)
...
```

Essa função recebe dois argumentos, concatena-os e exibe o resultado utilizando a função `imprime_nome`, que acabamos de criar.


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



#### Funções com resultado e funções sem resultados (métodos)

Até o momento criamos funções que apenas exibem algo na tela e não especificamente possuem um valor de retorno, ou um resultado retornado.

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

#### Mais exemplos de funções

```python title='funcoes.py'
def resolutiva_primeiro_grau(a, b):
    raiz = -b/a
    return raiz
```
Agora conseguimos resolver equações de primeiro grau, usando programação.
Por exemplo, qual é a raiz da função de primeiro grau: $2x + 16$?

Basta:

```python title='terminal: python -i funcoes.py'
resolutiva_primeiro_grau(2, 16):
-8.0
```

Vamos além!

Vamos tentar fazer um algoritmo da resolutiva de segundo grau:

```python title='funcoes.py'
import math
def resolutiva_segundo_grau(a, b, c):
    delta = b**2 - (4 * a * c) # Ou delta = math.pow(b, 2) - (4 * a * c)
    raiz_1 = (-b + math.sqrt(delta))/(2* a)
    raiz_2 = (-b - math.sqrt(delta))/(2* a)
    return raiz_1, raiz_2
```

Testando:

```python title='terminal: python -i funcoes.py'
>>> resolutiva_segundo_grau(2,3,-5)
(1.0, -2.5)
```

O exemplo acima resolve a função de segundo grau $2x^2 + 3x -5$

Mas o que aconteceria se por acaso confundirmos a ordem na passagem dos argumentos?

Bom, teríamos equações diferentes. Uma vez que, mudando a ordem, mudamos os coeficientes.

Por exemplo, alternando a ordem dos números 2 e 3 teríamos a equação $2x^2 + 2x - 5$, logo a raiz também seria diferente.

Para passar a ordem correta, precisamos ter acesso a declaração literal da função ou pedimos ajuda!


Ajuda em inglês é: help.

```python title='terminal'
import math
help(math.pow)
```

Como saída, obtemos um sistema interativo de ajuda do python

```txt
Help on built-in function pow in module math:

pow(x, y, /)
    Return x**y (x to the power of y).
~
```

Traduzindo:

```txt
Ajuda sobre a função interna pow no módulo math:

pow(x, y, /)
Retorna x**y (x elevado à potência de y).
~
```

Veja, não precisamos ir até o arquivo responsável pela implementação da função `pow` do módulo embutido do Python.
Basta passar por parâmetro o nome do objeto que queiramos consultar.

#### Usando o `help` como nossas funções

```python title='terminal'
>>> help(resolutiva_segundo_grau)
```

Obtemos:

```txt
Help on function resolutiva_segundo_grau in module __main__:

resolutiva_segundo_grau(a, b, c)
```

Ops! Conseguimos ver o nome dos parâmetros, lembra-se de nomear corretamente.
Esses nomes não parecem ser significativos.

Primeiro vamos deixar os nomes mais claros:

```python title='funcoes.py'
import math
def resolutiva_segundo_grau(coeficiente_a, coeficiente_b, coeficiente_c):
    delta = coeficiente_b**2 - (4 * coeficiente_a * coeficiente_c) # Ou delta = math.pow(b, 2) - (4 * a * c)
    raiz_1 = (-coeficiente_b + math.sqrt(delta))/(2* coeficiente_a)
    raiz_2 = (-coeficiente_b - math.sqrt(delta))/(2* coeficiente_a)
    return raiz_1, raiz_2
```

Agora temos:

```txt
Help on function resolutiva_segundo_grau in module __main__:

resolutiva_segundo_grau(coeficiente_a, coeficiente_b, coeficiente_c)
```

Agora está mais claro, mas parece falta um maior detalhamento sobre o que nossa função faz.

Está faltando uma documentação!

Está faltando `DocString`

## DocString

As convenções das DocString é oficializada por meio de uma PEP (Vimos [PEP](../../Módulo 1/aula_02/#pep) na aula anterior).

### PEP 257 - Convenções DocString

Criada por David Goodger e pelo fundador do Python Guido van Rossum


Essa PEP documenta a semântica e as convenções a Documentos Python.

Existem duas formas de docstrings: Única-linha ou Múltiplas-linhas

### Única linha

Única-linha são usadas para caso realmente óbvios. Portanto devem caber em uma linha, uma frase.

```python title='funcoes.py'
def calcula_potencia(base, expoente):
    """Fornecido a base e expoente, retorna a potência."""
    potencia = base ** expoente
    return potencia
```

```python title='terminal: python -i funcoes.py'
help(calcula_potencia)
```

Resulta em:

```txt
Help on function calcula_potencia in module __main__:

calcula_potencia(base, expoente)
    Fornecido a base e expoente, retorna a potência.
```

Perceba que a docstring documentada na função agora aparece quando passamos o nome da função para o `help` do Python.


Vale destacar alguns pontos:

- Aspas triplas são usadas mesmo que a string caiba em uma linha. Isso torna mais fácil expandi-lo posteriormente.
- As aspas de fechamento estão na mesma linha das aspas de abertura. Esse parece melhor para frases simples.
- Não há linha em branco antes ou depois da docstring.
- A docstring é uma frase que termina em um ponto final. Ela prescreve o função ou efeito do método como um comando (“Faça isto”, “Retorne aquilo”), não como uma descrição; por exemplo, não escreva “Retorna a potência...”. 
- A doutrina de uma linha NÃO deve ser uma “assinatura” reiterando a parâmetros de função/método (que podem ser obtidos por introspecção).
    - Não faça:
    ```python title='funcoes.py'
            def calcula_potencia(base, expoente):
            """function(base, expoente) -> float"""
            potencia = base ** expoente
            return potencia
    ```

### Múltiplas-linhas

Vamos começar pelo exemplo:


```python title='funcoes.py'
import math
def resolutiva_segundo_grau(coeficiente_a, coeficiente_b, coeficiente_c):
    """Retorna as raízes de uma equação de segundo grau.

    Argumentos:
    coeficiente_a -- Coeficiente que multiplica x^2.
    coeficiente_b -- Coeficiente que multiplica x.
    coeficiente_c -- Coeficiente independente.
    """
    delta = coeficiente_b**2 - (4 * coeficiente_a * coeficiente_c) # Ou delta = math.pow(b, 2) - (4 * a * c)
    raiz_1 = (-coeficiente_b + math.sqrt(delta))/(2* coeficiente_a)
    raiz_2 = (-coeficiente_b - math.sqrt(delta))/(2* coeficiente_a)
    return raiz_1, raiz_2
```

Documentos multilinhas consistem em uma linha de resumo, assim como uma linha docstring, seguido por uma linha em branco, seguido por um texto mais elaborado descrição. 

##### Linha de resumo:

- A linha de resumo pode ser usada pela indexação automática ferramentas; 
- É importante que caiba em uma linha e esteja separado de o restante da documentação por uma linha em branco. 

#### Docstring:

- O inteiro docstring é recuado da mesma forma que as aspas em sua primeira linha.


##### Docstring para funções:

- A docstring para uma função ou método deve resumir seu comportamento e documentar seus argumentos, valores de retorno, efeitos colaterais, exceções levantado e restrições sobre quando pode ser chamado (todos, se aplicável). 
- Argumentos opcionais devem ser indicados. 
- Deve ser documentado se os argumentos de palavras-chave fazem parte da interface.

##### Alguns exemplos de novas funções utilizando Docstring

```python title='formulas_muv.py'
# Fórmulas da aceleração do MUV

def aceleracao_muv(velocidade_final, velocidade_inicial, tempo):
    """ Fornecido a velocidade final (m/s), velocidade inicial (m/s) e o tempo (s), retorna a aceleração do movimento uniformemente variado (m/s²).
    
    Argumentos:
    velocidade_final -- Velocidade final do Movimento Uniformemente Variado
    velocidade_inicial -- Velocidade inicial do Movimento Uniformemente Variado
    tempo -- Tempo decorrido do Movimento Uniformemente Variado
    """
    aceleracao = (velocidade_final - velocidade_inicial) / tempo
    return aceleracao


def espaco_final_muv(espaco_inicial, velocidade_inicial, tempo, aceleracao):
    """ Fornecido o espaço inicial (m), velocidade inicial (m/s), tempo (s) e a aceleração (m/s²), retorna o espaço final.
    
    Argumentos:
    espaco_inicial -- Espaço inicial do Movimento Uniformemente Variado
    velocidade_inicial -- Velocidade inicial do Movimento Uniformemente Variado
    tempo -- Tempo decorrido do Movimento Uniformemente Variado
    aceleracao -- Aceleração do Movimento Uniformemente Variado
    """
    espaco_final_muv = espaco_inicial + velocidade_inicial * tempo + (aceleracao * tempo ** 2)/2
    return espaco_final_muv
```


```python title="Terminal - python -i formulas_muv.py"
help(aceleracao_muv)
```

```txt title='help interativo'
Help on function aceleracao_muv in module __main__:

aceleracao_muv(velocidade_final, velocidade_inicial, tempo)
    Fornecido a velocidade final (m/s), velocidade inicial (m/s) e o tempo (s), retorna a aceleração do movimento uniformemente variado (m/s²).

    Argumentos:
    velocidade_final -- Velocidade final do Movimento Uniformemente Variado
    velocidade_inicial -- Velocidade inicial do Movimento Uniformemente Variado
    tempo -- Tempo decorrido do Movimento Uniformemente Variado
```


```python title="Terminal - python -i formulas_muv.py"
# Calculando a aceleração de um objeto móvel de velocidade final 10 m/s, velocidade inicial de 2 m/s decorridos 5 segundos.
aceleracao_muv(10, 2, 5)
1.6
```



## Entrada de teclado

Para interagirmos com nossas funções estamos passando seu argumento manualmente.

Podemos fazer isso de maneira mais interativa, no sentido de que o próprio usuário que está interagindo com a função carregue seus argumentos.

O Python fornece uma função integrada chamada `input` que interrompe o programa e espera que usuário digite algo.

Quando o usuário pressionar Enter, o programa volta a ser executado e input, que é uma função **retorna** o que o usuário digitou como uma string.

```python
>>> texto = input()
Teste de texto
>>> texto
'Teste de texto'
```


A função `input` tem como parâmetro uma string que é exibida ao usuário como orientação, a chamamos de argumento prompt.

```python
>>> nome = input('Insira seu nome: ')
Insira seu nome: Everson
>>> nome
'Everson'
```


Podemos passar por meio de uma variável o argumento prompt

```python
>>> mensagem_usuario_nome = 'Insira seu nome: '
>>> nome = input(mensagem_usuario_nome)
Insira seu nome: Everson
>>> nome
'Everson'
```


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



## A função dir do Python

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

# Aula 04 - Novos operadores e manipulação de scripts em Python

Fundamentos de algoritmos e introdução à programação em Python

Prof. Everson Otoni


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



## IDLE - (Slide da primeira aula) 

O instalador do Python para Windows contém o módulo IDLE por padrão.

IDLE é um Ambiente de Desenvolvimento e Aprendizagem Integrado.

Para iniciar o shell interativo IDLE, procure o ícone IDLE no menu Iniciar e clique duas vezes nele.

![w:450](https://raw.githubusercontent.com/eversonott/fundamentos-algoritmos/main/slides/md/imagens/idle.png)



## IDLE - (Slide da primeira aula) 

Onde efetivamente, o *interpretador* Python, um programa. Lê e executa o código Python.

![w:500](https://raw.githubusercontent.com/eversonott/fundamentos-algoritmos/main/slides/md/imagens/idle_uso.gif)




--
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

