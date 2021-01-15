print('\033[34m CADASTRAMENTO DE PESSOAS \n\033[0m')

mulheres_menores_de_20 = maiores_de_18 = homens = 0

while True:
    idade = input('IDADE: ')
    sexo = input('SEXO: [M/F] ').upper()
    if idade.isnumeric() == False or sexo.isalpha() == False:
        print('INVÁLIDO! CADASTRO NÃO ACEITO. ')

    elif sexo not in 'MF':
        print('INVÁLIDO! CADASTRO NÃO FEITO.')

    else:
        #####
        if int(idade) >= 18:
            maiores_de_18 += 1
        if sexo == 'M':
            homens += 1
        if sexo == 'F':
            if int(idade) <= 20:
                mulheres_menores_de_20 += 1
    print('-=-'*12)

    while True:
        r = input('DESEJA CADASTRAR MAIS ALGUÉM? [S/N] ').upper()

        if r == 'N':
            break

        elif r == 'S':
            idade = input('IDADE: ')
            sexo = input('SEXO: [M/F] ').upper()

            if idade.isnumeric() == False or sexo.isalpha() == False:
                print('INVÁLIDO! CADASTRO NÃO ACEITO. ')

            elif sexo not in 'MF':
                print('INVÁLIDO! CADASTRO NÃO FEITO.')

            else:
                if int(idade) >= 18:
                    maiores_de_18 += 1
                if sexo == 'M':
                    homens += 1
                if sexo == 'F':
                    if int(idade) <= 20:
                        mulheres_menores_de_20 += 1
            print('-=-' * 12)

        else:
            print('INVÁLIDO!')
            print('-=-' * 12)
    break

print('\n'+'-=-'*12, '\n')
print(f'FORAM CADASTRADOS: \nHOMENS: {homens} Cadastros \nMULHERES COM 20 ANOS OU MENOS: {mulheres_menores_de_20} Cadastros \nMAIORES DE 18 ANOS: {maiores_de_18} Cadastros')
