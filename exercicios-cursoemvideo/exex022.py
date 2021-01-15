nome = str(input(' Digite seu nome. ')).srip()
#O strip() vai retirar os espaços antes e depois
print('{}'.format(nome.upper()))
print('{}'.format(nome.lower()))
print('O nome todo, com espaços, tem {} letras. '.format(len(nome) - nome.count(' ')))
print('O primeiro nome tem {} letras. '.format(len(nome.split()[0])))
