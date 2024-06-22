nascimento = int(input('Digite seu ano de nascimento: '))
idade = 2023 - nascimento
if idade > 18:
    print(f'Já se passaram {idade - 18} anos do prazo do seu alistamento!')
elif idade < 18:
    print(f'Ainda faltam {18 - idade} anos para a data do seu alistamento!')
else:
    print(f'Você completou {idade} anos e está na hora de se alistar!')