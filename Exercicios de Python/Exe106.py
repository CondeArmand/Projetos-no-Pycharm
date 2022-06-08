from time import sleep
c = ('\033[m',
     '\033[0;31m')


def ajuda(com):
    título(f'Acessando o manual do comando /{com}/', 1)
    help(com)
    sleep(2)


def título(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


# Programa principal.
comando = ''
while True:
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('ATÉ LOGO!', 1)
