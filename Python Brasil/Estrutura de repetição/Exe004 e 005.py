x = 0
while x == 0:
    popA = float(input('Informe a população inicial A: '))
    taxaA = float(input('Informe a taxa de crescimento da população A: '))
    taxaA = taxaA / 100
    popB = float(input('Informe a população inicial B: '))
    taxaB = float(input('Informe a taxa de crescimento da população B: '))
    taxaB = taxaB / 100
    qtAnos = 0

    while popA < popB:
        popA = popA + taxaA * popA
        popB = popB + taxaB * popB
        qtAnos = qtAnos + 1

    print('Levou-se {} anos!'.format(qtAnos))
    print('popA = {:.2f} e popB = {:.2f}'.format(popA, popB))

    x = int(input('''Deseja repetir o processo?
[0] Sim
[1] Não
'''))