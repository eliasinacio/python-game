km = int(input(' Qual será a distância em km da viagem? '))
if km <= 200:
    preço = km * 0.50
    print(' O preço da sua passagem será R$ {} '.format(preço))
else:
    preço2 = km * 0.45
    print(' O preço da sua passagem será R$ {}'.format(preço2))