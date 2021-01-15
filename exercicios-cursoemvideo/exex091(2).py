from random import randint
from operator import itemgetter
jogadas = {
    'jogador1': randint(1,6),
    'jogador2': randint(1,6),
    'jogador3': randint(1,6),
    'jogador4': randint(1,6)
}

ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)
print(jogadas)
print(ranking)