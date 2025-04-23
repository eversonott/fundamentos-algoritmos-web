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


