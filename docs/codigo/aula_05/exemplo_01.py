import math

print(f'O valor aproximado de pi é: {math.pi:.2f}')

print(f'O valor ainda mais aproximado de pi é: {math.pi:.2f}')

cadastro = {'Jõao': 2312, 'Madalena': 4351, 'Alisson': 345}
for nome, id in cadastro.items():
    print(f'{nome} ==> {id}')

for nome, id in cadastro.items():
    print(f'{nome:10} ==> {id:3}')
