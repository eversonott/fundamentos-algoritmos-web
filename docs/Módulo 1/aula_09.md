---
search:
  exclude: true
---
---
marp: true
theme: rose-pine
style: |
  .columns {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1rem;
  }
---
# Aula 07 - Introdução à iteração : instrução While e Break
Fundamentos de algoritmos e introdução à programação em Python 

Prof. Everson Otoni

---

## Iteração

É a capacidade de executar um bloco de instruções repetidamente.

Vimos iteração, usando a recursividade.

---

## Reatribuição

É possível fazer mais de uma atribuição para a mesma variável.

Uma nova atribuição faz uma variável existente referir-se a um novo valor.

```python
>>> x = 5
>>> x
5
>>> x = 7
>>> x
7
```
---


Perceba que uma atribuição não é uma igualdade matemática.

Interpretar `a = b` como iguais é equivocado, na verdade o valor de `b` é atribuído a variável de nome "a". Porém a relação simétrica da igualdade não é válida, uma vez que um valor não pode ser atribuído à um nome.

```python
>>> 7 = x
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
```
---



Em matemática, uma proposição de igualdade é *verdadeira* ou *falsa* "para sempre".

Em Python, uma instrução de atribuição pode tornar duas variáveis iguais, mas elas não precisam se manter assim:


```python
>>> a = 5
>>> b = a ## Agora "a" e "b" são iguais.
>>> a = 3
>>> b
5
```

A terceira linha modifica o valor de *a*, mas não muda o valor de *b*, então após a terceira linha elas já não são iguais.

---

## Atualização de variáveis

Uma atualização é um tipo muito comum de retribuição.

O "novo" valor da variável depende do "velho".

Portanto, para atualizar uma variável é necessário que a variável exista.

Antes de poder atualizar uma variável é preciso **inicializa-lá**, normalmente com uma atribuição simples:

```python
>>> x = 0
>>> x = x + 1
```

Atualizar uma variável acrescentando 1 chama-se **incremento**
Subtrair 1 chama-se **decremento**.

---

## Instrução While

Os computadores muitas vezes são usados para automatizar tarefas repetitivas

Em um programa de computador, a repetição também é chamada de **iteração**.

Vimos que usando condicionais, executamos um bloco de código quando uma certa condição é verdadeira.

---


Assim como em condicionais, a instrução `while` executa o bloco de código se a condição é verdadeira. Porém depois que o bloco é executado o programa **volta** a verificar se a condição é verdadeira. Se for, então o bloco é executado novamente.

Quando a condição for avaliada como falsa, então a execução "salta" para a instrução não endentada.

---


```Python
def contagem_regressiva(numero):
    while numero > 0:
        print(numero)
        numero = numero - 1
    print('Lançar')
```

Podemos ler a instrução `while` como "enquanto".
Ou seja, "Enquanto `numero` for maior que 0, mostre o valor de `numero` e então decremente `numero`.

Quando chegar a 0, mostre a palavra *Lançar*.

---


1. Determine se a condição é verdadeira ou falsa.
2. Se a condição for verdadeira, execute o bloco de código e então volte ao passo 1.
3. Se for falsa, saia da instrução `while` e continue a execução.


Esse tipo de fluxo chama-se loop, porque o terceiro passo faz um volta (loop) de volta ao topo.

Perceba que, o corpo do loop deve mudar o valor de uma ou mais variáveis para que, a certa altura, a condição fique falsa e o loop termine.

Senão o loop vai se repetir para sempre, e teremos um **looop infinito**

---


Um laço `while` é perfeito para situações em que precisamos repetir, mas não sabemos quantas vezes.

Suponha que temos que calcular os primeiros múltiplos de 73 que sejam maiores que 3951.
Uma forma de resolver esse problema é gerar sucessivamente os múltiplos positivos de 73 até alcançarmos um número que 3951.

Em outras palavras, *enquanto múltiplo ≤ 73, geramos o próximo múltiplo*.

```Python
multiplo = 73
while multiplo <= 3951:
    multiplo = multiplo + 73
print(multiplo)
```

```Python
4015
```
---


```Python
multiplo = 73
while multiplo <= 3951:
    multiplo = multiplo + 73
print(multiplo)
```

```Python
4015
```

Quando a condição do laço `while` é avaliada como `False`, a execução do laço termina. O valor de `multiplo` é então, maior que 3951.

Como o valor anterior de `multiplo` não foi maior, ele terá o valor que queremos: o menor múltiplo maior do que 3951.

---

## Instrução break

As vezes não se sabe que está na hora de terminar um loop até que já esteja na metade do corpo.

Nesse caso, pod usar a instrução `break` para sair do loop.

Por exemplo, suponha que você quer receber uma entrada do usuário até que este digite "Fim". 

```Python
while True:
    linha = input('> ')
    if linha == 'fim':
        break
    print(linha)
print('Fim!')
```

A condição do loop é `True`, que sempre é verdade, então o loop roda até que chegue à instrução de interrupção.

---


Cada vez que passa pelo loop, o programa apresenta um colchete angular.

Se o usuário digitar **fim**, a instrução **break** sai do loop.

Senão, o programa ecoa o quer que o usuário digite e volta ao topo do loop.
 
Perceba que com essa instrução `break` podemos verificar a condição em qualquer lugar do loop (não somente no topo)

Podemos exprimir a condição de parada afirmativamente:
- "Pare quando isto acontecer"

Em vez de negativamente
- "Continue a seguir até que isso aconteça"

---


# Aula 08 - Conclusão da instrução while (Iteração), strings e listas

Fundamentos de algoritmos e introdução à programação em Python 

Prof. Everson Otoni

---

## Raízes quadradas

Loops muitas vezes são usados em programas que calculam resultados numéricos que começam com uma reposta aproximada e melhoram iterativamente.

Uma forma de calcular raízes quadradas é o método de Newton.

Suponha que queira saber a raiz quadrada de um número, o chamaremos de `radicando`, Se começar com quase qualquer estimativa, é possível calcular uma estimativa melhor com a seguinte fórmula:

$$
\text{raiz} = \dfrac{\text{estimativa} + \text{radicando} / \text{estimativa}}{2}
$$

---


```Python
>>> radicando = 4
>>> estimativa = 3
>>> raiz = (estimativa + radicando / estimativa) / 2
>>> raiz
2.1666666666666665
```

O resultado é mais próximo à resposta correta ($\sqrt{4} = 2$).

Se repetirmos o processo com a nova estimativa, chegamos ainda mais perto:

```Python
>>> estimativa = raiz
>>> raiz = (estimativa + radicando / estimativa) / 2
>>> raiz
2.0064102564102564
```

---


```Python
>>> estimativa = raiz
>>> raiz = (estimativa + radicando / estimativa) / 2
>>> raiz
2.0000102400262145
>>> estimativa = raiz
>>> raiz = (estimativa + radicando / estimativa) / 2
>>> raiz
2.0000000000262146
```

Em geral, não sabemos com antecedência quantos passos são necessários para chegar à resposta correta, mas sabemos quando chegarmos lá porque a estimativa para de mudar.

Ou seja, quando raiz == estimativa, podemos parar.

---


```Python
while True:
    print(estimativa)
    raiz = (estimativa + radicando / estimativa) / 2
    if raiz == estimativa:
        break
    estimativa = raiz
```

Para maior parte de valores de `radicando` funciona bem, mas pode ser perigoso testar para alguns tipos de valores.

---


Em vez de verificar se `raiz` e `estimativa` são exatamente iguais, é mais seguro usar a função integrada `abs` para calcular o valor absoluto ou magnitude da diferença entre eles:

```Python
while True:
    print(estimativa)
    raiz = (estimativa + radicando / estimativa) / 2
    if abs(raiz - estimativa) < 0.00001:
        break
    estimativa = raiz
```

---

## Algoritmos

O método de Newton é um exemplo de um **algoritmo**: um processo mecânico para resolver uma categoria de problemas.

Técnicas qua aprendemos em matemática básica, como transporte na adição, o empréstimo na subtração e a divisão longa são todos algoritmos.

Algoritmos, são processos mecânicos, nos quais cada passo segue a partir do último, de acordo com um conjunto de regras simples.

Algumas coisas que as pessoas fazem naturalmente, sem dificuldade ou pensamento consciente, são as mais difíceis para exprimir algoritmicamente.

---

## Strings

Já sabemos que o tipo string em Python é denominado de `str`.

Usado para representar e manipular dados de texto.

Uma **sequência** de caracteres, incluindo espaços, pontuação e diversos símbolos.

Um valor de string é representado como uma sequência de caracteres delimitada por apóstrofos.

---

### Operadores relacionais

Além de ser possível comparar se duas strings são iguais ou diferentes com os operadores de comparação: `==` e `!=`.

Os operadores de comparação `<`e `>` comparam strings usando a ordem do dicionário.

```Python
primeiro_nome = 'abc'
segundo_nome = 'abd'
primeiro_nome < segundo_nome
True
```

---

### Operador in

Como uma string é uma sequência de caracteres.

Podemos verificar se um caractere aparece em uma string, usando o operador **in**:

```Python
>>> linguagem = 'Python'
>>> 'y' in linguagem
True
>>> 's' in linguagem
False
```

---


O operador **in** também pode ser usado para verificar se uma string aparece em outra:

```Python
>>> 'th' in linguagem
True
```

Como 'th' aparece na string `linguagem`, dizemos que 'th' é uma **substring** de `linguagem`.

---

### Operador de indexação

Os caracteres individuais de uma string podem ser acessados usando o **operador de indexação [ ]**.

Índice de um caractere em uma string é o deslocamento do caractere (ou seja, a posição na string) com relação ao primeiro caractere.

O primeiro caractere tem sempre índice 0, o segundo tem índice 1 (pois está a uma distância do primeiro caractere)

```Python
>>> linguagem[0]
'P'
>>> linguagem[1]
'y'
>>> linguagem[5]
'n'
```
---

#### Representação gráfica

---

### Operador de indexação negativo

Índices negativos podem ser usados para acessar os caracteres do final (lado direito) da string.

Por exemplo, o último caractere e o penúltimo caractere podem ser acessados usando os índices negativos -1 e -2, respectivamente.

```Python
>>> linguagem[-1]
'n'
>>> linguagem[-2]
'o'
```
---

#### Representação gráfica

---

### Operadores - Resumo

| Uso          | Explicação                                                                      |
|--------------------|---------------------------------------------------------------------------------|
| x in s       | Verdadeiro se x for uma substring da string s, e falso caso contrário           |
| x not in s   | Falso se a string x for uma substring da strings s, e verdadeiro caso contrário |
| s + t        | Concatenação da string s com a string t                                         |
| s * n | Concatenação de n cópias de s                                                   |
| n * s | Concatenação de n cópias de s                                                   |
---


| Uso          | Explicação                                                                      |
|--------------------|---------------------------------------------------------------------------------|
| s[i]         | Caractere da strings s no índice i                                              |
| len(s)       | Comprimento da strings s                                                        |
---

## Listas

Podemos organizar os dados em uma lista.

Fazemos isso cotidianamente, uma lista de compras, uma lista de cursos, uma lista de contatos, uma lista de músicas e assim por diante.

Em Python, as listas são armazenadas em um tipo de objeto denominado `lista`

Assim como uma string, uma lista é uma sequência de valores.
Porém em uma lista, eles podem ser de qualquer tipo, portanto é uma sequência de objetos.

```Python
>>> animais = ['peixe', 'cachorro', 'gato']
```

---


A variável `animais` é avaliada como a lista:

```Python
>>> animais
['peixe', 'cachorro', 'gato']
```
Em Python, uma lista é representada como uma sequência de objetos separados por vírgulas, dentro colchetes.

Uma lista vazia é representada como [ ].

---


As listas podem conter itens de diferentes tipos.

```Python
>>> coisas = ['um', 2, [3, 4]]
```

A lista `coisas` tem três itens: 
- o primeiro é uma string 'um'. 
- o segundo é um inteiro 2.
- o terceiro é a lista [3, 4].

Uma lista dentro de outra lista é uma lista aninhada.

---

### Operadores de Lista

A maioria dos operadores que utilizamos para strings, podem ser utilizados para listas.

Os itens na lista podem ser acessados individualmente usando o operador de indexação ([ ]).

### Operador de indexação

```Python
>>> animais = ['peixe', 'cachorro', 'gato']
>>> animais[0]
'peixe'
>>> animais[1]
'cachorro'
>>> animais[-1]
'gato'
```

---

### Representação gráfica

---

### Comprimento

O comprimento de uma lista, ou seja, o número de itens nela, é calculado usando a função `len()`.

```Python
>>> len(animais)
3
``` 

---

### Operadores de lista - "Adição e multiplicação"

Assim como as strings, as listas podem ser "adicionadas" ou "multiplicadas" por um número inteiro qualquer, isso significam que podem ser *concatenadas*.


```Python
>>> animais + animais
['peixe', 'cachorro', 'gato', 'peixe', 'cachorro', 'gato']
```

```Python
>>> animais * 3
['peixe', 'cachorro', 'gato', 'peixe', 'cachorro', 'gato', 'peixe', 'cachorro', 'gato']
```

---

### Operadores de lista - Operador in

Para verificar se determinados elementos estão presentes na lista, utilizamos o operador `in` em uma expressão booleana.

Por exemplo, é avaliado como `True`, se a string `'coelho'` estiver presente como elemento na lista `animais`.

```Python
>>> 'coelho' in animais
False
```

```Python
>>> 'peixe' in animais
True
```

---

### Algumas funções embutidas para listas


Temos as funções `min()`, `max()` e `sum()`, que possuem como entrada um objeto iterável e retornam, respectivamente, o menor item, o maior item e a soma dos itens da lista.

```Python
>>> notas = [23.99, 19.99, 34.50, 120.99]
>>> min(notas)
19.99
```

```Python
>>> notas = [23.99, 19.99, 34.50, 120.99]
>>> max(notas)
120.99
```

```Python
>>> notas = [23.99, 19.99, 34.50, 120.99]
>>> sum(notas)
199.47
```

---


E para elementos que não são numéricos?

---
### Resumo dos operadores e funções de listas

| Uso| Explicação|
|----|-----------|
|x in lst| Verdadeiro se o objeto x estiver na lista lst, caso contrário, falso.|
|x not in lst| Falso se o objeto x estiver na lista lst, caso contrário, verdadeiro.|
|lstA + lstB| Concatenação das listas lstA e lstB|
|lst * n ou n * lst| Concatenação de *n* cópias da lista lst|
|lst[i]| Item no índice **i** da lista lst|
|len(lst)| Comprimento ou tamanho da lista lst|
|min(lst)| Menor item da lista lst|

---

| Uso| Explicação|
|----|-----------|
|max(lst)| Maior item na lista lst|
|sum(lst)| Soma dos itens na lista lst|

---

### Métodos de lista ou funções **sobre** listas

Diferente de funções que recebem como entrada as listas, como vimos com as funções: min(), max() e sum().

Existem as funções **sobre** listas. Elas fazem parte de todo tipo de objeto lista e por isso são conhecidas como métodos.

Por exemplo, para adicionar um novo animal a lista `animais` sem precisar realizar toda a atribuição novamente. Podemos utilizar o método `append()` [acrescentar].

```Python
>>> animais.append('tartaruga')
>>> animais
['peixe', 'cachorro', 'gato', 'tartaruga']
```

---

#### append(object)

```Python
>>> animais.append('tartaruga')
```

Observe como chamamos o método `append`. 

Utilizamos uma notação de ponto.

Passamos com entrada o novo elemento a ser adicionado sobre a lista em questão. Ou seja, a função `append()` é uma função lst, não pode ser chamada por si só. Deve sempre ser chamada sobre alguma lista `lst`.

E por fim o novo elemento é acrescentado ao final da lista.

---

#### count(value)

Até o momento temos:
```Python
>>> animais
['peixe', 'cachorro', 'gato', 'tartaruga']
```

Vamos realizar um novo acréscimo. Um novo item.

```Python
>>> animais.append('gato')
>>> animais
['peixe', 'cachorro', 'gato', 'tartaruga', 'gato']
```

---


Existe também o método `count()` [contar]. Quando chamado sobre uma lista com um argumento de entrada, ele retorna o número de vezes que o argumento aparece como item na lista.

```python
>>> animais.count('gato')
2
```

---

#### remove(value)

```python
>>> animais
['peixe', 'cachorro', 'gato', 'tartaruga', 'gato']
```

Para remover um item da lista, utilizamos o método `remove()` [remover]. Que necessita também de um argumento.


```python
>>> animais.remove('gato')
>>> animais
['peixe', 'cachorro', 'tartaruga', 'gato']
```

Perceba que o método `remove()`, remove a primeira ocorrência do item que é passado como parâmetro.

---

#### pop(index=-1)

Ainda sobre remover itens, temos também o método `pop()`.

`pop()` remove o item na posição fornecida (indexada) na lista e retorna o item removido. Se nenhum índice for especificado, `pop()` remove e retorna o ultimo item da lista.

```python
>>> animais
['peixe', 'cachorro', 'tartaruga', 'gato']
```

```python
>>> animais.pop()
'gato'
>>> animais
['peixe', 'cachorro', 'tartaruga']
```

---


```python
>>> animais.pop(0)
'peixe'
>>> animais
['cachorro', 'tartaruga']
```

---


