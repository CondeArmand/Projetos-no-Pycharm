from random import randrange
from random import randint
from time import sleep
itens = ('PEDRA', 'PAPEL', 'TESOURA')
cp = randint(0, 2)
num = randrange(3)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
adv = int(input('Qual a sua jogada? '))
if adv == 0 or adv == 1 or adv == 2:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')
    print('-=' * 18)
    print('O jogador jogou {}'.format(itens[adv]))
    print('O computador escolheu {}'.format(itens[cp]))
    print('-=' * 18)
    if adv == num:
        print('EMPATE!!!')
    elif adv == 0 and num == 2 or adv == 1 and num == 0 or adv == 2 and num == 1:
        print('O JOGADOR VENCEU!')
    elif num == 0 and adv == 2 or num == 1 and adv == 0 or num == 2 and adv == 1:
        print('A MAQUINA VENCEU!')
else:
    print('ERRO, INSIRA UMA OPÇÃO VALIDA')