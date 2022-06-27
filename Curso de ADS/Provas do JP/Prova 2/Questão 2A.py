from Functions import decimalPraBinario
print('<<< Conversor de Decimal para Binario >>>')
while True:
    try:
        num = int(input('Informe um valor decimal inteiro: '))
    except ValueError:
        print("Error! Informe um valor decimal inteiro valido!")
        continue
    else:
        break
print('==' * 20)
print(f'O número {num} em binario é {decimalPraBinario(num)}')
