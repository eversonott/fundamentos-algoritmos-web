# Aula 03 - Variáveis, expressões e instruções
{% set aula = "03" %}
{% set link = "" %}
{% set objetivos = [
  "Diferenciar linguagens naturais e formais, compreendendo a precisão exigida na programação"
]
%}
{% include "templates/cabecalho_sem_video.md" %}


## 📚 Linguagens naturais vs. formais

- **Linguagens naturais**: como português ou inglês, usadas na fala cotidiana.
- **Linguagens formais**: criadas para fins específicos (ex: matemática, química, programação)

Programação exige **precisão sintática**:

```python
print("Olá")   # Correto
print(Olá)     # Erro: sem aspas
```

> Um pequeno erro de pontuação pode impedir um programa de funcionar!

---

## 🐞 Depuração (debugging)

Erros fazem parte da vida de quem programa:

- Um **bug** é um erro no código
- **Depurar** é o processo de encontrar e corrigir erros

> Um famoso bug foi literalmente um inseto dentro do computador!

Aprender a depurar é tão importante quanto escrever código.

---

## Variável

Um dos recursos eficientes de uma linguagem de programação é a capacidade de 
manipular variáveis.

**Uma variável é um nome que se refere a um valor.**

!!! tip "Experimente"
    Crie uma variável chamada `mensagem` com o valor `'Olá, Python!'` e use `print(mensagem)` para exibir.
    Em seguida, mude o valor da variável para `'Aprendendo variáveis'` e exiba novamente.

## Instruções de atribuição

Uma *instrução de atribuição* cria uma nova variável e dá um valor a ela:

```python
>>> mensagem = 'Esta é uma mensagem de teste'
>>> numero = 17
>>> pi = 3.141592653589793
```

Existem aqui três atribuições.

A primeira atribui uma string a uma nova variável chamada mensagem.

A segunda dá o número inteiro 17 a variável chamada numero.

A terceira atribui o valor (aproximado) de π a variável denominada de "pi".

### 💼 Mini-projeto – Assinatura de e-mail automática

Crie variáveis para armazenar:

- Seu nome
- Seu curso ou cargo
- Sua instituição (real ou fictícia)

Combine os dados em um `print()` que exiba uma assinatura:

```sh
Rafael Souza  
Estudante de Informática  
IF do Norte
```

## PEP 8

### PEP

Documento que fornece convenções de codificação para o código Python que compreende a biblioteca padrão na distribuição principal do Python.

### A PEP 8 
Escrito pelo próprio fundador do Python, o Guido van Rossum.

Guia de estilo que evolui com tempo à medida que convenções adicionais são identificadas ou se tornem obsoletas devido a mudanças na própria linguagem.

É um conjunto de diretrizes que têm como objetivo melhorar a legibilidade do código e torná-lo consistente em todo o amplo espectro do código Python.


## Convenções de nomenclatura

Existem algumas convenções,que sugerem certos padrões de nomenclatura que atualmente são recomendados.

### Princípio primordial

Os nomes que são visíveis para o usuário devem seguir convenções que reflitam o uso e não a implementação.

O nome explicita o seu uso.


### Estilos de nomenclatura

Os seguintes estilos de nomenclatura são comumente distinguidos em:

- b (única letra minúscula)
- B (única letra MAIÚSCULA)
- minúsculas
- minúsculas_separadas_por_sublinhados
- MAIÚSCULAS
- MAIÚSCULAS_SEPARADAS_POR_SUBLINHADOS
- PalavrasComecamPorMaiusculas (Corcova do camelo - CamelCase ou CapWords)
- palavrasComecamPorMaisculasComExcecaoDaPrimeiraPalavra (Variação da "Corcova do camelo")


### Nomes a evitar

Nunca use os caracteres 'l' (L minúsculo), 'O' (o maiúsculo) ou 'I' (i maiúsculo) sozinhos como nomes de variáveis. Em algumas fontes, esses caracteres são indistinguíveis dos números um e zero.


## Nome das variáveis

Geralmente e recomenda-se escolher nomes significativos para as variáveis.

Nomes de variáveis podem ser tão longos quanto queira.

Podem conter letras com números, mas nunca podem começar com um número.

**A convenção é utilizar apenas letras minúsculas para nomes de variáveis.**


### Nomes que revelem o seu propósito

Escolher bons nomes leva tempo, mas economiza mais.

O nome de uma variável, função ou classe deve:

- Lhe dizer porque existe

- O que faz

- Como é usado

**Dica: Se um nome requer um comentário de código, então não revela seu propósito.**


```python
d = 25 ## dias decorridos do pagamento
```

O nome "d" não revela nada. Não indica a ideia de tempo decorrido, nem de dias e nem com o que o tempo está relacionado.


```python
dias_decoridos_pagamento = 25
```

### Faça distinções significativas

Os programadores criam problemas para si mesmos quando criam um código voltado unicamente para o compilador ou interpretador.

Lembre-se programa-se não para o computador, toda linguagem é construída socialmente.

Se os nomes precisam ser diferentes, então também devem ter significados distintos.

Não basta adicionar números ou palavras comuns, mesmo que o compilador ou interpretador fique satisfeito.

Por exemplo:

```python
## Errado
a1 = 'Bernado'
a2 = 'Beatriz'
a3 = 'Caio'
```
Usar números sequenciais em nomes (a1, a2, a3,...,aN) é o oposto de nome expressivos.

Geram confusão, simplesmente não oferecem informação alguma ou dica sobre a intenção de seu criador.


```python
## Certo
nome_dos_alunos = ['Bernardo', 'Beatriz', 'Caio']
```

Veremos adiante o que significa a instrução acima.

Palavras muito comuns são outra forma de distinção que nada expressam.

Palavras muito comuns são redundantes. O nome de uma variável jamais deve conter a palavra "variável".

Faça a distinção dos nomes de uma forma que o leitor compreenda as diferenças


### Use nomes pronunciáveis

Use a parte do cérebro que evoluiu para lidar com a língua falada para nomes pronunciáveis.

**A programação é uma atividade social**

```python
## Errado
gedtamdhms()
```
No caso acima a função gedtamdhms, seu criador usou a seguinte lógica:

- gerador: ge
- data: dt
- ano: a
- mês: m
- dia: d
- hora: h
- minuto: m
- segundo: s

Se pronunciaria como "gê dê tê a eme dê agá eme ése"

```python
## Certo
gerador_data_completa()
```


### Use nomes passíveis de busca

Nomes de uma só letra ou números não são fáceis de localizá-los ao longo de um texto.

Por exemplo, pode-se localizar facilmente a variável *quantidade_max_materias_por_estudante*, do que localizar o número *7*.

Nomes, definições e várias outras expressões que possuem tal número, usado para outros propósitos podem ser resultados da busca.

Logo, nomes longos se sobressaem aos curtos.


### Evite o mapeamento mental

Os leitores não devem ter de traduzir mentalmente os nomes que você escolheu por outros que eles conheça.

Não use termos do domínio do problema e nem os da solução.

Esse é o problema com nomes de variáveis de uma só letra.
Certamente um contador de iterações pode ser chamado de "i", "j" ou "k" - isso já se tornou uma tradição.


### Não dê uma de espertinho

Se os nomes forem muito "espertinhos", apenas as pessoas que compartilhem do mesmo senso de humor que seu dono irão entendê-los ou lembrá-los.

```python
## Certo
granada()
```
Saberão o que a função *granada* faz? Talvez. É engraçado, mas talvez seja melhor uma função chamada de *apaga_itens*.

```python
## Certo
apaga_itens()
```

Essas brincadeiras em código costumam aparecer na forma de coloquialismos e gírias. E até mesmo piadas de baixo calão.

**Diga o que você quer expressar, expresse o que você quer dizer.**


### Adicione um contexto significativo

Há poucos nomes que são significativos por si só - a maioria não é.

Utilize nomes que façam parte do contexto do leitor. E em último recurso adicione prefixos ao nome.

Imagine as varáveis chamadas *primeiro_nome*, *sobrenome*, *logradouro*, *numero*, *cidade*, *estado*, *cep*. Vistas juntas, fica bem claro que ela formam um endereço.

Mas e se fosse visto as variáveis *numero* e *estado* sozinhas? Seria assumido que fazem parte de um endereço?

A variável de nome *estado* poderia estar associada ao valor do estado cível, por exemplo.

### 🎯 Microdesafio – Nome confuso vs. nome claro

Crie duas variáveis:

- Uma com nome ruim (ex: x, a2)
- Uma com nome claro (ex: media_final)

Atribua valores e exiba com print(). Depois responda:

> Se você visse esse código daqui a 15 dias, qual nome te ajudaria a entender o que ele faz?

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



