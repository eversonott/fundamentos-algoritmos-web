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
# Recursividade

## Recursão

Já vimos que uma função pode chamar outra.

Mas uma função pode chamar a si mesma.

Pode não ser óbvio, mas esse é um dos recursos computacionais muito utilizado em programação e não é apenas uma chamada de função diferente da usual.

---

A recursão é uma **técnica** de solução de problemas que expressa a solução para um problema em termos de soluções para **subproblemas do problema original**.

Como já mencionado, as funções desenvolvidas solucionando um problema recursivamente chamarão a si mesmas, e nos referimos a elas como **funções recursivas**.

Enquanto discutimos quando a recursão deve ou não ser usada, aparece a questão do **tempo de execução do programa**.
Até agora, não nos preocupamos muito com a eficiência de nossos programas. A recursividade muda isso.


---

## Funções Recursivas

Exemplo de um função que chama a si mesma:

```python
>>> def contagem_regressiva(numero):
...     print(numero)
...     contagem_regressiva(numero - 1)
...
```

Perceba que na **implementação** da função `contagem_regressiva`, a própria função `contagem_regressiva` é **chamada**.

Portanto, a função `contagem_regressiva` chama a si mesma. Logo, trata-se de uma **chamada recursiva**.

--- 


```python
>>> def contagem_regressiva(numero):
...     print(numero)
...     contagem_regressiva(numero - 1)
...
```
Qual é o comportamento dessa função, se executarmos a chamada de função `contagem_regressiva(3)` ?

```python
>>> contagem_regressiva(3)
```
---


```python
>>> def contagem_regressiva(numero):
...     print(numero)
...     contagem_regressiva(numero - 1)
...
```

- Quando executamos `contagem_regressiva(3)`: 
    - A entrada 3 é exibida.
    - `contagem_regressiva()` é chamada sobre a entrada decrementada uma unidade, ou seja, 3 - 1 = 2
    - Continuamos rastreando a execução `contagem_regressiva(2)`.


---


```python
>>> def contagem_regressiva(numero):
...     print(numero)
...     contagem_regressiva(numero - 1)
...
```

- Quando executamos `contagem_regressiva(2)`: 
    - A entrada 2 é exibida.
    - `contagem_regressiva()` é chamada sobre a entrada decrementada uma unidade, ou seja, 2 - 1 = 1
    - Continuamos rastreando a execução `contagem_regressiva(1)`.


---


```python
>>> def contagem_regressiva(numero):
...     print(numero)
...     contagem_regressiva(numero - 1)
...
```

- Quando executamos `contagem_regressiva(1)`: 
    - A entrada 1 é exibida.
    - `contagem_regressiva()` é chamada sobre a entrada decrementada uma unidade, ou seja, 1 - 1 = 0
    - Continuamos rastreando a execução `contagem_regressiva(0)`.

---


```python
>>> def contagem_regressiva(numero):
...     print(numero)
...     contagem_regressiva(numero - 1)
...
```

- Quando executamos `contagem_regressiva(0)`: 
    - A entrada 0 é exibida.
    - `contagem_regressiva()` é chamada sobre a entrada decrementada uma unidade, ou seja, 0 - 1 = -1
    - Continuamos rastreando a execução `contagem_regressiva(-1)`.

---


- Quando executamos `contagem_regressiva(-1)`:
    - ...

Parece que a execução nunca terminará.

---


Vamos verificar:

```python
>>> contagem_regressiva(3)
3
2
1
0
-1
-2
...
```

O comportamento da função é fazer a contagem regressiva, começando com o número da entrada original.

---


Se "deixarmos" a chamada de função `contagem_regressiva(3)` executar por um tempo, obteremos:

```python
>>> contagem_regressiva(3)
...
-2
...
-994
-995
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in contagem_regressiva
  File "<stdin>", line 3, in contagem_regressiva
  File "<stdin>", line 3, in contagem_regressiva
  [Previous line repeated 996 more times]
RecursionError: maximum recursion depth exceeded
```

---


Temos diversas linhas de mensagem de erro, e somos informados que a **profundidade máxima de recursão foi excedida**.

A execução estava seguindo **indefinidamente**, mas o interpretador Python parou com isso.

O ponto principal a se entender aqui, é que uma **função recursiva** chamará a si mesma **indefinidamente**, a menos que modifiquemos a função de modo que haja uma **condição de parada**.

---


Suponha que o comportamento que queríamos alcançar com a função `contagem_regressiva` fosse:

```python
>>> contagem_regressiva(3)
3
2
1
Lançar!!!
```

```python
>>> contagem_regressiva(1)
1
Lançar!!!
```

```python
>>> contagem_regressiva(0)
Lançar!!!
```
---


```python
>>> contagem_regressiva(3)
3
2
1
Lançar!!!
```

A função `contagem_regressiva()` deverá contar até 0, começando de uma entrada informada;

Quando 0 (zero) for alcançado, o texto `Lançar!!!` deverá ser apresentado.

---


Para implementar essa versão de `contagem_regressiva()`, consideramos dois casos que dependem do valor da entrada:
- Quando a entrada `numero` é 0 (zero) ou negativa.
    - Chamamos esse caso de **`caso básico`** da recursão.
    - Essa é condição que garantirá que a função recursiva **não irá chamar a si mesma indefinidamente**.
- Quando a entrada `numero` é positiva.
    - Executará a mesma coisa de antes.


---


Temos então:

```python
>>> def contagem_regressiva(numero):
...     if numero <= 0:                 ## caso básico
...         print('Lançar!!!')          
...     else:                                       ## numero > 0 (positivo): etapa recursiva                   
...         print(numero)                           ## exibe numero primeiro
...         contagem_regressiva(numero - 1)         ## regride a partir de numero - 1
...
```

---


Uma função recursiva que termina sempre terá:
- Um ou mais casos básicos, que oferecem a condição de término para a recursão.
    - Na função `contagem_regressiva()`, o caso básico é a condição `numero <= 0`, em que `numero` é a entrada.

- Uma ou mais chamadas recursivas, que precisam estar nos argumentos que ficam "mais próximos" do caso básico do que a entrada da função.
    - Na função `contagem_regressiva()`, a única chamada recursiva é feita sobre `numero - 1`, que está "mais próxima" do caso básico do que a entrada `numero`.

---


O significado de "mais próximo" depende do problema resolvido pela função recursiva.

A ideia é que cada chamada recursiva seja feita sobre entradas do problema que estejam mais próximas do caso básico.
Isso garante que as chamadas recursivas, por fim, cheguem ao caso básico que encerrará a execução.

---


Para desenvolver funções recursivas, é necessário aprender a pensar recursivamente.

Ou seja, descrever a solução de um problema em termos de soluções de seus subproblemas.

---

## Pensamento Recursivo

Precisamos desenvolver uma função recursiva `exibe_numero_vertical()`, que aceita um número inteiro não negativo como entrada e exibe seus dígitos empilhados verticalmente. Por exemplo:

```python
>>> exibe_numero_vertical(3124)
3
1
2
4
```

---


1. Precisamos definir o caso básico da recursão
    - Podemos fazer isso respondendo à pergunta: 
    `Quando o problema de exibir verticalmente é fácil?`
    `Para que tipo de número inteiro não negativo?`
        - Certamente o problema é fácil, quando a entrada tiver apenas um dígito.
        - Nesse caso exibimos a própria entrada.

```python
>>> exibe_numero_vertical(6)
6
```

---


1. (continuação). Tomamos a decisão de que o caso básico é quando temos: 
`numero <  10`, logo:

```python
>>> def exibe_numero_vertical(numero):
...     if numero < 10:             ## Caso Básico: numero tem 1 dígito.
...         print(numero)          
...     else:                       ## Etapa recursiva: numero tem 2 ou mais dígitos.                 
...         ...         ## Restante da função.
...
```

---


Temos então, a função `exibe_numero_vertical()` que exibe `numero` se este for menor que 10 (ou seja, se `numero` for um número de único dígito:

```python
>>> exibe_numero_vertical(4):
4
```

```python
>>> exibe_numero_vertical(15):
>>> 
```

---


2. Consideramos agora o caso em que a entrada `numero` tem dois ou mais dígitos.
    - Nesse caso gostaríamos de quebrar o problema de exibição vertical do número em subproblemas "mais fáceis".
    - Esses subproblemas precisam envolver, necessariamente, a exibição de números "menores" que a entrada original `numero`.
        - Nesse problema "menor" deverá nos levar para mais perto do caso básico, um número de único dígito.
        - Isso sugere que nossa chamada recursiva deverá ser sobre um número que tenha menos dígitos que a entrada original.

---


Por exemplo, para `numero` com dois dígitos, quebramos o problema:
a. Exibir verticalmente o número obtido removendo o último dígito. Esse número é "menor" porque tem menos um dígito.
- Para `numero = 3124`, isso significaria chamar a função `exibe_numero_vertical()` sobre 312.
b. Exibir o último dígito. Para `numero = 3124`, isso significa exibir 4.

---


Lembra dos últimos operadores que aprendemos?

O último número pode ser obtido, utilizando o operador módulo (%):

```python
>>> numero = 3124
>>> numero % 10
4
```

Podemos "remover" o último dígito, usando o operador de divisão inteira (//):

```python
>>> numero = 3124
>>> numero // 10
312
```

Agora podemos escrever a função recursiva completa.

---


```python
>>> def exibe_numero_vertical(numero):
...     if numero < 10:             ## Caso Básico: numero tem 1 dígito.
...         print(numero)               ## Exibe número.
...     else:                       ## Etapa recursiva: numero tem 2 ou mais dígitos.                 
...         exibe_numero_vertical(numero // 10)     ## Exibe recursivamente todos menos o último dígito.
...            
...         print(numero % 10)                      ## Exibe último dígito.
...
```

```python
>>> exibe_numero_vertical(3124)
3
1
2
4
```

---

### Resumo

1. Primeiro, decida sobre o caso básico ou casos do problema que podem ser resolvidos diretamente, sem recursão.

2. Descubra como quebrar o problema para que sejam mais próximos do caso básico;
Os subproblemas devem ser resolvidos recursivamente. As soluções para os subproblemas são usadas para construir a solução do problema original.

---

## Chamadas de Função Recursivas e a Pilha de Programa

O que acontece quando uma função de recursão é executada?




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


