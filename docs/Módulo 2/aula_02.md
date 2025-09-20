# Aula 02 - Análise de algoritmos e suas complexidades (pt. 1)


{% set aula = "01" %}
{% set link = "gjcuwUxTQGY" %}
{% set objetivos = ["Um entendimento do algoritmo de ordenação por inserção.", "Introduzir os conceitos de análise de algoritmo.", "O uso do pior caso de execução.", "Ordem de crescimento dos algoritmos."] %}


{% include "templates/cabecalho_sem_video.md" %}

---


## Ordenação por inserção - Passo a passo


![](https://upload.wikimedia.org/wikipedia/commons/2/25/Insertion_sort_animation.gif){: .center .shadow}


Para os passos a seguir vamos usar a lista numérica: `[6, 5, 4, 2]`

Iremos implementar a função `ordenacao_insercao`.
Essa função irá receber um objeto python do tipo `list` e com seus elementos numéricos.

Portanto temos:

```py title="ordenacao_insercao" linenums="1"
lista_numerica = [6, 5, 4, 2]

def ordenacao_insercao(lista):
    ...

```

Vamos implementar com calma e usando `print` para verificar os estados dos valores envolvidos (teste de mesa):

Inicialmente temos uma lista numérica desordenada e posteriormente teremos ela ordenada.

Vamos dividir a parte principal do nosso script em antes de chamar a função e depois.

```py title="ordenacao_insercao" linenums="1"
lista_numerica = [6, 5, 4, 2]

def ordenacao_insercao(lista):
    ...

print(f'Lista Desordenada: {lista_numerica} \n')
ordenacao_insercao(lista_numerica)
print(f'Lista Ordenada: {lista_numerica} \n')

```

Para:

```sh title="Terminal"
python ordenacao_insercao.py
```

Temos:

```sh title="Saída"
Lista Desordenada: [6, 5, 4, 2]

Lista Ordenada: [6, 5, 4, 2]

```

Vamos agora implementar algumas funções de impressões que nos auxiliarão:

Para vermos os índices:

```py title="ordenacao_insercao"
def imprime_indices(lista):
    lista_indices = []
    for i in range(0, len(lista)):
        lista_indices.append(i)
    print(f'Indices: {lista_indices}')
```

Atualizando a função principal:

```py title="ordenacao_insercao"
def ordenacao_insercao(lista):
    imprime_indices(lista)
```

```sh title="Saída"
Lista Desordenada: [6, 5, 4, 2]

Indices: [0, 1, 2, 3]
Lista Ordenada: [6, 5, 4, 2]

```

Para vermos os valores:

```py title="ordenacao_insercao"
def imprime_valores(lista):
	print(lista)
```

Atualizando a função principal:

```py title="ordenacao_insercao"
def ordenacao_insercao(lista):
    imprime_indices(lista)
    imprime_valores
```

```sh title="Saída"
Lista Desordenada: [6, 5, 4, 2]

Indices: [0, 1, 2, 3]
Valores: [6, 5, 4, 2]
Lista Ordenada: [6, 5, 4, 2]


```




Como sempre precisamos verificar em qual índice o valor está, vamos juntas as duas funções
em um função que nos trás uma "única" impressão:


```py title="ordenacao_insercao"
def imprime(lista):
	imprime_indices(lista)
	imprime_valores(lista)
	print('')
```

Atualizando a função principal:

```py title="ordenacao_insercao"
def ordenacao_insercao(lista):
    imprime(lista)
```


```sh title="Saída"
Lista Desordenada: [6, 5, 4, 2]

Indices: [0, 1, 2, 3]
Valores: [6, 5, 4, 2]

Lista Ordenada: [6, 5, 4, 2]

```

Temos, então até agora:

```py title="ordenacao_insercao" linenums="1"
def imprime_indices(lista):
    lista_indices = []
    for i in range(0, len(lista)):
        lista_indices.append(i)
    print(f'Indices: {lista_indices}')

def imprime_valores(lista):
	print(f'Valores: {lista}')
	
def imprime(lista):
	imprime_indices(lista)
	imprime_valores(lista)
	print('')

def ordenacao_insercao(lista):
	imprime(lista)
	
lista_numerica = [6, 5, 4, 2]

print(f'Lista Desordenada: {lista_numerica} \n')
ordenacao_insercao(lista_numerica)
print(f'Lista Ordenada: {lista_numerica} \n')
```

Vamos a implementação de fato!

A partir de agora vamos partir de discussões e erros mais simples até chegar ao algoritmos de fato.

```py title="ordenacao_insercao" linenums="15"
def ordenacao_insercao(lista):
	imprime(lista)
	
	for i in range(0, len(lista)):
		if lista[i] > lista[i + 1]:
			# Trocar lista[i + 1] com lista[i]
			...
```

Há um problema, e antes de implementarmos a troca, podemos perceber:

```sh title="Saída"
if lista[i] > lista[i + 1]:
                  ~~~~~^^^^^^^
IndexError: list index out of range
```

Isso acontece que estamos sempre comparando com o termo mais a direita, mais sucessor.


Acontece que nosso `i` vai até o último índice e compara o último índice com um índice que não existe.

Vamos corrigir isso, deixando o `i` ir apenas ao penúltimo índice.


Vamos usar um print para verificar isso.

```py title="ordenacao_insercao" linenums="15" hl_lines="4"
def ordenacao_insercao(lista):
	imprime(lista)
	
	for i in range(0, len(lista) - 1):
		print(f'Índice i: {i}')
		if lista[i] > lista[i + 1]:
			# Trocar lista[i + 1] com lista[i]
			...
```

```sh title="Saída" hl_lines="6-8"
Lista Desordenada: [6, 5, 4, 2]

Indices: [0, 1, 2, 3]
Valores: [6, 5, 4, 2]

Índice i: 0
Índice i: 1
Índice i: 2
Lista Ordenada: [6, 5, 4, 2]

```

Vamos fazer a troca e chamar a impressão a cada troca:

```py title="ordenacao_insercao" linenums="15" hl_lines="8-11"
def ordenacao_insercao(lista):
	imprime(lista)
	
	for i in range(0, len(lista) - 1):
		print(f'Índice i: {i}')
		if lista[i] > lista[i + 1]:
			# Trocar lista[i + 1] com lista[i]
			valor_menor = lista[i + 1]
			lista[i + 1] = lista[i]
			lista[i] = valor_menor
			imprime(lista)
```

```sh title="Saída" hl_lines="6 8 10 12 14 16"
Lista Desordenada: [6, 5, 4, 2]

Indices: [0, 1, 2, 3]
Valores: [6, 5, 4, 2]

Índice i: 0
Indices: [0, 1, 2, 3]
Valores: [5, 6, 4, 2]

Índice i: 1
Indices: [0, 1, 2, 3]
Valores: [5, 4, 6, 2]

Índice i: 2
Indices: [0, 1, 2, 3]
Valores: [5, 4, 2, 6]

Lista Ordenada: [5, 4, 2, 6]
```

Vamos analisar o que houve:

- Na primeira iteração, com `i = 0`:

    - Indices: [0, 1, 2, 3]
    - Valores: [6, 5, 4, 2]
    
    - Começamos olhando para o primeiro elemento.
    - Trocamos o `lista[0] = 6` e `lista[1] = 5`.

        - Indices: [0, 1, 2, 3]
        - Valores: [5, 6, 4, 2]

Normal!

- Na segunda iteração, com `i = 1`.
    - Indices: [0, 1, 2, 3]
    - Valores: [5, 6, 4, 2]

    - Começamos olhando para o segundo elemento.
    - Trocamos `lista[1] = 6` e `lista[2] = 4`.
        - Indices: [0, 1, 2, 3]
        - Valores: [5, 4, 6, 2]


O problema surge aqui!

Não estamos implementando o nosso algoritmo, pois ainda teríamos que ordenar o valores `[5, 4]` para `[4, 5]`.

Lembre-se que com o baralho, quando já temos cartas (ordenadas) na mão esquerda (para destros) temos que olhar para todas as cartas.

E verificar onde devemos inserir.

Portanto se tenho em uma mão `[5, 6]` e tiro do baralho uma carta `[4]` devo olhar para o `6`, quanto para o `5`.

`[4]` vai para a esquerda de `[6]`, mas também vai a esquerda de `[5]`, ou seja, vai a esquerda de `[5, 6]`.

Logo: `[4, 5, 6]`.


Vamos pensar, voltando para a programação:

No nosso caso, ainda com `i = 1`, temos que olhar para o `lista[0]`.

Ou seja, enquanto o elemento a esquerda for maior que nosso elemento a ser trocado e não chegamos ao início, devemos continuar trocando.

Isso me parece um `while`.

Repita até enquanto a condição for verdadeira.

Repita até os valores maiores que 4 estarem a direita de 4.

Voltamos ao código, como estamos falando de termos anteriores, vamos usar o termo `indice_anterior`

```py title="ordenacao_insercao" linenums="15" hl_lines="6-9 11-13 15"
def ordenacao_insercao(lista):
	imprime(lista)
	
	for i in range(0, len(lista) - 1):
		print(f'Índice i: {i}')
		indice_anterior = i - 1
		print(f'Índice anterior: {indice_anterior}')
		while lista[indice_anterior] > lista[indice_anterior + 1]:
			print(f'Índice anterior: {indice_anterior}')
			# Trocar lista[indice_anterior + 1] com lista[indice_anterior]
			valor_menor = lista[indice_anterior + 1]
			lista[indice_anterior + 1] = lista[indice_anterior]
			lista[indice_anterior] = valor_menor
			imprime(lista)
			indice_anterior -= 1
```

```sh title="Saída" linenums="1" hl_lines="7 12 18 22"
Lista Desordenada: [6, 5, 4, 2]

Indices: [0, 1, 2, 3]
Valores: [6, 5, 4, 2]

Índice i: 0
Índice anterior: -1
Índice i: 1
Índice anterior: 0
Índice anterior: 0
Indices: [0, 1, 2, 3]
Valores: [5, 6, 4, 2]

Índice i: 2
Índice anterior: 1
Índice anterior: 1
Indices: [0, 1, 2, 3]
Valores: [5, 4, 6, 2]

Índice anterior: 0
Indices: [0, 1, 2, 3]
Valores: [4, 5, 6, 2]

Lista Ordenada: [4, 5, 6, 2]

```

Na linha 12, temos o `5` a esquerda de `6`.

Na linha 18, temos o `4` a esquerda de `6`.

Na linha 22, finalmente, o `4` esquerda de `[5,6]`.


Mas perceba que o elemento `2`, continua desordenado.

Precisamos que nosso `i` vá até o último índice (`3`) para que compare:

`lista[2] = 6  > lista[3] = 2`

Mas temos um problema, nosso último índice anterior é -1. 

Perceba na linha 20, o índice anterior é impresso como 0. 

Porém essa impressão vem antes da linha de decremento (`indice_anterior -= 1`)

Ou seja, se entrarmos novamente no while, irá considerar a lista como cíclica.

E iremos comparar `lista[-1] = 2 > lista[0] = 4` e essa não é o tipo de comparação que queremos para validar nosso `while`

Precisamos garantir, antes de incluir `i = len(lista)` que nosso `indice_anterior` percorra os índices `>= 0`:

```py title="ordenacao_insercao" linenums="15" hl_lines="7"
def ordenacao_insercao(lista):
	imprime(lista)
	
	for i in range(0, len(lista)):
		print(f'Índice i: {i}')
		indice_anterior = i - 1
		print(f'Índice anterior: {indice_anterior}')
		while indice_anterior >= 0 and lista[indice_anterior] > lista[indice_anterior + 1]:
			print(f'Índice anterior: {indice_anterior}')
			# Trocar lista[indice_anterior + 1] com lista[indice_anterior]
			valor_menor = lista[indice_anterior + 1]
			lista[indice_anterior + 1] = lista[indice_anterior]
			lista[indice_anterior] = valor_menor
			imprime(lista)
			indice_anterior -= 1
```

```sh title="Saída" linenums="1" hl_lines="38"
Lista Desordenada: [6, 5, 4, 2]

Indices: [0, 1, 2, 3]
Valores: [6, 5, 4, 2]

Índice i: 0
Índice anterior: -1
Índice i: 1
Índice anterior: 0
Índice anterior: 0
Indices: [0, 1, 2, 3]
Valores: [5, 6, 4, 2]

Índice i: 2
Índice anterior: 1
Índice anterior: 1
Indices: [0, 1, 2, 3]
Valores: [5, 4, 6, 2]

Índice anterior: 0
Indices: [0, 1, 2, 3]
Valores: [4, 5, 6, 2]

Índice i: 3
Índice anterior: 2
Índice anterior: 2
Indices: [0, 1, 2, 3]
Valores: [4, 5, 2, 6]

Índice anterior: 1
Indices: [0, 1, 2, 3]
Valores: [4, 2, 5, 6]

Índice anterior: 0
Indices: [0, 1, 2, 3]
Valores: [2, 4, 5, 6]

Lista Ordenada: [2, 4, 5, 6]
```


Algoritmo de ordenação por inserção, implementado!

Limpando os print, ficamos com:

```py title="ordenacao_insercao" linenums="15" 
def ordenacao_insercao(lista):
	for i in range(0, len(lista)):
		indice_anterior = i - 1
		while indice_anterior >= 0 and lista[indice_anterior] > lista[indice_anterior + 1]:
			valor_menor = lista[indice_anterior + 1]
			lista[indice_anterior + 1] = lista[indice_anterior]
			lista[indice_anterior] = valor_menor
			indice_anterior -= 1
```

Em python podemos fazer reatribuições simultâneas:

```py title="ordenacao_insercao" linenums="15" hl_lines="6" 
def ordenacao_insercao(lista):
	for i in range(0, len(lista)):
		indice_anterior = i - 1
		while indice_anterior >= 0 and lista[indice_anterior] > lista[indice_anterior + 1]:
			lista[indice_anterior + 1], lista[indice_anterior] = lista[indice_anterior], lista[indice_anterior + 1]
			indice_anterior -= 1
```

## Análise da ordenação por inserção

O tempo necessário pelo procedimento `ordenacao_insercao` depende da entrada:

- Ordenar mil números demora mais que ordenar três números.

Além disso, a ordenação por inserção pode demorar tempo diferentes para ordenar duas sequências de entrada do mesmo tamanho, dependendo do quanto elas já estejam ordenadas:

- Ordenar `[2, 5, 4, 6]` é muito mais rápido que ordenar `[2, 6, 5, 4]`.
    - A lista numérica `[2, 5, 4, 6]` entra menos vezes no `while` do que `[2, 6, 5, 4]`.
    - Observe que ambas listas tem `len(lista) = 5`




Em termos gerais, o tempo gasto por um algoritmo cresce com o tamanho da entrada.

Portanto, é tradicional descrever o tempo de execução de um programa em **função do tamanho de sua entrada**.

### O tempo de execução



O tempo de execução de um algoritmo em determinada entrada é o número de operações primitivas ou "passos" executados.

#### Tempo constante para cada linha

**Vamos adotar que uma quantidade de tempo constante é exigida para executar cada linha do nosso pseudo código.**

Uma linha pode demorar uma quantidade de tempo diferente de outra linha, mas consideremos que cada execução de `i-ésima` linha leva um tempo $c_i$, onde $c_i$ é uma constante.


#### Quantidade de vezes que uma linha é executada


Como estamos falando de número de operações, e já definimos que cada linha terá um tempo constante.

Agora precisamos avaliar quantas vezes cada linha é executada.


Para isso partiremos do nosso algoritmo mais simples:


```py title="ordenacao_insercao" linenums="15" 
def ordenacao_insercao(lista):
	for i in range(0, len(lista)):
		indice_anterior = i - 1
		while indice_anterior >= 0 and lista[indice_anterior] > lista[indice_anterior + 1]:
			lista[indice_anterior + 1], lista[indice_anterior] = lista[indice_anterior], lista[indice_anterior + 1]
			indice_anterior -= 1
```

Para facilitar ainda mais a análise, vamos simplificar alguns nomes:
Não é uma boa prática, mas necessitamos desta mudança para fins didáticos.

```py title="ordenacao_insercao" linenums="15" 
def ordenacao_insercao(lista):
	for i in range(0, len(lista)):
		i_ant = i - 1
		while i_ant >= 0 and lista[i_ant] > lista[i_ant + 1]:
			lista[i_ant + 1], lista[i_ant] = lista[i_ant], lista[i_ant + 1]
			i_ant -= 1
```

Iremos tratar `len(lista)` como `n`, ou seja, `n` é quantidade de elementos.

- A linha `for i in range(0, len(lista)):` é executada `n + 1`.

    - Ela precisa ser executada uma vez a mais para desvalidar o `i` que ficará fora do `range`.
    
    - Lembre-se `len(lista)` não é inclusivo no `for`, justamente para relacionarmos a condição de parada com o tamanho, quando iniciamos em `0`.

- A linha `i_ant = i - 1` é executada `n`.

    - Ela está dentro do `for` e a cada iteração é executada. Há 

##### O While do nosso algoritmo

Para discutirmos a próxima linha vamos fazer diversas inferências:
Vamos manter a escrita em itens para entender melhor as implicações.

- A linha `while i_ant >= 0 and lista[i_ant] > lista[i_ant + 1]:` é executada uma quantidade que depende de quanto a lista está ordenada com seus valores anteriores.
    
    - Esta linha depende de cada lista, ou seja, depende de cada caso.

    - Depende da quantidade de elementos desordenados/ordenados anteriormente.

    - Então temos, no mínimo `1` elemento anterior e no máximo `n - 1` elementos anteriores (para o último elemento). 
    Considerando uma iteração a mais para sair do `while`, temos no máximo `n` elementos.
    Perceba que aqui estamos considerando o pior caso (- iremos detalhar adiante), que é uma lista numérica ordenada decrescentemente.

    - Chamamos de limite inferior: `1`.

    - Chamamos de limite superior: `n`.

    - Temos uma função que varia dentro desses limites. Um termo geral $f(k)$
        
        - Ou seja, $f(k)$ variando de $1$ a $n$.

    - A quantidade de vezes que a linha será executada é igual:
        
        - $f(1) + f(2) + f(3) + \cdots + f(n)$

    - Temos um somatório:
        
        - $\sum_{k=1}^{n} f(k)$

        - Como f(k) é a própria quantidade de termos anterior ($f(k) = k$), temos:

        - $\sum_{k=1}^{n} f(k) = \sum_{k = 1}^{n} k = 1 + 2 + \cdots +  n$

            - Somatório de uma progressão aritmética de $\text{razão} = 1$

                - $\sum_{k = 1}^{n} k = \dfrac{n}{2} \cdot (n + 1)$

    - Concluindo, finalmente:

        - A linha `while i_ant >= 0 and lista[i_ant] > lista[i_ant + 1]:` é executada $\dfrac{n}{2} \cdot (n + 1)$.

- A linha `lista[i_ant + 1], lista[i_ant] = lista[i_ant], lista[i_ant + 1]` é executada uma vez menos que a linha do nosso querido `while`.

    - $\sum_{k=1}^{n - 1} f(k) - 1$, $f(k) = k$.

    - $\sum_{k=1}^{n} f(k) - 1 = \sum_{k=1}^{n} k - 1 = \dfrac{(n-1)}{2} \cdot ((n-1) +1) = \dfrac{n-1}{2} \cdot n$ 

    - A linha `lista[i_ant + 1], lista[i_ant] = lista[i_ant], lista[i_ant + 1]` é executada $\dfrac{n-1}{2} \cdot n$

- A linha `i_ant -= 1` está dentro do while assim como a linha anterior da troca
    
    - A linha `i_ant -= 1` é executada $\dfrac{n-1}{2} \cdot n$


Partiremos de uma fórmula confusa que utiliza todos os custos de instrução $c_i$ e a quantidade de vezes de cada linha até uma notação muito mais simples, que também é mais concisa e mais fácil de manipular.

E será por meio dessa notação mais simples também que facilitará a tarefa de determinar se um algoritmo é mais eficiente que outro.


Vamos então organizar os custos e a quantidade em uma tabela

### Ordenação por inserção com custo


|linha|def ordenacao_insercao(lista):|custo|vezes|
|-|-|-|-|
    |1|&emsp;`for i in range(0, len(lista)):`|$c_1$|n + 1|
        |2|&emsp;&emsp; `i_ant = i - 1`|$c_2$|n|
        |3|&emsp;&emsp;`while i_ant >= 0 and lista[i_ant] > lista[i_ant + 1]:`|$c_3$|$\dfrac{n}{2} \cdot (n + 1)$|
        |4|&emsp;&emsp;&emsp;`lista[i_ant + 1], lista[i_ant] = lista[i_ant], lista[i_ant + 1]`|$c_4$|$\dfrac{n-1}{2} \cdot n$|
        |5|&emsp;&emsp;&emsp;`i_ant -= 1`|$c_5$|$\dfrac{n-1}{2} \cdot n$|

O tempo de execução do algoritmo é a soma dos tempos de execução para cada instrução executada.

Para calcular o $T(n)$, o tempo de execução da ordenação por inserção de uma entrada de $n$ valores, somamos os produtos das colunas `custo` e `vezes`, obtendo:


$$\begin{equation}
\begin{split}
T(n) &= c_1 \cdot  (n + 1) + c_2 \cdot (n) + c_3 \cdot  \biggl(\dfrac{n}{2} \cdot (n + 1)\biggl) + c_4 \cdot \biggl(\dfrac{n-1}{2} \cdot n \biggl)+ \\
    &\quad c_5 \cdot  \biggl(\dfrac{n-1}{2} \cdot n\biggl)\\
\end{split}
\end{equation}$$

Como a multiplicação por $\dfrac{1}{2}$ ou uma divisão por $2$ é sempre constante na função.

Agregamos essa operação com um escalar, como uma operação que envolve uma multiplicação constate.

Logo agregamos ao tempo constate de cada linha, que também é um fator multiplicativo.

Então temos:

$$\begin{equation}
\begin{split}
T(n) &= c_1 \cdot  (n + 1) + c_2 \cdot (n) + c_3 \cdot  (n \cdot (n + 1))
+ c_4 \cdot ((n-1) \cdot n )+ \\
    &\quad c_5 \cdot  ((n-1) \cdot n)\\
\end{split}
\end{equation}$$

Vamos agora multiplicar os termos que envolvem $n$:

$$\begin{equation}
\begin{split}
T(n) &= c_1 \cdot  (n + 1) + c_2 \cdot (n) + c_3 \cdot  (n^2 + n)
+ c_4 \cdot (n^2 - n)+ \\
    &\quad c_5 \cdot  (n^2 - n)\\
\end{split}
\end{equation}$$

Vamos fazer a multiplicação pelas constantes:

$$\begin{equation}
\begin{split}
T(n) &= 1c_1 n + 1c_1 + c_2 n +  1c_3 n^2 + 1 c_3n +  1c_4 n^2 - 1c_4 n + 1c_5 n^2 - 1c_5 n\\
\end{split}
\end{equation}$$

Vamos agrupar os termos semelhantes, colocando-os lado a lado:

$$\begin{equation}
\begin{split}
T(n) &= 1c_3 n^2 + 1c_4 n^2 + 1c_5 n^2 + 1c_1 n  + 1c_2 n + 1 c_3n  - 1c_4 n  - 1c_5 n + 1c_1\\
\end{split}
\end{equation}$$

Colocando em evidência:


$$\begin{equation}
\begin{split}
T(n) &= (c_3 + c_4  + c_5)n^2 + (c_1 + c_2 + c_3 - c_4 - c_5)n + 1c_1\\
\end{split}
\end{equation}$$

Reconsiderando as constantes:

$$\begin{equation}
\begin{split}
T(n) &= an^2 + bn + c\\
\end{split}
\end{equation}$$


Portanto o pior caso é uma **função quadrática** de $n$.


## Poque usar o pior caso?

O tempo de execução do pior caso de um algoritmo estabelece um limite superior para o tempo de execução para qualquer entrada.

Conhecer o pior tempo garante que o algoritmo nunca demorará mais do que esse tempo.

## Ordem de crescimento

Ao falar da taxa de crescimento ou ordem de crescimento, simplificamos. Portanto, consideramos apenas o termo inicial de uma fórmula, já que o termos de ordem mais baixa são relativamente insignificantes para grandes valores de $n$.

Ignoramos também o coeficiente constante do termo inicial, visto que fatores constantes são menos significativos que a taxa de crescimento.

## Finalmente a análise do pior caso do algoritmo de ordenação por inserção

**Afirmamos, por fim que a ordenação por inserção tem um tempo de execução do pior caso igual à $\Theta(n^2)$ (lido como "teta de $n$ ao quadrado).**

Conclusão, em geral, consideramos que um algoritmo é mais eficiente que outro se seu tempo de execução do pior caso apresenta um ordem de crescimento mais baixa.

E agora? Existe alguma ordenação que tem $\Theta < \Theta(n^2)$? A análise de algoritmos apenas começou!

