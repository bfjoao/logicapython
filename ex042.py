r1 = int(input('Digite o valor da primeira reta: '))
r2 = int(input('Digite o valor da segunda reta: '))
r3= int(input('Digite o valor da terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM formar um triângulo')
    if r1 == r2 == r3:
        print('O triângulo formado será EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        print('O triângulo formado será ESCALENO!')
    else:
        print('O triângulo formado é ISÓSCELES')
else:
    print('Os segmentos acima NÃO podem formar um triângulo!')