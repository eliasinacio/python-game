import random

lista = []
for num in range(0,5):
    lista.append(random.randint(0, 10))

tuple(lista)

print(lista)
print(f'O maior número é {max(lista)} e o menor é {min(lista)}')