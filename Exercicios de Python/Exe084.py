temporary = []
main = []
maiorpeso = menorpeso = 0
sn = 's'
while sn == 's':
    temporary.append(str(input('Nome: ')))
    temporary.append(float(input('Peso: ')))
    if len(main) == 0:
        maiorpeso = menorpeso = temporary[1]
    else:
        if temporary[1] > maiorpeso:
            maiorpeso = temporary[1]
        if temporary[1] < menorpeso:
            menorpeso = temporary[1]
    main.append(temporary[:])
    temporary.clear()
    sn = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]
print('-=-' * 30)
print(f'Os dados foram {main}')
print(f'Ao todo você cadastrou {len(main)} pessoas.')
print(F'O maior peso foi de {maiorpeso}Kg. Peso de ', end='')
for p in main:
    if p[1] == maiorpeso:
        print(f'[{p[0]}]', end='')
print()
print(f'O menor peso foi de {menorpeso}Kg. Peso de ', end='')
for p in main:
    if p[1] == menorpeso:
        print(f'[{p[0]}]', end='')
