lista = list()

for num in range(0, 5):
    valor = int(input('Digite um valor: '))
    lista.append(valor)

print(lista)

print(f'O maior valor digitado foi {max(lista)}, na(s) posição(ões): ',end='')
for pos, num in enumerate(lista):
    if num == max(lista):
        print(pos,end='...')

print(f'\nO menor valor digitado foi {min(lista)}, na(s) posição(ões): ',end='')
for pos, num in enumerate(lista):
    if num == min(lista):
        print(pos,end='...')
