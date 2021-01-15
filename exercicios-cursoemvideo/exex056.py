nomes = idades = sexos = nomesh = idadesh = nomesm = idadesm = []

for a in range(0, 1):
    nome = input(' Qual o seu nome? ')
    idade = int(input(' Qual sua idade? '))
    sexo = input(' Qual o seu sexo:[M/F] ')

    if sexo == 'M':
        nomesh.append(nome)
        idadesh.append(idade)

    # ACHAR AS MULHERES COM MENOS DE 20 ANOS
    elif sexo == 'F':
        if idade < 20:
            nomesm.append(nome)
            idadesm.append(idade)

    nomes.append(nome)
    idades.append(idade)
    sexos.append(sexo)

#ACHAR O HOMEM MAIS VELHO:
if len(idadesh) != 0:
    maior = max(idadesh)
    pos_maior_idade = idadesh.index(maior)
    homem_mais_velho = nomesh[pos_maior_idade]
    print('\n O homem mais velho é {} e tem {} anos. '.format(homem_mais_velho.capitalize(), max(idadesh)))

#MULHERES MENORES DE 20 ANOS:

print('\n Têm {} mulheres com menos de 20 anos. São elas: '.format(len(nomesm)))
for t in nomesm:
    print('', t.capitalize(), end='')
    print(', de {} anos. '.format(idadesm[nomesm.index(t)]))

#ACHAR A MÉDIA DAS IDADES:
b = 0

for c in range(0, len(idades)):
    b += idades[c]

print('\n A média das idades dos indivíduis é {}'.format(b/len(idades)))
