p = float(input(' Informe o preço do produto. \n > '))
pc = float(input(' Digite a porcentagem de desconto. \n >'))
print(' Seu produto de R${} com {:.0f} % de desconto, vale agora R${:.2f}'.format(p, pc, ((100 - pc) /100) *p))