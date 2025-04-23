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
# Aula 10 - Instrução For
Fundamentos de algoritmos e introdução à programação em Python 

Prof. Everson Otoni

---

## Iteração - Instrução For

Uma tarefa comum a todas as sequências é realizar uma ação sobre cada objeto.

Por exemplo, poderíamos percorrer uma lista de compras para verificar se comprou tudo o que está nela.

Poderíamos percorrer uma lista de filmes (serviço de streaming) e verificar se foram assistidos ou não, ou se são de determinado gênero ou não.

Podemos também percorres um nome a fim de soletrá-lo.

---


Como podemos implementar um programa que soletre um string digitada pelo usuário?

Algo como:

```Python
>>>
Digite uma palavra: Ariel
A palavra soletrada:
A
r
i
e
l
```

---


Precisamos de um método que nos permitirá executar uma instrução `print()` para cada caractere da string.

Para isso iremos utilizar a instrução de laço `for`.


```Python
palavra = input('Digite uma palavra: ')
print('A palavra soletrada: ')

for caractere in palavra:
    print(caractere)
```

---


```Python
>>> for caractere in palavra:
...     print(caractere)
...
```

`caractere` é um nome de variável.

A instrução de laço `for` atribuirá repetidamente os caracteres (itens) da string `palavra` à variável `caractere`.

Se a palavra for a string `'Ariel'`, `caractere` primeiro terá o valor `'A'`, depois `'r'`, depois `'i'`, depois `'e'` e por fim `'l'`.

Para cada valor de `caractere`, a instrução endentada `print(caractere)` é executada.

---



---


O laço `for` portanto percorre os itens de uma lista.

Por exemplo, para percorrer os objetos de string representando os animais de estimação:

```Python
>>> animais = ['peixe', 'gato', 'cachorro']
>>> for animal in animais:
...     print(animal)
...
peixe
gato
cachorro
```

O laço `for` executa a seção endentada `print(animal)` três vezes, uma para cada valor de animal.

O valor é primeiro `peixe`, depois `gato` e, por fim `cachorro`.


---


## A variável do Laço for

A variável `caractere` em

```Python
>>> for caractere in palavra:
...     print(caractere)
...
```

E a variável `animal` em

```Python
>>> for animal in animais:
...     print(animal)
...
```

---

## Iteração - Instrução For


São apenas nomes de variável, escolhidos para tornar o programa mais significativo. Poderíamos ter escrito os laços da mesma com, digamos, o nome de variável `x`:

```Python
>>> for x in palavra:
...     print(x)

>>> for x in animais:
...     print(x)
```

Ao mudarmos o nome da variável do laço `for`, também precisamos mudar qualquer ocorrência dela no corpo do laço `for`.

---


```Python
for <variável> in <sequência>:
    <bloco de código endentado>
<bloco de código não endentado>
```

O laço `for` atribuirá com sucesso objetos de <sequência> à <variável>, na ordem em que aparecem da esquerda para a direita.

O <bloco de código endentado>, normalmente denominado `corpo` do laço `for`, é executado uma vez para cada valor de <variável>.

Dizemos que o laço `for` percorre os objetos na sequência.

Após o <bloco de código endentado> ter sido executado pela última vez, a execução retoma com as instruções após laço `for`.

E o <bloco de código não endentado> é executado.

---


Vamos combinar o laço `for` com uma instrução `if`.

Nossa proposta é escrever uma aplicação que comece pedindo ao usuário para digitar uma frase.

Depois que ele fizer isso, o programa exibirá todas as vogais, e nenhuma outra letra.\

```Python
>>>
Digite uma frase: caso de teste
a
o
e
e
e
```

---


- Precisamos de uma instrução `input()` para ler a frase.
- Um laço `for` para percorrer os caracteres da string de entrada 
- E, cada iteração do laço, uma instrução `if` para verificar se o caractere atual é uma vogal. Se for, ele é impresso.

---

## Função range(stop) ou range(start, stop, step=1)

Com frequência necessitamos percorrer uma sequência de números em determinado intervalo, mesmo que a lista de números não seja dada explicitamente.

Seus argumentos devem ser sempre inteiros.

Se o argumento `step` for omitido, será usado o padrão 1.

Se o argumento `start` for omitido, será usado o padrão 0.

Se step for zero, uma exceção `ValueError` será retornada.

---


A função `range(n)` normalmente é usada para percorrer a sequência de inteiros `0, 1, 2, ..., n - 1.1

```Python
>>> for i in range(10):
...     print(i)
...
0
1
2
3
4
5
6
7
8
9
```

---


Se quisermos que a sequência comece em determinado número diferente de zero `start` (início) e termine **antes** do número `stop` (fim):
```Python
>>> for i in range(1,11):
...     print(i)
...
1
2
3
4
5
6
7
8
9
10
```

---


Podemos percorrer a sequência de inteiros começando em `start` (ínicio), usando um tamanho de `step` (passo) e terminando antes do número `stop` (fim).

```Python
>>> for i in range(0, 30, 5):
...     print(i)
...
0
5
10
15
20
25
```

---


```Python
>>> for i in range(0, -10, -1):
...     print(i)
...
0
-1
-2
-3
-4
-5
-6
-7
-8
-9
```

---



A função range não gera uma lista e sim uma sequência numérica. Mais especificamente, progressões aritméticas.

Portanto se comporta como uma lista, mas na verdade não é.

---



A vantagem do tipo `range` sobre um `list`, por exemplo é que um objeto `range` sempre terá a mesma quantidade (pequena) de memória, não importa o tamanho do intervalo o mesmo esteja representado, já que ele apenas armazena os valores `start`, `stop` e `step`, calculando itens individuais e subintervalos conforme necessário).

---


Podemos gerar listas de sequências numéricas, utilizando o `range` e a função embutida que converte em lista (`list`).

```Python
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

```Python
>>> list(range(1,11))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

```Python
>>> list(range(0,30,5))
[0, 5, 10, 15, 20, 25]
```

```Python
>>> list(range(0, -10, -1))
[0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
```

---

## Padrões de uso - Laço de Iteração 

Já usamos o laços para apenas percorrer os caracteres de uma string:

```Python
>>> palavra = 'Ariel'
>>> for caractere in palavra:
... print(caractere)
...
A
r
i
e
l
```

---


Já usamos o laços para apenas percorrer os itens de uma lista:

```Python
>>> animais = ['peixe', 'gato', 'cachorro']
>>> for animal in animais:
...     print(animal)
...
peixe
gato
cachorro
```

---



Percorrer uma sequência explícita de valores e realizar alguma ação sobre cada valor é o padrão de uso mais simples para um laço, porém muito mais simples para um laço `for` do que um laço `while`.


```Python
>>> frutas = ['banana', 'maça', 'pera', 'laranja']
>>> indice = 0
>>> while indice < len(frutas):
...     fruta = frutas[indice]
...     print(fruta)
...     indice = indice + 1
...
banana
maça
pera
laranja
```
---


Esse loop atravessa a lista de frutas e exibe cada fruta sozinha em uma linha.

A condição do loop é `index < len(frutas)`.

Quando `indice` é igual ao comprimento da lista, a condição é falsa e o corpo do loop não é mais executado.
O último item acessado é aquele com índice `len(frutas) - 1`, que é o útimo item na lista.

---


Para percorerr os itens de uma lista e exibi-los usando for:


```Python
>>> for fruta in frutas:
...     print(fruta)
...
banana
maça
pera
laranja
```

---

## Padrões de uso - Laço Contador

Outro padrão de laço que podemos usar é a repetição por uma sequência de inteiros, especificada com a função `range()`:


```Python
>>> for numero in range(10):
...     print(numero, end=' ')
...     0 1 2 3 4 5 6 7 8 9
...
```

Usamos esse padrão, quando precisamos executar um bloco de código para cada inteiro em algum intervalo (range).

---

Por exemplo, para encontrar e exibir todos os números pares de 0 até algum inteiro qualquer:

```Python
>>> limite = 10
>>> for numero in range(10):
...     if numero % 2 == 0:
...         print(numero, end = ' ')
...
0 2 4 6 8
```

---

## Padrões de uso - Laço Acumulador

Um padrão comum nos laços é acumular "alguma coisa" em cada iteração do laço.

Dada uma lista de números, por exemplo, poderíamos querer somar os números.

Para fazer isso usando um laço `for`, primeiro precisamos introduzir uma variável que manterá a soma. Essa variável é inicializada em 0; depois, um laço `for` pode ser usado para percorrer os números da lista e somá-los a variável.

```Python
>>> pontuacao = [3, 2, 7, -1, 9]
>>> minhaSoma = 0 ## Inicializando o acumulador
>>> for numero in pontuacao:
...     minhaSoma = minhaSoma + numero
...
>>> minhaSoma
20
```

---

---


