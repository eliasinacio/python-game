n1 = int(input( '\033[1;34;40m DIGITE UM NUMERO INTEIRO: '))
n2 = int(input(' DIGITE MAIS UM NÚMERO INTEIRO: '))

if n1 > n2:
    print(' O NÚMERO {} É MAIOR QUE O NÚMERO {}.\033[0m'.format(n1, n2))

elif n1 < n2:
    print(' O NÚMERO {} É MENOR QUE O NÚMERO {}.\033[0m'.format(n1, n2))

else:
    print(' OS NÚMEROS {} E {} SÃO IGUAIS. \033[0m'.format(n1, n2))
