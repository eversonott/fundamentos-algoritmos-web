# Aula 02 – "Olá Mundo" da programação 
{% set aula = "02" %}
{% set link = "B_2R4LZSlJk" %}
{% set objetivos = [
  "Executar comandos básicos em Python utilizando o interpretador ou plataformas online",
  "Declarar variáveis e utilizar tipos de dados como int, float e str",
  "Escrever e testar pequenos algoritmos em Python com entrada, processamento e saída",
]
%}

{% include "templates/cabecalho.md" %}


## 🌀 Usando o interpretador e o IDLE

O **interpretador Python** pode ser usado via terminal ou através do **IDLE**, um ambiente simples que acompanha o instalador.

Para abrir o IDLE, busque por "IDLE" no menu Iniciar do Windows. 


![w:450](https://raw.githubusercontent.com/eversonott/fundamentos-algoritmos/main/slides/md/imagens/idle.png)

Você verá algo assim:


![w:500](https://raw.githubusercontent.com/eversonott/fundamentos-algoritmos/main/slides/md/imagens/idle_uso.gif)


A linha com `>>>` é o **prompt** do interpretador.

### Usando o terminal

Também podemos acessar o interpretador Python via terminal, ou seja, via CMD (Windows) ou shell (Linux), para isso você pode acessar o cmd novamente (Como no item Passo 5 - Verificação):

Basta digitar o comando:

```bash
python
```

Você terá algo como:

![](https://raw.githubusercontent.com/eversonott/fundamentos-algoritmos/main/slides/md/imagens/console_python.png)

A última linha que inicia com `>>>` é um prompt. São caracteres expostos pelo interpretador para indicar que está tudo pronto para receber entradas do usuário.

---

## 🎯 Microdesafio 1 – Interagindo com o Python

Abra o Google Colab ou o IDLE e execute o seguinte código:

```python
print("Olá, Mundo!")
```

- O que aconteceu?
- O que aconteceria se você **omitisse as aspas**?


O comando `print()` é usado para **exibir mensagens na tela**.

Ele pode receber:

- **Textos** entre aspas (ex: `"Olá!"`)
- **Números** (ex: `42`, `3.14`)
- **Variáveis** que guardam valores (veremos esse assunto com mais detalhe nas próximas aulas)

Experimente executar os comandos abaixo em sequência:

```python
print("Olá, Mundo!")
print(42)
mensagem = "Bem-vindo à programação!"
print(mensagem)
```

- O que aconteceu?
- O que mudaria se você **omitisse as aspas**?
- E se mudasse o valor da variável `mensagem`?

> 💡 O `print()` separa automaticamente os valores com espaço quando usamos vírgula.

```python
nome = "Ana"
idade = 18
print("Nome:", nome)
print("Idade:", idade)
```

Saída esperada:

```python
Nome: Ana
Idade: 18
```
---

## 🔄 Programas como algoritmos

Um programa é uma **sequência lógica de passos** para resolver um problema.

Considere o seguinte problema:

> "Quero saber a média de duas notas."

Em linguagem natural, o algoritmo seria:

1. Obter a primeira nota
2. Obter a segunda nota
3. Somar as duas
4. Dividir por 2
5. Exibir o resultado

Agora em Python:

```python
a = 7.5
b = 8.0
media = (a + b) / 2
print("A média é:", media)
```

> 🎯 Conexão feita: o algoritmo em linguagem natural virou código!

---

## 🧮 Operadores e tipos de dados

Python usa **símbolos especiais** para representar operações:

```python
>>> 6 + 7      # Soma
>>> 10 - 3     # Subtração
>>> 4 * 5      # Multiplicação
>>> 20 / 4     # Divisão
>>> 2 ** 3     # Exponenciação
```

Também há **valores diferentes**:

- `42` → inteiro (`int`)
- `3.14` → número decimal (`float`)
- `'Olá!'` → texto (`str`)

Você pode verificar os tipos com a função `type()`:

```python
>>> type(42)
<class 'int'>
>>> type("Olá")
<class 'str'>
```

---

## 🎯 Microdesafio 2 – Seu primeiro programa

Escreva um código em Python que:

1. Armazene seu nome em uma variável
2. Imprima uma saudação personalizada com seu nome

---

## 🧪 Mini-projeto – Calculadora de boas-vindas

!!! info "Objetivo"
    Trabalhar com variáveis do tipo `int`, conversão de minutos para horas, cálculo de porcentagens e exibição formatada com `print()`.

Crie um programa que:

1. Armazene seu **nome** e **idade**
2. Armazene a quantidade de **minutos por semana na internet** e de **estudo**
3. Converta os minutos para horas
4. Calcule a porcentagem de tempo gasto em cada atividade, considerando 168 horas na semana
5. Exiba os resultados com `print()` e porcentagens arredondadas para duas casas decimais


=== "📤 Saída esperada"
    ```
    Nome: Rafa
    Idade: 17
    Tempo na internet: 15.18%
    Tempo de estudo: 7.59%
    Outras atividades: 77.23%
    ```

!!! tip "Experimente" 
    Tente alterar os minutos ou adicionar novas categorias como minutos_sono.
    Você pode transformar isso em uma visualização da sua rotina semanal!

> 💡 Dica: experimente com valores diferentes, explore erros e veja o que acontece.

---

