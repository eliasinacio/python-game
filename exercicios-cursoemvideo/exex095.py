jogadores = []
jogador = {'nome': '', 'partidasJogadas': '', 'golsPorPartida': ''}

print('>' * 5, 'Jogadores x Gols', '<' * 5)

while True:
    print('-=-' * 10)
    nome = str(input('Nome: ')).capitalize()
    if nome == '999':
        break
    partidas = int(input('Partidas jogadas: '))
    gols = []
    for partida in range(0, partidas):
        golsPorPartida = int(input(f'Gols na partida {partida + 1}: '))
        gols.append(golsPorPartida)

    jogador['nome'] = nome
    jogador['partidasJogadas'] = partidas
    jogador['golsPorPartida'] = gols

    jogadores.append(jogador.copy())

    jogador['nome'] = ''
    jogador['partidasJogadas'] = ''
    jogador['golsPorPartida'] = ''

print('-=-' * 19)
print('Num.      Jogador                Part.    Gols  ')
for num, jogador in enumerate(jogadores):
    print(f' {num + 1:<10}{jogador["nome"]:<23}{jogador["partidasJogadas"]:<8}{jogador["golsPorPartida"]}')

while True:
    print('-=-' * 19)
    print('Digite 999 para encerrar.')
    analise = int(input('Digite o número referente ao jogador para mais informações: '))
    if analise == 999:
        break
    if analise > len(jogadores):
        print('ERRO. Digite Novamente.')
        continue
    print('-=-' * 12)
    print(f'Jogador: {jogadores[analise -1]["nome"]}')
    print(f'Partidas jogadas: {jogadores[analise -1]["partidasJogadas"]}')
    print(f'Gols: {jogadores[analise -1]["golsPorPartida"]}')
    print('-=-' * 12)

print('<' * 5, 'ENCERRANDO', '>' * 5)
