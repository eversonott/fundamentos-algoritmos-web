# Aula 15 - Tuplas e Revisão
---
## Tuplas

Em Python além de listas e dicionário, existe uma outra classe de coleções, contanier e estrutura de
dados nativa que são as tuplas.

A tupla se comporta como uma lista, porém são imutáveis. Um objeto do tipo "tuple"contém uma
sequência de valores separados por vírgulas e delimitados por parênteses (()) em vez de colchetes([]).

```python
>>> dias = ( 'Seg' , 'Ter' , 'Qui' )
>>> dias
('Seg', 'Ter', 'Qui')
```

```python
>>> type(dias)
<class 'tuple'>
```

Podemos utilizar o operador de indexação para acessar itens da tupla 
usando o deslocamento do item como índice, assim como fizemos com os 
objetos de uma lista.

```python
>>> dias[2]
'Qui'
```

Também é possível realizar fatiamento, uma vez que os itens são ordenados.

```python
>>> dias[0:2]
('Seg', 'Ter')
```

Como são objetos imutáveis, a tentativa de mudar o objeto "tuple"ou de inclusão de novos itens
não é permitida.

Podemos usar a atribuição de tuplas para guardar os elementos 
separadamente:

Ao percorrer um dicionário usando uma instrução for e o método de dicionário "items()", obtemos

```python
horario_vago = {'Dia da semana': 'Quarta', 'Período': 'Manhã', 'Horário inicial': 9, 'Horário final': 11}
for horario in horario_vago.items():
    type(horario)
<class 'tuple'>
<class 'tuple'>
<class 'tuple'>
<class 'tuple'>
```

Portanto podemos utilizar os elementos de `items()` de maneira separada.

```python
for chave, valor in horario_vago.items():
    print(f'{chave}: {valor}')
...
Dia da semana: Quarta
Período: Manhã
Horário inicial: 9
Horário final: 11
```

## Proposta de revisão do módulo 1

Criar uma aplicação utilizando todos os conceitos trabalhados em aula e apreendidos, que ofereça as quatro operações básicas:

- Criar
- Ler
- Atualizar
- Deletar

Nosso acrônimo em português, é CLAD, mais conhecido como: CRUD (Create, Read, Update e Delete).

## Inspiração

- Objetos:
    - Administrador
    - Usuário
    - Aplicação (Regra de negócio)
        - Exemplos:
            - "Calculadoras matemáticas"
            - Sistemas de gerenciamento
                - Notas
                - Compras
                - Agenda


## Funcionalidades - Interfaces

- Administrativas

- Usuários 

Sejam criativos!
