# Aula 03 - Variáveis e convenções de nomenclatura
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


