tupla = ('Carro', 32000, 'Casa', 300000, 'Internet', 300, 'Spotify', 40, 'PC', 3000)
print('#=#'*14)
print('LISTAGEM DE PREÇOS'.center(40))
print('#=#'*14)
for t in range(0,9,2):
    print(f'{tupla[t]:-<29} R$ {tupla[t+1]:>9.2f}')
print('#=#'*14)