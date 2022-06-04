from random import randint
from time import sleep
lista = []
jogos = list()
count = 0
print('-' * 30)
print('     JOGA NA MEGA SENA     ')
print('-' * 30)
qtda = int(input('Quantos jogos você quer que eu sorteie? '))
for c in range(qtda):
    count = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            count += 1
        if count >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
print('-=-' * 3, f'SORTEANDO {qtda} JOGOS', '-=-' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-=-' * 5, 'BOA SORTE', '-=-' * 5)
