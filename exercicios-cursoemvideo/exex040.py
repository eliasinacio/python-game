N1 = float(input(' DIGITE SUA PRIMEIRA NOTA: '))
N2 = float(input(' DIGITE SUA SEGUNDA NOTA: '))

MÉDIA = (N1 + N2) / 2

if MÉDIA <= 5:
    print('\033[1;31;40m SINTO MUITO, SUA MÉDIA É {}. VOCÊ FOI REPROVADO. \033[0m'.format(MÉDIA))

elif MÉDIA >= 7:
    print(' \033[1;34;40m PARABÉNS! SUA MÉDIA É {}. VOCÊ FOI APROVADO. \033[0m'.format(MÉDIA))

elif MÉDIA > 5 and MÉDIA < 7:
    print('\033[0;33m SUA MÉDIA É {}, MAS VOCÊ TEM A CHANCE DE IR PARA A RECUPERAÇÃO. \033[0m'.format(MÉDIA))
