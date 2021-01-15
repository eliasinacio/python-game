print(" Bom dia! ")
x = int(input(' Insira um valor qualquer. '))
y = int(input(' Insira outro valor. '))
z = int(input(" O que deseja fazer com esse valores? \n 1: Somá-los. \n 2: Subtraí-los. \n 3: Multiplicá-los. \n 4: Dividí-los. \n 5: Potenciá-los. \n 6: Radiciá-los. \n "))

if z == 1:
	k = x + y
	print(' A soma de', x, 'com', y, 'vale', k)

elif z == 2:
	k = x - y
	print(x, 'menos', y, 'vale', k)
	
elif z == 3:
	k = x * y
	print(' A multiplicação de', x, 'por', y, 'vale', k)
	
elif z == 4:
	k = x/y
	print(x, 'dividido para', y, 'vale', k)

elif z == 5:
	k = x ** y
	print(x, 'elevado a', y, 'vale ', k)
	
elif z == 6:
	k = x ** (1/y)
	print(' A',y,'° raiz de ', x, 'vale', k)