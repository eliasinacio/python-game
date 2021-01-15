lista = list()
va = True
while va == True:
    valor = int(input('Digite um valor: '))

    while True:
        cond = input('Deseja continuar? [S/N]  ').upper()
        if cond in 'SN':
            if cond == 'S':
                break
            elif cond == 'N':
                va = False
                break
        else:
            print('Erro. Inválido.')
    lista.append(valor)

lista.sort(reverse=True)
print(f'\nForam digitados {len(lista)} números: \n{lista} ')
if 5 in lista:
    print(f'O número 5 foi digitado {lista.count(5)} vez(es). ')
else:
    print('O número 5 não foi digitado. ')