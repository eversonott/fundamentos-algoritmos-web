---
search:
  exclude: true
---
# Aula 04 - Módulos (pt. 2) e pacotes em Python

{% set aula = "04" %}
{% set link = "" %}
{% set pesquisas = true %}
{% set codigos = true %}
{% set slides = false %}
{% set objetivos = [
"Módulos em Python embutidos", 
"O uso da função `dir()` com módulos", 
"Pacotes em Python"] 
%}
{% include "templates/cabecalho.md" %}

---
## Módulos

![](https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExYW43Y3lnOWFpNG44bHhhdzhxZzRmb2lqMmp3bndieXN0ODhoOXp0ZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/xUA7aVbrKntotcCzVS/giphy.webp){: .center .shadow}

Já vimos, desde [Aula 04 - Manipulação de scripts em Python no Módulo 1](./Módulo 1/aula_04.md#idle-slide-da-primeira-aula){:target="_blank"} como executar um programa maior e executá-lo usando o arquivo como entrada, ou seja, criação e manipulação de scripts em Python.

Uma boa prática para programas muito grandes é dividi-lo em arquivos menores, afim de facilitar a manutenção.

Também é preferível usar um arquivo separado para uma função que você escreveria em vários programas diferentes. 

> Lembre-se repetição de código não é uma boa prática

### Criando módulos

Para isso, basta colocar as definições em um arquivo e então usá-las em um script ou em uma execução do interpretador.

Esse arquivo, chama-se módulo. 

**Um módulo, portanto, é um arquivo contendo definições e instruções Python.**

Vamos criar um módulo que contenha os dois algoritmos de ordenação que vimos até agora.

```py title="ordenacoes.py" linenums="1" hl_lines="2 8"
def ordenacao_insercao(lista_recebida):
    lista = lista_recebida
    for i in range(0, len(lista)):
        indice_anterior = i - 1
        while indice_anterior >= 0 and lista[indice_anterior] > lista[indice_anterior + 1]:
            lista[indice_anterior + 1], lista[indice_anterior] = lista[indice_anterior], lista[indice_anterior + 1]
            indice_anterior -= 1
    return lista


def intercalar_listas_ordenadas(esquerda, direita):
    indice_esq = 0
    indice_dir = 0
    resultado = []

    while indice_esq < len(esquerda) and indice_dir < len(direita):
        if esquerda[indice_esq] <= direita[indice_dir]:
            resultado.append(esquerda[indice_esq])
            indice_esq += 1
        else:
            resultado.append(direita[indice_dir])
            indice_dir += 1

    while indice_esq < len(esquerda):
        resultado.append(esquerda[indice_esq])
        indice_esq += 1

    while indice_dir < len(direita):
        resultado.append(direita[indice_dir])
        indice_dir += 1
    return resultado


def ordenacao_intercalacao(lista):
    tamanho = len(lista)

    indice_meio = tamanho // 2

    if tamanho <= 1:
        return lista
    else:
        metade_esquerda = ordenacao_intercalacao(lista[:indice_meio])
        metade_direita = ordenacao_intercalacao(lista[indice_meio:])
        return intercalar_listas_ordenadas(metade_esquerda, metade_direita)

```

Modificamos o algoritmo da função `ordenacao_insercao` para que se comporte da mesma maneira que `ordenacao_intercalacao` retornando a lista.


Vamos agora criar um arquivo que utilizará do nosso módulo recém criado.

Para isso utilizamos `import` para "importar" o módulo.  


```py title="aula_04_modulos.py" linenums="1"
import ordenacao

```

Nossa estrutura de arquivos e pastas está assim:

```
.
├── aula_04_modulos.py
└── ordenacoes.py
```

O arquivo que vamos usar o módulo e o próprio módulo estão **na mesma pasta**.


Até agora só adicionamos o nome do módulo `ordenacao`.

Usando o nome do módulo importado, podemos acessar as funções.

```py title="aula_03_modulos.py" linenums="1" hl_lines="7 13"
import ordenacoes

arranjo = [6, 5, 4, 2]
print(arranjo)

print("Por inserção: ", ordenacoes.ordenacao_insercao(arranjo))

arranjo = [6, 5, 4, 2]
print(arranjo)

print("Por intercalação: ", ordenacoes.ordenacao_intercalacao(arranjo))
```

```shell title="Resposta do comando: python aula_04_modulos.py" hl_lines="2 4"
[6, 5, 4, 2]
Por inserção:  [2, 4, 5, 6]
[6, 5, 4, 2]
Por intercalação:  [2, 4, 5, 6]

```

É claro que, se pretendemos usar muitas vezes uma função importada, podemos atribuí-la a um nome local:


```py title="aula_03_modulos.py" linenums="1" hl_lines="3 7 11 13 17"
import ordenacoes

insercao = ordenacoes.ordenacao_insercao

arranjo = [6, 5, 4, 2]
print('Arranjo desornedado:', arranjo)
print("Ordenado por inserção:", insercao(arranjo))

arranjo = [45, 34, 4, 2, 1]
print('Arranjo desornedado:', arranjo)
print("Ordenado por inserção: ", insercao(arranjo))

merge_sort = ordenacoes.ordenacao_intercalacao

arranjo = [346, 120, 58, 23, 11]
print('Arranjo desornedado:', arranjo)
print("Ordenado por intercalação: ", merge_sort(arranjo))
```

```shell title="Resposta do comando: python aula_04_modulos.py" hl_lines="2 4"
Arranjo desornedado: [6, 5, 4, 2]
Ordenado por inserção: [2, 4, 5, 6]
Arranjo desornedado: [45, 34, 4, 2, 1]
Ordenado por inserção:  [1, 2, 4, 34, 45]
Arranjo desornedado: [346, 120, 58, 23, 11]
Ordenado por intercalação:  [11, 23, 58, 120, 346]
```


Um módulo pode conter tanto instruções executáveis quanto definições de funções e classes (veremos posteriormente).

Essa instruções e definições só são executadas somente na **primeira vez** que o módulo é encontrado em uma instrução de importação (`import`, que vimos até agora).

Módulos podem importar outros módulos.

Costuma-se colocar todas as instruções `import` no início do módulo (ou script, se preferir).

As definições do módulo importado, se colocados no nível de um módulo (fora de quaisquer funções ou classes), serão adicionadas a espaço de **nomes globais** do módulo.


### Variantes do `import`

Existe uma variante da instrução `import`, que importa definições de um módulo diretamente para o espaço de nomes do módulo importador. Por exemplo:


```py title="aula_03_ex2.py" linenums="1" hl_lines="1 5 9"
from ordenacoes import ordenacao_insercao, ordenacao_intercalacao

arranjo = [6, 5, 4, 2]
print(arranjo)
print("Por inserção: ", ordenacao_insercao(arranjo))

arranjo = [6, 5, 4, 2]
print(arranjo)
print("Por intercalação: ", ordenacao_intercalacao(arranjo))

```

Dessa maneira, o nome do módulo de onde foram feitas as importações não é colocado no espaço de nomes locais, ou seja,


`ordenacao` não está definido como objeto.

Se o nome do módulo é seguindo pela palavra-chave `as`, que significa alias (ˈālēəs), ou seja, pseudônimo ou "apelido".

O nome a seguir é vinculado diretamente ao módulo importado.


```py title=">>> Terminal interativo do arquivo aula_04_modulos.py" hl_lines="1"
	>>> import ordenacao as algoritmos
    >>> arranjo = [6, 5, 4, 2]
	>>> algoritmos.ordenacao_insercao(arranjo)
	>>> arranjo
	[2, 4, 5, 6]
```

Isto importa o módulo, da mesma maneira que `import ordenacao` fará, com a diferença de estar disponível com o nome `algoritmos`.

Também podemos usar `as` com a palavra-chave `from`, e obter efeitos similares:

```py title=">>> Terminal interativo!" hl_lines="1"
    >>> from ordenacao import ordenacao_insercao as insercao
    >>> arranjo = [6, 5, 4, 2]
    >>> insercao(arranjo)
    >>> arranjo
    [2, 4, 5, 6]
```

Assim não é necessário notação de ponto e nem declarar um objeto local para simplificar o nome do objeto.


!!! danger "Atenção"
    Por eficiência, cada módulo é importado apenas uma vez por sessão do intérprete. Portanto, se você alterar seus módulos, deverá reiniciar o interpretador, ou se for apenas um módulo que deseja testar, use importlib.reload(). Por exemplo:

    ```py title=">>> Terminal interativo!" 
        >>> import importlib
        >>> importlib.reload(`nome do módulo`)
    ```


Quando um módulo é chamado, o interpretador procura um módulo embutido com este nome.

Módulos embutidos podem ser listados com: `sys.builtin_module_names`.

```py title="Terminal interativo"
>>> import sys
>>> sys.builtin_module_names
('_abc', '_ast', '_codecs', '_collections', '_functools', '_imp', '_io', 
'_locale', '_operator', '_signal', '_sre', '_stat', '_string', '_suggestions', 
'_symtable', '_sysconfig', '_thread', '_tokenize', '_tracemalloc', '_typing', 
'_warnings', '_weakref', 'atexit', 'builtins', 'errno', 'faulthandler', 'gc', 
'itertools', 'marshal', 'posix', 'pwd', 'sys', 'time')
```

Se não encontra, procura um arquivo com o mesmo nome em uma lista de diretórios incluídos na variável `sys.path`. Que nada mais é do que uma lista de strings que especifica o caminho de pesquisa para módulos.


```py title="Terminal interativo"
>>> import sys
>>> sys.path
['', '/usr/lib/python313.zip', '/usr/lib/python3.13', 
 '/usr/lib/python3.13/lib-dynload', 
 '/home/aristoteles/.local/lib/python3.13/site-packages', 
 '/usr/lib/python3.13/site-packages']
```

Como se trata de uma lista podemos modificá-la com as operações típicas de lista, por exemplo:
```py title="Terminal interativo"
>>> import sys
>>> sys.path.append('../guido/lib/python')
```

Como diria o Tio Ben, use com responsabilidade.

### Função `dir()`

Relembrando da função `dir()` que vimos em [Aula 03 - Funções do Módulo 1](../../Módulo 1/aula_03/#ainda-sobre-funcoes-embutidas).

Sem argumentos, `dir()` lista os nomes atualmente definidos:

```py title="Terminal interativo" 
>>> dir()
['__annotations__', '__builtins__', '__cached__', '__doc__', 
 '__file__', '__loader__', '__name__', '__package__', '__spec__']
```

Vamos considerar novamente o módulo `ordenacao.py`:

```py title="ordenacao.py" linenums="1"
--8<-- "./codigo/aula_04/ordenacoes.py"
```

```py title="Terminal interativo" hl_lines="5 9"
>>> import ordenacoes
>>> dir()
['__annotations__', '__builtins__', '__cached__', '__doc__', 
 '__file__', '__loader__', '__name__', '__package__', '__spec__', 
 'ordenacoes']
>>> dir(ordenacoes)
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__',
 '__name__', '__package__', '__spec__', 
 'intercalar_listas_ordenadas', 'ordenacao_insercao', 'ordenacao_intercalacao']
```

Temos como retorno os nomes: `intercalar_listas_ordenadas`, `ordenacao_insercao`, `ordenacao_intercalacao`

Ou seja, a função `dir()` lista todo tipo de nomes: variáveis, módulos, funções, etc.

### Módulo `builtins`

Para listar os nomes de variáveis e funções embutidas. Utilizamos o módulo padrão `builtins`:


```py title="Terminal interativo" 
>>> import builtins
>>> dir(builtins)
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException',
 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning',
 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError',
 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning',
 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False',
 'FileExistsError', 'FileNotFoundError', 'FloatingPointError',
 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError',
 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError',
 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError',
 'MemoryError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented',
 'NotImplementedError', 'OSError', 'OverflowError',
 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError',
 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning',
 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError',
 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError',
 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError',
 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning',
 'ValueError', 'Warning', 'ZeroDivisionError', '_', '__build_class__',
 '__debug__', '__doc__', '__import__', '__name__', '__package__', 'abs',
 'all', 'any', 'ascii', 'bin', 'bool', 'bytearray', 'bytes', 'callable',
 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits',
 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit',
 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr',
 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass',
 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview',
 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property',
 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice',
 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars',
 'zip']
```

Explore-as!
Use `help()` para te auxiliar.

## Pacotes

Um pacote é uma coleção de módulos.

Portanto passamos da configuração:

```sh
.
├── aula_04_modulos.py
└── ordenacoes.py
```

Para:
```sh
.
├── aula_04_modulos.py
└── ordenacao
    ├── __init__.py
    ├── insercao.py
    └── intercalacao.py
```

E até mesmo:

```sh
.
├── algoritmos
│   ├── __init__.py
│   └── ordenacao
│       ├── __init__.py
│       ├── insercao.py
│       └── intercalacao.py
└── aula_04_modulos.py
```
Os pacotes servem para estruturar o "espaço de nomes" dos módulos Python, usando "nomes de módulos com pontos".

Por exemplo, o nome do módulo `A.B`, designa um submódulo chamado `B`, em um pacote chamado `A`.
Isso facilita a organização entre módulos, evitando a preocupação com nomes de variáveis globais.



### Alguns uso de pacotes


Na importação, Python busca pelo subdiretório com o mesmo nome, nos diretórios listados em `sys.path`

Os aquivos `__init__` são necessários para que o Python trate diretórios contendo o arquivo como pacotes.
No caso mais simples `__init__` pode ser um arquivo vazio, tendo a potencialidade de executar um código de inicialização do pacote, ou configurar variáveis.

Podemos importar módulos individuais:

```py title="aula_04_modulos.py"
import algoritmos.ordenacao.insercao
```

Isso carrega o submódulo algoritmos.ordenacao.insercao


Lembrando para utilizarmos dessa maneira, deve-se referenciar o nome completo, ou usar o apelido:

```py title="aula_04_modulos.py"
algoritmos.ordenacao.insercao.ordenacao_insercao(arranjo)
```

```py title="aula_04_modulos.py"
import algoritmos.ordenacao.insercao as ord

arranjo = [6, 5, 4, 2]
print(arranjo)

print("Por inserção: ", ord.ordenacao_insercao(arranjo))
```

Podemos também importar uma única variável ou função:

```py title="aula_04_modulos.py"
from algoritmos.ordenacao.intercalacao import ordenacao_intercalacao

arranjo = [6, 5, 4, 2]
print(arranjo)

print("Por intercalção: ", ordenacao_intercalacao(arranjo))
```

Agora a função `ordenacao_intercalacao` está acessível diretamente sem prefixo:

```py title="aula_04_modulos.py"
print("Por intercalção: ", ordenacao_intercalacao(arranjo))
```


!!! note "Observe:"

    - Ao utilizar a notação `from pacote import item`, o `item` pode ser um subpacote, submódulo, classe, função ou variável.

    - Em oposição, a notação `import item.subtitem.subsubitem`, cada item, com exceção do último, deve ser um pacote.

O último pode ser também um pacote ou módulo, mas nunca uma classe, função ou variável contida em um módulo.

### Referência em um mesmo pacote

Para os exemplos a seguir vamos considerar a seguinte estrutura de um projeto:

Vamos projetar um pacote para gerenciamento uniforme de arquivos de som.

Há diferentes formatos de arquivos de áudio. Vamos considerar as extensões `.wav`, `.aiff` e `.au`. 

Além de ser necessário módulos de conversão entre os formatos. Também precisaremos realizar operações diferentes nos arquivos de áudio, como: mixagem, eco, equalização, efeitos stereo artificial, entre outros. Isso significa mais módulos.

Vamos pensar em uma possível estrutura hierárquica para nosso pacote:


```shell title="in audio/"
.
├── audio
│   ├── __init__.py
│   ├── formatos
│   │   ├── __init__.py
│   │   ├── wav_leitura.py
│   │   ├── wav_escrita.py
│   │   ├── aiff_leitura.py
│   │   ├── aiff_escrita.py
│   │   ├── au_leitura.py
│   │   └── au_escrita.py
│   ├── efeitos
│   │   ├── __init__.py
│   │   ├── reverso.py
│   │   └── eco.py
│   └── filtros
│       ├── __init__.py
│       ├── karaoke.py
│       ├── equalizador.py
│       └── codificador_voz.py
└── arquivo_qualquer.py
```


Quando estruturamos pacotes compostos por subpacotes (como o pacote `audio` do nosso exemplo), pode-se usar a sintaxe de importações **absolutas** ou **relativas** para se referir aos submódulos **irmãos**.

Por exemplo, se o módulo `audio.filtros.codificador_voz` precisar usar o módulo `eco` do subpacote `audio.efeitos`.

#### Modo absoluto:

```py title="./audio/filtros/codificador_voz.py"
from audio.efeitos import eco
```

No módulo absoluto o caminho parte da pasta principal (pacote `audio`). Por isso é absoluto, pois a referência é absoluta em qualquer módulo, de qualquer subpacote.

#### Modo relativos:

Importações relativas, utilizam pontos para indicar o pacote pai e o atual, envolvidos.

Para importar o módulo `audio.filtros.equalizador`:

```py title="./audio/filtros/codificador_voz.py"
from . import equalizador
```

Para importar o subpacote `audio.efeitos`, de fato:

```py title="./audio/filtros/codificador_voz.py"
from .. import efeitos
```

Para importar o módulo `audio.formatos.wav_leitura`:

```py title="./audio/filtros/codificador_voz.py"
from ..formatos import wav_leitura
```

Perceba que no último exemplo, com os `..` foi possível escalar a pasta pai (subpacote filtros) e ir "relativamente" ao pacote `audio`. Assim, sendo possível "navegar" até o subpacote `formatos` e importar seu módulo `wav_leitura`


Note, portanto que os `imports` **relativos** são baseados no nome do módulo atual.

### Importando TUDO!

O que acontece quando escrevemos `from audio.efeitos import *`?

Asterisco (\*) é um caractere coringa que significa **todos**.

Funcionalmente, esse comando vasculha o sistema de arquivos e encontra todos os submódulos presentes no pacote e os importa.

Mas analiticamente, isso poderia demorar muito a depender da quantidade de submódulos presentes, o que ocasionaria efeitos colaterais indesejáveis.

Uma solução seria o autor do pacote fornecer um índice explícito do pacote.
E para isso deve-se utilizar o arquivo `__init__.py`.

Definimos, então um lista chamada `__all__`, que indicará os nomes dos módulos a serem importados quando a instrução, por exemplo `from audio.efeitos import *` for acionada.


```py title="./audio/efeitos/__init__.py"
__all__ = ["eco"]
```

Isso significa que agora `from audio.efeitos import *` fica restrito a importar somente o módulo `eco`. Claro é inviável criar uma lista com um único item, apenas estamos utilizando do critério didático.

### Outras funções do `__init__.py`

Se houver algum código dentro do arquivo `__init__.py`, ele será executado durante o processo de importação do pacote. Por exemplo, pode ser necessário configurar variáveis globais, log ou algum outro dado que seu módulo necessita carregar previamente.

#### Exemplo real:

Temos abaixo o diretório principal do Numpy:

!!! note "NumPy"
    NumPy é o pacote fundamental para computação científica em Python. É uma biblioteca Python que fornece um objeto array multidimensional, vários objetos derivados (como arrays e matrizes mascaradas) e um variedade de rotinas para operações rápidas em arrays, incluindo matemática, lógica, manipulação de formas, classificação, seleção, E/S, transformadas discretas de Fourier, álgebra linear básica, estatística básica operações, simulação aleatória e muito mais.
    [Mais informações](https://numpy.org/doc/stable/user/whatisnumpy.html){:target="_blank"}

```py title="in ./numpy/"
.
├── __config__.py.in
├── __init__.cython-30.pxd
├── __init__.pxd
├── __init__.py
├── __init__.pyi
├── _array_api_info.py
├── _array_api_info.pyi
├── _configtool.py
├── _distributor_init.py
├── _expired_attrs_2_0.py
├── _globals.py
├── _pytesttester.py
├── _pytesttester.pyi
├── conftest.py
├── ctypeslib.py
├── ctypeslib.pyi
├── dtypes.py
├── dtypes.pyi
├── exceptions.py
├── exceptions.pyi
├── matlib.py
├── meson.build
├── py.typed
├── version.pyi
├── _build_utils
├── _core
├── _pyinstaller
├── _typing
├── _utils
├── char
├── compat
├── core
├── distutils
├── doc
├── f2py
├── fft
├── lib
├── linalg
├── ma
├── matrixlib
├── polynomial
├── random
├── rec
├── strings
├── testing
├── tests
└── typing
```

Vamos dar uma olhada no arquivo `__init__.py`:




```py title="./numpy/__init__.py" linenums="1"
--8<-- "./codigo/aula_04/numpy/__init__.py"
```

<!--
## Pesquisas sobre a aula

 --8<-- "./Módulo 2/Pesquisas/aula_04.html"--->

