times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico-PR', 'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza', 'Goiás', 'Bahia', 'Vasco', 'Atlético-MG', 'Fluminense', 'Botafogo', 'Ceará', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')

print('Times do Brasileirão 2019: ',end='')
for time in times:
    if time != times[-1]:
        print(time, end=' ')
    else:
        print(time)
print('-=-'*20)
print('Os 5 primeiros colocados são: ',end='')
for pos in range(0, 5):
    print(times[pos], end=' ')
print('\n','-=-'*20)
print(f'Os 4 últimos são: {times[-4:]}')
print('-=-'*20)
print('Times em ordem alfabética: ', sorted(times))
print('-=-'*20)
print(f'Chapecoense está em {times.index("Chapecoense")+1}º colocado. ')