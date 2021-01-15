'''
a + b < c
a + c < b
b + c < c
'''
r1 = int(input(' Digite o valor de uma reta: '))
r2 = int(input(' Digite um valor de outra reta: '))
r3 = int(input(' Digite o valor de outra reta: '))
if (r1 + r2) > r3 and (r1 + r3) > r2 and (r2 + r3) > r1:
    print(' Sim, um triângulo pode ser formado com essas retas. ')

else:
    print(' Essas retas não podem formar um triângulo. ')