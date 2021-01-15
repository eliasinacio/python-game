from math import pow, sqrt, ceil
b = int(input(' Digite a medida do cateto: '))
c = int(input(' Digite a medida do outro cateto: '))
a = sqrt(pow(b,2) + pow(c,2))
print(' A hipotenusa vale {}. '.format(ceil(a)))
