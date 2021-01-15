from datetime import *
ano = int(input('\033[1;30m DIGITE EM QUAL ANO VOCÊ NASCEU: '))
idade = date.today().year - ano

print(' CATEGORIA: ', end='')

if idade <= 9:
    print('MIRÍM.')

elif idade > 9 and idade <= 14:
    print('INFANTIL.')

elif idade > 14 and idade <= 19:
    print('JÚNIOR.')

elif idade > 19 and idade <= 20:
    print('SÊNIOR.')

elif idade > 20:
    print('MASTER.')