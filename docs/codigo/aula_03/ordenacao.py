def ordenacao_insercao(lista):
    for indice_chave in range(1, len(lista)):
        chave = lista[indice_chave]
        indice_anterior = indice_chave - 1
        while indice_anterior >= 0 and lista[indice_anterior] > chave:
            indice_posterior = indice_anterior + 1
            lista[indice_posterior] = lista[indice_anterior]
            indice_anterior = indice_anterior - 1 
        lista[indice_anterior + 1] = chave 

def ordenacao_flutuacao(arranjo):
    for i in range(len(arranjo)):
        for j in range(len(arranjo) - i - 1):
            if arranjo[j] > arranjo[j + 1]:
                arranjo[j], arranjo[j + 1] = arranjo[j + 1], arranjo[j]


def soma(x,y):
    return x + y
