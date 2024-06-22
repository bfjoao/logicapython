peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura * altura)
if imc < 18.5:
    print(f'Seu imc é {imc:.1f} e você está ABAIXO do peso!')
elif imc >= 18.5 and imc <= 25:
    print(f'Seu imc é {imc:.1f} e você está com peso IDEAL!')
elif imc > 25 and imc <= 30:
    print(f'Seu imc é {imc:.1f} e você está com SOBREPESO!')
elif imc > 30 and imc <= 40:
    print(f'Seu imc é {imc:.1f} e você está com OBESIDADE!')
else:
    print(f'Seu imc é {imc:.1f} e vocÊ está com OBESIDADE MÓRBIDA')
