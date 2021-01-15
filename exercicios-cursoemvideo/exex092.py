from datetime import date
nome = str(input('Digite seu nome: ')).capitalize()
anoNascimento = int(input('Digite seu ano de nascimento: '))
carteiraDeTrabalho = int(input('Digite sua CTPS: [0, caso não tenha] '))
idade = (date.today().year - anoNascimento)

dict = {'nome': nome, 'idade': idade}

if carteiraDeTrabalho != 0:
    dict['ctps'] = carteiraDeTrabalho

    if idade >= 16:
        anoContratacao = int(input('Informe o ano de contratação: '))
        salario = float(input('Informe o valor do salário: R$ '))
        aposentadoria = ((anoContratacao + 35) - date.today().year) + idade
        dict['contratação'] = anoContratacao
        dict['salário'] = salario
        dict['aposentadoria'] = aposentadoria

print(dict)
for key, value in dict.items():
    print(f'{key} tem  {value}')