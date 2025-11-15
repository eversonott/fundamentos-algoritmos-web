import math

numero = 345

print(f'O meu número é {numero}')
print(f'O meu número é {numero:1}')
print(f'O meu número é {numero:2}')
print(f'O meu número é {numero:3}')
print(f'O meu número é {numero:4}')
print(f'O meu número é {numero:5}')
print(f'O meu número é {numero:6}')

clientes = [{'nome': 'A', 'valor' : 345}, {'nome': 'B', 'valor': 4356}, {'nome': 'C', 'valor': 2}]

print('|Nome|Valor depositado|')
for cliente in clientes:
    nome_cliente = cliente['nome']
    valor_depositado = cliente['valor']
    print(f'|{nome_cliente}|', end='')
    print(f'{valor_depositado}|')

print('|Nome|Valor depositado|')
for cliente in clientes:
    nome_cliente = cliente['nome']
    valor_depositado = cliente['valor']
    print(f'|{nome_cliente:4}|', end='')
    print(f'{valor_depositado:16}|')

print(f'O valor aproximado de pi é: {math.pi:.4f}')

print(f'O valor ainda mais aproximado de pi é: {math.pi:.2f}')

