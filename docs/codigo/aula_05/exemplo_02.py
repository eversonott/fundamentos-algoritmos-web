aulas = 12
inicio = 9
fim = 11
curso = 'Fundamentos de algoritmos'
print(f'Oferta: {curso=} {aulas=} {inicio=}h e {fim=}h.')


from math import radians as radianos
from math import sin as seno
theta = 30
print(f'{theta=} {seno(radianos(theta))=:.3f}')

from random import randrange
for i in range(10):
    theta = randrange(0,366)
    print(f'{theta=} {seno(radianos(theta))=:.3f}')

