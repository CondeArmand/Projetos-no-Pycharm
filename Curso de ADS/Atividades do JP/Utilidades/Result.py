def result(soma1, soma2, nome1, nome2):
    # resultados
    resultado1 = 21 - soma1
    resultado2 = 21 - soma2
    if resultado1 > 0 and resultado2 > 0:
        if resultado1 < resultado2:
            return f'{nome1} fez mais pontos'
        elif resultado2 < resultado1:
            return f'{nome2} fez mais pontos'
    elif resultado1 < 0 < resultado2:
        return f'{nome1} estourou e {nome2} fez mais pontos'
    elif resultado2 < 0 < resultado1:
        return f'{nome2} estourou e {nome1} fez mais pontos'


def winner(soma1, soma2, nome1, nome2):
    if soma1 == soma2:
        return 'Empate'
    if soma1 > soma2:
        return f'{nome1} ganhou e {nome2} perdeu'
    if soma2 > soma1:
        return f'{nome2} ganhou e {nome1} perdeu'
