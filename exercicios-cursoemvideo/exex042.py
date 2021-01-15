R1 = float(input(' DIGITE O TAMANHO DA PRIMEIRA RETA: '))
R2 = float(input(' DIGITE O TAMANHO DA SEGUNDA RETA: '))
R3 = float(input(' DIGITE O TAMANHO DA ÚLTIMA RETA: '))

if (R1 + R2) > R3 and (R2 + R3) > R1 and (R1 + R3) > R2:
    print(' AS RETAS PODEM FORMAR UM TRIÂNGULO. ')
    if R1 == R2 == R3:
        print(' ELE SERÁ EQUILÁTERO. ')
    elif R1 == R2 and R1 != R3:
        print(' ELE SERÁ ISÓSCELES. ')
    elif R1 != R2 and R2 != R3 and R1 != R3:
        print(' ELE SERÁ ESCALENO. ')
    elif R2 == R3 and R1 != R2:
        print(' ELE SERÁ ISÓSCELES. ')
    elif R1 == R3 and R2 != R3:
        print(' ELE SERÁ ISÓSCELES. ')

else:
    print(' AS RETAS NÃO PODEM FORMAR UM TRIÂNGULO')