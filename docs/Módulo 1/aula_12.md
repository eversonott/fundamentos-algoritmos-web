---
search:
  exclude: true
---
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
# Aula 10 - Instrução For
Fundamentos de algoritmos e introdução à programação em Python 

Prof. Everson Otoni

---

## Iteração - Instrução For

Uma tarefa comum a todas as sequências é realizar uma ação sobre cada objeto.

Por exemplo, poderíamos percorrer uma lista de compras para verificar se comprou tudo o que está nela.

Poderíamos percorrer uma lista de filmes (serviço de streaming) e verificar se foram assistidos ou não, ou se são de determinado gênero ou não.

Podemos também percorres um nome a fim de soletrá-lo.

---


Como podemos implementar um programa que soletre um string digitada pelo usuário?

Algo como:

```Python
>>>
Digite uma palavra: Ariel
A palavra soletrada:
A
r
i
e
l
```

---


Precisamos de um método que nos permitirá executar uma instrução `print()` para cada caractere da string.

Para isso iremos utilizar a instrução de laço `for`.


```Python
palavra = input('Digite uma palavra: ')
print('A palavra soletrada: ')

for caractere in palavra:
    print(caractere)
```

---


```Python
>>> for caractere in palavra:
...     print(caractere)
...
```

`caractere` é um nome de variável.

A instrução de laço `for` atribuirá repetidamente os caracteres (itens) da string `palavra` à variável `caractere`.

Se a palavra for a string `'Ariel'`, `caractere` primeiro terá o valor `'A'`, depois `'r'`, depois `'i'`, depois `'e'` e por fim `'l'`.

Para cada valor de `caractere`, a instrução endentada `print(caractere)` é executada.

---



---


O laço `for` portanto percorre os itens de uma lista.

Por exemplo, para percorrer os objetos de string representando os animais de estimação:

```Python
>>> animais = ['peixe', 'gato', 'cachorro']
>>> for animal in animais:
...     print(animal)
...
peixe
gato
cachorro
```

O laço `for` executa a seção endentada `print(animal)` três vezes, uma para cada valor de animal.

O valor é primeiro `peixe`, depois `gato` e, por fim `cachorro`.


---


## A variável do Laço for

A variável `caractere` em

```Python
>>> for caractere in palavra:
...     print(caractere)
...
```

E a variável `animal` em

```Python
>>> for animal in animais:
...     print(animal)
...
```

---

## Iteração - Instrução For


São apenas nomes de variável, escolhidos para tornar o programa mais significativo. Poderíamos ter escrito os laços da mesma com, digamos, o nome de variável `x`:

```Python
>>> for x in palavra:
...     print(x)

>>> for x in animais:
...     print(x)
```

Ao mudarmos o nome da variável do laço `for`, também precisamos mudar qualquer ocorrência dela no corpo do laço `for`.

---


```Python
for <variável> in <sequência>:
    <bloco de código endentado>
<bloco de código não endentado>
```

O laço `for` atribuirá com sucesso objetos de <sequência> à <variável>, na ordem em que aparecem da esquerda para a direita.

O <bloco de código endentado>, normalmente denominado `corpo` do laço `for`, é executado uma vez para cada valor de <variável>.

Dizemos que o laço `for` percorre os objetos na sequência.

Após o <bloco de código endentado> ter sido executado pela última vez, a execução retoma com as instruções após laço `for`.

E o <bloco de código não endentado> é executado.

---


Vamos combinar o laço `for` com uma instrução `if`.

Nossa proposta é escrever uma aplicação que comece pedindo ao usuário para digitar uma frase.

Depois que ele fizer isso, o programa exibirá todas as vogais, e nenhuma outra letra.\

```Python
>>>
Digite uma frase: caso de teste
a
o
e
e
e
```

---


- Precisamos de uma instrução `input()` para ler a frase.
- Um laço `for` para percorrer os caracteres da string de entrada 
- E, cada iteração do laço, uma instrução `if` para verificar se o caractere atual é uma vogal. Se for, ele é impresso.

---

## Função range(stop) ou range(start, stop, step=1)

Com frequência necessitamos percorrer uma sequência de números em determinado intervalo, mesmo que a lista de números não seja dada explicitamente.

Seus argumentos devem ser sempre inteiros.

Se o argumento `step` for omitido, será usado o padrão 1.

Se o argumento `start` for omitido, será usado o padrão 0.

Se step for zero, uma exceção `ValueError` será retornada.

---


A função `range(n)` normalmente é usada para percorrer a sequência de inteiros `0, 1, 2, ..., n - 1.1

```Python
>>> for i in range(10):
...     print(i)
...
0
1
2
3
4
5
6
7
8
9
```

---


Se quisermos que a sequência comece em determinado número diferente de zero `start` (início) e termine **antes** do número `stop` (fim):
```Python
>>> for i in range(1,11):
...     print(i)
...
1
2
3
4
5
6
7
8
9
10
```

---


Podemos percorrer a sequência de inteiros começando em `start` (ínicio), usando um tamanho de `step` (passo) e terminando antes do número `stop` (fim).

```Python
>>> for i in range(0, 30, 5):
...     print(i)
...
0
5
10
15
20
25
```

---


```Python
>>> for i in range(0, -10, -1):
...     print(i)
...
0
-1
-2
-3
-4
-5
-6
-7
-8
-9
```

---



A função range não gera uma lista e sim uma sequência numérica. Mais especificamente, progressões aritméticas.

Portanto se comporta como uma lista, mas na verdade não é.

---



A vantagem do tipo `range` sobre um `list`, por exemplo é que um objeto `range` sempre terá a mesma quantidade (pequena) de memória, não importa o tamanho do intervalo o mesmo esteja representado, já que ele apenas armazena os valores `start`, `stop` e `step`, calculando itens individuais e subintervalos conforme necessário).

---


Podemos gerar listas de sequências numéricas, utilizando o `range` e a função embutida que converte em lista (`list`).

```Python
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

```Python
>>> list(range(1,11))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

```Python
>>> list(range(0,30,5))
[0, 5, 10, 15, 20, 25]
```

```Python
>>> list(range(0, -10, -1))
[0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
```

---

## Padrões de uso - Laço de Iteração 

Já usamos o laços para apenas percorrer os caracteres de uma string:

```Python
>>> palavra = 'Ariel'
>>> for caractere in palavra:
... print(caractere)
...
A
r
i
e
l
```

---


Já usamos o laços para apenas percorrer os itens de uma lista:

```Python
>>> animais = ['peixe', 'gato', 'cachorro']
>>> for animal in animais:
...     print(animal)
...
peixe
gato
cachorro
```

---



Percorrer uma sequência explícita de valores e realizar alguma ação sobre cada valor é o padrão de uso mais simples para um laço, porém muito mais simples para um laço `for` do que um laço `while`.


```Python
>>> frutas = ['banana', 'maça', 'pera', 'laranja']
>>> indice = 0
>>> while indice < len(frutas):
...     fruta = frutas[indice]
...     print(fruta)
...     indice = indice + 1
...
banana
maça
pera
laranja
```
---


Esse loop atravessa a lista de frutas e exibe cada fruta sozinha em uma linha.

A condição do loop é `index < len(frutas)`.

Quando `indice` é igual ao comprimento da lista, a condição é falsa e o corpo do loop não é mais executado.
O último item acessado é aquele com índice `len(frutas) - 1`, que é o útimo item na lista.

---


Para percorerr os itens de uma lista e exibi-los usando for:


```Python
>>> for fruta in frutas:
...     print(fruta)
...
banana
maça
pera
laranja
```

---

## Padrões de uso - Laço Contador

Outro padrão de laço que podemos usar é a repetição por uma sequência de inteiros, especificada com a função `range()`:


```Python
>>> for numero in range(10):
...     print(numero, end=' ')
...     0 1 2 3 4 5 6 7 8 9
...
```

Usamos esse padrão, quando precisamos executar um bloco de código para cada inteiro em algum intervalo (range).

---

Por exemplo, para encontrar e exibir todos os números pares de 0 até algum inteiro qualquer:

```Python
>>> limite = 10
>>> for numero in range(10):
...     if numero % 2 == 0:
...         print(numero, end = ' ')
...
0 2 4 6 8
```

---

## Padrões de uso - Laço Acumulador

Um padrão comum nos laços é acumular "alguma coisa" em cada iteração do laço.

Dada uma lista de números, por exemplo, poderíamos querer somar os números.

Para fazer isso usando um laço `for`, primeiro precisamos introduzir uma variável que manterá a soma. Essa variável é inicializada em 0; depois, um laço `for` pode ser usado para percorrer os números da lista e somá-los a variável.

```Python
>>> pontuacao = [3, 2, 7, -1, 9]
>>> minhaSoma = 0 ## Inicializando o acumulador
>>> for numero in pontuacao:
...     minhaSoma = minhaSoma + numero
...
>>> minhaSoma
20
```

---

---



# Aula 11 - Dicionários e tuplas
Fundamentos de algoritmos e introdução à programação em Python 

Prof. Everson Otoni

---

## Dicionários

Em uma lista temos índices que têm que ser números inteiros, em um dicionário, eles podem ser de **quase** qualquer tipo.

---


Um dicionário contém uma coleção de índices, que se chamam **chaves** e uma coleção de **valores**. 

Cada chave é associada com um único valor.

A associação de uma chave e um valor chama-se **par chave-valor** ou **item**.

---

## Índices definidos pelo usuário

Suponha que tenhamos que armazenar registros para uma empresa com 50000 funcionários.

O ideal é que possamos processar o registro de cada empregado usando apenas um número de identificação, como CPF ou RG ou um número de cadastro, da seguinte forma:

```Python
>>> funcionario[987654321]
['Isaac', 'Asimov']
>>> funcionario[864209753]
['Marie', 'Curie']
>>> funcionario[100010010]
['Mario', 'Puzo']
```

---



No índice 987654321, é armazenado o nome o sobrenome do funcionário com o identificador 987-65-4321, Isaac Asimov. 

O nome e sobrenome são armazenados em uma lista que poderia conter informações adicionais, como endereço, data de nascimento, cargo e assim por diante.

Nos índices 864209753 e 100010010, serão armazenados os registros para ['Marie', 'Curie'] e ['Mario', 'Puzo'].

Em geral, no índice **i**, estará armazenado o registro (nome e sobrenome) do funcionário com identificador **i**.

---


Se `funcionario` fosse uma **list**, precisaríamos ter uma lista muito grande. Ela precisaria ser maior que o valor inteiro do maior identificador de empregado.

Os nossos identificadores possuem nove dígitos. Portanto `funcionario` precisaria ter o tamanho de 1 000 000 000.

Isso já é grande, mesmo que possamos acomodar uma lista tão grande, ela seria um desperdiço, já que a maior parte da lista estará vazia. Somente 50 mil posições da lista serão usadas.

---


Outro problema com as listas é que nossos números de identificação não são realmente valores inteiros, pois são indicados usando hifens, como 987-65-4321, e podem começar com 0, como 012-34-5678.

Esses valores são melhores representados por meio de string.

O problema é que os itens de lista têm como finalidade serem acessados usando um índice inteiro que representa a posição do item em um conjunto.

O que queremos portanto, é acessar itens usando "índices definidos pelo usuário", como '864-20-9753' ou '987-65-4321'.

O tipo embutido, denominado **dicionário** nos permite usar esses índices.

---


```Python
>>> funcionario = {
    '987-65-4321': ['Isaac', 'Asimov'],
    '864-20-9753': ['Marie', 'Curie'],
    '100-01-0010': ['Mario', 'Puzo']
}
```

Escrevemos a instrução usando múltiplas linhas para enfatizar que o "índice" '987-65-4321' corresponde ao valor ['Isaac', 'Asimov'], o "índice" '864-20-9753' corresponde ao valor ['Marie', 'Curie'], o "índice" '100-01-0010' corresponde ao valor ['Mario', 'Puzo'] e assim por diante.

---


Vamos verificar se o dicionário `funcionario` funciona como desejamos:

```Python
>>> funcionario['987-65-4321']
['Isaac', 'Asimov']
>>> funcionario['864-20-9753']
['Marie', 'Curie']
```

O dicionário difere de uma lista porque um item em um dicionário é acessado usando um "índice" especificado pelo usuário, em vez do índice representando a posição dos itens em um conjunto.

---

## Propriedades

O tipo de dicionário em Python, indicado por **dict**, é um tipo de contêiner ou estrutura de dados, assim como **list** e **str**.

Um dicionário contém pares de (chave, valor). Como mencionamos inicialmente.

O formato geral da expressão avaliada como um objeto dicionário é:
`{<chave 1 > : <valor 1>, <chave 2> : <valor 2>, ..., <chave i > : <valor i>,}`

---


A **chave&& e o **valor** são ambos objetos objetos.

A **chave** é o "índice" usado para acessar o **valor**.

Assim, em nosso dicionário `funcionario` '100-01-0010' é a chave e ['Mario', 'Puzo'] é o valor.

Os pares (chave, valor) em uma expressão do dicionário são separados por vírgulas e delimitados em chaves ({}) (em vez de colchetes [], usados para as listas).

---


A chave e valor em cada par de (chave, valor) são separados por um sinal de dois pontos (:), com a chave estando à esquerda e o valor à direita dos dois pontos.

As chaves podem ser de qualquer tipo, desde que o tipo seja imutável (não mude).
Objetos de string e numéricos podem ser chaves, enquanto objetos do tipo **list** não podem.

O valor pode ter qualquer tipo.

---


Frequentemente dizemos que uma chave **mapeia** se valor ou é o índice de seu valor.

Como dicionários podem ser vistos como um mapeamento entre chaves e valores, em geral, são chamados de **mapas**.

Temos abaixo, um dicionário mapeando abreviações de dia da semana 'Seg', 'Ter', 'Qua', 'Qui' (as chaves) aos dias correspondentes 'Segunda', 'Terça', 'Quarta' e 'Quinta' (os valores):

```Python
>>> dias = {'Seg':'Segunda', 'Ter':'Terça', 'Qua':'Quarta ', 'Qui':'Quinta'}
```

---


Os valores no dicionário são acessados por chave, e não por índice (ou deslocamento). 

Para acessar o valor 'Quarta' no dicionário dias, usamos a chave 'Qua':

```Python
>>> dias['Qua']
'Quarta'
```
E não índice 2.

```Python
>>> dias[2]
Traceback (most recent call last):
  File "<python-input-6>", line 1, in <module>
    dias[2]
    ~~~~^^^
KeyError: 2
```
A exceção KeyError nos diz que estamos usando uma chave ilegal, nesse caso, indefinida

---


Os pares (chave, valor) no dicionário não são ordenados, e nenhuma hipótese de ordenação pode ser feita.

Dicionários são mutáveis, assim como as listas. Um dicionário pode ser modificado para conter um novo par de (chave, valor):

```Python
>>> dias['Sex'] = 'sexta'
>>> dias
{'Seg': 'Segunda', 'Ter': 'Terça', 'Qua': 'Quarta ', 'Qui': 'Quinta', 'Sex': 'sexta'}
```

Isso implica que os dicionários possuem tamanho dinâmico.

---


O dicionário também pode ser modificado de modo que uma chave existente se refira a um novo valor:

```Python
>>> dias['Sex'] = 'Sexta'
>>> dias
{'Seg': 'Segunda', 'Ter': 'Terça', 'Qua': 'Quarta ', 'Qui': 'Quinta', 'Sex': 'Sexta'}
```

Um dicionário vazio pode ser definido usando o construtor padrão dict() ou simplesmente como:

```Python
>>> d = {}
>>> c = dict()
>>> d
{}
>>> c
{}
```

---

## Operadores

A classe de dicionário aceita alguns dos mesmos operadores que a classe de lista aceita. Já vimos que o operador de indexação ([]) pode ser usado para acessar um valor usando a chave como índice:

```Python
>>> dias['Qua']
'Quarta'
```

O operador de indexação também pode ser usado para alterar o valor correspondente a uma chave ou incluir um novo par de (chave, valor) ao dicionário:

```Python
>>> dias
{'Seg': 'Segunda', 'Ter': 'Terça', 'Qua': 'Quarta ', 'Qui': 'Quinta', 'Sex': 'Sexta'}
>>> dias['Sab'] = 'Sábado'
>>> dias
{'Seg': 'Segunda', 'Ter': 'Terça', 'Qua': 'Quarta ', 'Qui': 'Quinta', 'Sex': 'Sexta', 'Sab': 'Sábado'}
'Quarta'
```

---


O tamanho de um dicionário (ou seja, o número de pares [chave, valor] existentes) pode ser obtido usando a função len:

```Python
>>> len(dias)
6
```

Os operadores in e not in são usados para verificar se um objeto é uma **chave** no dicionário:

```Python
>>> 'Sex' in dias
True
>>> 'Sexta' in dias ## 'Sexta' é um valor não uma chave.
False
>>> 'Dom' in dias
False
>>> 'Dom' not in dias
True
```

---


Existem operadores que a classe list aceita, mas a classe dict não. 

Por exemplo, o operador de indexação [] não pode ser usado para obter um pedaço de um dicionário. 
Isso faz sentido: um pedaço implica uma ordem, e não há ordem em um dicionário. 

Também não são aceitos os operadores + e *, entre outros.

---

## Métodos

Embora as classes list e dict compartilhem muitos operadores, há somente um método que elas compartilham: 
pop(chave). 

Esse método aceita uma chave e, se a chave estiver no dicionário, ele remove o par de (chave, valor) associado do dicionário
e retorna o valor:

```Python
>>> dias
{'Seg': 'Segunda', 'Ter': 'Terça', 'Qua': 'Quarta ', 'Qui': 'Quinta', 'Sex': 'Sexta', 'Sab': 'Sábado'}
```

```Python
>>> dias.pop('Ter')
'Terça '
>>> dias.pop('Sex')
'Sexta'
>>> dias
{'Seg': 'Segunda', 'Qua': 'Quarta ', 'Qui': 'Quinta', 'Sab': 'Sábado'}
```

---

### update(iterable)

`iterable`: 
    Um dicionário ou objeto iterável com pares de chave-valor, que será inserido no dicionário.

Quando o dic d1 chama o método update() com o dicionário do argumento de entrada d2, todos os pares (chave, valor) de d2 são acrescentados a d1, possivelmente escrevendo sobre pares (chave, valor) de d1.


```Python
>>> dias
{'Seg': 'Segunda', 'Qua': 'Quarta ', 'Qui': 'Quinta', 'Sab': 'Sábado'}
```

```Python
>>> favoritos = {'Qui':'Quinta', 'Sex':'Sexta ','Sab':'Sáb'}
>>> dias.update(favoritos)
>>> dias 
{'Seg': 'Segunda', 'Qua': 'Quarta ', 'Qui': 'Quinta', 'Sab': 'Sáb', 'Sex': 'Sexta '}
```


---


```Python
>>> dias 
{'Seg': 'Segunda', 'Qua': 'Quarta ', 'Qui': 'Quinta', 'Sab': 'Sáb', 'Sex': 'Sexta '}
```

O par de (chave, valor) 'Sex':'Sexta' foi acrescentado a `dias`.

E o par de (chave, valor) 'Sab':'Sáb' substituiu o par 'Sab':'Sábado', originalmente no dicionário `dias`.

Observe que somente uma cópia do par de (chave, valor) 'Qui':'Quinta' pode estar no dicionário.


---

### keys(), values() e items()

Métodos de dicionário particularmente úteis são keys(), values() e items(): eles retornam chaves, valores e pares (chave, valor), respectivamente, no dicionário.

```Python
>>> dias 
{'Seg': 'Segunda', 'Qua': 'Quarta ', 'Qui': 'Quinta', 'Sab': 'Sáb', 'Sex': 'Sexta '}
```

O método keys() retorna as chaves do dicionário:
```Python
>>> chaves = dias.keys()
>>> chaves
dict_keys(['Seg', 'Qua', 'Qui', 'Sab', 'Sex'])
```
O objeto retornado pelo método keys() não é uma lista. Vamos verificar seu tipo:
```Python
>>> type(chaves)
<class 'dict_keys'>
```

---


Vamos entender o uso desse novo tipo `<class 'dict_keys'>`:

Normalmente esse tipo de objeto é usado para percorrer as chaves do dicionário, por exemplo:

```Python
>>> for chave in dias.keys():
...     print(chave)
...
Seg
Qua
Qui
Sab
Sex
```

Assim, a classe `dict_keys` aceita iteração.

---



Os métodos de dicionário values() e itens() também retornam objetos que podemos percorrer.

O método values() normalmente é usado para percorrer os valores de um dicionário:
```Python
>>> for valor in dias.values():
...     print(valor)
...
Segunda
Quarta
Quinta
Sáb
Sexta
```

---



O método items() normalmente é usado para percorrer os pares (chave, valor) do dicionário:

```Python
>>> for item in dias.items():
...     print(item)
...
('Seg', 'Segunda')
('Qua', 'Quarta ')
('Qui', 'Quinta')
('Sab', 'Sáb')
('Sex', 'Sexta ')
```

Os pares (chave, valor) no contêiner obtido avaliando dias.items() aparecem em um formato que ainda não vimos.

Esse formato é uma representação de um objeto contêiner do tipo tuple,

---

## Substituto para a Condição Multivias

Quando apresentamos os dicionários, nossa motivação foi a necessidade de um contêiner com índices definidos pelo usuário.

Mas há outros usos alternativos para os dicionários.

Suponha que quiséssemos desenvolver uma pequena função, chamada `complete()`, que aceite a abreviação de um dia da semana, como 'Ter', e retorne o dia correspondente, que para a entrada 'Ter' seria 'Terça', algo como:

```Python
>>> complete('Ter')
'Terça'
```

---


Uma forma de implementar a função seria usar uma instrução if multivias:

```Python
def complete(abreviacao):
    'retorna dia da semana correspondente à abreviação'
    if abreviacao == 'Seg':
        return 'Segunda'
    elif abreviacao == 'Ter':
        return 'Terça '
    elif ...
        ...
    else: ## abreviação deve ser Dom
        return 'Domingo'
```

---



O problema principal com a implementação é que ela simplesmente exagera usando uma instrução if de sete vias para implementar o que, na realidade, é um “mapeamento” entre abreviações de dia e os dias correspondentes da semana. 

Agora já sabemos como implementar esse mapeamento usando um dicionário:


```Python
def complete(abreviacao):
    dias = {'Seg': 'Segunda', 'Ter':'Terça', 'Qua':'Quarta', 
    'Qui': 'Quinta', 'Sex': 'Sexta', 'Sab': 'Sábado', 'Dom':'Domingo'}
    return dias[abreviacao]
```

---

## Coleção de contadores

Uma aplicação importante do tipo de dicionário é seu uso no cálculo do número de ocorrências de “coisas” em um conjunto maior.

Um mecanismo de busca, por exemplo, pode ter que calcular a frequência de cada palavra em uma página Web a fim de calcular sua relevância em relação às consultas ao mecanismo de busca.

---


Em uma escala menor, suponha que queiramos contar a frequência de cada nome em uma lista de nomes de estudante, como esta:


```Python
>>> estudantes = ['Yuri', 'Marco', 'Brenno', 'Maria', 'Franklin', 'Franklin', 'Marco', 'Gustavo', 'Marco']
```

Mais precisamente, gostaríamos de implementar uma função `frequencia()`, que aceite uma lista como estudantes na entrada e calcule o número de ocorrências de cada item distinto da lista.

---


Como é comum, existem diferentes maneiras de implementar a função `frequencia()`. 

Contudo, a melhor maneira é criar um contador para cada item distinto na lista e depois percorrer os itens na lista: para cada item visitado, o contador correspondente é incrementado. 

Para que isso funcione, precisamos responder a três perguntas:

1. Como saber quantos contadores precisamos?
2. Como armazenamos todos os contadores?
3. Como associamos um contador a um item da lista?


---



1. Como saber quantos contadores precisamos?

Não se preocupe com a quantidade de contadores que precisamos, vamos criá-los dinamicamente, conforme a necessidade.

Em outras palavras, criamos um contador para um item somente quando, ao
percorrermos a lista, encontrarmos o item pela primeira vez.


---



2. Como armazenamos todos os contadores?
3. Como associamos um contador a um item da lista?


Podemos usar um dicionário para armazenar os contadores. Cada contador de item será um valor no dicionário, e o próprio item será a chave correspondente ao valor. 

Por exemplo, a string 'Yuri' seria a chave e o valor correspondente seria seu contador. O mapeamento do dicionário entre chaves e valores também responde à terceira pergunta.

---


Agora, também podemos decidir o que a função `frequencia()` deverá retornar: 
- Um dicionário mapeando cada item distinto na lista ao número de vezes que ele ocorre na lista:


```Python
>>> estudantes = ['Yuri', 'Marco', 'Brenno', 'Maria', 'Franklin', 'Franklin', 'Marco', 'Gustavo', 'Marco']
>>> frequencia(estudantes)
{'Yuri': 1, 'Marco': 3, 'Brenno': 1, 'Maria': 1, 'Franklin':2, 'Gustavo': 1}
```



