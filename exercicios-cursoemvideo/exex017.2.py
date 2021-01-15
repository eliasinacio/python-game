from math import hypot

ca = float(input(' Informe o tamanho do cateto. '))
co = float(input(' Informe o tamanho do segundo cateto. '))
hip = hypot(ca, co)
print(' O tamanho da hipotenusa vale {}. '.format(hip))