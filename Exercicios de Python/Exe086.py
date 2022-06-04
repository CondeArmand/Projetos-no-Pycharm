matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = pares = soma3column = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = par = int(input(f'Digite um valor para [{l}, {c}]: '))
        if par % 2 == 0:
            pares += par
print('-=-' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print(f'A soma dos valores pares é {pares}.')
soma3column = matriz[0][2] + matriz[1][2] + matriz[2][2]
print(f'A soma dos valores da terceira coluna é {soma3column}.')
print(f'O maior valor da segunda linha é {max(matriz[1])}.')
