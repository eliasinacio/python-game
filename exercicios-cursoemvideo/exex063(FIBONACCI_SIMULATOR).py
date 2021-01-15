print('\033[31m   -=SIMULADOR FIBONACCI=- ')
valor = int(input('\033[0mINDIQUE QUANTOS TERMOS DEVEM SER MOSTRADOS: '))

contador = 1
a = p = 1

print('\033[34m{} >>'.format(p), end=' ')#34éazul
lista = [p]

while contador < valor:
    #MOSTRA O ÚLTIMO ELEMENTO DA LISTA, INICIANDO POR p.
    if contador < valor:
        if contador == (valor - 1):
            print(lista[-1])
        else:
            print(lista[-1], end=' >> ')

    #QUANDO SÓ TIVER p NA LISTA, ADICIONA ELE MESMO.
    if len(lista) == 1:
        lista.append(lista[-1])

    #QUANDO TIVEREM MAIS ELEMENTOS NA LISTA, SOMA-SE OS DOIS ÚLTIMOS E PÕE A SOMA NA LISTA.
    if len(lista) >= 2:
        a = lista[-1] + lista[-2]
        lista.append(a)

    contador += 1
