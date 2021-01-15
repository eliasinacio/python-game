def leiaint(a):
    b = input(a)
    while True:
        if b == '':
            break
        try:
            int(b)
            return b
            break
        
        except:
            print(f'\033[1;31mErro! <{b}> não é inteiro. Digite um número inteiro válido.\033[0m')
            b = input(a)

def leiafloat(b):
    a = input(b)
    
    while True:
        if a == '':
            break
        if a.isnumeric() == True:
            print(f'\033[1;31mErro! <{a}> não é número de ponto flutuante. \nDigite um número inteiro válido.\033[0m')
            a = input(b)
            continue
        try:
            float(a)
            return a
            break
        
        except:
            try:
                a = a.replace(',', '.')
                float(a)
                return a
                break
            
            except:
                print(f'\033[1;31mErro! <{a}> não é número de ponto flutuante. \nDigite um número inteiro válido.\033[0m')
                a = input(b)
    

num = leiafloat('Digite um valor com ponto flutuante: ')
num2 = leiaint('Digite um valor inteiro: ')


if num != None:
    print(f'Voce digitou o número real: {num}')
else:
    print('Real não inserido.')

if num2 != None:
    print(f'Voce digitou o inteiro: {num2}')
else:
    print('Inteiro não inserido.')