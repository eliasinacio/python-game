from datetime import *
ano = datetime.today().year

menores = []
maiores = []

for i in range(0, 7):
    g = int(input(' DIGITE SEU ANO DE NASCIMENTO: '))
    dif = ano - g
    if dif >= 18:
        maiores.append(dif)
    else:
        menores.append(dif)

qM = len(maiores)
qm = len(menores)

print(' Das pessoas nascidas no anos citados, {} são menores.\n Elas têm as seguintes idades: {}'.format(qm, menores))
print(' Das pessoas nascidas no anos citados, {} são maiores.\n Elas têm as seguintes idades: {}'.format(qM, maiores))