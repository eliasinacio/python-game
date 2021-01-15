from exex086 import matriz

pares = terceiraColuna = 0

for i in matriz:
    for t in i:
        if t % 2 == 0:
            pares += t

    terceiraColuna += i[2]

matriz[1].sort()
segundaLinha = matriz[1][-1]
print('-=-'*9)
print(f'A soma dos valores pares da matriz equivale a: {pares}')
print(f'A soma dos valores da terceira coluna equivale a: {terceiraColuna}')
print(f'O maior valor da segunda linha é: {segundaLinha}')
