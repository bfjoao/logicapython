num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] BINÁRIO
[ 2 ] OCTAL
[ 3 ] HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print(f'O numéro {num} convertido para binário é {bin(num)[2:]}')
elif opção == 2:
    print(f'O número {num} convertido para octal é {oct(num)[2:]}')
elif opção == 3:
    print(f'O número {num} convertido para hexadecimal é {hex(num)[2:]}')
else:
    print(f'Opção inválida! Tente novamente')