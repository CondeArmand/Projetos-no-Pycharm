# Head
from random import randint
from time import sleep


def linha():
    print('==' * 20)


def escreva(txt):
    print('~' * (4 + (len(txt))))
    print(f'  {txt}')
    print('~' * (4 + (len(txt))))


acerto = 0
# Main program
escreva(''' JOGO DE ADIVINHAÇÃO''')
while True:
    while True:
        player = int(input('Chute um valor entre 1 a 6: '))
        if player > 6 or player < 1:
            print('ERRO, somente informe valores entre 1 a 6.')
        else:
            break
    dados = {'dado 1': randint(1, 6), 'dado 2': randint(1, 6), 'dado 3': randint(1, 6)}
    print('Jogando os dados...')
    sleep(1)
    linha()
    for v in dados.values():
        if player == v:
            acerto += 1
    for k, v in dados.items():
        print(f'O {k} deu [{v}]')
        sleep(0.7)
    print('--' * 20)
    if acerto == 0:
        print('Você não acertou nenhum número')
    else:
        print(f'Você acertou', 'uma vez!' if acerto == 1 else 'duas vezes!' if acerto == 2 else 'três vezes. '
                                                                                                'Sensacional!')
    linha()
    while True:
        continueSN = input('Deseja jogar novamente? [S/N] ').lower().strip()[0]
        if continueSN not in 'sn':
            print('ERRO, digite somente S ou N!')
        else:
            break
    if continueSN == 'n':
        print('Terminando...')
        sleep(1)
        print('<< OBRIGADO POR JOGAR! VOLTE SEMPRE!!! >>')
        break
    linha()
    acerto = 0
