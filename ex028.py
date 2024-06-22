from random import randint
print('Hmmm pensando em um número entre 0 e 5...')
num = int(input('Tente adivinhar o número: '))
computador = randint(0, 5)
if num == computador:
    print('Parabéns você adivinhou o número!')
else:
    print(f'Que pena! Eu pensei no número {computador} você errou!')
print('----FIM----')