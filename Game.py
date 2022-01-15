# História já salva, creio que o python já pode ser apagado

# Rascunho_Jogo_
#FALAS TÊM 3 ESPAÇOS ANTES DO '-' E 4 SE NÃO O TIVER;
#HISTÓRIA TEM 1 ESPAÇO E SEMPRE EM CAPS;
#TÍTULOS E DIAS TÊM 3 ESPAÇOS;
#OPÇÕES TÊM 4 ESPAÇOS.

#import playsound
from time import sleep

def ret(a):
    sleep(a)
    print('\033[1;30m .', end='')
    sleep(a)
    print('.', end='')
    sleep(a)
    print('.\n')


def inicio_sem_musica():
    print('\033[1;30;107m BEM-VINDO! \033[1;0m'.center(130))
    nome = input('\033[1;30;107m QUAL O SEU NOME, JOGADOR? \033[1;0m\n         '.center(140))
    sleep(1)
    print(
        '\033[1;30;107m CUIDADO COM SUAS ESCOLHAS, {}, ELAS PODEM TE MATAR. \033[1;0m'.format(nome.upper()).center(130))
    sleep(1)
    v1 = input('\033[1;30;107m PRESSIONE ENTER PARA INICIAR E PARA VALIDAR SUAS ESCOLHAS. \033[1;0m \n'.center(132))
    if v1 != '"':
        print('\033[1;30;107m -=START=- \033[1;30;0m\n'.center(130))


# Tentativa de musica tema durante o menu
'''
def inicio_com_musica():
    winsound.PlaySound("game_inicio.wav", winsound.SND_FILENAME+winsound.SND_LOOP+winsound.SND_ASYNC+winsound.SND_NOSTOP)
    print('\033[1;30;107m BEM-VINDO! \033[1;0m'.center(130))
    nome = input('\033[1;30;107m QUAL O SEU NOME, JOGADOR? \033[1;0m\n         '.center(140))
    sleep(1)
    print(
        '\033[1;30;107m CUIDADO COM SUAS ESCOLHAS, {}, ELAS PODEM TE MATAR. \033[1;0m'.format(nome.upper()).center(130))
    sleep(1)
    v1 = input('\033[1;30;107m PRESSIONE ENTER PARA INICIAR E PARA VALIDAR SUAS ESCOLHAS. \033[1;0m \n'.center(132))
    if v1 != '"':
        print('\033[1;30;107m -=START=- \033[1;30;0m\n'.center(130))
    winsound.PlaySound('SystemExit', winsound.SND_PURGE)'''


inicio_sem_musica()

ret(1)

sleep(1)
print('   SEGUNDA-FEIRA, 4 DE JULHO - 7Hrs DA MANHÃ \n')
sleep(3)
print(' VOCÊ ESTÁ CORRENDO POR UMA ESPÉCIE DE COLINA.')
sleep(2)
print(' AS PESSOAS FICARAM ESTRANHAS, AGRESSIVAS. SEUS AMIGOS TENTARAM MATÁ-LO.')
sleep(2)
print(' VOCÊ NÃO ENTENDE O QUE ESTÁ ACONTECENDO. \n')
sleep(3.2)
print('\033[1;34m   -Ainda estão atrás de mim?')
sleep(2.2)
print('    Não vou parar para descobrir.')
sleep(2.2)
print('    Que merda será que aconteceu?', end='')
sleep(1.9)
print(' Por que estavam daquele jeito? ')
sleep(2.2)
print('    Meu Deus! Será que têm mais pessoas assim?')
sleep(2.2)
print('    Preciso chegar até a polícia. ') #Ou alguém que saiba de algo.
sleep(2)
print('    Espero que tenha uma estrada no fim dessa colina, ou algo assim... \n')
ret(2)
sleep(2)

print('\033[1;34m   -Que droga! O rio.\n')
sleep(3)


print('\033[1;30m VOCÊ ENCONTROU UM RIO.')
sleep(2)
print(' HÁ UM CAMINHO NA BEIRADA. ')
sleep(2)
print(' TEM UM BARCO PEQUENO NA MARGEM.')
sleep(2)
print(' HÁ UMA ESTRADA DO OUTRO LADO. NÃO PARECE DIFÍCIL DE ATRAVESSÁ-LO.')
sleep(2)
print('  ')
sleep(1)
escolha = int(input('    > 1. SEGUIR PELA MARGEM RIO ACIMA. \n    > 2. ATRAVESSAR O RIO COM O BARCO. \n    > 3. DESCER O RIO COM O BARCO. \n      '))
if escolha == 1:
    sleep(1.5)
    print('\033[1;34m   -Acho que vou seguir esse caminho rio acima. ')
    sleep(2)
    print('    Pode ser que eu ache alguém que possa ajudar. \033[1;30m')
    sleep(2)
    print('\n VOCÊ ESTÁ SEGUINDO PELA BEIRA DO RIO. ')
    print(' SUA CABEÇA DÓI. E O VENTO FRIO PARECE CORTAR A PELE.\n')
    sleep(2)
    print('   \033[1;34m-O que aconteceu com eles?')
    sleep(2)
    print('    E por que eu não fiquei daquele jeito também? ')
    sleep(2)
    print('    Alguma coisa acontecu e ocasionou isso... Mas o quê? ')
    ret(2)
    sleep(2)
    print('\033[1m   DOMINGO, 3 DE JULHO - 22Hrs NOITE (NOITE ANTERIOR) \n   SALÃO DO CHALÉ\n')
    sleep(3)
    print(
        '   TERRY: \033[1;32m-Olha cara: estão dizendo na TV que essa noite\n           \033[1mum meteoro vai passar bem perto da Terra! \n')
    sleep(5)
    print('\033[1;34m   -Foda! Espero que não o bastante para cair. Haha.')
    sleep(2.3)
    print('    Agora me ajuda aqui com essas malas, cara, daqui a pouco eu vou sair.\n')
    sleep(3)
    print('\033[1;30m   TERRY LEVANTA\n')
    sleep(1)
    print(
        '   TERRY: \033[1;32m-Já disse pra você viajar na terça, cara, a gente pode ir pescar amanhã. \n           Tem um rio aqui perto, dizem que é bom pra pescaria.')
    sleep(3)
    print('\033[1;34m\n   -Obrigado. Mas não. Eu preciso ir esta noite.')
    sleep(2)
    print('    Prometi a Ângela que encontraria ela amanhã.\n')
    sleep(2)
    print('   \033[1;30mTERRY: \033[1;32m-Ah cara, liga pra ela. Sei lá, pede mais um tempinho.')
    sleep(2)
    print('           Você veio de tão longe pra ficar só um fim de semana?')
    sleep(2)
    print('           E os outros vão ficar putos.')


elif escolha == 2:
    sleep(2)
    print('\n\033[1;34m   -Parece mais fácil atravessar o rio. ')
    sleep(2)
    print('    Vou tentar pegar o barco. \n')
    ret(1)
    print('\033[1m VOCÊ USOU O BARCO PARA ATRAVESSAR O RIO. ')
    sleep(2)
    print(' O CAMINHO PARECE SER USADO FREQUENTEMENTE, FÁCIL DE ANDAR.\n')
    ret(2)
    sleep(2)
    print('\033[1;34m   -Para onde devo ir? Onde será que tem alguém? ')
    sleep(2)
    print('    Que droga de lugar escolhemos para passar o feriado. Tudo deserto. ')
    sleep(2)
    print('    Tá bem, tenho que manter a calma. Tentar entender o que realmnte aconteceu... \n')
    ret(2)
    sleep(2)
    print('\033[1m   DOMINGO, 3 DE JULHO - 22Hrs NOITE (NOITE ANTERIOR) \n   SALÃO DO CHALÉ\n')
    sleep(3)
    print(
        '   TERRY: \033[1;32m-Olha cara: estão dizendo na TV que essa noite\n           \033[1mum meteoro vai passar bem perto da Terra! \n')
    sleep(5)
    print('\033[1;34m   -Foda! Espero que não o bastante para cair. Haha.')
    sleep(2.3)
    print('    Agora me ajuda aqui com essas malas, cara, daqui a pouco eu vou sair.\n')
    sleep(3)
    print('\033[1;30m   TERRY LEVANTA\n')
    sleep(1)
    print(
        '   TERRY: \033[1;32m-Já disse pra você viajar na terça, cara, a gente pode ir pescar amanhã. \n           Tem um rio aqui perto, dizem que é bom pra pescaria.')
    sleep(3)
    print('\033[1;34m\n   -Obrigado. Mas não. Eu preciso ir esta noite.')
    sleep(2)
    print('    Prometi a Ângela que encontraria ela amanhã.\n')
    sleep(2)
    print('   \033[1;30mTERRY: \033[1;32m-Ah cara, liga pra ela. Sei lá, pede mais um tempinho.')
    sleep(2)
    print('           Você veio de tão longe pra ficar só um fim de semana?')
    sleep(2)
    print('           E os outros vão ficar putos.')


elif escolha == 3:
    sleep(2)
    print('\033[1;34m\n   -Vamos lá, acho que vou pegar esse barco.')
    sleep(2)
    print('    Talvez rio abaixo possa haver alguém que saiba o que está acontecendo. \n')
    sleep(2.5)
    print('\033[1;30m VOCÊ ENTROU NO BARCO, NÃO PARECE TER FUROS NELE. HÁ UM REMO NO INTERIOR.')
    sleep(2.5)
    print(' VOCÊ NÃO TEM IDEIA DO QUE FAZER MAS PRECISA SAIR DAÍ.\n')
    ret(1)
    sleep(2)
    print(' VOOCÊ ESTÁ REMANDO HÁ ALGUNS MINUTOS. ')
    sleep(2.5)
    print(' A ÁGUA FRIA ESPIRRA DO RIO E DÁ CALAFRIOS.\n')
    sleep(2)
    print('\033[1;34m   -O que será que aconteceu com eles?')
    sleep(2)
    print('    Será que todos ficaram loucos? ')
    sleep(2)
    print('    Mas por que eu não fiquei daquele jeito? ')
    sleep(2)
    print('    Tenho que ficar calmo. Lembrar... o que aconteceu... \033[1;30m')
    ret(2)
    sleep(2)
    print('\033[1m   DOMINGO, 3 DE JULHO - 22Hrs NOITE (NOITE ANTERIOR) \n   SALÃO DO CHALÉ\n')
    sleep(3)
    print('   TERRY: \033[1;32m-Olha cara: estão dizendo na TV que essa noite\n           \033[1mum meteoro vai passar bem perto da Terra! \n')
    sleep(5)
    print('\033[1;34m   -Foda! Espero que não o bastante para cair. Haha.')
    sleep(2.3)
    print('    Agora me ajuda aqui com essas malas, cara, daqui a pouco eu vou sair.\n')
    sleep(3)
    print('\033[1;30m   TERRY LEVANTA\n')
    sleep(1)
    print('   TERRY: \033[1;32m-Já disse pra você viajar na terça, cara, a gente pode ir pescar amanhã. \n           Tem um rio aqui perto, dizem que é bom pra pescaria.')
    sleep(3)
    print('\033[1;34m\n   -Obrigado. Mas não. Eu preciso ir esta noite.')
    sleep(2)
    print('    Prometi a Ângela que encontraria ela amanhã.\n')
    sleep(2)
    print('   \033[1;30mTERRY: \033[1;32m-Ah cara, liga pra ela. Sei lá, pede mais um tempinho.')
    sleep(2)
    print('           Você veio de tão longe pra ficar só um fim de semana?')
    sleep(2)
    print('           E os outros vão ficar putos.')


'''LEMBRETES >> 
    -> O QUE ELE VÊ E FAZ ELE FUGIR (?) 
        -> ELE BRIGA COM OS AMIGOS (?) 
    -> ELE SÓ FOGE OU VAI BUSCAR AJUDA (?) 
'''

'''Caminho da história >>
    -> Primeiro ele foge/tenta entender o que está acontecendo
    -> Depois algo relacionado a ele ir atrás da namorada... 
'''
