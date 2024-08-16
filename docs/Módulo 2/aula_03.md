
# Aula 03 - Análise de algoritmos e suas complexidades (continuação) e Módulos em Python

{% set aula = "03" %}
{% set link = "WfPIxKBEjPI" %}
{% set objetivos = [
"Ordenação por flutuação entendimento do algoritmo e sua análise", 
"Introdução à ideia de módulo"] %}


{% include "templates/cabecalho.md" %}

---

## Ordenação por flutuação - BubbleSort

![](https://upload.wikimedia.org/wikipedia/commons/3/37/Bubble_sort_animation.gif){: .center .shadow}

A ordenação por flutuação, permuta repetidamente elementos adjacentes que estão fora de ordem, ou seja, o conjunto (ou arranjo) é percorrido diversas vezes, e a cada passagem faz "flutuar" para o "topo" o maior elemento.

Essa permutação lembra a forma como as bolhas de ar em um tanque com água, por serem menos densas sobem para o próprio nível. E disso advém o nome do algoritmo.


### Pseudo-código

```py title="pseudocodigo_ordenacao_insercao" linenums="1"
def ordenacao_flutuacao(A):
    Para i = 0 até A.comprimento, faça:
        Para j = 0 até A.comprimento -i - 1
            Se A[j] > A[j + 1]
                valor_temporario = A[j]
                A[j] = A[j + 1]
                A[j + 1] = valor_temporario
```

### Tabela de custos

Faça uma tabela de custos e quantidade de vezes uma linha é executada.


|linha|def ordenacao_flutuacao(A):|custo|vezes|
|-----|---------------------------|-----|-----|
|1    |&emsp;Para i = 0 até A.comprimento, faça:|$c_1$|n|
|2    |&emsp;&emsp; Para j = 0 até A.comprimento -i -1|$c_2$|$\sum_{i=1}^{n} t_i$|
|3    |&emsp;&emsp;&emsp; Se A[j] > A[j + 1]|$c_3$|$\sum_{i=1}^{n} t_i$|
|4    |&emsp;&emsp;&emsp;&emsp; valor_temporario = A[j]|$c_4$|$\sum_{i=1}^{n} (t_i - 1)$|
|5    |&emsp;&emsp;&emsp;&emsp;A[j] = A[j + 1]|$c_5$|$\sum_{i=1}^{n} (t_i - 1)$|
|6    |&emsp;&emsp;&emsp;&emsp; A[j + 1] = valor_temporario|$c_6$|$\sum_{i=1}^{n} (t_i - 1)$|


### Pior caso


Estudo do $T(n)$ para o pior caso.

Definição $\Theta(n^2)$


Para o pior caso, ou seja, um arranjo de $n$ elementos, ordenado de maneira decrescente. Temos que, nossas linhas $2$ e $3$ será executada $n, n - 1, n-2,\cdots  1$ vezes. Logo, para cada $i$, $A[j]$ sempre será **maior** que $A[j + 1] e será executado $n - i -1$. Teremos então para as linhas $4$, $5$ e $6$: $n - 1, n - 2, n - 3, \cdots, 1$ ou $0, 1, 2, 3, 4, i - 1$ vezes.

Logo, $t_i = i$. E $t_i - 1 = i - 1$, temos:

$$T(n) = c_1n + c_2\sum_{i=1}^{n} + c_3\sum_{i=1}^{n} i + c_4\sum_{i=1}^{n} (i - 1)+ c_5\sum_{i=1}^{n} (i - 1) + c_6\sum_{i=1}^{n} (i - 1)$$

$$T(n) = c_1n + (c_2+ c_3)\sum_{i=1}^{n} i + (c_4 + c_5 + c_6)\sum_{i=1}^{n} (i - 1)$$


$$T(n) = c_1n + (c_2 + c_3)\dfrac{1}{2}n(n + 1) + (c_4 + c_5 + c_6)\dfrac{1}{2}(n - 1)n$$

$$T(n) = c_1n + \dfrac{c_2 + c_3}{2}n^2 + \dfrac{c_2 + c_3}{2}n + \dfrac{c_4 + c_5 + c_6}{2}n^2 - \dfrac{c_4 + c_5 + c_6}{2}n$$

$$T(n) = \dfrac{c_2 + c_3 + c_4 + c_5 + c_6}{2}n^2 + \biggl[c_1 + \dfrac{c_2 + c_3 - c_4 - c_5 - c_6}{2}\biggl]n $$

$$T(n) = c_7n^2 + c_8n$$

$$\Theta(n^2)$$

Ainda não foi dessa vez, que nosso $\Theta < \Theta(n^2)$


## Módulos

![](https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExYW43Y3lnOWFpNG44bHhhdzhxZzRmb2lqMmp3bndieXN0ODhoOXp0ZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/xUA7aVbrKntotcCzVS/giphy.webp){: .center .shadow}

Já vimos, desde [Aula 04 - Manipulação de scripts em Python no Módulo 1](./Módulo 1/aula_04.md#idle-slide-da-primeira-aula){:target="_blank"} como executar um programa maior e executá-lo usando o arquivo como entrada, ou seja, criação e manipulação de scripts em Python.

Uma boa prática para programas muito grandes é dividi-lo em arquivos menores, afim de facilitar a manutenção.

Também é preferível usar um arquivo separado para uma função que você escreveria em vários programas diferentes. 

> Lembre-se repetição de código não é uma boa prática

## Criando módulos

Para isso, basta colocar as definições em um arquivo e então usá-las em um script ou em uma execução do interpretador.

Esse arquivo, chama-se módulo. Um módulo, portanto, é um arquivo contendo definições e instruções Python.

Vamos criar um módulo que contenha os dois algoritmos de ordenação que vimos até agora.

```py title="ordenacao.py" linenums="1"
def ordenacao_insercao(lista):
    for indice_chave in range(1, len(lista)):
        chave = lista[indice_chave]
        indice_anterior = indice_chave - 1
        while indice_anterior >= 0 and lista[indice_anterior] > chave:
            indice_posterior = indice_anterior + 1
            lista[indice_posterior] = lista[indice_anterior]
            indice_anterior = indice_anterior - 1 
        lista[indice_anterior + 1] = chave 

def ordenacao_flutuacao(arranjo):
    for i in range(len(arranjo)):
        for j in range(len(arranjo) - i - 1):
            if arranjo[j] > arranjo[j + 1]:
                arranjo[j], arranjo[j + 1] = arranjo[j + 1], arranjo[j]

```

Vamos agora criar um arquivo que utilizará do nosso módulo recém criado.

Para isso utilizamos `import` para "importar" o módulo.  


```py title="aula_03_modulos.py" linenums="1"
import ordenacao

```

Nossa estrutura de arquivos e pastas está assim:

```
.
├── aula_03_modulos.py
└── ordenacao.py
```

Até agora só adicionamos o nome do módulo `ordenacao`.

Usando o nome do módulo importado, podemos acessar as funções.

```py title="aula_03_modulos.py" linenums="1" hl_lines="7 13"
import ordenacao

arranjo = [6, 5, 4, 2]
print(arranjo)


ordenacao.ordenacao_insercao(arranjo)
print("Por inserção: ", arranjo)

arranjo = [6, 5, 4, 2]
print(arranjo)

ordenacao.ordenacao_flutuacao(arranjo)
```

```shell title="Resposta do comando `python aula_03_modulos.py`" hl_lines="2 4"
[6, 5, 4, 2]
Por inserção:  [2, 4, 5, 6]
[6, 5, 4, 2]
Por flutuação:  [2, 4, 5, 6]
```

É claro que, se pretendemos usar muitas vezes uma função importada, podemos atribui-lá a um nome local:


```py title="aula_03_modulos.py" linenums="1" hl_lines="7 8 17"
import ordenacao

arranjo = [6, 5, 4, 2]
print(arranjo)


insercao = ordenacao.ordenacao_insercao
insercao(arranjo)
print("Por inserção: ", arranjo)

arranjo = [6, 5, 4, 2]
print(arranjo)

ordenacao.ordenacao_flutuacao(arranjo)

arranjo2 = [45, 34, 4, 2, 1]
insercao(arranjo2)
print("Por inserção: ", arranjo2)

```

## Ainda sobre módulos

Um módulo pode conter tanto instruções executáveis quanto definições de funções e classes (veremos posteriormente).

Essa instruções e definições só são executadas somente na **primeira vez** que o módulo é encontrado em uma instrução de importação (`import`, que vimos até agora).

Módulos podem importar outros módulos.

Costuma-se colocar todas as instruções `import` no início do módulo (ou script, se preferir).

As definições do módulo importado, se colocados no nível de um módulo (fora de quaisquer funções ou classes), serão adicionadas a espaço de nomes globais do módulo.

### Variantes do `import`

Existe uma variante da instrução `import`, que importa definições de um módulo diretamente para o espaço de nomes do módulo importador. Por exemplo:


```py title="aula_03_ex2.py" linenums="1" hl_lines="1 7 13"
from ordenacao import ordenacao_flutuacao, ordenacao_insercao

arranjo = [6, 5, 4, 2]
print(arranjo)


ordenacao_insercao(arranjo)
print("Por inserção: ", arranjo)

arranjo = [6, 5, 4, 2]
print(arranjo)

ordenacao_flutuacao(arranjo)
print("Por flutuação: ", arranjo)
```

Dessa maneira, o nome do módulo de onde foram feitas as importações não é colocado no espaço de nomes locais (`ordenacao` não está definido).

Se o nome do módulo é seguindo pela palavra-chave `as`, o nome a seguir é vinculado diretamente ao módulo importado.

```py title=">>> Terminal interativo!" hl_lines="1"
	>>> import ordenacao as algoritmos
    >>> arranjo = [6, 5, 4, 2]
	>>> algoritmos.ordenacao_insercao(arranjo)
	>>> arranjo
	[2, 4, 5, 6]
```

Isto importa o módulo, da mesma maneira que `import ordenacao` fará, com a diferença de estar disponível com o nome `algoritmos`.

Também podemos usar `as` com a palavra-chave `from`, e obeter efeitos similares:

```py title=">>> Terminal interativo!" hl_lines="1"
    >>> from ordenacao import ordenacao_insercao as insercao
    >>> arranjo = [6, 5, 4, 2]
    >>> insercao(arranjo)
    >>> arranjo
    [2, 4, 5, 6]
```


!!! danger "Atenção"
    Por eficiência, cada módulo é importado apenas uma vez por sessão do intérprete. Portanto, se você alterar seus módulos, deverá reiniciar o interpretador, ou se for apenas um módulo que deseja testar, use importlib.reload(). Por exemplo:

    ```py title=">>> Terminal interativo!" 
        >>> import importlib
        >>> importlib.reload(`nome do módulo`)
    ```

Continuamos na Aula 04
