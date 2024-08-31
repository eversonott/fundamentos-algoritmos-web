with open('saida.txt', 'x') as arq:
    print('Saída pelo print', file = arq)

print('Agosto', 31, 9.0)

print('Agosto', 31, 9.0, sep='-')

print('Agosto', 31, 9.0, sep=',')

print('Agosto', 31, 9.0, sep=',', end=' - Fim de mês')
