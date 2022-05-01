from math import hypot
y = float(input('Comprimento do cateto oposto: '))
x = float(input('Comprimento do cateto adjacente: '))
print('A hipotenusa vai medir {:.2f}'.format(hypot(x, y)))
