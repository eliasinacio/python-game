n = int(input(' DIGITE UM NÚMERO: '))
lista = []

for i in range(2, n):
    if n % i == 0:
        lista.append(i)

if len(lista) == 0:
    print(' Esse número é primo.')

else:
    print(' Esse número não é primo.')
    print(' Ele é divisível por: {}'.format(lista))
