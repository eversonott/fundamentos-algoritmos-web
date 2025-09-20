# Aula 01 - Aula Inaugural do curso e introdução à análise de algoritmos


{% set aula = "01" %}
{% set link = "" %}
{% set objetivos = ["Recursos computacionais", "Modelo RAM", "Discussão inicial de como analisar algoritmos"] %}

{% include "templates/cabecalho_sem_video.md" %}


---
## Reapresentação

- Em que estágio educacional estão? (ano escolar, curso técnico ...)

- Qual graduação ou licenciatura pretende fazer ou começaram a fazer?

- O que esperam do módulo 2?

---

## Iniciativa

O presente curso é a continuação do Módulo 1 ofertado no primeiro semestre.

A iniciativa de criar um novo curso e não ofertar o mesmo surgiu em diálogo 
com os estudantes e por conta da extensão dos conceitos ainda considerados 
"fundamentais" na aprendizagem inicial de programação e de linguagem.


---

## Revisão

- Variáveis
- Funções
- Operadores
- Expressões booleanas, operadores relacionais, operadores lógicos e execução condicional
- Recursividade
- Iteração
    - While
    - For
- Listas
- Dicionários
- Tuplas

---

## Análise de algoritmos - Uma brevíssima introdução

Analisar um algoritmo significa prever os recursos de que o algoritmo necessita.

Recursos como:

- Memória
- Capacidade de transmissão de dados
- Capacidade de hardware

O recurso que o algoritmo mais necessita é o **tempo**.

![Alt Text](https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExMWQwbmVwczBrdG8yY2xrMnp6ZWxkZm44ZDFvM2EwbDRmZm1yNjJ5bCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/um2kBnfo55iW4ZH1Fa/giphy.gif)

---

### A análise

Perceba que ao analisar um algoritmo por diferentes critérios, podemos determinar a qualidade inferior ou superior.

Para entender melhor a análise, admitimos que as instruções serão executadas uma após outra, sem operações concorrentes.


---

### Modelo RAM

Para nosso pensamento computacional pensamos um modelo de computação genérico de máquina de acesso aleatório (random-access machine, RAM).

No modelo RAM encontramos:

- Instruções aritméticas 
    - soma, subtração, multiplicação, divisão, resto, piso, teto.
- Movimentação de dados
    - Carregar, armazenar e copiar
- Movimentação de controle
    - Desvio condicional, incondicional, chamada e retorno de sub-rotinas

**Cada uma dessas instruções demora uma quantidade de tempo constante.**

![](https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExcHdiMWJ4Y2RubWFzM2JxNHk5NzMyYzAzejdwd3gxZmxpdnd6N2FqdSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/8YBpKSm3uPWG9Ca0F4/giphy.gif)

---

### Comportamento dos algoritmos

Uma análise de um algoritmo simples no modelo de RAM pode ser desafiante.

As ferramentas matemáticas exigidas podem incluir:

- Análise combinatória
- Teoria das probabilidades
- Habilidade em álgebra
- Capacidade de identificar os termos significativos

O comportamento de um algoritmo pode ser diferente para cada entrada possível.

Portanto é necessário resumir esse comportamento em fórmulas simples, de fácil compreensão.

---

## Ordenação por inserção (Insertion-Sort)

- Entrada: Uma sequência de $n$ números
- Saída: Uma permutação (reordenação) da sequência de entrada

Ou

- Entrada: $<a_1, \ a_2, \ \cdots, \ a_n>$
- Saída: $<{a'}_1, \ {a'}_2, \ \cdots, \ {a'}_n>$, tal que ${a'}_1 \ \leq {a'}_2 \ \leq \ \cdots \ \leq {a'}_n$


Os números que desejamos ordenar são conhecidos como **chaves**.

---

### A "lógica"


A ordenação por inserção funciona da maneira como muitas pessoas ordenam as cartas em um jogo de baralho.

![](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi0.wp.com%2Fstudyalgorithms.com%2Fwp-content%2Fuploads%2F2014%2F01%2Finsertion_srot.jpg%3Fresize%3D503%252C433%26ssl%3D1&f=1&nofb=1&ipt=f1f22d900136458f8a031ad7ac2364015567cfb4bf4bd8c161978e124bc17df4&ipo=images)



- Iniciamos com mão esquerda vazia e as cartas viradas para baixo, na mesa.

- Em seguida, retiramos uma carta de cada vez da mesa e a inserimos na posição correta na mão esquerda.

- Para encontrar a posição correta para uma carta, nós a comparamos com cada uma das cartas que já estão na mão.

As cartas que seguramos na mão esquerda são ordenadas, e essas cartas eram as que estavam na parte superior da pilha sobre a mesa.

---

#### 2 cartas

Suponhamos que temos 2 cartas sobre a mesa.

1. A primeira carta da pilha possui valor 6.
    - A mão esquerda inicialmente está vazia, e agora contem a carta de valor 5.
2. A segunda carta da pilha, possui valor 5.
    - Olhamos para a carta na mão esquerda: <6>
    - Como 5 é menor que 6, colocamos a segunda carta a esquerda da primeira carta: <5,6>

Perceba que o arranjo inicial era <6, 5> e o final <5, 6>.

---

#### 3 cartas

1. A primeira carta da pilha possui valor 6.
    - A mão esquerda inicialmente está vazia, e agora contem a carta de valor 5.
2. A segunda carta da pilha, possui valor 5.
    - Olhamos para a carta na mão esquerda: <6>
    - Como 5 é menor que 6, colocamos a segunda carta a esquerda da primeira carta: <2,5>
3. A terceira carta da pilha, possui valor 4.
    - Olhamos para as cartas na mão esquerda: <5, 6>
    - Como 4 é menor que 5, colocamos a terceira carta a esquerda da segunda carta: <2, 4, 5>

Perceba que o arranjo inicial era <6, 5, 4> e o final <4, 5, 6>.

---

#### 4 cartas

1. A primeira carta da pilha possui valor 6.
    - A mão esquerda inicialmente está vazia, e agora contem a carta de valor 5.
2. A segunda carta da pilha, possui valor 5.
    - Olhamos para a carta na mão esquerda: <6>
    - Como 5 é menor que 6, colocamos a segunda carta a esquerda da primeira carta: <2,5>
3. A terceira carta da pilha, possui valor 4.
    - Olhamos para as cartas na mão esquerda: <5, 6>
    - Como 4 é menor que 5, colocamos a terceira carta a esquerda da segunda carta: <2, 4, 5>
4. A quarta carta da pilha possui valor 2.
    - Olhamos para as cartas na mão esquerda: <4, 5, 6>
    - Como 2 é menor que 4, colocamos a quarta carta a esquerda da terceira carta ordenada: <2, 4, 5, 6>

Perceba que o arranjo inicial era <6, 5, 4, 2> e o final <2, 4, 5, 6>.


### Vamos implementar


