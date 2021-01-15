nome = str(input('Digite o nome do aluno: ')).capitalize()
media = float(input('Digite a média do aluno: '))

boletim = {'aluno': nome, 'media': media}


if media >= 7:
    boletim['situação'] = 'Aprovado'
else:
    boletim['situação'] = 'Reprovado'

print(f'O aluno {boletim["aluno"]} tem média {boletim["media"]} e foi {boletim["situação"]}')