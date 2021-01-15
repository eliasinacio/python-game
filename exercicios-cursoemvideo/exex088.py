import time
from random import *
lista = []
indice = 0
print('$='*12+'$')
print('PALPITES MEGA SENA'.center(24))
print('$='*12+'$')
jogos = int(input('\nQuantos jogos serão feitos: '))

for jogo in range(0, jogos):
    lista.append(list())

    for n in range(0,6):
        lista[indice].append(randint(1,60))

    indice += 1

print('Seus palpites são: ')
for t in lista:
    t.sort()
    print(t)
    time.sleep(1)