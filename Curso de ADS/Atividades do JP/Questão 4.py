from Utilidades.Result import result
from random import choice
from Utilidades import create_deck, shuffle, linha
soma1 = soma2 = carta1 = carta2 = ganhou1 = ganhou2 = 0
player1 = dict()
player2 = dict()
player1_cards = list()
player2_cards = list()
deck = create_deck()
shuffle(deck)
player1['nome'] = str(input('Jogador 1, informe seu nome: '))
player2['nome'] = str(input('Jogador 2, informe seu nome: '))
for c in range(3):
    # Player 1
    player1_card = (choice(deck))
    player1_cards.append(player1_card)
    cartas1 = player1_card[0]

    if cartas1.isdigit():
        cartas1 = int(cartas1)
        soma1 += cartas1
    elif cartas1 in 'AQJK':
        carta1 = 1
        soma1 += carta1
    # Player 2
    player2_card = (choice(deck))
    player2_cards.append(player2_card)
    cartas2 = player2_card[0]

    if cartas2.isdigit():
        cartas2 = int(cartas2)
        soma2 += cartas2
    elif cartas2 in 'AQJK':
        cartas2 = 1
        soma2 += cartas2
player1['cartas'] = player1_cards
player2['cartas'] = player2_cards
resultado = result(soma1, soma2, {player1["nome"][:]}, {player2["nome"][:]})
linha()
print(f'As cartas do(a) {player1["nome"]} foram {player1["cartas"]}')
print(f'E as cartas do(a) {player2["nome"]} foram {player2["cartas"]}')
print(f'A(O) {player1["nome"]} fez {soma1} pontos')
print(f'A(O) {player2["nome"]} 2 fez {soma2} pontos')
linha()
resultado1 = 21 - soma1
resultado2 = 21 - soma2
if resultado1 > 0 and resultado2 > 0:
    if resultado1 < resultado2:
        print(f'{player1["nome"]} fez mais pontos')
        ganhou1 += 1
    elif resultado2 < resultado1:
        print(f'{player2["nome"]} fez mais pontos')
        ganhou2 += 1
    elif resultado1 < 0 < resultado2:
        print(f'{player1["nome"]} estourou')
        ganhou1 += 1
    elif resultado2 < 0 < resultado1:
        print(f'{player2["nome"]} estourou')
        ganhou2 += 1
    elif resultado1 == resultado2:
        print('Empate')
linha()
if ganhou1 > ganhou2:
    print(f'{player1["nome"]} ganhou')
elif ganhou2 > ganhou1:
    print(f'{player2["nome"]} ganhou')
elif soma1 == soma2:
    print(f'{player1["nome"]} e {player2["nome"]} empataram')
linha()
