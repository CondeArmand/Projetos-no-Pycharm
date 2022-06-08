import random
rota1 = rota2 = rota3 = falhas = 0
rotas = ('M1', 'M2', 'falha')
print('Processando...')
for o in range(10000000 + 1):
    origem = 1
    travel = random.choices(rotas, weights=(60, 30, 10), k=1)
    # rotas
    if travel[0] == 'M1':
        # Rota1
        rotas1_1 = ('M3', 'M4', 'falha')
        travel1_1 = random.choices(rotas1_1, weights=(50, 30, 20), k=1)

        if travel1_1[0] == 'M3':

            rotas1_2 = ('destino', 'falha')
            travel1_2 = random.choices(rotas1_2, weights=(90, 10), k=1)

            if travel1_2[0] == 'destino':
                rota1 += origem
            else:
                falhas += origem

        elif travel1_1[0] == 'M4':
            # Rota2
            rotas1_3 = ('destino', 'falha')
            travel1_3 = random.choices(rotas1_3, weights=(80, 20), k=1)

            if travel1_3[0] == 'destino':
                rota2 += origem
            else:
                falhas += origem

        else:
            falhas += 1
    elif travel[0] == 'M2':
        rotas2_2 = ('M5', 'falha')
        travel2_2 = random.choices(rotas2_2, weights=(95, 5), k=1)

        if travel2_2[0] == 'M5':
            rotas2_3 = ('destino', 'falha')
            travel2_3 = random.choices(rotas2_3, weights=(85, 15), k=1)

            if travel2_3[0] == 'destino':
                rota3 += origem
            else:
                falhas += origem

    else:
        falhas += origem

print(f'Estatisticas do envio de {o} pacotes:')
print(f'{rota1} pacotes chegaram pela Rota1;')
print(f'{rota2} pacotes chegaram pela Rota2;')
print(f'{rota3} pacotes chegaram pela Rota3;')
print(f'{falhas} pacotes se perderam (Falharam).')
