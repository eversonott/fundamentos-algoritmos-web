---
Objetivos dessa aula:
{% for item in objetivos %}
- {{item}}
{% endfor %}

??? tip "Caso prefira ver a aula em vídeo"
    {% if link == ""%}
	Esse aula ainda não está disponível em formato de vídeo, somente em texto ou live!
    {% else %}
    ![type:video](https://www.youtube.com/embed/{{link}})
    {% endif %}

{% include "templates/botoes.md" %}
