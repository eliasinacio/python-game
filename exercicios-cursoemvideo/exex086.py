matriz = [
    [],
    [],
    []
]

for n in range(0,3):
    matriz[0].append(int(input('Digite um valor [linha 1]\n>> ')))
for n in range(0,3):
    matriz[1].append(int(input('Digite um valor [linha 2]\n>> ')))
for n in range(0, 3):
    matriz[2].append(int(input('Digite um valor [linha 3]\n>> ')))

print('-=-'*9)
print(matriz[0])
print(matriz[1])
print(matriz[2])