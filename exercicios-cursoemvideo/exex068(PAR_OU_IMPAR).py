from random import randint

print('\033[35m-=-'*17, '\n-=--=--=-', end='')
print('PAR OU ÍMPAR'.center(33), end='')
print('-=--=--=-\n'+'-=-'*17)
ganhos = 0
perdas = 0
print('\n\033[3;36mO computador escolhe um número aleatório de 0 a 10.\nTente vencê-lo no par ou ímpar.\033[0m')
while True:
    print('\033[35m')
    print('NOVA RODADA'.center(40))
    print('\033[35m')

    pc = randint(0,10)
    PI = input('DIGITE [P] PARA ESCOLHER PAR E [I] PARA ÍMPAR: ').upper()

    while PI not in 'IP':
        PI = input('INVÁLIDO. TENTE NOVAMENTE: [P/I] ').upper()
        PI = PI
    else:
        jogada = int(input('FAÇA SUA JOGADA: [0 A 10] \n>>> '))
        soma = jogada + pc

        if PI == 'I':
            if soma % 2 == 0:
                print('\n\033[31mSINTO MUITO. VOCÊ PERDEU.\033[35m')
                print(f'{jogada} + {pc} = {soma} >>> PAR')
                perdas += 1
            else:
                print('\n\033[36mPARABÉNS!! VOCÊ GANHOU.\033[35m')
                print(f'{jogada} + {pc} = {soma} >>> ÍMPAR')
                ganhos += 1

        else:
            if soma % 2 == 0:
                print('\n\033[36mPARABÉNS!! VOCÊ GANHOU.\033[35m')
                print(f'{jogada} + {pc} = {soma} >>> PAR')
                ganhos += 1
            else:
                print('\n\033[31mSINTO MUITO. VOCÊ PERDEU. \033[35m')
                print(f'{jogada} + {pc} = {soma} >>> ÍMPAR\n')
                perdas += 1
    print('-=-'*17)
    REP = input('DESEJA CONTINUAR? [S/N] ').upper()
    print('-=-' * 17)
    if REP == 'N':
        break

print('OBRIGADO! ATÉ A PRÓXIMA. ')
print(f'VOCÊ GANHOU {ganhos} RODADA(S) E PERDEU {perdas}.')