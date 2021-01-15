import random
a = input(' Digite o nome de um aluno. ')
b = input(' Digite o nome de outro aluno. ')
c = input(' Digite o nome de mais um aluno. ')
d = input(' Digite o nome de outro aluno.')
nomes = [a, b, c, d]
e = random.sample(nomes, k=4)
print(' A ordem das apresentações será: {}'.format(e))
