N = ""
while N != 'F' or 'M':
    N = input('QUAL O SEU SEXO: [F/M] ').upper()
    if N == 'F' or N == 'M':
        break
    else:
        print('NÃO ENTENDI.')
        continue
if N == 'M':
    print('OBRIGADO, SENHOR!')
if N == 'F':
    print('OBRIGADO, SENHORITA!')

'''EM UM WHILE break PARA; continue CONTINUA E pass NÃO FAZ NADA'''