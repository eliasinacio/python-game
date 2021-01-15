tupla = ('python', 'programaçao', 'sucesso', 'ano novo', 'linguagem', 'faculdade', 'trabalho', 'sonhos', 'amor')

for palavra in tupla:
    print(f'\nA palavra {palavra.upper()} tem as seguintes vogais: ', end='')
    for letra in palavra:
        if letra in 'aeiou':
            print(letra, end=' ')