import time

print('\033[31m -=SIMULADOR DE PROGRESSÕES ARITMÉTICAS=-')
time.sleep(1.5)

a1 = int(input('\033[0mDIGITE O PRIMEIRO TERMO: '))
razao = int(input('INFORME A RAZÃO: '))
quant_terms = int(input('INFORME QUANTOS TERMOS VOCÊ QUER: '))

count = 1

print('\033[34m{}; '.format(a1),end='')

while count != quant_terms:
    if count < quant_terms:
        a1 += razao
        print('\033[34m{}; '.format(a1),end='')
        if count == quant_terms:
            print('\033[34m{}; '.format(a1))

    count += 1

    if count == quant_terms:
        mais = input('\033[0m\nDESEJA CONTINUAR? [S/N]  ').upper()
        if mais == 'S':
            quantos_mais = int(input('INFORME QUANTOS TERMOS DESEJA VER: '))
            quant_terms += quantos_mais
        if mais == 'N':
            print('\nCERTO. OBRIGADO!\nENCERRANDO...')
            time.sleep(1)
            break
