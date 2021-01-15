cardinal = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
extenso = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte']

num = input('DIGITE UM NÚMERO: ')

while True:
    while num.isnumeric() == False or int(num) not in cardinal:
        num = input('ERRO. DIGITE NOVAMENTE: ')

    print(f'VOCÊ DIGITOU O NÚMERO {extenso[int(num)].upper()}')
    break