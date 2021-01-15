from time import sleep
from random import choice

print('\033[1;32m-=-' * 12)
print('VAMOS BRINCAR DE JOKEMPÔ!'.center(36))
print('-=-' * 12)

sleep(1)
jogador = int(input(' QUAL A SUA JOGADA? \n 1. PEDRA; \n 2. PAPEL; \n 3. TESOURA; \n > '))

lista = ['PEDRA', 'PAPEL', 'TESOURA']
pc = choice(lista)
sleep(0.7)
print(' Jo...', end=' ')
sleep(0.7)
print('Kem...', end=' ')
sleep(0.7)
print('Pô!!!')
sleep(0.7)

if jogador == 1:
    print('\n VOCÊ: PEDRA')
    print(' COMPUTADOR:',pc)
    sleep(0.5)
    print(' .', end='')
    sleep(0.5)
    print('.', end='')
    sleep(0.5)
    print('.')
    if pc == 'PEDRA':
        print(' HMM FOI UM EMPATE!')
    elif pc == 'PAPEL':
        print(' PAPEL EMBRULHA PEDRA. VOCÊ PERDEU!')
    elif pc == 'TESOURA':
        print(' PEDRA QUEBRA TESOURA. VOCÊ VENCEU!')

if jogador == 2:
    print('\n VOCÊ: PAPEL')
    print(' COMPUTADOR:',pc)
    sleep(0.5)
    print(' .', end='')
    sleep(0.5)
    print('.', end='')
    sleep(0.5)
    print('.')
    if pc == 'PEDRA':
        print(' PAPEL EMBRULHA PEDRA. VOCÊ VENCEU!')
    if pc == 'PAPEL':
        print(' TEMOS UM EMPATE! ')
    if pc == 'TESOURA':
        print(' TESOURA CORTA PAPEL. VOCÊ PERDEU!')

if jogador == 3:
    print('\n VOCÊ: TESOURA')
    print(' COMPUTADOR:',pc)
    sleep(0.5)
    print(' .', end='')
    sleep(0.5)
    print('.', end='')
    sleep(0.5)
    print('.')
    if pc == 'PEDRA':
        print(' PEDRA QUEBRA TESOURA. VOCÊ PERDEU!')
    elif pc == 'TESOURA':
        print(' EMPATAMOS!')
    if pc == 'PAPEL':
        print(' TESOURA CORTA PAPEL. VOCÊ VENCEU!')