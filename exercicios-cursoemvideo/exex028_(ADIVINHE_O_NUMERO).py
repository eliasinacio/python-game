from random import randint
from time import sleep
n1 = randint(1, 5)
print('\033[1;34m-==-' * 16)
print('\033[1;35m TENTE ADIVINHAR O NÚMERO QUE ESTOU PENSANDO. DE 0 A 5. ')
print('\033[1;34m-==-' * 16)
n2 = int(input(' CHUTE: '))
print(' VAMOS VER...')
sleep(2)
if n1 == n2:
    print(' PARABÉNS! VOCÊ ACERTOU.')
else:
    print(' Sinto muito, você errou. O número era: {}'.format(n1))