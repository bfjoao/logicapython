from math import hypot
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
hipotenusa = hypot(co, ca)
print(f'A hipotenusa é {hipotenusa:.2f}')
