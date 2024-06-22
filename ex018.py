from math import cos, sin, tan, radians
n = float(input('Digite o ângulo: '))
cosseno = cos(radians(n))
seno = sin(radians(n))
tangente = tan(radians(n))
print(f'O ângulo de {n} tem o COSSENO de {cosseno:.2f}')
print(f'O ângulo de {n} tem o SENO de {seno:.2f}')
print(f'O ângulo de {n} tem a TANGENTE de {tangente:.2f}')
