nome = str(input('Digite seu nome: ')).strip()
separa = nome.split()
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
print(f'Seu nome tem ao todo {len(nome) - nome.count(" ")} letras')
print(f'Seu primeiro nome é {separa[0]} e ele tem {len(separa[0])} letras')


