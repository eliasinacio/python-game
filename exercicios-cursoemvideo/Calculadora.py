print("Olá! ")

operacao = int(input(
    "O que deseja  que eu faça? \n"
    "[1] Soma. \n" 
    "[2] Subtração. \n"
    "[3] Multiplicação. \n"
    "[4] Divisão. \n"
    "[5] Potenciação. \n"
    "[6] Radiciação. \n"
    "[7] Equação de 2º grau.\n>>> "
))

while True:
    while operacao == 1:
        x = float(input('Digite o primeiro número. '))
        y = float(input('Insira o valor a ser somado. '))
        m = input('Mais algum número? [Se não, digite 0] \n')

        while m == 'sim' or 'Sim':
            k = input(' Digite-o. ')
            if k == '':
                print(' A soma de dos valores inseridos equivale a {}' .format(x + y + k))
            elif k == int:
                print(' a soma dos valores inseridos equivale a {}'.format(x + y + k))
    if operacao == 2:
        x = float(input(' Insira um valor. '))
        y = float(input(' Insira o valor a ser subtraído. '))
        k = x - y
        print('{} menos {} equivale a {} ' .format(x, y, k))

    elif operacao == 3:
        x = float(input(' Digite um valor numérico. '))
        y = float(input(' Digite o valor por quem {} vai ser multiplicado. ' .format(x)))
        k = x * y
        print(' A multiplicação de {} por {} equivale a {}' .format(x, y, k))

    elif operacao == 4:
        x = float(input(' Insira um valor dividendo. '))
        y = float(input(' Digite o valor divisor. '))
        k = x / y
        print(' {} dividido para {} vale {} ' .format(x, y, k))

    elif operacao == 5:
        x = float(input(' Digite o valor da base. '))
        y = float(input(' Insira o valor do expoente. '))
        k = x ** y
        print('{} elevado a {} equivale a{}' .format(x, y, k))

    elif operacao == 6:
        x = float(input(' Insira um valor. '))
        y = float(input(' Insira o valor do índice da raíz. '))
        k = x ** (1 / y)
        print(' A raiz {}ª de {} vale {}' .format(y, x, k))

    rep = input(' Mais alguma coisa? [Digite o valor referente à operação ou 0 para encerrar] ')
    if rep == 0:
        break