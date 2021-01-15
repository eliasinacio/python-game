dias = int(input(' Por quantos dias o carro foi alugado? \n> '))
km = float(input(' Quantos km foram rodados? \n> '))
y = (km*0.15) + (dias*60)
print(' TOTAL A PAGAR: R$ {:.2f}'.format(y))