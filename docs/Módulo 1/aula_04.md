
marp: true
theme: rose-pine
style: |
  .columns {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1rem;
  }

# Aula 04 - Novos operadores e manipulação de scripts em Python

Fundamentos de algoritmos e introdução à programação em Python

Prof. Everson Otoni


## Novos operadores - Divisão por piso e módulo

O operador de **divisão pelo piso**, `//`, divide dois números e arredonda o resultado para um número inteiro para baixo.


Por exemplo, suponha que o tempo de execução de um filme seja de 105 minutos.

Podemos querer saber a quanto isso corresponde em horas.

Usando a divisão convencional, temos um ponto flutuante como resposta.


```python
>>> minutos_total_filme = 105
>>> minutos_total_filme / 60
1.75
```


 

Não é comum escrever horas com números decimais. 

A divisão pelo piso devolve o número inteiro de horas, ignorando a parte fracionária.

```python
>>> minutos_total_filme = 105
>>> horas_filme = minutos_filme // 60
>>> horas_filme
1
```




Se ainda queremos obter o restante, podemos subtrair a hora inteira recém descoberta da quantidade inicial de minutos:

```python
>>> minutos_restante_filme = minutos_total_filme - horas_filme * 60
>>> minutos_restante_filme
45
```




Uma alternativa para descobrir os minutos restante, seria usar o **operador módulo**, %, que divide dois números e devolve o resto.

```python
>>> minutos_restante_filme = minutos_total_filme % 60
>>> minutos_restante_filme
45
```

Perceba que apenas utilizando os novos operadores conseguiríamos responder a pergunta inicial, em duas instruções.

```python
>>> minutos_total_filme = 105
>>> minutos_total_filme // 60
1
>>> minutos_total_filme % 60
45
```



## Novos operadores - Módulo

O operador por módulo é mais útil do que parece.

É possível, por meio de seu uso verificar se um número é divisível por outro.

Se `x % y` for zero, então x é divisível por y.

Também é possível extrair o dígito ou dígitos mais à direita de um número.

Por exemplo, `x % 10` produz o dígito mais à direita de x (na base 10).
Da mesma forma que `x % 100` produz os dois últimos dígitos.



## IDLE - (Slide da primeira aula) 

O instalador do Python para Windows contém o módulo IDLE por padrão.

IDLE é um Ambiente de Desenvolvimento e Aprendizagem Integrado.

Para iniciar o shell interativo IDLE, procure o ícone IDLE no menu Iniciar e clique duas vezes nele.

![w:450](https://raw.githubusercontent.com/eversonott/fundamentos-algoritmos/main/slides/md/imagens/idle.png)



## IDLE - (Slide da primeira aula) 

Onde efetivamente, o *interpretador* Python, um programa. Lê e executa o código Python.

![w:500](https://raw.githubusercontent.com/eversonott/fundamentos-algoritmos/main/slides/md/imagens/idle_uso.gif)



## Prática!



