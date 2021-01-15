cidade = input(' Digite o nome da cidade. ')
p1 = cidade.lower().split()
if p1[0] == 'santo':
    print(' O nome da cidade inicia com Santo.')

elif p1[0] != 'santo':
    print(' O nome da cidade não inicia com Santo.', end='')
    if 'santo' in cidade.lower():
        print(' Mas possui em seu interior.')