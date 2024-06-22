salario = float(input('Digite o valor do seu salário: R$'))
if salario > 1250:
    print(f'Você recebeu um aumento e seu novo salário passará a ser: R${salario + (salario * 10/100)}')
else:
    print(f'Você recebeu um aumento e seu novo salário passará a ser: R${salario + (salario * 15/100)}')