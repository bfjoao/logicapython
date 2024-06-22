alt = float(input('Qual a altura da parede em metros? '))
lar = float(input('Qual a largura da parede em metros? '))
area = (alt*lar)
l = area / 2
print(f'A área de sua parede é de {area:.2f}m² e você vai precisar de {l:.1f} litros de tinta para pinta-la')
