print('\033[1;31mCALCULADOR DE FATORIAL\033[0m'.center(40))
n = int(input('DIGITE UM NÚMERO: '))
m = p = n
print('{}! = '.format(n),end='')

while n != 0:
    m -= 1
    if n != 0:
        n = n * m
        print('{} x '.format(p),end='')
        p -= 1
    if m == 1:
        print(p,end=' = ')
        break
print(n)