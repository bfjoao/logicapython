maior = 0
menor = 0
for c in range(1 , 6):
    peso = float(input(f'Peso da {c}ª pessoa: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O MAIOR peso lido foi de {maior}Kg')
print(f'O MENOR peso lido foi {menor}Kg')