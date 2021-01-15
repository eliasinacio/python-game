LISTA = []
n1 = int(input('DIGITE UM NÚMERO: '))
n2 = int(input('DIGITE OUTRO NÚMERO: '))
R = ''

LISTA.append(n1)
LISTA.append(n2)
print(LISTA)

while R != ' ':
    INT = int(input('''\nO QUE DESEJA QUE EU FAÇA AGORA: 
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVO NÚMERO
[5] LIMPAR
[6] ENCERRAR\n>>> '''))

    if INT == 1:
        SOMA = 0
        LEN = len(LISTA)
        for a in range(0, LEN):
            SOMA += LISTA[a]
        print('\nA SOMA DOS NÚMEROS INFORMADOS EQUIVALE A:\n>>>', SOMA)

    elif INT == 2:
        MULT = 1
        for a in LISTA:
            MULT = MULT * a
        print('\nA MULTIPLICAÇÃO DOS NÚMEROS INFORMADOS EQUIVALE A:\n>>>', MULT)

    elif INT == 3:
        MAIOR = max(LISTA)
        print('DOS NÚMEROS INFORMADOS, O MAIOR É: ',MAIOR)

    elif INT == 4:
        n3 = int(input('DIGITE O NÚMERO: '))
        print(n3,'FOI ADICIONADO.')
        LISTA.append(n3)
        print(LISTA)
    elif INT == 5:
        LISTA = LISTA = []

    elif INT == 6:
        print('\nOK. ENCERRANDO...')
        break