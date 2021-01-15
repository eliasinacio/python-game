preço = float(input(' DIGITE O VALOR DO PRODUTO: '))
compra = int(input('\n QUAL SERÁ O TIPO DA COMPRA? \n 1. À VISTA; (10% DESCONT0) \n 2. À VISTA - CARTÃO; (5% DESCONTO) \n 3. 2x NO CARTÃO; \n 4. 3x OU MAIS; (20% JUROS) '))

if compra == 1:
    Nvalor = (90/100) * preço
    print('\n VOCÊ TEM DIREITO A 10% DE DESCONTO.\n SUA COMPRA SAIRÁ NO VALOR DE R${:.2f}'.format(Nvalor))

elif compra == 2:
    Nvalor = (95/100) * preço
    print('\n VOCÊ GANHOU 5% DE DESCONTO.\n SUA COMPRA SAIRÁ NO VALOR DE R${}'.format(Nvalor))

elif compra == 3:
    print('\n VOCÊ NÃO TEM DIREITO AO DESCONTO.\n O VALOR A SER PAGO É 2x R${}'.format(preço/2))

elif compra == 4:
    Nvalor = (120/100) * preço
    print('\n SUA COMPRA TERÁ 20% DE JUROS.\n O VALOR A SER PAGO É DE R${} DIVIDIDO EM PRESTAÇÕES'.format(Nvalor))
