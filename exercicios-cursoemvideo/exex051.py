a1 = int(input(' INDIQUE O PRIMEIRO TERMO: '))
r = int(input(' INDIQUE A RAZÃO: '))
s = a1
print('{},'.format(s), end=' ')
for n in range(0,10):
    s += r
    if n != 9:
        print('{},'.format(s), end=' ')
    else:
        print(s)