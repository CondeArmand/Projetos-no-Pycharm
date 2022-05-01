pares = 0
for n in range(0, 5):
    num = int(input())
    if num % 2 == 0:
        pares = pares + 1
print('{} valores pares'.format(pares))
