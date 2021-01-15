from time import sleep
def linha(tam):
    print('='*tam)

def contador(inicio, fim, passo):
    if passo == 0:
        if inicio < fim:
            passo = 1
        else:
            passo = -1
    if inicio > fim and passo > 0:
        passo = -passo
    else:
        fim +=1
    for num in range(inicio, fim, passo):
        print(f'{num}',end=' ')
        sleep(0.6)
    print()


linha(20)
contador(1,10,1)
linha(20)
contador(10,-1,-1)
linha(20)
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
print('Sua lista: ')
contador(inicio, fim, passo)