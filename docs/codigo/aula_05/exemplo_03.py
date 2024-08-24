print('Somos os {} que dizem "{}"!'.format('cavaleiros', 'Ni'))

print('{0} e {1}'.format('spam', 'bacon'))
print('{1} e {0}'.format('spam', 'bacon'))


print('Eu não gosto de {prato}'.format(prato = 'spam'))

print('John: {0}; Eric: {2}; Terry: {1}.'.format(84, 77, 81))


tabela = {'John': 84, 'Eric': 81, 'Terry': 77}
print('John: {0[John]}; Eric: {0[Eric]}; Terry: {0[Terry]}.'.format(tabela))
print('John: {0[John]}; Eric: {0[Eric]}; Terry: {0[Terry]}.'.format(tabela))


numeros = [1, 2, 3, 5, 6]
def adicao(*lista):
    return sum(lista)
print(adicao(*numeros))

dados = {'fruta': 'morango', 'vegetal': 'batata', 'bacon':'span'}

def definicao(**dados):
    for item in dados:
        print(dados[item])

definicao(**dados)


print('John: {John}; Eric: {Eric}; Terry: {Terry}.'.format(**tabela))
