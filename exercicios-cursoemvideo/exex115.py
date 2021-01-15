from registro import *

while True:
    registro()
    a = receber_opção()
    
    if a == 1:
        mostrar_cadastrados()
    
    elif a == 2:
        novo_cadastro()
    
    else:
        print('\n\n\033[1;32m     ENCERRANDO...')
        break