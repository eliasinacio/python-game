
lista = []

valor1 = int(input('Digite um valor: '))
lista.append(valor1)

valor2 = int(input('Digite outro valor: '))
if valor2 < valor1 or valor2 == valor1:
    lista.insert(0, valor2)
else:
    lista.append(valor2)

valor3 = int(input('Digite mais um valor: '))
if valor3 < lista[0] or valor3 == lista[0]:
    lista.insert(0, valor3)
elif valor3 > lista[-1] or valor3 == lista[-1]:
    lista.append(valor3)
else:
    lista.insert(1, valor3)

valor4 = int(input('Digite mais um valor; '))
if valor4 < lista[0] or valor4 == lista[0]:
    lista.insert(0, valor4)
elif valor4 > lista[-1] or valor4 == lista[-1]:
    lista.append(valor4)
elif valor4 < lista[-1] and valor4 > lista[-2]:
    if valor4 == lista[-1] or valor4 == lista[-2]:
        lista.insert(2, valor4)
    else:
        lista.insert(2, valor4)
else:
    lista.insert(1, valor4)

valor5 = int(input('Digite outro valor: '))
if valor5 < lista[0]:
    lista.insert(0, valor5)
    print('add pela regra 1')
elif valor5 > lista[-1]:
    lista.append(valor5)
    print('add pela regra 2')
elif valor5 >= lista[0] and valor5 <= lista[1]:
    lista.insert(1, valor5)
elif valor5 >= lista[1] and valor5 <= lista[2]:
    lista.insert(2, valor5)
elif valor5 >= lista[2] and valor5 <= lista[3]:
    lista.insert(3, valor5)

print(lista) 