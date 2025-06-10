# Aula 09 - Dúvidas, Revisão e Pensamento Recursivo

{% set aula = "09" %}
{% set link = "ehMnhND4wOg" %}
{% set objetivos = 
[
  "Revisar operadores relacionais, lógicos e estruturas condicionais da Aula 07",
  "Consolidar o entendimento da recursão por meio da função exibe_numero_vertical",
  "Distinguir com clareza o caso básico e a etapa recursiva em funções recursivas",
  "Aprofundar o pensamento recursivo como prática de resolução de problemas"
]

%}
{% include "templates/cabecalho.md" %}


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
 <!--
## Chamadas de Função Recursivas e a Pilha de Programa

O que acontece quando uma função de recursão é executada?
 -->


