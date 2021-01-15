import cores

cores.negrito()
cores.azul()
print('-=-'*13)
print('SUPERMERCADO ALLIAZ'.center(38))
print('CONTROLE DE PREÇOS'.center(37))
print('-=-'*13)
cores.branco()

lista_produtos = []
lista_preços = []
maiores_de_mil = total = 0

while True:
    try:
        nome = input('QUAL O NOME DO PRODUTO: ').upper()
        preço = float(input('INFORME O PREÇO: '))

        lista_produtos.append(nome)
        lista_preços.append(preço)
        cores.verde()
        print(f'{nome} CADASTRADO.')
        cores.branco()
        if preço > 1000:
            maiores_de_mil += 1

    except:
        cores.vermelho()
        print('ERRO. PRODUTO NÃO CADASTRADO.')
        cores.branco()

    while True:
        conf = input('\nDESEJA CADASTRAR MAIS ALGUM PRODUTO? [S/N]  ').upper()
        if conf == 'N':
            break

        elif conf == 'S':
            try:
                nome = input('DIGITE O NOME DO PRODUTO: ').upper()
                preço = float(input('VALOR: '))

                lista_produtos.append(nome)
                lista_preços.append(preço)
                cores.verde()
                print(f'{nome} CADASTRADO. ')
                cores.branco()
                if preço >= 1000:
                    maiores_de_mil += 1

            except:
                cores.vermelho()
                print('INVÁLIDO')
                cores.branco()

        else:
            cores.vermelho()
            print('INVÁLIDO')
            cores.branco()
    break

for i in lista_preços:
    i = float(i)
    total += i

menor_preço = min(lista_preços)
loc_men_preço = lista_preços.index(menor_preço)
produto_mais_barato = lista_produtos[loc_men_preço]
cores.azul()
print('\n','-=-'*13)
print('RESULTADO'.center(36))
print('-=-'*13)
cores.branco()
cores.negrito()

print(f'\nTOTAL: R${total:.2f}')
print(f'PRODUTO DE MENOR VALOR: {produto_mais_barato} DE R${menor_preço:.2f}')
if maiores_de_mil > 0:
    print(f'{maiores_de_mil} PRODUTOS CUSTAM MAIS QUE R$1.000,00')