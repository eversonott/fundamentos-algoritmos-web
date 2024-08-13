def ordenacao_flutuacao_demonstrativo(arranjo):
    contador = 0
    for i in range(len(arranjo)):
        print("\ni: ", i)
        for j in range(len(arranjo) - i - 1):
            print("j: ", j, end="")
            if arranjo[j] > arranjo[j + 1]:
                arranjo[j], arranjo[j + 1] = arranjo[j + 1], arranjo[j]
                contador += 1
            print(" -> ", arranjo)
        contador += 1

    arranjo2 = [55, 23, 12, 2]
    ordenacao_flutuacao(arranjo2)
    print(arranjo2)

    print(contador)


def ordenacao_flutuacao(arranjo):
    for i in range(len(arranjo)):
        for j in range(len(arranjo) - i - 1):
            if arranjo[j] > arranjo[j + 1]:
                arranjo[j], arranjo[j + 1] = arranjo[j + 1], arranjo[j]



