def escrever(string):
    tamanho = len(string)
    print('='*2+'='*tamanho+'='*2)
    print(string.center(tamanho+4))
    print('='*2+'='*tamanho+'='*2)


frase = str(input('Frase: '))
escrever(frase)