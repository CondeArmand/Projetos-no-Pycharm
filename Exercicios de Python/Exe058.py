from random import randint
compute_random = randint(0, 10)
player = -1
tentativas = 1
print('''Sou seu computador...
Acabei de pensar em número entre 0 e 10.
Será que você consegue adivinhar qual foi?''')
while player != compute_random:
    player = int(input('Qual é seu palpite? '))
    if player < compute_random:
        print('Mais... Tente mais uma vez.')
        tentativas += 1
    elif player > compute_random:
        print('Menos... Tente mais uma vez.')
        tentativas += 1
print(f'Acertou com {tentativas} tentativas. Parabéns!')
