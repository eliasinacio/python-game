def notas(*nt, sit=False):
    
    '''
    gerenciador de notas de alunos:
    nt= notas; sit= Situação, se deve ser mostrada ou não.
    nota máxima;
    nota mínima;
    média;
    situação.
    
    '''
    lst = list(nt)
    dic = dict()
    dic['Nº de Notas'] = len(lst)
    dic['Maior nota'] = max(lst)
    dic['Menor nota'] = min(lst)
    
    cont = 0
    for i in lst:
        cont += i
    media = cont/len(lst)
    dic['Média'] = f'{media:.2f}'
    
    if sit == True:
        if media >= 7:
            sit = 'Boa'
        elif media <7:
            sit = 'Ruim'
        dic['Situação'] = sit
    
    print(dic)
    
notas(2.5, 3.3, 4.8, 5.2, 6.9, 7.7, 9.8)
print()
notas(2, 6,5, 9, 7, sit=True)
print()
notas(5, 2, 7, 9, 0, 7, sit=False)
print()
notas( 8, 7, 4, 9, sit=True)