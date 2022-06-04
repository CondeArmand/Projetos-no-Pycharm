listanums = []
qtad = int(input('Quantos números deseja? '))
for c in range(qtad):
    num = int(input('Digite um número: '))
    if num not in listanums:
        listanums.append(num)
print(f'Você digitou os valores {sorted(listanums)}')