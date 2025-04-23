---
search:
  exclude: true
---
# Aula 08 - Selenium

{% set aula = "08" %}
{% set link = "I8Zh1HwhAIQ" %}
{% set codigos = false %}
{% set pesquisas = false %}
{% set slides = false %}
{% set objetivos = [""]%}
{% include "templates/cabecalho.md" %}

---
## Conceito

Selenium é um projeto que abrange uma variedade de ferramentas e bibliotecas que permitem e suportam a automação de navegadores da web.

Ele fornece extensões para emular a interação do usuário com os navegadores, um servidor de distribuição para escalonar a alocação do navegador, e a infraestrutura para implementações da Especificação W3C WebDriver que permite escrever código intercambiável para todos os principais navegadores da web.

### W3C WebDriver

WebDriver é uma interface de controle remoto que permite a introspecção e o controle dos agentes do usuário. Ele fornece um protocolo de conexão neutro em plataforma e idioma como uma forma de programas fora de processo para instruir remotamente o comportamento dos navegadores da web.

É fornecido um conjunto de interfaces para descobrir e manipular elementos DOM em documentos da web e para controlar o comportamento de um agente de usuário. Destina-se principalmente a permitir que autores da web escrevam testes que automatizam um agente de usuário a partir de um processo de controle separado, mas também pode ser usado de forma a permitir scripts no navegador para controlar um navegador - possivelmente separado.

## WebDriver Selenium

O WebDriver manipula um navegador nativamente, como um usuário faria, seja localmente ou em uma máquina remota usando o servidor Selenium, marca um salto em termos de automação do navegador.

Selenium WebDriver refere-se a ambas as ligações de linguagem e as implementações do código de controle do navegador individual. Isso é comumente referido como apenas WebDriver.


### Elemento Web

#### Encontrando Elementos Web

Localizando elementos com base nos valores providenciados pelo localizador.

Um dos aspectos mais fundamentais do uso do Selenium é obter referências de elementos para trabalhar. O Selenium oferece várias estratégias de localizador para identificar exclusivamente um elemento. Há muitas maneiras de usar os localizadores em cenários complexos. Para os propósitos desta documentação, vamos considerar este trecho de HTML:



```html
<ol id="vegetables">
 <li class="potatoes">…
 <li class="onions">…
 <li class="tomatoes"><span>O tomate é um vegetal</span>…
</ol>
<ul id="fruits">
  <li class="bananas">…
  <li class="apples">…
  <li class="tomatoes"><span>O tomate é uma fruta</span>…
</ul>
```

##### Primeiro Elemento correspondente

Muitos localizadores irão corresponder a vários elementos na página. O método de elemento de localização singular retornará uma referência ao primeiro elemento encontrado dentro de um determinado contexto.



###### Avaliando o DOM inteiro

Quando o metodo find element é chamado na instância do driver, ele retorna uma referência ao primeiro elemento no DOM que corresponde ao localizador fornecido. Esse valor pode ser guardado e usado para ações futuras do elemento. Em nosso exemplo HTML acima, existem dois elementos que têm um nome de classe de “tomatoes” então este método retornará o elemento na lista “vegetables”.

```py title='Terminal'
vegetable = driver.find_element(By.CLASS_NAME, "tomatoes")
```


###### Avaliando um subconjunto do DOM

Ao em vez de tentar encontrar um localizador unico no DOM inteiro, normalmente é útil restringir a busca ao escopo de outro elemento já localizado. No exemplo acima existem dois elementos com um nome de classe de “tomatoes” e é um pouco mais desafiador obter a referência para o segundo.

Uma possível solução seria localizar um elemento com um atributo único que seja um ancestral do elemento desejado e não um ancestral do elemento indesejado, então invoque o find element nesse objeto:

```py
fruits = driver.find_element(By.ID, "fruits")
fruit = fruits.find_element(By.CLASS_NAME,"tomatoes")
```

###### Localizador otimizado

Uma pesquisa aninhada pode não ser a estratégia de localização mais eficaz, pois requer dois comandos separados a serem emitidos para o navegador.

Para melhorar um pouco o desempenho, podemos usar CSS ou XPath para encontrar esse elemento com um único comando. Veja as sugestões de estratégia do localizador na nossa sessão de Práticas de teste incentivadas .

Para esse exemplo, utilizaremos o CSS Selector:

```py
fruit = driver.find_element(By.CSS_SELECTOR,"#fruits .tomatoes")
```


##### Todos os elementos correspondentes 

Existem vários casos de uso para a necessidade de obter referências a todos os elementos que correspondem a um localizador, em vez do que apenas o primeiro. Os métodos plurais find elements retornam uma coleção de referências de elementos. Se não houver correspondências, uma lista vazia será retornada. Nesse caso, referências a todos os itens da lista de frutas e vegetais serão retornadas em uma coleção.

```py
plants = driver.find_elements(By.TAG_NAME, "li")
```


###### Obter Elemento

Muitas vezes você obterá uma coleção de elementos, mas quer trabalhar apenas com um elemento específico, o que significa que você precisa iterar sobre a coleção e identificar o que você deseja.

```py
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

    # Navegar até a URL
driver.get("https://www.example.com")

    # Obtém todos os elementos disponiveis com o nome da tag 'p'
elements = driver.find_elements(By.TAG_NAME, 'p')

for e in elements:
    print(e.text)
```

##### Localizar Elementos em um Elemento

Ele é usado para localizar a lista de WebElements filhos correspondentes dentro do contexto do elemento pai. Para realizar isso, o WebElement pai é encadeado com o ‘findElements’ para acessar seus elementos filhos.

```py
## Obter elementos do elemento pai usando TAG_NAME 
    # Obtém o elemento com o nome da tag 'div'
element = driver.find_element(By.TAG_NAME, 'div')

    # Obtém todos os elementos disponíveis com o nome da tag 'p'
elements = element.find_elements(By.TAG_NAME, 'p')
for e in elements:
    print(e.text)

##obter elementos do elemento pai usando XPATH
##NOTA: para utilizar o XPATH do elemento atual, você deve adicionar "." para o início do caminho

    # Obtenha o primeiro elemento da tag 'ul'
element = driver.find_element(By.XPATH, '//ul')

    # obter filhos da tag 'ul' com a tag 'li'
elements  = driver.find_elements(By.XPATH, './/li')
for e in elements:
    print(e.text)
```

##### Obter elemento ativo

Ele é usado para rastrear (ou) encontrar um elemento DOM que tem o foco no contexto de navegação atual.

```py
  from selenium import webdriver
  from selenium.webdriver.common.by import By

  driver = webdriver.Chrome()
  driver.get("https://www.google.com")
  driver.find_element(By.CSS_SELECTOR, '[name="q"]').send_keys("webElement")

    # Obter atributo do elemento atualmente ativo
  attr = driver.switch_to.active_element.get_attribute("title")
  print(attr)
```

### Interagindo com os elementos

Um conjunto de instruções de alto nível para manipular controles de formulário.

Existem apenas 5 comandos básicos que podem ser executados em um elemento:

    clique (aplica-se a qualquer elemento)
    enviar chaves (aplica-se apenas a campos de texto e elementos editáveis ​​de conteúdo)
    claro (aplica-se apenas a campos de texto e elementos editáveis ​​de conteúdo)
    enviar (aplica-se apenas a elementos de formulário)
    select (veja Selecionar Elementos da Lista )

#### Validações adicionais
Esses métodos são projetados para emular de perto a experiência do usuário, portanto, ao contrário da Actions API , ela tenta realizar duas coisas antes de tentar a ação especificada.

1. Se determinar que o elemento está fora da janela de visualização, rola o elemento para view , especificamente isso alinhará a parte inferior do elemento com a parte inferior da janela de visualização.
    
2. Isso garante que o elemento seja interativo antes de tomar a ação. Isso pode significar que a rolagem não foi bem-sucedida ou que o elemento não é exibido de outra forma. Determinar se um elemento é exibido em uma página era muito difícil de definir diretamente na especificação do webdriver , então o Selenium envia um comando de execução com um átomo JavaScript que verifica coisas que manteriam o elemento seja exibido. Se determinar que um elemento não está na viewport, não é exibido, não interacionável com teclado ou não interativo com ponteiro , ele retorna um de elemento não interativo . erro

#### Clique

O comando de clique do elemento é executado em o centro do elemento. Se o centro do elemento estiver obscurecido por algum motivo, O Selenium retornará um erro de interceptação de clique no elemento.


```py
    # Navigate to url
driver.get("https://www.selenium.dev/selenium/web/inputs.html")

    # Click on the element 
driver.find_element(By.NAME, "color_input").click()
```

#### Enviar chaves

O comando elemento enviar chaves digita as chaves fornecidas em um editável elemento . Normalmente, isso significa que um elemento é um elemento de entrada de um formulário com um text tipo ou um elemento com um content-editable atributo. Se não for editável, um erro de estado de elemento inválido é retornado.

Aqui está a lista de possíveis pressionamentos de teclas que o WebDriver suporta.

```py
    # Navigate to url
driver.get("https://www.selenium.dev/selenium/web/inputs.html")

    # Clear field to empty it from any previous data
driver.find_element(By.NAME, "email_input").clear()

	# Enter Text
driver.find_element(By.NAME, "email_input").send_keys("admin@localhost.dev" )
```


#### Clear

O comando element clear redefine o conteúdo de um elemento. Isso requer que um elemento seja editável , e reconfigurável . Tipicamente, isso significa que um elemento é um elemento de entrada de um formulário com um text tipo ou um elemento com um content-editable atributo. Se estas condições não forem satisfeitas, um erro de estado de elemento inválido é retornado.

```py
    # Navigate to url
	driver.get("https://www.selenium.dev/selenium/web/inputs.html")

    # Clear field to empty it from any previous data
	driver.find_element(By.NAME, "email_input").clear()
```

### Localizando elementos

Formas de identificar um ou mais elementos no DOM.

Um localizador é uma forma de identificar elementos numa página. São os argumentos passados aos métodos Finders .

Visite os nossas diretrizes e recomendações para dicas sobre locators, incluindo quais usar e quando, e também porque é que deve declarar localizadores separadamente dos finders.

#### Estratégias de seleção de elemento

Existem oito estratégias diferentes de localização de elementos embutidas no WebDriver:

|Localizador|	Descrição|
|-----------||
|class name|	Localiza elementos cujo nome de classe contém o valor de pesquisa (nomes de classes compostas não são permitidos)|
|css selector|	Localiza elementos que correspondem a um seletor CSS|
|id|	Localiza elementos cujo atributo de ID corresponde ao valor de pesquisa|
|name|	Localiza elementos cujo atributo NAME corresponde ao valor de pesquisa|
|link text|	Localiza elementos âncora cujo texto visível corresponde ao valor de pesquisa|
|partial link text|	Localiza elementos âncora cujo texto visível contém o valor da pesquisa. Se vários elementos forem correspondentes, apenas o primeiro será selecionado.|
|tag name|	Localiza elementos cujo nome de tag corresponde ao valor de pesquisa|
|xpath|	Localiza elementos que correspondem a uma expressão XPath|


#### Estratégias de seleção de elemento

Para trabalhar em um elemento web usando Selenium, precisamos primeiro localizá-lo na página web. O Selenium nos fornece os métodos mencionados acima, com os quais podemos localizar o elemento no página. Para entender e criar o localizador usaremos o seguinte trecho de HTML.

```html
<html>
<body>
<style>
.information {
  background-color: white;
  color: black;
  padding: 10px;
}
</style>
<h2>Contact Selenium</h2>

<form action="/action_page.php">
  <input type="radio" name="gender" value="m" />Male &nbsp;
  <input type="radio" name="gender" value="f" />Female <br>
  <br>
  <label for="fname">First name:</label><br>
  <input class="information" type="text" id="fname" name="fname" value="Jane"><br><br>
  <label for="lname">Last name:</label><br>
  <input class="information" type="text" id="lname" name="lname" value="Doe"><br><br>
  <label for="newsletter">Newsletter:</label>
  <input type="checkbox" name="newsletter" value="1" /><br><br>
  <input type="submit" value="Submit">
</form> 

<p>To know more about Selenium, visit the official page 
<a href ="www.selenium.dev">Selenium Official Page</a> 
</p>

</body>
</html>
```

##### class name

O elemento da web da página HTML pode ter classe de atributo. Podemos ver um exemplo no trecho de HTML mostrado acima. Podemos identificar esses elementos usando o localizador de nome de classe disponível em selênio.


```py
driver = webdriver.Chrome()
driver.find_element(By.CLASS_NAME, "information")
```


##### css selector

CSS é a linguagem usada para estilizar páginas HTML. Podemos usar a estratégia de localizador de seletor css para identificar o elemento na página. Se o elemento tiver um id, criamos o localizador como css = #id. Caso contrário, o formato que seguimos é css =[attribute=value] . Vejamos um exemplo do snippet HTML acima. Criaremos um localizador para o primeiro nome caixa de texto, usando css.

```py
    driver = webdriver.Chrome()
	driver.find_element(By.CSS_SELECTOR, "#fname")
```

##### id
Podemos usar o atributo ID disponível com o elemento em uma página da web para localizá-lo. Geralmente a propriedade ID deve ser exclusiva para um elemento na página web. Iremos identificar o campo Sobrenome usando-o.


```py
driver = webdriver.Chrome()
driver.find_element(By.ID, "lname")
```

##### name
Podemos usar o atributo NAME disponível com o elemento em uma página da web para localizá-lo. Geralmente a propriedade NAME deve ser exclusiva para um elemento na página web. Identificaremos a caixa de seleção do boletim informativo usando-a.

```py
driver = webdriver.Chrome()
driver.find_element(By.NAME, "newsletter")
  
```

##### link text
Podemos usar o atributo NAME disponível com o elemento em uma página da web para localizá-lo. Geralmente a propriedade NAME deve ser exclusiva para um elemento na página web. Identificaremos a caixa de seleção do boletim informativo usando-a.

```py
driver = webdriver.Chrome()
driver.find_element(By.LINK_TEXT, "Selenium Official Page")
```

##### partial link text
Podemos usar o atributo NAME disponível com o elemento em uma página da web para localizá-lo. Geralmente a propriedade NAME deve ser exclusiva para um elemento na página web. Identificaremos a caixa de seleção do boletim informativo usando-a.


```py
driver = webdriver.Chrome()
driver.find_element(By.PARTIAL_LINK_TEXT, "Official Page")
```

##### tag name
Podemos usar a própria HTML TAG como localizador para identificar o elemento web na página. A partir do trecho HTML compartilhado acima, vamos identificar o link, usando sua tag html “a”.

```py
driver = webdriver.Chrome()
driver.find_element(By.TAG_NAME, "a")
```

##### xpath
Um documento HTML pode ser considerado um documento XML e então podemos usar XPath qual será o caminho percorrido para chegar ao elemento de interesse para localizar o elemento. O XPath pode ser um xpath absoluto, criado a partir da raiz do documento. Exemplo - /html/form/input[1]. Isso retornará o botão de opção masculino. Ou o xpath pode ser relativo. Exemplo- //input[@name='fname']. Isso retornará o caixa de texto do primeiro nome. Vamos criar um localizador para botão de opção feminino usando XPath.

```py
driver = webdriver.Chrome()
driver.find_element(By.XPATH, "//input[@value='f']")
```

#### Utilizando Localizadores

O FindElement facilita o uso de localizadores! Para a maioria dos idiomas, tudo que você precisa fazer é utilizar webdriver.common.by.By, porém em outros é tão simples quanto definir um parâmetro na função FindElement


##### By

```py
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.find_element(By.CLASS_NAME, "information")
```

##### ByChained



##### ByAll



## Primeiro script com o Selenium

Oito passos básicos

Tudo que o Selenium faz é enviar comandos ao navegador de internet para fazer algo ou solicitar informações dele. A maior parte do que você irá fazer com o Selenium é uma combinação desses comandos básicos.


### 1. Iniciando uma sessão


```py title='Terminal'
driver = webdriver.Chrome()
```

### 2. Agindo no navegador de internet
Nesse exemplo estamos navegando para uma página web.

```py title='Terminal'
driver.get('https://www.selenium.dev/selenium/web/web-form.html')
```

### 3. Solicitando informação do navegador de internet

Existem diversos tipos de informação sobre o navegador de internet que você pode solicitar, incluindo window handles, tamanho / posição do navegador, cookies, alertas e etc.

```py titulo='Terminal'
titulo = driver.title
```

### 4. Estabelecendo uma Estratégia de Espera

Sincronizar o código ao estado atual do navegador é um dos maiores desafios quando se trabalha com o Selenium, fazer isso de maneira bem feita é um tópico avançado.

Essencialmente, você quer ter certeza absoluta de que o elemento está na página antes de tentar localizá-lo e o elemento está em um estado interativo antes de você tentar interagir com ele.

Uma espera implícita raramente é a melhor solução, mas é a mais fácil de demonstrar aqui, então vamos usá-la como um substituto.

```py title='Terminal'
driver.implicitly_wait(0.5)
```

### 5. Encontrando um elemento
A maioria dos comandos na maior parte das sessões do Selenium são relacionados a elementos e você não pode interagir com um sem o primeiro encontrando um elemento.

```py title='Terminal'
box_texto = driver.find_element(by=By.NAME, value="my-text")
botao_enviar = driver.find_element(by=By.CSS_SELECTOR, value="button")
```

### 6. Agindo no elemento

Há apenas um punhado de ações a serem executadas em um elemento, mas você irá usá-las com frequência.

```py title='Terminal'
box_texto.send_keys('Selenium')
botao_enviar.click()
```

### 7. Solicitando informações do elemento

Elementos podem guardar muitas informações que podem ser solicitadas.

```py title='Terminal'
texto = message.text
```

### 8. Encerrando a sessão

Isso encerra o processo do driver, que por padrão também fecha o navegador. Nenhum outro comando pode ser enviado para esta instância do driver.

```py title='Terminal'
driver.quit()
```

### Executando um script Selenium

```py title='Terminal'
python primeiro_script.py
```

## Usos comuns

A maioria das pessoas usa o Selenium para executar testes automatizados para aplicações web, mas o Selenium suporta qualquer caso de uso de automação de navegador.

### Tarefas Repetitivas

Talvez seja necessário fazer login em um site e baixar algo ou enviar um formulário. Você pode criar um script Selenium para ser executado com um serviço em horários pré-definidos.

### Web Scrapping

Está a tentar recolher dados de um site que não tem uma API? O Selenium permitirá que você faça isso, mas certifique-se de estar familiarizado com os termos de serviço do site termos de serviço do site, pois alguns sites não permitem isso e outros até bloqueiam o Selenium.

### Testes

Executar o Selenium para testes requer fazer asserções sobre as ações tomadas pelo Selenium. Então uma boa biblioteca de asserções é necessária. Características adicionais para prover estrutura para testes requerem o uso de [Test Runner] (#test-runners).


Todo material relacionado a esta aula, foi retirado da [documentação oficial do Selenium](https://www.selenium.dev/pt-br/documentation/), versão 4.0
