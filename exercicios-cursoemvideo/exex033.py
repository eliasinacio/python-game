import math
n1 = int(input(' Digite um número: '))
n2 = int(input(' Digite outro número: '))
n3 = int(input(' Digite mais um número: '))
lista = [n1, n2, n3]
lista.sort()
print(' O maior número é {} e o menor é {}. '.format(lista[2], lista[0]))