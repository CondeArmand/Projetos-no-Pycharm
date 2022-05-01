import random
from time import sleep
num = random.randrange(6)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
adv = int(input('Tente adivinhar o numero escolhido: '))
print('Processando...')
sleep(3)
if adv == num:
    print('Você acertou! Parabens!')
else:
    print('Você errou! Eu pensei no número {} e não no {}!'.format(num, adv))
