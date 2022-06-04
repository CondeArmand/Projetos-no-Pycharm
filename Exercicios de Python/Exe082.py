lista = []
pares = []
impares = []
qtad = int(input('Quantos números deseja inserir? '))
for c in range(qtad):
    lista.append(int(input('Digite um número: ')))
    if lista[-1] % 2 == 0:
        pares.append(lista[-1])
    else:
       impares.append(lista[-1])
print(f'A lista completa é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')
