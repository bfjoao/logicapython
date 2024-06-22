valor = float(input('Digite o valor do produto: R$'))
print('''OPÇÕES DE PAGAMENTO: 
[ 1 ] À VISTA DINHEIRO OU CHEQUE
[ 2 ] À VISTA NO CARTÃO
[ 3 ] EM ATÉ 2X NO CARTÃO
[ 4 ] EM 3X OU MAIS NO CARTÃO''')
forma = int(input('QUAL A FORMA DESEJADA? '))
if forma == 1:
    print(f'A forma desejada foi à vista no dinheiro e o valor do produto ficará R${valor - (valor * 10/100)}')
elif forma == 2:
    print(f'A forma desejada foi à vista no cartão e o valor do produto ficará R${valor - (valor * 5/100)}')
elif forma == 3:
    print(f'A forma desejada foi em até 2x no cartão e o valor do produto ficará R${valor}')
else:
    print(f'A forma desejada foi em 3x ou mais no cartão e o valor do produto ficará R${valor + (valor * 20/100)}')