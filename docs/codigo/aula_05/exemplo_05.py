import math

pi = math.pi

print('Esse é o número pi: ', pi, 'ele possui algumas casas decimais')

print(f'Esse é o número pi: {pi}')

print(f'Esse é número pi: {pi:.2f} com duas casas decimais.')


cadastro = {'Jõao': 2312, 'Madalena': 4351, 'Alisson': 345}

print(cadastro.items())

for nome, id in cadastro.items():
    print(f'{nome:10} ==> {id:4}')
