
# Aula 04 - Expressões, Instruções, Funções, Docstring e Entrada de teclado

{% set aula = "04" %}
{% set link = "ChKzqUPZTNI" %}
{% set objetivos = 
[
  "Compreender e utilizar expressões com variáveis, operadores e valores em Python",
  "Diferenciar e aplicar instruções de atribuição, exibição e concatenação de strings",
  "Criar códigos comentados e legíveis utilizando boas práticas de documentação",
  "Identificar e interpretar erros de sintaxe, execução e semântica em programas",
  "Aplicar operações com strings como concatenação e repetição em contextos práticos"
]
%}
{% include "templates/cabecalho.md" %}


## Expressões 

**Uma expressão é uma combinação de valores, variáveis e operadores.**

Um valor por si mesmo é considerado uma expressão, assim como uma variável, portanto as expressões seguintes são todas **legais**.

```python
>>> 42
42
```

```python
>>> numero_de_dias
17
```

```python
>>> numero_de_dias + 10
27
```

Quando se digita uma expressão no prompt, o interpretador a **avalia**, ou seja, ele encontra o valor da expressão. No exemplo, o *numero_de_dias* tem o valor *17* e *numero_de_dias + 10* tem o valor *27*.


!!! tip "Teste você mesmo"
    Crie uma variável `dias = 5`
    Depois, calcule e imprima quantas **horas** e quantos **minutos** há nesses 5 dias. 



### Mini-projeto 2 – Inventário do Mochileiro Espacial 🚀🪐

!!! info "Objetivo"
    Aplicar expressões matemáticas com variáveis e valores decimais em um contexto criativo, utilizando operações de soma, multiplicação, subtração e divisão para resolver um problema com múltiplas etapas.

#### 🌌 Contexto

Você é o comandante de uma missão intergaláctica que sofreu um pouso forçado em um planeta. Para sobreviver até o resgate, você depende do conteúdo da sua **mochila de emergência**.

Na mochila, há:

- `12` cápsulas de oxigênio (cada uma ocupa `1.5` unidades de volume)
- `8` porções de comida liofilizada (cada uma ocupa `2.2` unidades)
- `3` kits de reparo (cada um ocupa `3.75` unidades)

A mochila suporta **no máximo 40 unidades de volume**.

---

#### 📋 Tarefas

1. Crie variáveis para representar as quantidades e volumes dos itens.
2. Calcule o **volume total ocupado atualmente**.
3. Calcule **quanto espaço ainda está disponível**.
4. Calcule **quantas cápsulas extras de oxigênio** (1.5 de volume) você poderia adicionar com o espaço restante.
5. Agora, **remova 1 kit de reparo** e refaça os cálculos dos passos 3 e 4 com a nova configuração.

---

#### Desafio bônus

> E se você pudesse montar **duas mochilas diferentes**:  
> uma com foco em sobrevivência, e outra com foco em manutenção da nave.  
> Quais itens priorizaria em cada uma? Justifique sua escolha.

---



## Instrução

Uma **instrução** é uma unidade de código que tem um efeito, como criar uma variável ou exibir um valor.

Uma instrução de atribuição:

```python
>>> nota_de_matematica = 9.5
```

Uma instrução de exibição:

```python
>>> print(nota_de_matematica)
```

Quando se digita uma instrução, o interpretador a **executa**, o que significa que ele faz exatamente o que a instrução diz.

### 🎯 Microdesafio – Me apresente ao Python!

Crie três variáveis:

- Seu nome (str)
- Sua idade (int)
- Sua altura (float)

Depois, use `print()` para se apresentar, como se o Python estivesse te conhecendo.


## Operações com strings

Em geral, não é possível executar operações matemáticas com strings, mesmo se elas parecerem com as operações com números.

```python
## Errado
'2' - '1'
'python' / 'programação'
'leitura' * 'prática'
```

Há duas exceções, *+* e *\**


O operador *+* executa uma **concatenação de strings**, ou seja, une as strings pelas extremidades. Por exemplo

```python
>>> nome_usuario = 'brenno'
>>> servidor_email = '@gmail.com'
>>> print(nome_usuario + servidor_email)
brenno@gmail.com
```


O operador *\** também funciona em strings; ele executa a repetição.

```python
>>> nome_usuario = 'brenno'
>>> print(nome_usuario * 3)
brennobrennobrenno
```

Se um dos valores for uma string, o outro tem de ser um número inteiro.

O uso de *+* e *\** faz sentido por analogia com a adição e multiplicação.

### 🎯 Microdesafio – Bio de rede social

Crie três variáveis:

- `nome_usuario` = "larinha"

- `emoji` = "✨"

- `plataforma` = "@insta"

> Experimente trocar os símbolos e nomes para criar outras bios.

## Comentários

Muitas vezes mesmo que faça o uso de bons nomes para variáveis, funções, classes entre outras atribuições. Haverá a necessidade de acrescentar notas aos programas desenvolvidos.

Essas notas são chamadas de **comentários**.

```python
# Registra a porcentagem dos minutos que passaram

porcetagem_minutos = (minutos_decorridos / 60) * 100
```

Nesse caso, o comentário aparece unicamente em uma linha.

Também é possível pôr comentários no fim das linhas:

```python
porcetagem_minutos = (minutos_decorridos / 60) * 100 # Registra a porcentagem dos minutos que passaram
```

Tudo do **#** ao fim da linha é ignorado - não tem efeito na execução do programa.

Bons nomes de variáveis, como discutimos, reduzem a necessidade de comentários.

Nomes longos podem tornar expressões complexas de ler, nessas horas os comentários serão muito bem-vindos.


!!! tip "Pratique"
    Escreva um pequeno código com 2 variáveis e 1 operação.
    Adicione um comentário explicando o que cada linha faz.


### 🎯 Microdesafio – Código comentado

Crie um código simples que calcule a quantidade de passos por minuto de uma caminhada.
Comente cada linha com `#` explicando o que está sendo feito:

> Agora reescreva o mesmo código sem comentários. Qual versão você prefere ler?

## Depuração

Existem três tipos de erros que podem ocorrer em um programa.

- Erros de sintaxe
- Erros de tempo de execução
- Erros semânticos


### Erros de sintaxe

A "sintaxe" refere-se à estrutura de um programa e suas respectivas regras.

Por exemplo, estruturalmente os parênteses devem vir em pares correspondentes.

```python
## Errado
1 + 2)
File "<stdin>", line 1
    1 + 2)
         ^
SyntaxError: unmatched ')'
```

No inicio você pode passar muito tempo rastreando erros de sintaxe, ao adquirir experiência, você fará menos erros e os encontrará mais rápido.


### Erros de tempo de execução

Esse tipo de erro não aparece até que o programa seja executado. Esses erros também se chamam de **exceções** porque normalmente indicam que algo excepcional (e ruim) aconteceu.



```python
>>> 10 * (1/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
```


### Erros semânticos

O terceiro tipo de erro é "semântico", ou seja, relacionado ao significado.

Se houver um erro semântico no seu programa, ele será executado sem gerar mensagens de erro, mas não vai fazer a coisa **certa**. Vai fazer algo diferente, mas especificamente, vai fazer o que você disse para fazer.

Identificar erros semânticos pode ser complicado, porque é preciso trabalhar de trás para a frente, vendo a saída do programa e tentando compreender o que ele está fazendo.

