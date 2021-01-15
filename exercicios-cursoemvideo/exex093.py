g = 0
nome = str(input('Digite o nome do jogador: ')).capitalize()
qp = int(input(f'Quantas partidas {nome} jogou? '))
dic = {'nome': nome, 'golsPorPartida': []}

for i in range(0,qp):
    gols = int(input(f'Quantos gols {nome} fez na {i+1}ª partida? '))
    dic['golsPorPartida'].append(gols)
    g += gols

dic['golsTemporada'] = g
print('-=-'*12)
print(dic)
print('-=-'*12)
for key, value in dic.items():
    print(f'{key} -->>  {value}.')
print('-=-'*12)
for partida, value in enumerate(dic['golsPorPartida']):
    print(f'Na {partida+1}ª Partida {nome} fez {value} gol(s).')