# Head
from random import randint
from time import sleep
escolhas = {1: 'Pedra', 2: 'Tesoura', 3: 'Papel'}

# Main
print('=' * 30)
print(f'{"<< JOKENPO >>":^30}')
print('=' * 30)
while True:
    player = int(input('''Digite 1 para escolher Pedra;
Digite 2 para escolher Tesoura;
Digite 3 para escolher Papel;
-> '''))
    print('-=-' * 10)
    cpu = randint(1, 3)
    print('JO...')
    sleep(1)
    print('KEN...')
    sleep(1)
    print('PO!!!')
    print('-=-' * 10)
    if player == 1 and cpu == 2 or player == 2 and cpu == 3 or player == 3 and cpu == 1:
        print(f'\033[3;32mVocê escolheu {escolhas[player]} e o computador escolheu {escolhas[cpu]}. Você '
              f'VENCEU!\033[m')
    elif cpu == 1 and player == 2 or cpu == 2 and player == 3 or cpu == 3 and player == 1:
        print(f'\033[3;31mVocê escolheu {escolhas[player]} e o computador escolheu {escolhas[cpu]}. O computador '
              f'Venceu!\033[m')
    else:
        print(f'\033[3;33mVocê escolheu {escolhas[player]} e o computador escolheu {escolhas[cpu]}. Deu Empate!\033[m')
    print('-=-' * 10)
    continuar = input('Você deseja jogar novamente? [S/N] ').strip().upper()[0]
    print('_' * 30)
    if continuar == 'N':
        break

