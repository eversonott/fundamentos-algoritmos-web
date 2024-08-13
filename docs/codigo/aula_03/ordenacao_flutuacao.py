def ordenacao_flutuacao_demonstrativo(arranjo):
    contador = 0
    contador2 = 0
    for i in range(len(arranjo) - 1):
        print("\ni: ", i)
        for j in range(len(arranjo) - i - 1):
            print("j: ", j, end="")
            if arranjo[j] > arranjo[j + 1]:
                arranjo[j], arranjo[j + 1] = arranjo[j + 1], arranjo[j]
                contador += 1
                contador2 += 1
                print(" -> trocou", arranjo[j+1], "por", arranjo[j], "e vice-versa.")
                print("->", arranjo)
        contador2 += 1


    print("\nLinha 2 e 3 foram executadas:", contador)
    print("Linha 4, 5 e 6 foram executadas:", contador2)


def ordenacao_flutuacao(arranjo):
    for i in range(len(arranjo)):
        for j in range(len(arranjo) - i - 1):
            if arranjo[j] > arranjo[j + 1]:
                arranjo[j], arranjo[j + 1] = arranjo[j + 1], arranjo[j]



