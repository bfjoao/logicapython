n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
if n1 > n2:
    print(f'O primeiro valor é MAIOR!')
elif n2 > n1:
    print(f'O segundo valor é MAIOR!')
else:
    print('Não existe valor maior, os dois números são IGUAIS!')