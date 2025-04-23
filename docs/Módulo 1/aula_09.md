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
# Aula 09 - Métodos de lista

Fundamentos de algoritmos e introdução à programação em Python 

Prof. Everson Otoni

---

## Métodos de lista ou funções **sobre** listas 

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

### reverse()

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

### sort(key=None, reverse=False)

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


### Como ordenar uma lista aninhada?

Por exemplo, como ordenar a lista que armazena uma lista de nome de estudantes e suas respectivas notas?

```python
avaliacoes = [['Ana', 8], ['Amanda',9], ['Leonardo', 4]]
```

O método `sort()` irá ordenar pelo nome (ordenação lexicográfica) ou ordenação numérica por notas?

---

#### sort(key=None, reverse=False)

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


### insert(index, object)

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

### extend(iterable)

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


### index(value, start=0, stop=9223372036854775807)

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

## Métodos de lista ou funções **sobre** listas 


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


