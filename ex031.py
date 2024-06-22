km = int(input('Qual a distância da sua viagem em km? '))
if km <= 200:
    print(f'Sua viagem vai custar {km * 0.50:.2f}')
else:
    print(f'Sua viagem vai custar {km * 0.45:.2f}')
