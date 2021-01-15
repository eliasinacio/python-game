exp = input('Digite uma expressão: ')
lista = list()

for p in exp:
    if p == '(':
        lista.append('(')
    elif p == ')':
        if len(lista) != 0:
            lista.pop()
        else:
            break

if len(lista) != 0:
    print('Operação Inválida.')
else:
    print('Operação Válida')
