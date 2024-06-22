velocidade = float(input('Qual a velocidade do carro ao passar o radar? Km/h '))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print(f'Você ultrapassou o limite de velocidade e foi multado! Sua multa será no valor de R${multa}')
else:
    print('Você está dentro do limite de velocidade!')

