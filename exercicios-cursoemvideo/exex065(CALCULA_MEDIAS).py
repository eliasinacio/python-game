t = int(input('DIGITE UM VALOR: '))
contagem = 1
soma = t
lista = [t]
while True:
    add = input('DESEJA ADICIONAR MAIS UM VALOR? [S/N]  ').upper()
    if add == 'S':
        t = int(input('DIGITE O NÚMERO: '))
        soma += t
        contagem += 1
        lista.append(t)

    if add == 'N':
        print('O MAIOR VALOR DIGITADO FOI \033[36m{}\033[0m'.format(max(lista)))
        print('E O MENOR FOI \033[36m{}\033[0m'.format(min(lista)))
        media = soma / contagem
        print('A MÉDIA DOS {} VALORES INSERIDOS É {}:'.format(contagem, media))
        print('{}/{} = {}'.format(soma, contagem, media))
        break

    if add.isalpha() == False:
        print('INVÁLIDO')
        continue