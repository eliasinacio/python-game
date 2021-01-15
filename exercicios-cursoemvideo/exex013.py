s = float(input(' Informe o valor da quantia. \n >'))
tp = float(input(' Digite o valor da porcentagem. \n >'))
print(' Após a variação de {}% o valor será de R${:.2f}'.format(tp, (( 100 +tp)/100) *s))