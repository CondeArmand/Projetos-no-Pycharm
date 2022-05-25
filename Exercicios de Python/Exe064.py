n = total = soma = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    if n < 999:
        soma += n
        total += 1
print(f'Você digitou {total} números e a soma entre eles foi {soma}.')
