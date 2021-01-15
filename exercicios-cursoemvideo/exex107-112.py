from moedas import *


valor = lerDinheiro("Digite um valor: R$ ")
#print()
#print(f"O dobro de R$ {format_valor(valor)} é: R$ {format_valor(dobro(valor, fmt=True))}.")
#print(f'O triplo de R$ {format_valor(valor)} é: R$ {format_valor(triplo(valor, True))}.')

taxa1 = lerDinheiro('Taxa de acréscimo: ')

#print(f'R$ {format_valor(valor)} com acréscimo de {taxa1}%: R$ {format_valor(acre(valor, taxa1, True))}')

taxa2 = lerDinheiro('Taxa de desconto: ')
#print(f'R$ {format_valor(valor)} com desconto de {taxa2}%: R$ {format_valor(decre(valor, taxa2, True))}')
#print()

resumo(valor, taxa1, taxa2)