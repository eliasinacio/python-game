sal = float(input(' Digite o valor do seu salário: '))
if sal > 1250:
    ns = (110/100) * sal
    print(' Você recebeu um aumento de 10%, seu novo salário é de R$ {} '.format(ns))

else:
    ns1 = (115/100) * sal
    print(' Você recebeu um aumento de 15%, seu novo salário é de R$ {} '.format(ns1))