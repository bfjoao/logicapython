from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Vamos jogar jokenpo, escolha uma opção:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Sua escolha: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-' * 12)
print(f'O jogador escolheu {itens[jogador]}')
print(f'O computador escolheu {itens[computador]}')
print('-' * 12)
if computador == 0:
    if jogador == 0:
        print('EMPATOU!')
    elif jogador == 1:
        print('VOCÊ GANHOU!')
    elif jogador == 2:
        print('O COMPUTADOR GANHOU!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1:
    if jogador == 0:
        print('O COMPUTADOR GANHOU!')
    elif jogador == 1:
        print('EMPATOU!')
    elif jogador == 2:
        print('VOCÊ GANHOU!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2:
    if jogador == 0:
        print('VOCÊ GANHOU!')
    elif jogador == 1:
        print('O COMPUTADOR GANHOU!')
    elif jogador == 2:
        print('EMPATOU!')
    else:
        print('JOGADA INVÁLIDA!')



