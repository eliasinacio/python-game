print('\033[31m       -=SIMULADOR DE PROGRESSÕES ARITMÉTICAS=-\033[0m')
a1 = int(input('DIGITE O PRIMEIRO TERMO: '))
R = int(input('INDIQUE A RAZÃO: '))

S = 0
print('{} >> '.format(a1), end='')

while S != 10:
    a1 += R
    if S != 9:
        print('{} >> '.format(a1), end='')
    else:
        print('{}'.format(a1))
    S += 1
