
# Leitura do arquivo
with open('f-strings.txt', encoding='utf-8') as arq:
    for linha in arq:
        print(linha, end="")

# Escrita no arquivo
texto = 'Podemos utilizar o especificador \':\' com f-strings.\n'
with open('f-strings.txt', 'a', encoding='utf-8') as arq:
    arq.write(texto)




