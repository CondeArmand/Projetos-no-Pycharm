on = 'Y'
while on == 'Y':
    base = int(input('Informe o valor da base: '))
    expoente = 0
    while expoente <=0:
        expoente = int(input('Informe o valor do expoente: '))
        if expoente <= 0:
            print('O expoente deve ser positivo!')
    potencia = 1
    for n in range(1, expoente + 1):
        potencia *= base
    print('\n{} elevado a {}º potencia = {}'.format(base, expoente, potencia))

    on = input('''\nDeseja repetir o processo?
[Y] Sim? Ou [N] Não?
''').upper()