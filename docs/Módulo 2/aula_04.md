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

## Módulos (continuação)

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
['', '/home/aristoteles/.pyenv/versions/3.13.0b2/lib/python313.zip', 
'/home/aristoteles/.pyenv/versions/3.13.0b2/lib/python3.13', 
'/home/aristoteles/.pyenv/versions/3.13.0b2/lib/python3.13/lib-dynload', 
'/home/aristoteles/.pyenv/versions/3.13.0b2/lib/python3.13/site-packages']
```

Como se trata de uma lista podemos modificá-la com as operações típicas de lista, por exemplo:


```py title="Terminal interativo"
>>> import sys
>>> sys.path.append('../guido/lib/python')
```

### Função `dir()`

Relembrando da função `dir()` que vimos em [Aula 03 - Funções do Módulo 1](../../Módulo 1/aula_03/#ainda-sobre-funcoes-embutidas).

Vamos considerar novamente o módulo `ordenacao.py`:

```py title="ordenacao.py" linenums="1"
--8<-- "./codigo/aula_04/ordenacao.py"
```

```py title="Terminal interativo" 
>>> import ordenacao, sys
>>> dir(ordenacao)
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', 
'__name__', '__package__', '__spec__', 'ordenacao_flutuacao', 
'ordenacao_insercao']
>>> dir(sys)
['__breakpointhook__', '__displayhook__', '__doc__', '__excepthook__', 
'__interactivehook__', '__loader__', '__name__', '__package__', '__spec__', 
'__stderr__', '__stdin__', '__stdout__', '__unraisablehook__',
'_base_executable', '_baserepl', '_clear_internal_caches', 
'_clear_type_cache', '_current_exceptions', '_current_frames', 
'_debugmallocstats', '_framework', '_get_cpu_count_config', 
'_getframe', '_getframemodulename', '_git', '_home', '_is_gil_enabled', 
'_is_interned', '_setprofileallthreads', '_settraceallthreads', 
'_stdlib_dir', '_xoptions', 'abiflags', 'activate_stack_trampoline', 
'addaudithook', 'api_version', 'argv', 'audit', 'base_exec_prefix', 
'base_prefix', 'breakpointhook', 'builtin_module_names', 'byteorder', 
'call_tracing', 'copyright', 'deactivate_stack_trampoline', 'displayhook', 
'dont_write_bytecode', 'exc_info', 'excepthook', 'exception', 'exec_prefix', 
'executable', 'exit', 'flags', 'float_info', 'float_repr_style', 
'get_asyncgen_hooks', 'get_coroutine_origin_tracking_depth', 
'get_int_max_str_digits', 'getallocatedblocks', 'getdefaultencoding', 
'getdlopenflags', 'getfilesystemencodeerrors', 'getfilesystemencoding', 
'getprofile', 'getrecursionlimit', 'getrefcount', 'getsizeof', 
'getswitchinterval', 'gettrace', 'getunicodeinternedsize', 'hash_info', 
'hexversion', 'implementation', 'int_info', 'intern', 'is_finalizing', 
'is_stack_trampoline_active', 'maxsize', 'maxunicode', 'meta_path', 
'modules', 'monitoring', 'orig_argv', 'path', 'path_hooks', 
'path_importer_cache', 'platform', 'platlibdir', 'prefix', 'ps1', 'ps2', 
'pycache_prefix', 'set_asyncgen_hooks', 
'set_coroutine_origin_tracking_depth', 'set_int_max_str_digits', 
'setdlopenflags', 'setprofile', 'setrecursionlimit', 'setswitchinterval', 
'settrace', 'stderr', 'stdin', 'stdlib_module_names', 'stdout', 
'thread_info', 'unraisablehook', 'version', 'version_info', 'warnoptions']
```

Sem argumentos, `dir()` lista os nomes atualmente definidos:


```py title="Terminal interativo" 
>>> import ordenacao
>>> arranjo = [12, 8, 5, 3, 2]
>>> insert_sort = ordenacao.ordenacao_insercao
>>> insert_sort(arranjo)
>>> dir()
['CAN_USE_PYREPL', '__annotations__', '__builtins__', '__cached__', 
'__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 
'arranjo', 'insert_sort', 'interactive_console', 'ordenacao', 'os', 'sys']
```

Temos como retorno os nomes: `arranjo`, `ordenacao` e `insert_sort`.

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

## Pacotes
Um pacote é uma coleção de módulos.

Os pacotes servem para estruturar o "espaço de nomes" dos módulos Python,  usando "nomes de módulos com pontos".

Por exemplo, o nome do módulo `A.B`, designa um submódulo chamado `B`, em um pacote chamado `A`.
Isso facilita a organização entre módulos, evitando a preocupação com nomes de variáveis globais.

### Alguns uso de pacotes

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

Na importação, Python busca pelo subdiretório com o mesmo nome, nos diretórios listados em `sys.path`

Os aquivos `__init__` são necessários para que o Python trate diretórios contendo o arquivo como pacotes.
No caso mais simples `__init__` pode ser um arquivo vazio, tendo a potencialidade de executar um código de inicialização do pacote, ou configurar variáveis.

Podemos importar módulos individuais:


```py title="./arquivo_qualquer.py"
import audio.efeitos.eco
```

Isso carrega o submódulo audio.efeitos.eco

Lembrando para utilizarmos dessa maneira, deve-se referenciar o nome completo, como em:

```py title="./arquivo_qualquer.py"
audio.efeitos.eco.eco_filtro(entrada, saida, delay=0.7, atten=4)
```

Podemos também importar uma única variável ou função:

```py title="./arquivo_qualquer.py"
from audio.efeitos.eco import eco_filtro
```

Agora a função `eco_filtro` está acessível diretamente sem prefixo:

```py title="./arquivo_qualquer.py"
eco_filtro(entrada, saida, delay=0.7, atten=4)
```



!!! note "Observe:"

    - Ao utilizar a notação `from pacote import item`, o `item` pode ser um subpacote, submódulo, classe, função ou variável.

    - Em oposição, a notação `import item.subtitem.subsubitem`, cada item, com exceção do último, deve ser um pacote.
O último pode ser também um pacote ou módulo, mas nunca uma classe, função ou variável contida em um módulo.

### Referência em um mesmo pacote

Quando estruturamos pacotes compostos por subpacotes (como o pacote `audio` do nosso exemplo), pode-se usar a sintaxe de importações **absolutas** ou **relativas** para se referir aos submódulos **irmãos**.

Por exemplo, se o módulo `audio.filtros.codificador_voz` precisar usar o módulo `eco` do subpacote `audio.efeitos`.

Modo absoluto:

```py title="./audio/filtros/codificador_voz.py"
from audio.efeitos import eco
```

No módulo absoluto o caminho parte da pasta principal (pacote `audio`). Por isso é absoluto, pois a referência é absoluta em qualquer módulo, de qualquer subpacote.

Modo relativos:

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

### Importando o `*`

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

A critério de exemplo real:

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


## Pesquisas sobre a aula

--8<-- "./Módulo 2/Pesquisas/aula_04.html"

