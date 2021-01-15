from random import choice
def sorteio(a):
    sorteados = []
    for i in range(0, 5):
        sorteados.append(choice(a))
    return sorteados

def pares(b):
    soma = 0
    for i in b:
        if i % 2 == 0:
            soma += i
    return soma
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

sorteio1 = sorteio(lista)
print(f'Os números Sorteados foram: {sorteio1}')
print(f'A soma dos números pares: {pares(sorteio1)}')
