cadastrados = []
cadastroLocal = {'nome': [], 'sexo': [], 'idade': []}

while True:
    print('Digite 999 para encerrar. ')
    nome = str(input('Nome: ')).capitalize()
    if nome == '999':
        break
    sexo = str(input('Sexo: [M/F] ')).upper()
    if sexo not in 'MF':
        print('Erro')
        continue
    idade = int(input('Idade: '))
    cadastroLocal['nome'].append(nome)
    cadastroLocal['sexo'].append(sexo)
    cadastroLocal['idade'].append(idade)

    cadastrados.append(cadastroLocal.copy())

    cadastroLocal['nome'] = []
    cadastroLocal['sexo'] = []
    cadastroLocal['idade'] = []
    print('-=-'*12)

# A) QUANTAS PESSOAS CADASTRADAS:
numeroDeCadastros = len(cadastrados)

somaIdades = 0
mulheres = []
for cadastro in cadastrados:
    # B) MÉDIA DAS IDADES:
    somaIdades += cadastro['idade'][0]

    # C) UMA LISTA COM TODAS AS MULHERES:
    if cadastro['sexo'][0] == 'F':
        mulheres.append(cadastro['nome'][0])

# D) IDADES ACIMA DA MÉDIA
acimaDaMedia = []
for cadastro in cadastrados:
    if cadastro['idade'][0] > (somaIdades/numeroDeCadastros):
        acimaDaMedia.append(cadastro['nome'][0])

# OUTPUT
print('-=-'*12)
print(f'Foram cadastradas {numeroDeCadastros} pessoas. ')
print(f'A média de idades é: {somaIdades/numeroDeCadastros:.1f}.')

if len(mulheres) != 0:
    print(f'Mulheres cadastradas: ')
    for mulher in mulheres:
        print(f'-{mulher}')

print(f'Pessoas com idades acima da média ({somaIdades/numeroDeCadastros:.1f}):')
if len(acimaDaMedia) == 0:
    print('0')
else:
    for pessoa in acimaDaMedia:
        print(f'-{pessoa}')
