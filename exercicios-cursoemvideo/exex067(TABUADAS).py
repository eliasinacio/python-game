print('\033[34m-=-'*10)
print('SIMULADOR DE TABUADAS'.center(30))
while True:
    print('\033[34m-=-'*10)
    num = int(input('DIGITE UM VALOR: '))
    if num < 0:
        break

    for i in range(1, 11):
        print(f'{i:>2} x {num:>2} = {i*num:>2}')

print('ENCERRANDO...')