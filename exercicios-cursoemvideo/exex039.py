from datetime import *
ANO = date.today().year

ANONS = int(input(' DIGITE O ANO EM QUE VOCÊ NASCEU: '))

ALISTAMENTO = ANONS + 18

if ALISTAMENTO < ANO:
    print(' VOCÊ JÁ DEVIA TER SE ALISTADO NO SERVIÇO MILITAR HÁ {} ANOS. '.format(ANO - ALISTAMENTO))

elif ALISTAMENTO == ANO:
    print(' VOCÊ DEVE SE ALISTAR NO SERVIÇO MILITAR ESTE ANO. ')

elif ALISTAMENTO > (ANO - 1):
    print(' VOCÊ AINDA NÃO PRECISA SE ALISTAR NO SERVIÇO MILITAR AINDA. APENAS EM {}. '.format(ALISTAMENTO))