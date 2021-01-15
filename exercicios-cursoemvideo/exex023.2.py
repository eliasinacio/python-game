num = int(input(' Digite um número de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(' UNIDADE: {} '.format(u))
print(' DEZENA: {} '.format(d))
print(' CENTENA: {} '.format(c))
print(' MILHAR: {}'.format(m))
#O resto 10 vai isolar o número
#a divisão inteira vai apagar o útimo número antes do que vai ser utilizado