from math import factorial
n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    c -= 1
print(factorial(n))
