pares = 0
impares = 0
for n in range(0, 10):
    num = int(input())
    if (num % 2) == 0:
        pares = pares + 1
    else:
        impares = impares + 1
print('''Quantidade de números pares: {}
Quantidade de números ímpares: {}'''.format(pares, impares))
