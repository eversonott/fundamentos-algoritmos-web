def ordenacao_insercao(lista_recebida):
    lista = lista_recebida
    for i in range(0, len(lista)):
        indice_anterior = i - 1
        while indice_anterior >= 0 and lista[indice_anterior] > lista[indice_anterior + 1]:
            lista[indice_anterior + 1], lista[indice_anterior] = lista[indice_anterior], lista[indice_anterior + 1]
            indice_anterior -= 1
    return lista


def intercalar_listas_ordenadas(esquerda, direita):
    indice_esq = 0
    indice_dir = 0
    resultado = []

    while indice_esq < len(esquerda) and indice_dir < len(direita):
        if esquerda[indice_esq] <= direita[indice_dir]:
            resultado.append(esquerda[indice_esq])
            indice_esq += 1
        else:
            resultado.append(direita[indice_dir])
            indice_dir += 1

    while indice_esq < len(esquerda):
        resultado.append(esquerda[indice_esq])
        indice_esq += 1

    while indice_dir < len(direita):
        resultado.append(direita[indice_dir])
        indice_dir += 1
    return resultado


def ordenacao_intercalacao(lista):
    tamanho = len(lista)

    indice_meio = tamanho // 2

    if tamanho <= 1:
        return lista
    else:
        metade_esquerda = ordenacao_intercalacao(lista[:indice_meio])
        metade_direita = ordenacao_intercalacao(lista[indice_meio:])
        return intercalar_listas_ordenadas(metade_esquerda, metade_direita)
