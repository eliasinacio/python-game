frase = input(' Digite uma frase qualquer. ')
print(' A frase possui {} letras a '.format(frase.lower().count('a')))
print(' A primeira letra a está na posição {}. '.format(frase.strip().lower().find('a')))
print(' A última letra a ocupa a posição {}.'.format(frase.strip().lower().rfind('a')))
