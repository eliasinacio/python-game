s = c = 0
while True:
    v = int(input('DIGITE UM VALOR. [999 PARA PARAR] \n>>> '))
    if v == 999:
        break
    c += 1
    s += v
print(f'A SOMA DOS {c} VALORES DIGITADOS É {s}.')