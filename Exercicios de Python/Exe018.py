from math import sin, cos, tan, radians
a = float(input('Digite o ângulo desejado: '))
print('O ângulo de {} tem o SENO de {:.2f}'.format(a, sin(radians(a))))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(a, cos(radians(a))))
print('O ângulo de {} tem o TANGENTE de {:.2f}'.format(a, tan(radians(a))))
