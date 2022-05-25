from random import randint
count = 0
print('=-=' * 25)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-=' * 25)
while True:
    cpu = randint(0, 100)
    player = int(input('Diga um valor: '))
    pi_choice = input('Par ou ímpar? [P/I] ').strip().upper()[0]
    pi_result = ''
    print('-' * 20)
    print(f'Você jogou {player} e o computador jogou {cpu}. Total de {player + cpu} ', end='')
    print('Deu PAR'if (player + cpu) % 2 == 0 else 'Deu ÍMPAR')
    print('-' * 20)
    if (player + cpu) % 2 == 0:
        pi_result = 'P'
        if pi_choice == pi_result:
            print('Você VENCEU!')
            count += 1
        else:
            print(f'GAME OVER! Você ganhou {count} partidas.')
            break
    elif (player + cpu) % 2 == 1:
        pi_result = 'IiÍí'
        if pi_choice in pi_result:
            print('Você VENCEU!')
            count += 1
        else:
            print(f'GAME OVER! Você ganhou {count} partidas.')
            break
    print('Vamos jogar novamente...')