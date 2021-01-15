from random import randint
from time import sleep
jogadores = {
'jogador_1': randint(1,6),
'jogador_2': randint(1,6),
'jogador_3': randint(1,6),
'jogador_4': randint(1,6)
}
jogadoresEmOrdem = [0, 1, 2, 3]

d = 0
for key, value in jogadores.items():
    if value > d:
        d = value
        jogadoresEmOrdem[0] = [key, value]

k = 0
for key, value in jogadores.items():
    if key != jogadoresEmOrdem[0][0]:
        if value > k:
            k = value
            jogadoresEmOrdem[1] = [key, value]

l = 0
for key, value in jogadores.items():
    if key != jogadoresEmOrdem[0][0] and key != jogadoresEmOrdem[1][0]:
        if value > l:
            l = value
            jogadoresEmOrdem[2] = [key, value]

m = 0
for key, value in jogadores.items():
    if key != jogadoresEmOrdem[0][0] and key != jogadoresEmOrdem[1][0] and key != jogadoresEmOrdem[2][0]:
        if value > m:
            m =  value
            jogadoresEmOrdem[3] = [key, value]

dic2 = {
    jogadoresEmOrdem[0][0]:jogadoresEmOrdem[0][1],
    jogadoresEmOrdem[1][0]:jogadoresEmOrdem[1][1],
    jogadoresEmOrdem[2][0]:jogadoresEmOrdem[2][1],
    jogadoresEmOrdem[3][0]:jogadoresEmOrdem[3][1]
}

print('Jogadas por jogador: ')
for jogador, jogada in jogadores.items():
    print(f'{jogador} com {jogada}.')
    sleep(1)

print()
print('Ranking Jogadas: ')
for jogada in range(0,4):
    print(f'{jogada+1}º Lugar: {jogadoresEmOrdem[jogada][0]} com {jogadoresEmOrdem[jogada][1]}.')
    sleep(1)