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
# Aula 05 - Expressões booleanas, Operadores Relacionais, Operadores Lógicos e Execução Condicional

Fundamentos de algoritmos e introdução à programação em Python

Prof. Everson Otoni


--
## Expressões booleanas 

Uma expressão booleana é uma expressão que pode ser verdadeira ou falsa.

Os exemplos seguintes usam o operador `==`, que **compara** dois operando e produz `True` se forem iguais e `False` se não forem

```python
>>> 5 == 5
True
>> 5 == 6
False
```

---


`True` e `False` são valores especiais que pertencem ao tipo booleano.

Não são strings.

```python
>>> type(True)
<class 'bool'>
>> type(False)
<class 'bool'>
```

---

### Operadores relacionais

Dentre os **operadores relacionais**, temos:

O operador `==`, que compara se dois valores são iguais.

O operador `!=`, que compara se dois valores são diferentes.

O operador `>`, que compara se um valor é maior a outro.

O operador `<`, que compara se um valor é menor a outro.

O operador `>=`, que compara se um valor é maior ou igual a outro.

O operador `<=`, que compara se um valor é menor ou igual a outro.

---


Alguns símbolos do Python são diferentes dos símbolos matemáticos.

Um erro comum é usar apenas um sinal de igual (=) em vez de um sinal duplo (==).

`=` é um sinal de atribuição e `==` é um operador relacional.

---

### Operadores lógicos

Há três **operadores lógicos**: `and`, `or` e `not`. 

Sua semântica é referente ao significado em inglês.

Por exemplo, 

`x > 0 and x < 10` só é verdade (`True`) se x for maior que 0 `e` menor que 10.

`n % 2 == 0 or n % 3 == 0` é verdadeiro (`True`) se *uma ou as duas* condição(ões) for(em) verdadeira(s), isto é, se o número for divisível por 2 `ou` 3.

`not (x > y)` é verdade (`True`) se x > y for falso, isto é, se x for `menor que ou igual a` y. 
O operador `not` nega uma expressão booleana.

---


O Python não é muito estrito com os operandos dos operadores lógicos.

E aceita qualquer número que não seja zero como `True`.

Essa característica possui sua utilidade, mas há sutilezas que podem ser confusas. 

Portanto use com moderação.


---

## Execução condicional

Para escrever programas, quase sempre precisamos da capacidade de **verificar condições** e mudar o comportamento do programa de acordo com essas condições.

É por meio das **instruções condicionais** que essa capacidade é possível.

A forma mais simples de uma instrução desse tipo é a instrução `if` ("Se", em português).

---

## Execução condicional

```python
>>> if x > 0:
...     print('x é positivo')
...
```

Perceba que há um expressão booleana (`x > 0`) após o `if`. Ela é chamada de **condição**. 

Perceba também que a instrução após a condição é endentada e delimitada por `:`.

Isso significa que assim como a função, aqui também temos um escopo de existência.

Ou melhor, todas as instruções endentadas após a condição, só serão executadas se a condição for verdadeira (possuir valor `True`)

---

### Execução alternativa

A execução alternativa (else ou "senão ou caso contrário") é utilizada quando há duas possibilidades e a condição determina qual será executada.

```python
>>> if num % 2 == 0:
...     print('É par')
... else:
...     print('É impar')
...
```

Se o resto quando num for dividido por 2 for 0, então sabemos que x é par e o programa exibe a uma mensagem para par.

Se a condição for falso, o segundo conjunto de instruções é executado. Logo x é impar e uma mensagem de acordo é exibida.

Como há apenas duas possibilidade para uma condição, ou verdadeira ou falsa, exatamente uma das alternativas será executada. Essas duas alternativas são ramos no fluxo de execução.

---

Meio limitante apenas duas opções, não?

---

## Condicionais encadeadas

As vezes, há mais de duas possibilidades e precisamos de mais de dois ramos no fluxo de execução.

Podemos utilizar condicionais encadeadas (no sentindo de interligadas).

```python
>>> if x < y:
...     print('x é menor que y <=> y é maior que x')
... elif x > y
...     print('x é maior que y <=> y é menor que x')
... else:
...     print('x é igual à y <=> y é igual à x')
...
```

`elif` é uma abreviatura de "else if" (caso contrário, se)

---

### elif

É importante notar, que cada condição é verificada em ordem.

Se uma delas for verdadeira, o ramo correspondente é executado e a instrução é encerrada.

Mesmo, se por acaso, mais de uma condição for verdade, só o primeiro ramo verdadeiro é executado.


---
## Condicionais aninhadas

Condicionais podem ser aninhados (dentro) de outros condicionais.

Por exemplo,


```python
>>> if x == y:
...     print('x é igual à y <=> y é igual a x')
... else:
...     if x < y:
...         print('x é menor que y <=> y é maior que x')
...     else:
...         print('x é maior que y <=> y é menor que x')
...
```

O condicional mais externo, possui dois ramos.
O primeiro ramo contém uma instrução simples **(if)**.
O segundo ramo contém mais duas instruções internas, onde inclusive uma delas, possui uma outra instrução condicional.

---



 Embora seja possível, **condicionais aninhadas** são difíceis de ler rapidamente.

 É uma boa ideia evitá-las quando for possível.

Os operadores lógicos muitas vezes oferecem uma resolução mais simples para instruções aninhadas.

---




Usando condicionais aninhadas

```python
>>> if x > 0:
...     if x < y:
...         print('x é um número positivo de um único dígito')
...
```

Usando operadores lógicos

```python
>>> if x > 0 and x < 10:
...     print('x é um número positivo de um único dígito')
...
```

---

