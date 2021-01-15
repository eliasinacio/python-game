frase = str(input(' DIGITE UMA FRASE: '))
frase = frase.lower().strip()

n = len(frase)

lista = []

for i in range(0, n):
    lista.append(frase[i])
    print(frase[i])
    if ' ' in lista:
        lista.pop()
        print(lista)

palavra = ''.join(lista)

print(palavra)

lista.reverse()
revjun = ''.join(lista)

print(revjun)

if palavra == revjun:
    print('É um palímdromo. ')

else:
    print('Não é um palímdromo. ')