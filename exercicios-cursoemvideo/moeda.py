def dobro(valor, fmt=False): 
    """
    Retorna o dobro do valor inserido como parâmetro.
    Se True, retorna formatado para reais.
    Senão, retorna em forma de <float>
    """
    if fmt==True:
        return f'{(valor*2):.2f}'  
    else:
        return valor*2

def triplo(valor, fmt=False):
    """
    Retorna o triplo do valor inserido como parâmetro.
    Se True, retorna formatado para reais.
    Senão, retorna em forma de <float>
    """
    if fmt==True:
        return f'{(valor*3):.2f}'  
    else:
        return valor*3

def acre(valor, taxa, fmt=False):
    """
    Retorna o valor inserido como parâmetro com acrécimo de <taxa>%.
    Se True, retorna formatado para reais.
    Senão, retorna em forma de <float>
    """
    if fmt==True:
        return f'{(((100+taxa)/100)*valor):.2f}'  
    else:
        return ((100+taxa)/100)*valor

def decre(valor, taxa, fmt=False):
    """
    Retorna o valor inserido como parâmetro com decrécimo de <taxa>%.
    Se True, retorna formatado para reais.
    Senão, retorna em forma de <float>
    """
    if fmt==True:
        return f'{(((100-taxa)/100)*valor):.2f}'  
    else:
        return ((100-taxa)/100)*valor

 
def format_valor(valor):                                  ###  Exercício 108
    """
    Formata para valor de reais:  0,00
    """
    valor = str(valor)
    valor = valor.replace('.', ',')
    return f'{valor}'

### Exercício 110
def resumo(valor, taxa1, taxa2): 
    print('-=-'*10)
    print("RESUMO".center(30))
    print('-=-'*10)
    
    print(f'Valor:              ', f'R$ {format_valor(valor)}')
    print(f'Dobro:              ', f'R$ {format_valor(dobro(valor, True))}')
    print(f'Triplo:             ', f'R$ {format_valor(triplo(valor, True))}')
    print(f'+{taxa1:4}%:             ', f'R$ {format_valor(acre(valor, taxa1, True))}')
    print(f'-{taxa2:4}%:             ', f'R$ {format_valor(decre(valor, taxa2, True))}')
    print('-=-'*10)
    

### Validar Diheiro                        ### Exercício 112
def lerDinheiro(num):
    while True:
        try:
            valor = input(num)
            valor = valor.replace(',', '.')
            valor = float(valor)
            return valor
            break
        except:
            print("\033[1;31mValor inválido\033[m")