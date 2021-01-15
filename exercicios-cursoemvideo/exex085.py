numeros = [[],[]]
for i in range(0,7):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)

numeros[0].sort()
numeros[1].sort()
print(f'Os valores pares são: {numeros[0]}')
print(f'Os valores ímpares são: {numeros[1]}')