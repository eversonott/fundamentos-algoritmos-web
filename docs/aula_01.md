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
# Aula 01 - Aula Inaugural do curso

Fundamentos de algoritmos e introdução à programação em python II

Prof. Everson Otoni


---
## Reapresentação

- Em que estágio educacional estão? (ano escolar, curso técnico ...)

- Qual graduação ou licenciatura pretende fazer?

- Por que se inscreveram no módulo 2?

- O que esperam do módulo 2?
---

## Iniciativa

O presente curso é a continuação do Módulo 1 ofertado no primeiro semestre.

A iniciativa de criar um novo curso e não ofertar o mesmo surgiu em diálogo com os estudantes e por conta da extensão dos conceitos ainda considerados fundamentais na aprendizagem inicial de programação e de linguagem.


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

O recurso que o algoritmo mais necessita é o tempo.

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

---

### Comportamento do algoritmo

Uma análise de um algoritmo simples no modelo de RAM pode ser desafiante.

As ferramentas matemáticas exigidas podem incluir:
- Análise combinatória
- Teoria das probabilidades
- Habilidade em álgebra
- Capacidade de identificar os termos significativos

O comportamento de um algoritmo pode ser diferente para cada entrada possível.

Portanto é necessário resumir esse comportamento em fórmulas simples, de fácil compreensão.

---

### Ordenação por inserção (Insertion-Sort)

- Entrada: Uma sequência de $n$ números
- Saída: Uma permutação (reordenação) da sequência de entrada

Ou

- Entrada: $<a_1, \ a_2, \ \cdots, \ a_n>$
- Saída: $<{a'}_1, \ {a'}_2, \ \cdots, \ {a'}_n>$, tal que ${a'}_1 \ \leq {a'}_2 \ \leq \ \cdots \ \leq {a'}_n$


Os números que desejamos ordenar são conhecidos como **chaves**.

---

#### A "lógica"


A ordenação por inserção funciona da maneira como muitas pessoas ordenam as cartas em um jogo de baralho.

![](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi0.wp.com%2Fstudyalgorithms.com%2Fwp-content%2Fuploads%2F2014%2F01%2Finsertion_srot.jpg%3Fresize%3D503%252C433%26ssl%3D1&f=1&nofb=1&ipt=f1f22d900136458f8a031ad7ac2364015567cfb4bf4bd8c161978e124bc17df4&ipo=images)

---

#### Funcionamento

- Iniciamos com mão esquerda vazia e as cartas viradas para baixo, na mesa.

- Em seguida, retiramos uma carta de cada vez da mesa e a inserimos na posição correta na mão esquerda.

- Para encontrar a posição correta para uma carta, nós a comparamos com cada uma das cartas que já estão na mão.

As cartas que seguramos na mão esquerda são ordenadas, e essas cartas eram as que estavam na parte superior da pilha sobre a mesa.

---

##### 2 cartas

Suponhamos que temos 2 cartas sobre a mesa.

1. A primeira carta da pilha possui valor 5.
    - A mão esquerda inicialmente está vazia, e agora contem a carta de valor 5.
2. A segunda carta da pilha, possui valor 2.
    - Olhamos para a carta na mão esquerda: <5>
    - Como 2 é menor que 5, colocamos a segunda carta a esquerda da primeira carta: <2,5>

Perceba que o arranjo inicial era <5, 2> e o final <2, 5>.

---

##### 3 cartas

1. A primeira carta da pilha possui valor 5.
    - A mão esquerda inicialmente está vazia, e agora contem a carta de valor 5.
2. A segunda carta da pilha, possui valor 2.
    - Olhamos para a carta na mão esquerda: <5>
    - Como 2 é menor que 5, colocamos a segunda carta a esquerda da primeira carta ordenada: <2,5>
3. A terceira carta da pilha, possui valor 4.
    - Olhamos para as cartas na mão esquerda: <2, 5>
    - Como 4 é menor que 5, colocamos a terceira carta a esquerda da segunda carta: <2, 4, 5>

Perceba que o arranjo inicial era <5, 2, 4> e o final <2, 4, 5>.

---

##### 4 cartas

1. A primeira carta da pilha possui valor 5.
    - A mão esquerda inicialmente está vazia, e agora contem a carta de valor 5.
2. A segunda carta da pilha, possui valor 2.
    - Olhamos para a carta na mão esquerda: <5>
    - Como 2 é menor que 5, colocamos a segunda carta a esquerda da primeira carta: <2,5>
3. A terceira carta da pilha, possui valor 4.
    - Olhamos para as cartas na mão esquerda: <2, 5>
    - Como 4 é menor que 5, colocamos a terceira carta a esquerda da segunda carta ordenada: <2, 4, 5>

---

4. A quarta carta da pilha possui valor 6.
    - Olhamos para as cartas na mão esquerda: <2, 4, 5>
    - Como 6 é maior que 5, colocamos a quarta carta a direita da terceira carta ordenada: <2, 4, 5, 6>

Perceba que o arranjo inicial era <5, 2, 4, 6> e o final <2, 4, 5, 6>.

---

##### Conclusão

Como o comparativo é binário, ou seja, exige dois elementos. Podemos sempre começar a partir do passo 2.

Logo iniciamos a partir do segundo elemento.

Perceba que a ordenação ocorre da esquerda para a direita.


---

#### Pseudocódigo

O pseudocódigo se assemelha muito com as linguagens de programação C, C++, Python e Pascal.

No pseudocódigo é empregado qualquer método expressivo que seja mais claro e conciso para especificar um dado algoritmo.

Às vezes, o método mais claro é a linguagem natural.

O pseudocódigo não se preocupa com questões de engenharia de software. Isso significa que não se preocupa com abstrações de dados, módulos e erros.

O pseudocódigo transmite a essência do algoritmo de modo mais conciso.

---

##### O pseudocódigo de fato

```py title="pseudocodigo.py" linenums="1"
def ordenacao_insercao(A):
    Para i = 1 até A.comprimento, faça:
        chave = A[i]
        // Inserir A[i] na sequência ordenada A[0, ..., i -1]
        j = i - 1
        Enquanto j > -1 e A[j] > chave, faça:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = chave
```


---

##### Ordenação por inserção

```py title="ordenacao_insercao.py" linenums="1" hl_lines="2 5"
def ordenacao_insercao(lista):
    for indice_chave in range(1, len(lista)):
        chave = lista[indice_chave]
        indice_anterior = indice_chave - 1
        while indice_anterior >= 0 and lista[indice_anterior] > chave:
            indice_posterior = indice_anterior + 1
            # Troca o elemento maior de posição, desloca para "direita"
            lista[indice_posterior] = lista[indice_anterior]
            # Corrige o indíce, após o comparativo.
            indice_anterior = indice_anterior - 1 
        # Mantém na ordem inicial, já que o termo posterior é menor ou igual.
        lista[indice_anterior + 1] = chave 
```


---

###### Explicações

A variável `i` inicia a partir do segundo elemento da lista. 
Como concluímos, a comparação é binária, e compara o posterior com o anterior.

`chave = lista[i]` armazena o valor numérico (elemento) na posição `i`.

A condição `j >= 0 and lista[j] > chave` faz o comparativo.
Se o elemento anterior for maior que o elemento posterior. Há um inversão de posições (`lista[j + 1] = lista[j]`)
Por conta dessa inversão, temos que voltar uma posição (`j = j -1`)


Se o elemento anterior não for maior que o elemento posterior, ele será igual ou menor. Logo fora do escopo do while, temos `lista[j + 1] = chave`

---

###### Caso de teste



