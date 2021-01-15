km = float(input(' Qual a velocidade do veículo? '))
if km > 80:
    multa = (km - 80.0) * 7.0
    print(' Você excedeu o limite de velocidade. Irá pagar uma multa de R$ {:.0f},00'.format(multa))
else:
    print(' Sem problemas. Você não excedeu o limite de velocidade. ')