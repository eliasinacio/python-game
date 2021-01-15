peso = float(input(' DIGITE SEU PESO: (UTILIZANDO PONTO)  '))
altura = float(input(' DIGITE SUA ALTURA: (UTILIZANDO PONTO)  '))

IMC = peso / (altura * altura)

print('SEU IMC: {:.1f}'.format(IMC))
print(' SEU STATUS É DE', end='')

if IMC < 18.5:
    print(' ABAIXO DO PESO.')

elif IMC >= 18.5 and IMC < 25:
    print(' PESO NORMAL.')

elif IMC >= 25 and IMC < 30:
    print(' SOBREPESO.')

elif IMC >= 30 and IMC < 40:
    print(' OBESIDADE.')

elif IMC >= 40:
    print(' OBESIDADE MÓRBIDA. ')