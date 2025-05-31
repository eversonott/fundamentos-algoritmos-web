# Aula 06 - Funções e Docstrings

{% set aula = "06" %}
{% set link = "N3aN16o57Pk" %}
{% set objetivos = 
[
  "Compreender o escopo local de variáveis e parâmetros em funções",
  "Criar funções com retorno utilizando a palavra-chave return",
  "Aplicar boas práticas de documentação com Docstrings conforme a PEP 257",
  "Utilizar a função input para capturar dados do usuário de forma interativa",
  "Resolver problemas práticos com funções que recebem argumentos e retornam valores"
]

%}
{% include "templates/cabecalho.md" %}## Funções (continuação)

### Novas funções (continuação)

#### As variáveis e os parâmetros são locais

Quando uma variável é criada dentro de uma função seja ela parâmetro ou não, ela é local, ou seja, só existe dentro da função. Só existe dentro do escopo da função.

```python
>>> def imprime_concatenacao_duas_strings(parte_inicial, parte_final):
...     texto = parte_inicial + parte_final
...     imprime_nome(texto)
...
```

Essa função recebe dois argumentos, concatena-os e exibe o resultado utilizando a função `imprime_nome`, que acabamos de criar.


```python
>>> terceiro_verso = 'Mas tenho muito tempo, '
>>> quarto_verso = 'temos todo tempo do mundo'
>>> imprime_concatenacao_duas_strings(terceiro_verso, quarto_verso)
Mas tenho muito tempo, temos todo tempo do mundo
```
Quando `imprime_concatenacao_duas_strings` é encerrada, a variável `texto` é destruída.

```python
>>> print(texto)
NameError: name 'texto' is not defined.
```



#### Funções com resultado e funções sem resultados (métodos)

Até o momento criamos funções que apenas exibem algo na tela e não especificamente possuem um valor de retorno, ou um resultado retornado.

Vamos criar agora uma função que tenha como mesmo princípio que a função `math.pow`.

```python
>>> def calcula_potencia(base, expoente):
...     potencia = base ** expoente
...     return potencia
...


>>> print(calcula_potencia(2,3))
8
```

Com o uso do termo `return` nossa função gera um resultado ou nos devolve um objeto.


---

#### Mais exemplos de funções

```python title='funcoes.py'
def resolutiva_primeiro_grau(a, b):
    raiz = -b/a
    return raiz
```
Agora conseguimos resolver equações de primeiro grau, usando programação.
Por exemplo, qual é a raiz da função de primeiro grau: $2x + 16$?

Basta:

```python title='terminal: python -i funcoes.py'
resolutiva_primeiro_grau(2, 16):
-8.0
```

Vamos além!

Vamos tentar fazer um algoritmo da resolutiva de segundo grau:

```python title='funcoes.py'
import math
def resolutiva_segundo_grau(a, b, c):
    delta = b**2 - (4 * a * c) # Ou delta = math.pow(b, 2) - (4 * a * c)
    raiz_1 = (-b + math.sqrt(delta))/(2* a)
    raiz_2 = (-b - math.sqrt(delta))/(2* a)
    return raiz_1, raiz_2
```

Testando:

```python title='terminal: python -i funcoes.py'
>>> resolutiva_segundo_grau(2,3,-5)
(1.0, -2.5)
```

O exemplo acima resolve a função de segundo grau $2x^2 + 3x -5$

Mas o que aconteceria se por acaso confundirmos a ordem na passagem dos argumentos?

Bom, teríamos equações diferentes. Uma vez que, mudando a ordem, mudamos os coeficientes.

Por exemplo, alternando a ordem dos números 2 e 3 teríamos a equação $2x^2 + 2x - 5$, logo a raiz também seria diferente.

Para passar a ordem correta, precisamos ter acesso a declaração literal da função ou pedimos ajuda!


Ajuda em inglês é: help.

```python title='terminal'
import math
help(math.pow)
```

Como saída, obtemos um sistema interativo de ajuda do python

```txt
Help on built-in function pow in module math:

pow(x, y, /)
    Return x**y (x to the power of y).
~
```

Traduzindo:

```txt
Ajuda sobre a função interna pow no módulo math:

pow(x, y, /)
Retorna x**y (x elevado à potência de y).
~
```

Veja, não precisamos ir até o arquivo responsável pela implementação da função `pow` do módulo embutido do Python.
Basta passar por parâmetro o nome do objeto que queiramos consultar.

#### Usando o `help` como nossas funções

```python title='terminal'
>>> help(resolutiva_segundo_grau)
```

Obtemos:

```txt
Help on function resolutiva_segundo_grau in module __main__:

resolutiva_segundo_grau(a, b, c)
```

Ops! Conseguimos ver o nome dos parâmetros, lembra-se de nomear corretamente.
Esses nomes não parecem ser significativos.

Primeiro vamos deixar os nomes mais claros:

```python title='funcoes.py'
import math
def resolutiva_segundo_grau(coeficiente_a, coeficiente_b, coeficiente_c):
    delta = coeficiente_b**2 - (4 * coeficiente_a * coeficiente_c) # Ou delta = math.pow(b, 2) - (4 * a * c)
    raiz_1 = (-coeficiente_b + math.sqrt(delta))/(2* coeficiente_a)
    raiz_2 = (-coeficiente_b - math.sqrt(delta))/(2* coeficiente_a)
    return raiz_1, raiz_2
```

Agora temos:

```txt
Help on function resolutiva_segundo_grau in module __main__:

resolutiva_segundo_grau(coeficiente_a, coeficiente_b, coeficiente_c)
```

Agora está mais claro, mas parece falta um maior detalhamento sobre o que nossa função faz.

Está faltando uma documentação!

Está faltando `DocString`

## DocString

As convenções das DocString é oficializada por meio de uma PEP (Vimos [PEP](../../Módulo 1/aula_02/#pep) na aula anterior).

### PEP 257 - Convenções DocString

Criada por David Goodger e pelo fundador do Python Guido van Rossum


Essa PEP documenta a semântica e as convenções a Documentos Python.

Existem duas formas de docstrings: Única-linha ou Múltiplas-linhas

### Única linha

Única-linha são usadas para caso realmente óbvios. Portanto devem caber em uma linha, uma frase.

```python title='funcoes.py'
def calcula_potencia(base, expoente):
    """Fornecido a base e expoente, retorna a potência."""
    potencia = base ** expoente
    return potencia
```

```python title='terminal: python -i funcoes.py'
help(calcula_potencia)
```

Resulta em:

```txt
Help on function calcula_potencia in module __main__:

calcula_potencia(base, expoente)
    Fornecido a base e expoente, retorna a potência.
```

Perceba que a docstring documentada na função agora aparece quando passamos o nome da função para o `help` do Python.


Vale destacar alguns pontos:

- Aspas triplas são usadas mesmo que a string caiba em uma linha. Isso torna mais fácil expandi-lo posteriormente.
- As aspas de fechamento estão na mesma linha das aspas de abertura. Esse parece melhor para frases simples.
- Não há linha em branco antes ou depois da docstring.
- A docstring é uma frase que termina em um ponto final. Ela prescreve o função ou efeito do método como um comando (“Faça isto”, “Retorne aquilo”), não como uma descrição; por exemplo, não escreva “Retorna a potência...”. 
- A doutrina de uma linha NÃO deve ser uma “assinatura” reiterando a parâmetros de função/método (que podem ser obtidos por introspecção).
    - Não faça:
    ```python title='funcoes.py'
            def calcula_potencia(base, expoente):
            """function(base, expoente) -> float"""
            potencia = base ** expoente
            return potencia
    ```

### Múltiplas-linhas

Vamos começar pelo exemplo:


```python title='funcoes.py'
import math
def resolutiva_segundo_grau(coeficiente_a, coeficiente_b, coeficiente_c):
    """Retorna as raízes de uma equação de segundo grau.

    Argumentos:
    coeficiente_a -- Coeficiente que multiplica x^2.
    coeficiente_b -- Coeficiente que multiplica x.
    coeficiente_c -- Coeficiente independente.
    """
    delta = coeficiente_b**2 - (4 * coeficiente_a * coeficiente_c) # Ou delta = math.pow(b, 2) - (4 * a * c)
    raiz_1 = (-coeficiente_b + math.sqrt(delta))/(2* coeficiente_a)
    raiz_2 = (-coeficiente_b - math.sqrt(delta))/(2* coeficiente_a)
    return raiz_1, raiz_2
```

Documentos multilinhas consistem em uma linha de resumo, assim como uma linha docstring, seguido por uma linha em branco, seguido por um texto mais elaborado descrição. 

##### Linha de resumo:

- A linha de resumo pode ser usada pela indexação automática ferramentas; 
- É importante que caiba em uma linha e esteja separado de o restante da documentação por uma linha em branco. 

#### Docstring:

- O inteiro docstring é recuado da mesma forma que as aspas em sua primeira linha.


##### Docstring para funções:

- A docstring para uma função ou método deve resumir seu comportamento e documentar seus argumentos, valores de retorno, efeitos colaterais, exceções levantado e restrições sobre quando pode ser chamado (todos, se aplicável). 
- Argumentos opcionais devem ser indicados. 
- Deve ser documentado se os argumentos de palavras-chave fazem parte da interface.

##### Alguns exemplos de novas funções utilizando Docstring

```python title='formulas_muv.py'
# Fórmulas da aceleração do MUV

def aceleracao_muv(velocidade_final, velocidade_inicial, tempo):
    """ Fornecido a velocidade final (m/s), velocidade inicial (m/s) e o tempo (s), retorna a aceleração do movimento uniformemente variado (m/s²).
    
    Argumentos:
    velocidade_final -- Velocidade final do Movimento Uniformemente Variado
    velocidade_inicial -- Velocidade inicial do Movimento Uniformemente Variado
    tempo -- Tempo decorrido do Movimento Uniformemente Variado
    """
    aceleracao = (velocidade_final - velocidade_inicial) / tempo
    return aceleracao


def espaco_final_muv(espaco_inicial, velocidade_inicial, tempo, aceleracao):
    """ Fornecido o espaço inicial (m), velocidade inicial (m/s), tempo (s) e a aceleração (m/s²), retorna o espaço final.
    
    Argumentos:
    espaco_inicial -- Espaço inicial do Movimento Uniformemente Variado
    velocidade_inicial -- Velocidade inicial do Movimento Uniformemente Variado
    tempo -- Tempo decorrido do Movimento Uniformemente Variado
    aceleracao -- Aceleração do Movimento Uniformemente Variado
    """
    espaco_final_muv = espaco_inicial + velocidade_inicial * tempo + (aceleracao * tempo ** 2)/2
    return espaco_final_muv
```


```python title="Terminal - python -i formulas_muv.py"
help(aceleracao_muv)
```

```txt title='help interativo'
Help on function aceleracao_muv in module __main__:

aceleracao_muv(velocidade_final, velocidade_inicial, tempo)
    Fornecido a velocidade final (m/s), velocidade inicial (m/s) e o tempo (s), retorna a aceleração do movimento uniformemente variado (m/s²).

    Argumentos:
    velocidade_final -- Velocidade final do Movimento Uniformemente Variado
    velocidade_inicial -- Velocidade inicial do Movimento Uniformemente Variado
    tempo -- Tempo decorrido do Movimento Uniformemente Variado
```


```python title="Terminal - python -i formulas_muv.py"
# Calculando a aceleração de um objeto móvel de velocidade final 10 m/s, velocidade inicial de 2 m/s decorridos 5 segundos.
aceleracao_muv(10, 2, 5)
1.6
```



## Entrada de teclado

Para interagirmos com nossas funções estamos passando seu argumento manualmente.

Podemos fazer isso de maneira mais interativa, no sentido de que o próprio usuário que está interagindo com a função carregue seus argumentos.

O Python fornece uma função integrada chamada `input` que interrompe o programa e espera que usuário digite algo.

Quando o usuário pressionar Enter, o programa volta a ser executado e input, que é uma função **retorna** o que o usuário digitou como uma string.

```python
>>> texto = input()
Teste de texto
>>> texto
'Teste de texto'
```


A função `input` tem como parâmetro uma string que é exibida ao usuário como orientação, a chamamos de argumento prompt.

```python
>>> nome = input('Insira seu nome: ')
Insira seu nome: Everson
>>> nome
'Everson'
```


Podemos passar por meio de uma variável o argumento prompt

```python
>>> mensagem_usuario_nome = 'Insira seu nome: '
>>> nome = input(mensagem_usuario_nome)
Insira seu nome: Everson
>>> nome
'Everson'
```


Se `input` retorna um valor do tipo string, como fazer entradas numéricas?

Basta usar as funções que convertem valores.

```python
>>> idade = int(input('Insira sua idade: '))
29
>>> idade
29
>>> type(idade)
<class 'int'>
>>> idade
29
```


