nums = [[], []]
qtd = int(input('Quantos valores deseja inserir? '))
for c in range(qtd):
    num = int(input(f'Digite o {c + 1}º valor: '))
    if num % 2 == 0:
        nums[0].append(num)
    else:
        nums[1].append(num)
print('-=-' * 30)
print(f'Os valores pares digitados foram: {sorted(nums[0])}')
print(f'Os valores impares digitados foram: {sorted(nums[1])}')
