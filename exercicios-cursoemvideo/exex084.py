lista_dados = list()
abaixo_da_media = list()
acima_da_media = list()
cont = 0
print('CADASTRAMENTO DE PESO')
while True:
    print('-=-' * 10)
    dadoNome = str(input('Digite seu nome: '))
    dadoPeso = float(input('Digite seu peso: '))
    lista_dados.append([dadoNome, dadoPeso])
    if dadoPeso >= 100:
        acima_da_media.append(dadoNome)
    elif dadoPeso <= 70:
        abaixo_da_media.append(dadoNome)

    cont += 1
    conf = str(input('Deseja cadastrar mais alguém? [S/N] ')).upper()
    if conf == 'S':
        continue
    elif conf == 'N':
        break
    else:
        print('\n ERRO!')
        break

print('\n'+'-=-'*10)
print(f'Foram cadastradas {cont} pessoas. ')
print('As pessoas leves cadastradas (com peso menor de 70 Kg) são: ',end='')
for pessoa in abaixo_da_media:
    print(pessoa.capitalize(),end=', ')
print('\nAs pessoas pesadas (com peso maior de 100 Kg) são: ',end='')
for pessoa in acima_da_media:
    print(pessoa.capitalize(),end=', ')