cores = ['\033[1;40m'
        '\033[1;41m', 
        '\033[1;42m', 
        '\033[1;43m', 
        '\033[1;44m', 
        '\033[1;45m', 
        '\033[1;46m']


def mostra(frase, cor=0):
    tam = len(frase) +4
    print(cores[cor], end='')
    print('~'*tam)
    print(f'  {frase}')
    print('~'*tam)
    print(cores[0])
    
    
def ajuda(pes):
    """
    Parecido com o <help>, porém, menos eficiente
    Funciona para funções, classes, métodos, etc...
    """
    print(cores[4])
    help(pes)
    print(cores[0])
         
    
while True:
    mostra('>>> AJUDA PYTHON <<<', cor=3)
    pes = input('\033[mPesquisa: ')
    if pes == 'não' or pes == 'NÃO' or pes in 'nN' or pes == 'exit':
        mostra('Encerrando...', cor=4)
        break
    ajuda(pes)
