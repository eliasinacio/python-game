num = int(input(' DIGITE O VALOR A SER CONVERTIDO: '))
print(''' PARA QUAL DOS ITENS ABAIXO VOCÊ DESEJA CONVERTER: 
 1. OCTAL;
 2. BINÁRIO; 
 3. HEXADECIMAL;\n''')
escolha = int(input(' SUA ESCOLHA: \n'))
if escolha == 1:
    print(' {} convertido para OCTAL equivale a {}'.format(num, oct(num)[2:]))
elif escolha == 2:
    print(' {} convertido para BINÁRIO equivale a {}'.format(num, bin(num)[2:]))

elif escolha == 3:
    print(' {} convertido para HEXADECIMAL equivale a {}'.format(num, hex(num)[2:]))