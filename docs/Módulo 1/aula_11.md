
# Aula 11 - Strings, Listas e seus Operadores e Métodos

{% set aula = "11" %}
{% set link = "bNOMcWrDFVs" %}
{% set objetivos = 
[
  "Compreender o tipo `str` como sequência de caracteres e utilizar seus operadores: `in`, `[]`, `+`, `*`",
  "Acessar elementos de strings e listas por indexação direta e negativa, e realizar fatiamentos",
  "Aplicar operadores e funções como `len()`, `min()`, `max()` e `sum()` sobre listas",
  "Utilizar os principais métodos de listas como `append`, `pop`, `remove`, `insert`, `sort`, `reverse` e `extend`",
  "Resolver problemas práticos manipulando listas com diferentes tipos de dados e estruturas aninhadas"
]
%}
{% include "templates/cabecalho.md" %}



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



