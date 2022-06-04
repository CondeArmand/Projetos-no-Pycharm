nums = []
for c in range(5):
    nums.append(int(input(f'Digite um valor para a posição {c}: ')))
print('=-=' * 40)
print(f'Você digitou os valores {nums}')
print(f'O maior valor digitado foi {max(nums)} nas posições ', end='')
for i, v in enumerate(nums):
    if v == max(nums):
        print(f'{i}... ', end='')
print()
print(f'O menor valor digitado foi {min(nums)} nas posições ', end='')
for i, v in enumerate(nums):
    if v == min(nums):
        print(f'{i}... ', end='')
