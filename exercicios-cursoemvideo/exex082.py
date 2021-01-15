lista = list()
val = True
while val == True:
    num = int(input('Digite um valor: '))
    while True:
        cond = input('Deseja continuar? [S/N] ').upper()
        if cond == 'S':
            break
        elif cond == 'N':
            val = False
            break
        else:
            print('Inválido. ')
    lista.append(num)

pares = list()
impares = list()

for num in lista:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print(f'Foram digitados: {lista}')
print(f'Pares: {pares}')
print(f'Ímpares: {impares}')