número = int(input(' Digite um número de 0 a 9999. '))
num = str(número)
if número >= 1000:
    print(' O número {} possui {} unidade(s), '.format(num, num[3]), end='')
    print('{} dezena(s), {} centena(s) e {} milhar(es). '.format(num[2], num[1], num[0]))

elif número >= 100 <= 999:
    print(' O número {} possui {} unidade(s), '.format(num, num[2]), end='')
    print('{} dezena(s) e {} centena(s).'.format(num[1], num[0]))

elif número >= 10 <=99:
    print(' O número {} possui {} unidade(s) e {} dezena(s). '.format(num, num[2], num[1]))

elif número >= 0 <= 9:
    print(' O número {} possui {} unidade(s). '.format(num, num[0]))