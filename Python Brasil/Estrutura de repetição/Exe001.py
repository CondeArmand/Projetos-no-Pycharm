while True:
    nota = int(input('Informe sua nota: '))
    if 0 <= nota <= 10:
        print('Valor valido.')
        break
    else:
        print('Valor invalido, digite novamente.')

