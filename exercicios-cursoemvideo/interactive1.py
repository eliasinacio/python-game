dic = {'nomes': [], 'idades': [], 'sexo': [], 'CPFs': [], 'emails': []}

print('\033[1;36m')
print('-=-'*59)
print('-=-'*26, "CADASTRO DE PESSOAS".ljust(19), '-=-'*26)

while True:
    print('-=-' * 59)
    nome = input('\n Digite seu nome completo: \n ').upper()
    idade = int(input('\n Digite sua idade: \n '))
    sexo = str(input('\n Qual o seu sexo? [M/F]\n ')).upper()
    email = input('\n Digite seu email: \n ')
    cpf = input('\n Digite seu email: ')

    if sexo in 'MF':
        dic['sexo'].append(sexo)
        dic['nomes'].append(nome)
        dic['idades'].append(idade)

    else:
        print('Erro! Cadastro inválido. ')
        pass

    print(dic)
