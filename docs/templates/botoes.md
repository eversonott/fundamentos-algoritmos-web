
{% if link == "" %}[Aula :fontawesome-brands-youtube:](){.md-button}{% else %}[Aula :fontawesome-brands-youtube:](https://youtu.be/{{link}}?list=PLocgY_9IQz_r-qwv6pwiO2EGniGAIt49q){:target="_blank", .md-button}{% endif %}
{% if slides is true %}[Slides :fontawesome-solid-file-powerpoint:](..Módulo 2/Slides/aula_{{aula}}.pdf){:target="_blank", .md-button}{% else %}[Slides :fontawesome-solid-file-powerpoint:](){.md-button}{% endif %}
{% if codigos is true %}[Códigos :fontawesome-solid-code:](../Módulo 2/Códigos/aula_{{aula}}.md){.md-button }{% else %}[Códigos :fontawesome-solid-code:](){.md-button}{% endif %}
{% if pesquisas is true %}[Pesquisas :material-message-question:](../Módulo 2/Pesquisas/aula_{{aula}}.md){.md-button}{% else %}[Pesquisas :material-message-question:](){.md-button}{% endif %}
