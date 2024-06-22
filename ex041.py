nasc = int(input('Digite sua data de nascimento: '))
idade = 2023 - nasc
if idade <= 9:
    print(f'Você tem {idade} anos e sua categoria é MIRIM!')
elif idade > 9 and idade <= 14:
    print(f'Você tem {idade} anos e sua categoria é INFANTIL!')
elif idade > 14 and idade <= 19:
    print(f'Você tem {idade} anos e sua categoria é JUNIOR!')
elif idade > 19 and idade <=20:
    print(f'Você tem {idade} anos e sua categoria é SÊNIOR!')
else:
    print(f'Você tem {idade} anos e sua categoria é MASTER!')