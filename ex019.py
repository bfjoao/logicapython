from random import choice
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print(f'Entre os alunos {n1}, {n2}, {n3} e {n4} o escolhido para apagar o quadro foi o {escolhido}')

