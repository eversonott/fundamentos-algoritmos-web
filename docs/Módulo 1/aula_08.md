
# Aula 08 - Recursividade

{% set aula = "08" %}
{% set link = "jBWWcD6BRH4" %}
{% set objetivos = 
[
  "Compreender o conceito de recursão como solução baseada em subproblemas",
  "Reconhecer a estrutura de uma função recursiva com caso básico e chamada a si mesma",
  "Evitar chamadas infinitas garantindo uma condição de parada adequada",
  "Desenvolver o pensamento recursivo por meio de exemplos guiados",
  "Construir funções recursivas simples, como contagem regressiva e exibição vertical de dígitos"
]

%}
{% include "templates/cabecalho.md" %}


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



Temos diversas linhas de mensagem de erro, e somos informados que a **profundidade máxima de recursão foi excedida**.

A execução estava seguindo **indefinidamente**, mas o interpretador Python parou com isso.

O ponto principal a se entender aqui, é que uma **função recursiva** chamará a si mesma **indefinidamente**, a menos que modifiquemos a função de modo que haja uma **condição de parada**.



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




