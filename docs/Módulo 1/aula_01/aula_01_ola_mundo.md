# Aula 01 – "Olá Mundo" da programação 

{% set aula = "01b" %}
{% set link = "" %}
{% set objetivos = [
  "Entender a importância de aprender programação com autonomia e senso crítico",
  "Executar comandos básicos em Python utilizando o interpretador ou plataformas online",
  "Declarar variáveis e utilizar tipos de dados como int, float e str",
  "Escrever e testar pequenos algoritmos em Python com entrada, processamento e saída",
  "Diferenciar linguagens naturais e formais, compreendendo a precisão exigida na programação"
]
%}

{% include "templates/cabecalho_sem_video.md" %}

##  Antes de qualquer código: uma conversa importante

Vivemos um momento em que **ferramentas de inteligência artificial** (como o ChatGPT, Copilot, Gemini, etc.) são capazes de gerar códigos a partir de comandos escritos em linguagem natural. Isso levanta uma pergunta importante:

> **Ainda faz sentido aprender a programar do zero, linha por linha, com a ajuda de um professor ou professora humana?**

Nossa resposta é: **sim, mais do que nunca**.

---

### 🤔 Mas por quê?

#### 1. **A IA não pensa por você**
As ferramentas de IA **respondem**, mas **não compreendem** o problema que você quer resolver.  
Sem entender os fundamentos da programação, você pode até copiar um código, mas não saberá **por que** ele funciona — ou **por que falha**.

#### 2. **Programação é pensamento estruturado**
Aprender a programar é aprender a:
- **Analisar situações**
- **Modelar soluções**
- **Expressar essas soluções com clareza**

Essas habilidades são humanas, transferíveis e vão muito além da programação.

#### 3. **IA erra, e você precisa saber identificar**
Ferramentas como o ChatGPT podem:
- Inventar bibliotecas
- Escrever código incompatível com seu ambiente
- Usar soluções ineficientes ou ultrapassadas

Você precisa ter **critério técnico** para revisar, corrigir ou adaptar o que foi gerado.

> ⚠️ Uma IA não é um oráculo — é uma ferramenta. Você precisa saber usá-la com senso crítico.

#### 4. **O aprendizado prático constrói autonomia**
Codar "com as próprias mãos" ensina mais do que apenas repetir comandos.  
Ajuda você a:
- Lidar com erros reais
- Testar hipóteses
- Depurar, melhorar e documentar

Esse processo **não pode ser terceirizado** se seu objetivo é realmente aprender.

---

## 👣 Nosso caminho aqui

Este curso foi pensado para quem quer **aprender de verdade**.

> Vamos juntos do “Olá, Mundo!” até a construção de pequenos programas, entendendo cada passo do caminho.

Você não precisa ter experiência prévia, mas precisa estar disposto a experimentar, errar, refletir e seguir em frente.

E sim, **vamos aprender a usar ferramentas modernas**, inclusive IA, **mas só depois de dominar o essencial**.

---

## 💻 Comece sem instalar nada!

Para acompanhar as aulas, você pode escolher:

- Instalar o **Python 3** no seu computador, como mostraremos mais adiante;
- Ou usar uma **plataformas online**, como:
    - [Google Colab](https://colab.research.google.com/) – baseado em notebooks, ideal para quem tem conta Google.


---

## O que é um programa ou software?

Um programa é uma sequência de instruções que executa uma operação computacional. Essas operações podem ser:

- **Matemáticas**, como calcular médias ou resolver equações;
- **Simbólicas**, como substituir palavras em um texto;
- **Gráficas**, como exibir imagens ou animações.

> Inclusive, este conteúdo que você está lendo agora foi gerado a partir de um programa!

---

## Cientista da computação: quem é?

- Assim como os matemáticos, usam **linguagens formais** para representar ideias;
- Como engenheiros, projetam e testam **soluções estruturadas**;
- Sua principal habilidade? **Resolver problemas** de forma criativa, estruturada e precisa.

---

## A forma básica dos programas

Quase toda linguagem de programação compartilha instruções fundamentais:

- **Entrada** – Receber dados do teclado, arquivo, rede...
- **Saída** – Exibir ou gravar resultados
- **Operações matemáticas** – Soma, subtração, multiplicação...
- **Execução condicional** – Fazer algo **se** uma condição for verdadeira
- **Repetição** – Executar ações várias vezes (laços)

---

## 🐍 Instalando o Python 3 no Windows

A instalação do Python pode ser feita pelo site:

[https://www.python.org/downloads](https://www.python.org/downloads)


### Passo 1 - Acesso inicial

Para instalar o Python no seu sistema operacional Windows, você precisará baixar o instalador.

> https://www.python.org/downloads/

![w:800](https://raw.githubusercontent.com/eversonott/fundamentos-algoritmos/main/slides/md/imagens/download_python.png)

Isso fará o download do Python 3 para sistemas 64 bits


### Passo 2 - Download e customização

Faça o download do instalador executável do Windows (32 ou 64 bits) e clique duas vezes nele para iniciar o assistente de instalação do python, como mostrado abaixo.

![w:500](https://raw.githubusercontent.com/eversonott/fundamentos-algoritmos/main/slides/md/imagens/instalacao_python.png)

O processo de instalação é bem simples.

> ⚠️ Marque a opção **"use admin privileges when installing py.exe"** antes de clicar em "Install Now".
> ⚠️ Marque a opção **"Add python.exe to PATH"** antes de clicar em "Install Now".


### Passo 3 - Instalação

A tela abaixo será mostrada. Aguarde enquanto o instalador completa o processo de instalação.


![w:800](https://raw.githubusercontent.com/eversonott/fundamentos-algoritmos/main/slides/md/imagens/instalacao_python_progresso.png)

### Passo 4 - Finalização

Se tudo ocorrer bem, a próxima tela será mostrada. Clique em "Close".


![w:800](https://raw.githubusercontent.com/eversonott/fundamentos-algoritmos/main/slides/md/imagens/instalacao_python_concluida.png)


### Passo 5 - Verificação

Para verificar se a instalação do Python foi bem-sucedida, pesquise no menu iniciar por "cmd" e clique duas vezes para abri-lo.


![w:500](https://raw.githubusercontent.com/eversonott/fundamentos-algoritmos/main/slides/md/imagens/instalacao_python_verificacao.png)

Após instalar, abra o **Prompt de Comando (cmd)** e digite:

```bash
python --version
```

Se a instalação estiver correta, verá a versão do Python instalada.

Podemos perceber que há uma tríade de número após o nome "Python", esse número indica qual é versão ques está sendo utilizada.

---

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
