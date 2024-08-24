# Aula 05 - Entrada e Saída de arquivos (pt. 1)

{% set aula = "05" %}
{% set link = "" %}
{% set codigos = true %}
{% set pesquisas = true %}
{% set slides = false %}
{% set objetivos = ["Formatação de saída", "Strings", "Leitura de arquivos"]%}
{% include "templates/cabecalho.md" %}

---


## Refinando a formatação de saída

Muitas vezes desejamos um maior controle sobre a formatação da saída do que simplesmente exibir valores separados por espaço.

### Strings literais formatadas

Também conhecidas como f=strings, permite que se inclua o valor de expressões Python dentro de uma string, prefixando-a com `f` ou com `F` e escrevendo expressões na forma `{expressão}`.

```py title="Terminal interativo - aula_05/exemplo_01.py"
>>> import math
>>> print(f'O valor aprozimado de pi é {math.pi}.')
O valor aproximado de pi é: 3.141592653589793
```

#### Usando o especificador ':'


```py title="Terminal interativo - aula_05/exemplo_01.py"
>>> import math
>>> print(f'O valor aprozimado de pi é {math.pi:.2f}.')
O valor aproximado de pi é: 3.14.
```

Passando um inteiro após `':'` fará com que o campo tenha um número mínimo de caracteres de largura. Isso é eficiente para alinhar colunas.

Mas conciliando `':'` com um tipo de apresentação numérica. No nosso caso: `.2f`, considera uma notação de ponto-flutuante (float ou número real). Em que o número após o `.` determina exatamente quantos dígitos após a vírgula.

Alinhamento de colunas utilizando `':'`:

Sem `':'`:

```py title="Terminal interativo - aula_05/exemplo_01.py"
>>> cadastro = {'Jõao': 2312, 'Madalena': 4351, 'Alisson': 345}
>>> for nome, id in cadastro.items():
...     print(f'{nome} ==> {id}')
...
Jõao ==> 2312
Madalena ==> 4351
Alisson ==> 345
```

Com `':'`:

```py title="Terminal interativo - aula_05/exemplo_01.py"
>>> cadastro = {'Jõao': 2312, 'Madalena': 4351, 'Alisson': 345}
>>> for nome, id in cadastro.items():
...     print(f'{nome:10} ==> {id:3}')
...
Jõao       ==> 2312
Madalena   ==> 4351
Alisson    ==> 345
```

#### Usando o especificador '='

Esse especificador expande a expressão para seu nome e valor.


```py title="Terminal interativo - aula_05/exemplo_02.py"
>>> aulas = 12
>>> inicio = 9
>>> fim = 11
>>> curso = 'Fundamentos de algoritmos'
>>> print(f'Oferta: {curso=} {aulas=} {inicio=}h e {fim=}h.')
Oferta: curso='Fundamentos de algoritmos' aulas=12 inicio=9h e fim=11h.
```

Podemos usar o `=` pode exibir toda a expressão para que os cálculos possam ser mostrados:



```py title="Terminal interativo - aula_05/exemplo_02.py"
>>> from math import radians as radianos
>>> from math import sin as seno
>>> theta = 30
>>> print(f'{theta=} {seno(radianos(theta))=:.3f}')
theta=30 seno(radianos(theta))=0.500
```

##### Bônus: módulo random

Temos um módulo embutido em Python que implementa geradores de números pseudo-aleatórios para vários distribuições.

```py title="Terminal interativo - aula_05/exemplo_02.py"
>>> from math import radians as radianos
>>> from math import sin as seno
>>> from random import randrange
>>> theta = 30
>>> print(f'{theta=} {seno(radianos(theta))=:.3f}')
>>> for i in range(10):
...     theta = randrange(0,366)
...     print(f'{theta=} {seno(radianos(theta))=:.3f}')
...
theta=276 seno(radianos(theta))=-0.995
theta=167 seno(radianos(theta))=0.225
theta=69 seno(radianos(theta))=0.934
theta=33 seno(radianos(theta))=0.545
theta=362 seno(radianos(theta))=0.035
theta=24 seno(radianos(theta))=0.407
theta=73 seno(radianos(theta))=0.956
theta=317 seno(radianos(theta))=-0.682
theta=182 seno(radianos(theta))=-0.035
theta=44 seno(radianos(theta))=0.695
```

A cada nova interpretação, será novos ângulos. 

Pensem nas possibilidades para testarmos fórmulas?! Ou até mesmo algoritmos próprios.
![](https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExZmVyZ3Jna3huejF1b2hwenFuZWhiOWFhcmsxaGw1MTFqNGt0ZXZiZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/DhstvI3zZ598Nb1rFf/giphy.webp){: .center .shadow width=150px}

### O método format()

Executa uma operação de formatação de string.
As chaves e seus conteúdos (chamados campos de formatação) são substituídos pelos objetos passados para o método `str.format()`.

Pode-se usar 

```py title="Terminal interativo - aula_05/exemplo_03.py"
>>> print('Somos os {} que dizem "{}"!'.format('cavaleiros', 'Ni'))
Somos os cavaleiros que dizem "Ni"!
```

![](https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExZHFxc2NmOGx3b3Rkd242Y3M2dmM0eGNjdGc2bW84OXpjOXJkbjBtOSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/35aVstfJYNlEA/giphy.gif){: .center .shadow}

#### O uso de chaves com o `format()`

Um número nas chaves pode ser usado para referenciar a posição do objeto passado pelos campos de formatação.


```py title="Terminal interativo - aula_05/exemplo_03.py"
>>> print('{0} e {1}'.format('spam', 'bacon'))
>>> print('{1} e {0}'.format('spam', 'bacon'))
```

??? Note "Referência"
    ![type:video](https://www.youtube.com/embed/_bW4vEo1F4E)
    
    O termo `spam` que hoje usamos, veio dessa esquete do Monty Python.

#### Renomeação com o `format()`

Os argumentos de `format()` podem ser renomeados e seus valores podem ser referenciados utilizando o nome do argumento.

```py title="Terminal interativo - aula_05/exemplo_03.py"
>>> print('Eu não gosto de {prato}'.format(prato = 'spam'))
Eu não gosto de spam
```

#### Uso de dicionários com o `format()`

Para strings de formatação longas demais, podemos fazer referência utilizando a estrutura de dados `dict` (dicionário), e realizar a referência diretamente com um nome (chave) do que com a posição.


```py title="Terminal interativo - aula_05/exemplo_03.py"
>>> print('John: {0}; Michael: {2}; Terry: {1}'.format(84, 77, 81))
John: 84; Eric: 81; Terry: 77.
```

Na execução acima, perceba que o valor correto da idade depende diretamente da posição.

Se organizarmos os dados (nome e idade) em um dicionário, e referenciarmos pela chave (nome), fica mais intuitivo. E a possibilidade ao erro diminui.


```py title="Terminal interativo - aula_05/exemplo_03.py"
>>> dados = {'John': 84, 'Eric': 81, 'Terry': 77}
>>> print('John: {0[John]}; Terry: {0[Terry]}; Eric: {0[Eric]}.'.format(dados))
John: 84; Eric: 81; Terry: 77.
```

Perceba que precisamos referência o dicionário com `0` (por meio do `format()`) para acessá-lo com a devida chave.

##### Operador `*` ou `**`

Além de serem utilizados para a multiplicação e exponenciação, os operados `*` e `**`, respectivamente, podem ser utilizados como para 'acessar' um número variável de argumentos e um número arbitrário de argumentos de **palavras-chaves**.

Usando `*`:

```py title="Terminal interativo - aula_05/exemplo_03.py"
>>> numeros = [1, 2, 3, 5, 6]
>>> def adicao(*lista):
...     return sum(lista)
...
>>> print(adicao(*numeros))
17
```

Usando `**`:

```py title="Terminal interativo - aula_05/exemplo_03.py"
>>> dados = {'fruta': 'morango', 'vegetal': 'batata', 'bacon':'span'}
>>> def definicao(**dados):
...     for item in dados:
...         print(dados[item])
...
>>> definicao(**dados)
morango
batata
span
```

Portanto podemos utilizar dados do tipo `dict`, `format()` e operados: `*` e `**`:

```py title="Terminal interativo - aula_05/exemplo_03.py"
>>> dados = {'John': 84, 'Eric': 81, 'Terry': 77}
>>> print('John: {John}; Terry: {Terry}; Eric: {Eric}.'.format(**dados))
John: 84; Eric: 81; Terry: 77.
```

Com `**` operamos diretamente sobre as chaves do dicionário.

Podemos construir colunas alinhadas:

## Leitura de arquivos

### Open 

> Open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

A princípio vamos considerar dois argumentos posicionais e um argumento nomeado, os argumentos: file, mode, encoding.

`file` é uma objeto que representa um caminho (absoluto ou relativo ao diretório atual) do arquivo que será aberto.

`mode` é uma string opcional que especifica o modo no qual o arquivo é aberto. O valor padrão é `'r'`, o qual significa abrir para leitura em modo texto.

!!! danger "Importante:"
    No modo texto, se `encoding` não for especificado, a codificação usada depende da plataforma. Uma função é chamada para obter a codificação da localidade atual.

#### Modos disponíveis

|Caractere  |Significado                                                                               |
|-----------|-------------------------------------------------------------------------------------------|
|`'r'`      |Abre para leitura (padrão)                                                                 |
|`'w'`      |Abre para escrita, truncando o arquivo primeiro (remove tudo que estava contido no arquivo.|
|`'x'`      |Abre para criação exclusiva, falha caso o arquivo exista.                                  |
|`'a'`      |Abre para escrita, anexa ao final do arquivo caso o mesmo exista.                          |
|`'b'`      |Abre o arquivo no modo binário.                                                            |
|`'t'`      |Abre o arquivo no modo texto (padrão).                                                     |
|`'+'`      |Abre o arquivo para atualização (leitura e escrita)                                        |


Perceba que temos dois padrões: Leitura e modo texto. O modo padrão `'r'` equivale à `'rt'`. A opção `'r+'` abre o arquivo para leitura e escrita, sem truncar.

!!! info "Detalhe:"
    A opção `'b'` irá abrir o arquivo no *modo binário*. Isso significa que os dados são lidos e escritos em **bytes**, por isso também que não é preciso especificar o `encoding`.

### A palavra-chave `with`

`with` é um gerenciado de contexto, um objeto que define o contexto de tempo de execução a ser estabelecido em uma instrução.

Um gerenciador de contexto lida com a entrada e saída doo contexto por tempo de execução necessário para a execução do bloco de código.

Seu uso para a leitura de arquivos se justifica, porque `with` garante o fechamento do arquivo após a abertura (contexto). 

Considere o arquivo que será lido:

```py title="aula_05/nomes.txt" linenums="1"
--8<-- "./codigo/aula_05/nomes.txt"
```

```py title="Terminal interativo - aula_05/exemplo_04.py"
>>> with open('nomes.txt', encoding='utf-8') as arq:
...     nomes = arq.read()
...
>>> print(nomes)
Graham Chapman
John Cleese
Eric Idle
Terry Jones
Michael Palin

```

Vamos entender o que aconteceu:

Sobre o `encoding`, UTF-8 é o padrão de codificação mais utilizado. Compatível com o ASCII (sistema de representação de letras, algarismos e sinais de pontuação e de controle desenvolvido em 1960).

`read(size=-1)` é um método do objeto arquivo. Esse método lê o arquivo até determinada quantidade de caracteres ou até o final do arquivo (EOF - End of file) - **padrão**, quando o tamanho é omitidoo ou negativo. Devolve esses dados em uma string (modo texto) ou bytes (modo binário).

O método `f.readline() também retorna uma `string`, porém lê uma única linha do arquivo; O caractere de quebra de linha (`\n`) é mantido ao final da string, esse caractere só é omitido, caso o arquivo não termine com uma quebra de linha. 

```py title="Terminal interativo - aula_05/exemplo_04.py"
>>> with open('nomes.txt', encoding='utf-8') as arq:
...     nomes = arq.readline()
...
>>> print(nomes)
Graham Chapman

```

O método `f.readlines()` retorna uma lista, em que cada item é uma linha, inclusive com o caractere de quebra de linha (`\n`).

```py title="Terminal interativo - aula_05/exemplo_04.py"
>>> with open('nomes.txt', encoding='utf-8') as arq:
...     nomes = arq.readlines()
...
>>> print(nomes)
['Graham Chapman\n', 'John Cleese\n', 'Eric Idle\n', 'Terry Jones\n'
, 'Michael Palin\n']
```


#### Maneira alternativa de leitura


Podemos iterar sobre o objeto arquivo para ler as linhas.

```py title="Terminal interativo - aula_05/exemplo_04.py"
>>> with open('nomes.txt', encoding='utf-8') as arq:
...     for linha in arq:
...         print(linha, end='')
...
Graham Chapman
John Cleese
Eric Idle
Terry Jones
Michael Palin
```

## Pesquisas sobre a aula

--8<-- "./Módulo 2/Pesquisas/aula_05.html"

