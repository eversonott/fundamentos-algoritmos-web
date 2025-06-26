
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


## Métodos de lista


---

### Métodos de lista ou funções **sobre** listas 

Como vimos na aula anterior, existe funções associadas diretamente as listas e elas chamamos de métodos de listas.

---


Até agora vimos:

|Método|Descrição|
|-----|-----|
|append(object)| Novo elemento é acrescentado ao final da lista (como último item)|
|count(value)| Retorna o número de vezes que o argumento aparace como item|
|remove(value)| Remove a primeira ocorrência do item que é passado como parâmetro|
|pop(index=-1)| Caso há argumento, remove o item na posição fornecida. Por padrão remove o último item.|

---

#### reverse()

O método de listas, `reverse()`, reverte a ordem dos objetos.


```python
>>> animais
['cachorro', 'tartaruga']
```

```python
>>> animais.reverse()
['tartaruga', 'cachorro']
```

---

#### sort(key=None, reverse=False)

O método `sort()` classifica os itens na lista em ordem crescente, usando a ordenação que se aplica "naturalmente" aos objetos na lista.

Por exemplo, como a lista `animais` contém objetos do tipo string, a ordem será lexicográfica (ordem do dicionário ou alfabética)

---


Para demonstrar vamos adicionar novos elementos.

```python
>>> animais.append('gato')
>>> animais.append('arara')
>>> animais.append('coelho')
```

```python
>>> animais
['tartaruga', 'cachorro', 'gato', 'arara', 'coelho']
```

```python
>>> animais.sort()
>>> animais
['arara', 'cachorro', 'coelho', 'gato', 'tartaruga']
```

---


Em uma lista de números, a ordem de classificação é numérica crescente.

```python
>>> frequencias = [4, 2, 8, 5]
>>> frequencias.sort()
>>> frequencias
[2, 4, 5, 8]
```

---


Podemos ordenar decrescentemente, utilizando o parâmetro `reverse` com o valor booleano `True`.

Por padrão, esse parâmetro é definido como `False`, já que por padrão as ordenações com `sort()` são do tipo `crescente`.

```python
>>> frequencias
[2, 4, 5, 8]
>>> frequencias.sort(reverse=True)
>>> frequencias
[8, 5, 4, 2]
```

---


#### Como ordenar uma lista aninhada?

Por exemplo, como ordenar a lista que armazena uma lista de nome de estudantes e suas respectivas notas?

```python
avaliacoes = [['Ana', 8], ['Amanda',9], ['Leonardo', 4]]
```

O método `sort()` irá ordenar pelo nome (ordenação lexicográfica) ou ordenação numérica por notas?

---

##### sort(key=None, reverse=False)

Por padrão o método `sort()` ordenará pelo primeiro item das listas ordenadas.

Ou seja, ordenará pelo elemento de índice zero de cada item da lista principal.

No nosso caso são strings, portanto a ordenação será lexicográfica.

```python
>>> avaliacoes = [['Ana', 8], ['Amanda',9], ['Leonardo', 4]]
>>> avaliacoes.sort()
[['Amanda', 9], ['Ana', 8], ['Leonardo', 4]]
```

Perceba que `['Amanda', 9]` está como primeiro item, diferente de `['Ana', 8]`, porque segundo a ordem de dicionário, `m < n`.

---

E se quisermos ordenar pelas notas de cada estudante?

---


 Nesse caso devemos fornecer uma função chave (`key fuction`) para direcionar a ordenação.

 Essa função é aplicada uma única vez para cada item da lista e é utilizada para classificá-lo na ordenação.

Para isso precisamos criar uma função, que no nosso caso irá receber cada lista aninhada, ou seja, cada item da lista mais externa.

Como queremos que cada lista aninhada seja ordenada pelo seu segundo item, temos que retornar justamente esse item em nossa função.

```python
def ordena_notas(lista_aninhada):
    return lista_aninhada[1] ## Segundo item (nota) de cada lista aninhada.
```

---



Utilizamos o parâmetro `key` do método `sort()`, é através desse parâmetro que passamos a nossa função que direcionará a classificação dos itens ma ordenação da lista.

```python
>>> avaliacoes
[['Amanda', 9], ['Ana', 8], ['Leonardo', 4]]
>>> avaliacoes.sort(key=ordena_notas)
>>> avaliacoes
[['Leonardo', 4], ['Ana', 8], ['Amanda', 9]]
```

Perceba que passamos apenas o nome da função, se "chamamento" ocorre quando a ordenação é executada comparada item a item (dentro do método `sort()`.

---


#### insert(index, object)

Vimos que podemos remover itens de uma lista passando um valor (`remove()`) ou um índice (`pop()`).

Para inserir temos, o método `append()`, que insere um novo item ao final da lista.

- Mas como inserir itens em outras posições da lista?

---


Nesse caso usamos o método `insert()`, que recebe como argumentos, um índice e um valor, respectivamente.

O primeiro argumento é o índice do elemento antes da inserção.

O segundo argumento é objeto ou valor que é será inserido.

---


Por exemplo, consideramos nossa lista de frequências.
```python
>>> frequencias
[8, 5, 4, 2]
```

Se queiramos que o novo item seja inserido entre o elemento `4` e o elemento `2`:

```python
>>> frequencias.insert(3, 6)
>>> frequencias
[8, 5, 4, 6, 2]
```

Antes da inserção o novo valor assume índice igual à 3.

---


Parece trivial, mas não tanto quando queremos fazer um `append()` usando `insert()`.

Para inserir na última posição, temos que passar como índice, uma valor que até então não está alocado.

```python
>>> frequencias.insert(5, 7)
>>> frequencias
[8, 6, 5, 4, 2, 7]
```
Perceba que nosso primeiro argumento não é igual ao nosso último índice existente antes da inserção.

---

#### extend(iterable)

Ainda sobre adicionar novos itens.

- Como faríamos para adicionar novos elementos ao final de uma lista, em uma única vez?

A resposta imediata seria: concatenando!

Vejamos...

----


Por exemplo,


```python
>>> letras = ['C', 'u', 'r', 's', 'o']
>>> linguagem = 'Python'
```

Como adicionar os elementos (letras) da string `'Python'` na lista `letras`?

Se tentarmos por concatenação, temos:
```python
>>> letras + linguagem
TypeError: can only concatenate list (not "str") to list
```

Temos um erro de tipo, não é possível concatenar tipos de objetos diferentes.

----


O tipo de objeto string é iterável, uma vez que toda string é um conjunto de elementos. Um espécie de estrutura de dados.

Podemos iterar sobre seus elementos, que chamamos de caracteres.

Em listas, possuímos um método específico que adiciona qualquer objeto iterável em Python à uma lista, veremos mais adiante outros objetos como listas que são iteráveis.

----


Esse método é o `extend` que recebe como argumento qualquer objeto iterável, e adiciona os elementos desse objeto à lista.

```python
>>> letras.extend(linguagem)
>>> letras
['C', 'u', 'r', 's', 'o', 'P', 'y', 't', 'h', 'o', 'n']
```

A lista foi "estendida" anexando elementos do objeto iterável.

---


#### index(value, start=0, stop=9223372036854775807)

O método `index()` devolve o índice (base-zero) do primeiro item cujo valor é igual ao passado como argumento.

Retorna "ValueError", se o valor passado não existe.

```python
>>> letras
['C', 'u', 'r', 's', 'o', 'P', 'y', 't', 'h', 'o', 'n']
>>> letras.index('z')
ValueError: 'z' is not in list
>>> letras.index('o')
4
```

---


Existe o conceito de fatiamento em objetos que indexáveis e iteráveis do tipo str e lst.

Uma fatia é um segmento, uma parte desses objetos.

O operador `[n:m]` retorna a parte da string ou lista do "enésimo" elemento ao "emésimo". Incluindo o primeiro e excluindo o último.

Se o primeiro índice for omitido, a fatia começa do início do objeto.

Se omitir o segundo índice, a fatia vai até o fim do objeto.

Se omitir ambos, a fatia é uma cópia.

---


Alguns exemplos:

```Python
>>> linguagem = 'Python'
>>> linguagem[0:2]
'Py'
>>> linguagem[:5]
'Pytho'
>>> linguagem[:6]
'Python'
>>> linguagem[:len(linguagem)]
'Python'
```
Perceba que o segundo índice do operador de fatiamento é excludente, e por isso para que a fatia seja o próprio "todo" é necessário passar o tamanho total e não o último índice (base-zero)

---


Mais alguns exemplos:

```Python
>>> animais
['tartaruga', 'cachorro', 'gato', 'arara', 'coelho']
>>> animais[2:]
['gato', 'arara', 'coelho']
>>> animais[0:4]
['tartaruga', 'cachorro', 'gato', 'arara']
>>> animais[5:5]
[] ## índices iguais equivalem ao objeto vazio.
>>> animais[0:15] ## Se o índice de fim for maior que o último índice,
['tartaruga', 'cachorro', 'gato', 'arara', 'coelho'] 
## A fatia equivale ao "todo". [n:m > len(object)] = [n:len(object)]
```

---


Podemos utilizar a referência com índices negativos

```Python
>>> animais
['tartaruga', 'cachorro', 'gato', 'arara', 'coelho']
>>> animais[2:-1]
['gato', 'arara']
>>> animais[-2:-1]
['arara']
>>> animais[-4:-2]
['cachorro', 'gato']
>>> animais[0:-2]
['tartaruga', 'cachorro', 'gato']
```

---


Os argumentos opcionais `start` e `end` são interpretados como nas noções de fatiamento que acabamos de ver.

São usados portanto, para limitar a busca para uma subsequência específica da lista.

```python
>>> letras
['C', 'u', 'r', 's', 'o', 'P', 'y', 't', 'h', 'o', 'n']
>>> letras.index('o')
4
>>> letras.index('o',5)
9
>>> letras.index('o',10,len(letras))
ValueError: 'o' is not in list
```

---

### Métodos de lista ou funções **sobre** listas 


Até agora vimos:

|Método|Descrição|
|-----|-----|
|append(object)| Novo elemento é acrescentado ao final da lista (como último item)|
|count(value)| Retorna o número de vezes que o argumento aparace como item|
|remove(value)| Remove a primeira ocorrência do item que é passado como parâmetro|
|pop(index=-1)| Caso há argumento, remove o item na posição fornecida. Por padrão remove o último item.|


---



Até agora vimos:

|Método|Descrição|
|-----|-----|
|reverse()| Reverte a ordem dos itens.|
|sort(key=None, reverse=False)|Ordena os itens decrescentemente ou crescentemente.|
|insert(index, object)| Insere um item na lista de acordo com o índice passado por argumento.|
|extend(iterable)|Adiciona os itens de um objeto iterável em uma lista.|

---



E por fim:

|Método|Descrição|
|-----|-----|
|index(value, start=0, stop=9223372036854775807)| Busca a primeira ocorrência do item, por seu valor e retorna seu índice. Podendo ou não fatiar a lista.|

---



