valor_1 = int(input('Digite um valor: '))
valor_2 = int(input('Digite mais um valor: '))
valor_3 = int(input('Digite outro valor: '))
valor_4 = int(input('Digite mais um valor: '))

numeros = (valor_1, valor_2, valor_3, valor_4)
print(f'Você digitou os números: {numeros}')
if 9 in numeros:
    print(f'O número 9 foi digitado {numeros.count(9)} vezes. ')

cont = 0
pares = []
for t in numeros:
    if t % 2 == 0:
        cont += 1
        pares.append(t)

print(f'Foram digitados {cont} números pares: {pares} ')

lista = []

for pos, i in enumerate(numeros):
    if i == 3:
        lista.append(pos)

if 3 in numeros:
    print('O número 3 foi digitado na(s) posição(ões): ',end=' ')
    for i in lista:
        while i != lista[-1]:
            print(i+1, end=' e ')
            break
        else:
            print(i+1)