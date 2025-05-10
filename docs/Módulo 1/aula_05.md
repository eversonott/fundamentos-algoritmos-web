
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



## Prática!



