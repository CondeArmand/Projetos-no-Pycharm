numeros = []
sn = 'S'
cont = 0
while sn == 'S':
    numeros.append(int(input('Digite um número: ')))
    sn = input('Quer continuar? [S/N] ').upper().strip()
    cont += 1
print(f'Você digitou {cont} números e a média foi {sum(numeros) / cont}')
print(f'O maior valor foi {max(numeros)} e o menor foi {min(numeros)}')
