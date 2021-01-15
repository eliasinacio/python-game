from random import randint
from time import sleep

n1 = randint(0, 10)

print('\033[1;34m-==-' * 16)
print('\033[1;35m TENTE ADIVINHAR O NÚMERO QUE ESTOU PENSANDO. DE 0 A 10. ')
print('\033[1;34m-==-' * 16)

contagem = 1

while n1 <= 10:
    n2 = int(input(' CHUTE: '))
    print(' VAMOS VER...')
    sleep(1)
    if n1 != n2:
        if n1 > n2:
            print('QUASE! MAIOR.',end=' ')
        if n1 < n2:
            print('QUASE! MENOR.',end=' ')
        contagem += 1
        print('TENTE NOVAMENTE. ')
        continue
    elif n1 == n2:
        print('VOCÊ ACERTOU!!! ')
        break

print('VOCÊ TENTOU {} VEZES ATÉ ACERTAR. '.format(contagem))
