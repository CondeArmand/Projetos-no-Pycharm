# Head
jogador = dict()
jogador['nome'] = str(input('Nome do jogador: '))
qtde = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
gols = list()
# Main 1
for c in range(qtde):
    gols.append(int(input(f'    Quantos gols na partida {c + 1}º? ')))
jogador['gols'] = gols[:]
jogador['total'] = sum(gols)
print('==' * 20)
print(jogador)
print('==' * 20)
# Main 2
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('==' * 20)
# Main 3
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for k, v in enumerate(gols):
    print(f'   -> Na partida {k + 1}, fez {v} gols')
print(f'Foi um total de {sum(gols)} gols')
