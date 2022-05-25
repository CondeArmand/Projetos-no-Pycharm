while True:
    print('-' * 40)
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 40)
    if n > 0:
        for c in range(10):
            print(f'{n} x {c + 1} = {n * (c + 1)}')
    else:
        break
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')