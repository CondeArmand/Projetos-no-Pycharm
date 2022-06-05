def linha():
    print('==' * 20)


def max_valor(*valores):
    linha()
    print('Analisando os valores passados...')
    for n in valores:
        print(f'{n} ', end='')
    print(f'Foram informados {len(valores)} valores ao todo.')
    print(f'O maior valor informado foi', f'{max(valores)}' if len(valores) > 0 else '0')
    linha()


max_valor(2, 9, 4, 5, 7, 1)
max_valor(4, 7, 0)
max_valor(1, 2)
max_valor(1)
max_valor()
