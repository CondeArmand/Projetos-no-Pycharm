from random import randint
from time import sleep


def sorteador():
    valores = list()
    for i in range(5):
        valores.append(randint(1, 10))
    print('Sorteando 5 valores da lista: ', end='')
    for n in valores:
        print(f'{n} ', end='')
        sleep(0.3)
    print('PRONTO!')
    return valores


def soma_pares(valores):
    soma = 0
    for n in valores:
        if n % 2 == 0:
            soma += n
    print(f'Somando os valores pares de {valores}, temos {soma}')


soma_pares(sorteador())
