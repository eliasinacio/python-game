def ficha(nome='', gols=''):
    """

nome= Nome do jogador; gols= Gols que o jogador fez.
    """
    if nome=='' and gols=='':
        print('Nenhum dado foi informado.')
    else: 
        nome = str(nome)
        if nome in '1234567890':
            gols = int(nome)
            nome = '<Desconhecido>'
        elif gols == '':
            gols = '<Não Informado>'
        
        print(f'Nome do jogador: {nome.capitalize()} \nNº de gols: {gols}')

print()
ficha(2)
print()
ficha('elias')
print()
ficha('elias', 5)
print()
ficha()