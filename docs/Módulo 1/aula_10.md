# Aula 10 - Introdução à iteração: instrução while, break e continue

{% set aula = "10" %}
{% set link = "KPdA7La-yJg" %}
{% set objetivos = 
[
  "Compreender o conceito de iteração e utilizar a instrução `while` em Python",
  "Aplicar reatribuições, atualizações e atribuições aumentadas em variáveis",
  "Utilizar `break` e `continue` para controlar o fluxo de execução em laços",
  "Construir algoritmos com somatórias, contagens e condições de parada dinâmicas",
  "Implementar métodos iterativos como o de Newton para aproximação de raízes"
]
%}
{% include "templates/cabecalho.md" %}

## Iteração

É a capacidade de executar um bloco de instruções repetidamente.

Vimos iteração, usando a recursividade.



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


Perceba que uma atribuição não é uma igualdade matemática.

Interpretar `a = b` como iguais é equivocado, na verdade o valor de `b` é atribuído a variável de nome "a". Porém a relação simétrica da igualdade não é válida, uma vez que um valor não pode ser atribuído à um nome.

```python
>>> 7 = x
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
```




Em matemática, uma proposição de igualdade é *verdadeira* ou *falsa* "para sempre".

Em Python, uma instrução de atribuição pode tornar duas variáveis iguais, mas elas não precisam se manter assim:


```python
>>> a = 5
>>> b = a # Agora "a" e "b" são iguais.
>>> a = 3 # A variável "b" possui o mesmo valor da variável "a"
>>> b
5
```

A terceira linha modifica o valor de *a*, mas não muda o valor de *b*, então após a terceira linha elas já não são iguais.



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
subtrair 1 chama-se **decremento**.



## Instrução While

Os computadores muitas vezes são usados para automatizar tarefas repetitivas

Em um programa de computador, a repetição também é chamada de **iteração**.

Vimos que usando condicionais, executamos um bloco de código quando uma certa condição é verdadeira.




Assim como em condicionais, a instrução `while` executa o bloco de código se a condição é verdadeira. Porém depois que o bloco é executado o programa **volta** a verificar se a condição é verdadeira. Se for, então o bloco é executado novamente.

Quando a condição for avaliada como falsa, então a execução "salta" para a instrução não endentada.

### Incremento simples

Vamos criar uma função `incremento_simples()` que imprime os números de 1 a 5 usando um laço `while`. A função não recebe parâmetros e imprime os números em linhas separadas.

```py
def incremento_simples():
    x = 1
    while x < 6:
        print(x)
        x = x + 1
# A saída será 1,2,3,4,5. Demonstra reatribuição básica no laço.
```

<iframe width="800" height="500" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=def%20incremento_simples%28%29%3A%0A%20%20%20%20x%20%3D%201%0A%20%20%20%20while%20x%20%3C%206%3A%0A%20%20%20%20%20%20%20%20print%28x%29%0A%20%20%20%20%20%20%20%20x%20%3D%20x%20%2B%201%0A%0Aincremento_simples%28%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=20&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>

Perceba que apenas quando `x = 6`, é verificado que `6 < 6 = False` (passo 21) e a execução "sai" do `while`.




### Contador decrescente
Crie uma função `contador_decrescente()` que imprime os números de 5 até 0 em ordem decrescente. 
Use um laço `while` e decremento.

```py
def contador_decrescente():
    n = 5
    while n >= 0:
        print(n)
        n = n - 1
    #  Imprime 5,4,3,2,1,0. Ensina decremento e condição de parada.
```

### Atribuições

Já vimos que as instruções de atribuição são usadas para (re)vincular 
nomes a valores e modificar atributos ou itens de objetos mutáveis:

A mais frequente e comumente usada é a instrução de atribuição 
básica.

Neste tipo de atribuição, atribuiremos o valor diretamente à 
variável.


<span style="color:#B87333;">nome_objeto</span> = <span style="color:#4A5D23;"> valor</span>


#### Atribuição aumentada

A atribuição aumentada é a combinação, em uma única instrução, de uma
operação binária e uma instrução de atribuição:

Uma instrução de atribuição aumentada como `x -= 1` pode ser 
reescrita como `x = x - 1` para obter um efeito semelhante, mas não 
exatamente igual. 


Na versão aumentada, `x` é avaliado apenas uma vez.


Além disso, quando possível, a operação real é executada no local, o 
que significa que, em vez de criar um novo objeto e atribuí-lo ao 
alvo, o objeto antigo é modificado.


Ao contrário das atribuições normais, as atribuições aumentadas 
avaliam o lado esquerdo antes de avaliar o lado direito. 

Por exemplo, `a += f(x)` primeiro procura `a`, então avalia `f(x)` e 
executa a adição e, por último, escreve o resultado de volta para a.

Como temos qualquer operação binária associada com a instrução 
aumentada, teremos:

##### Atribuição de adição (+=)


###### Atribuição normal/básica

```py
a = 10
a = a + 5
# Saída: 15
```

###### Atribuição aumentada

```py
a = 10
a += 5 
# Saída: 15
```


##### Atribuição de subtração (-=)

###### Atribuição normal/básica

```py
b = 20
b = b - 4
# Saída: 16
```

###### Atribuição aumentada

```py
b = 20
b -= 4
# Saída: 16
```

##### Atribuição de multiplicação (*=)

###### Atribuição normal/básica

```py
c = 12
c = c * 5
# Saída: 60
```

###### Atribuição aumentada

```py
c = 12
c *= 5
# Saída: 60
```

##### Atribuição de divisão (/=)

###### Atribuição normal/básica

```py
d = 21
d = d / 3
# Saída: 7
```

###### Atribuição aumentada

```py
d = 21
d /= 3
# Saída: 7
```


### Laço sem executar
Crie uma função `laco_sem_execucao()` que utiliza um laço `while` com condição falsa desde o início. Verifique que nada será impresso.

Por exemplo:

```py
def laco_sem_execucao():
    x = 10
    while x < 5:
        print("Não vai aparecer")
```
Perceba que nada é impresso. 

Isso mostra que `while` verifica antes.

Parece trivial, mas há muita confusão com a última iteração e 
condição quando é falsa.


### Soma de 1 a 10
Crie uma função `soma_1_a_10()` que retorna a soma dos números de 1 
até 10 utilizando um laço `while`.

```py
def soma_1_a_10():
    soma_progressiva = 0
    numero_atual = 1

    while numero_atual <= 10:
        soma_progressiva += numero_atual
        numero_atual += 1

    print(soma_progressiva)

# Retorna 55. É soma de 1 a 10 com acumulador (soma progressiva).
```



#### O que é uma **somatória**?

Na matemática, a **somatória** é uma forma compacta de escrever a soma de vários termos seguindo uma **regra**.

A notação mais comum é:

$$
\sum_{i=a}^{b} f(i)
$$

Onde:

* $\sum$ é o símbolo de soma (sigma)
* $i$ é a **variável de controle** (como um contador)
* $a$ é o valor **inicial**
* $b$ é o valor **final**
* $f(i)$ é a **expressão** que define o que somar (ex.: $i$, $i^2$, $2i$, etc.)

---

#### E o código em Python?

```python
soma_progressiva = 0
numero_atual = 1

while numero_atual <= 10:
    soma_progressiva += numero_atual
    numero_atual += 1

print(soma_progressiva)
```

---

#### Agora, vamos relacionar cada parte do código com a notação matemática:

| Elemento da somatória matemática | Parte equivalente no código Python | Função                               |
| -------------------------------- | ---------------------------------- | ------------------------------------ |
| $\sum$                           | `soma_progressiva += ...`          | Acumula o valor a cada passo         |
| $i = 1$ (início do índice)       | `numero_atual = 1`                 | Inicializa o contador                |
| $i \leq 10$ (limite final)       | `while numero_atual <= 10:`        | Define a condição de parada          |
| $i \leftarrow i + 1$             | `numero_atual += 1`                | Atualiza o índice a cada passo       |
| $f(i) = i$                       | `soma_progressiva += numero_atual` | Soma o valor atual de `i` à variável |
| resultado da soma                | `print(soma_progressiva)`          | Mostra o valor acumulado ao final    |

---


!!! warning "Conclusão:" 
    A somatória é como um **loop** que começa de um número inicial, soma cada valor calculado pela **regra da função**, e **para quando chega no valor final**. O que a matemática escreve com $\sum$, a programação escreve com `while`, `for` (veremos em breve), `+=` e variáveis.

---

#### Exemplo:

**Somatória matemática:**

$$
\sum_{i=1}^{4} i = 1 + 2 + 3 + 4 = 10
$$

**Código equivalente:**

```python
soma = 0
i = 1
while i <= 4:
    soma += i
    i += 1
print(soma)  # saída: 10
```

---



A ligação entre código e notação matemática é muito clara quando pensamos que:

* O **índice da somatória** vira o **contador da repetição**.
* O **limite inferior e superior** da somatória viram a **condição do loop**.
* A **função $f(i)$** é o que está sendo **acumulado** no código.
* E o **símbolo de somatório $\sum$** é substituído por um **acumulador** com `+=`.

---


Se variarmos **a regra da somatória**, podemos criar algoritmos inspirados no original, mudando:

- 🔁 **O intervalo** (início e fim)
- ➕ **A função de soma** (quadrado, cubo, pares, ímpares, múltiplos, etc.)
- ➕ **O passo do incremento**

---

#### Exemplos de variações com base no algoritmo inicial


##### 1. Somar os **números pares de 2 a 20**
\[
\sum_{i=2,4,\dots,20} i
\]

```python
soma_progressiva = 0
numero_atual = 2

while numero_atual <= 20:
    soma_progressiva += numero_atual
    numero_atual += 2  # passo 2 para pular ímpares

print(soma_progressiva)
```

---

##### 2. Somar os **quadrados** dos números de 1 a 5
\[
\sum_{i=1}^{5} i^2 = 1^2 + 2^2 + 3^2 + 4^2 + 5^2
\]

```python
soma_progressiva = 0
numero_atual = 1

while numero_atual <= 5:
    soma_progressiva += numero_atual ** 2
    numero_atual += 1

print(soma_progressiva)
```

---

##### 3. Somar os **múltiplos de 3** de 3 até 30
\[
\sum_{i=3,6,\dots,30} i
\]

```python
soma_progressiva = 0
numero_atual = 3

while numero_atual <= 30:
    soma_progressiva += numero_atual
    numero_atual += 3

print(soma_progressiva)
```

---

##### 4. Somar os números de **10 a 1 (decrescente)**
\[
\sum_{i=10}^{1} i
\]

```python
soma_progressiva = 0
numero_atual = 10

while numero_atual >= 1:
    soma_progressiva += numero_atual
    numero_atual -= 1

print(soma_progressiva)
```

---

#### Moral da história

O algoritmo original é um **modelo base de somatória**, e qualquer **função somatória** pode ser implementada variando:

- O **intervalo de varredura** (`inicio`, `fim`)
- A **função aplicada a cada termo** (ex: \(i\), \(i^2\), \(2i\))
- O **incremento ou passo** (1, 2, 3, etc.)

!!! warning "Faça você mesmo!" 
    Agora construa uma **função genérica** de somatória com esses parâmetros.


```Python
def contagem_regressiva(numero):
    while numero > 0:
        print(numero)
        numero = numero - 1
    print('Lançar')
```

Podemos ler a instrução `while` como "enquanto".


1. Determine se a condição é verdadeira ou falsa.
2. "Enquanto" a condição for verdadeira, execute o bloco de código e então volte "ao `while`".
3. Se for falsa, saia da instrução `while` e continue a execução, seguindo um fluxo linear.


Esse tipo de fluxo chama-se loop, porque o terceiro passo faz um volta (loop) de volta ao topo.

!!! warning ""
    Perceba que, o corpo do loop deve mudar o valor de uma ou mais variáveis para que, a certa altura, a condição fique falsa e o loop termine.

Senão o loop vai se repetir para sempre, e teremos um **looop infinito**




Um laço `while` é perfeito para situações em que precisamos repetir, mas não sabemos quantas vezes.

Suponha que temos que determinar o primeiro múltiplo de 73 após 3951.
Uma forma de resolver esse problema é gerar sucessivamente os múltiplos positivos de 73 até alcançarmos 3951.

Perceba que não sabemos quantas iterações são necessárias.

Em outras palavras, *enquanto múltiplo ≤ 3951, geramos o próximo múltiplo*.

```Python
multiplo = 73
while multiplo <= 3951:
    multiplo = multiplo + 73

print(multiplo)
```

```Python
4015
```

Quando a condição do laço `while` é avaliada como `False`, a execução 
do laço termina. O valor de `multiplo` é então, maior que 3951.

Como o valor anterior de `multiplo` não foi maior, ele terá o valor 
que queremos: o menor múltiplo maior do que 3951.



## Instrução break

As vezes não se sabe que está na hora de terminar um loop até que já 
esteja na metade do corpo.

Nesse caso, podemos usar a instrução `break` para sair do loop.

Por exemplo, suponha que você quer receber uma entrada do usuário até 
que este digite "fim". 


A condição do loop é `True`, que sempre é verdade, então o loop roda 
até que chegue à instrução de interrupção.


```py
msg = 'Para sair do programa digite "fim".: '
entrada_usuario = input(msg)
while True:
    entrada_usuario = input(msg)
    if msg.lower() == 'fim':
        print('Até mais...')
        break
```


Cada vez que passa pelo loop, o programa apresenta uma mensagem.

Se o usuário digitar **fim**, a instrução **break** sai do loop.

Senão, o programa **ecoa** o quer que o usuário digite e volta ao topo do loop.
 
Perceba que com essa instrução `break` podemos verificar a condição 
em qualquer lugar do loop (não somente no topo)

Podemos exprimir a condição de parada afirmativamente:
- "Pare quando isto acontecer"

Em vez de negativamente
- "Continue a seguir até que isso aconteça"

Crie uma função `primeiro_par_maior_que_um()` que encontra o menor 
número par maior ou igual a 1 usando `while True` e `break`.

```Python
def primeiro_par_maior_que_um():
    n = 1
    while True:
        if n % 2 == 0:
            break
        n += 1
    print(n)
```

Esse método parece até simples, mas a ideia é sempre aumentar a 
complexidade do problema a parte de uma resolução trivial.

Agora, vamos criar uma função `primeiro_par_maior(n)` que encontra o menor
número par maior ou igual a qualquer número, usando `while True` e 
`break`.

Para isso, `n` se torna um parâmetro recebido

```Python
def primeiro_par_maior(n):
    while True:
        if n % 2 == 0:
            break
        n += 1
    print(n)
```

Podemos usar `break` para somatórios também, como:

### 1. Somar os números pares de 2 a 20

```python
soma_progressiva = 0
numero_atual = 2

while True:
    if numero_atual > 20:
        break
    soma_progressiva += numero_atual
    numero_atual += 2

print(soma_progressiva)
```

---

### 2. Somar os quadrados dos números de 1 a 5

```python
soma_progressiva = 0
numero_atual = 1

while True:
    if numero_atual > 5:
        break
    soma_progressiva += numero_atual ** 2
    numero_atual += 1

print(soma_progressiva)
```

---

### 3. Somar os múltiplos de 3 de 3 até 30

```python
soma_progressiva = 0
numero_atual = 3

while True:
    if numero_atual > 30:
        break
    soma_progressiva += numero_atual
    numero_atual += 3

print(soma_progressiva)
```

---

### 4. Somar os números de 10 a 1 (decrescente)

```python
soma_progressiva = 0
numero_atual = 10

while True:
    if numero_atual < 1:
        break
    soma_progressiva += numero_atual
    numero_atual -= 1

print(soma_progressiva)
```

---

A estrutura `while True` com `break` pode parecer mais “livre” e é útil em casos em que a condição de parada depende de **mais de uma verificação** ou **decisões internas ao laço**.


Nos exemplos acima, ela substitui com clareza o `while` com condição explícita, mantendo o controle de fluxo visível com o `break`.


---

## Instrução `continue`

O `continue` faz com que a **iteração atual seja interrompida 
imediatamente**, pulando o restante do bloco dentro do laço (`while` 
ou `for`) e **indo direto para a próxima iteração**.

Só pode ser usado dentro de um laço, não é permitido dentro de 
funções ou classes aninhadas sem estarem dentro de um `while` ou 
`for`.

---

### Exemplo: ignorar o valor 3 e exibir outros números

```python
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue  # pula o print quando i == 3
    print(i)
```

**Saída:**
```
1
2
4
5
6
```

- Quando `i == 3`, o `continue` faz com que o `print(i)` seja 
ignorado, e o laço continua normalmente.

---

### Quando usar `continue`

- **Remover/ignorar casos específicos**, especialmente entradas 
inválidas ou indesejadas:
  
  ```python
  i = 0
  while i < 10:
      i += 1
      if i % 2 == 0:
          continue  # ignora pares
      print(i)      # imprime apenas ímpares
  ```
  **Saída:**
  ```
  1
  3
  5
  7
  9
  ```
  Aqui o `continue` permite manter a lógica clara e evitar colisões 
  no código.

**Reduzir níveis excessivos de indentação**:

Com `continue`, evita-se criar blocos `else` grandes para cada 
condição de filtro — o código fica mais limpo e legível.

---

### Exemplo: separar múltiplos de 3

Vamos ignorar números múltiplos de 3 ao listar:

```python
n = 0
while n < 15:
    n += 1
    if n % 3 == 0:
        continue  # ignora múltiplos de 3
    print(n)
```

**Saída:**
```
1
2
4
5
7
8
10
11
13
14
```

- O `continue` salta o `print` que estaria após, evitando que 
múltiplos de 3 sejam exibidos.

---

### Regras sintáticas

- Só pode ser usado dentro de `while` ou `for` — utilizá-lo fora de 
laço gera erro .
- Ele afeta **apenas o laço em que está inserido**, sem quebrar estruturas externas como `if` ou funções.

---

### O uso do `continue`

Facilita a **leitura** do código, destacando rapidamente condições 
que devem ser ignoradas.

**Torna a lógica mais clara**, evitando complexidade com muitos 
`if/else`.

É um **controle de fluxo direto e intencional**, equivalente a um 
“goto” (vá para) eficiente que vai ao início do laço.

---

### Resumo

```python
while condição:
    # … operações anteriores …
    if caso_especial:
        continue  # pula direto para o início do laço
    # … operações principais …
```

---


## Contexto: `if/elif/else` com `continue` e `break`

* `continue`: interrompe a *iteração atual* e vai imediatamente para a próxima, pulando o restante do bloco do laço .
* `break`: encerra **todo o laço**, saindo completamente dele .
* São frequentemente usados dentro de `if/elif/else` para controlar o fluxo de forma seletiva .

---

### Exemplo prático: laço `while` com `if/elif/else`, `continue` e `break`

```python
n = 0
while True:
    n += 1
    if n % 7 == 0:
        print(f"{n} é múltiplo de 7 → ignorado")
        continue  # pula esta iteração
    elif n % 5 == 0:
        print(f"{n} é múltiplo de 5 → laço encerrado")
        break     # sai completamente do laço
    else:
        print(f"{n} não é múltiplo de 5 nem 7")
```

**O que acontece:**

1. `n` começa em 1, será incrementado até encontrar um múltiplo de 7 ou 5.
2. Ao encontrar **múltiplo de 7**, executa `continue`: ignora o resto e volta ao início do laço sem sair do loop.
3. Ao encontrar **múltiplo de 5**, executa `break`: sai do laço imediatamente.
4. Nos outros casos, imprime uma mensagem padrão.

---

**Comparando comportamento: `continue` x `break`**

| Situação | `n % 7 == 0`      | `n % 5 == 0`   | Outro caso    |
| -------- | ----------------- | -------------- | ------------- |
| Ação     | Ignora (continua) | Encerra o laço | Executa else  |
| Teste    | `if` clause       | `elif` clause  | `else` clause |

```python
# Exemplo simplificado
while True:
    n += 1
    if n == 3:
        continue  # vai para próxima iteração; não imprime
    elif n == 5:
        break     # sai do laço por completo
    print(n)
```

**Saída esperada**: 1, 2, 4 — e depois sai.

---

### Por que usar as duas instruções juntas?

* `continue` limpa rapidamente casos que você quer **ignorar**, sem precisar envolver toda a lógica em indentação de `else`.
* `break` detecta uma **condição de término** (ex: limite atingido, sinal de parada) e permite encerrar o laço.

Esse padrão é comum quando há múltiplas condições:

```python
while True:
    valor = ler_valor()
    if valor inválido:
        continue  # ignora e tenta novamente
    elif valor == valor_de_saida:
        break     # para o laço
    processar(valor)
```

Uma estrutura clara, legível e eficiente .

---

* Use `continue` dentro de `if` para **pular imediatamente** a iteração atual.
* Use `break` dentro de `elif` (ou `if`) para **sair completamente** do laço.
* Essa combinação, junto com `else`, torna seu laço `while` **mais legível** e **seletivo**.
* Evita aninhamentos complexos e melhora a clareza da lógica.




## Raízes quadradas

Loops muitas vezes são usados em programas que calculam resultados numéricos que começam com uma reposta aproximada e melhoram iterativamente.

Uma forma de calcular raízes quadradas é o método de Newton.

Suponha que queira saber a raiz quadrada de um número, o chamaremos de `radicando`, Se começar com quase qualquer estimativa, é possível calcular uma estimativa melhor com a seguinte fórmula:

$$
\text{raiz} = \dfrac{\text{estimativa} + \text{radicando} / \text{estimativa}}{2}
$$




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




```Python
while True:
    print(estimativa)
    raiz = (estimativa + radicando / estimativa) / 2
    if raiz == estimativa:
        break
    estimativa = raiz
```

Para maior parte de valores de `radicando` funciona bem, mas pode ser perigoso testar para alguns tipos de valores.




Em vez de verificar se `raiz` e `estimativa` são exatamente iguais, é mais seguro usar a função integrada `abs` para calcular o valor absoluto ou magnitude da diferença entre eles:

```Python
while True:
    print(estimativa)
    raiz = (estimativa + radicando / estimativa) / 2
    if abs(raiz - estimativa) < 0.00001:
        break
    estimativa = raiz
```



## Algoritmos

O método de Newton é um exemplo de um **algoritmo**: um processo mecânico para resolver uma categoria de problemas.

Técnicas qua aprendemos em matemática básica, como transporte na adição, o empréstimo na subtração e a divisão longa são todos algoritmos.

Algoritmos, são processos mecânicos, nos quais cada passo segue a partir do último, de acordo com um conjunto de regras simples.

Algumas coisas que as pessoas fazem naturalmente, sem dificuldade ou pensamento consciente, são as mais difíceis para exprimir algoritmicamente.





