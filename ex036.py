casa = float(input('Qual o valor da casa que deseja comprar? R$'))
salario = float(input('Qual o valor do seu salário? R$'))
anos = int(input('Em quantos anos deseja pagar a casa? '))
prestação = casa / (anos * 12)
print(f'Para pagar uma casa de {casa:.2f} em {anos} a prestação será de {prestação:.2f}')
minimo = (salario * 30) / 100
if prestação <= minimo:
    print('Seu empréstimo foi CONCEDIDO!')
else:
    print('Seu empréstimo foi NEGADO pois o valor da parcela é maior que 30% do seu salário!')
