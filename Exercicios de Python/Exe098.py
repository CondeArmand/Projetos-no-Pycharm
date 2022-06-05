from time import sleep


def linha():
    print('==' * 20)


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    linha()
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(1)

    if i < f:
        for n in range(i, f + 1, p):
            print(f'{n} ', end='')
            sleep(0.3)
        print('FIM!')
    else:
        for n in range(i, f - 1, p * -1):
            print(f'{n} ', end='')
            sleep(0.3)
        print('FIM!')


# Main program
contador(1, 10, 1)
contador(10, 0, 2)
linha()
print('Agora é a sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)
