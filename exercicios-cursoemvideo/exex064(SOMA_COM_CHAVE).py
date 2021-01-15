k = soma = 0
while True:
    t = int(input('DIGITE UM NÚMERO: [999 PARA] '))
    if t == 999:
        print('SOMA DOS {} NÚMEROS DIGITADOS: {}'.format(k, soma))
        break
    else:
        soma += t
        k += 1
        print('Hmm')