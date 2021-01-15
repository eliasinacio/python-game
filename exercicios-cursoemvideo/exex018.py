from math import sin, cos, radians, tan

a = int(input(' Digite o valor do ângulo. '))
print(' o SENO de {} vale {:.2f}'.format(a, sin(radians(a))))
print(' O COSSENO de {} vale {:.2f}'.format(a, cos(radians(a))))
print(' A TANGENTE de {} vale {:.2f} '.format(a, tan(radians(a))))