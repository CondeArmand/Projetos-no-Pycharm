from random import randint
sorteador = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os números sorteados foram {sorteador}')
print(f'O maior número sorteado foi {max(sorteador)}')
print(f'O menor número sorteado foi {min(sorteador)}')
