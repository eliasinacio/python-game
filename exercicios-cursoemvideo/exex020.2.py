from random import shuffle
a1 = input(' Nome do Aluno: ')
a2 = input(' Nome do Aluno: ')
a3 = input(' Nome do Aluno: ')
a4 = input(' Nome do Aluno: ')
lista = [a1, a2, a3, a4]
shuffle(lista)
print(' A ordem de apresentação será \n {}'.format(lista))