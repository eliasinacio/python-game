salário = float(input(' Digite o valor do seu salário: '))
valor = float(input(' Qual o valor da casa desejada: '))
anos = int(input(' Em quantos anos você deseja pagar? '))

prestação = valor / (anos * 12)
ps = (30/100) * salário

if prestação <= ps:
    print(' Seu empréstimo foi aprovado! ')
    print(' As prestações serão de R${:.2f}, seu salário cobre tal valor. '.format(prestação))
    print(' 30% do seu salário equivale a: R${:.2f} '.format(ps))

else:
    print(' Seu empréstimo foi negado. ')
    print(' 30% do seu salário equivale a R${:.2f} '.format(ps))
    print(' Seu salário não cobre as prestações do empréstimo, que seriam de R${:.2f} '.format(prestação))
