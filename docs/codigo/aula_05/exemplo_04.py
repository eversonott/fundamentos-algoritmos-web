with open('nomes.txt', encoding='utf-8') as arq:
    nomes = arq.read()

print(nomes)

with open('nomes.txt', encoding='utf-8') as arq:
    nomes = arq.readline()

print(nomes)

with open('nomes.txt', encoding='utf-8') as arq:
    nomes = arq.readlines()

print(nomes)

with open('nomes.txt', encoding='utf-8') as arq:
    for linha in arq:
        print(linha, end='')


