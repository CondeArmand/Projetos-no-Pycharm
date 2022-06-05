# Head
def titulo(txt):
    print(f'{txt:^20}')
    print(f'-' * 30)


def area(x, y):
    print(f'A área de um terreno {x:.1f}x{y:.1f} é de {x * y:.1f}m².')


# Main program
titulo("     Controle de Terrenos")
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
area(largura, comprimento)
