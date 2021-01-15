massas = []
for i in range(1, 6):
    massa = float(input(' DIGITE A MASSA DA {}ª PESSOA: '.format(i)))
    massas.append(massa)

massas.sort()

print(' O indivíduo de maior massa tem {} Kg.'.format(massas[-1]))