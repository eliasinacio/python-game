from time import sleep
def registro():
    sleep(1.6)
    print('\033[1;34m')
    print('~=~'*20)
    print('\033[1;32m           >> REGISTRO <<\033[1;34m'.center(60))
    print('~=~'*20)
    print()
    print('\033[1;32m      [1]   Mostrar Cadastrados')
    print('      [2]   Novo Cadastro      ')
    print('      [3]   Encerrar           \033[1;34m')
    print()
    print('~=~'*20,end='')         


def receber_opção():
    while True: 
        try:
            valor = int(input('\n\033[1;32m      Opção: \033[1;34m'))
            
            if valor >3 or valor <1:
                print('~=~'*20)
                print('\033[1;31m      Valor inválido. Digite novamente. \033[1;34m')
                print('~=~'*20, end='')
                pass
            
            else: 
                print('\033[1;34m')
                print('~=~'*20,end='')
                return valor
                break
        
        except:
            print('~=~'*20)
            print('\033[1;31m      Valor inválido. Digite novamente. \033[1;34m')
            print('~=~'*20)
    sleep(1.8)
            
def mostrar_cadastrados():
    print('\n\033[1;32m      NOMES                                   IDADES')
    cadastros = open('cadastros.txt', 'r')
    for line in cadastros:
        loc_vir = line.find(',')
        print(f'      {line[:loc_vir]:<40} {line[(loc_vir+2):(loc_vir+5)]:>4}',end='')
    cadastros.close()
    print('\033[1;34m')
    print('~=~'*20,end='')
    
    
def novo_cadastro():
    nome = input('\033[1;32m      Nome: ').capitalize()
    if nome == '':
        nome = '<Não Informado>'
    while True:
        try:
            idade = int(input('\033[1;32m      Idade: '))
            
            cadastros = open('cadastros.txt', 'a')
            lista = [nome, str(idade)]
            cad = ', '.join(lista)
            cadastros.write(f'{cad}\n')            
            cadastros.close()
            print(f'\n\033[1;32m      Cadastro de {nome} realizado com sucesso! ')
            
            break
        
        except:
            print('\033[1;31m      Inválido. Digite novamente')
    print('\033[1;34m')
    print('~=~'*20,end='')
