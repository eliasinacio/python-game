cadastros = []
cadastroLocal = []
print('-=-'*12)
print('CADASTRO DE NOTAS'.center(36))

while True:
    print('-=-'*12)
    nome = str(input('Aluno: ')).capitalize()
    nota_1 = float(input('Nota 1: '))
    nota_2 = float(input('Nota 2: '))
    cadastroLocal.append(nome)
    cadastroLocal.append(nota_1)
    cadastroLocal.append(nota_2)
    cadastros.append(cadastroLocal[:])
    cadastroLocal.clear()

    conf = str(input('Mais algum aluno? [S/N] ')).upper()
    if conf == 'N':
        break

print('-=-'*12)
print(f'    ALUNO                    MÉDIA')
for pos, aluno in enumerate(cadastros):
    print(f'{pos+1}   {aluno[0]:-<25}', f'{(aluno[1]+aluno[2])/2:.1f}')

while True:
    print('-=-'*12)
    individual = str(input('Deseja ver as notas individuais de algum aluno? [S/N] ')).upper()
    if individual == 'N':
        break
    elif individual == 'S':
        aluno = int(input('Digite o número referente ao aluno: '))

    print(f'Notas de {cadastros[aluno-1][0]}: {cadastros[aluno-1][1]} e {cadastros[aluno-1][2]}')

print('ENCERRANDO... VOLTE SEMPRE!')