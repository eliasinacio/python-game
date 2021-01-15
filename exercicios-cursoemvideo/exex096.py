def area(l, a):
    return l * a

largura = float(input('Largura: '))
altura = float(input('Altura: '))
Area = area(largura, altura)

print(f'A área do polígono é: {Area:.1f} m².')
