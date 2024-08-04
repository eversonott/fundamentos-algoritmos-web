# Aula 02 - Introdução ao conceito de complexidade de algoritmos

## Ordenação por inserção - Passo a passo



Para o exemplo iremos utilizar o arranjo: `A = < 5, 2, 4, 6 >`


```py title="pseudocodigo_ordenacao_insercao" linenums="1"
def ordenacao_insercao(A):
    Para i = 1 até A.comprimento, faça:
        chave = A[i]
        // Inserir A[i] na sequência ordenada A[0, ..., i -1]
        j = i - 1
        Enquanto j > -1 e A[j] > chave, faça:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = chave
```

Vamos considerar o arranjo:

|arranjo:|5|2|4|6|
|-|-|-|-|-|
|**índice:**|**0**|**1**|**2**|**3**|

### 1ª Iteração


#### 1⁰ passo: A comparação do menor elemento é sempre binária

|arranjo:|5|2|4|6|
|-|-|-|-|-|
|**índice:**|**0**|**1**|**2**|**3**|

```py title="pseudocodigo_ordenacao_insercao" linenums="1"  hl_lines="2"
def ordenacao_insercao(A):
    Para i = 1 até A.comprimento, faça:
        chave = A[i]
        // Inserir A[i] na sequência ordenada A[0, ..., i -1]
        j = i - 1
        Enquanto j > -1 e A[j] > chave, faça:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = chave
```


|arranjo:|5|2|4|6|
|-|-|-|-|-|
|**índice:**|**0**|**1**|**2**|**3**|
|i|-|1|-|-|

Começamos a partir do segundo elemento, para o ordenar o primeiro.
Uma vez que o comparativo necessita de dois elementos.
> Lembre-se: Uma sequência de apenas um número, já está ordenada.

#### 2⁰ passo: Determina a chave e o índice do seu termo anterior


```py title="pseudocodigo_ordenacao_insercao" linenums="1"  hl_lines="3 5"
def ordenacao_insercao(A):
    Para i = 1 até A.comprimento, faça:
        chave = A[i]
        // Inserir A[i] na sequência ordenada A[0, ..., i -1]
        j = i - 1
        Enquanto j > -1 e A[j] > chave, faça:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = chave
```


|arranjo:|5|2|4|6|
|-|-|-|-|-|
|**índice:**|**0**|**1**|**2**|**3**|
|i|-|1|-|-|-|
|chave:|-|2|-|
|j:|0|-|-|-|

A variável `chave` armazena o valor que queremos ordenar.

A variável `j` armazena o índice do termo anterior a chave.

#### 3⁰ passo: Se o termo anterior for menor que a chave, faz a troca

```py title="pseudocodigo_ordenacao_insercao" linenums="1"  hl_lines="6"
def ordenacao_insercao(A):
    Para i = 1 até A.comprimento, faça:
        chave = A[i]
        // Inserir A[i] na sequência ordenada A[0, ..., i -1]
        j = i - 1
        Enquanto j > -1 e A[j] > chave, faça:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = chave
```


|arranjo:|5|2|4|6|
|-|-|-|-|-|
|**índice:**|**0**|**1**|**2**|**3**|
|i|-|1|-|-|
|chave:|-|2|-|-|
|j:|0|-|-|-|
|**Enquanto**  <td colspan="4">índice do termo anterior estiver dentro do arranjo e o termo anterior for maior que a chave</td></tr>

##### 3.1⁰ passo: Como fazer a troca

```py title="pseudocodigo_ordenacao_insercao" linenums="1"  hl_lines="7 8"
def ordenacao_insercao(A):
    Para i = 1 até A.comprimento, faça:
        chave = A[i]
        // Inserir A[i] na sequência ordenada A[0, ..., i -1]
        j = i - 1
        Enquanto j > -1 e A[j] > chave, faça:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = chave
```

|arranjo:|5|5|4|6|
|-|-|-|-|-|
|**índice:**|**0**|**1**|**2**|**3**|
|i|-|1|-|-|
|chave:|-|2|-|-|
|**Enquanto**  <td colspan="4">índice do termo anterior estiver dentro do arranjo e o termo anterior for maior que a chave</td></tr>
|j:|-1|-|-|-|

Utilizando o índice do termo anterior, desloca o termo anterior uma casa a frente, ou seja, coloca o valor maior a direita.


#### 4⁰ passo: Transfere a chave para a posição mais à esquerda.

```py title="pseudocodigo_ordenacao_insercao" linenums="1"  hl_lines="9"
def ordenacao_insercao(A):
    Para i = 1 até A.comprimento, faça:
        chave = A[i]
        // Inserir A[i] na sequência ordenada A[0, ..., i -1]
        j = i - 1
        Enquanto j > -1 e A[j] > chave, faça:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = chave
```


|arranjo:|2|5|4|6|
|-|-|-|-|-|
|**índice:**|**0**|**1**|**2**|**3**|
|i|-|1|-|-|
|chave:|-|2|-|-|
|**Enquanto**  <td colspan="4">índice do termo anterior estiver dentro do arranjo e o termo anterior for maior que a chave</td></tr>
|j:|-1|-|-|-|


Usando o índice do termo anterior, que está decrementado uma unidade, transfere o valor chave para a posição mais a esquerda.


### 2ª Iteração


#### 1⁰ passo e 2⁰ passo

```py title="pseudocodigo_ordenacao_insercao" linenums="1"  hl_lines="2-3 5"
def ordenacao_insercao(A):
    Para i = 1 até A.comprimento, faça:
        chave = A[i]
        // Inserir A[i] na sequência ordenada A[0, ..., i -1]
        j = i - 1
        Enquanto j > -1 e A[j] > chave, faça:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = chave
```

|arranjo:|2|5|4|6|
|-|-|-|-|-|
|**índice:**|**0**|**1**|**2**|**3**|
|i|-|-|2|-|
|chave:|-|-|4|-|
|j:|-|1|-|-|

#### 3⁰ passo

```py title="pseudocodigo_ordenacao_insercao" linenums="1"  hl_lines="6-8"
def ordenacao_insercao(A):
    Para i = 1 até A.comprimento, faça:
        chave = A[i]
        // Inserir A[i] na sequência ordenada A[0, ..., i -1]
        j = i - 1
        Enquanto j > -1 e A[j] > chave, faça:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = chave
```


|arranjo:|2|5|5|6|
|-|-|-|-|-|
|**índice:**|**0**|**1**|**2**|**3**|
|i|-|-|2|-|
|chave:|-|-|4|-|
|**Enquanto**  <td colspan="4">índice do termo anterior estiver dentro do arranjo e o termo anterior for maior que a chave</td></tr>
|j:|0|-|-|-|


Dessa vez a condição que quebra o laço `A[j] > chave`, onde `2 > 4 = False`


#### 4⁰ passo

```py title="pseudocodigo_ordenacao_insercao" linenums="1"  hl_lines="9"
def ordenacao_insercao(A):
    Para i = 1 até A.comprimento, faça:
        chave = A[i]
        // Inserir A[i] na sequência ordenada A[0, ..., i -1]
        j = i - 1
        Enquanto j > -1 e A[j] > chave, faça:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = chave
```

|arranjo:|2|4|5|6|
|-|-|-|-|-|
|**índice:**|**0**|**1**|**2**|**3**|
|i|-|-|2|-|
|chave:|-|-|4|-|
|**Enquanto**  <td colspan="4">índice do termo anterior estiver dentro do arranjo e o termo anterior for maior que a chave</td></tr>
|j:|0|-|-|-|


### 3ª Iteração

#### 1⁰ passo e 2⁰ passo

```py title="pseudocodigo_ordenacao_insercao" linenums="1"  hl_lines="2-3 5"
def ordenacao_insercao(A):
    Para i = 1 até A.comprimento, faça:
        chave = A[i]
        // Inserir A[i] na sequência ordenada A[0, ..., i -1]
        j = i - 1
        Enquanto j > -1 e A[j] > chave, faça:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = chave
```

|arranjo:|2|4|5|6|
|-|-|-|-|-|
|**índice:**|**0**|**1**|**2**|**3**|
|i|-|-|-|3|
|chave:|-|-|-|6|
|j:|-|-|2|-|

#### 3⁰ passo

```py title="pseudocodigo_ordenacao_insercao" linenums="1"  hl_lines="6-8"
def ordenacao_insercao(A):
    Para i = 1 até A.comprimento, faça:
        chave = A[i]
        // Inserir A[i] na sequência ordenada A[0, ..., i -1]
        j = i - 1
        Enquanto j > -1 e A[j] > chave, faça:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = chave
```

|arranjo:|2|4|5|6|
|-|-|-|-|-|
|**índice:**|**0**|**1**|**2**|**3**|
|i|-|-|-|3|
|chave:|-|-|-|6|
|j:|-|-|2|-|

Não entramos no laço devido a condição `A[j] > chave`, onde `5 > 6 = False`

As linhas **7** e **8** não são executadas, e saltamos para a linha **9**.

#### 4⁰ passo

```py title="pseudocodigo_ordenacao_insercao" linenums="1"  hl_lines="9"
def ordenacao_insercao(A):
    Para i = 1 até A.comprimento, faça:
        chave = A[i]
        // Inserir A[i] na sequência ordenada A[0, ..., i -1]
        j = i - 1
        Enquanto j > -1 e A[j] > chave, faça:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = chave
```

|arranjo:|2|4|5|6|
|-|-|-|-|-|
|**índice:**|**0**|**1**|**2**|**3**|
|i|-|-|-|3|
|chave:|-|-|-|6|
|j:|-|-|2|-|

A linha **9** atribui na posição onde está a chave, a própria chave.

O arranjo final é permutado em sequência crescente.

## Análise da ordenação por inserção

O tempo necessário pelo procedimento `ordenacao_insercao` depende da entrada:

- Ordenar mil números demora mais que ordenar três números.

Além disso, a ordenação por inserção pode demorar tempo diferentes para ordenar duas sequências de entrada do mesmo tamanho, dependendo do quanto elas já estejam ordenadas.

Em termos gerais, o tempo gasto por um algoritmo cresce com o tamanho da entrada.

Portanto, é tradicional descrever o tempo de execução de um programa em função do tamanho de sua entrada.

### O tempo de execução

O tempo de execução de um algoritmo em determinada entrada é o número de operações primitivas ou "passos" executados.

Vamos adotar que uma quantidade de tempo constante é exigida para executar cada linha do nosso pseudo código.

Uma linha pode demorar uma quantidade de tempo diferente de outra linha, mas consideremos que cada execução de i-ésima linha leva um tempo `ci`, onde `ci` é uma constante.

Partiremos de uma fórmula confusa que utiliza todos os custos de instrução `ci` até uma notação muito mais simples, que também é mais concisa e mais fácil de manipular.

E será por meio dessa notação mais simples também que facilitará a tarefa de determinar se um algoritmo é mais eficiente que outro.

### Ordenação por inserção com custo


|linha|def ordenacao_insercao(A):|custo|vezes|
|-|-|-|-|
    |1|&emsp;Para i = 1 até A.comprimento, faça:|$c_1$|n|
        |2|&emsp;&emsp; chave = A[i]|$c_2$|n - 1|
        |3|// Inserir A[i] na sequência ordenada A[0, ..., i -1]|0|n - 1|
        |4|&emsp;&emsp;j = i - 1|$c_4$|n - 1|
        |5|&emsp;Enquanto j > -1 e A[j] > chave, faça:|$c_5$|$\sum_{i=1}^{n} t_i$|
            |6|&emsp;&emsp;&emsp;A[j + 1] = A[j]|$c_6$|$\sum_{i=1}^{n} (t_i - 1)$|
            |7|&emsp;&emsp;&emsp;j = j - 1|$c_7$|$\sum_{i=1}^{n} (t_i - 1)$|
        |8|&emsp;A[j + 1] = chave|$c_8$|n - 1|

O tempo de execução do algoritmo é a soma dos tempos de execução para cada instrução executada.

Para calcular o $T(n)$, o tempo de execução da ordenação por inserção de uma entrada de $n$ valores, somamos os produtos das colunas `custo` e `vezes`, obtendo:


$$\begin{equation}
\begin{split}
T(n) &= c_1n + c_2(n - 1) + c_4(n-1) + c_5\sum_{i=1}^{n} t_i + c_6\sum_{i=1}^{n} (t_i - 1)\\
 &\quad + c_7\sum_{i=1}^{n} (t_i - 1) + c_8(n - 1) \\
\end{split}
\end{equation}$$


### Série infinita (ou apenas série)

Em geral, se tentarmos somar os termos de uma sequência infinita ${a_n}^{\infty}_{n=1}$, obtemos:

$$a_1 + a_2 + a_3 + \cdots + a_n + \cdots$$

que é denominada uma série infinita, por simplicidade, pelo símbolo:

$$\sum_{n=1}^{\infty} a_n \text{ ou } \sum a_n$$

#### Sequência limitada

Uma sequência ${a_n}^{\infty}_{n=1}$ é **limitada superiormente** se existir um número M tal que:

$$a_n \leqslant M\text{, para todo }n \geqslant 1$$

Uma sequência ${a_n}^{\infty}_{n=1}$ é **limitada inferiormente** se existir um número m tal que:

$$m \leqslant a_n\text{, para todo }n \geqslant 1$$

Dizemos que uma sequência ${a_n}^{\infty}_{n=1}$ é **limitada** se for limitada superiormente e inferiormente.

### Analisando o pior caso



Se o arranjo estiver ordenado em ordem decrescente, resulta o pior caso de ordenação.

#### 1⁰ Iteração (i = 1)

##### j = 0

Nosso arranjo no pior caso é: <6, 5, 4, 2>

```py title="pseudocodigo_ordenacao_insercao" linenums="1"  hl_lines="2-3 5"
def ordenacao_insercao(A):
    Para i = 1 até A.comprimento, faça:
        chave = A[i]
        // Inserir A[i] na sequência ordenada A[0, ..., i -1]
        j = i - 1
        Enquanto j > -1 e A[j] > chave, faça:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = chave
```

|arranjo:|-|6|5|4|2|
|-|-|-|-|-|-|
|**índice:**|-|**0**|**1**|**2**|**3**|
|i|-|-|1|-|-|
|chave:|-|-|5|-|-|
|j:|-|0|-|-|-|

```py title="pseudocodigo_ordenacao_insercao" linenums="1"  hl_lines="6"
def ordenacao_insercao(A):
    Para i = 1 até A.comprimento, faça:
        chave = A[i]
        // Inserir A[i] na sequência ordenada A[0, ..., i -1]
        j = i - 1
        Enquanto j > -1 e A[j] > chave, faça:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = chave
```


|arranjo:|-|6|5|4|2|
|-|-|-|-|-|-|
|**índice:**|-|**0**|**1**|**2**|**3**|
|i|-|-|1|-|-|
|chave:|-|-|5|-|-|
|j:|-|0|-|-|-|
|**Enquanto**|-|0 > -1 = **True** e 6 > 5 = **True**|-|-|-|


##### j = -1

```py title="pseudocodigo_ordenacao_insercao" linenums="1"  hl_lines="7-8"
def ordenacao_insercao(A):
    Para i = 1 até A.comprimento, faça:
        chave = A[i]
        // Inserir A[i] na sequência ordenada A[0, ..., i -1]
        j = i - 1
        Enquanto j > -1 e A[j] > chave, faça:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = chave
```

|arranjo:|- |6|6|4|2|
|-|-|-|-|-|-|
|**índice:** |**-1**|**0**|**1**|**2**|**3**|
|i|-|-|1|-|-|
|chave:|-|-|5|-|-|
|**Enquanto**|-|0 > -1 = **True** e 6 > 5 = **True**|-|-|-|
|j:|-1|-|-|-|-|

```py title="pseudocodigo_ordenacao_insercao" linenums="1"  hl_lines="6"
def ordenacao_insercao(A):
    Para i = 1 até A.comprimento, faça:
        chave = A[i]
        // Inserir A[i] na sequência ordenada A[0, ..., i -1]
        j = i - 1
        Enquanto j > -1 e A[j] > chave, faça:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = chave
```

|arranjo:|- |6|6|4|2|
|-|-|-|-|-|-|
|**índice:** |**-1**|**0**|**1**|**2**|**3**|
|i|-|-|1|-|-|
|chave:|-|-|5|-|-|
|j:|-1|-|-|-|-|
|**Enquanto**|-1 > -1 = **False**|-|-|-|-|

```py title="pseudocodigo_ordenacao_insercao" linenums="1"  hl_lines="9"
def ordenacao_insercao(A):
    Para i = 1 até A.comprimento, faça:
        chave = A[i]
        // Inserir A[i] na sequência ordenada A[0, ..., i -1]
        j = i - 1
        Enquanto j > -1 e A[j] > chave, faça:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = chave
```

|arranjo:|-|5|6|4|2|
|-|-|-|-|-|-|
|**índice:** |**-1**|**0**|**1**|**2**|**3**|
|i|-|-|1|-|-|
|chave:|-|-|5|-|-|
|j:|-1|-|-|-|-|
|**Enquanto**|-1 > -1 = **False**|-|-|-|-|

#### 2⁰ Iteração (i = 2)

##### j = 1

```py title="pseudocodigo_ordenacao_insercao" linenums="1"  hl_lines="2-3 5"
def ordenacao_insercao(A):
    Para i = 1 até A.comprimento, faça:
        chave = A[i]
        // Inserir A[i] na sequência ordenada A[0, ..., i -1]
        j = i - 1
        Enquanto j > -1 e A[j] > chave, faça:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = chave
```

|arranjo:|-|5|6|4|2|
|-|-|-|-|-|-|
|**índice:** |**-1**|**0**|**1**|**2**|**3**|
|i|-|-|-|2|-|
|chave:|-|-|-|4|-|
|j:|-|-|1|-|-|

```py title="pseudocodigo_ordenacao_insercao" linenums="1"  hl_lines="6"
def ordenacao_insercao(A):
    Para i = 1 até A.comprimento, faça:
        chave = A[i]
        // Inserir A[i] na sequência ordenada A[0, ..., i -1]
        j = i - 1
        Enquanto j > -1 e A[j] > chave, faça:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = chave
```

|arranjo:|-|5|6|4|2|
|-|-|-|-|-|-|
|**índice:** |**-1**|**0**|**1**|**2**|**3**|
|i|-|-|-|2|-|
|chave:|-|-|-|4|-|
|j:|-|-|1|-|-|
|**Enquanto**|-|-|1 > -1 = **True** e 6 > 4 = **True**|-|-|

##### j = 0


```py title="pseudocodigo_ordenacao_insercao" linenums="1"  hl_lines="7-8"
def ordenacao_insercao(A):
    Para i = 1 até A.comprimento, faça:
        chave = A[i]
        // Inserir A[i] na sequência ordenada A[0, ..., i -1]
        j = i - 1
        Enquanto j > -1 e A[j] > chave, faça:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = chave
```

|arranjo:|-|5|6|6|2|
|-|-|-|-|-|-|
|**índice:** |**-1**|**0**|**1**|**2**|**3**|
|i|-|-|-|2|-|
|chave:|-|-|-|4|-|
|**Enquanto**|-|-|1 > -1 = **True** e 6 > 4 = **True**|-|-|
|j:|-|0|-|-|-|

```py title="pseudocodigo_ordenacao_insercao" linenums="1"  hl_lines="6"
def ordenacao_insercao(A):
    Para i = 1 até A.comprimento, faça:
        chave = A[i]
        // Inserir A[i] na sequência ordenada A[0, ..., i -1]
        j = i - 1
        Enquanto j > -1 e A[j] > chave, faça:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = chave
```

|arranjo:|-|5|6|6|2|
|-|-|-|-|-|-|
|**índice:** |**-1**|**0**|**1**|**2**|**3**|
|i|-|-|-|2|-|
|chave:|-|-|-|4|-|
|j:|-|0|-|-|-|
|**Enquanto**|-|0 > -1 = **True** e 5 > 4 = **True**|-|-|-|


##### j = -1

```py title="pseudocodigo_ordenacao_insercao" linenums="1"  hl_lines="7-8"
def ordenacao_insercao(A):
    Para i = 1 até A.comprimento, faça:
        chave = A[i]
        // Inserir A[i] na sequência ordenada A[0, ..., i -1]
        j = i - 1
        Enquanto j > -1 e A[j] > chave, faça:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = chave
```

|arranjo:|-|5|5|6|2|
|-|-|-|-|-|-|
|**índice:** |**-1**|**0**|**1**|**2**|**3**|
|i|-|-|-|2|-|
|chave:|-|-|-|4|-|
|**Enquanto**|-|0 > -1 = **True** e 5 > 4 = **True**|-|-|-|
|j:|-1|-|-|-|-|

```py title="pseudocodigo_ordenacao_insercao" linenums="1"  hl_lines="6"
def ordenacao_insercao(A):
    Para i = 1 até A.comprimento, faça:
        chave = A[i]
        // Inserir A[i] na sequência ordenada A[0, ..., i -1]
        j = i - 1
        Enquanto j > -1 e A[j] > chave, faça:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = chave
```

|arranjo:|-|5|5|6|2|
|-|-|-|-|-|-|
|**índice:** |**-1**|**0**|**1**|**2**|**3**|
|i|-|-|-|2|-|
|chave:|-|-|-|4|-|
|j:|-1|-|-|-|-|
|**Enquanto**|-1 > -1 = **False**|-|-|-|-|

```py title="pseudocodigo_ordenacao_insercao" linenums="1"  hl_lines="9"
def ordenacao_insercao(A):
    Para i = 1 até A.comprimento, faça:
        chave = A[i]
        // Inserir A[i] na sequência ordenada A[0, ..., i -1]
        j = i - 1
        Enquanto j > -1 e A[j] > chave, faça:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = chave
```

|arranjo:|-|4|5|6|2|
|-|-|-|-|-|-|
|**índice:** |**-1**|**0**|**1**|**2**|**3**|
|i|-|-|-|2|-|
|chave:|-|-|-|4|-|
|j:|-1|-|-|-|-|
|**Enquanto**|-1 > -1 = **False**|-|-|-|-|


#### 3⁰ Iteração (i = 3)

##### j = 2

```py title="pseudocodigo_ordenacao_insercao" linenums="1"  hl_lines="2-3 5"
def ordenacao_insercao(A):
    Para i = 1 até A.comprimento, faça:
        chave = A[i]
        // Inserir A[i] na sequência ordenada A[0, ..., i -1]
        j = i - 1
        Enquanto j > -1 e A[j] > chave, faça:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = chave
```

|arranjo:|-|4|5|6|2|
|-|-|-|-|-|-|
|**índice:** |**-1**|**0**|**1**|**2**|**3**|
|i|-|-|-|-|3|
|chave:|-|-|-|-|2|
|j:|-|-|-|2|-|

```py title="pseudocodigo_ordenacao_insercao" linenums="1"  hl_lines="6"
def ordenacao_insercao(A):
    Para i = 1 até A.comprimento, faça:
        chave = A[i]
        // Inserir A[i] na sequência ordenada A[0, ..., i -1]
        j = i - 1
        Enquanto j > -1 e A[j] > chave, faça:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = chave
```

|arranjo:|-|4|5|6|2|
|-|-|-|-|-|-|
|**índice:** |**-1**|**0**|**1**|**2**|**3**|
|i|-|-|-|-|3|
|chave:|-|-|-|-|2|
|j:|-|-|-|2|-|
|**Enquanto**|-|-|-|2 > -1 = **True** e 6 > 2 = **True**|-|


##### j = 1

```py title="pseudocodigo_ordenacao_insercao" linenums="1"  hl_lines="7-8"
def ordenacao_insercao(A):
    Para i = 1 até A.comprimento, faça:
        chave = A[i]
        // Inserir A[i] na sequência ordenada A[0, ..., i -1]
        j = i - 1
        Enquanto j > -1 e A[j] > chave, faça:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = chave
```

|arranjo:|-|4|5|6|6|
|-|-|-|-|-|-|
|**índice:** |**-1**|**0**|**1**|**2**|**3**|
|i|-|-|-|-|3|
|chave:|-|-|-|-|2|
|**Enquanto**|-|-|-|2 > -1 = **True** e 6 > 2 = **True**|-|
|j:|-|-|1|-|-|

```py title="pseudocodigo_ordenacao_insercao" linenums="1"  hl_lines="6"
def ordenacao_insercao(A):
    Para i = 1 até A.comprimento, faça:
        chave = A[i]
        // Inserir A[i] na sequência ordenada A[0, ..., i -1]
        j = i - 1
        Enquanto j > -1 e A[j] > chave, faça:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = chave
```

|arranjo:|-|4|5|6|6|
|-|-|-|-|-|-|
|**índice:** |**-1**|**0**|**1**|**2**|**3**|
|i|-|-|-|-|3|
|chave:|-|-|-|-|2|
|j:|-|-|1|-|-|
|**Enquanto**|-|-|1 > -1 = **True** e 5 > 2 = **True**|-|-|


##### j = 0

```py title="pseudocodigo_ordenacao_insercao" linenums="1"  hl_lines="7-8"
def ordenacao_insercao(A):
    Para i = 1 até A.comprimento, faça:
        chave = A[i]
        // Inserir A[i] na sequência ordenada A[0, ..., i -1]
        j = i - 1
        Enquanto j > -1 e A[j] > chave, faça:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = chave
```

|arranjo:|-|4|5|5|6|
|-|-|-|-|-|-|
|**índice:** |**-1**|**0**|**1**|**2**|**3**|
|i|-|-|-|-|3|
|chave:|-|-|-|-|2|
|**Enquanto**|-|-|1 > -1 = **True** e 5 > 2 = **True**|-|-|
|j:|-|0|-|-|-|

```py title="pseudocodigo_ordenacao_insercao" linenums="1"  hl_lines="6"
def ordenacao_insercao(A):
    Para i = 1 até A.comprimento, faça:
        chave = A[i]
        // Inserir A[i] na sequência ordenada A[0, ..., i -1]
        j = i - 1
        Enquanto j > -1 e A[j] > chave, faça:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = chave
```

|arranjo:|-|4|5|5|6|
|-|-|-|-|-|-|
|**índice:** |**-1**|**0**|**1**|**2**|**3**|
|i|-|-|-|-|3|
|chave:|-|-|-|-|2|
|j:|-|0|-|-|-|
|**Enquanto**|-|0 > -1 = **True** e 4 > 2 = **True**|-|-|-|


##### j = -1

```py title="pseudocodigo_ordenacao_insercao" linenums="1"  hl_lines="7-8"
def ordenacao_insercao(A):
    Para i = 1 até A.comprimento, faça:
        chave = A[i]
        // Inserir A[i] na sequência ordenada A[0, ..., i -1]
        j = i - 1
        Enquanto j > -1 e A[j] > chave, faça:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = chave
```

|arranjo:|-|4|4|5|6|
|-|-|-|-|-|-|
|**índice:** |**-1**|**0**|**1**|**2**|**3**|
|i|-|-|-|-|3|
|chave:|-|-|-|-|2|
|**Enquanto**|-|0 > -1 = **True** e 4 > 2 = **True**|-|-|-|
|j:|-1|-|-|-|-|

```py title="pseudocodigo_ordenacao_insercao" linenums="1"  hl_lines="6"
def ordenacao_insercao(A):
    Para i = 1 até A.comprimento, faça:
        chave = A[i]
        // Inserir A[i] na sequência ordenada A[0, ..., i -1]
        j = i - 1
        Enquanto j > -1 e A[j] > chave, faça:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = chave
```

|arranjo:|-|4|4|5|6|
|-|-|-|-|-|-|
|**índice:** |**-1**|**0**|**1**|**2**|**3**|
|i|-|-|-|-|3|
|chave:|-|-|-|-|2|
|j:|-1|-|-|-|-|
|**Enquanto**|-1 > -1 = **False**|-|-|-|-|

```py title="pseudocodigo_ordenacao_insercao" linenums="1"  hl_lines="9"
def ordenacao_insercao(A):
    Para i = 1 até A.comprimento, faça:
        chave = A[i]
        // Inserir A[i] na sequência ordenada A[0, ..., i -1]
        j = i - 1
        Enquanto j > -1 e A[j] > chave, faça:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = chave
```

|arranjo:|-|2|4|5|6|
|-|-|-|-|-|-|
|**índice:** |**-1**|**0**|**1**|**2**|**3**|
|i|-|-|-|-|3|
|chave:|-|-|-|-|2|
|j:|-1|-|-|-|-|
|**Enquanto**|-1 > -1 = **False**|-|-|-|-|

#### T(n) para o pior caso

Comparando cada elemento $A[i]$ com cada elemento do subarranjo ordenado inteiro (lado esquerdo), $A[0, \cdots, i - 1]$, e então $t_i = i$ para $1,2,3, \cdots, n$.

Perceba que a cada elemento a direita ($A[i]$) é necessário fazer toda a comparação nos subarranjos à esquerda ($A[0, \cdots, i - 1]$).

Logo no pior caso temos: 

$\sum_{i=1}^{n} t_i = \sum_{i=1}^{n} i = 1 + 2 + \cdots +  n$, é uma série aritmética e tem valor:

No nosso exemplo temos $n = 4$, logo: $\sum_{i=1}^{4} i = 1 + 2 + 3$, ou seja, a linha 6 é executada 6 vezes.


$\sum_{i=1}^{n} i = \dfrac{1}{2}n(n +1)$

Pelo mesmo princípio:

$\sum_{i=1}^{n} t_i - 1 = \sum_{i=1}^{n} i - 1 = \dfrac{1}{2}(n-1)((n-1) +1) = \dfrac{1}{2}(n-1)(n)$ 

Voltando ao nosso $T(n)$

$$\begin{equation}
\begin{split}
T(n) &= c_1n + c_2(n - 1) + c_4(n-1) + c_5\dfrac{1}{2}n(n +1) + c_6\dfrac{1}{2}(n-1)(n)\\
 &\quad + c_7\dfrac{1}{2}(n-1)(n) + c_8(n - 1) \\
\end{split}
\end{equation}$$

$$\begin{equation}
\begin{split}
T(n) &= c_1n + c_2(n - 1) + c_4(n-1) + c_5\dfrac{1}{2}n(n +1) + (c_6 + c_7) \dfrac{1}{2}(n-1)(n) \\
 &\quad +  c_8(n - 1) \\
\end{split}
\end{equation}$$

$$\begin{equation}
\begin{split}
T(n) &= c_1n + c_2(n - 1) + c_4(n-1) + c_5\dfrac{1}{2}n^2 +c_5\dfrac{1}{2}n + (c_6 + c_7)\dfrac{1}{2}n^2 \\
 &\quad -(c_6 + c_7)\dfrac{1}{2}n +  c_8(n - 1) \\
\end{split}
\end{equation}$$

$$\begin{equation}
\begin{split}
T(n) &= c_5\dfrac{1}{2}n^2 + (c_6 + c_7)\dfrac{1}{2}n^2 + c_1n + c_2n + c_4n \\
 &\quad -(c_6 + c_7)\dfrac{1}{2}n + c_8n + c_2 + c_4 + c_8\\
\end{split}
\end{equation}$$

$$\begin{equation}
\begin{split}
T(n) &= (c_5 + c_6 + c_7)\dfrac{1}{2}n^2 + (c_1 + c_2 + c_4 -((c_6 + c_7)\dfrac{1}{2})  + c_8)n \\
 &\quad  + c_2 + c_4 + c_8\\
\end{split}
\end{equation}$$


Podemos expressar esse tempo de execução do pior caso como $an^2 + bn + c$ para as constantes a, b e c que, mais uma vez, dependem dos custos de instrução $c_i$;

Portanto o pior caso é uma **função quadrática** de $n$.


## Poque usar o pior caso?

O tempo de execução do pior caso de um algoritmo estabelece um limite superior para o tempo de execução para qualquer entrada.

Conhecer o pior tempo garante que o algoritmo nunca demorará mais do que esse tempo.

Para alguns algoritmos, o pior caso ocorre com bastante frequência. Por exemplo, em uma pesquisa de um banco de dados , o pior caso do algoritmo de busca frequentemente ocorre quando a informação não existe.

Muitas vezes, o "caso médio" é quase tão ruim quanto o pior caso.
Suponha que escolhemos $n$ números aleatoriamente e aplicamos ordenação por inserção.

Quanto tempo transcorrerá até que o algoritmo determine o lugar no subarranjo $A[1, \cdots, i -1]$ em que deve ser inserido o elemento $A[i]$, qualquer?

Em uma média probabilística, metade dos elementos em $A[1, \cdots, i -1]$ é menor que $A[i]$ e metade dos elementos é maior.
Portanto, deve-se em média, verificar metade do subarranjo $A[1, \cdots, i -1], mesmo assim, nosso $t_i$ continua em função de $i$, como $t_i = i/2$. Resultando que o tempo de execução obtido no caso médio é uma função quadrática do tamanho da entrada, exatamente o que ocorre com o tempo de execução do pior caso.

## Ordem de crescimento

Ao falar da taxa de crescimento ou ordem de crescimento, simplificamos. Portanto, consideramos apenas o termo inicial de uma fórmula, já que o termos de ordem mais baixa são relativamente insignificantes para grandes valores de $n$.

Ignoramos também o coeficiente constante do termo inicial, visto que fatores constantes são menos significativos que a taxa de crescimento.

Afirmamos, por fim que a ordenação por inserção tem um tempo de execução do pior caso igual à $\Theta(n^2)$ (lido como "teta de $n$ ao quadrado).

Conclusão, em geral, consideramos que um algoritmo é mais eficiente que outro se seu tempo de execução do pior caso apresenta um ordem de crescimento mais baixa.

E agora? Existe alguma ordenação que tem $\Theta < \Theta(n^2)$? A análise de algoritmos apenas começou!

[Aula 03 - Um novo algoritmo de ordenação, uma nova análise](./aula_03.md)
