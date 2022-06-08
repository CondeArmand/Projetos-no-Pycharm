from random import choice
deck = {'paus': {'Ás': 1, 'cartas': (2, 3, 4, 5, 6, 7, 8, 9, 10), 'valete': 1, 'dama': 1, 'rei': 1},
        'copas': {'Ás': 1, 'cartas': (2, 3, 4, 5, 6, 7, 8, 9, 10), 'valete': 1, 'dama': 1, 'rei': 1},
        'ouro': {'Ás': 1, 'cartas': (2, 3, 4, 5, 6, 7, 8, 9, 10), 'valete': 1, 'dama': 1, 'rei': 1},
        'espadas': {'Ás': 1, 'cartas': (2, 3, 4, 5, 6, 7, 8, 9, 10), 'valete': 1, 'dama': 1, 'rei': 1}}
players = {'player1': str(input('Player 1, informe seu nome: ')), 'player2': str(input('Player 2, informe seu nome: '))}
cartas = list()
mão1 = cartas
mão2 = cartas

# Main program
while True:
    cartas = choice(choice(deck))
    if cartas not in players['player1']:
        if len(players['player1']) == 3:
            break
        players['player1'] = cartas

print(players['player1'])
