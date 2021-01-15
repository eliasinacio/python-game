valor = int(input('DIGITE O VALOR: '))
resto = 0
print('A QUANTIA SERÁ ENTREGUE DA SEGUINTE FORMA: ')

while valor != 0:
    inteiro = valor // 50
    resto = valor % 50
    if inteiro != 0:
        print(f'{inteiro} notas de R$50 reais.')

    while resto < 50:
        inteiro = resto // 20
        resto = resto % 20
        if inteiro != 0:
            print(f'{inteiro} notas de R$20 reais.')

        while resto < 20:
            inteiro = resto // 10
            resto = resto % 10
            if inteiro != 0:
                print(f'{inteiro} notas de R$10 reais.')

            while resto < 10:
                inteiro = resto // 5
                resto = resto % 5
                if inteiro != 0:
                    print(f'{inteiro} notas de R$5 reais.')

                while resto < 5:
                    inteiro = resto // 2
                    resto = resto % 2
                    if inteiro != 0:
                        print(f'{inteiro} notas de R$2 reais.')

                    while resto < 2 and resto != 0:
                        print('1 moeda de R$1 real.')

                        break
                    break
                break
            break
        break
    break