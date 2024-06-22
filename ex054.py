maior = 0
menor = 0
for c in range (1, 8):
    nasc = int(input(f'Em que ano a {c}ª pessoa nasceu? '))
    idade = 2023 - nasc
    if idade > 18:
        maior += 1
    else:
        menor += 1
print(f'{maior} pessoas já são MAIORES de idade!')
print(f'{menor} pessoas ainda são MENORES de idade!')




