lista = list()
while True:
    valor = int(input('Digite um valor: [0 para encerrar] \n>> '))
    if valor == 0:
        print('Encerrando...\n')
        break
    if valor not in lista:
        print('Valor adicionado. \n')
        lista.append(valor)
    else:
        print('Valor repetido. Não adicionado. \n')
        pass

lista.sort()

print(f'Os números digitados foram: ', end='')
for num in lista:
     print(num, end=' ')
