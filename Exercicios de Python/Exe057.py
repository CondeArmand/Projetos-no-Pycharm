sexo = input('Informe seu sexo: ').strip().upper()[0]
while sexo not in 'MmFf':
    sexo = input('Dado invalidos. Por favor, informe seu sexo: ').strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso.')
