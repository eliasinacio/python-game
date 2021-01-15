from random import choice
a = str(input(' Digite o nome do aluno. '))
b = str(input(' Digite o nome de outro aluno. '))
c = str(input(' Digite o nome do terceiro aluno. '))
d = str(input(' Digite o nome do último aluno. '))
als = [a, b, c, d]
print(' O aluno escolhido é {} '.format(choice(als)))