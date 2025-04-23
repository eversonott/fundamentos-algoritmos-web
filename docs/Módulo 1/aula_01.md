# Aula 01 - Caminhos da computação; Instalação Python
 
{% set aula = "01" %}
{% set link = "H55K5LS-mmc" %}
{% set objetivos = [
  "Compreender o que é Computação e suas múltiplas áreas de atuação",
  "Conhecer as principais características dos cursos de Sistemas de Informação, Ciência da Computação e Engenharia de Computação da USP",
  "Comparar os perfis, focos e grades curriculares desses três cursos",
  "Relacionar os interesses pessoais aos diferentes caminhos da Computação",
  "Refletir sobre qual curso mais se alinha ao seu perfil e aspirações profissionais"
  "Entender a importância de aprender programação com autonomia e senso crítico",
]
%}

{% include "templates/cabecalho.md" %}

 

## Objetivo da Aula

Apresentar e comparar três cursos da área de Computação da USP – **Sistemas de Informação**, **Ciência da Computação** e **Engenharia de Computação** – para ajudar estudantes do ensino médio a fazer escolhas profissionais mais conscientes.

---

## O que é Computação?

Computação vai além da programação. Envolve:

- Criar soluções tecnológicas para pessoas, empresas e indústrias;
- Entender como funcionam sistemas (hardware e software);
- Trabalhar com aplicativos, jogos, redes, inteligência artificial, robôs;
- Atuar em empresas de tecnologia, startups, ou centros de pesquisa.

---

## Três Caminhos da Computação na USP

### Sistemas de Informação

- **Foco:** criar e gerenciar sistemas que ajudam empresas na tomada de decisão.
- **Perfil do estudante:** gosta de tecnologia, mas também de negócios e gestão.
- **Destaques na grade:** banco de dados, engenharia de software, redes, gestão.
- **Mercado:** empresas privadas, bancos, startups, consultorias.

### Ciência da Computação

- **Foco:** estudo profundo da computação e desenvolvimento de tecnologias.
- **Perfil do estudante:** curte lógica, matemática e resolver problemas complexos.
- **Destaques na grade:** algoritmos, IA, robótica, computação gráfica.
- **Mercado:** empresas tech, pesquisa, desenvolvimento de software, inovação.

### Engenharia de Computação

- **Foco:** integração entre hardware e software — do código ao circuito.
- **Perfil do estudante:** gosta de eletrônica, robótica, automação e tecnologia física.
- **Destaques na grade:** física, circuitos, sistemas embarcados, telecomunicações.
- **Mercado:** indústria, automação, engenharia de hardware, tecnologia embarcada.

---

## Comparativo entre os Cursos

| Característica         | Sistemas de Informação       | Ciência da Computação        | Engenharia de Computação     |
|------------------------|------------------------------|------------------------------|------------------------------|
| **Foco**               | Tecnologia nos negócios      | Criação de tecnologias       | Integração hardware/software |
| **Matemática**         | Média                        | Alta                         | Muito alta + Física          |
| **Tecnologia**         | Aplicada                     | Teórica e aplicada           | Aplicada e física            |
| **Mercado**            | Empresarial, corporativo     | Pesquisa, inovação, software | Indústria, automação         |
| **Quem vai gostar?**   | Quem gosta de gestão + TI    | Quem curte lógica e desafios | Quem gosta de eletrônica     |

---

## Qual curso combina mais com você?

- **Curioso por negócios e sistemas?** → Sistemas de Informação
- **Ama resolver problemas e lógica?** → Ciência da Computação
- **Gosta de eletrônica e robótica?** → Engenharia de Computação

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

