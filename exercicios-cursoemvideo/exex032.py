from datetime import date
'''Os anos bissextos são múltiplos de 4, não múltiplos de 100 (1900 não é bissexto) e múltiplos de 400 (2000 é bissexto)'''
ano = int(input(' Digite um ano: \n Digite 0 para usar o ano atual. '))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(' O ano {} é BISSEXTO. '.format(ano))

else:
    print(' O ano {} não é BISSEXTO. '.format(ano))